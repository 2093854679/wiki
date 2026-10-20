---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_timer.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-timer"></a>

# DRV\_TIMER

<a id="drv-timer-api-status"></a>

## DRV\_TIMER API Status

| API |
| --- |
| [`drv_timer_reg_callback()`](#_CPPv422drv_timer_reg_callback8uint32_t8uint32_t14pfunc_tmr_cb_tPv "drv_timer_reg_callback") |
| [`drv_timer_start()`](#_CPPv415drv_timer_start8uint32_t8uint32_t15drv_tmr_count_e8uint32_t "drv_timer_start") |
| [`drv_timer_enable_interrupt()`](#_CPPv426drv_timer_enable_interrupt8uint32_t8uint32_tb "drv_timer_enable_interrupt") |
| [`drv_timer_stop()`](#_CPPv414drv_timer_stop8uint32_t8uint32_t "drv_timer_stop") |
| [`drv_timer_get_curr_tick()`](#_CPPv423drv_timer_get_curr_tick8uint32_t8uint32_t "drv_timer_get_curr_tick") |
| [`drv_timer_delay_us()`](#_CPPv418drv_timer_delay_us8uint32_t "drv_timer_delay_us") |

<a id="drv-timer-api-reference"></a>

## DRV\_TIMER API Reference

<a id="header-file"></a>

### Header File

- [driver/timer/drv\_timer.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/timer/drv_timer.h)

<a id="functions"></a>

### Functions

<a id="_CPPv422drv_timer_reg_callback8uint32_t8uint32_t14pfunc_tmr_cb_tPv"></a>

<a id="_CPPv322drv_timer_reg_callback8uint32_t8uint32_t14pfunc_tmr_cb_tPv"></a> <a id="_CPPv222drv_timer_reg_callback8uint32_t8uint32_t14pfunc_tmr_cb_tPv"></a> <a id="drv_timer_reg_callback__uint32_t.uint32_t.pfunc_tmr_cb_t.voidP"></a> <a id="drv__timer_8h_1ad1fc392a25ad4b062415df33e0e59493"></a> int32\_t drv\_timer\_reg\_callback(uint32\_t dev\_index, uint32\_t sub\_tmr\_index, [pfunc\_tmr\_cb\_t](#_CPPv414pfunc_tmr_cb_t "pfunc_tmr_cb_t") pfn\_cb, void \*pv\_arg)
:   register timer interrupt callback.

    注册子timer的中断处理函数

    参数:
    :   - **dev\_index** – **\[in\]** 设备index, 0: AON timer(32K) 1: APB timer(2M)
        - **sub\_tmr\_index** – **\[in\]** 子timer index, from 0 and less than TMR\_SUB\_TIMER\_NUM
        - **pfn\_cb** – **\[in\]** timer中断发生时需要调用的callback
        - **pv\_arg** – **\[in\]** callback带的参数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv415drv_timer_start8uint32_t8uint32_t15drv_tmr_count_e8uint32_t"></a>

<a id="_CPPv315drv_timer_start8uint32_t8uint32_t15drv_tmr_count_e8uint32_t"></a> <a id="_CPPv215drv_timer_start8uint32_t8uint32_t15drv_tmr_count_e8uint32_t"></a> <a id="drv_timer_start__uint32_t.uint32_t.drv_tmr_count_e.uint32_t"></a> <a id="drv__timer_8h_1a6f5c0cd086a544efc34d72bc71fcbec5"></a> int32\_t drv\_timer\_start(uint32\_t dev\_index, uint32\_t sub\_tmr\_index, [drv\_tmr\_count\_e](#_CPPv415drv_tmr_count_e "drv_tmr_count_e") e\_count\_dir, uint32\_t expire\_tick\_count)
:   start or restart a timer.

    启动一个timer，如果timer已经启动，则会表现为使用新的参数重新配置timer 如果timer的超时时间太短，建议先进行中断函数的配置

    参数:
    :   - **dev\_index** – **\[in\]** 设备index, 0: AON timer(32K) 1: APB timer(2M)
        - **sub\_tmr\_index** – **\[in\]** 子timer index, from 0 and less than TMR\_SUB\_TIMER\_NUM
        - **e\_count\_dir** – **\[in\]** 设置计数反向，see drv\_tmr\_count\_e
        - **expire\_tick\_count** – **\[in\]** 超时的tick，应该需要使用 DRV\_TMR\_GET\_CLK\_FREQ() 来计算设置的值

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426drv_timer_enable_interrupt8uint32_t8uint32_tb"></a>

<a id="_CPPv326drv_timer_enable_interrupt8uint32_t8uint32_tb"></a> <a id="_CPPv226drv_timer_enable_interrupt8uint32_t8uint32_tb"></a> <a id="drv_timer_enable_interrupt__uint32_t.uint32_t.b"></a> <a id="drv__timer_8h_1af3b6ba33e9f8f28d662ef2686d572747"></a> int32\_t drv\_timer\_enable\_interrupt(uint32\_t dev\_index, uint32\_t sub\_tmr\_index, bool enable)
:   enable or disable interrupt.

    收到开关对应timer的中断，注册中断的时候会自动打开中断

    参数:
    :   - **dev\_index** – **\[in\]** 设备index, 0: AON timer(32K) 1: APB timer(2M)
        - **sub\_tmr\_index** – **\[in\]** 子timer index, from 0 and less than TMR\_SUB\_TIMER\_NUM
        - **enable** – **\[in\]** true: enable false: disable

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv414drv_timer_stop8uint32_t8uint32_t"></a>

<a id="_CPPv314drv_timer_stop8uint32_t8uint32_t"></a> <a id="_CPPv214drv_timer_stop8uint32_t8uint32_t"></a> <a id="drv_timer_stop__uint32_t.uint32_t"></a> <a id="drv__timer_8h_1ab9bcc5fc4979fcb8f7530580099219fc"></a> int32\_t drv\_timer\_stop(uint32\_t dev\_index, uint32\_t sub\_tmr\_index)
:   stop a timer.

    停止一个timer，不使用timer的时候调用

    参数:
    :   - **dev\_index** – **\[in\]** 设备index, 0: AON timer(32K) 1: APB timer(2M)
        - **sub\_tmr\_index** – **\[in\]** 子timer index, from 0 and less than TMR\_SUB\_TIMER\_NUM

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv423drv_timer_get_curr_tick8uint32_t8uint32_t"></a>

<a id="_CPPv323drv_timer_get_curr_tick8uint32_t8uint32_t"></a> <a id="_CPPv223drv_timer_get_curr_tick8uint32_t8uint32_t"></a> <a id="drv_timer_get_curr_tick__uint32_t.uint32_t"></a> <a id="drv__timer_8h_1a660f57c4645cc2f23ef473da6cc6f2d0"></a> uint32\_t drv\_timer\_get\_curr\_tick(uint32\_t dev\_index, uint32\_t sub\_tmr\_index)
:   get the current tick of the select timer.

    获取timer的当前的计数值

    参数:
    :   - **dev\_index** – **\[in\]** 设备index, 0: AON timer(32K) 1: APB timer(2M)
        - **sub\_tmr\_index** – **\[in\]** 子timer index, from 0 and less than TMR\_SUB\_TIMER\_NUM

    返回:
    :   the current tick

<a id="_CPPv418drv_timer_delay_us8uint32_t"></a>

<a id="_CPPv318drv_timer_delay_us8uint32_t"></a> <a id="_CPPv218drv_timer_delay_us8uint32_t"></a> <a id="drv_timer_delay_us__uint32_t"></a> <a id="drv__timer_8h_1afebd8ba4b651788c4dda08d4c6118455"></a> void drv\_timer\_delay\_us(uint32\_t us)
:   delay us.

    使用apb timer用来做us的delay

    参数:
    :   **us** – **\[in\]** delay的us数值, \<\= 50

    返回:
    :   N/A

<a id="macros"></a>

### Macros

<a id="c.TMR_DEVICE_NUM"></a>

<a id="drv__timer_8h_1ae79f9d9b1f5ddbea9f7846c562914afd"></a> TMR\_DEVICE\_NUM

<a id="c.TMR_INDEX_AON_TIMER"></a>

<a id="drv__timer_8h_1a9b6ebea51404023496f2bff121c28cff"></a> TMR\_INDEX\_AON\_TIMER

<a id="c.TMR_INDEX_APB_TIMER"></a>

<a id="drv__timer_8h_1a7a45e4c633c4d37eb06b88df3459f22a"></a> TMR\_INDEX\_APB\_TIMER

<a id="c.TMR_SUB_TIMER_NUM"></a>

<a id="drv__timer_8h_1a7e36099616421acfc324d699d40ebf65"></a> TMR\_SUB\_TIMER\_NUM

<a id="c.SUB_TIMER_INDEX_freerun"></a>

<a id="drv__timer_8h_1aae42842587a54c71ee5faa9bbdba9111"></a> SUB\_TIMER\_INDEX\_freerun

<a id="c.DRV_TMR_GET_CLK_FREQ"></a>

<a id="drv__timer_8h_1aefde9247a34ad147eaac50ad8e2ca2ea"></a> DRV\_TMR\_GET\_CLK\_FREQ(dev\_index)

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv415drv_tmr_count_e"></a>

<a id="_CPPv315drv_tmr_count_e"></a> <a id="_CPPv215drv_tmr_count_e"></a> <a id="drv_tmr_count_e"></a> <a id="drv__timer_8h_1a5c5e32708dc4b379fcc38f08f535042c"></a> typedef enum [\_drv\_tmr\_count\_e](#_CPPv416_drv_tmr_count_e "_drv_tmr_count_e") drv\_tmr\_count\_e

<a id="_CPPv414pfunc_tmr_cb_t"></a>

<a id="_CPPv314pfunc_tmr_cb_t"></a> <a id="_CPPv214pfunc_tmr_cb_t"></a> <a id="pfunc_tmr_cb_t"></a> <a id="drv__timer_8h_1ab4b1331f5b2322359b9b518dca807006"></a> typedef void (\*pfunc\_tmr\_cb\_t)(uint32\_t dev\_index, uint32\_t sub\_tmr\_index, void \*pv\_arg)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv416_drv_tmr_count_e"></a>

<a id="_CPPv316_drv_tmr_count_e"></a> <a id="_CPPv216_drv_tmr_count_e"></a> <a id="drv__timer_8h_1a26024cf8a9eb860e5b15d359e3843351"></a> enum \_drv\_tmr\_count\_e
:   *Values:*

    <a id="_CPPv4N16_drv_tmr_count_e25DRV_TIMR_COUNT_DECREASINGE"></a>

    <a id="_CPPv3N16_drv_tmr_count_e25DRV_TIMR_COUNT_DECREASINGE"></a> <a id="_CPPv2N16_drv_tmr_count_e25DRV_TIMR_COUNT_DECREASINGE"></a> <a id="drv__timer_8h_1a26024cf8a9eb860e5b15d359e3843351ac98f0bdfc2dd7bb5386e1135f8971141"></a> enumerator DRV\_TIMR\_COUNT\_DECREASING

    <a id="_CPPv4N16_drv_tmr_count_e25DRV_TIMR_COUNT_INCREASINGE"></a>

    <a id="_CPPv3N16_drv_tmr_count_e25DRV_TIMR_COUNT_INCREASINGE"></a> <a id="_CPPv2N16_drv_tmr_count_e25DRV_TIMR_COUNT_INCREASINGE"></a> <a id="drv__timer_8h_1a26024cf8a9eb860e5b15d359e3843351a517dff26e3c95c5b068cf717eedb198c"></a> enumerator DRV\_TIMR\_COUNT\_INCREASING
    :   递减计数方式
