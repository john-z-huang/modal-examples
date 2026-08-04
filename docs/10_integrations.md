# 10：外部集成

将 Modal 与数据仓库、对象存储、监控、MCP、VPN 和应用框架结合。

返回 [案例总览](README.md)。

## `10_integrations/algolia_indexer.py`

- **作用**：运行文档爬虫并向 Algolia DocSearch 建立索引。
- **源码原题**：Algolia docsearch crawler
- **源码**：[打开 `10_integrations/algolia_indexer.py`](../10_integrations/algolia_indexer.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`modal.Stub`、`@app.function`、`@app.local_entrypoint`、`@modal.fastapi_endpoint`
- **常用启动方式**：`modal run 10_integrations/algolia_indexer.py`

## `10_integrations/cron_datasette.py`

- **作用**：定期构建数据并通过 Datasette 发布可探索的 SQLite 数据集。
- **源码原题**：Publish interactive datasets with Datasette
- **源码**：[打开 `10_integrations/cron_datasette.py`](../10_integrations/cron_datasette.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Period`、`modal.Volume`、`@app.function`、`@app.local_entrypoint`、`@modal.asgi_app`、`@modal.concurrent`
- **常用启动方式**：`modal run 10_integrations/cron_datasette.py`

## `10_integrations/dbt/dbt_duckdb.py`

- **作用**：用 Modal、DuckDB 与 dbt 构建可运行的数据仓库工作流。
- **源码原题**：Build your own data warehouse with DuckDB, DBT, and Modal
- **源码**：[打开 `10_integrations/dbt/dbt_duckdb.py`](../10_integrations/dbt/dbt_duckdb.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Period`、`modal.Secret`、`modal.Volume`、`@app.function`、`@app.local_entrypoint`、`@modal.asgi_app`、`@modal.concurrent`
- **常用启动方式**：`modal run 10_integrations/dbt/dbt_duckdb.py`

## `10_integrations/mcp_server_stateless.py`

- **作用**：用 FastMCP 在 Modal 上部署无状态的远程 MCP Server。
- **源码原题**：Deploy a remote, stateless MCP server on Modal with FastMCP
- **源码**：[打开 `10_integrations/mcp_server_stateless.py`](../10_integrations/mcp_server_stateless.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.function`、`@modal.asgi_app`
- **常用启动方式**：`modal run 10_integrations/mcp_server_stateless.py`

## `10_integrations/multion_news_agent.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：MultiOn: Twitter News Agent
- **源码**：[打开 `10_integrations/multion_news_agent.py`](../10_integrations/multion_news_agent.py)
- **关键对象**：`modal.App`、`modal.Cron`、`modal.Image`、`modal.Secret`、`@app.function`
- **常用启动方式**：`modal run 10_integrations/multion_news_agent.py`

## `10_integrations/pushgateway.py`

- **作用**：在 Function 中向 Prometheus Pushgateway 推送自定义指标。
- **源码原题**：Publish custom metrics with Prometheus Pushgateway
- **源码**：[打开 `10_integrations/pushgateway.py`](../10_integrations/pushgateway.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.cls`、`@modal.enter`、`@modal.exit`、`@modal.fastapi_endpoint`、`@modal.web_server`
- **常用启动方式**：`modal serve 10_integrations/pushgateway.py`

## `10_integrations/s3_bucket_mount.py`

- **作用**：将 S3 存储桶挂载到容器，用 DuckDB 分析 Parquet 出租车数据。
- **源码原题**：Analyze NYC yellow taxi data with DuckDB on Parquet files from S3
- **源码**：[打开 `10_integrations/s3_bucket_mount.py`](../10_integrations/s3_bucket_mount.py)
- **关键对象**：`modal.App`、`modal.CloudBucketMount`、`modal.Image`、`modal.Secret`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 10_integrations/s3_bucket_mount.py`

## `10_integrations/streamlit/serve_streamlit.py`

- **作用**：打包并以 Web 服务方式部署 Streamlit 应用。
- **源码原题**：Run and share Streamlit apps
- **源码**：[打开 `10_integrations/streamlit/serve_streamlit.py`](../10_integrations/streamlit/serve_streamlit.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.function`、`@modal.concurrent`、`@modal.web_server`
- **常用启动方式**：`modal serve 10_integrations/streamlit/serve_streamlit.py`

## `10_integrations/tailscale/modal_tailscale.py`

- **作用**：将 Modal App 接入 Tailscale 私有网络。
- **源码原题**：Add Modal Apps to Tailscale
- **源码**：[打开 `10_integrations/tailscale/modal_tailscale.py`](../10_integrations/tailscale/modal_tailscale.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`@app.function`
- **常用启动方式**：`modal run 10_integrations/tailscale/modal_tailscale.py`

## `10_integrations/webscraper.py`

- **作用**：把普通网页抓取函数作为最小 Modal App 运行。
- **源码原题**：A simple web scraper
- **源码**：[打开 `10_integrations/webscraper.py`](../10_integrations/webscraper.py)
- **关键对象**：`modal.App`、`modal.Function`、`modal.Image`、`modal.Period`、`modal.Secret`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 10_integrations/webscraper.py`

## `10_integrations/webscraper_old.py`

- **作用**：保留旧版网页抓取实现，便于对照 API 与写法演进。
- **源码原题**：Web Scraping on Modal
- **源码**：[打开 `10_integrations/webscraper_old.py`](../10_integrations/webscraper_old.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Period`、`modal.Secret`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 10_integrations/webscraper_old.py`
