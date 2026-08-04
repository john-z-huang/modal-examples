# 04：密钥与凭据

说明如何通过 Modal Secret 安全连接外部服务。

返回 [案例总览](README.md)。

## `04_secrets/db_to_sheet.py`

- **作用**：从 PostgreSQL 读取数据、调用天气 API，并把日报写入 Google Sheets。
- **源码原题**：Write to Google Sheets from Postgres
- **源码**：[打开 `04_secrets/db_to_sheet.py`](../04_secrets/db_to_sheet.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Period`、`modal.Secret`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 04_secrets/db_to_sheet.py`
