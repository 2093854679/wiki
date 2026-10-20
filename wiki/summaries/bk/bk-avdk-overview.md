---
type: summary
source_root: beken
sdk_family: bk_avdk
chip: BK7258
sdk_version: v2.0.1
verified_at: 2026-10-21
---

# BK7258 AVDK 音视频开发概览

> **TLDR:** BK7258 AVDK v2.0.1 面向摄像头、显示、音频和编解码；开发时优先核对多媒体开关配对、PSRAM 分配及目标工程配置，不套用 SMP 版本的核分工。

> **Source:** [快速入门](../../../raw/beken/bk_avdk/get-started.md), [多媒体功耗](../../../raw/beken/bk_avdk/power_save.md), [PSRAM 配置](../../../raw/beken/bk_avdk/psram_config.md)

## 要点

- 快速入门给出 `release/v2.0.1` SDK 获取与工程构建入口；基础平台配置需同时参考对应 IDK。
- 多媒体功耗指南将多媒体功能放在 CPU1，媒体接口内部封装 CPU1、电源域和 PSRAM 投票。应用应成对调用 open/close，避免退出功能后留下电源票。
- PSRAM 的 heap、音频、编码和显示等区域应按工程实际资源配置；帧尺寸、缓存帧数与各区域容量需要同时核对。
- 排查多媒体不能休眠时，可在启用相应 CLI 的工程中使用 `pm_debug 8` 检查媒体、PSRAM 与 CPU1 状态；该命令及其字段仅按此版本指南理解。

## 原文入口

- [API 参考](../../../raw/beken/bk_avdk/api-reference.md)
- [摄像头](../../../raw/beken/bk_avdk/camera.md)、[显示](../../../raw/beken/bk_avdk/display.md)、[GUI](../../../raw/beken/bk_avdk/gui.md)、[编解码](../../../raw/beken/bk_avdk/video_codec.md)
- [官方版本](https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/)

## Related

- [[bk-armino-framework]]
- [[bk7258-smp-architecture]]
- [[freertos-memory-management]]
