# 05：定时任务

演示 Cron 与周期性云端作业。

返回 [案例总览](README.md)。

## `05_scheduling/hackernews_alerts.py`

- **作用**：定时检索 Hacker News，并把匹配结果发送到 Slack。
- **源码原题**：Run cron jobs in the cloud to search Hacker News
- **源码**：[打开 `05_scheduling/hackernews_alerts.py`](../05_scheduling/hackernews_alerts.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Period`、`modal.Secret`、`@app.function`
- **常用启动方式**：`modal run 05_scheduling/hackernews_alerts.py`

## `05_scheduling/schedule_simple.py`

- **作用**：用 Modal 的调度器周期性触发远程任务。
- **源码原题**：Scheduling remote jobs
- **源码**：[打开 `05_scheduling/schedule_simple.py`](../05_scheduling/schedule_simple.py)
- **关键对象**：`modal.App`、`modal.Cron`、`modal.Period`、`@app.function`
- **常用启动方式**：`modal run 05_scheduling/schedule_simple.py`
