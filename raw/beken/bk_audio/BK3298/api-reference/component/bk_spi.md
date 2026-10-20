---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/component/bk_spi.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk24"></a>

# BK24

<a id="spi-api-status"></a>

## SPI API Status

| API |
| --- |
| [`bk_spi_open()`](#_CPPv411bk_spi_open8uint32_t "bk_spi_open") |
| [`bk_spi_close()`](#_CPPv412bk_spi_close8uint32_t "bk_spi_close") |
| [`bk_spi_get_default_config()`](#_CPPv425bk_spi_get_default_configP12spi_config_t "bk_spi_get_default_config") |
| [`bk_spi_config()`](#_CPPv413bk_spi_config8uint32_tP12spi_config_t "bk_spi_config") |
| [`bk_spi_write()`](#_CPPv412bk_spi_write8uint32_tP7uint8_t8uint32_t17pfunc_bk_spi_cb_tPv "bk_spi_write") |
| [`bk_spi_read()`](#_CPPv411bk_spi_read8uint32_tP7uint8_t8uint32_t17pfunc_bk_spi_cb_tPv "bk_spi_read") |
| [`bk_spi_transmit()`](#_CPPv415bk_spi_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t17pfunc_bk_spi_cb_tPv "bk_spi_transmit") |

<a id="spi-api-reference"></a>

## SPI API Reference

<a id="header-file"></a>

### Header File

- [component/spi/bk\_spi.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/component/spi/bk_spi.h)

<a id="functions"></a>

### Functions

<a id="_CPPv411bk_spi_open8uint32_t"></a>

<a id="_CPPv311bk_spi_open8uint32_t"></a> <a id="_CPPv211bk_spi_open8uint32_t"></a> <a id="bk_spi_open__uint32_t"></a> <a id="bk__spi_8h_1a927ced0d805d49788e7d8508cbf4027e"></a> int32\_t bk\_spi\_open(uint32\_t dev\_index)
:   beken spi open interface.

    提供spi open的接口,使用之前需要先open,参数是设备index，从0开始

    参数:
    :   **dev\_index** – **\[in\]** device index, from 0(the first device), \< [SPI\_DEVICE\_NUM](../driver/drv_spi.md#drv__spi_8h_1aec9518e431ecf70a6837c47752c7e5da)

    返回值:
    :   - **0** – fail
        - **other** – success

    返回:
    :   handle

<a id="_CPPv412bk_spi_close8uint32_t"></a>

<a id="_CPPv312bk_spi_close8uint32_t"></a> <a id="_CPPv212bk_spi_close8uint32_t"></a> <a id="bk_spi_close__uint32_t"></a> <a id="bk__spi_8h_1af4dc1830c4145b3a3fd2148c3a947a1f"></a> int32\_t bk\_spi\_close(uint32\_t dev\_index)
:   beken uart close.

    使用SPI结束后需要close,调用前需要先 [bk\_uart\_stop()](bk_uart.md#bk__uart_8h_1ae84f9e237f874c758bc285de73ebd6fe)

    参数:
    :   **dev\_index** – **\[in\]** device index, from 0(the first device), \< [SPI\_DEVICE\_NUM](../driver/drv_spi.md#drv__spi_8h_1aec9518e431ecf70a6837c47752c7e5da)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425bk_spi_get_default_configP12spi_config_t"></a>

<a id="_CPPv325bk_spi_get_default_configP12spi_config_t"></a> <a id="_CPPv225bk_spi_get_default_configP12spi_config_t"></a> <a id="bk_spi_get_default_config__spi_config_tP"></a> <a id="bk__spi_8h_1a9463c4a376f7626fbbab331cf6894a3a"></a> int32\_t bk\_spi\_get\_default\_config([spi\_config\_t](../driver/drv_spi.md#_CPPv412spi_config_t "spi_config_t") \*pt\_cfg)
:   beken uart get default spi config.

    可以条用此接口获取默认的spi配置参数

    参数:
    :   **pt\_cfg** – **\[out\]** pointer to the config struct

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv413bk_spi_config8uint32_tP12spi_config_t"></a>

<a id="_CPPv313bk_spi_config8uint32_tP12spi_config_t"></a> <a id="_CPPv213bk_spi_config8uint32_tP12spi_config_t"></a> <a id="bk_spi_config__uint32_t.spi_config_tP"></a> <a id="bk__spi_8h_1a88fadc741fc966a01cfcd06ef7b324c0"></a> int32\_t bk\_spi\_config(uint32\_t dev\_index, [spi\_config\_t](../driver/drv_spi.md#_CPPv412spi_config_t "spi_config_t") \*pt\_cfg)
:   uart config interface.

    在 [bk\_uart\_start()](bk_uart.md#bk__uart_8h_1adfeb8d1081e130d6bd5b5ac53f679c3e) 之前需要先进行相关参数的配置

    参数:
    :   - **dev\_index** – **\[in\]** device index, from 0(the first device), \< [SPI\_DEVICE\_NUM](../driver/drv_spi.md#drv__spi_8h_1aec9518e431ecf70a6837c47752c7e5da)
        - **pt\_cfg** – **\[in\]** pointer to the config struct

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv412bk_spi_write8uint32_tP7uint8_t8uint32_t17pfunc_bk_spi_cb_tPv"></a>

<a id="_CPPv312bk_spi_write8uint32_tP7uint8_t8uint32_t17pfunc_bk_spi_cb_tPv"></a> <a id="_CPPv212bk_spi_write8uint32_tP7uint8_t8uint32_t17pfunc_bk_spi_cb_tPv"></a> <a id="bk_spi_write__uint32_t.uint8_tP.uint32_t.pfunc_bk_spi_cb_t.voidP"></a> <a id="bk__spi_8h_1a56049e3016ea3fd5a3ca1e5727c983b3"></a> int32\_t bk\_spi\_write(uint32\_t dev\_index, uint8\_t \*tx\_buf, uint32\_t tx\_len, [pfunc\_bk\_spi\_cb\_t](#_CPPv417pfunc_bk_spi_cb_t "pfunc_bk_spi_cb_t") pfn\_cb, void \*p\_arg)
:   beken uart write interface.

    使用SPI来发送数据,如果pfn\_cb\=\=NULL，则该函数在把数据通过SPI送出去后才会返回 如果pfn\_cb!\=NULL，该函数会立即返回，等数据发送出去后通过 pfn\_cb进行通知 发送数据长度的不能大于0xFFF

    参数:
    :   - **dev\_index** – **\[in\]** device index, from 0(the first device), \< [SPI\_DEVICE\_NUM](../driver/drv_spi.md#drv__spi_8h_1aec9518e431ecf70a6837c47752c7e5da)
        - **tx\_buf** – **\[in\]** pointer to the send buffer
        - **tx\_len** – **\[in\]** send buffer length in bytes
        - **pfn\_cb** – **\[in\]** callback function for async send. it can be NULL if you do not want async send
        - **p\_arg** – **\[in\]** callback parameter

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv411bk_spi_read8uint32_tP7uint8_t8uint32_t17pfunc_bk_spi_cb_tPv"></a>

<a id="_CPPv311bk_spi_read8uint32_tP7uint8_t8uint32_t17pfunc_bk_spi_cb_tPv"></a> <a id="_CPPv211bk_spi_read8uint32_tP7uint8_t8uint32_t17pfunc_bk_spi_cb_tPv"></a> <a id="bk_spi_read__uint32_t.uint8_tP.uint32_t.pfunc_bk_spi_cb_t.voidP"></a> <a id="bk__spi_8h_1a860678e0960186cce87151a3a7547da1"></a> int32\_t bk\_spi\_read(uint32\_t dev\_index, uint8\_t \*rx\_buf, uint32\_t rx\_len, [pfunc\_bk\_spi\_cb\_t](#_CPPv417pfunc_bk_spi_cb_t "pfunc_bk_spi_cb_t") pfn\_cb, void \*p\_arg)
:   beken uart read interface.

    使用SPI接收数据,如果pfn\_cb\=\=NULL，则该函数从SPI收完数据后才会返回 如果pfn\_cb!\=NULL，该函数会立即返回，等后面数据收完后通过 pfn\_cb进行通知 接收数据长度的不能大于0xFFF

    参数:
    :   - **dev\_index** – **\[in\]** device index, from 0(the first device), \< [SPI\_DEVICE\_NUM](../driver/drv_spi.md#drv__spi_8h_1aec9518e431ecf70a6837c47752c7e5da)
        - **rx\_buf** – **\[in\]** pointer to the receive buffer
        - **rx\_len** – **\[in\]** receive buffer length in bytes
        - **pfn\_cb** – **\[in\]** callback function for async recevie. it can be NULL if you do not want async recevie
        - **p\_arg** – **\[in\]** callback parameter

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv415bk_spi_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t17pfunc_bk_spi_cb_tPv"></a>

<a id="_CPPv315bk_spi_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t17pfunc_bk_spi_cb_tPv"></a> <a id="_CPPv215bk_spi_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t17pfunc_bk_spi_cb_tPv"></a> <a id="bk_spi_transmit__uint32_t.uint8_tP.uint32_t.uint8_tP.uint32_t.pfunc_bk_spi_cb_t.voidP"></a> <a id="bk__spi_8h_1a246538013847570d61f1d36542994610"></a> int32\_t bk\_spi\_transmit(uint32\_t dev\_index, uint8\_t \*tx\_buf, uint32\_t tx\_len, uint8\_t \*rx\_buf, uint32\_t rx\_len, [pfunc\_bk\_spi\_cb\_t](#_CPPv417pfunc_bk_spi_cb_t "pfunc_bk_spi_cb_t") pfn\_cb, void \*p\_arg)
:   beken uart transmit interface.

    使用SPI进行发送数据同时接收，如果pfn\_cb\=\=NULL，则该函数从SPI通信完成后才会返回。 如果pfn\_cb!\=NULL，该函数会立即返回，等后面通信完成后通过 pfn\_cb进行通知。 发送数据长度的不能大于0xFFF 接收数据长度的不能大于0xFFF 本接口请注意预留足够的rx buffer，并且填写正确的rx\_len

    参数:
    :   - **dev\_index** – **\[in\]** device index, from 0(the first device), \< [SPI\_DEVICE\_NUM](../driver/drv_spi.md#drv__spi_8h_1aec9518e431ecf70a6837c47752c7e5da)
        - **tx\_buf** – **\[in\]** pointer to the send buffer
        - **tx\_len** – **\[in\]** send length in bytes
        - **rx\_buf** – **\[in\]** pointer to the receive buffer
        - **rx\_len** – **\[in\]** receive length in bytes
        - **pfn\_cb** – **\[in\]** callback function for async transmit. it can be NULL if you do not want async transmit
        - **p\_arg** – **\[in\]** callback parameter

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv417pfunc_bk_spi_cb_t"></a>

<a id="_CPPv317pfunc_bk_spi_cb_t"></a> <a id="_CPPv217pfunc_bk_spi_cb_t"></a> <a id="pfunc_bk_spi_cb_t"></a> <a id="bk__spi_8h_1affeecf5b4b2fbe79b26b31c0660db422"></a> typedef void (\*pfunc\_bk\_spi\_cb\_t)(uint8\_t dev\_index, void \*p\_arg)
