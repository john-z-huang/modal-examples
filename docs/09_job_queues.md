# 09：任务队列

组合 Dict、Queue、轮询和 Web 界面来处理异步后台作业。

返回 [案例总览](README.md)。

## `09_job_queues/dicts_and_queues.py`

- **作用**：组合持久化 Dict 与 Queue 管理生产者、消费者和任务状态。
- **源码原题**：Use Modal Dicts and Queues together
- **源码**：[打开 `09_job_queues/dicts_and_queues.py`](../09_job_queues/dicts_and_queues.py)
- **关键对象**：`modal.App`、`modal.Dict`、`modal.Function`、`modal.Image`、`modal.Queue`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 09_job_queues/dicts_and_queues.py`

## `09_job_queues/doc_ocr_jobs.py`

- **作用**：把文档 OCR 解析拆分为可扩展的后台队列任务。
- **源码原题**：Run a job queue that turns documents into structured data with Datalab Marker
- **源码**：[打开 `09_job_queues/doc_ocr_jobs.py`](../09_job_queues/doc_ocr_jobs.py)
- **关键对象**：`modal.App`、`modal.Function`、`modal.Image`、`modal.Volume`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 09_job_queues/doc_ocr_jobs.py`

## `09_job_queues/doc_ocr_webapp.py`

- **作用**：部署一个上传票据并异步展示 OCR 结果的 Web 应用。
- **源码原题**：Serve a receipt parsing web app
- **源码**：[打开 `09_job_queues/doc_ocr_webapp.py`](../09_job_queues/doc_ocr_webapp.py)
- **关键对象**：`modal.App`、`modal.Function`、`modal.FunctionCall`、`modal.Image`、`@app.function`、`@modal.asgi_app`、`@modal.concurrent`
- **常用启动方式**：`modal serve 09_job_queues/doc_ocr_webapp.py`

## `09_job_queues/web_job_queue_wrapper.py`

- **作用**：为后台队列增加 HTTP 提交、状态查询和结果读取接口。
- **源码原题**：Create a web wrapper for job queue, submission, polling, & results
- **源码**：[打开 `09_job_queues/web_job_queue_wrapper.py`](../09_job_queues/web_job_queue_wrapper.py)
- **关键对象**：`modal.App`、`modal.Function`、`modal.FunctionCall`、`modal.Image`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.asgi_app`、`@modal.concurrent`、`@modal.enter`
- **常用启动方式**：`modal run 09_job_queues/web_job_queue_wrapper.py`
