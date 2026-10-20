---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7236/zh_CN/v2.0.1/developer-guide/power_save/bk_32k_source.html
sdk_family: bk_idk
chip: BK7236
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="k"></a>

# 32k的时钟源说明和配置

32k的时钟源，有以下几种：

- rosc

优缺点:
功耗低，但是时钟精度相对来说不好，最优功耗时可以选用它。

- 外部26M分频出的时钟

优缺点：
精度好，功耗高相对高

- 外部32k时钟

优缺点：
精度好，功耗相对外部26M分频的时钟低

因此可以根据不同的业务和场景选用不同的32k时钟

<a id="id1"></a>

# 切换32k时钟源函数接口说明

枚举类型：

typedef enum
{

> PM\_LPO\_SRC\_DIVD, //32K from 26m
>
> PM\_LPO\_SRC\_X32K, //extern 32k
>
> PM\_LPO\_SRC\_ROSC, //32K from ROSC
>
> PM\_LPO\_SRC\_DEFAULT //32K from ROSC

}pm\_lpo\_src\_e

- 配置32K时钟源：

通过在工程中配置以下宏来配置32K的时钟源。
例如配置使用ROSC，以下两个宏都配置成n
CONFIG\_EXTERN\_32K\=n
CONFIG\_LPO\_SRC\_26M32K\=n

> | #配置 | CONFIG\_EXTERN\_32K | CONFIG\_LPO\_SRC\_26M32K |
> | --- | --- | --- |
> | 外部32k | y | n |
> | 26M分下来的32K | n | y |
> | rosc | n | n |

- 获取当前使用32K时钟源函数接口:

pm\_lpo\_src\_e bk\_pm\_lpo\_src\_get()

- 获取当前配置文件配置的32K时钟源:

/\*\*
:   - @brief get the 32k clock source configured by the customer
    - This API get the 32k clock source configured by the customer
    - @return
    - - PM\_LPO\_SRC\_X32K: support the external 32k clock
    - - PM\_LPO\_SRC\_ROSC: default support the ROSC
    - - PM\_LPO\_SRC\_DIVD: 32K from 26m

    */*

pm\_lpo\_src\_e bk\_clk\_32k\_customer\_config\_get();

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
- [设置TOUCH作为唤醒源，系统进入深度睡眠和低压睡眠说明](bk_touch_sleep.md)
- [使用外部32K时钟源](bk_use_extern32K.md)
- [设置WIFI低压保活说明](bk_wifi_alive.md)
- [如何动态切换CPU主频](bk_cpu_vote_freq.md)
- [如何启动和关闭CPU1](bk_vote_boot_cp1.md)
- [关闭多媒体模块接口参考](bk_close_multimedia.md)
- [低功耗问题分析](bk_Lowpower_problem_analysis.md)
- [低功耗问题分析checklist](bk_lowpower_checklist.md)
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
- [Bootloader与Ota](../bootloader_ota.md)
- [用例编写](../examples.md)
- [文档系统](../documentation.md)
- [安全](../../security.md)
- [OS 相关参考](../../os.md)
- [购买 BK7236 开发板](../../boards.md)
- [工程与示例](../../projects/projects.md)
- [样例 CLI 演示](../../examples.md)
- [开发与贡献代码流程](../../process.md)
