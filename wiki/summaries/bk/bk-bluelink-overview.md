---
type: summary
source_root: beken
sdk_family: bk_bluelink
chip: BK7258
sdk_version: v2.0.1
processor: null
---

# BK7258 BlueLink 蓝牙应用概览

> **TLDR:** BlueLink 基于 Armino AVDK 与 IDK 提供蓝牙应用参考，当前 wearable 工程把音频、通话、GATT 等能力组合在一起；具体 profile 与开关需查工程配置。
> **Source:** [BlueLink 首页](../../../raw/beken/bk_bluelink/BK7258/index.md)、[工程目录](../../../raw/beken/bk_bluelink/BK7258/projects.md)、[wearable 工程](../../../raw/beken/bk_bluelink/BK7258/projects/wearable.md)

## 关键要点

- **底座来自 AVDK/IDK。** 官方首页明确框架基于两者帮助开发蓝牙应用，平台配置仍回到 IDK。[首页](../../../raw/beken/bk_bluelink/BK7258/index.md)
- **按组合工程查入口。** wearable 概览列出 A2DP Sink、HFP、GATT、HOGPD、SPP、存储与 BT Manager 等子主题，不代表所有能力默认同时启用。[wearable](../../../raw/beken/bk_bluelink/BK7258/projects/wearable.md)
- **功能由项目宏控制。** wearable 文档列有 A2DP Sink、HFP 与 Doorbell 的配置开关，并给出 `bluetooth/wearable` 的编译工程名。[项目配置](../../../raw/beken/bk_bluelink/BK7258/projects/wearable.md)
- **定位问题时保留协议边界。** 蓝牙音频、通话、GATT 与配网各有不同子文档，应使用对应 profile 的初始化和示例，而不是仅凭框架名称生成 API。[工程导航](../../../raw/beken/bk_bluelink/BK7258/projects/wearable.md)

## 适用范围

适用于 BlueLink BK7258 v2.0.1。所读概览没有声明该工程的 SMP AP/CP 分工，也不用于推定 BK3298 BlueK 的兼容性。

## Related

- [[ble-protocol-overview]]
- [[bk-armino-framework]]
- [[bk-audio-bluek-overview]]
