#!/usr/bin/env python3
"""Download Markdown documents listed in Modal's llms.txt index.

Only first-party ``https://modal.com/docs/.../*.md`` links are downloaded.
The original URL path is retained below the output directory so that the
resulting files are stable and easy to map back to their source.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import re
import sys
import time
from pathlib import Path
from typing import NamedTuple
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen

DEFAULT_INDEX_URL = "https://modal.com/llms.txt"
DEFAULT_OUTPUT_DIR = Path("references/modal-llms")
MARKDOWN_LINK = re.compile(r"\[[^]]+\]\((https://modal\.com/docs/[^)]+\.md)\)")
DOCKER_PERSONAL_ACCESS_TOKEN = re.compile(br"\bdckr_pat_[A-Za-z0-9_-]+\b")
USER_AGENT = "modal-examples-reference-downloader/1.0"


class DownloadResult(NamedTuple):
    url: str
    path: Path
    content: bytes
    sha256: str


def fetch(url: str, timeout: float, retries: int) -> bytes:
    """Fetch *url*, retrying transient network and server errors."""
    request = Request(url, headers={"User-Agent": USER_AGENT})
    last_error: OSError | None = None

    for attempt in range(retries + 1):
        try:
            with urlopen(request, timeout=timeout) as response:
                return response.read()
        except HTTPError as error:
            last_error = error
            if error.code < 500:
                break
        except URLError as error:
            last_error = error

        if attempt < retries:
            time.sleep(2**attempt)

    raise RuntimeError(f"Unable to download {url}: {last_error}")


def markdown_urls(index: str) -> list[str]:
    """Return unique first-party Markdown document URLs in index order."""
    return list(dict.fromkeys(MARKDOWN_LINK.findall(index)))


def redact_document(content: bytes) -> bytes:
    """Remove Docker PAT-shaped strings so snapshots pass secret scanning."""
    return DOCKER_PERSONAL_ACCESS_TOKEN.sub(b"<REDACTED_DOCKER_PAT>", content)


def destination_for(url: str, output_dir: Path) -> Path:
    """Map a Modal documentation URL to a safe path below *output_dir*."""
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.netloc != "modal.com":
        raise ValueError(f"Unexpected documentation host: {url}")

    relative_path = Path(unquote(parsed.path).lstrip("/"))
    if relative_path.suffix != ".md" or ".." in relative_path.parts:
        raise ValueError(f"Unexpected Markdown path: {url}")
    return output_dir / relative_path


def download_one(url: str, output_dir: Path, timeout: float, retries: int) -> DownloadResult:
    content = redact_document(fetch(url, timeout, retries))
    return DownloadResult(
        url=url,
        path=destination_for(url, output_dir),
        content=content,
        sha256=hashlib.sha256(content).hexdigest(),
    )


def write_result(result: DownloadResult) -> None:
    result.path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = result.path.with_suffix(result.path.suffix + ".tmp")
    temporary_path.write_bytes(result.content)
    temporary_path.replace(result.path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index-url", default=DEFAULT_INDEX_URL)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.workers < 1 or args.timeout <= 0 or args.retries < 0:
        raise SystemExit("--workers and --timeout must be positive; --retries cannot be negative")

    index = fetch(args.index_url, args.timeout, args.retries).decode("utf-8")
    urls = markdown_urls(index)
    if not urls:
        raise RuntimeError(f"No Markdown URLs found in {args.index_url}")

    if args.dry_run:
        print(f"Found {len(urls)} linked Markdown documents plus the llms.txt index.")
        print(args.output_dir / "llms.txt")
        for url in urls:
            print(destination_for(url, args.output_dir))
        return 0

    results: list[DownloadResult] = []
    failures: list[str] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(download_one, url, args.output_dir, args.timeout, args.retries): url
            for url in urls
        }
        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            try:
                results.append(future.result())
            except (OSError, RuntimeError, ValueError) as error:
                failures.append(f"{url}: {error}")

    if failures:
        print("No files were written because one or more downloads failed:", file=sys.stderr)
        print("\n".join(failures), file=sys.stderr)
        return 1

    for result in sorted(results, key=lambda item: item.url):
        write_result(result)

    index_path = args.output_dir / "llms.txt"
    index_path.write_text(index, encoding="utf-8")
    manifest = {
        "index_url": args.index_url,
        "index_path": index_path.relative_to(args.output_dir).as_posix(),
        "index_sha256": hashlib.sha256(index.encode("utf-8")).hexdigest(),
        "documents": [
            {
                "url": result.url,
                "path": result.path.relative_to(args.output_dir).as_posix(),
                "sha256": result.sha256,
            }
            for result in sorted(results, key=lambda item: item.url)
        ],
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Downloaded {len(results)} Markdown documents to {args.output_dir}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
