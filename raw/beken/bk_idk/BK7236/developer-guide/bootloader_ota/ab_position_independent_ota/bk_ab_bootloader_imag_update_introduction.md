---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7236/zh_CN/v2.0.1/developer-guide/bootloader_ota/ab_position_independent_ota/bk_ab_bootloader_imag_update_introduction.html
sdk_family: bk_idk
chip: BK7236
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bootloader-bin"></a>

# Bootloader.bin的镜像更新说明

- 1.为了优化bootloader.bin镜像的版本发布，从tag:v2.0.1.8版本开始：bootloader镜像的打包路径发生改变，由原先的默认路径middleware/boards/更改为components/bk\_libs目录下。

  重要

  自从tag:v2.0.1.10之后的版本，已实现全自动插入bootloader.bin中的分区表，无需再手动修改bootloader中分区表。

  - 1.以bk\_avdk中customization/config\_ab工程为例修改分区步骤如下：
    :   - 1.当通过修改projects/customization/config\_ab/config/bk7236/bk7236\_partitions.csv文件来修改分区；
        - 2.直接make bk7236 PROJECT \= customization/config\_ab即可；
        - 3.无需手动修改components/bk\_libs/bk7236/bootloader/normal\_bootloader/bootloader.bin；

  重要

  bootloader镜像的打包路径发生改变，由原先的默认路径middleware/boards/更改为components/bk\_libs目录下。

  - 1.以7236的customization/config\_ab工程为例：
    :   - bootloader现路径为：components/bk\_libs/bk7236/bootloader/ab\_bootloader/bootloader.bin；
- 2.若升级过程中出现问题，请联系我们FAE支持。

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
- [AB分区位置无关升级原理](bk_upgrade_principle_introduction.md)
- [AB分区位置无关工程介绍](bk_ab_position_independent_project_introduction.md)
- [AB分区位置无关的编译命令介绍](bk_compile_command_introduction.md)
- [AB分区位置无关的升级镜像路径](bk_upgrade_image_route_introduction.md)
- [AB分区位置无关的优势](bk_upgrade_advantage_introduction.md)
- [AB分区位置无关的升级流程介绍](bk_upgrade_process_introduction.md)
- [AB分区位置无关的相关接口介绍](bk_upgrade_api_introduction.md)
- [AB分区位置无关的hash功能验证流程介绍](bk_hash_process_introduction.md)
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
