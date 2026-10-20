---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_rtc.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-rtc"></a>

# DRV\_RTC

<a id="drv-rtc-api-status"></a>

## DRV\_RTC API Status

| API |
| --- |
| [`drv_rtc_enable()`](#_CPPv414drv_rtc_enableb "drv_rtc_enable") |
| [`drv_rtc_set_time()`](#_CPPv416drv_rtc_set_timeP10rtc_time_t "drv_rtc_set_time") |
| [`drv_rtc_get_time()`](#_CPPv416drv_rtc_get_timeP10rtc_time_tP8uint64_t "drv_rtc_get_time") |
| [`drv_rtc_xsec_intr()`](#_CPPv417drv_rtc_xsec_intr8uint32_t13pfunc_intr_cb "drv_rtc_xsec_intr") |

<a id="drv-rtc-api-reference"></a>

## DRV\_RTC API Reference

<a id="header-file"></a>

### Header File

- [driver/rtc/drv\_rtc.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/rtc/drv_rtc.h)

<a id="functions"></a>

### Functions

<a id="_CPPv414drv_rtc_enableb"></a>

<a id="_CPPv314drv_rtc_enableb"></a> <a id="_CPPv214drv_rtc_enableb"></a> <a id="drv_rtc_enable__b"></a> <a id="drv__rtc_8h_1a175247d48dd44a916948f017b9c1a5c0"></a> int32\_t drv\_rtc\_enable(bool enable)
:   enable RTC or not.

    参数:
    :   **enable** – **\[in\]** enable:打开 disable:关闭

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416drv_rtc_set_timeP10rtc_time_t"></a>

<a id="_CPPv316drv_rtc_set_timeP10rtc_time_t"></a> <a id="_CPPv216drv_rtc_set_timeP10rtc_time_t"></a> <a id="drv_rtc_set_time__rtc_time_tP"></a> <a id="drv__rtc_8h_1ab2a8db987e541d7117b16b18519c02ca"></a> int32\_t drv\_rtc\_set\_time([rtc\_time\_t](#_CPPv410rtc_time_t "rtc_time_t") \*pt\_utc\_time)
:   set current time for RTC.

    给RTC配置当前时间

    备注

    pt\_utc\_time-\>tm\_year \>\= 1970 \&\& pt\_utc\_time-\>tm\_year \<\= 18281420

    参数:
    :   **pt\_utc\_time** – **\[in\]** 指向当前的时间的结构体

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416drv_rtc_get_timeP10rtc_time_tP8uint64_t"></a>

<a id="_CPPv316drv_rtc_get_timeP10rtc_time_tP8uint64_t"></a> <a id="_CPPv216drv_rtc_get_timeP10rtc_time_tP8uint64_t"></a> <a id="drv_rtc_get_time__rtc_time_tP.uint64_tP"></a> <a id="drv__rtc_8h_1a6c04e89ed9c5801d80db0df1aee3d25d"></a> int32\_t drv\_rtc\_get\_time([rtc\_time\_t](#_CPPv410rtc_time_t "rtc_time_t") \*pt\_utc\_time, uint64\_t \*pu8\_tick\_sec)
:   get current time from RTC。

    参数:
    :   - **pt\_utc\_time** – **\[out\]** 指向当前的时间的结构体，是输出参数
        - **pu8\_tick\_sec** – **\[out\]** 指向获取tick的指针,单位是秒，0s\=1970.1.1 0:0:0

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv417drv_rtc_xsec_intr8uint32_t13pfunc_intr_cb"></a>

<a id="_CPPv317drv_rtc_xsec_intr8uint32_t13pfunc_intr_cb"></a> <a id="_CPPv217drv_rtc_xsec_intr8uint32_t13pfunc_intr_cb"></a> <a id="drv_rtc_xsec_intr__uint32_t.pfunc_intr_cb"></a> <a id="drv__rtc_8h_1a80076095d2bce9c7f0f09d0945cbf945"></a> void drv\_rtc\_xsec\_intr(uint32\_t x\_sec, [pfunc\_intr\_cb](#_CPPv413pfunc_intr_cb "pfunc_intr_cb") pfn\_cb)
:   enable or disable interrupt every x seconds.

    设置每x秒产生中断,并配置中断函数（为NULL的时候表示关闭中断）

    参数:
    :   - **x\_sec** – **\[in\]** every x seconds generate interrupt
        - **pfn\_cb** – **\[in\]** callback for interrupt, NULL for disable interrupt

    返回:
    :   N/A

<a id="_CPPv424drv_rtc_deepsleep_wakeup8uint32_t"></a>

<a id="_CPPv324drv_rtc_deepsleep_wakeup8uint32_t"></a> <a id="_CPPv224drv_rtc_deepsleep_wakeup8uint32_t"></a> <a id="drv_rtc_deepsleep_wakeup__uint32_t"></a> <a id="drv__rtc_8h_1a4fd2e3c18f1996be40996a3b4fd8a1b0"></a> void drv\_rtc\_deepsleep\_wakeup(uint32\_t tick)

<a id="structures"></a>

### Structures

<a id="_CPPv411_rtc_time_t"></a>

<a id="_CPPv311_rtc_time_t"></a> <a id="_CPPv211_rtc_time_t"></a> <a id="_rtc_time_t"></a> <a id="struct__rtc__time__t"></a> struct \_rtc\_time\_t

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv410rtc_time_t"></a>

<a id="_CPPv310rtc_time_t"></a> <a id="_CPPv210rtc_time_t"></a> <a id="rtc_time_t"></a> <a id="drv__rtc_8h_1a11439e400582c6c2da4e89693eb742c4"></a> typedef struct [\_rtc\_time\_t](#_CPPv411_rtc_time_t "_rtc_time_t") rtc\_time\_t

<a id="_CPPv413pfunc_intr_cb"></a>

<a id="_CPPv313pfunc_intr_cb"></a> <a id="_CPPv213pfunc_intr_cb"></a> <a id="pfunc_intr_cb"></a> <a id="drv__rtc_8h_1a76f0528ee94471b1a4e523a1d01b6cba"></a> typedef void (\*pfunc\_intr\_cb)([rtc\_time\_t](#_CPPv410rtc_time_t "rtc_time_t") \*pt\_time)
