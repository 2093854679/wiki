---
type: concept
aliases:
  - SoftAP 配网任务
  - SOFTAP 配网
---

# SoftAP 配网任务

> **TLDR:** SoftAP 配网通过设备临时开启热点，让手机连接后提交目标 WiFi 凭据，设备再切换到 STA 模式连接目标 AP。

## 流程

1. 设备启动 SoftAP，设置 SSID、密码和本地 IP。
2. 启动 HTTP Server，提供配网页面或 POST 接口。
3. 手机连接设备热点，提交目标 WiFi 的 SSID 和密码。
4. 设备保存凭据，关闭 SoftAP 或切换 STA。
5. STA 连接目标 AP，并返回成功/失败状态。

## 易错点

- SoftAP 和 STA 状态切换时机不清晰。
- HTTP 接收参数没有做长度和编码校验。
- 凭据保存后没有考虑重启恢复。
- 连接失败没有回退到配网模式。

## Related

- [[wifi-basics]]
- [[task-development-records]]
- [[huang-learning-log]]
- [[internship-plan]]
