# Modal 案例中文导览

本目录按源码目录生成中文导览，覆盖仓库中可识别为 Modal 案例的 Python 脚本，以及基础 Notebook。每个条目均链接到对应源码；说明基于当前工作树的静态阅读，不代表已经部署或实际消耗云端资源。

## 使用方式

多数案例可从仓库根目录使用 `modal run <源码路径>` 启动；提供 Web 服务的案例通常使用 `modal serve` 或 `modal deploy`。运行前请阅读源文件的注释、配置所需 Secret，并留意 GPU、Volume、外部 API 与网络访问的成本和权限。

## 分册

- [01：快速入门](01_getting_started.md)：5 个案例。
- [02：构建容器镜像](02_building_containers.md)：3 个案例。
- [03：横向扩展](03_scaling_out.md)：3 个案例。
- [04：密钥与凭据](04_secrets.md)：1 个案例。
- [05：定时任务](05_scheduling.md)：2 个案例。
- [06：GPU 与机器学习](06_gpu_and_ml.md)：68 个案例。
- [07：Web 应用](07_web.md)：12 个案例。
- [08：进阶能力](08_advanced.md)：5 个案例。
- [09：任务队列](09_job_queues.md)：4 个案例。
- [10：外部集成](10_integrations.md)：11 个案例。
- [11：Notebook](11_notebooks.md)：2 个案例。
- [12：数据集](12_datasets.md)：4 个案例。
- [13：Sandbox](13_sandboxes.md)：10 个案例。
- [14：集群](14_clusters.md)：1 个案例。
- [杂项案例](misc.md)：9 个案例。

## 覆盖范围

本次共索引 140 个案例（139 个 Python 脚本和 1 个 Notebook）。`internal/` 是仓库测试与维护基础设施，不纳入案例说明；同一案例目录中的辅助模块会在所属条目中通过源码链接保留可追溯性。
