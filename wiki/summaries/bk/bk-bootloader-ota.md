---
type: summary
source_root: beken
sdk_family: bk_idk
chip: BK7236
sdk_version: v2.0.1
processor: null
---

# BK7236 Bootloader 与 OTA 方案概览

> **TLDR:** BK7236 文档分别介绍常规 OTA、A/B 位置无关升级和 TF-M 安全升级；执行区切换、首次启动确认、真实性及版本检查属于不同机制，需按所选方案实现。
> **Source:** [Bootloader/OTA 总目录](../../../raw/beken/bk_idk/BK7236/developer-guide/bootloader_ota.md)、[A/B 概述](../../../raw/beken/bk_idk/BK7236/developer-guide/bootloader_ota/ab_position_independent_ota/bk_ab_position_independent_ota_overview.md)、[A/B 升级原理](../../../raw/beken/bk_idk/BK7236/developer-guide/bootloader_ota/ab_position_independent_ota/bk_upgrade_principle_introduction.md)、[安全升级](../../../raw/beken/bk_idk/BK7236/developer-guide/bootloader_ota/bk_security_ota.md)

## 关键要点

- **先选方案。** 总目录将 bootloader 和常规 OTA、A/B 位置无关 OTA、安全 OTA 单独列出；不能把安全升级打包规则直接套进常规 A/B 工程。[方案目录](../../../raw/beken/bk_idk/BK7236/developer-guide/bootloader_ota.md)
- **A/B 使用备用执行区。** 当前在 A 时下载到 B，当前在 B 时下载到 A，重启后由 bootloader 校验并配置 Flash 映射选择执行区。[A/B 概述](../../../raw/beken/bk_idk/BK7236/developer-guide/bootloader_ota/ab_position_independent_ota/bk_ab_position_independent_ota_overview.md)／[升级原理](../../../raw/beken/bk_idk/BK7236/developer-guide/bootloader_ota/ab_position_independent_ota/bk_upgrade_principle_introduction.md)
- **回退有明确条件。** A/B 原文说明 Hash 失败保持旧区，新区首次运行后若应用未确认该执行区，下次启动返回旧区；这不等于任何运行故障都能无条件自动回滚。[确认与回退](../../../raw/beken/bk_idk/BK7236/developer-guide/bootloader_ota/ab_position_independent_ota/bk_upgrade_principle_introduction.md)
- **安全 OTA 的镜像布局不同。** 文档使用 TF-M FWU：BL2 采用 A/B，SPE+NSPE 合并为 ALL 镜像并走单地址搬运；因此不能概括为“所有固件都是双 App 分区”。[安全升级设计](../../../raw/beken/bk_idk/BK7236/developer-guide/bootloader_ota/bk_security_ota.md)
- **完整性、真实性与防降级分别核验。** 安全升级说明包括下载 CRC32、FWU 检查、重启后的 BOOTROM/BL2 验证及版本检查；这些要求限定在该安全升级方案。[安全检查](../../../raw/beken/bk_idk/BK7236/developer-guide/bootloader_ota/bk_security_ota.md)

## 适用范围

只覆盖 BK7236 IDK v2.0.1。分区、确认 API、升级包格式和安全开关必须跟随工程；不推定 BK7235、BK7236N、BK7239 或其它 SDK 文档族采用相同方案。

## Related

- [[bk-security-framework]]
- [[bk-armino-framework]]
- [[http-upload-task]]
