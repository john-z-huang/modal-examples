# 12：数据集

演示下载、转换、存储或分析常见机器学习数据集。

返回 [案例总览](README.md)。

## 运行下载任务

这四个脚本没有 `local_entrypoint`，因此不能只运行文件名。请从仓库根目录显式指定远程 Function：

```bash
uv run modal run 12_datasets/coco.py::import_transform_load
uv run modal run 12_datasets/imagenet.py::import_transform_load
uv run modal run 12_datasets/laion400.py::import_transform_load
uv run modal run 12_datasets/rosettafold.py::import_transform_load
```

先将每个脚本中的 `bucket_name` 与 `modal.Secret.from_name(...)` 改为自己可访问的 S3 bucket 和 AWS 凭据 Secret。仓库中的 `aws-s3-modal-examples-datasets` 与 `modal-examples-datasets` 是示例配置，普通账号通常没有访问权限。`imagenet.py` 还需要 `kaggle-api-token` Secret；它的 `KAGGLE_API_TOKEN` 值会原样写入容器内的 `~/.kaggle/kaggle.json`。

这些是长时间、高存储占用的远程下载任务。运行前应确认账户配额、数据集授权与预算：COCO 最长 5 小时并申请 600 GiB 临时盘；ImageNet 最长 8 小时并申请 1 TiB；LAION-400 最长 20 小时并申请 512 GiB；RoseTTAFold 最长 24 小时并申请约 2.5 TiB。完成后数据会写入 CloudBucketMount 指向的 bucket。

可选地，使用 [Notebook 章节](11_notebooks.md#配合数据集案例使用-jupyter-server) 中说明的改造版 Jupyter Server 查看挂载的结果；原始 `jupyter_inside_modal.py` 不包含这些脚本的源码或 bucket 挂载。

## `12_datasets/coco.py`

- **作用**：下载、准备或分析公开数据集，并演示数据在 Modal 容器与持久化存储间的流动。
- **源码原题**：coco
- **源码**：[打开 `12_datasets/coco.py`](../12_datasets/coco.py)
- **关键对象**：`modal.App`、`modal.CloudBucketMount`、`modal.Function`、`modal.Image`、`modal.Secret`、`@app.function`
- **常用启动方式**：`modal run 12_datasets/coco.py::import_transform_load`

## `12_datasets/imagenet.py`

- **作用**：下载、准备或分析公开数据集，并演示数据在 Modal 容器与持久化存储间的流动。
- **源码原题**：imagenet
- **源码**：[打开 `12_datasets/imagenet.py`](../12_datasets/imagenet.py)
- **关键对象**：`modal.App`、`modal.CloudBucketMount`、`modal.Function`、`modal.Image`、`modal.Secret`、`@app.function`
- **常用启动方式**：`modal run 12_datasets/imagenet.py::import_transform_load`

## `12_datasets/laion400.py`

- **作用**：下载、准备或分析公开数据集，并演示数据在 Modal 容器与持久化存储间的流动。
- **源码原题**：laion400
- **源码**：[打开 `12_datasets/laion400.py`](../12_datasets/laion400.py)
- **关键对象**：`modal.App`、`modal.CloudBucketMount`、`modal.Function`、`modal.Image`、`modal.Secret`、`@app.function`
- **常用启动方式**：`modal run 12_datasets/laion400.py::import_transform_load`

## `12_datasets/rosettafold.py`

- **作用**：下载、准备或分析公开数据集，并演示数据在 Modal 容器与持久化存储间的流动。
- **源码原题**：rosettafold
- **源码**：[打开 `12_datasets/rosettafold.py`](../12_datasets/rosettafold.py)
- **关键对象**：`modal.App`、`modal.CloudBucketMount`、`modal.Function`、`modal.Image`、`modal.Secret`、`@app.function`
- **常用启动方式**：`modal run 12_datasets/rosettafold.py::import_transform_load`
