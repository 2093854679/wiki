---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/component/bk_uart.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk-uart"></a>

# BK\_UART

<a id="bk-uart-api-status"></a>

## BK\_UART API Status

| API |
| --- |
| [`bk_uart_open()`](#_CPPv412bk_uart_open8uint32_t "bk_uart_open") |
| [`bk_uart_close()`](#_CPPv413bk_uart_close8uint32_t "bk_uart_close") |
| [`bk_uart_config()`](#_CPPv414bk_uart_config8uint32_tP13bk_uart_cfg_t "bk_uart_config") |
| [`bk_uart_start()`](#_CPPv413bk_uart_start8uint32_t "bk_uart_start") |
| [`bk_uart_stop()`](#_CPPv412bk_uart_stop8uint32_t "bk_uart_stop") |
| [`bk_uart_write()`](#_CPPv413bk_uart_write8uint32_tP7uint8_t8uint16_t18pfunc_bk_uart_cb_t "bk_uart_write") |
| [`bk_uart_read()`](#_CPPv412bk_uart_read8uint32_tP7uint8_t8uint16_t18pfunc_bk_uart_cb_t "bk_uart_read") |

<a id="bk-uart-api-reference"></a>

## BK\_UART API Reference

<a id="header-file"></a>

### Header File

- [component/uart/bk\_uart.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/component/uart/bk_uart.h)

<a id="functions"></a>

### Functions

<a id="_CPPv412bk_uart_open8uint32_t"></a>

<a id="_CPPv312bk_uart_open8uint32_t"></a> <a id="_CPPv212bk_uart_open8uint32_t"></a> <a id="bk_uart_open__uint32_t"></a> <a id="bk__uart_8h_1af86330ac99c563641b726b621d42e64b"></a> uint32\_t bk\_uart\_open(uint32\_t dev\_index)
:   beken uart open interface.

    提供uart open的接口,使用之前需要先open,参数是设备index，从0开始

    参数:
    :   **dev\_index** – **\[in\]** device index, from 0(the first device), \< UART\_DEVICE\_NUM

    返回值:
    :   - **0** – fail
        - **other** – success

    返回:
    :   handle

<a id="_CPPv413bk_uart_close8uint32_t"></a>

<a id="_CPPv313bk_uart_close8uint32_t"></a> <a id="_CPPv213bk_uart_close8uint32_t"></a> <a id="bk_uart_close__uint32_t"></a> <a id="bk__uart_8h_1aea8c980807674f138d8b7a0b2bd0973b"></a> int32\_t bk\_uart\_close(uint32\_t handle)
:   beken uart close.

    使用UART结束后需要close,调用前需要先 [bk\_uart\_stop()](#bk__uart_8h_1ae84f9e237f874c758bc285de73ebd6fe)

    参数:
    :   **handle** – **\[in\]** return value of [bk\_uart\_open()](#bk__uart_8h_1af86330ac99c563641b726b621d42e64b)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv414bk_uart_config8uint32_tP13bk_uart_cfg_t"></a>

<a id="_CPPv314bk_uart_config8uint32_tP13bk_uart_cfg_t"></a> <a id="_CPPv214bk_uart_config8uint32_tP13bk_uart_cfg_t"></a> <a id="bk_uart_config__uint32_t.bk_uart_cfg_tP"></a> <a id="bk__uart_8h_1ade2d5f342c5ba3372067e877f174f3d4"></a> int32\_t bk\_uart\_config(uint32\_t handle, [bk\_uart\_cfg\_t](#_CPPv413bk_uart_cfg_t "bk_uart_cfg_t") \*pt\_cfg)
:   uart config interface.

    在 [bk\_uart\_start()](#bk__uart_8h_1adfeb8d1081e130d6bd5b5ac53f679c3e) 之前需要先进行相关参数的配置

    参数:
    :   - **handle** – **\[in\]** return value of [bk\_uart\_open()](#bk__uart_8h_1af86330ac99c563641b726b621d42e64b)
        - **pt\_cfg** – **\[in\]** pointer to the config struct

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv413bk_uart_start8uint32_t"></a>

<a id="_CPPv313bk_uart_start8uint32_t"></a> <a id="_CPPv213bk_uart_start8uint32_t"></a> <a id="bk_uart_start__uint32_t"></a> <a id="bk__uart_8h_1adfeb8d1081e130d6bd5b5ac53f679c3e"></a> int32\_t bk\_uart\_start(uint32\_t handle)
:   beken uart start.

    start uart function after config uart parameter

    参数:
    :   **handle** – **\[in\]** return value of [bk\_uart\_open()](#bk__uart_8h_1af86330ac99c563641b726b621d42e64b)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv412bk_uart_stop8uint32_t"></a>

<a id="_CPPv312bk_uart_stop8uint32_t"></a> <a id="_CPPv212bk_uart_stop8uint32_t"></a> <a id="bk_uart_stop__uint32_t"></a> <a id="bk__uart_8h_1ae84f9e237f874c758bc285de73ebd6fe"></a> int32\_t bk\_uart\_stop(uint32\_t handle)
:   beken uart stop.

    stop uart function, 和 [bk\_uart\_start()](#bk__uart_8h_1adfeb8d1081e130d6bd5b5ac53f679c3e) 的动作相反

    参数:
    :   **handle** – **\[in\]** return value of [bk\_uart\_open()](#bk__uart_8h_1af86330ac99c563641b726b621d42e64b)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv413bk_uart_write8uint32_tP7uint8_t8uint16_t18pfunc_bk_uart_cb_t"></a>

<a id="_CPPv313bk_uart_write8uint32_tP7uint8_t8uint16_t18pfunc_bk_uart_cb_t"></a> <a id="_CPPv213bk_uart_write8uint32_tP7uint8_t8uint16_t18pfunc_bk_uart_cb_t"></a> <a id="bk_uart_write__uint32_t.uint8_tP.uint16_t.pfunc_bk_uart_cb_t"></a> <a id="bk__uart_8h_1a4b4b97f396c2988d84e33bc95697936d"></a> int32\_t bk\_uart\_write(uint32\_t handle, uint8\_t \*pu1\_buf, uint16\_t buf\_len, [pfunc\_bk\_uart\_cb\_t](#_CPPv418pfunc_bk_uart_cb_t "pfunc_bk_uart_cb_t") pfn\_cb)
:   beken uart write interface.

    使用UART来发送一些数据出去,如果pfn\_cb\=\=NULL，则该函数在把数据通过uart送出去后才会返回 如果pfn\_cb!\=NULL，该函数会立即返回，等数据发送出去后通过 pfn\_cb进行通知

    参数:
    :   - **handle** – **\[in\]** return value of [bk\_uart\_open()](#bk__uart_8h_1af86330ac99c563641b726b621d42e64b)
        - **pu1\_buf** – **\[in\]** pointer to the send buffer
        - **buf\_len** – **\[in\]** send buffer length in bytes
        - **pfn\_cb** – **\[in\]** callback function for async send. it can be NULL if you do not want async send

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv412bk_uart_read8uint32_tP7uint8_t8uint16_t18pfunc_bk_uart_cb_t"></a>

<a id="_CPPv312bk_uart_read8uint32_tP7uint8_t8uint16_t18pfunc_bk_uart_cb_t"></a> <a id="_CPPv212bk_uart_read8uint32_tP7uint8_t8uint16_t18pfunc_bk_uart_cb_t"></a> <a id="bk_uart_read__uint32_t.uint8_tP.uint16_t.pfunc_bk_uart_cb_t"></a> <a id="bk__uart_8h_1a9086eee93f509a58f6e7e5f0f87b44eb"></a> int32\_t bk\_uart\_read(uint32\_t handle, uint8\_t \*pu1\_buf, uint16\_t buf\_len, [pfunc\_bk\_uart\_cb\_t](#_CPPv418pfunc_bk_uart_cb_t "pfunc_bk_uart_cb_t") pfn\_cb)
:   beken uart read interface.

    使用UART收一些数据回来,如果pfn\_cb\=\=NULL，则该函数从uart收完数据后才会返回 如果pfn\_cb!\=NULL，该函数会立即返回，等后面数据收完后通过 pfn\_cb进行通知

    参数:
    :   - **handle** – **\[in\]** return value of [bk\_uart\_open()](#bk__uart_8h_1af86330ac99c563641b726b621d42e64b)
        - **pu1\_buf** – **\[in\]** pointer to the receive buffer
        - **buf\_len** – **\[in\]** receive buffer length in bytes
        - **pfn\_cb** – **\[in\]** callback function for async recevie. it can be NULL if you do not want async recevie

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422bk_uart_get_drv_handle8uint32_t"></a>

<a id="_CPPv322bk_uart_get_drv_handle8uint32_t"></a> <a id="_CPPv222bk_uart_get_drv_handle8uint32_t"></a> <a id="bk_uart_get_drv_handle__uint32_t"></a> <a id="bk__uart_8h_1a67a8623fe676dfe2cfe87fe03d373dc5"></a> uint32\_t bk\_uart\_get\_drv\_handle(uint32\_t handle)
:   get drv uart handle

    使用BK uart的handle找到驱动的handle

    参数:
    :   **handle** – **\[in\]** return value of [bk\_uart\_open()](#bk__uart_8h_1af86330ac99c563641b726b621d42e64b)

    返回:
    :   drv uart handle

<a id="structures"></a>

### Structures

<a id="_CPPv414_bk_uart_cfg_t"></a>

<a id="_CPPv314_bk_uart_cfg_t"></a> <a id="_CPPv214_bk_uart_cfg_t"></a> <a id="_bk_uart_cfg_t"></a> <a id="struct__bk__uart__cfg__t"></a> struct \_bk\_uart\_cfg\_t

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv418pfunc_bk_uart_cb_t"></a>

<a id="_CPPv318pfunc_bk_uart_cb_t"></a> <a id="_CPPv218pfunc_bk_uart_cb_t"></a> <a id="pfunc_bk_uart_cb_t"></a> <a id="bk__uart_8h_1abb77dbf194af62781b32941f3d7a6f65"></a> typedef void (\*pfunc\_bk\_uart\_cb\_t)(uint32\_t handle, uint8\_t \*pu1\_buf, uint16\_t buf\_len)

<a id="_CPPv413bk_uart_cfg_t"></a>

<a id="_CPPv313bk_uart_cfg_t"></a> <a id="_CPPv213bk_uart_cfg_t"></a> <a id="bk_uart_cfg_t"></a> <a id="bk__uart_8h_1a09c5d8e9c8bd8a7164d57f99b75d497e"></a> typedef struct [\_bk\_uart\_cfg\_t](#_CPPv414_bk_uart_cfg_t "_bk_uart_cfg_t") bk\_uart\_cfg\_t
