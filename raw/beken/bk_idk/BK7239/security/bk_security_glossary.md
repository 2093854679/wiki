---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7239/zh_CN/v2.2.1/security/bk_security_glossary.html
sdk_family: bk_idk
chip: BK7239
processor: ''
sdk_version: v2.2.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 安全术语

备注

在描述系统安全时，会直接使用本节介绍的安全术语!

<a id="id2"></a>

## 术语

相关述语与简写含义：

> - `S` \- Security world，表示安全世界。为 ARM Cortex-M33 中与 TrustZone 相关的概念。
> - `NS` \- Non-Security world，表示非安全世界。为 ARM Cortex-M33 中与 TrustZone 相关的概念。
> - `S/NS Aware` \- 特指自身能依据 S/NS 信号进行安全控制的设备。
> - `P` \- Privilege，表示 M33 运行在特权级。
> - `NP` \- Non-Privilege，表示 M33 运行在非特权级。
> - `M33` \- ARM Cortex-M33 处理器。
> - `TZ` \- TrustZone，M33 中引入的安全机制，通过 TZ 将 CPU 核隔离成 S/NS。
> - `PPC` \- Peripheral Protection Control，BK7239 外设安全属性配置与控制器。
> - `MPC` \- Memory Protection Control，BK7239 块存储安全属性配置与控制器。
> - `BL1` \- 特指固化在芯片中的 BootROM。
> - `BL2` \- Bootloader，在 BK7239 中特指 MCUBOOT。

## 模块导航

- [简介](../introduction.md)
- [快速入门](../get-started.md)
- [H/W 参考手册](../hw-reference.md)
- [API 参考手册](../api-reference.md)
- [开发者指南](../developer-guide.md)
- [安全](../security.md)
- [PSA-L3/SESIP-L3 认证](bk_security_cert.md)
- [安全概述](bk_security_overview.md)
- [安全引擎](bk_security_enginee.md)
- [安全启动](bk_security_boot.md)
- [安全调试](bk_security_debug.md)
- [安全标识](bk_security_uid.md)
- [OTP](bk_security_otp.md)
- [EFUSE](bk_security_efuse.md)
- [FLASH 加密](bk_flash_aes.md)
- [防故障注入攻击](bk_security_fih.md)
- [漏洞披露](bk_security_bug_report.md)
- [OS 相关参考](../os.md)
- [购买 BK7239 开发板](../boards.md)
- [样例 CLI 演示](../examples.md)
- [开发与贡献代码流程](../process.md)
