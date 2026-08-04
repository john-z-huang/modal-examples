# 03：横向扩展

关注并行映射、动态批处理、参数搜索和运行时资源配置。

返回 [案例总览](README.md)。

## `03_scaling_out/basic_grid_search.py`

- **作用**：将一组超参数组合并行运行，用于选择较优配置。
- **源码原题**：Hyperparameter search
- **源码**：[打开 `03_scaling_out/basic_grid_search.py`](../03_scaling_out/basic_grid_search.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 03_scaling_out/basic_grid_search.py`

## `03_scaling_out/cls_with_options.py`

- **作用**：通过 Cls.with_options 为同一类在运行时派生不同资源与扩缩容配置。
- **源码原题**：Override Modal resource options (GPU, scaling) at runtime with Cls.with_options
- **源码**：[打开 `03_scaling_out/cls_with_options.py`](../03_scaling_out/cls_with_options.py)
- **关键对象**：`modal.App`、`modal.Cls`、`@app.cls`、`@app.local_entrypoint`、`@modal.method`
- **常用启动方式**：`modal run 03_scaling_out/cls_with_options.py`

## `03_scaling_out/dynamic_batching.py`

- **作用**：把多个独立请求合并为动态批次，提高服务吞吐量。
- **源码原题**：Dynamic batching for ASCII and character conversion
- **源码**：[打开 `03_scaling_out/dynamic_batching.py`](../03_scaling_out/dynamic_batching.py)
- **关键对象**：`modal.App`、`modal.Function`、`modal.Image`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.batched`
- **常用启动方式**：`modal run 03_scaling_out/dynamic_batching.py`
