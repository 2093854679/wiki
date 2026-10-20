---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/component/bk_timer.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk-timer"></a>

# BK\_TIMER

<a id="bk-timer-api-status"></a>

## BK\_TIMER API Status

| API |
| --- |
| [`bk_timer_create()`](#_CPPv415bk_timer_create16pfunc_bk_timer_tPv8uint32_t "bk_timer_create") |
| [`bk_timer_start_periodic()`](#_CPPv423bk_timer_start_periodic8uint32_t8uint32_t "bk_timer_start_periodic") |
| [`bk_timer_start_once()`](#_CPPv419bk_timer_start_once8uint32_t8uint32_t "bk_timer_start_once") |
| [`bk_timer_stop()`](#_CPPv413bk_timer_stop8uint32_t "bk_timer_stop") |
| [`bk_timer_destroy()`](#_CPPv416bk_timer_destroy8uint32_t "bk_timer_destroy") |

<a id="bk-timer-api-reference"></a>

## BK\_TIMER API Reference

<a id="header-file"></a>

### Header File

- [component/timer/bk\_timer.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/component/timer/bk_timer.h)

<a id="functions"></a>

### Functions

<a id="_CPPv415bk_timer_create16pfunc_bk_timer_tPv8uint32_t"></a>

<a id="_CPPv315bk_timer_create16pfunc_bk_timer_tPv8uint32_t"></a> <a id="_CPPv215bk_timer_create16pfunc_bk_timer_tPv8uint32_t"></a> <a id="bk_timer_create__pfunc_bk_timer_t.voidP.uint32_t"></a> <a id="bk__timer_8h_1ab76440cd6f069817d6d478fde5a01c8d"></a> uint32\_t bk\_timer\_create([pfunc\_bk\_timer\_t](#_CPPv416pfunc_bk_timer_t "pfunc_bk_timer_t") pfn\_timer\_func, void \*pv\_arg, uint32\_t caller\_addr)
:   create a timer.

    创建一个timer,即超时后会执行pfn\_timer\_func

    参见

    [bk\_timer\_destroy()](#bk__timer_8h_1a1f00791eb2d39955f7d66bec1aaaa8a2) 来销毁创建的timer

    备注

    该timer在xtal 26M被关闭的时候会停止跳动

    参数:
    :   - **pfn\_timer\_func** – **\[in\]** timer执行函数
        - **pv\_arg** – **\[in\]** timer执行函数的参数
        - **caller\_addr** – **\[in\]** caller address, 不清楚时可以传0

    返回值:
    :   - **0** – fail
        - **other** – success

    返回:
    :   timer handle

<a id="_CPPv423bk_timer_start_periodic8uint32_t8uint32_t"></a>

<a id="_CPPv323bk_timer_start_periodic8uint32_t8uint32_t"></a> <a id="_CPPv223bk_timer_start_periodic8uint32_t8uint32_t"></a> <a id="bk_timer_start_periodic__uint32_t.uint32_t"></a> <a id="bk__timer_8h_1af735d893792557062e6a453bb04d737e"></a> int32\_t bk\_timer\_start\_periodic(uint32\_t timer\_handle, uint32\_t timeout\_half\_us)
:   start a periodic timer.

    启动一个周期性的timer

    参见

    [bk\_timer\_stop()](#bk__timer_8h_1a903a54e8dbeedb3e68052c0562523268)

    参数:
    :   - **timer\_handle** – **\[in\]** [bk\_timer\_create()](#bk__timer_8h_1ab76440cd6f069817d6d478fde5a01c8d)的返回值
        - **timeout\_half\_us** – **\[in\]** 周期时间,单位是 0.5us

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419bk_timer_start_once8uint32_t8uint32_t"></a>

<a id="_CPPv319bk_timer_start_once8uint32_t8uint32_t"></a> <a id="_CPPv219bk_timer_start_once8uint32_t8uint32_t"></a> <a id="bk_timer_start_once__uint32_t.uint32_t"></a> <a id="bk__timer_8h_1a5742546c7e168dab9fb91de4dec2f415"></a> int32\_t bk\_timer\_start\_once(uint32\_t timer\_handle, uint32\_t timeout\_half\_us)
:   start a timer only once.

    启动一个一次性的timer

    参见

    [bk\_timer\_stop()](#bk__timer_8h_1a903a54e8dbeedb3e68052c0562523268)

    参数:
    :   - **timer\_handle** – **\[in\]** [bk\_timer\_create()](#bk__timer_8h_1ab76440cd6f069817d6d478fde5a01c8d)的返回值
        - **timeout\_half\_us** – **\[in\]** 超时时间,单位是 0.5us

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv413bk_timer_stop8uint32_t"></a>

<a id="_CPPv313bk_timer_stop8uint32_t"></a> <a id="_CPPv213bk_timer_stop8uint32_t"></a> <a id="bk_timer_stop__uint32_t"></a> <a id="bk__timer_8h_1a903a54e8dbeedb3e68052c0562523268"></a> int32\_t bk\_timer\_stop(uint32\_t timer\_handle)
:   stop a timer.

    停止一个timer，后面可以通过调用bk\_timer\_start\_xxx()再次启动

    参数:
    :   **timer\_handle** – **\[in\]** [bk\_timer\_create()](#bk__timer_8h_1ab76440cd6f069817d6d478fde5a01c8d)的返回值

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416bk_timer_destroy8uint32_t"></a>

<a id="_CPPv316bk_timer_destroy8uint32_t"></a> <a id="_CPPv216bk_timer_destroy8uint32_t"></a> <a id="bk_timer_destroy__uint32_t"></a> <a id="bk__timer_8h_1a1f00791eb2d39955f7d66bec1aaaa8a2"></a> int32\_t bk\_timer\_destroy(uint32\_t timer\_handle)
:   destroy a timer.

    销毁一个timer，不再使用该timer的时候应该调用该函数

    参见

    [bk\_timer\_create()](#bk__timer_8h_1ab76440cd6f069817d6d478fde5a01c8d)

    参数:
    :   **timer\_handle** – **\[in\]** [bk\_timer\_create()](#bk__timer_8h_1ab76440cd6f069817d6d478fde5a01c8d)的返回值

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv416pfunc_bk_timer_t"></a>

<a id="_CPPv316pfunc_bk_timer_t"></a> <a id="_CPPv216pfunc_bk_timer_t"></a> <a id="pfunc_bk_timer_t"></a> <a id="bk__timer_8h_1a7ef751ee581d8e94d6efba756e850518"></a> typedef int32\_t (\*pfunc\_bk\_timer\_t)(void \*pv\_arg)
