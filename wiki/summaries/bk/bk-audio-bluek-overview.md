---
type: summary
source_root: beken
sdk_family: bk_audio
chip: BK3298
sdk_version: latest
processor: null
---

# BK3298 BlueK 开发入口

> **TLDR:** BK Audio 的 BK3298 入口称为 Armino BlueK，快速入门覆盖工具环境、产品工程编译、生成带 CRC 镜像和 UART 烧录；公开指南部分下载地址仍为待填写。
> **Source:** [BlueK 首页](../../../raw/beken/bk_audio/BK3298/index.md)、[快速入门](../../../raw/beken/bk_audio/BK3298/get-started.md)、[开发指南](../../../raw/beken/bk_audio/BK3298/developer-guide.md)

## 关键要点

- **文档分区。** 官网首页把资料分为快速入门、API 参考和开发者指南，具体功能参数应读该芯片原文。[首页](../../../raw/beken/bk_audio/BK3298/index.md)
- **工程以产品划分。** 入门页以 `BK3298-tws` 构建目录为例，编译产生对应 BIN，随后由配置工具生成带 CRC 的烧录文件。[快速入门](../../../raw/beken/bk_audio/BK3298/get-started.md)
- **烧录链路独立核对。** 文档展示 Windows UART 烧录及 BK_BT_Toolkit 的配置/烧录流程；日志还涉及工程生成的 `0_log_string.dat`。[烧录与日志](../../../raw/beken/bk_audio/BK3298/get-started.md)
- **公开信息有缺口。** 快速入门中的 SDK 源码、工具链和部分工具下载位置仍写“待填写”；这些信息不能由知识库补猜。开发指南另提供出厂、配件、按键、OTA 与测试入口。[入门限制](../../../raw/beken/bk_audio/BK3298/get-started.md)／[指南目录](../../../raw/beken/bk_audio/BK3298/developer-guide.md)

## 适用范围

适用于官网 BK3298 `latest` 文档路径，这个路径不是固定 SDK 发布号。未核实 AP/CP 架构；不把 BK7258 AVDK 的音频接口或参数迁入本芯片摘要。

## Related

- [[ble-protocol-overview]]
- [[bk-toolkit-overview]]
- [[embedded-coding-standards]]
