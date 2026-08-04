# 08：进阶能力

介绍异步、并行执行、访问控制和延迟结果查询。

返回 [案例总览](README.md)。

## `08_advanced/generators_async.py`

- **作用**：用 async/await 方式消费远程异步生成器。
- **源码原题**：Run async generator function on Modal
- **源码**：[打开 `08_advanced/generators_async.py`](../08_advanced/generators_async.py)
- **关键对象**：`modal.App`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 08_advanced/generators_async.py`

## `08_advanced/hello_world_async.py`

- **作用**：比较同步与异步远程 Function 的调用写法。
- **源码原题**：Async functions
- **源码**：[打开 `08_advanced/hello_world_async.py`](../08_advanced/hello_world_async.py)
- **关键对象**：`modal.App`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 08_advanced/hello_world_async.py`

## `08_advanced/parallel_execution.py`

- **作用**：通过 spawn 与 gather 并发提交任务并汇总结果。
- **源码原题**：Parallel execution on Modal with spawn and gather
- **源码**：[打开 `08_advanced/parallel_execution.py`](../08_advanced/parallel_execution.py)
- **关键对象**：`modal.App`、`modal.FunctionCall`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 08_advanced/parallel_execution.py`

## `08_advanced/poll_delayed_result.py`

- **作用**：把耗时计算提交到后台，并提供可轮询的结果 URL。
- **源码原题**：Polling for a delayed result on Modal
- **源码**：[打开 `08_advanced/poll_delayed_result.py`](../08_advanced/poll_delayed_result.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.function`、`@modal.asgi_app`
- **常用启动方式**：`modal serve 08_advanced/poll_delayed_result.py`

## `08_advanced/restricted_volumes.py`

- **作用**：在受限访问环境中按最小权限挂载 Volume。
- **源码原题**：restricted volumes
- **源码**：[打开 `08_advanced/restricted_volumes.py`](../08_advanced/restricted_volumes.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Sandbox`、`modal.Volume`
- **常用启动方式**：`modal run 08_advanced/restricted_volumes.py`
