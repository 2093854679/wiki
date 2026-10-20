---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/component/bk_temperature.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk-temperature"></a>

# BK\_TEMPERATURE

<a id="bk-temperature-api-status"></a>

## BK\_TEMPERATURE API Status

| API |
| --- |
| [`bk_temp_open()`](#_CPPv412bk_temp_open8uint32_t "bk_temp_open") |
| [`bk_temp_close()`](#_CPPv413bk_temp_close8uint32_t "bk_temp_close") |
| [`bk_temp_get()`](#_CPPv411bk_temp_get8uint32_tb18pfunc_bk_temp_cb_tPv "bk_temp_get") |

<a id="bk-temperature-api-reference"></a>

## BK\_TEMPERATURE API Reference

<a id="header-file"></a>

### Header File

- [component/temperature/bk\_temperature.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/component/temperature/bk_temperature.h)

<a id="functions"></a>

### Functions

<a id="_CPPv412bk_temp_open8uint32_t"></a>

<a id="_CPPv312bk_temp_open8uint32_t"></a> <a id="_CPPv212bk_temp_open8uint32_t"></a> <a id="bk_temp_open__uint32_t"></a> <a id="bk__temperature_8h_1aa1b6c5eb0984cabb57d947bb08152bfb"></a> uint32\_t bk\_temp\_open(uint32\_t dev\_index)
:   beken temperature open.

    使用之前需要先open,参数是设备index，从0开始

    参数:
    :   **dev\_index** – **\[in\]** device index, from 0(the first device)

    返回值:
    :   - **0** – fail
        - **other** – success

    返回:
    :   handle

<a id="_CPPv413bk_temp_close8uint32_t"></a>

<a id="_CPPv313bk_temp_close8uint32_t"></a> <a id="_CPPv213bk_temp_close8uint32_t"></a> <a id="bk_temp_close__uint32_t"></a> <a id="bk__temperature_8h_1afa65fec44f1dae7ac1b91a54857da7a1"></a> int32\_t bk\_temp\_close(uint32\_t handle)
:   beken temperature close.

    使用 temperature 结束后需要close,和 [bk\_temp\_open()](#bk__temperature_8h_1aa1b6c5eb0984cabb57d947bb08152bfb) 是配对的

    参数:
    :   **handle** – **\[in\]** return value of [bk\_temp\_open()](#bk__temperature_8h_1aa1b6c5eb0984cabb57d947bb08152bfb)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv411bk_temp_get8uint32_tb18pfunc_bk_temp_cb_tPv"></a>

<a id="_CPPv311bk_temp_get8uint32_tb18pfunc_bk_temp_cb_tPv"></a> <a id="_CPPv211bk_temp_get8uint32_tb18pfunc_bk_temp_cb_tPv"></a> <a id="bk_temp_get__uint32_t.b.pfunc_bk_temp_cb_t.voidP"></a> <a id="bk__temperature_8h_1ae097e5d1aecaf28c21ee98c0304e4be0"></a> int32\_t bk\_temp\_get(uint32\_t handle, bool smoothing, [pfunc\_bk\_temp\_cb\_t](#_CPPv418pfunc_bk_temp_cb_t "pfunc_bk_temp_cb_t") pfn\_cb, void \*pv\_arg)
:   beken temperature get data.

    获取一次当前的温度信息,该函数是一个异步函数，温度结果是 pfunc\_bk\_temp\_cb\_t 的参数temp

    参数:
    :   - **handle** – **\[in\]** return value of [bk\_temp\_open()](#bk__temperature_8h_1aa1b6c5eb0984cabb57d947bb08152bfb)
        - **smoothing** – **\[in\]** 是否做平滑处理
        - **pfn\_cb** – **\[in\]** 通知结果的callback
        - **pv\_arg** – **\[in\]** callback的参数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv418pfunc_bk_temp_cb_t"></a>

<a id="_CPPv318pfunc_bk_temp_cb_t"></a> <a id="_CPPv218pfunc_bk_temp_cb_t"></a> <a id="pfunc_bk_temp_cb_t"></a> <a id="bk__temperature_8h_1af2902bd3ff8ab534a5ee09c2f3974ffc"></a> typedef void (\*pfunc\_bk\_temp\_cb\_t)(uint32\_t handle, uint16\_t temp, void \*pv\_arg)
