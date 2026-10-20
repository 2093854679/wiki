---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v2.0.1/developer-guide/config_tools/bk_config_ota.html
sdk_family: bk_idk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="ota"></a>

<a id="bk-config-ota"></a>

# OTA 配置

OTA 主要用于配置打包与防版本降级攻击的安全计数器。

<a id="id1"></a>

## OTA 配置表

OTA 配置表为 CSV 文件，下面为一个配置示例：

| Bin | Version | SecurityCounter | OTA |
| --- | --- | --- | --- |
| bl2.bin |  | 1 | FALSE |
| tfm\_s.bin |  | 1 | TRUE |
| cpu0\_app.bin |  | 1 | TRUE |

分区表固定为四列：

> - `Bin` \- 必选项，表示可执行二进制文件名字。对于特定二进制文件 xx.bin，其对应的 OTA 分区名字为 secondary\_xx，参考 [分区命名规则](bk_config_partitions.md#bk-config-partitions-table)。
> - `Version` \- 可选项，一般不需要配置。
> - `SecurityCounter` \- 可选项，表示版本安全计数器。安全启动使能时必须配置，用于防止版本降级攻击。安全启动验证版本合法之后
>   会读取该值，与 OTP/NV 中的安全计数器作比较，仅当升级版本的安全计数器不小于 OTP/NV 中的值时才允许启动。
> - `OTA` \- 可选项。表示对应的 Bin 是否要打包在 ota.bin 中。

备注

1. partitions.csv 中 secondary 为前缀的分区才允许做 OTA。分区有 OTA 能力时，才能在 ota.csv 中配置是否进行 OTA。
2. 应用分区 `SecurityCounter` 与 `OTA` 配置必须一致。

## 模块导航

- [简介](../../introduction.md)
- [快速入门](../../get-started.md)
- [H/W 参考手册](../../hw-reference.md)
- [API 参考手册](../../api-reference.md)
- [开发者指南](../../developer-guide.md)
- [软件架构与分层](../architecture.md)
- [构建](../build_config.md)
- [配置与工具](../config_tools.md)
- [概述](bk_config_overview.md)
- [Kconfig 配置](bk_config_kconfig.md)
- [分区配置](bk_config_partitions.md)
- [自动化分区配置](bk_config_auto_partitions.md)
- [安全配置](bk_config_security.md)
- [OTP/Efuse 配置](bk_config_otp_efuse.md)
- [非安全版本OTP使用介绍](bk_nosecure_version_of_otp_usage_instructions.md)
- [烧录工具 BKFIL](bk_tool_bkfil.md)
- [系统安全](../security.md)
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
