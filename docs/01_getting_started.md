# 01：快速入门

用最小代码理解 App、Function、远程调用与结果收集。

返回 [案例总览](README.md)。

## `01_getting_started/generators.py`

- **作用**：从远程生成器逐项消费流式结果。
- **源码原题**：Run a generator function on Modal
- **源码**：[打开 `01_getting_started/generators.py`](../01_getting_started/generators.py)
- **关键对象**：`modal.App`、`modal.Function`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 01_getting_started/generators.py`

## `01_getting_started/get_started.py`

- **作用**：以安装、认证和首次远程调用为线索完成入门流程。
- **源码原题**：get started
- **源码**：[打开 `01_getting_started/get_started.py`](../01_getting_started/get_started.py)
- **关键对象**：`modal.App`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 01_getting_started/get_started.py`

## `01_getting_started/hello_world.py`

- **作用**：定义一个最小远程 Function，并从本地入口调用它。
- **源码原题**：Hello, world!
- **源码**：[打开 `01_getting_started/hello_world.py`](../01_getting_started/hello_world.py)
- **关键对象**：`modal.App`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 01_getting_started/hello_world.py`

## `01_getting_started/inference.py`

- **作用**：把一个简单推理函数部署到 Modal 并远程执行。
- **源码原题**：inference
- **源码**：[打开 `01_getting_started/inference.py`](../01_getting_started/inference.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.function`
- **常用启动方式**：`modal run 01_getting_started/inference.py`

## `01_getting_started/inference_map.py`

- **作用**：用 Function.map 将一组输入分发到多次远程调用。
- **源码原题**：inference map
- **源码**：[打开 `01_getting_started/inference_map.py`](../01_getting_started/inference_map.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 01_getting_started/inference_map.py`
