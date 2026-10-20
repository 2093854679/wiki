---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7235/zh_CN/v1.5/developer-guide/security/bk_security_scheme_selection.html
sdk_family: bk_idk
chip: BK7235
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 安全方案

BK7256的安全方案支持secure boot、flash加解密、固件版本防回滚等功能，针对不同的安全需求，有以下三种场景可选择：

> - 仅开启security boot
> - 仅开启flash encrypt
> - security boot和flash encrypt都开启

1. 仅开启security boot

特点：
:   - 会强制检查镜像的真实性\+完整性，确保只有客户的代码可以运行
    - 烧写在flash上的镜像是明文
    - 密钥被保护，secureboot开启后软件不可读
    - bootloader不可更新
    - secureboot key、ota key可以定制
    - 支持版本防回滚

    镜像选择：首次烧写选择镜像all\_app\_pack\_sign\_crc.bin，烧写地址0x0
    :   更新app时烧写镜像app\_pack\_sign\_crc.bin，烧写地址0x11000

2. 仅开启flash encrypt

特点：
:   - 确保了镜像的机密性，烧写在flash上的镜像是密文
    - 密钥不被保护，软件可读出
    - Bootloader和app可通过串口更新
    - flash加密密钥可自主设定，OTA 传输加密的key固定使用默认值
    - 不支持版本防回滚

镜像选择：烧写镜像all\_app\_pack\_enc\_crc.bin，烧写地址0x0

3. security boot和flash encrypt都开启

特点：
:   - 提供最高等级的安全保护，真实性\+完整性\+机密性
    - 密钥被保护，secureboot开启后软件不可读
    - bootloader不可更新
    - secureboot key、flash加密的key、OTA传输加密的 key可以定制
    - 支持版本防回滚

    镜像选择：首次烧写选择镜像all\_app\_pack\_sign\_enc\_crc.bin，烧写地址0x0
    :   更新app时烧写镜像app\_pack\_sign\_enc\_crc.bin，烧写地址0x11000

以上安全相关镜像在buildappbk7256encrypt路径下。

重要

建议使用安全功能时security boot和flash encrypt都开启，使用最高等级的保护。

## 模块导航

- [简介](../../introduction.md)
- [快速入门](../../get-started.md)
- [H/W 参考手册](../../hw-reference.md)
- [API 参考手册](../../api-reference.md)
- [开发者指南](../../developer-guide.md)
- [软件架构与分层](../architecture.md)
- [构建与配置](../build_config.md)
- [系统安全](../security.md)
- [安全概述](bk_security_overview.md)
- [安全使用](bk_security_usermenu.md)
- [OTP和eFuse的配置及读写方法](bk_OTP_and_eFuse_usermenu.md)
- [低功耗与电源管理](../power_save.md)
- [内存与性能](../memory_perf.md)
- [设备管理框架](../driver_model.md)
- [外设与驱动](../peripheral.md)
- [事件机制](../event.md)
- [出错与日志](../error_log.md)
- [系统调试](../debug_trace.md)
- [Wi-Fi](../wifi.md)
- [Bluetooth](../bluetooth.md)
- [HTTP](../http.md)
- [OS 抽象层](../os_abstraction.md)
- [OS 移植指南](../porting.md)
- [Bootloader和OTA](../bootloader.md)
- [特定芯片相关指南](../boards.md)
- [特定 CPU 相关指南](../cpu.md)
- [用例编写](../examples.md)
- [文档系统](../documentation.md)
- [分区规范](../partition_specification.md)
- [OS 相关参考](../../os.md)
- [样例演示](../../examples.md)
- [应用开发](../../application.md)
- [产品解决方案](../../projects.md)
- [开发与贡献代码流程](../../process.md)
- [云平台](../../clounds.md)
- [版本](../../release-notes.md)
