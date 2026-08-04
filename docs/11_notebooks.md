# 11：Notebook

展示如何在 Notebook 或 Sandbox 中使用 Modal。

返回 [案例总览](README.md)。

## 配合数据集案例使用 Jupyter Server

`jupyter_inside_modal.py` 适合交互式查看文件、检查日志和迭代实验；它**不是**当前 `12_datasets/` 脚本的直接启动器。原始实现只把自己的 Modal Volume 挂载到 `/root/cache`，并未把仓库的 `12_datasets/` 源码、数据集所需的 CloudBucketMount 或相关 Secret 放入 Jupyter 容器。

启动临时 Jupyter Server：

```bash
uv run modal run 11_notebooks/jupyter_inside_modal.py --timeout 1500
```

在浏览器打开终端输出的 tunnel URL，并输入配置的 Jupyter token。生产使用前应把源码中的固定 token `1234` 改为不可猜测的随机值。该 Server 的 Function 声明超时为 1,500 秒，因此这里的 `--timeout` 不应设置得更大。

如需在 Jupyter 中查看数据集下载的结果，应先改造 `jupyter_inside_modal.py`：把 `12_datasets/` 通过 `Image.add_local_dir(...)` 加入镜像，并用与你的数据集脚本相同的 `modal.CloudBucketMount` 挂载自己的 bucket，例如 `/mnt/datasets`。完成后可以在 Notebook 中浏览该挂载目录；若确实要在 Notebook 单元格中启动任务，可运行：

```python
!modal run /root/modal-examples/12_datasets/coco.py::import_transform_load
```

不过，推荐从本机终端启动下载任务，再将 Jupyter 用于检查数据和调试。这样源码上传、认证和日志的边界更清晰。

## `11_notebooks/basic.ipynb`

- **作用**：在本地 Jupyter Notebook 中定义并调用 Modal Function，观察远程 GPU 结果。
- **源码原题**：basic
- **源码**：[打开 `11_notebooks/basic.ipynb`](../11_notebooks/basic.ipynb)
- **关键对象**：`modal.App`、`@app.function`
- **常用启动方式**：`jupyter notebook 11_notebooks/basic.ipynb`

## `11_notebooks/jupyter_inside_modal.py`

- **作用**：在远程环境启动 Jupyter，并把连接方式暴露给本地用户。
- **源码原题**：jupyter inside modal
- **源码**：[打开 `11_notebooks/jupyter_inside_modal.py`](../11_notebooks/jupyter_inside_modal.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 11_notebooks/jupyter_inside_modal.py`
