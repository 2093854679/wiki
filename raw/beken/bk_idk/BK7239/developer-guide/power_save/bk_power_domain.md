---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7239/zh_CN/v2.2.1/developer-guide/power_save/bk_power_domain.html
sdk_family: bk_idk
chip: BK7239
processor: ''
sdk_version: v2.2.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 电源域说明

<a id="id2"></a>

## 电源域说明

<a id="id3"></a>

### 初识电源域

整个开发板分为三类电源域：
:   - 板级的电源域
    - 模拟部分电源域
    - 数字部分电源域

---

<a id="id4"></a>

### 模拟部分电源域

模拟电源域主要覆盖晶振、PLL、模拟前端、偏置与参考电路等模拟模块。
这些模块通常与时钟精度、射频性能和模拟信号质量强相关，在不同工作场景下对功耗和性能有直接影响。

模拟电源域下各业务模块同样支持按场景进行电源管理：
:   - 业务运行时，按需保持关键模拟模块上电，确保功能和性能稳定；
    - 进入低功耗前，关闭不必要的模拟子模块，降低静态和动态功耗；
    - 退出低功耗后，按业务时序恢复对应模拟模块，避免功能异常或性能抖动。

<a id="id5"></a>

### 引脚电源域与模块对应关系

从芯片引脚上看，相关电源域与模块对应关系如下：
:   - VCCPA：PA（功率放大器）模块电源；
    - VCCPAD：PAD/IO 模块电源；
    - VCCIF：IF（中频接口）模块电源；
    - VCCA：模拟公共模块电源；
    - VCCRXRF：RF 接收链路模块电源；
    - VCCPLL：PLL 模块电源。

其中电压分组如下：
:   - VCCPA、VCCPAD 与 VBAT 一致；
    - VCCIF、VCCA、VCCRXRF、VCCPLL 与 VDDA 一致。

<a id="vdddig-digital-core"></a>

### 数字部分电源为VDDDIG \- Digital Core电源域

Digital Core电源域下各个业务模块有自己单独的子电源域。各个业务可以根据自己的工作场景来决定上电还是下电，这样功耗控制很灵活，不同的产品形态达到最优功耗。

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
- [时钟说明](bk_clock.md)
- [CPU主频说明](bk_cpu_frequency.md)
- [系统状态机说明](bk_fsm.md)
- [状态机切换说明](bk_fsm.md)
- [设置GPIO作为唤醒源，系统进入深度睡眠和低压睡眠说明](bk_gpio_sleep.md)
- [设置RTC作为唤醒源，系统进入深度睡眠和低压睡眠说明](bk_rtc_sleep.md)
- [32k的时钟源说明](bk_32k_source.md)
- [切换32k时钟源函数接口说明](bk_32k_source.md)
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
