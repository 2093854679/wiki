---
type: summary
source_root: beken
sdk_family: bk_idk
chip: BK7236
sdk_version: v2.0.1
processor: null
---

# BK7236 安全架构概览

> **TLDR:** BK7236 安全文档围绕 M33 TrustZone、外设/内存隔离、BL1/BL2 验签和 Flash AES/CRC 展开；各能力依赖具体配置，生命周期章节尚为 TBC，不能据此补出完整状态机。
> **Source:** [安全总目录](../../../raw/beken/bk_idk/BK7236/security.md)、[安全架构](../../../raw/beken/bk_idk/BK7236/security/bk_security_overview.md)、[安全启动](../../../raw/beken/bk_idk/BK7236/security/bk_security_boot.md)、[Flash AES/CRC](../../../raw/beken/bk_idk/BK7236/security/bk_flash_aes.md)、[生命周期](../../../raw/beken/bk_idk/BK7236/security/bk_security_lcs.md)

## 关键要点

- **先理解隔离边界。** M33 TrustZone 区分安全/非安全世界，PPC 管外设属性、MPC 管内存块属性；软件划分为 SPE 与 NSPE，安全世界包含启动链与安全服务。[安全架构](../../../raw/beken/bk_idk/BK7236/security/bk_security_overview.md)
- **安全启动是显式模式。** 文档区分传统下载与安全启动，安全模式下 BL1 验证 BL2，再由 BL2 验证后续镜像；密钥、分区、安全配置及 OTP/EFUSE 部署需要配合完成。[安全启动](../../../raw/beken/bk_idk/BK7236/security/bk_security_boot.md)
- **Flash 加密不能脱离地址与 CRC。** 指令口经 Flash Controller 进行 CRC 与 AES 处理，数据口访问路径不同；文档说明密钥配置到 OTP，并在 EFUSE 使能相应功能，不能简写为“eFuse 保存所有密钥”。[Flash AES/CRC](../../../raw/beken/bk_idk/BK7236/security/bk_flash_aes.md)
- **已发布目录与已完成说明要区分。** 目录包含 FIH、调试、OTP、EFUSE 等主题，但生命周期正文仅为 `TBC`；这份原文不支持既有摘要中的 Raw→Test→Provisioning→Secure→RMA 状态机，也不支持将所有安全特性写成默认开启。[目录](../../../raw/beken/bk_idk/BK7236/security.md)／[生命周期原文](../../../raw/beken/bk_idk/BK7236/security/bk_security_lcs.md)

## 适用范围

只覆盖 BK7236 IDK v2.0.1 的公开说明。本文不声称 Flash 解密无性能开销，不泛化认证等级或量产状态，也不推定其它芯片具备相同安全架构。具体密钥、锁定位及升级方式需核对交付 SDK 和对应原文。

## Related

- [[bk-armino-framework]]
- [[bk-bootloader-ota]]
- [[bk-armino-overview]]
