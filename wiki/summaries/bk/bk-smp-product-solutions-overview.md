---
type: summary
source_root: beken
sdk_family: [bk_dashboard, bk_doorbell, bk_ipc]
chip: [BK7258, BK7259]
sdk_version:
  BK7258: v3.1.1
  BK7259: v4.0.1
processor: null
---

# BK SMP 仪表、门铃与 IPC 方案导航

> **TLDR:** Dashboard、Doorbell、IPC 是基于 AVDK SMP 的产品方案；先选产品与芯片版本，再核对显示、摄像头、低功耗和蓝牙从控配置，底层平台问题回到同版本 SMP 文档。
> **Source:** [BK7258 仪表](../../../raw/beken/bk_dashboard/BK7258/index.md)、[BK7259 仪表](../../../raw/beken/bk_dashboard/BK7259/index.md)、[BK7258 门铃](../../../raw/beken/bk_doorbell/BK7258/index.md)、[BK7259 门铃](../../../raw/beken/bk_doorbell/BK7259/index.md)、[BK7259 IPC](../../../raw/beken/bk_ipc/BK7259/index.md)

## 关键区别

- **Dashboard。** BK7258 方案使用 BK3515NS 蓝牙从控，面向多分辨率 LVGL 仪表；BK7259 方案写明 BK3515N 从控及 MIPI DSI+LVGL。两份首页都链接各自版本的 AVDK SMP。[BK7258](../../../raw/beken/bk_dashboard/BK7258/index.md)／[BK7259](../../../raw/beken/bk_dashboard/BK7259/index.md)
- **Doorbell BK7258。** 首页覆盖可视门铃、低功耗保活、MJPEG 显示兼容和 4M 变体，采集入口含 UVC/DVP。[BK7258 门铃](../../../raw/beken/bk_doorbell/BK7258/index.md)
- **Doorbell BK7259。** 首页覆盖可视门铃、低功耗保活和双向可视对讲，写明 MIPI/UVC 采集、H.264、MIPI LCD、双向音频及 BLE 配网。[BK7259 门铃](../../../raw/beken/bk_doorbell/BK7259/index.md)
- **IPC BK7259。** 首页面向无屏 IPC、AOV 低功耗和 ISP/H264E 联调，含 MIPI CSI、H.264 图传、双向音频及 AP 掉电保活的方案入口。[BK7259 IPC](../../../raw/beken/bk_ipc/BK7259/index.md)

## 适用范围

官网默认路径分别为 BK7258 v3.1.1 和 BK7259 v4.0.1；具体方案正文还以 v3.1.x/v4.0.x 描述底座。本文仅做选型导航，不据首页推定各示例功能已同时启用，也不推定 AP/CP API 可互换。

## Related

- [[bk-armino-framework]]
- [[bk-ai-solution-overview]]
- [[bk-controller-overview]]
- [[wifi-networking-stack]]
