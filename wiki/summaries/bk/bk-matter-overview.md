---
type: summary
source_root: beken
sdk_family: bk_matter
chip: [BK7235, BK7236, BK7256, BK7258]
sdk_version: v2.0.1
processor: null
---

# BK Matter 开发框架概述

> **TLDR:** BK Matter 将 Matter 数据模型和交互机制接入 Beken 平台；开发路径是选设备类型、完成芯片适配和构建、验证配网控制，再处理证书、认证及量产数据，各示例的芯片支持要分别确认。
> **Source:** [Matter 首页](../../../raw/beken/bk_matter/index.md)、[Matter 基础](../../../raw/beken/bk_matter/matter-basic.md)、[快速入门](../../../raw/beken/bk_matter/get-started.md)、[Beken 应用开发](../../../raw/beken/bk_matter/matter-examples.md)、[工具目录](../../../raw/beken/bk_matter/matter-tools.md)

## 关键要点

- **先建立协议模型。** 官方简介把 Matter 定义为基于 IP 的应用层连接标准，说明 Fabric、Node、Endpoint、Cluster 及 Read/Write/Invoke/Subscribe；这些概念不同于底层 Wi-Fi API。[Matter 基础](../../../raw/beken/bk_matter/matter-basic.md)
- **应用与平台适配分层。** `components/matter/connectedhomeip` 包含 Matter SDK，`src/platform/Beken` 提供 BLE、Wi-Fi、KV 等平台适配；应用由设备类型对应的 Beken example 定制。[应用开发](../../../raw/beken/bk_matter/matter-examples.md)
- **构建有附加工具依赖。** 快速入门在 Armino 环境外还要求 gn、ninja 和 ZAP，并给出 BK7236 的 Matter 工程构建示例；应按所选源码分支核对依赖。[快速入门](../../../raw/beken/bk_matter/get-started.md)
- **测试与量产分开查。** 文档分别提供 chip-tool、ZAP、chip-cert、factory-data、OTA provider 和生态配网测试入口，产品还应下钻认证及量产流程。[工具目录](../../../raw/beken/bk_matter/matter-tools.md)／[认证与量产](../../../raw/beken/bk_matter/matter-production.md)
- **不能用首页芯片列表推定每种角色。** 官网中心将四个芯片指向同一文档集，但应用页的 Matter Controller 示例只明确列 BK7235/BK7256/BK7258；具体设备类型与角色的支持应以对应工程为准。[Controller 示例](../../../raw/beken/bk_matter/matter-examples.md#matter-controller-example)

## 适用范围

覆盖官网 Matter v2.0.1 共用中文文档入口及其关联的 BK7235/BK7236/BK7256/BK7258。本文不推定所有芯片均支持 Thread 或所有 Matter 角色，也不将 BK Wi-Fi Controller 方案与 Matter Controller 混同。

## Related

- [[bk-armino-framework]]
- [[iot-communication-protocols]]
- [[bk-controller-overview]]
- [[bk-bootloader-ota]]
