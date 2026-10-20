---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7235/zh_CN/v1.5/developer-guide/power_save/bk_wifi_alive.html
sdk_family: bk_idk
chip: BK7235
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="wifi"></a>

# 设置WIFI低压保活说明

<a id="id1"></a>

## 设置WIFI低压保活调用函数和调用顺序说明

- 1. 当使用BT配置完网络，不要使用BT时，可以把它，这样可以达到更低的功耗
  > bk\_ble\_deinit();
  >
  > 关闭BT
- 2.bk\_wifi\_send\_listen\_interval\_req(10);

  > 设置DTIM10(1:DTIM1)
- 3. bk\_pm\_sleep\_mode\_set(PM\_MODE\_LOW\_VOLTAGE);
  > 设置睡眠模式，进入低压睡眠。
- 4. demo\_sta\_app\_init(“a”, “b”);
  > 连接路由器（a:路由器的名字;b:路由器的密码）
- 5. bk\_pm\_module\_vote\_sleep\_ctrl(PM\_POWER\_MODULE\_NAME\_APP,0x1,0x0);
  > 向系统中投应用程序的票。

(备注：一定需要设备连接上路由器，拿到IP地址，才调用以上函数bk\_pm\_module\_vote\_sleep\_ctrl()投APP的票，不然移动设备不能网络唤醒测试设备)

备注：

> - 1. BT和WIFI的票，BT和WIFI模块内部进入睡眠后自己投上，SDK内部做好，应用程序不用关注
> - 2. 当系统中BT或WIFI模块没有上电时，系统会自动给这两个模块投上sleep的票。

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
- [使用外部32K时钟源说明](bk_use_extern32K.md)
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
