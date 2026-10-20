---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7236/zh_CN/v2.0.1/security/bk_security_cert.html
sdk_family: bk_idk
chip: BK7236
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 安全认证

重要

BK7236 当前正在进行 PSA-L2/SESIP-L2 安全认证…

<a id="psa-l2"></a>

## PSA-L2 认证概述

PSA-L2 是 IoT 领域最权威的安全认证标准，通过 PSA-L2 认证的设备具有下述安全功能：

> - `安全标识` \- 每台设备可以唯一地被标识。
> - `安全生命周期` \- 设备有完善的生命周期管理。
> - `鉴权` \- 设备可向第三方证明可信的，且不可克隆的。
> - `隔离` \- 硬件层支持安全与非安全世界的隔离。
> - `安全启动` \- 确保加载与运行的程序是合法的。
> - `安全升级` \- 确保升级过程是安全的。
> - `防回滚` \- 防止启动合法的，但版本较低的软件。
> - `安全接口` \- 确保安全世界提供的接口是安全的，不会因为非安全世界调用接口而造成安全问题。
> - `安全服务` \- 提供硬件安全配置/部署方式，以确保其他安全功能得以实现。

您可参考 [PSA](https://www.arm.com/zh-TW/architecture/security-features/platform-security) 了解 PSA-L2，SESIP-L2 相关信息。

## 模块导航

- [简介](../introduction.md)
- [快速入门](../get-started.md)
- [H/W 参考手册](../hw-reference.md)
- [API 参考手册](../api-reference.md)
- [开发者指南](../developer-guide.md)
- [安全](../security.md)
- [安全术语](bk_security_glossary.md)
- [安全概述](bk_security_overview.md)
- [安全引擎](bk_security_enginee.md)
- [安全启动](bk_security_boot.md)
- [安全调试](bk_security_debug.md)
- [生命周期](bk_security_lcs.md)
- [安全标识](bk_security_uid.md)
- [OTP](bk_security_otp.md)
- [EFUSE](bk_security_efuse.md)
- [FLASH 加密](bk_flash_aes.md)
- [防故障注入攻击](bk_security_fih.md)
- [安全编程](bk_security_programing.md)
- [漏洞披露](bk_security_bug_report.md)
- [OS 相关参考](../os.md)
- [购买 BK7236 开发板](../boards.md)
- [工程与示例](../projects/projects.md)
- [样例 CLI 演示](../examples.md)
- [开发与贡献代码流程](../process.md)
