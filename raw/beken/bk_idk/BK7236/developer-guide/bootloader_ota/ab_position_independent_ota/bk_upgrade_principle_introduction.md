---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7236/zh_CN/v2.0.1/developer-guide/bootloader_ota/ab_position_independent_ota/bk_upgrade_principle_introduction.html
sdk_family: bk_idk
chip: BK7236
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="ab"></a>

# AB分区位置无关升级原理

> - 当APP(应用程序)运行在A分区并进行OTA（Over-the-AirTechnology）升级时，
>   :   - 根据分区表将升级固件从服务器下载分区B，下载成功之后,进行reboot。
>       - 然后，bootloader进行hash验证来数据的准确性，若数据没问题，则设置jump跳转地址为A区起始地址且设置flash相关控制寄存器bit位值为1，则运行到B分区；(当升级完第一次启动后，运行到app中客户没有进行执行分区B确认的话，下次启动会返回到分区A)
>       - 否则，则设置jump跳转地址为A区起始地址且设置flash相关控制寄存器bit位值为0，还是运行在A分区。
> - 当APP运行在B分区并进行OTA升级时，
>   :   - 即从服务器下载镜像A，下载镜像完成之后进行reboot。
>       - 然后，bootloader进行hash来验证数据的准确性，则设置jump跳转地址为A区起始地址且设置flash相关控制寄存器bit位值为0，则运行到A分区；(当升级完第一次启动后，运行到app中客户没有进行执行分区A确认的话，下次启动会返回到分区B)
>       - 否则，则设置jump跳转地址为A区起始地址且设置flash相关控制寄存器bit位值为1，还是运行在B分区。

## 模块导航

- [简介](../../../introduction.md)
- [快速入门](../../../get-started.md)
- [H/W 参考手册](../../../hw-reference.md)
- [API 参考手册](../../../api-reference.md)
- [开发者指南](../../../developer-guide.md)
- [软件架构与分层](../../architecture.md)
- [构建](../../build_config.md)
- [配置与工具](../../config_tools.md)
- [低功耗与电源管理](../../power_save.md)
- [内存与性能](../../memory_perf.md)
- [设备管理框架](../../driver_model.md)
- [外设与驱动](../../peripheral.md)
- [事件机制](../../event.md)
- [出错与日志](../../error_log.md)
- [系统调试](../../debug_trace.md)
- [Wi-Fi](../../wifi.md)
- [Bluetooth](../../bluetooth.md)
- [HTTP](../../http.md)
- [OS 抽象层](../../os_abstraction.md)
- [Bootloader与Ota](../../bootloader_ota.md)
- [bootloader和常规ota](../bootloader_and_ota.md)
- [ab位置无关升级](../ab_position_independent_ota.md)
- [AB分区位置无关ota概述](bk_ab_position_independent_ota_overview.md)
- [AB分区位置无关工程介绍](bk_ab_position_independent_project_introduction.md)
- [AB分区位置无关的编译命令介绍](bk_compile_command_introduction.md)
- [AB分区位置无关的升级镜像路径](bk_upgrade_image_route_introduction.md)
- [AB分区位置无关的优势](bk_upgrade_advantage_introduction.md)
- [AB分区位置无关的升级流程介绍](bk_upgrade_process_introduction.md)
- [AB分区位置无关的相关接口介绍](bk_upgrade_api_introduction.md)
- [AB分区位置无关的hash功能验证流程介绍](bk_hash_process_introduction.md)
- [AB的bootloader镜像更新介绍](bk_ab_bootloader_imag_update_introduction.md)
- [增加AB分区功能或建立AB工程的介绍](bk_introduce_ab_functionality_or_establishing_ab_project.md)
- [安全ota升级](../bk_security_ota.md)
- [用例编写](../../examples.md)
- [文档系统](../../documentation.md)
- [安全](../../../security.md)
- [OS 相关参考](../../../os.md)
- [购买 BK7236 开发板](../../../boards.md)
- [工程与示例](../../../projects/projects.md)
- [样例 CLI 演示](../../../examples.md)
- [开发与贡献代码流程](../../../process.md)
