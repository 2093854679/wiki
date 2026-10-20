---
type: summary
source_root: beken
sdk_family: bk_controller
chip: [BK7236, BK7239N]
sdk_version:
  BK7236: v2.0.1
  BK7239N: v2.1.1
processor: null
---

# BK Wi-Fi Controller 方案概览

> **TLDR:** BK Controller 是配合外部主控工作的私有 Wi-Fi Controller 方案，关注主控休眠或下电时由 Controller 独立维持服务器连接；BK7236 与 BK7239N 的接口说明不同。
> **Source:** [BK7236 首页](../../../raw/beken/bk_controller/BK7236/index.md)、[BK7236 简介](../../../raw/beken/bk_controller/BK7236/introduction.md)、[BK7239N 首页](../../../raw/beken/bk_controller/BK7239N/index.md)、[BK7239N 简介](../../../raw/beken/bk_controller/BK7239N/introduction.md)

## 关键要点

- **主控与 Controller 共同开发。** 官方简介要求主控侧开发软件来控制 WLAN 扫描、连接等能力；这是外部主控/Controller 的分工，不等于 BK SMP 的 AP/CP 分工。[BK7236 简介](../../../raw/beken/bk_controller/BK7236/introduction.md)
- **重点是低功耗保活。** 文档面向 IPC、门铃、门锁场景，要求主控深睡或下电期间 Controller 仍能独立完成服务器保活。[BK7236](../../../raw/beken/bk_controller/BK7236/introduction.md)／[BK7239N](../../../raw/beken/bk_controller/BK7239N/introduction.md)
- **芯片接口要区分。** BK7236 简介写明主控通信可用 SDIO 或 USB；BK7239N 简介写明 SDIO，不能根据 BK7236 推定后者 USB 支持。[BK7236 接口](../../../raw/beken/bk_controller/BK7236/introduction.md)／[BK7239N 接口](../../../raw/beken/bk_controller/BK7239N/introduction.md)
- **按开发侧查指南。** 首页分别提供主控适配与 Controller 开发入口；BK7239N 还单列调测、产测和工程示例，具体协议及约束应继续下钻。[BK7236 导航](../../../raw/beken/bk_controller/BK7236/index.md)／[BK7239N 导航](../../../raw/beken/bk_controller/BK7239N/index.md)

## 适用范围

适用于 BK7236 v2.0.1、BK7239N v2.1.1 的官网默认中文文档。首页虽说明基于 IDK 扩展，其平台链接指向 BK7258 IDK；这是原站交叉链接，不能据此把目标芯片改成 BK7258。

## Related

- [[bk-armino-framework]]
- [[wifi-dtim10-tcp-keepalive]]
- [[bk-smp-product-solutions-overview]]
