# 02：构建容器镜像

展示如何把依赖、CUDA 工具链和 Python 包放入可复现的 Modal Image。

返回 [案例总览](README.md)。

## `02_building_containers/import_sklearn.py`

- **作用**：在自定义 Image 中安装 scikit-learn，再运行一个简单模型。
- **源码原题**：Install scikit-learn in a custom image
- **源码**：[打开 `02_building_containers/import_sklearn.py`](../02_building_containers/import_sklearn.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.function`
- **常用启动方式**：`modal run 02_building_containers/import_sklearn.py`

## `02_building_containers/install_cuda.py`

- **作用**：比较 GPU Function 自带驱动与自行安装完整 CUDA Toolkit 的场景。
- **源码原题**：Installing the CUDA Toolkit on Modal
- **源码**：[打开 `02_building_containers/install_cuda.py`](../02_building_containers/install_cuda.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 02_building_containers/install_cuda.py`

## `02_building_containers/install_flash_attn.py`

- **作用**：构建含 PyTorch 与 FlashAttention 的 GPU 镜像并验证内核。
- **源码原题**：Install Flash Attention on Modal
- **源码**：[打开 `02_building_containers/install_flash_attn.py`](../02_building_containers/install_flash_attn.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.function`
- **常用启动方式**：`modal run 02_building_containers/install_flash_attn.py`
