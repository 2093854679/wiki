---
type: summary
source_root: beken
sdk_family: bk_mesh
chip: BK7236
sdk_version: v2.0.1
processor: null
---

# BK Wi-Fi Mesh 开发概览

> **TLDR:** BK-MESH 是基于 Beken IDK 的 Wi-Fi Mesh 框架，面向覆盖扩展、多设备接入、自主组网与修复；应用开发需要同时核对 SDK 工程、串口角色和配套 Mesh App。
> **Source:** [Mesh 首页](../../../raw/beken/bk_mesh/BK7236/index.md)、[框架简介](../../../raw/beken/bk_mesh/BK7236/introduction.md)、[快速入门](../../../raw/beken/bk_mesh/BK7236/get-started.md)

## 关键要点

- **框架定位。** 官方简介说明 BK-WIFI-MESH 提供 Wi-Fi 覆盖扩展、更多接入设备及自主组网、自主修复能力，底座是 Beken IDK。[简介](../../../raw/beken/bk_mesh/BK7236/introduction.md)
- **当前入口以 BK7236 为例。** 入门页使用 BK7236 开发板，默认工程是 `projects/bk_mesh/3_led`，新建工程可参考 `projects/bk_mesh/app`。[工程配置](../../../raw/beken/bk_mesh/BK7236/get-started.md)
- **分清 Log 与 AT 串口。** 文档分别配置 `CONFIG_UART_PRINT_PORT`、`CONFIG_DEFAULT_AT_PORT`，并要求使用对应串口观察运行状态。[快速入门](../../../raw/beken/bk_mesh/BK7236/get-started.md)
- **编译与手机侧管理分别查。** 入门页规定 Linux 编译、Windows UART 烧录；配套 Mesh App 文档另含群组、节点、拓扑、灯光及本地/云 OTA 的使用入口。[SDK 入门](../../../raw/beken/bk_mesh/BK7236/get-started.md)／[Mesh App](../../../raw/beken/bk_toolkit/meshapp/index.md)

## 适用范围

本摘要以 BK7236 v2.0.1 官网默认文档为范围。入门页提及其它芯片的工具链不代表所有示例均兼容；不同芯片应另核验源码配置。AP/CP 分工未在所读概览中核实。

## Related

- [[bk-armino-framework]]
- [[wifi-networking-stack]]
- [[bk-toolkit-overview]]
