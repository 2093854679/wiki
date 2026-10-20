---
type: summary
source_root: beken
sdk_family: bk_findmy
chip: BK3633
sdk_version: v2.0.1
processor: null
---

# BK3633 FindMy 开发概览

> **TLDR:** BK3633 FindMy 的入门链路是选择 Apple、Google 或组合工程，配置配件与出厂信息，再完成编译、UART 烧录及对应生态测试。
> **Source:** [FindMy 首页](../../../raw/beken/bk_findmy/BK3633/index.md)、[快速入门](../../../raw/beken/bk_findmy/BK3633/get-started.md)、[开发指南](../../../raw/beken/bk_findmy/BK3633/developer-guide.md)

## 关键要点

- **工程按生态区分。** 快速入门分别列出 `projects/app_findmy`、`projects/google_findmy` 和 `projects/all_findmy`；编译、输出文件与测试说明应跟随所选工程。[快速入门](../../../raw/beken/bk_findmy/BK3633/get-started.md)
- **先配身份，再制作固件。** 原文要求首次编译前检查配件信息，首次烧录前检查出厂信息；开发指南提供两个独立配置入口。[配件信息](../../../raw/beken/bk_findmy/BK3633/developer-guide/accessory_information.md)／[出厂信息](../../../raw/beken/bk_findmy/BK3633/developer-guide/factory_config.md)
- **构建与烧录是两个环节。** 文档覆盖 Linux、Windows+Cygwin 的构建环境及 UART 烧录；源码仓库账号需要项目审核，公开文档不等于源码已公开授权。[环境与烧录](../../../raw/beken/bk_findmy/BK3633/get-started.md)
- **产品适配不止协议 API。** 指南还包含加速度传感器、蜂鸣器、按键、OTA、Apple UARP 及各生态测试入口。[开发指南目录](../../../raw/beken/bk_findmy/BK3633/developer-guide.md)

## 适用范围

适用于官网默认 BK3633 FindMy v2.0.1 文档。未核实 AP/CP 分工，不套用 BK7258/BK7259 的 SMP 结构。原文工具链版本存在不同段落示例，实际构建应以所获 SDK 交付说明核对。

## Related

- [[ble-protocol-overview]]
- [[bk-bootloader-ota]]
- [[embedded-coding-standards]]
