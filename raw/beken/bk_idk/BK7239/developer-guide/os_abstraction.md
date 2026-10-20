---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7239/zh_CN/v2.2.1/developer-guide/os_abstraction/index.html
sdk_family: bk_idk
chip: BK7239
processor: ''
sdk_version: v2.2.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="os"></a>

# OS 抽象层

<a id="id1"></a>

## OS 抽象层介绍

> - OS抽象层主要为了适配Armino平台不同的操作系统
> - 对于不同的操作系统，OS抽象层对外提供一套统一的接口
> - 目前Armino平台OS抽象层支持的操作系统有FreeRTOS，鸿蒙OS，RTThread.
> - 目前Armino平台posix接口仅支持FreeRTOS V10.4操作系统，默认关闭，若使用，需要打开CONFIG\_FREERTOS\_POSIX配置开关

备注

- 在使用FreeRTOS的posix功能的时候，在引用posix相关头文件之前，需要先引用FreeRTOS\_POSIX.h头文件；
- 可以在components/bk\_rtos/freertos/posix/freertos\_impl/include/portable/bk/FreeRTOS\_POSIX\_portable.h中自定义相关配置。

<a id="os-api"></a>

## OS API详细信息

- [OS API](../api-reference/system/os.md)
- [Posix API](../api-reference/system/posix.md)

## 模块导航

- [简介](../introduction.md)
- [快速入门](../get-started.md)
- [H/W 参考手册](../hw-reference.md)
- [API 参考手册](../api-reference.md)
- [开发者指南](../developer-guide.md)
- [软件架构与分层](architecture.md)
- [构建](build_config.md)
- [配置与工具](config_tools.md)
- [低功耗与电源管理](power_save.md)
- [设备管理框架](driver_model.md)
- [外设与驱动](peripheral.md)
- [事件机制](event.md)
- [出错与日志](error_log.md)
- [系统调试](debug_trace.md)
- [Wi-Fi](wifi.md)
- [Bluetooth](bluetooth.md)
- [HTTP](http.md)
- [OS API](../api-reference/system/os.md)
- [Posix API](../api-reference/system/posix.md)
- [Bootloader与Ota](bootloader_ota.md)
- [用例编写](examples.md)
- [文档系统](documentation.md)
- [安全](../security.md)
- [OS 相关参考](../os.md)
- [购买 BK7239 开发板](../boards.md)
- [样例 CLI 演示](../examples.md)
- [开发与贡献代码流程](../process.md)
