# 杂项案例

收录尚未归入编号章节的实验性或专项案例。

返回 [案例总览](README.md)。

## `misc/batch_inference/batch_inference_using_huggingface.py`

- **作用**：使用 Hugging Face 模型进行批量远程推理。
- **源码原题**：Batch inference using a model from Huggingface
- **源码**：[打开 `misc/batch_inference/batch_inference_using_huggingface.py`](../misc/batch_inference/batch_inference_using_huggingface.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.enter`、`@modal.method`
- **常用启动方式**：`modal run misc/batch_inference/batch_inference_using_huggingface.py`

## `misc/chronos_forecasting.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：chronos forecasting
- **源码**：[打开 `misc/chronos_forecasting.py`](../misc/chronos_forecasting.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.cls`、`@app.local_entrypoint`、`@modal.enter`、`@modal.method`
- **常用启动方式**：`modal run misc/chronos_forecasting.py`

## `misc/hello_shebang.py`

- **作用**：演示把 Modal 脚本作为可执行文件直接启动的 shebang 写法。
- **源码原题**：Syntax for making modal scripts executable
- **源码**：[打开 `misc/hello_shebang.py`](../misc/hello_shebang.py)
- **关键对象**：`modal.App`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run misc/hello_shebang.py`

## `misc/isaac_lab_rl.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：isaac lab rl
- **源码**：[打开 `misc/isaac_lab_rl.py`](../misc/isaac_lab_rl.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run misc/isaac_lab_rl.py`

## `misc/kafka_microbatch_etl.py`

- **作用**：将 Kafka 消息按有界微批次执行 ETL。
- **源码原题**：Kafka micro-batch ETL (bounded)
- **源码**：[打开 `misc/kafka_microbatch_etl.py`](../misc/kafka_microbatch_etl.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run misc/kafka_microbatch_etl.py`

## `misc/parseable_otel.py`

- **作用**：把 Modal 遥测数据通过 OpenTelemetry 导出到 Parseable。
- **源码原题**：Export Modal telemetry to Parseable with OpenTelemetry
- **源码**：[打开 `misc/parseable_otel.py`](../misc/parseable_otel.py)
- **关键对象**：`modal.App`、`modal.Cls`、`modal.Image`、`modal.Secret`、`@app.cls`、`@app.local_entrypoint`、`@modal.enter`、`@modal.exit`、`@modal.method`
- **常用启动方式**：`modal run misc/parseable_otel.py`

## `misc/quic/quic_yolo_modal.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：quic yolo modal
- **源码**：[打开 `misc/quic/quic_yolo_modal.py`](../misc/quic/quic_yolo_modal.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.cls`、`@app.function`、`@modal.asgi_app`、`@modal.enter`
- **常用启动方式**：`modal run misc/quic/quic_yolo_modal.py`

## `misc/test_case_generator.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：LLM-Generated Unit Test Development
- **源码**：[打开 `misc/test_case_generator.py`](../misc/test_case_generator.py)
- **关键对象**：`modal.App`、`modal.Cls`、`modal.Function`、`modal.Image`、`modal.Sandbox`、`modal.Volume`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.concurrent`
- **常用启动方式**：`modal run misc/test_case_generator.py`

## `misc/vector_similarity_search.py`

- **作用**：组合 sentence-transformers 与 pgvector 完成向量相似度检索。
- **源码原题**：Vector similarity search with pgvector and sentence-transformers
- **源码**：[打开 `misc/vector_similarity_search.py`](../misc/vector_similarity_search.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run misc/vector_similarity_search.py`
