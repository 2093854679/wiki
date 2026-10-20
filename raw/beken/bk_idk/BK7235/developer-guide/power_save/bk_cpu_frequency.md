---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7235/zh_CN/v1.5/developer-guide/power_save/bk_cpu_frequency.html
sdk_family: bk_idk
chip: BK7235
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="cpu"></a>

# CPU时钟源说明

CPU有以下时钟源：

- 26M
- DCO
- 320M
- 480M

备注：
CPU主频最高可以达到320M，系统不支持运行到480M，可以通过分频使用240M。

<a id="id1"></a>

## CPU主频切换说明

- 可以根据业务需要动态的切频率来达到最优功耗,CPU主频切换相对来说比较复杂，SDK内部来实现。
- CPU主频最高可以达到320M

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
- [系统状态机说明](bk_fsm.md)
- [状态机切换说明](bk_fsm.md)
- [设置GPIO作为唤醒源，系统进入深度睡眠和低压睡眠说明](bk_gpio_sleep.md)
- [设置RTC作为唤醒源，系统进入深度睡眠和低压睡眠说明](bk_rtc_sleep.md)
- [设置TOUCH作为唤醒源，系统进入深度睡眠和低压睡眠说明](bk_touch_sleep.md)
- [设置32K时钟源说明](bk_32k_source.md)
- [使用外部32K时钟源说明](bk_use_extern32K.md)
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
