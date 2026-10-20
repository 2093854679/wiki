---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/component/bk_sadc.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk-sadc"></a>

# BK\_SADC

<a id="bk-sadc-api-status"></a>

## BK\_SADC API Status

| API |
| --- |
| [`bk_sadc_open()`](#_CPPv412bk_sadc_open8uint32_t "bk_sadc_open") |
| [`bk_sadc_close()`](#_CPPv413bk_sadc_close8uint32_t "bk_sadc_close") |
| [`bk_sadc_get()`](#_CPPv411bk_sadc_get8uint32_tP13bk_sadc_blk_t "bk_sadc_get") |
| [`bk_sadc_convert_to_voltage()`](#_CPPv426bk_sadc_convert_to_voltage8uint32_t "bk_sadc_convert_to_voltage") |

<a id="bk-sadc-api-reference"></a>

## BK\_SADC API Reference

<a id="header-file"></a>

### Header File

- [component/sadc/bk\_sadc.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/component/sadc/bk_sadc.h)

<a id="functions"></a>

### Functions

<a id="_CPPv412bk_sadc_open8uint32_t"></a>

<a id="_CPPv312bk_sadc_open8uint32_t"></a> <a id="_CPPv212bk_sadc_open8uint32_t"></a> <a id="bk_sadc_open__uint32_t"></a> <a id="bk__sadc_8h_1afc3c75ce6a566a16b22e2a6c8eab2304"></a> uint32\_t bk\_sadc\_open(uint32\_t dev\_index)
:   beken SADC open.

    使用之前需要先open,参数是设备index，从0开始

    参数:
    :   **dev\_index** – **\[in\]** device index, from 0(the first device)

    返回值:
    :   - **0** – fail
        - **other** – success

    返回:
    :   handle

<a id="_CPPv413bk_sadc_close8uint32_t"></a>

<a id="_CPPv313bk_sadc_close8uint32_t"></a> <a id="_CPPv213bk_sadc_close8uint32_t"></a> <a id="bk_sadc_close__uint32_t"></a> <a id="bk__sadc_8h_1a29f9125002845b80f1bb713943b70668"></a> int32\_t bk\_sadc\_close(uint32\_t handle)
:   beken SADC close.

    使用SADC结束后需要close,和 [bk\_sadc\_open()](#bk__sadc_8h_1afc3c75ce6a566a16b22e2a6c8eab2304) 是配对的

    参数:
    :   **handle** – **\[in\]** return value of [bk\_sadc\_open()](#bk__sadc_8h_1afc3c75ce6a566a16b22e2a6c8eab2304)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv411bk_sadc_get8uint32_tP13bk_sadc_blk_t"></a>

<a id="_CPPv311bk_sadc_get8uint32_tP13bk_sadc_blk_t"></a> <a id="_CPPv211bk_sadc_get8uint32_tP13bk_sadc_blk_t"></a> <a id="bk_sadc_get__uint32_t.bk_sadc_blk_tP"></a> <a id="bk__sadc_8h_1a9b7763c9d36cc38ba0a69041590575f9"></a> int32\_t bk\_sadc\_get(uint32\_t handle, [bk\_sadc\_blk\_t](#_CPPv413bk_sadc_blk_t "bk_sadc_blk_t") \*pt\_blk)
:   beken SADC get data.

    使用SADC来接收一些采样到的数据,该函数是一个异步函数

    参数:
    :   - **handle** – **\[in\]** return value of [bk\_sadc\_open()](#bk__sadc_8h_1afc3c75ce6a566a16b22e2a6c8eab2304)
        - **pt\_blk** – **\[in\]** 指向一个接收信息的结构体。pt\_blk-\>pu2\_out指向待接收数据的buffer，其长度是 pt\_blk-\>out\_size 接收的结果会通过 pt\_blk-\>pfn\_cb 来通知

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426bk_sadc_convert_to_voltage8uint32_t"></a>

<a id="_CPPv326bk_sadc_convert_to_voltage8uint32_t"></a> <a id="_CPPv226bk_sadc_convert_to_voltage8uint32_t"></a> <a id="bk_sadc_convert_to_voltage__uint32_t"></a> <a id="bk__sadc_8h_1a91e90e877e6209daeab3472f65557197"></a> uint32\_t bk\_sadc\_convert\_to\_voltage(uint32\_t adc\_out\_data)
:   将adc采样的数据转换成输入端的毫伏电压

    备注

    该函数在callback中调用才会得到正确的值

    参数:
    :   **adc\_out\_data** – **\[in\]** adc output data

    返回:
    :   input voltage in mV

<a id="structures"></a>

### Structures

<a id="_CPPv414_bk_sadc_blk_t"></a>

<a id="_CPPv314_bk_sadc_blk_t"></a> <a id="_CPPv214_bk_sadc_blk_t"></a> <a id="_bk_sadc_blk_t"></a> <a id="struct__bk__sadc__blk__t"></a> struct \_bk\_sadc\_blk\_t

<a id="macros"></a>

### Macros

<a id="c.SADC_CHN_0_GPIO6"></a>

<a id="bk__sadc_8h_1a5905e6a1afd69de4100c9cb94bd518bb"></a> SADC\_CHN\_0\_GPIO6

<a id="c.SADC_CHN_1_VREF"></a>

<a id="bk__sadc_8h_1a9d2402e657af640999072711a5a86188"></a> SADC\_CHN\_1\_VREF

<a id="c.SADC_CHN_2_VBAT"></a>

<a id="bk__sadc_8h_1ac265f50ccf620a004fa9f223eaa3ce5a"></a> SADC\_CHN\_2\_VBAT

<a id="c.SADC_CHN_3_VTEMP"></a>

<a id="bk__sadc_8h_1ab98ee95e46d34851b50afa7561786a5d"></a> SADC\_CHN\_3\_VTEMP

<a id="c.SADC_CHN_4_HALF_VUSB"></a>

<a id="bk__sadc_8h_1a174c235fe49d2c286db83713a26863f8"></a> SADC\_CHN\_4\_HALF\_VUSB

<a id="c.SADC_CHN_5_GPIO9"></a>

<a id="bk__sadc_8h_1a9bcb276ab5e426d6832bdd54e60a5815"></a> SADC\_CHN\_5\_GPIO9

<a id="c.SADC_CHN_7_GPIO12"></a>

<a id="bk__sadc_8h_1a01a07636d6930c934275213b01889cfe"></a> SADC\_CHN\_7\_GPIO12

<a id="c.SADC_CHN_8_TOUCH"></a>

<a id="bk__sadc_8h_1a5e9d32cc7e856f7017f3594b9366adb4"></a> SADC\_CHN\_8\_TOUCH

<a id="c.SADC_CHN_9_GPIO13"></a>

<a id="bk__sadc_8h_1a38453d1536deb354144e84981453a1e1"></a> SADC\_CHN\_9\_GPIO13

<a id="c.SADC_CHN_10_GPIO14"></a>

<a id="bk__sadc_8h_1ad0318c8d1ab08d0ba03c9fb6c9e16ddf"></a> SADC\_CHN\_10\_GPIO14

<a id="c.SADC_CHN_11_GPIO15"></a>

<a id="bk__sadc_8h_1a1455ede707c3d4549e179f83f563cb7e"></a> SADC\_CHN\_11\_GPIO15

<a id="c.SADC_CHN_12_GPIO16"></a>

<a id="bk__sadc_8h_1a83ecc6482efea0fe4ab65bd65c43b3b2"></a> SADC\_CHN\_12\_GPIO16

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv418pfunc_bk_sadc_cb_t"></a>

<a id="_CPPv318pfunc_bk_sadc_cb_t"></a> <a id="_CPPv218pfunc_bk_sadc_cb_t"></a> <a id="pfunc_bk_sadc_cb_t"></a> <a id="bk__sadc_8h_1abe2ce5245b07298f54b233a7409f7ffc"></a> typedef void (\*pfunc\_bk\_sadc\_cb\_t)(uint32\_t handle, int32\_t err\_code, void \*pv\_arg)

<a id="_CPPv413bk_sadc_blk_t"></a>

<a id="_CPPv313bk_sadc_blk_t"></a> <a id="_CPPv213bk_sadc_blk_t"></a> <a id="bk_sadc_blk_t"></a> <a id="bk__sadc_8h_1a99699a940091b5f90634ffa392023ae5"></a> typedef struct [\_bk\_sadc\_blk\_t](#_CPPv414_bk_sadc_blk_t "_bk_sadc_blk_t") bk\_sadc\_blk\_t
