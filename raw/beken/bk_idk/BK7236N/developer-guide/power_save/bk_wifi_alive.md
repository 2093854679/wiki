---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7236n/zh_CN/v2.2.1/developer-guide/power_save/bk_wifi_alive.html
sdk_family: bk_idk
chip: BK7236N
processor: ''
sdk_version: v2.2.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="wifi"></a>

# 设置WIFI低压保活说明

<a id="id1"></a>

## 设置WIFI低压保活调用函数和调用顺序说明

- 1. 当使用BLE配置完网络，不要使用BLE时，可以关闭BLE，以达到更低的功耗;
  > bk\_bluetooth\_deinit();
  >
  > 关闭BLE
- 2.bk\_wifi\_send\_listen\_interval\_req(10);

  > 设置listen interval为10;
- 3. bk\_pm\_sleep\_mode\_set(PM\_MODE\_LOW\_VOLTAGE);
  > 设置睡眠模式，进入低压睡眠。
- 4. demo\_sta\_app\_init(“ssid”, password”);
  > 连接路由器（ssid:路由器的名字;password:路由器的密码）
- 5. bk\_pm\_module\_vote\_sleep\_ctrl(PM\_SLEEP\_MODULE\_NAME\_APP,0x1,0x0);
  > 向系统中投应用程序的票。

(备注：一定需要设备连接上路由器，拿到IP地址，才调用以上函数bk\_pm\_module\_vote\_sleep\_ctrl()投APP的票，不然移动设备不能网络唤醒测试设备)

备注：

> - 1. BLE和WIFI的票，BLE和WIFI模块内部进入睡眠后自己投上，SDK内部做好，应用程序不用关注
> - 2. 当系统中BLE或WIFI模块没有上电时，系统会自动给这两个模块投上sleep的票。

<a id="id2"></a>

## WiFi低压保活参考数据

BK7236N低压保活功耗参考数据，测试条件为DTIM\=10，设备已连接到路由器并关闭蓝牙，进入低压睡眠模式：

| 供电电压 | WiFi频段 | 典型电流值 |
| --- | --- | --- |
| 3.3V | 2.4G | 约95uA |

备注

1. 极限功耗测试条件与标准测试条件相同：DTIM\=10，设备已连接到路由器并关闭蓝牙
2. 实际功耗可能因具体应用场景、硬件版本和环境因素而略有差异

## 模块导航

- [简介](../../introduction.md)
- [快速入门](../../get-started.md)
- [H/W 参考手册](../../hw-reference.md)
- [API 参考手册](../../api-reference.md)
- [开发者指南](../../developer-guide.md)
- [软件架构与分层](../architecture.md)
- [构建](../build_config.md)
- [配置与工具](../config_tools.md)
- [低功耗与电源管理](../power_save.md)
- [电源域说明](bk_power_domain.md)
- [时钟说明](bk_clock.md)
- [CPU主频说明](bk_cpu_frequency.md)
- [系统状态机说明](bk_fsm.md)
- [状态机切换说明](bk_fsm.md)
- [设置GPIO作为唤醒源，系统进入深度睡眠和低压睡眠说明](bk_gpio_sleep.md)
- [设置RTC作为唤醒源，系统进入深度睡眠和低压睡眠说明](bk_rtc_sleep.md)
- [32k的时钟源说明](bk_32k_source.md)
- [切换32k时钟源函数接口说明](bk_32k_source.md)
- [低功耗问题分析](bk_Lowpower_problem_analysis.md)
- [设备管理框架](../driver_model.md)
- [外设与驱动](../peripheral.md)
- [事件机制](../event.md)
- [出错与日志](../error_log.md)
- [系统调试](../debug_trace.md)
- [Wi-Fi](../wifi.md)
- [Bluetooth](../bluetooth.md)
- [HTTP](../http.md)
- [OS 抽象层](../os_abstraction.md)
- [Bootloader与Ota](../bootloader_ota.md)
- [用例编写](../examples.md)
- [文档系统](../documentation.md)
- [安全](../../security.md)
- [OS 相关参考](../../os.md)
- [购买 BK7236N 开发板](../../boards.md)
- [用例指南](../../examples.md)
- [开发与贡献代码流程](../../process.md)
