# 13：Sandbox

介绍隔离代码执行、交互环境、编程代理和 Sandbox 预热池。

返回 [案例总览](README.md)。

## `13_sandboxes/codelangchain/agent.py`

- **作用**：将 LangChain/LangGraph 编程代理与隔离的 Modal Sandbox 集成。
- **源码原题**：Build a coding agent with Modal Sandboxes and LangGraph
- **源码**：[打开 `13_sandboxes/codelangchain/agent.py`](../13_sandboxes/codelangchain/agent.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Sandbox`、`modal.Secret`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 13_sandboxes/codelangchain/agent.py`

## `13_sandboxes/codelangchain/langserve.py`

- **作用**：将 LangChain/LangGraph 编程代理与隔离的 Modal Sandbox 集成。
- **源码原题**：Deploy LangChain and LangGraph applications with LangServe
- **源码**：[打开 `13_sandboxes/codelangchain/langserve.py`](../13_sandboxes/codelangchain/langserve.py)
- **关键对象**：`modal.App`、`modal.Secret`、`@app.function`、`@modal.asgi_app`
- **常用启动方式**：`modal serve 13_sandboxes/codelangchain/langserve.py`

## `13_sandboxes/codelangchain/src/nodes.py`

- **作用**：将 LangChain/LangGraph 编程代理与隔离的 Modal Sandbox 集成。
- **源码原题**：State
- **源码**：[打开 `13_sandboxes/codelangchain/src/nodes.py`](../13_sandboxes/codelangchain/src/nodes.py)
- **关键对象**：`modal.Sandbox`
- **常用启动方式**：`modal run 13_sandboxes/codelangchain/src/nodes.py`

## `13_sandboxes/cua/computer_use_vnc.py`

- **作用**：通过 VNC 实时观察浏览器自动化代理在 Sandbox 内操作。
- **源码原题**：Watch a Browser Use agent drive Chromium over VNC
- **源码**：[打开 `13_sandboxes/cua/computer_use_vnc.py`](../13_sandboxes/cua/computer_use_vnc.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Probe`、`modal.Sandbox`、`modal.Server`、`@app.function`、`@app.local_entrypoint`、`@modal.asgi_app`、`@modal.concurrent`
- **常用启动方式**：`modal run 13_sandboxes/cua/computer_use_vnc.py`

## `13_sandboxes/jupyter_sandbox.py`

- **作用**：在独立 Sandbox 中启动可交互的 Jupyter 环境。
- **源码原题**：Run a Jupyter notebook in a Modal Sandbox
- **源码**：[打开 `13_sandboxes/jupyter_sandbox.py`](../13_sandboxes/jupyter_sandbox.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Sandbox`、`modal.Secret`
- **常用启动方式**：`modal run 13_sandboxes/jupyter_sandbox.py`

## `13_sandboxes/opencode_server.py`

- **作用**：在 Sandbox 中运行 OpenCode 编程代理服务。
- **源码原题**：Run OpenCode in a Modal Sandbox
- **源码**：[打开 `13_sandboxes/opencode_server.py`](../13_sandboxes/opencode_server.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Sandbox`、`modal.Secret`
- **常用启动方式**：`modal run 13_sandboxes/opencode_server.py`

## `13_sandboxes/safe_code_execution.py`

- **作用**：在隔离的多语言 Sandbox 中运行不可信代码。
- **源码原题**：Run arbitrary code in a sandboxed environment
- **源码**：[打开 `13_sandboxes/safe_code_execution.py`](../13_sandboxes/safe_code_execution.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Sandbox`
- **常用启动方式**：`modal run 13_sandboxes/safe_code_execution.py`

## `13_sandboxes/sandbox_agent.py`

- **作用**：让编程代理在隔离的 Modal Sandbox 内执行工具调用。
- **源码原题**：Run Claude Code in a Modal Sandbox
- **源码**：[打开 `13_sandboxes/sandbox_agent.py`](../13_sandboxes/sandbox_agent.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Sandbox`、`modal.Secret`
- **常用启动方式**：`modal run 13_sandboxes/sandbox_agent.py`

## `13_sandboxes/sandbox_pool.py`

- **作用**：维持健康的预热 Sandbox 池，降低交互任务的启动延迟。
- **源码原题**：Maintain a pool of warm Sandboxes that are healthy and ready to serve requests
- **源码**：[打开 `13_sandboxes/sandbox_pool.py`](../13_sandboxes/sandbox_pool.py)
- **关键对象**：`modal.App`、`modal.Function`、`modal.Image`、`modal.Period`、`modal.Probe`、`modal.Queue`、`modal.Sandbox`、`@app.function`、`@modal.concurrent`、`@modal.fastapi_endpoint`
- **常用启动方式**：`modal run 13_sandboxes/sandbox_pool.py`

## `13_sandboxes/simple_code_interpreter.py`

- **作用**：构建带会话状态的 Sandbox 代码解释器。
- **源码原题**：Build a stateful, sandboxed code interpreter
- **源码**：[打开 `13_sandboxes/simple_code_interpreter.py`](../13_sandboxes/simple_code_interpreter.py)
- **关键对象**：`modal.App`、`modal.Sandbox`
- **常用启动方式**：`modal run 13_sandboxes/simple_code_interpreter.py`
