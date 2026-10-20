---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7239/zh_CN/v2.2.1/developer-guide/power_save/bk_32k_source.html
sdk_family: bk_idk
chip: BK7239
processor: ''
sdk_version: v2.2.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="k"></a>

# 32k的时钟源说明

32k的时钟源，有以下几种：

- rosc32k

优缺点:
功耗低，但是时钟精度相对来说不好，最优功耗时可以选用它。

- 外部晶体40M分频32k

优缺点：
精度好，功耗高相对高

- 外部晶体32k

优缺点：
精度好，功耗相对外部40M分频的时钟低

因此可以根据不同的业务和场景选用不同的32k时钟

<a id="id1"></a>

# 切换32k时钟源函数接口说明

枚举类型：

```
typedef enum
{
    PM_LPO_SRC_DIVD, //32K from 40m
    PM_LPO_SRC_X32K,    //extern 32k
    PM_LPO_SRC_ROSC,    //32K from ROSC
    PM_LPO_SRC_DEFAULT  //32K from ROSC
}pm_lpo_src_e;
```

---

- 设置32K时钟源函数接口：

bk\_pm\_lpo\_src\_set(pm\_lpo\_src\_e lpo\_src)

- 获取当前使用32K时钟源函数接口:

pm\_lpo\_src\_e bk\_pm\_lpo\_src\_get()

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
- [设置WIFI低压保活说明](bk_wifi_alive.md)
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
- [购买 BK7239 开发板](../../boards.md)
- [样例 CLI 演示](../../examples.md)
- [开发与贡献代码流程](../../process.md)
