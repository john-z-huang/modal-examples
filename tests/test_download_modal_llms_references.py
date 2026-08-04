"""Tests for the Modal LLM-reference downloader."""

import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parents[1] / "scripts" / "download_modal_llms_references.py"
SPEC = importlib.util.spec_from_file_location("reference_downloader", SCRIPT)
assert SPEC and SPEC.loader
downloader = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(downloader)


class MarkdownUrlsTest(unittest.TestCase):
    def test_keeps_unique_first_party_markdown_links(self) -> None:
        index = """
- [Guide](https://modal.com/docs/guide)
- [Images](https://modal.com/docs/guide/images.md)
- [Duplicate](https://modal.com/docs/guide/images.md)
- [External](https://example.com/docs/page.md)
"""

        self.assertEqual(
            downloader.markdown_urls(index),
            ["https://modal.com/docs/guide/images.md"],
        )

    def test_preserves_documentation_path_below_output_directory(self) -> None:
        self.assertEqual(
            downloader.destination_for(
                "https://modal.com/docs/sdk/py/latest/App.md", Path("references/modal-llms")
            ),
            Path("references/modal-llms/docs/sdk/py/latest/App.md"),
        )

    def test_rejects_path_traversal(self) -> None:
        with self.assertRaises(ValueError):
            downloader.destination_for(
                "https://modal.com/docs/%2E%2E/private.md", Path("references/modal-llms")
            )

    def test_redacts_docker_pat_shaped_strings(self) -> None:
        self.assertEqual(
            downloader.redact_document(b"token=dckr_pat_example-token"),
            b"token=<REDACTED_DOCKER_PAT>",
        )


if __name__ == "__main__":
    unittest.main()
