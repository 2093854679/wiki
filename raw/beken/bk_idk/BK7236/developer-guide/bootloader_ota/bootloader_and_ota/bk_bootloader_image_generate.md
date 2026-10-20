---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7236/zh_CN/v2.0.1/developer-guide/bootloader_ota/bootloader_and_ota/bk_bootloader_image_generate.html
sdk_family: bk_idk
chip: BK7236
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bootloader"></a>

# 四.Bootloader镜像文件生成

- 1.直接编译生成bootloader.bin；具体编译步骤如下：

  - 1）进入bootloader代码目录下；
  - 2）make clean
  - 3）make
  - 4）在PACK目录下执行generate.bat脚本，在generate\_out目录下生成bootloader.bin以及对应的bootloader\_crc.bin

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
- [Bootloader简介](bk_bootloader_brief_introduction.md)
- [L_bootloader介绍](bk_l_bootloader.md)
- [UP_bootloader和ota介绍](bk_up_bootloader_and_ota.md)
- [ota升级固件介绍](bk_ota_upgrade_image.md)
- [Bootloader镜像更新说明](bk_bootloader_imag_update.md)
- [ab位置无关升级](../ab_position_independent_ota.md)
- [安全ota升级](../bk_security_ota.md)
- [用例编写](../../examples.md)
- [文档系统](../../documentation.md)
- [安全](../../../security.md)
- [OS 相关参考](../../../os.md)
- [购买 BK7236 开发板](../../../boards.md)
- [工程与示例](../../../projects/projects.md)
- [样例 CLI 演示](../../../examples.md)
- [开发与贡献代码流程](../../../process.md)
