---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7235/zh_CN/v1.5/developer-guide/power_save/bk_use_extern32K.html
sdk_family: bk_idk
chip: BK7235
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="k"></a>

# 使用外部32K

<a id="id1"></a>

## 开启外部32K时钟源方法

- 确保硬件已经焊接了外部32K时钟源
- 在middleware/soc/bk72xx/bk7256.defconfig中设置CONFIG\_EXTERN\_32K\=y

重要

当本地工程应用于其他项目时，为避免定义外部32K影响该工程，请新建工程，将CONFIG\_EXTERN\_32K定义在根目录下projects的新建工程的config/bk72xx.config中。
新建工程方法参考： [OS移植介绍](../porting.md)

<a id="id2"></a>

## 使用外部32K时钟源注意事项

> 因为外部32K引脚和DVP camera复用，当camera和外部32K同时使用时，为避免camera对外部32K干扰，需要按照以下顺序操作：

- camera init： camera上电之前先将32K时钟源切换到PM\_LPO\_SRC\_DIVD
- camera deinit：camera下电之后再将32K时钟源切换到PM\_LPO\_SRC\_X32K

重要

使用外部32K时，如果camera与其他模块共用ldo电源，在deinit时必须所有使用该ldo电源的模块关闭之后再切换32K时钟源到PM\_LPO\_SRC\_X32K(例如在camera deinit中不切换为外部32K时钟源，在该LDO电源关闭后再切换32K时钟源)。

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
- [电源域说明](bk_power_domain.md)
- [时钟说明](bk_clock.md)
- [CPU主频说明](bk_cpu_frequency.md)
- [系统状态机说明](bk_fsm.md)
- [状态机切换说明](bk_fsm.md)
- [设置GPIO作为唤醒源，系统进入深度睡眠和低压睡眠说明](bk_gpio_sleep.md)
- [设置RTC作为唤醒源，系统进入深度睡眠和低压睡眠说明](bk_rtc_sleep.md)
- [设置TOUCH作为唤醒源，系统进入深度睡眠和低压睡眠说明](bk_touch_sleep.md)
- [设置32K时钟源说明](bk_32k_source.md)
- [设置WIFI低压保活说明](bk_wifi_alive.md)
- [低功耗模块的典型问题和配置说明](bk_typical_problem_config.md)
- [低功耗问题分析](bk_Lowpower_problem_analysis.md)
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
