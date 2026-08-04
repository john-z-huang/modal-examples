# 14：集群

展示多节点 PyTorch 训练集群的基础构成。

返回 [案例总览](README.md)。

## `14_clusters/simple_torch_cluster.py`

- **作用**：准备多节点 PyTorch 分布式训练的容器、脚本与集群配置。
- **源码原题**：Simple PyTorch cluster
- **源码**：[打开 `14_clusters/simple_torch_cluster.py`](../14_clusters/simple_torch_cluster.py)
- **关键对象**：`modal.App`、`modal.Function`、`modal.Image`、`@app.function`、`@modal.experimental`
- **常用启动方式**：`modal run 14_clusters/simple_torch_cluster.py`
