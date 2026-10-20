---
type: summary
source_root: beken
sdk_family: bk_idk
chip: BK7236
sdk_version: v2.0.1
processor: null
---

# BK7236 Wi-Fi API v2.0 使用概览

> **TLDR:** BK7236 文档中的 Wi-Fi API v2.0 采用事件驱动，按通用、接口和模块分组；使用时要核对接口共存限制、初始化顺序、配置预留字段和函数当前支持状态。
> **Source:** [BK7236 Wi-Fi APIs](../../../raw/beken/bk_idk/BK7236/api-reference/wifi/bk_wifi.md)

## 关键要点

- **接口独立不等于能任意共存。** 驱动提供 STA、AP、Monitor 三种逻辑接口；原文明确 Monitor 启动时 STA 启动会失败，其它限制需查具体函数。[接口说明](../../../raw/beken/bk_idk/BK7236/api-reference/wifi/bk_wifi.md#wi-fi-interface)
- **API 分三组。** 通用组包括初始化、国家码等；接口组面向 STA/AP/Monitor；模块组包含 scan、filter 等操作。[API 分类](../../../raw/beken/bk_idk/BK7236/api-reference/wifi/bk_wifi.md#wi-fi-api-categories)
- **初始化与配置有顺序。** `bk_wifi_init()` 是其它 Wi-Fi 操作前的初始化入口；STA 需要先成功设置配置再启动。配置可使用默认宏，预留字段必须清零，并检查返回值。[初始化和配置原文](../../../raw/beken/bk_idk/BK7236/api-reference/wifi/bk_wifi.md)
- **事件回调保持简短。** 应用通过 API 操作驱动，再由事件获取结果；文档建议将复杂工作转交自己的应用任务，并先读示例确认用法。[开发模型](../../../raw/beken/bk_idk/BK7236/api-reference/wifi/bk_wifi.md#user-development-model)
- **声明不代表已实现。** 这份文档的 `bk_wifi_deinit()` 仍标记为尚未支持；查询 API 时应阅读 Attention 和错误返回，不能只从函数列表推断可用性。[函数支持状态](../../../raw/beken/bk_idk/BK7236/api-reference/wifi/bk_wifi.md)

## 适用范围

本摘要只核验 BK7236 IDK v2.0.1 文档。Wi-Fi API 名称中的 v2.0 是接口代际，不等于 SDK 版本；不推定 BK7235、BK7236N、BK7258 或 SMP AP/CP 行为一致。

## Related

- [[bk-armino-framework]]
- [[wifi-networking-stack]]
- [[wifi-basics]]
- [[bk-low-power]]
