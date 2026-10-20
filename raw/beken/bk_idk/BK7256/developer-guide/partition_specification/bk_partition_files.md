---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/developer-guide/partition_specification/bk_partition_files.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 分区修改的组成

<a id="id2"></a>

## 一.分区修改的组成

修改分区涉及到四个部分:

重要

- 分区表制作
- 打包脚本的配置文件
- 链接脚本配置文件（sag）的制作
- bootloader的分区表制作

<a id="id3"></a>

## 二．需修改的文件及存放位置示例

重要

- 因编译脚本对app工程有特殊限制，针对bootloader.bin的修改只能替换middlewareboardsbk7256bootloader.bin，放在projects/app/bootloader.bin无效；
- 除app以外的其它工程没有此限制，bootloader.bin可直接放在工程根目录下；

以bk7256为例，当在app工程下修改分区，涉及的文件如下：

<a id="id4"></a>
![overflow](../../../../_assets/f93a6807d1c8410d81f0-partition_example.png)


图1编译报错图示

## 模块导航

- [简介](../../introduction.md)
- [快速入门](../../get-started.md)
- [H/W 参考手册](../../hw-reference.md)
- [API 参考手册](../../api-reference.md)
- [开发者指南](../../developer-guide.md)
- [软件架构与分层](../architecture.md)
- [构建与配置](../build_config.md)
- [系统安全](../security.md)
- [低功耗与电源管理](../power_save.md)
- [内存与性能](../memory_perf.md)
- [1、内存概述](../memory_perf.md)
- [2、PSRAM概述](../memory_perf.md)
- [3. PSRAM 划分](../memory_perf.md)
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
- [物理地址与逻辑地址的关系介绍](bk_partition_introduce.md)
- [如何调整分区](bk_partition_usermenu.md)
- [声网开发指南](../agora.md)
- [华镇语音识别开发指南](../wanson_asr.md)
- [OS 相关参考](../../os.md)
- [样例演示](../../examples.md)
- [应用开发](../../application.md)
- [工程](../../projects_work.md)
- [产品解决方案](../../projects.md)
- [开发与贡献代码流程](../../process.md)
- [云平台](../../clounds.md)
- [版本](../../release-notes.md)
