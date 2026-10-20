---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v2.0.1/developer-guide/security/bk_flash_aes.html
sdk_family: bk_idk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="flash-aes"></a>

# FLASH AES 加密

![8](../../../../_assets/d07691133d63fc368cae-security_flash.svg)

如上图所示，BK7258 FLASH 提供了两中访问接口：数据口与指令口。为确保指令的安全性，FLASH 指令口访问提供了
AES 加密机制。当经由 FLASH 指令口写数据时，FLASH 控制器会使用存放在 OTP 中的 AES KEY 自动对
写入的数据加密；当通过 FLASH 指令口读取数据时，FLASH 控制器会使用 AES KEY 对读出的数据进行解密。

通常，FLASH 指令口仅用在下述三种情况中：

> - CPU 从 FLASH 取指。
> - BL1/BL2 安全启动。
> - OTA 升级。

其他情况都应该走 FLASH 数据口访问 FLASH。

<a id="id1"></a>

## 配置

要使用 FLASH AES 加密功能，需做下述配置：

> - security.csv 中使能并配置 AES KEY，请参考 [安全配置](../config_tools/bk_config_security.md#bk-config-security)。
> - EFUSE 中使能 FLASH AES 功能，并将 KEY 部署到 OTP 中，请参考 [OTP EFUSE 配置](../config_tools/bk_config_otp_efuse.md#bk-config-otp-efuse)。

重要

BK7258 暂不支持自动生成随机 FLASH AES KEY，需要用户手动配置 AES KEY，为确保存放在
FLASH 中指令安全，您需要妥善保管好您的 FLASH AES KEY。

## 模块导航

- [简介](../../introduction.md)
- [快速入门](../../get-started.md)
- [H/W 参考手册](../../hw-reference.md)
- [API 参考手册](../../api-reference.md)
- [开发者指南](../../developer-guide.md)
- [软件架构与分层](../architecture.md)
- [构建](../build_config.md)
- [配置与工具](../config_tools.md)
- [系统安全](../security.md)
- [安全术语](bk_security_glossary.md)
- [PSA-L2/SESIP-L2 认证](bk_security_cert.md)
- [安全概述](bk_security_overview.md)
- [安全引擎](bk_security_enginee.md)
- [安全启动](bk_security_boot.md)
- [安全调试](bk_security_debug.md)
- [生命周期](bk_security_lcs.md)
- [安全标识](bk_security_uid.md)
- [防故障注入攻击](bk_security_fih.md)
- [漏洞报告](bk_security_bug_report.md)
- [安全编程](bk_security_programing.md)
- [低功耗与电源管理](../power_save.md)
- [内存与性能](../memory_perf.md)
- [设备管理框架](../driver_model.md)
- [外设与驱动](../peripheral.md)
- [事件机制](../event.md)
- [出错与日志](../error_log.md)
- [系统调试](../debug_trace.md)
- [稳定性问题调试](../debug_stability.md)
- [Wi-Fi](../wifi.md)
- [Bluetooth](../bluetooth.md)
- [HTTP](../http.md)
- [OS 抽象层](../os_abstraction.md)
- [Bootloader与Ota](../bootloader_ota.md)
- [用例编写](../examples.md)
- [文档系统](../documentation.md)
- [OS 相关参考](../../os.md)
- [样例演示](../../examples.md)
- [应用开发](../../application.md)
- [开发与贡献代码流程](../../process.md)
- [云平台](../../cloud.md)
- [工程与示例](../../projects/projects.md)
