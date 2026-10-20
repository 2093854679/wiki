---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_spi.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-spi"></a>

# DRV\_SPI

<a id="drv-spi-api-status"></a>

## DRV\_SPI API Status

| API |
| --- |
| [`drv_spi_init()`](#_CPPv412drv_spi_init7uint8_t "drv_spi_init") |
| [`drv_spi_deinit()`](#_CPPv414drv_spi_deinit8uint32_t "drv_spi_deinit") |
| [`drv_spi_config()`](#_CPPv414drv_spi_config8uint32_tP12spi_config_t "drv_spi_config") |
| [`drv_spi_set_enable()`](#_CPPv418drv_spi_set_enable8uint32_t7uint8_t "drv_spi_set_enable") |
| [`drv_spi_register_tx_finish_cbk()`](#_CPPv430drv_spi_register_tx_finish_cbk8uint32_t14pfunc_spi_cb_tPv "drv_spi_register_tx_finish_cbk") |
| [`drv_spi_register_rx_finish_cbk()`](#_CPPv430drv_spi_register_rx_finish_cbk8uint32_t14pfunc_spi_cb_tPv "drv_spi_register_rx_finish_cbk") |
| [`drv_spi_register_slv_cs_release_cbk()`](#_CPPv435drv_spi_register_slv_cs_release_cbk8uint32_t25pfunc_spi_cs_release_cb_tPv "drv_spi_register_slv_cs_release_cbk") |
| [`drv_spi_unregister_tx_finish_cbk()`](#_CPPv432drv_spi_unregister_tx_finish_cbk8uint32_t "drv_spi_unregister_tx_finish_cbk") |
| [`drv_spi_unregister_rx_finish_cbk()`](#_CPPv432drv_spi_unregister_rx_finish_cbk8uint32_t "drv_spi_unregister_rx_finish_cbk") |
| [`drv_spi_unregister_slv_cs_release_cbk()`](#_CPPv437drv_spi_unregister_slv_cs_release_cbk8uint32_t "drv_spi_unregister_slv_cs_release_cbk") |
| [`drv_spi_tx_clr()`](#_CPPv414drv_spi_tx_clr8uint32_t "drv_spi_tx_clr") |
| [`drv_spi_rx_clr()`](#_CPPv414drv_spi_rx_clr8uint32_t "drv_spi_rx_clr") |
| [`drv_spi_tx()`](#_CPPv410drv_spi_tx8uint32_tP7uint8_t8uint32_t "drv_spi_tx") |
| [`drv_spi_rx()`](#_CPPv410drv_spi_rx8uint32_tP7uint8_t8uint32_t "drv_spi_rx") |
| [`drv_spi_txrx()`](#_CPPv412drv_spi_txrx8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t "drv_spi_txrx") |
| [`drv_spi_transmit()`](#_CPPv416drv_spi_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t "drv_spi_transmit") |
| [`drv_spi_tx_async()`](#_CPPv416drv_spi_tx_async8uint32_tP7uint8_t8uint32_t "drv_spi_tx_async") |
| [`drv_spi_rx_async()`](#_CPPv416drv_spi_rx_async8uint32_tP7uint8_t8uint32_t "drv_spi_rx_async") |
| [`drv_spi_txrx_async()`](#_CPPv418drv_spi_txrx_async8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t "drv_spi_txrx_async") |
| [`drv_spi_transmit_async()`](#_CPPv422drv_spi_transmit_async8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t "drv_spi_transmit_async") |
| [`drv_spi_dma_tx()`](#_CPPv414drv_spi_dma_tx8uint32_tP7uint8_t8uint32_t "drv_spi_dma_tx") |
| [`drv_spi_dma_rx()`](#_CPPv414drv_spi_dma_rx8uint32_tP7uint8_t8uint32_t "drv_spi_dma_rx") |
| [`drv_spi_dma_transmit()`](#_CPPv420drv_spi_dma_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t "drv_spi_dma_transmit") |
| [`drv_spi_slave_tx()`](#_CPPv416drv_spi_slave_tx8uint32_tP7uint8_t8uint32_t "drv_spi_slave_tx") |
| [`drv_spi_slave_rx()`](#_CPPv416drv_spi_slave_rx8uint32_tP7uint8_t8uint32_t "drv_spi_slave_rx") |
| [`drv_spi_slave_transmit()`](#_CPPv422drv_spi_slave_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t "drv_spi_slave_transmit") |
| [`drv_spi_slave_tx_aync()`](#_CPPv421drv_spi_slave_tx_aync8uint32_tP7uint8_t8uint32_t "drv_spi_slave_tx_aync") |
| [`drv_spi_slave_rx_aync()`](#_CPPv421drv_spi_slave_rx_aync8uint32_tP7uint8_t8uint32_t "drv_spi_slave_rx_aync") |
| [`drv_spi_slave_transmit_async()`](#_CPPv428drv_spi_slave_transmit_async8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t "drv_spi_slave_transmit_async") |
| [`drv_spi_slave_dma_tx()`](#_CPPv420drv_spi_slave_dma_tx8uint32_tP7uint8_t8uint32_t "drv_spi_slave_dma_tx") |
| [`drv_spi_slave_dma_rx()`](#_CPPv420drv_spi_slave_dma_rx8uint32_tP7uint8_t8uint32_t "drv_spi_slave_dma_rx") |
| [`drv_spi_slave_dma_transmit()`](#_CPPv426drv_spi_slave_dma_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t "drv_spi_slave_dma_transmit") |

<a id="drv-spi-pin-and-gpio-map"></a>

## DRV\_SPI Pin and GPIO Map

| SPI Pin | Number |
| --- | --- |
| SPI0 SCK | 13 |
| SPI0 CSN | 14 |
| SPI0 MOSI | 15 |
| SPI0 MISO | 16 |

<a id="drv-spi-api-reference"></a>

## DRV\_SPI API Reference

<a id="header-file"></a>

### Header File

- [driver/spi/drv\_spi.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/spi/drv_spi.h)

<a id="functions"></a>

### Functions

<a id="_CPPv412drv_spi_init7uint8_t"></a>

<a id="_CPPv312drv_spi_init7uint8_t"></a> <a id="_CPPv212drv_spi_init7uint8_t"></a> <a id="drv_spi_init__uint8_t"></a> <a id="drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1"></a> uint32\_t drv\_spi\_init(uint8\_t dev\_index)
:   init a spi device.

    初始化设备，在使用spi功能前需要调用它获取device instance

    参数:
    :   **dev\_index** – **\[in\]** device index, from 0(the first device)

    返回值:
    :   - **0** – fail
        - **other** – success

    返回:
    :   device instance

<a id="_CPPv414drv_spi_deinit8uint32_t"></a>

<a id="_CPPv314drv_spi_deinit8uint32_t"></a> <a id="_CPPv214drv_spi_deinit8uint32_t"></a> <a id="drv_spi_deinit__uint32_t"></a> <a id="drv__spi_8h_1a09c2082ebef771f5335b2199181b8868"></a> int32\_t drv\_spi\_deinit(uint32\_t dev\_instance)
:   deinit a spi device.

    反初始化spi设备，对drv\_spi\_init()进行反向操作

    参数:
    :   **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv414drv_spi_config8uint32_tP12spi_config_t"></a>

<a id="_CPPv314drv_spi_config8uint32_tP12spi_config_t"></a> <a id="_CPPv214drv_spi_config8uint32_tP12spi_config_t"></a> <a id="drv_spi_config__uint32_t.spi_config_tP"></a> <a id="drv__spi_8h_1a25107c0bdcfed7934c526c73757083e1"></a> int32\_t drv\_spi\_config(uint32\_t dev\_instance, [spi\_config\_t](#_CPPv412spi_config_t "spi_config_t") \*p\_param)
:   config spi parameter.

    对spi设备参数的配置，在配置前需要确保spi处于关闭状态

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **p\_param** – **\[in\]** 参数结构体指针

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv418drv_spi_set_enable8uint32_t7uint8_t"></a>

<a id="_CPPv318drv_spi_set_enable8uint32_t7uint8_t"></a> <a id="_CPPv218drv_spi_set_enable8uint32_t7uint8_t"></a> <a id="drv_spi_set_enable__uint32_t.uint8_t"></a> <a id="drv__spi_8h_1a8c480de36d2c29b5c5f5c40c2678a881"></a> int32\_t drv\_spi\_set\_enable(uint32\_t dev\_instance, uint8\_t enable)
:   enable or disable spi device

    开起或者关闭spi的设备

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **enable** – **\[in\]** enable or disable

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv430drv_spi_register_tx_finish_cbk8uint32_t14pfunc_spi_cb_tPv"></a>

<a id="_CPPv330drv_spi_register_tx_finish_cbk8uint32_t14pfunc_spi_cb_tPv"></a> <a id="_CPPv230drv_spi_register_tx_finish_cbk8uint32_t14pfunc_spi_cb_tPv"></a> <a id="drv_spi_register_tx_finish_cbk__uint32_t.pfunc_spi_cb_t.voidP"></a> <a id="drv__spi_8h_1a6852e884347ccd5f7d16ec263c7b26ec"></a> int32\_t drv\_spi\_register\_tx\_finish\_cbk(uint32\_t dev\_instance, [pfunc\_spi\_cb\_t](#_CPPv414pfunc_spi_cb_t "pfunc_spi_cb_t") pfn\_cb, void \*pv\_arg)
:   register tx finish callback function

    注册发送结束回调函数，此函数通知用户此次发送结束

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pfn\_cb** – **\[in\]** callback when tx finish
        - **pv\_arg** – **\[in\]** callback parameter

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv430drv_spi_register_rx_finish_cbk8uint32_t14pfunc_spi_cb_tPv"></a>

<a id="_CPPv330drv_spi_register_rx_finish_cbk8uint32_t14pfunc_spi_cb_tPv"></a> <a id="_CPPv230drv_spi_register_rx_finish_cbk8uint32_t14pfunc_spi_cb_tPv"></a> <a id="drv_spi_register_rx_finish_cbk__uint32_t.pfunc_spi_cb_t.voidP"></a> <a id="drv__spi_8h_1aaa4ef375ea21b7938a19bd2b1ba9d6d8"></a> int32\_t drv\_spi\_register\_rx\_finish\_cbk(uint32\_t dev\_instance, [pfunc\_spi\_cb\_t](#_CPPv414pfunc_spi_cb_t "pfunc_spi_cb_t") pfn\_cb, void \*pv\_arg)
:   register rx finish callback function

    注册接收结束回调函数，此函数通知用户此次接收结束

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pfn\_cb** – **\[in\]** callback when rx finish
        - **pv\_arg** – **\[in\]** callback parameter

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv435drv_spi_register_slv_cs_release_cbk8uint32_t25pfunc_spi_cs_release_cb_tPv"></a>

<a id="_CPPv335drv_spi_register_slv_cs_release_cbk8uint32_t25pfunc_spi_cs_release_cb_tPv"></a> <a id="_CPPv235drv_spi_register_slv_cs_release_cbk8uint32_t25pfunc_spi_cs_release_cb_tPv"></a> <a id="drv_spi_register_slv_cs_release_cbk__uint32_t.pfunc_spi_cs_release_cb_t.voidP"></a> <a id="drv__spi_8h_1ab0ba17160cb4f291aa14b86d229344ce"></a> int32\_t drv\_spi\_register\_slv\_cs\_release\_cbk(uint32\_t dev\_instance, [pfunc\_spi\_cs\_release\_cb\_t](#_CPPv425pfunc_spi_cs_release_cb_t "pfunc_spi_cs_release_cb_t") pfn\_cb, void \*pv\_arg)
:   register rx finish callback function

    注销CS释放回调函数，仅spi做slave有效

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pfn\_cb** – **\[in\]** callback when rx finish
        - **pv\_arg** – **\[in\]** callback parameter

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv432drv_spi_unregister_tx_finish_cbk8uint32_t"></a>

<a id="_CPPv332drv_spi_unregister_tx_finish_cbk8uint32_t"></a> <a id="_CPPv232drv_spi_unregister_tx_finish_cbk8uint32_t"></a> <a id="drv_spi_unregister_tx_finish_cbk__uint32_t"></a> <a id="drv__spi_8h_1ad90296954931b3c096820648de1e0fb7"></a> int32\_t drv\_spi\_unregister\_tx\_finish\_cbk(uint32\_t dev\_instance)
:   unregister tx finish callback function

    注销接收结束回调函数

    参数:
    :   **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv432drv_spi_unregister_rx_finish_cbk8uint32_t"></a>

<a id="_CPPv332drv_spi_unregister_rx_finish_cbk8uint32_t"></a> <a id="_CPPv232drv_spi_unregister_rx_finish_cbk8uint32_t"></a> <a id="drv_spi_unregister_rx_finish_cbk__uint32_t"></a> <a id="drv__spi_8h_1a8f7d470ab191516f0eec1dab6bf1b33d"></a> int32\_t drv\_spi\_unregister\_rx\_finish\_cbk(uint32\_t dev\_instance)
:   unregister rx finish callback function

    注销接收结束回调函数

    参数:
    :   **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv437drv_spi_unregister_slv_cs_release_cbk8uint32_t"></a>

<a id="_CPPv337drv_spi_unregister_slv_cs_release_cbk8uint32_t"></a> <a id="_CPPv237drv_spi_unregister_slv_cs_release_cbk8uint32_t"></a> <a id="drv_spi_unregister_slv_cs_release_cbk__uint32_t"></a> <a id="drv__spi_8h_1ab9a66ce0e52ad7dffaba536680af7a59"></a> int32\_t drv\_spi\_unregister\_slv\_cs\_release\_cbk(uint32\_t dev\_instance)
:   unregister rx finish callback function

    注销CS释放回调函数，仅spi做slave有效 回调函数中会携带，当前实际接收或者发送的数据长度

    参数:
    :   **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv414drv_spi_tx_clr8uint32_t"></a>

<a id="_CPPv314drv_spi_tx_clr8uint32_t"></a> <a id="_CPPv214drv_spi_tx_clr8uint32_t"></a> <a id="drv_spi_tx_clr__uint32_t"></a> <a id="drv__spi_8h_1a2314ce8add36944698ebddc31ab4362a"></a> int32\_t drv\_spi\_tx\_clr(uint32\_t dev\_instance)
:   disable spi tx operation

    参数:
    :   **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv414drv_spi_rx_clr8uint32_t"></a>

<a id="_CPPv314drv_spi_rx_clr8uint32_t"></a> <a id="_CPPv214drv_spi_rx_clr8uint32_t"></a> <a id="drv_spi_rx_clr__uint32_t"></a> <a id="drv__spi_8h_1a687c7d7c3d1c882f37d36c6eee810118"></a> int32\_t drv\_spi\_rx\_clr(uint32\_t dev\_instance)
:   disable spi rx operation

    参数:
    :   **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv410drv_spi_tx8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv310drv_spi_tx8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv210drv_spi_tx8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_tx__uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1a6cb3d4f21f359eaeeea454b4b6c47cbe"></a> int32\_t drv\_spi\_tx(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size)
:   spi master send

    spi同步发送，发送完成才会退出函数 发送数据长度的不能大于0xFFF 发送完成不会调用注册的发送完成回调函数通知用户

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_buf** – **\[in\]** 发送数据缓存指针
        - **size** – **\[in\]** 发送的数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv410drv_spi_rx8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv310drv_spi_rx8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv210drv_spi_rx8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_rx__uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1a5ed1e1155281ab1379dd429b978db858"></a> int32\_t drv\_spi\_rx(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size)
:   spi master receive

    spi同步接收，接收完成才会退出函数 接收数据长度的不能大于0xFFF 接收完成不会调用注册的接收完成回调函数通知用户

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_buf** – **\[in\]** 接收数据缓存指针
        - **size** – **\[in\]** 接收的数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv412drv_spi_txrx8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv312drv_spi_txrx8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv212drv_spi_txrx8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_txrx__uint32_t.uint8_tP.uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1a1535a3f7b5d0808e22463f0d022f19f2"></a> int32\_t drv\_spi\_txrx(uint32\_t dev\_instance, uint8\_t \*pu1\_tx\_buf, uint32\_t tx\_size, uint8\_t \*pu1\_rx\_buf, uint32\_t rx\_size)
:   spi master send and receive data

    spi同步发送接收，发送接收完成才会退出函数 先发送数据，然后再接收数据 发送数据长度加上接收数据长度的不能大于0xFFF 发送，接收完毕后都不会调用注册的接收完成回调函数通知用户

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_tx\_buf** – **\[in\]** 发送数据缓存指针
        - **tx\_size** – **\[in\]** 发送数据长度，byte
        - **pu1\_rx\_buf** – **\[in\]** 接收数据缓存指针
        - **rx\_size** – **\[in\]** 接收数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416drv_spi_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv316drv_spi_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv216drv_spi_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_transmit__uint32_t.uint8_tP.uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1a8a14c94f762faca95ede54b549bac230"></a> int32\_t drv\_spi\_transmit(uint32\_t dev\_instance, uint8\_t \*pu1\_tx\_buf, uint32\_t tx\_size, uint8\_t \*pu1\_rx\_buf, uint32\_t rx\_size)
:   spi master send and receive data

    spi全双工同步接口 发送数据长度的不能大于0xFFF 接收数据长度的不能大于0xFFF 发送，接收完毕后都不会调用注册的接收完成回调函数通知用户

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_tx\_buf** – **\[in\]** 发送数据缓存指针
        - **tx\_size** – **\[in\]** 发送数据长度，byte
        - **pu1\_rx\_buf** – **\[in\]** 接收数据缓存指针
        - **rx\_size** – **\[in\]** 接收数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416drv_spi_tx_async8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv316drv_spi_tx_async8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv216drv_spi_tx_async8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_tx_async__uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1aa5883837181b9cd4873f3b891dbef83e"></a> int32\_t drv\_spi\_tx\_async(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size)
:   spi master send

    spi异步发送，发送完成会调用注册的发送完成回调函数通知用户 发送数据长度的不能大于0xFFF

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_buf** – **\[in\]** 发送数据缓存指针
        - **size** – **\[in\]** 发送的数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416drv_spi_rx_async8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv316drv_spi_rx_async8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv216drv_spi_rx_async8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_rx_async__uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1a0b8ed50afa052fdc70ced565cbe0ee6e"></a> int32\_t drv\_spi\_rx\_async(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size)
:   spi master receive

    spi异步接收，接收完成会调用注册的接收完成回调函数通知用户 接收数据长度的不能大于0xFFF

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_buf** – **\[in\]** 接收数据缓存指针
        - **size** – **\[in\]** 接收的数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv418drv_spi_txrx_async8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv318drv_spi_txrx_async8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv218drv_spi_txrx_async8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_txrx_async__uint32_t.uint8_tP.uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1af005b13b5ac9ae838e0d3d4f402307eb"></a> int32\_t drv\_spi\_txrx\_async(uint32\_t dev\_instance, uint8\_t \*pu1\_tx\_buf, uint32\_t tx\_size, uint8\_t \*pu1\_rx\_buf, uint32\_t rx\_size)
:   spi master send and receive data

    spi发送接收异步接口 先发送数据，然后再接收数据 发送数据长度加上接收数据长度的不能大于0xFFF 发送，接收完毕后都会调用注册的接收完成回调函数通知用户

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_tx\_buf** – **\[in\]** 发送数据缓存指针
        - **tx\_size** – **\[in\]** 发送数据长度，byte
        - **pu1\_rx\_buf** – **\[in\]** 接收数据缓存指针
        - **rx\_size** – **\[in\]** 接收数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422drv_spi_transmit_async8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv322drv_spi_transmit_async8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv222drv_spi_transmit_async8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_transmit_async__uint32_t.uint8_tP.uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1a52183df98500b85f5b35ae287718847d"></a> int32\_t drv\_spi\_transmit\_async(uint32\_t dev\_instance, uint8\_t \*pu1\_tx\_buf, uint32\_t tx\_size, uint8\_t \*pu1\_rx\_buf, uint32\_t rx\_size)
:   spi master send and receive data

    spi全双工异步接口 发送数据长度的不能大于0xFFF 接收数据长度的不能大于0xFFF 发送，接收完毕后都会调用注册的接收完成回调函数通知用户

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_tx\_buf** – **\[in\]** 发送数据缓存指针
        - **tx\_size** – **\[in\]** 发送数据长度，byte
        - **pu1\_rx\_buf** – **\[in\]** 接收数据缓存指针
        - **rx\_size** – **\[in\]** 接收数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv414drv_spi_dma_tx8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv314drv_spi_dma_tx8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv214drv_spi_dma_tx8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_dma_tx__uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1a0af2a22641c74ae57e434b9a89d06c1c"></a> int32\_t drv\_spi\_dma\_tx(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size)
:   spi master send

    spi 使用dma的异步发送，发送完成会调用注册的发送完成回调函数通知用户 发送数据长度的不能大于0xFFF

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_buf** – **\[in\]** 发送数据缓存指针
        - **size** – **\[in\]** 发送的数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv414drv_spi_dma_rx8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv314drv_spi_dma_rx8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv214drv_spi_dma_rx8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_dma_rx__uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1a285ee840eb84358f6b5dc67bdb6d59c7"></a> int32\_t drv\_spi\_dma\_rx(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size)
:   spi master receive

    spi使用dma的异步接收，接收完成会调用注册的接收完成回调函数通知用户 接收数据长度的不能大于0xFFF

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_buf** – **\[in\]** 接收数据缓存指针
        - **size** – **\[in\]** 接收的数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420drv_spi_dma_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv320drv_spi_dma_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv220drv_spi_dma_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_dma_transmit__uint32_t.uint8_tP.uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1a1824d0a6951069763b6d461ab43fbe4f"></a> int32\_t drv\_spi\_dma\_transmit(uint32\_t dev\_instance, uint8\_t \*pu1\_tx\_buf, uint32\_t tx\_size, uint8\_t \*pu1\_rx\_buf, uint32\_t rx\_size)
:   spi master send and receive data

    spi全双工DMA接口 发送数据长度的不能大于0xFFF 接收数据长度的不能大于0xFFF 此接口与drv\_spi\_transmit()和drv\_spi\_transmit\_async()接口存在区别，不能做到相互替换

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_tx\_buf** – **\[in\]** 发送数据缓存指针
        - **tx\_size** – **\[in\]** 发送数据长度，byte
        - **pu1\_rx\_buf** – **\[in\]** 接收数据缓存指针，接收完毕后接收缓存前面会包含tx\_size个无效数据。
        - **rx\_size** – **\[in\]** 接收数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416drv_spi_slave_tx8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv316drv_spi_slave_tx8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv216drv_spi_slave_tx8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_slave_tx__uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1abc7e7c2542ced59dba13536b97cef740"></a> int32\_t drv\_spi\_slave\_tx(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size)
:   spi slave send

    spi同步发送，发送完成才会退出函数 发送数据长度的不能大于0xFFF 发送完成不会调用注册的发送完成回调函数通知用户

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_buf** – **\[in\]** 发送数据缓存指针
        - **size** – **\[in\]** 发送的数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416drv_spi_slave_rx8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv316drv_spi_slave_rx8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv216drv_spi_slave_rx8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_slave_rx__uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1aab83d6a88bf35e506b28aa72c8900c94"></a> int32\_t drv\_spi\_slave\_rx(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size)
:   spi slave receive

    spi同步接收，接收完成才会退出函数 接收数据长度的不能大于0xFFF 接收完成不会调用注册的接收完成回调函数通知用户

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_buf** – **\[in\]** 接收数据缓存指针
        - **size** – **\[in\]** 接收的数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422drv_spi_slave_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv322drv_spi_slave_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv222drv_spi_slave_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_slave_transmit__uint32_t.uint8_tP.uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1a609a92846549f608379035ea6ffaaee9"></a> int32\_t drv\_spi\_slave\_transmit(uint32\_t dev\_instance, uint8\_t \*pu1\_tx\_buf, uint32\_t tx\_size, uint8\_t \*pu1\_rx\_buf, uint32\_t rx\_size)
:   spi slave send and receive data

    spi全双工同步接口 发送数据长度的不能大于0xFFF 接收数据长度的不能大于0xFFF 发送，接收完毕后都不会调用注册的接收完成回调函数通知用户

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_tx\_buf** – **\[in\]** 发送数据缓存指针
        - **tx\_size** – **\[in\]** 发送数据长度，byte
        - **pu1\_rx\_buf** – **\[in\]** 接收数据缓存指针
        - **rx\_size** – **\[in\]** 接收数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421drv_spi_slave_tx_aync8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv321drv_spi_slave_tx_aync8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv221drv_spi_slave_tx_aync8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_slave_tx_aync__uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1a1a7e2c2ed338fd453e929124e84a3a6d"></a> int32\_t drv\_spi\_slave\_tx\_aync(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size)
:   spi slave send

    spi异步发送，发送完成会调用注册的发送完成回调函数通知用户 发送数据长度的不能大于0xFFF

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_buf** – **\[in\]** 发送数据缓存指针
        - **size** – **\[in\]** 发送的数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421drv_spi_slave_rx_aync8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv321drv_spi_slave_rx_aync8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv221drv_spi_slave_rx_aync8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_slave_rx_aync__uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1a2527acce7721b310b2eb82a8383337f8"></a> int32\_t drv\_spi\_slave\_rx\_aync(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size)
:   spi slave receive

    spi异步接收，接收完成会调用注册的接收完成回调函数通知用户 接收数据长度的不能大于0xFFF

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_buf** – **\[in\]** 接收数据缓存指针
        - **size** – **\[in\]** 接收的数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv428drv_spi_slave_transmit_async8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv328drv_spi_slave_transmit_async8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv228drv_spi_slave_transmit_async8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_slave_transmit_async__uint32_t.uint8_tP.uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1afe28bacb0e070e25b7aad288e5c23d11"></a> int32\_t drv\_spi\_slave\_transmit\_async(uint32\_t dev\_instance, uint8\_t \*pu1\_tx\_buf, uint32\_t tx\_size, uint8\_t \*pu1\_rx\_buf, uint32\_t rx\_size)
:   spi slave send and receive data

    spi全双工异步接口 发送数据长度的不能大于0xFFF 接收数据长度的不能大于0xFFF 发送，接收完毕后都会调用注册的接收完成回调函数通知用户

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_tx\_buf** – **\[in\]** 发送数据缓存指针
        - **tx\_size** – **\[in\]** 发送数据长度，byte
        - **pu1\_rx\_buf** – **\[in\]** 接收数据缓存指针
        - **rx\_size** – **\[in\]** 接收数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420drv_spi_slave_dma_tx8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv320drv_spi_slave_dma_tx8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv220drv_spi_slave_dma_tx8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_slave_dma_tx__uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1adc5c0b9e0f5abb7a3ea3757b99f6003a"></a> int32\_t drv\_spi\_slave\_dma\_tx(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size)
:   spi slave send

    spi 使用dma的异步发送，发送完成会调用注册的发送完成回调函数通知用户 发送数据长度的不能大于0xFFF

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_buf** – **\[in\]** 发送数据缓存指针
        - **size** – **\[in\]** 发送的数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420drv_spi_slave_dma_rx8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv320drv_spi_slave_dma_rx8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv220drv_spi_slave_dma_rx8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_slave_dma_rx__uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1a981d4336cc05aaa1e478e0335e9efe6a"></a> int32\_t drv\_spi\_slave\_dma\_rx(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size)
:   spi slave receive

    spi使用dma的异步接收，接收完成会调用注册的接收完成回调函数通知用户 接收数据长度的不能大于0xFFF

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_buf** – **\[in\]** 接收数据缓存指针
        - **size** – **\[in\]** 接收的数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426drv_spi_slave_dma_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv326drv_spi_slave_dma_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv226drv_spi_slave_dma_transmit8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_spi_slave_dma_transmit__uint32_t.uint8_tP.uint32_t.uint8_tP.uint32_t"></a> <a id="drv__spi_8h_1a724aab235bda06e13e11c088dc3d3996"></a> int32\_t drv\_spi\_slave\_dma\_transmit(uint32\_t dev\_instance, uint8\_t \*pu1\_tx\_buf, uint32\_t tx\_size, uint8\_t \*pu1\_rx\_buf, uint32\_t rx\_size)
:   spi slave send and receive data

    spi全双工DMA接口 发送数据长度的不能大于0xFFF 接收数据长度的不能大于0xFFF 此接口与drv\_spi\_transmit()和drv\_spi\_transmit\_async()接口存在区别，不能做到相互替换

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_tx\_buf** – **\[in\]** 发送数据缓存指针
        - **tx\_size** – **\[in\]** 发送数据长度，byte
        - **pu1\_rx\_buf** – **\[in\]** 接收数据缓存指针
        - **rx\_size** – **\[in\]** 接收数据长度，byte

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv412spi_config_t"></a>

<a id="_CPPv312spi_config_t"></a> <a id="_CPPv212spi_config_t"></a> <a id="spi_config_t"></a> <a id="structspi__config__t"></a> struct spi\_config\_t
:   SPI device config struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N12spi_config_t4roleE"></a>

    <a id="_CPPv3N12spi_config_t4roleE"></a> <a id="_CPPv2N12spi_config_t4roleE"></a> <a id="spi_config_t::role__spi_role_e"></a> <a id="structspi__config__t_1a2d10475c7bc4979b0d36f88b96dc6d8c"></a> [spi\_role\_e](#_CPPv410spi_role_e "spi_role_e") role
    :   SPI as master or slave

    <a id="_CPPv4N12spi_config_t3clkE"></a>

    <a id="_CPPv3N12spi_config_t3clkE"></a> <a id="_CPPv2N12spi_config_t3clkE"></a> <a id="spi_config_t::clk__uint32_t"></a> <a id="structspi__config__t_1ac0377e4369272f8e98a5be9fb12febac"></a> uint32\_t clk
    :   SPI HW work clock

    <a id="_CPPv4N12spi_config_t9baud_rateE"></a>

    <a id="_CPPv3N12spi_config_t9baud_rateE"></a> <a id="_CPPv2N12spi_config_t9baud_rateE"></a> <a id="spi_config_t::baud_rate__uint32_t"></a> <a id="structspi__config__t_1a3e13ccc08ecf811ba2471f5eb3cc7baa"></a> uint32\_t baud\_rate
    :   SPI transmit and receive SCK clock

    <a id="_CPPv4N12spi_config_t9wire_modeE"></a>

    <a id="_CPPv3N12spi_config_t9wire_modeE"></a> <a id="_CPPv2N12spi_config_t9wire_modeE"></a> <a id="spi_config_t::wire_mode__spi_wire_mode_e"></a> <a id="structspi__config__t_1ac02d4d8759813f1f711f6679fd79afa4"></a> [spi\_wire\_mode\_e](#_CPPv415spi_wire_mode_e "spi_wire_mode_e") wire\_mode
    :   SPI wire mode

    <a id="_CPPv4N12spi_config_t4cpolE"></a>

    <a id="_CPPv3N12spi_config_t4cpolE"></a> <a id="_CPPv2N12spi_config_t4cpolE"></a> <a id="spi_config_t::cpol__spi_cpol_e"></a> <a id="structspi__config__t_1a660dadd4cbcb687369298bf013646e09"></a> [spi\_cpol\_e](#_CPPv410spi_cpol_e "spi_cpol_e") cpol
    :   SPI clock cpol

    <a id="_CPPv4N12spi_config_t4cphaE"></a>

    <a id="_CPPv3N12spi_config_t4cphaE"></a> <a id="_CPPv2N12spi_config_t4cphaE"></a> <a id="spi_config_t::cpha__spi_cpha_e"></a> <a id="structspi__config__t_1acbcf5f2ca12f7eaa54ab90fe630db298"></a> [spi\_cpha\_e](#_CPPv410spi_cpha_e "spi_cpha_e") cpha
    :   SPI clock cpha

    <a id="_CPPv4N12spi_config_t9bit_orderE"></a>

    <a id="_CPPv3N12spi_config_t9bit_orderE"></a> <a id="_CPPv2N12spi_config_t9bit_orderE"></a> <a id="spi_config_t::bit_order__spi_bit_order_e"></a> <a id="structspi__config__t_1ab71932c62fa1fb3177812b7b3d59ca5b"></a> [spi\_bit\_order\_e](#_CPPv415spi_bit_order_e "spi_bit_order_e") bit\_order
    :   SPI bit order, MSB/LSB

<a id="macros"></a>

### Macros

<a id="c.SPI_DEVICE_NUM"></a>

<a id="drv__spi_8h_1aec9518e431ecf70a6837c47752c7e5da"></a> SPI\_DEVICE\_NUM
:   SPI DEVICE NUMBERS

<a id="c.CONFIG_SPI_DMA"></a>

<a id="drv__spi_8h_1ab48c72d2892a8e5a988da51856973ed6"></a> CONFIG\_SPI\_DMA

<a id="c.DMA_DEVICE_INDEX_FOR_SPI"></a>

<a id="drv__spi_8h_1ac1ac766bf46747d4c8b6dedf83c44eea"></a> DMA\_DEVICE\_INDEX\_FOR\_SPI

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv414pfunc_spi_cb_t"></a>

<a id="_CPPv314pfunc_spi_cb_t"></a> <a id="_CPPv214pfunc_spi_cb_t"></a> <a id="pfunc_spi_cb_t"></a> <a id="drv__spi_8h_1a9d4165cd179e88ec9cc1f85d059f5150"></a> typedef void (\*pfunc\_spi\_cb\_t)(uint32\_t dev\_instance, int32\_t err\_code, uint32\_t op\_len, void \*param)

<a id="_CPPv425pfunc_spi_cs_release_cb_t"></a>

<a id="_CPPv325pfunc_spi_cs_release_cb_t"></a> <a id="_CPPv225pfunc_spi_cs_release_cb_t"></a> <a id="pfunc_spi_cs_release_cb_t"></a> <a id="drv__spi_8h_1ac8dd742904d289f079625ce514629677"></a> typedef void (\*pfunc\_spi\_cs\_release\_cb\_t)(uint32\_t dev\_instance, int32\_t err\_code, uint32\_t tx\_len, uint32\_t rx\_len, void \*param)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv410spi_role_e"></a>

<a id="_CPPv310spi_role_e"></a> <a id="_CPPv210spi_role_e"></a> <a id="drv__spi_8h_1acfd868e5572b50024d47511d4d19d82a"></a> enum spi\_role\_e
:   SPI device role mode definition.

    *Values:*

    <a id="_CPPv4N10spi_role_e14SPI_ROLE_SLAVEE"></a>

    <a id="_CPPv3N10spi_role_e14SPI_ROLE_SLAVEE"></a> <a id="_CPPv2N10spi_role_e14SPI_ROLE_SLAVEE"></a> <a id="drv__spi_8h_1acfd868e5572b50024d47511d4d19d82aa09c1f921b6707d02a9bd1e41817767a5"></a> enumerator SPI\_ROLE\_SLAVE
    :   SPI as slave

    <a id="_CPPv4N10spi_role_e15SPI_ROLE_MASTERE"></a>

    <a id="_CPPv3N10spi_role_e15SPI_ROLE_MASTERE"></a> <a id="_CPPv2N10spi_role_e15SPI_ROLE_MASTERE"></a> <a id="drv__spi_8h_1acfd868e5572b50024d47511d4d19d82aa1f8bc6aa1f8e48dca00f24d45a7a2977"></a> enumerator SPI\_ROLE\_MASTER
    :   SPI as master

<a id="_CPPv410spi_cpol_e"></a>

<a id="_CPPv310spi_cpol_e"></a> <a id="_CPPv210spi_cpol_e"></a> <a id="drv__spi_8h_1a4e8b03bf39d8527abacab8ec3df7ad9c"></a> enum spi\_cpol\_e
:   SPI CPOL definition.

    *Values:*

    <a id="_CPPv4N10spi_cpol_e10SPI_CPOL_0E"></a>

    <a id="_CPPv3N10spi_cpol_e10SPI_CPOL_0E"></a> <a id="_CPPv2N10spi_cpol_e10SPI_CPOL_0E"></a> <a id="drv__spi_8h_1a4e8b03bf39d8527abacab8ec3df7ad9cae25d638f77351e4a5bfc97602d9d036f"></a> enumerator SPI\_CPOL\_0
    :   SPI clock phase low

    <a id="_CPPv4N10spi_cpol_e10SPI_CPOL_1E"></a>

    <a id="_CPPv3N10spi_cpol_e10SPI_CPOL_1E"></a> <a id="_CPPv2N10spi_cpol_e10SPI_CPOL_1E"></a> <a id="drv__spi_8h_1a4e8b03bf39d8527abacab8ec3df7ad9cade6883ea54f4627100872a6c71ed728f"></a> enumerator SPI\_CPOL\_1
    :   SPI clock phase high

<a id="_CPPv410spi_cpha_e"></a>

<a id="_CPPv310spi_cpha_e"></a> <a id="_CPPv210spi_cpha_e"></a> <a id="drv__spi_8h_1afdccd98385fc528905c5730f83598c78"></a> enum spi\_cpha\_e
:   SPI CPHA definition.

    *Values:*

    <a id="_CPPv4N10spi_cpha_e10SPI_CPHA_0E"></a>

    <a id="_CPPv3N10spi_cpha_e10SPI_CPHA_0E"></a> <a id="_CPPv2N10spi_cpha_e10SPI_CPHA_0E"></a> <a id="drv__spi_8h_1afdccd98385fc528905c5730f83598c78a453298c9885db4b51f527c6ad290c7f6"></a> enumerator SPI\_CPHA\_0
    :   SPI clock phase the first edge

    <a id="_CPPv4N10spi_cpha_e10SPI_CPHA_1E"></a>

    <a id="_CPPv3N10spi_cpha_e10SPI_CPHA_1E"></a> <a id="_CPPv2N10spi_cpha_e10SPI_CPHA_1E"></a> <a id="drv__spi_8h_1afdccd98385fc528905c5730f83598c78a304d3e66edefcab8e781eb4efd42a38b"></a> enumerator SPI\_CPHA\_1
    :   SPI clock phase the second edge

<a id="_CPPv415spi_wire_mode_e"></a>

<a id="_CPPv315spi_wire_mode_e"></a> <a id="_CPPv215spi_wire_mode_e"></a> <a id="drv__spi_8h_1ad72509a3cc51134fd37793e7170e72f0"></a> enum spi\_wire\_mode\_e
:   SPI Work line mode definition.

    *Values:*

    <a id="_CPPv4N15spi_wire_mode_e14SPI_4WIRE_MODEE"></a>

    <a id="_CPPv3N15spi_wire_mode_e14SPI_4WIRE_MODEE"></a> <a id="_CPPv2N15spi_wire_mode_e14SPI_4WIRE_MODEE"></a> <a id="drv__spi_8h_1ad72509a3cc51134fd37793e7170e72f0a9b77a68d98cde0380fdad756c0538c6a"></a> enumerator SPI\_4WIRE\_MODE
    :   SPI four wire mode

    <a id="_CPPv4N15spi_wire_mode_e14SPI_3WIRE_MODEE"></a>

    <a id="_CPPv3N15spi_wire_mode_e14SPI_3WIRE_MODEE"></a> <a id="_CPPv2N15spi_wire_mode_e14SPI_3WIRE_MODEE"></a> <a id="drv__spi_8h_1ad72509a3cc51134fd37793e7170e72f0ab1f434fba6c742beb626fda478c69062"></a> enumerator SPI\_3WIRE\_MODE
    :   SPI three wire mode (no cs)

<a id="_CPPv415spi_bit_order_e"></a>

<a id="_CPPv315spi_bit_order_e"></a> <a id="_CPPv215spi_bit_order_e"></a> <a id="drv__spi_8h_1ae4797b549e4bf5bb099063dbc87764b9"></a> enum spi\_bit\_order\_e
:   SPI bit order definition.

    *Values:*

    <a id="_CPPv4N15spi_bit_order_e13SPI_MSB_FIRSTE"></a>

    <a id="_CPPv3N15spi_bit_order_e13SPI_MSB_FIRSTE"></a> <a id="_CPPv2N15spi_bit_order_e13SPI_MSB_FIRSTE"></a> <a id="drv__spi_8h_1ae4797b549e4bf5bb099063dbc87764b9a8912f763c0e7854e08dfbe61b7a57cc6"></a> enumerator SPI\_MSB\_FIRST
    :   SPI MSB first

    <a id="_CPPv4N15spi_bit_order_e13SPI_LSB_FIRSTE"></a>

    <a id="_CPPv3N15spi_bit_order_e13SPI_LSB_FIRSTE"></a> <a id="_CPPv2N15spi_bit_order_e13SPI_LSB_FIRSTE"></a> <a id="drv__spi_8h_1ae4797b549e4bf5bb099063dbc87764b9a5a6abe145caf9794d5a70e5472ee988f"></a> enumerator SPI\_LSB\_FIRST
    :   SPI LSB first
