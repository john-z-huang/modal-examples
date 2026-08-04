# 07：Web 应用

涵盖 Web Function、ASGI/WSGI、流式响应、服务器与实时通信。

返回 [案例总览](README.md)。

## `07_web/badges.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：Serve a dynamic SVG badge
- **源码**：[打开 `07_web/badges.py`](../07_web/badges.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.function`、`@modal.fastapi_endpoint`
- **常用启动方式**：`modal serve 07_web/badges.py`

## `07_web/basic_web.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：Hello world wide web!
- **源码**：[打开 `07_web/basic_web.py`](../07_web/basic_web.py)
- **关键对象**：`modal.App`、`modal.Cls`、`modal.Image`、`@app.cls`、`@app.function`、`@modal.enter`、`@modal.fastapi_endpoint`
- **常用启动方式**：`modal serve 07_web/basic_web.py`

## `07_web/count_faces.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：Run OpenCV face detection on an image
- **源码**：[打开 `07_web/count_faces.py`](../07_web/count_faces.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.function`、`@app.get`、`@app.post`、`@modal.asgi_app`
- **常用启动方式**：`modal serve 07_web/count_faces.py`

## `07_web/discord_bot.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：Serve a Discord Bot on Modal
- **源码**：[打开 `07_web/discord_bot.py`](../07_web/discord_bot.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`@app.function`、`@app.local_entrypoint`、`@modal.asgi_app`、`@modal.concurrent`
- **常用启动方式**：`modal run 07_web/discord_bot.py`

## `07_web/fastapi_app.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：Deploy FastAPI app with Modal
- **源码**：[打开 `07_web/fastapi_app.py`](../07_web/fastapi_app.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.function`、`@modal.asgi_app`、`@modal.fastapi_endpoint`
- **常用启动方式**：`modal serve 07_web/fastapi_app.py`

## `07_web/fastrtc_flip_webcam.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：Run a FastRTC app on Modal
- **源码**：[打开 `07_web/fastrtc_flip_webcam.py`](../07_web/fastrtc_flip_webcam.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.function`、`@modal.asgi_app`、`@modal.concurrent`
- **常用启动方式**：`modal serve 07_web/fastrtc_flip_webcam.py`

## `07_web/flask_app.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：Deploy Flask app with Modal
- **源码**：[打开 `07_web/flask_app.py`](../07_web/flask_app.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.function`、`@modal.wsgi_app`
- **常用启动方式**：`modal serve 07_web/flask_app.py`

## `07_web/flask_streaming.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：Deploy Flask app with streaming results with Modal
- **源码**：[打开 `07_web/flask_streaming.py`](../07_web/flask_streaming.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.function`、`@modal.wsgi_app`
- **常用启动方式**：`modal serve 07_web/flask_streaming.py`

## `07_web/server.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：Deploy HTTP Servers with ultra low latency on Modal
- **源码**：[打开 `07_web/server.py`](../07_web/server.py)
- **关键对象**：`modal.App`、`@app.local_entrypoint`、`@app.server`、`@modal.enter`
- **常用启动方式**：`modal run 07_web/server.py`

## `07_web/server_sticky.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：Sticky routing for Modal Servers
- **源码**：[打开 `07_web/server_sticky.py`](../07_web/server_sticky.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.local_entrypoint`、`@app.server`、`@modal.enter`
- **常用启动方式**：`modal run 07_web/server_sticky.py`

## `07_web/streaming.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：Deploy a FastAPI app with streaming responses
- **源码**：[打开 `07_web/streaming.py`](../07_web/streaming.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.function`、`@modal.asgi_app`、`@modal.fastapi_endpoint`
- **常用启动方式**：`modal serve 07_web/streaming.py`

## `07_web/webrtc/webrtc_yolo.py`

- **作用**：以 WebRTC 承载低延迟媒体流，并在服务端执行实时视觉处理。
- **源码原题**：Real-time object detection with WebRTC and YOLO
- **源码**：[打开 `07_web/webrtc/webrtc_yolo.py`](../07_web/webrtc/webrtc_yolo.py)
- **关键对象**：`modal.App`、`modal.Dict`、`modal.Function`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.cls`、`@app.function`、`@modal.asgi_app`、`@modal.concurrent`
- **常用启动方式**：`modal serve 07_web/webrtc/webrtc_yolo.py`
