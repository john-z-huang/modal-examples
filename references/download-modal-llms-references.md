# 下载 Modal LLM 参考资料

`scripts/download_modal_llms_references.py` 从 Modal 官方的
[`llms.txt`](https://modal.com/llms.txt) 提取 `modal.com/docs` 下列出的 `.md`
链接，并保存原始 Markdown 正文和 `llms.txt` 索引本身。它不抓取索引中的 HTML
导航页或站外链接。

默认输出目录是 `references/modal-llms/`。下载后的目录结构保留 URL 路径，例如
`https://modal.com/docs/guide/images.md` 对应
`references/modal-llms/docs/guide/images.md`；索引保存为
`references/modal-llms/llms.txt`。同目录的 `manifest.json` 记录索引及每个文档的
源 URL、相对路径和 SHA-256 校验和。

为避免将文档中意外出现的 Docker Personal Access Token 格式字符串提交到 GitHub，
脚本会将其替换为 `<REDACTED_DOCKER_PAT>`；其他内容按原始 Markdown 保存。

运行：

```bash
uv run python scripts/download_modal_llms_references.py
```

先查看将要下载的文件而不写入磁盘：

```bash
uv run python scripts/download_modal_llms_references.py --dry-run
```

可用 `--output-dir` 指定其他目标目录，使用 `--workers` 调整并发下载数。任何文档
下载失败时，脚本不会写入本轮下载的 Markdown 或清单，以免留下不完整快照；成功时
会以临时文件替换方式写入每个文件。

退出码：成功（包括 `--dry-run`）为 0；参数无效或至少一个下载失败为非零。
