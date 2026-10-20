---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_sdio.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-sdio"></a>

# DRV\_SDIO

<a id="drv-sdio-api-status"></a>

## DRV\_SDIO API Status

| API |
| --- |
| [`drv_sdio_init()`](#_CPPv413drv_sdio_init8uint32_t "drv_sdio_init") |
| [`drv_sdio_deinit()`](#_CPPv415drv_sdio_deinit8uint32_t "drv_sdio_deinit") |
| [`drv_sdio_set_sys_clk()`](#_CPPv420drv_sdio_set_sys_clk16sdio_clock_src_e16sdio_clock_div_e "drv_sdio_set_sys_clk") |
| [`drv_sdio_send_cmd()`](#_CPPv417drv_sdio_send_cmd8uint32_tP17sdio_cmd_config_t "drv_sdio_send_cmd") |
| [`drv_sdio_wait_cmd_rsp()`](#_CPPv421drv_sdio_wait_cmd_rsp8uint32_t8uint32_t "drv_sdio_wait_cmd_rsp") |
| [`drv_sdio_get_cmd_rsp_argument()`](#_CPPv429drv_sdio_get_cmd_rsp_argument8uint32_t15sdio_response_e "drv_sdio_get_cmd_rsp_argument") |
| [`drv_sdio_set_data_timeout()`](#_CPPv425drv_sdio_set_data_timeout8uint32_t8uint32_t "drv_sdio_set_data_timeout") |
| [`drv_sdio_config_data()`](#_CPPv420drv_sdio_config_data8uint32_tPK18sdio_data_config_t "drv_sdio_config_data") |
| [`drv_sdio_read_data_fifo()`](#_CPPv423drv_sdio_read_data_fifo8uint32_tP8uint32_t "drv_sdio_read_data_fifo") |
| [`drv_sdio_write_data_fifo()`](#_CPPv424drv_sdio_write_data_fifo8uint32_t8uint32_t "drv_sdio_write_data_fifo") |
| [`drv_sdio_read_data_start()`](#_CPPv424drv_sdio_read_data_start8uint32_t "drv_sdio_read_data_start") |
| [`drv_sdio_write_data_start()`](#_CPPv425drv_sdio_write_data_start8uint32_t "drv_sdio_write_data_start") |
| [`drv_sdio_wait_read_done()`](#_CPPv423drv_sdio_wait_read_done8uint32_t "drv_sdio_wait_read_done") |
| [`drv_sdio_wait_write_done()`](#_CPPv424drv_sdio_wait_write_done8uint32_t "drv_sdio_wait_write_done") |
| [`drv_sdio_interrupt_callback_register()`](#_CPPv436drv_sdio_interrupt_callback_register8uint32_t15pfunc_sdio_cb_tPv "drv_sdio_interrupt_callback_register") |
| [`drv_sdio_get_rx_fifo_addr()`](#_CPPv425drv_sdio_get_rx_fifo_addr8uint32_t "drv_sdio_get_rx_fifo_addr") |
| [`drv_sdio_get_tx_fifo_addr()`](#_CPPv425drv_sdio_get_tx_fifo_addr8uint32_t "drv_sdio_get_tx_fifo_addr") |
| [`drv_sdio_set_tx_empty()`](#_CPPv421drv_sdio_set_tx_empty8uint32_t8uint32_t "drv_sdio_set_tx_empty") |
| [`drv_sdio_wait_tx_fifo_empty()`](#_CPPv427drv_sdio_wait_tx_fifo_empty8uint32_t "drv_sdio_wait_tx_fifo_empty") |
| [`drv_sdio_sd_reset()`](#_CPPv417drv_sdio_sd_reset8uint32_t "drv_sdio_sd_reset") |
| [`drv_sdio_clear_wr_end_int()`](#_CPPv425drv_sdio_clear_wr_end_int8uint32_t "drv_sdio_clear_wr_end_int") |

<a id="drv-sdio-pin-and-gpio-map"></a>

## DRV\_SDIO Pin and GPIO Map

| SDIO Pin | Number |
| --- | --- |
| SDIO CLK | 2 |
| SDIO CSN | 3 |
| SDIO DATA\[0\] | 4 |
| SDIO DATA\[1\] | 5 |
| SDIO DATA\[3\] | 10 |
| SDIO DATA\[4\] | 11 |

<a id="drv-sdio-api-reference"></a>

## DRV\_SDIO API Reference

<a id="header-file"></a>

### Header File

- [driver/sdio/drv\_sdio.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/sdio/drv_sdio.h)

<a id="functions"></a>

### Functions

<a id="_CPPv413drv_sdio_init8uint32_t"></a>

<a id="_CPPv313drv_sdio_init8uint32_t"></a> <a id="_CPPv213drv_sdio_init8uint32_t"></a> <a id="drv_sdio_init__uint32_t"></a> <a id="drv__sdio_8h_1a131967564a09612ac395aacd543628b2"></a> uint32\_t drv\_sdio\_init(uint32\_t dev\_index)
:   Init the sdio host driver.

    This API init the resoure common:

    - Power up the sdio
    - Enable sdio host interrupt
    - Configure the sdio clock soure to 26M

    **Attention**
    :   1\. This API should be called before any other sdio host APIs

    返回值:
    :   - **0** – fail
        - **other** – success

    返回:
    :   device instance

<a id="_CPPv415drv_sdio_deinit8uint32_t"></a>

<a id="_CPPv315drv_sdio_deinit8uint32_t"></a> <a id="_CPPv215drv_sdio_deinit8uint32_t"></a> <a id="drv_sdio_deinit__uint32_t"></a> <a id="drv__sdio_8h_1a442eb5aeb125cfcbe456a81b3e0117f8"></a> int32\_t drv\_sdio\_deinit(uint32\_t dev\_instance)
:   Deinit the sdio host driver.

    - Reset all configuration of sdio host to default value

      - Clear sdio host interrupt status
    - Power down the sdio host
    - Disable sdio host interrupt

    参数:
    :   **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420drv_sdio_set_sys_clk16sdio_clock_src_e16sdio_clock_div_e"></a>

<a id="_CPPv320drv_sdio_set_sys_clk16sdio_clock_src_e16sdio_clock_div_e"></a> <a id="_CPPv220drv_sdio_set_sys_clk16sdio_clock_src_e16sdio_clock_div_e"></a> <a id="drv_sdio_set_sys_clk__sdio_clock_src_e.sdio_clock_div_e"></a> <a id="drv__sdio_8h_1a7c363922f77f2ccb8d4fd8984028374b"></a> void drv\_sdio\_set\_sys\_clk([sdio\_clock\_src\_e](#_CPPv416sdio_clock_src_e "sdio_clock_src_e") clock\_src, [sdio\_clock\_div\_e](#_CPPv416sdio_clock_div_e "sdio_clock_div_e") clock\_div)
:   Set the sdio clock.

    参数:
    :   - **clock\_src** – **\[in\]** clock的源头
        - **clock\_div** – **\[in\]** 分频系数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv417drv_sdio_send_cmd8uint32_tP17sdio_cmd_config_t"></a>

<a id="_CPPv317drv_sdio_send_cmd8uint32_tP17sdio_cmd_config_t"></a> <a id="_CPPv217drv_sdio_send_cmd8uint32_tP17sdio_cmd_config_t"></a> <a id="drv_sdio_send_cmd__uint32_t.sdio_cmd_config_tP"></a> <a id="drv__sdio_8h_1a9a358ba96582647ffe03a6fa999b83eb"></a> int32\_t drv\_sdio\_send\_cmd(uint32\_t dev\_instance, [sdio\_cmd\_config\_t](#_CPPv417sdio_cmd_config_t "sdio_cmd_config_t") \*p\_cmd)
:   Send the command from host to slave.

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **p\_cmd** – **\[in\]** command the configuration information for the command

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421drv_sdio_wait_cmd_rsp8uint32_t8uint32_t"></a>

<a id="_CPPv321drv_sdio_wait_cmd_rsp8uint32_t8uint32_t"></a> <a id="_CPPv221drv_sdio_wait_cmd_rsp8uint32_t8uint32_t"></a> <a id="drv_sdio_wait_cmd_rsp__uint32_t.uint32_t"></a> <a id="drv__sdio_8h_1a503465a40a03b49ec1bebf34a8fa2b8d"></a> int32\_t drv\_sdio\_wait\_cmd\_rsp(uint32\_t dev\_instance, uint32\_t cmd\_index)
:   Host wait for salve command response.

    函数是阻塞式等待slave响应，不能与drv\_sdio\_interrupt\_callback\_register进行混用

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **cmd\_index** – **\[in\]** cmd\_index the command index

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv429drv_sdio_get_cmd_rsp_argument8uint32_t15sdio_response_e"></a>

<a id="_CPPv329drv_sdio_get_cmd_rsp_argument8uint32_t15sdio_response_e"></a> <a id="_CPPv229drv_sdio_get_cmd_rsp_argument8uint32_t15sdio_response_e"></a> <a id="drv_sdio_get_cmd_rsp_argument__uint32_t.sdio_response_e"></a> <a id="drv__sdio_8h_1a27f56b91da5172756f5900f9fb75b5b2"></a> uint32\_t drv\_sdio\_get\_cmd\_rsp\_argument(uint32\_t dev\_instance, [sdio\_response\_e](#_CPPv415sdio_response_e "sdio_response_e") argument\_index)
:   Get the command response.

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **argument\_index** – **\[in\]** argument\_index the command argument index

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425drv_sdio_set_data_timeout8uint32_t8uint32_t"></a>

<a id="_CPPv325drv_sdio_set_data_timeout8uint32_t8uint32_t"></a> <a id="_CPPv225drv_sdio_set_data_timeout8uint32_t8uint32_t"></a> <a id="drv_sdio_set_data_timeout__uint32_t.uint32_t"></a> <a id="drv__sdio_8h_1a7f861520af9868c3ff2072bd16f020b0"></a> int32\_t drv\_sdio\_set\_data\_timeout(uint32\_t dev\_instance, uint32\_t timeout)
:   Set the data timeout.

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **timeout** – **\[in\]** timeout the data timeout

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420drv_sdio_config_data8uint32_tPK18sdio_data_config_t"></a>

<a id="_CPPv320drv_sdio_config_data8uint32_tPK18sdio_data_config_t"></a> <a id="_CPPv220drv_sdio_config_data8uint32_tPK18sdio_data_config_t"></a> <a id="drv_sdio_config_data__uint32_t.sdio_data_config_tCP"></a> <a id="drv__sdio_8h_1a7abfb939ae40b3ee66683be5c18955fb"></a> int32\_t drv\_sdio\_config\_data(uint32\_t dev\_instance, const [sdio\_data\_config\_t](#_CPPv418sdio_data_config_t "sdio_data_config_t") \*data\_config)
:   Config the data.

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **data\_config** – **\[in\]** data\_config the configuration information for the data

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv423drv_sdio_read_data_fifo8uint32_tP8uint32_t"></a>

<a id="_CPPv323drv_sdio_read_data_fifo8uint32_tP8uint32_t"></a> <a id="_CPPv223drv_sdio_read_data_fifo8uint32_tP8uint32_t"></a> <a id="drv_sdio_read_data_fifo__uint32_t.uint32_tP"></a> <a id="drv__sdio_8h_1a4dfd1fc65609ed8d3ba60dd3ed254758"></a> int32\_t drv\_sdio\_read\_data\_fifo(uint32\_t dev\_instance, uint32\_t \*pu4\_buf)
:   Read data from rx fifo.

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu4\_buf** – **\[in\]** pointer to read data

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424drv_sdio_write_data_fifo8uint32_t8uint32_t"></a>

<a id="_CPPv324drv_sdio_write_data_fifo8uint32_t8uint32_t"></a> <a id="_CPPv224drv_sdio_write_data_fifo8uint32_t8uint32_t"></a> <a id="drv_sdio_write_data_fifo__uint32_t.uint32_t"></a> <a id="drv__sdio_8h_1a5db1fff7bb95cd8db72b945dc52ebfce"></a> int32\_t drv\_sdio\_write\_data\_fifo(uint32\_t dev\_instance, uint32\_t write\_data)
:   Write data to tx fifo.

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **write\_data** – **\[in\]** write\_data pointer to data to write

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424drv_sdio_read_data_start8uint32_t"></a>

<a id="_CPPv324drv_sdio_read_data_start8uint32_t"></a> <a id="_CPPv224drv_sdio_read_data_start8uint32_t"></a> <a id="drv_sdio_read_data_start__uint32_t"></a> <a id="drv__sdio_8h_1aa5dbce9871dbb70ee9368fa6ea07da4b"></a> int32\_t drv\_sdio\_read\_data\_start(uint32\_t dev\_instance)
:   host starts reading data from slave

    参数:
    :   **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425drv_sdio_write_data_start8uint32_t"></a>

<a id="_CPPv325drv_sdio_write_data_start8uint32_t"></a> <a id="_CPPv225drv_sdio_write_data_start8uint32_t"></a> <a id="drv_sdio_write_data_start__uint32_t"></a> <a id="drv__sdio_8h_1a0eb9af63a509e43cd65f333c1986e6fb"></a> int32\_t drv\_sdio\_write\_data\_start(uint32\_t dev\_instance)
:   host starts writing data to slave

    参数:
    :   **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv423drv_sdio_wait_read_done8uint32_t"></a>

<a id="_CPPv323drv_sdio_wait_read_done8uint32_t"></a> <a id="_CPPv223drv_sdio_wait_read_done8uint32_t"></a> <a id="drv_sdio_wait_read_done__uint32_t"></a> <a id="drv__sdio_8h_1a34988dd5691bb02a9edc1c6b5b89ba8e"></a> int32\_t drv\_sdio\_wait\_read\_done(uint32\_t dev\_instance)
:   wait read data done

    函数是阻塞式等待slave响应，不能与drv\_sdio\_interrupt\_callback\_register进行混用

    参数:
    :   **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424drv_sdio_wait_write_done8uint32_t"></a>

<a id="_CPPv324drv_sdio_wait_write_done8uint32_t"></a> <a id="_CPPv224drv_sdio_wait_write_done8uint32_t"></a> <a id="drv_sdio_wait_write_done__uint32_t"></a> <a id="drv__sdio_8h_1a186cc7bab8b2f79599ca940d29011696"></a> int32\_t drv\_sdio\_wait\_write\_done(uint32\_t dev\_instance)
:   wait read data done

    函数是阻塞式等待host发送数据完成，，不能与drv\_sdio\_interrupt\_callback\_register进行混用

    参数:
    :   **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv436drv_sdio_interrupt_callback_register8uint32_t15pfunc_sdio_cb_tPv"></a>

<a id="_CPPv336drv_sdio_interrupt_callback_register8uint32_t15pfunc_sdio_cb_tPv"></a> <a id="_CPPv236drv_sdio_interrupt_callback_register8uint32_t15pfunc_sdio_cb_tPv"></a> <a id="drv_sdio_interrupt_callback_register__uint32_t.pfunc_sdio_cb_t.voidP"></a> <a id="drv__sdio_8h_1a69d4acdcb872f69c2dbad318a1955627"></a> int32\_t drv\_sdio\_interrupt\_callback\_register(uint32\_t dev\_instance, [pfunc\_sdio\_cb\_t](#_CPPv415pfunc_sdio_cb_t "pfunc_sdio_cb_t") pfn\_cb, void \*pv\_arg)
:   register callback to sdio drvier

    注册了此函数，sdio的操作结果将通过回调函数通知用户。 此函数不能drv\_sdio\_wait\_write\_done(),[drv\_sdio\_wait\_read\_done()](#drv__sdio_8h_1a34988dd5691bb02a9edc1c6b5b89ba8e),[drv\_sdio\_wait\_cmd\_rsp()](#drv__sdio_8h_1a503465a40a03b49ec1bebf34a8fa2b8d)进行混用

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pfn\_cb** – **\[in\]** callback function for async recevie. it can be NULL if you do not want async recevie
        - **pv\_arg** – **\[in\]** callback function paramters

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425drv_sdio_get_rx_fifo_addr8uint32_t"></a>

<a id="_CPPv325drv_sdio_get_rx_fifo_addr8uint32_t"></a> <a id="_CPPv225drv_sdio_get_rx_fifo_addr8uint32_t"></a> <a id="drv_sdio_get_rx_fifo_addr__uint32_t"></a> <a id="drv__sdio_8h_1a0dd57438b57e9cec39fd32723f123fa6"></a> uint32\_t drv\_sdio\_get\_rx\_fifo\_addr(uint32\_t dev\_instance)
:   get rx fifo address

    参数:
    :   **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)

    返回:
    :   address

<a id="_CPPv425drv_sdio_get_tx_fifo_addr8uint32_t"></a>

<a id="_CPPv325drv_sdio_get_tx_fifo_addr8uint32_t"></a> <a id="_CPPv225drv_sdio_get_tx_fifo_addr8uint32_t"></a> <a id="drv_sdio_get_tx_fifo_addr__uint32_t"></a> <a id="drv__sdio_8h_1a2efa1f4717b2c657fcaad3cdaa0779e4"></a> uint32\_t drv\_sdio\_get\_tx\_fifo\_addr(uint32\_t dev\_instance)
:   get tx fifo address

    参数:
    :   **dev\_instance** – **\[in\]** return value of [drv\_spi\_init()](drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)

    返回:
    :   address

<a id="_CPPv421drv_sdio_set_tx_empty8uint32_t8uint32_t"></a>

<a id="_CPPv321drv_sdio_set_tx_empty8uint32_t8uint32_t"></a> <a id="_CPPv221drv_sdio_set_tx_empty8uint32_t8uint32_t"></a> <a id="drv_sdio_set_tx_empty__uint32_t.uint32_t"></a> <a id="drv__sdio_8h_1aa23e232b2c5bd2c036fca49cf4dc97a6"></a> int32\_t drv\_sdio\_set\_tx\_empty(uint32\_t dev\_instance, uint32\_t enable)

<a id="_CPPv427drv_sdio_wait_tx_fifo_empty8uint32_t"></a>

<a id="_CPPv327drv_sdio_wait_tx_fifo_empty8uint32_t"></a> <a id="_CPPv227drv_sdio_wait_tx_fifo_empty8uint32_t"></a> <a id="drv_sdio_wait_tx_fifo_empty__uint32_t"></a> <a id="drv__sdio_8h_1a4ec8aac8c5d61f2b31f0834bac666b6b"></a> int32\_t drv\_sdio\_wait\_tx\_fifo\_empty(uint32\_t dev\_instance)

<a id="_CPPv417drv_sdio_sd_reset8uint32_t"></a>

<a id="_CPPv317drv_sdio_sd_reset8uint32_t"></a> <a id="_CPPv217drv_sdio_sd_reset8uint32_t"></a> <a id="drv_sdio_sd_reset__uint32_t"></a> <a id="drv__sdio_8h_1aa30f440bb553a9df1a270c0cf3c372d5"></a> int32\_t drv\_sdio\_sd\_reset(uint32\_t dev\_instance)

<a id="_CPPv425drv_sdio_clear_wr_end_int8uint32_t"></a>

<a id="_CPPv325drv_sdio_clear_wr_end_int8uint32_t"></a> <a id="_CPPv225drv_sdio_clear_wr_end_int8uint32_t"></a> <a id="drv_sdio_clear_wr_end_int__uint32_t"></a> <a id="drv__sdio_8h_1a413047b5a86afd3042ceaf2add47f0e0"></a> int32\_t drv\_sdio\_clear\_wr\_end\_int(uint32\_t dev\_instance)

<a id="structures"></a>

### Structures

<a id="_CPPv417sdio_cmd_config_t"></a>

<a id="_CPPv317sdio_cmd_config_t"></a> <a id="_CPPv217sdio_cmd_config_t"></a> <a id="sdio_cmd_config_t"></a> <a id="structsdio__cmd__config__t"></a> struct sdio\_cmd\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17sdio_cmd_config_t9cmd_indexE"></a>

    <a id="_CPPv3N17sdio_cmd_config_t9cmd_indexE"></a> <a id="_CPPv2N17sdio_cmd_config_t9cmd_indexE"></a> <a id="sdio_cmd_config_t::cmd_index__uint32_t"></a> <a id="structsdio__cmd__config__t_1a67c5576a5cc56265a500a871ddce9a92"></a> uint32\_t cmd\_index
    :   sdio command index, between 0 and 63

    <a id="_CPPv4N17sdio_cmd_config_t8argumentE"></a>

    <a id="_CPPv3N17sdio_cmd_config_t8argumentE"></a> <a id="_CPPv2N17sdio_cmd_config_t8argumentE"></a> <a id="sdio_cmd_config_t::argument__uint32_t"></a> <a id="structsdio__cmd__config__t_1a9e1419043bdc0ab15848333710095a6b"></a> uint32\_t argument
    :   sdio command argument

    <a id="_CPPv4N17sdio_cmd_config_t8responseE"></a>

    <a id="_CPPv3N17sdio_cmd_config_t8responseE"></a> <a id="_CPPv2N17sdio_cmd_config_t8responseE"></a> <a id="sdio_cmd_config_t::response__sdio_cmd_rsp_e"></a> <a id="structsdio__cmd__config__t_1a932ea127c4af34312458a42c77ba94f8"></a> [sdio\_cmd\_rsp\_e](#_CPPv414sdio_cmd_rsp_e "sdio_cmd_rsp_e") response
    :   sdio command response type

    <a id="_CPPv4N17sdio_cmd_config_t16wait_rsp_timeoutE"></a>

    <a id="_CPPv3N17sdio_cmd_config_t16wait_rsp_timeoutE"></a> <a id="_CPPv2N17sdio_cmd_config_t16wait_rsp_timeoutE"></a> <a id="sdio_cmd_config_t::wait_rsp_timeout__uint32_t"></a> <a id="structsdio__cmd__config__t_1a666b7783d243185fe6689d7a4feb2a98"></a> uint32\_t wait\_rsp\_timeout
    :   sdio wait for slave command response timeout

    <a id="_CPPv4N17sdio_cmd_config_t9crc_checkE"></a>

    <a id="_CPPv3N17sdio_cmd_config_t9crc_checkE"></a> <a id="_CPPv2N17sdio_cmd_config_t9crc_checkE"></a> <a id="sdio_cmd_config_t::crc_check__b"></a> <a id="structsdio__cmd__config__t_1acadf33e15598be21ff923234aad86f4d"></a> bool crc\_check
    :   sdio whether need to check slave response crc value

<a id="_CPPv418sdio_data_config_t"></a>

<a id="_CPPv318sdio_data_config_t"></a> <a id="_CPPv218sdio_data_config_t"></a> <a id="sdio_data_config_t"></a> <a id="structsdio__data__config__t"></a> struct sdio\_data\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18sdio_data_config_t8data_dirE"></a>

    <a id="_CPPv3N18sdio_data_config_t8data_dirE"></a> <a id="_CPPv2N18sdio_data_config_t8data_dirE"></a> <a id="sdio_data_config_t::data_dir__sdio_data_direction_e"></a> <a id="structsdio__data__config__t_1add4f9f44f39e54db41bb325a5e9d5d20"></a> [sdio\_data\_direction\_e](#_CPPv421sdio_data_direction_e "sdio_data_direction_e") data\_dir
    :   sdio data direction

    <a id="_CPPv4N18sdio_data_config_t16multi_block_flagE"></a>

    <a id="_CPPv3N18sdio_data_config_t16multi_block_flagE"></a> <a id="_CPPv2N18sdio_data_config_t16multi_block_flagE"></a> <a id="sdio_data_config_t::multi_block_flag__b"></a> <a id="structsdio__data__config__t_1a60185dc98b48c4db90039727f5559367"></a> bool multi\_block\_flag
    :   sdio received data multiple blocks true: multiple blocks flash: single block

    <a id="_CPPv4N18sdio_data_config_t15data_block_sizeE"></a>

    <a id="_CPPv3N18sdio_data_config_t15data_block_sizeE"></a> <a id="_CPPv2N18sdio_data_config_t15data_block_sizeE"></a> <a id="sdio_data_config_t::data_block_size__uint32_t"></a> <a id="structsdio__data__config__t_1a1039e018ea87b0d6e5c681b821dc0034"></a> uint32\_t data\_block\_size
    :   sdio data block size

    <a id="_CPPv4N18sdio_data_config_t12data_timeoutE"></a>

    <a id="_CPPv3N18sdio_data_config_t12data_timeoutE"></a> <a id="_CPPv2N18sdio_data_config_t12data_timeoutE"></a> <a id="sdio_data_config_t::data_timeout__uint32_t"></a> <a id="structsdio__data__config__t_1a522f442e42452248d2e18bdb8918e367"></a> uint32\_t data\_timeout
    :   sdio data timeout

    <a id="_CPPv4N18sdio_data_config_t8data_lenE"></a>

    <a id="_CPPv3N18sdio_data_config_t8data_lenE"></a> <a id="_CPPv2N18sdio_data_config_t8data_lenE"></a> <a id="sdio_data_config_t::data_len__uint32_t"></a> <a id="structsdio__data__config__t_1abc92f9e4cb0fa4de563321265a2f5b62"></a> uint32\_t data\_len
    :   sdio data length

    <a id="_CPPv4N18sdio_data_config_t9bus_widthE"></a>

    <a id="_CPPv3N18sdio_data_config_t9bus_widthE"></a> <a id="_CPPv2N18sdio_data_config_t9bus_widthE"></a> <a id="sdio_data_config_t::bus_width__sdio_bus_width_e"></a> <a id="structsdio__data__config__t_1a5885ea2d095987a5d7403d0e3ed9f65c"></a> [sdio\_bus\_width\_e](#_CPPv416sdio_bus_width_e "sdio_bus_width_e") bus\_width
    :   sdio data bus width

    <a id="_CPPv4N18sdio_data_config_t13data_byte_selE"></a>

    <a id="_CPPv3N18sdio_data_config_t13data_byte_selE"></a> <a id="_CPPv2N18sdio_data_config_t13data_byte_selE"></a> <a id="sdio_data_config_t::data_byte_sel__sdio_data_byte_sel_e"></a> <a id="structsdio__data__config__t_1a20cb6d5502775bbae007f485af0e4c6c"></a> [sdio\_data\_byte\_sel\_e](#_CPPv420sdio_data_byte_sel_e "sdio_data_byte_sel_e") data\_byte\_sel
    :   sdio wires transfer data with little-endian or big-endian

<a id="macros"></a>

### Macros

<a id="c.SDIO_DEV_NUM"></a>

<a id="drv__sdio_8h_1af1aeb5b5a02d4f642074ae2025eca165"></a> SDIO\_DEV\_NUM

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv415pfunc_sdio_cb_t"></a>

<a id="_CPPv315pfunc_sdio_cb_t"></a> <a id="_CPPv215pfunc_sdio_cb_t"></a> <a id="pfunc_sdio_cb_t"></a> <a id="drv__sdio_8h_1a63234210e792b389194396f1e3ff5704"></a> typedef void (\*pfunc\_sdio\_cb\_t)(int32\_t status, [sdio\_op\_type\_e](#_CPPv414sdio_op_type_e "sdio_op_type_e") op\_type, void \*param)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv415sdio_response_e"></a>

<a id="_CPPv315sdio_response_e"></a> <a id="_CPPv215sdio_response_e"></a> <a id="drv__sdio_8h_1a62d4bab023a4d2f3b9b81b06748a3cff"></a> enum sdio\_response\_e
:   *Values:*

    <a id="_CPPv4N15sdio_response_e9SDIO_RSP0E"></a>

    <a id="_CPPv3N15sdio_response_e9SDIO_RSP0E"></a> <a id="_CPPv2N15sdio_response_e9SDIO_RSP0E"></a> <a id="drv__sdio_8h_1a62d4bab023a4d2f3b9b81b06748a3cffadbea8458d8da53859841bdfc579fd752"></a> enumerator SDIO\_RSP0
    :   sdio response regiseter 0

    <a id="_CPPv4N15sdio_response_e9SDIO_RSP1E"></a>

    <a id="_CPPv3N15sdio_response_e9SDIO_RSP1E"></a> <a id="_CPPv2N15sdio_response_e9SDIO_RSP1E"></a> <a id="drv__sdio_8h_1a62d4bab023a4d2f3b9b81b06748a3cffa639b0ba7d3c105560e58de2de17d03e8"></a> enumerator SDIO\_RSP1
    :   sdio response regiseter 1

    <a id="_CPPv4N15sdio_response_e9SDIO_RSP2E"></a>

    <a id="_CPPv3N15sdio_response_e9SDIO_RSP2E"></a> <a id="_CPPv2N15sdio_response_e9SDIO_RSP2E"></a> <a id="drv__sdio_8h_1a62d4bab023a4d2f3b9b81b06748a3cffa90f851a307f3f6eacf00d1e7b5e6d16c"></a> enumerator SDIO\_RSP2
    :   sdio response regiseter 2

    <a id="_CPPv4N15sdio_response_e9SDIO_RSP3E"></a>

    <a id="_CPPv3N15sdio_response_e9SDIO_RSP3E"></a> <a id="_CPPv2N15sdio_response_e9SDIO_RSP3E"></a> <a id="drv__sdio_8h_1a62d4bab023a4d2f3b9b81b06748a3cffa1311220621ef4ab71a496c66e81d9f6e"></a> enumerator SDIO\_RSP3
    :   sdio response regiseter 3

<a id="_CPPv414sdio_cmd_rsp_e"></a>

<a id="_CPPv314sdio_cmd_rsp_e"></a> <a id="_CPPv214sdio_cmd_rsp_e"></a> <a id="drv__sdio_8h_1ac3f99ec96ae1788998e5f03334cbe5c1"></a> enum sdio\_cmd\_rsp\_e
:   *Values:*

    <a id="_CPPv4N14sdio_cmd_rsp_e17SDIO_CMD_RSP_NONEE"></a>

    <a id="_CPPv3N14sdio_cmd_rsp_e17SDIO_CMD_RSP_NONEE"></a> <a id="_CPPv2N14sdio_cmd_rsp_e17SDIO_CMD_RSP_NONEE"></a> <a id="drv__sdio_8h_1ac3f99ec96ae1788998e5f03334cbe5c1af526a55c779c8e952add91bc0b40d5c1"></a> enumerator SDIO\_CMD\_RSP\_NONE
    :   sdio not need slave respond the command

    <a id="_CPPv4N14sdio_cmd_rsp_e18SDIO_CMD_RSP_SHORTE"></a>

    <a id="_CPPv3N14sdio_cmd_rsp_e18SDIO_CMD_RSP_SHORTE"></a> <a id="_CPPv2N14sdio_cmd_rsp_e18SDIO_CMD_RSP_SHORTE"></a> <a id="drv__sdio_8h_1ac3f99ec96ae1788998e5f03334cbe5c1a678af30bf76c24db296ae1add6659bbc"></a> enumerator SDIO\_CMD\_RSP\_SHORT
    :   sdio need slave long response

    <a id="_CPPv4N14sdio_cmd_rsp_e17SDIO_CMD_RSP_LONGE"></a>

    <a id="_CPPv3N14sdio_cmd_rsp_e17SDIO_CMD_RSP_LONGE"></a> <a id="_CPPv2N14sdio_cmd_rsp_e17SDIO_CMD_RSP_LONGE"></a> <a id="drv__sdio_8h_1ac3f99ec96ae1788998e5f03334cbe5c1ad91601fb5c9c96eb4901fe8636d11101"></a> enumerator SDIO\_CMD\_RSP\_LONG
    :   sdio need slave short response

<a id="_CPPv421sdio_data_direction_e"></a>

<a id="_CPPv321sdio_data_direction_e"></a> <a id="_CPPv221sdio_data_direction_e"></a> <a id="drv__sdio_8h_1a1fd756025d87a2194291d4d2ee7a6895"></a> enum sdio\_data\_direction\_e
:   *Values:*

    <a id="_CPPv4N21sdio_data_direction_e16SDIO_DATA_DIR_RDE"></a>

    <a id="_CPPv3N21sdio_data_direction_e16SDIO_DATA_DIR_RDE"></a> <a id="_CPPv2N21sdio_data_direction_e16SDIO_DATA_DIR_RDE"></a> <a id="drv__sdio_8h_1a1fd756025d87a2194291d4d2ee7a6895a47acc1a987559f987d48bb959e61895f"></a> enumerator SDIO\_DATA\_DIR\_RD
    :   sdio data direction read

    <a id="_CPPv4N21sdio_data_direction_e16SDIO_DATA_DIR_WRE"></a>

    <a id="_CPPv3N21sdio_data_direction_e16SDIO_DATA_DIR_WRE"></a> <a id="_CPPv2N21sdio_data_direction_e16SDIO_DATA_DIR_WRE"></a> <a id="drv__sdio_8h_1a1fd756025d87a2194291d4d2ee7a6895a1a9655970bbbdb6cf05bcce852c283b3"></a> enumerator SDIO\_DATA\_DIR\_WR
    :   sdio data direction write

<a id="_CPPv416sdio_clock_src_e"></a>

<a id="_CPPv316sdio_clock_src_e"></a> <a id="_CPPv216sdio_clock_src_e"></a> <a id="drv__sdio_8h_1af7472bcee89dae010512c9a523b66282"></a> enum sdio\_clock\_src\_e
:   *Values:*

    <a id="_CPPv4N16sdio_clock_src_e13SDIO_CLK_XTALE"></a>

    <a id="_CPPv3N16sdio_clock_src_e13SDIO_CLK_XTALE"></a> <a id="_CPPv2N16sdio_clock_src_e13SDIO_CLK_XTALE"></a> <a id="drv__sdio_8h_1af7472bcee89dae010512c9a523b66282a3c11695062b69b1bc7ba3c92ac7fc973"></a> enumerator SDIO\_CLK\_XTAL
    :   sdio clk source, XTAL 26M

    <a id="_CPPv4N16sdio_clock_src_e13SDIO_CLK_DPLLE"></a>

    <a id="_CPPv3N16sdio_clock_src_e13SDIO_CLK_DPLLE"></a> <a id="_CPPv2N16sdio_clock_src_e13SDIO_CLK_DPLLE"></a> <a id="drv__sdio_8h_1af7472bcee89dae010512c9a523b66282af2b666327e62892f492d21bcce0c704b"></a> enumerator SDIO\_CLK\_DPLL
    :   sdio clk source, DPLL top:336M

<a id="_CPPv416sdio_clock_div_e"></a>

<a id="_CPPv316sdio_clock_div_e"></a> <a id="_CPPv216sdio_clock_div_e"></a> <a id="drv__sdio_8h_1ab92295f39f5911adebedb2edca570faf"></a> enum sdio\_clock\_div\_e
:   *Values:*

    <a id="_CPPv4N16sdio_clock_div_e13SDIO_CLK_DIV1E"></a>

    <a id="_CPPv3N16sdio_clock_div_e13SDIO_CLK_DIV1E"></a> <a id="_CPPv2N16sdio_clock_div_e13SDIO_CLK_DIV1E"></a> <a id="drv__sdio_8h_1ab92295f39f5911adebedb2edca570fafa94f08e1602adf54607df3a1ae1981d57"></a> enumerator SDIO\_CLK\_DIV1
    :   sdio clk source, division 1

    <a id="_CPPv4N16sdio_clock_div_e13SDIO_CLK_DIV2E"></a>

    <a id="_CPPv3N16sdio_clock_div_e13SDIO_CLK_DIV2E"></a> <a id="_CPPv2N16sdio_clock_div_e13SDIO_CLK_DIV2E"></a> <a id="drv__sdio_8h_1ab92295f39f5911adebedb2edca570fafad2f4cc9ec127cc577fd0a214426ef900"></a> enumerator SDIO\_CLK\_DIV2
    :   sdio clk source, division 2

    <a id="_CPPv4N16sdio_clock_div_e13SDIO_CLK_DIV3E"></a>

    <a id="_CPPv3N16sdio_clock_div_e13SDIO_CLK_DIV3E"></a> <a id="_CPPv2N16sdio_clock_div_e13SDIO_CLK_DIV3E"></a> <a id="drv__sdio_8h_1ab92295f39f5911adebedb2edca570fafadb1e68961a4bab1fb3d32d74f57827aa"></a> enumerator SDIO\_CLK\_DIV3
    :   sdio clk source, division 3

    <a id="_CPPv4N16sdio_clock_div_e13SDIO_CLK_DIV4E"></a>

    <a id="_CPPv3N16sdio_clock_div_e13SDIO_CLK_DIV4E"></a> <a id="_CPPv2N16sdio_clock_div_e13SDIO_CLK_DIV4E"></a> <a id="drv__sdio_8h_1ab92295f39f5911adebedb2edca570fafa2d980eeda84a8672426fbc08b8fb658a"></a> enumerator SDIO\_CLK\_DIV4
    :   sdio clk source, division 4

    <a id="_CPPv4N16sdio_clock_div_e13SDIO_CLK_DIV5E"></a>

    <a id="_CPPv3N16sdio_clock_div_e13SDIO_CLK_DIV5E"></a> <a id="_CPPv2N16sdio_clock_div_e13SDIO_CLK_DIV5E"></a> <a id="drv__sdio_8h_1ab92295f39f5911adebedb2edca570fafa898d2b6def551566b73f179107b4623b"></a> enumerator SDIO\_CLK\_DIV5
    :   sdio clk source, division 5

    <a id="_CPPv4N16sdio_clock_div_e13SDIO_CLK_DIV6E"></a>

    <a id="_CPPv3N16sdio_clock_div_e13SDIO_CLK_DIV6E"></a> <a id="_CPPv2N16sdio_clock_div_e13SDIO_CLK_DIV6E"></a> <a id="drv__sdio_8h_1ab92295f39f5911adebedb2edca570fafa9bf2f69a797b35c49e8738a50d3164e9"></a> enumerator SDIO\_CLK\_DIV6
    :   sdio clk source, division 6

    <a id="_CPPv4N16sdio_clock_div_e13SDIO_CLK_DIV7E"></a>

    <a id="_CPPv3N16sdio_clock_div_e13SDIO_CLK_DIV7E"></a> <a id="_CPPv2N16sdio_clock_div_e13SDIO_CLK_DIV7E"></a> <a id="drv__sdio_8h_1ab92295f39f5911adebedb2edca570fafaaa127db3c614057346dadd784b6b2878"></a> enumerator SDIO\_CLK\_DIV7
    :   sdio clk source, division 7

    <a id="_CPPv4N16sdio_clock_div_e13SDIO_CLK_DIV8E"></a>

    <a id="_CPPv3N16sdio_clock_div_e13SDIO_CLK_DIV8E"></a> <a id="_CPPv2N16sdio_clock_div_e13SDIO_CLK_DIV8E"></a> <a id="drv__sdio_8h_1ab92295f39f5911adebedb2edca570fafa9eb5cd1f0534f24c0d5d7ac96ffc6372"></a> enumerator SDIO\_CLK\_DIV8
    :   sdio clk source, division 8

<a id="_CPPv416sdio_bus_width_e"></a>

<a id="_CPPv316sdio_bus_width_e"></a> <a id="_CPPv216sdio_bus_width_e"></a> <a id="drv__sdio_8h_1ad1eeca9ab57598f2e0d6353716ec25df"></a> enum sdio\_bus\_width\_e
:   *Values:*

    <a id="_CPPv4N16sdio_bus_width_e20SDIO_BUS_WIDTH_1LINEE"></a>

    <a id="_CPPv3N16sdio_bus_width_e20SDIO_BUS_WIDTH_1LINEE"></a> <a id="_CPPv2N16sdio_bus_width_e20SDIO_BUS_WIDTH_1LINEE"></a> <a id="drv__sdio_8h_1ad1eeca9ab57598f2e0d6353716ec25dfa1faaf49e0643b2eb9a3751b55f4d68fb"></a> enumerator SDIO\_BUS\_WIDTH\_1LINE
    :   sdio bus width 1 line

    <a id="_CPPv4N16sdio_bus_width_e20SDIO_BUS_WIDTH_4LINEE"></a>

    <a id="_CPPv3N16sdio_bus_width_e20SDIO_BUS_WIDTH_4LINEE"></a> <a id="_CPPv2N16sdio_bus_width_e20SDIO_BUS_WIDTH_4LINEE"></a> <a id="drv__sdio_8h_1ad1eeca9ab57598f2e0d6353716ec25dfaa49186b1322313dbfa612bce641b6ca7"></a> enumerator SDIO\_BUS\_WIDTH\_4LINE
    :   sdio bus width 4 line

<a id="_CPPv420sdio_data_byte_sel_e"></a>

<a id="_CPPv320sdio_data_byte_sel_e"></a> <a id="_CPPv220sdio_data_byte_sel_e"></a> <a id="drv__sdio_8h_1a2e3b54fd7cb2cd3cf77eaf03271d913c"></a> enum sdio\_data\_byte\_sel\_e
:   *Values:*

    <a id="_CPPv4N20sdio_data_byte_sel_e23SDIO_DATA_LITTLE_ENDIANE"></a>

    <a id="_CPPv3N20sdio_data_byte_sel_e23SDIO_DATA_LITTLE_ENDIANE"></a> <a id="_CPPv2N20sdio_data_byte_sel_e23SDIO_DATA_LITTLE_ENDIANE"></a> <a id="drv__sdio_8h_1a2e3b54fd7cb2cd3cf77eaf03271d913ca489aac9c75aa2486e18e8703990b3a3d"></a> enumerator SDIO\_DATA\_LITTLE\_ENDIAN
    :   sdio wires transfer data with little-endian

    <a id="_CPPv4N20sdio_data_byte_sel_e20SDIO_DATA_BIG_ENDIANE"></a>

    <a id="_CPPv3N20sdio_data_byte_sel_e20SDIO_DATA_BIG_ENDIANE"></a> <a id="_CPPv2N20sdio_data_byte_sel_e20SDIO_DATA_BIG_ENDIANE"></a> <a id="drv__sdio_8h_1a2e3b54fd7cb2cd3cf77eaf03271d913ca221b1d9fc2011ac35c1ddbfb6b3502ff"></a> enumerator SDIO\_DATA\_BIG\_ENDIAN
    :   sdio wires transfer data with big-endian

<a id="_CPPv414sdio_op_type_e"></a>

<a id="_CPPv314sdio_op_type_e"></a> <a id="_CPPv214sdio_op_type_e"></a> <a id="drv__sdio_8h_1a077a1210e7deb683cbf09337ea47c650"></a> enum sdio\_op\_type\_e
:   *Values:*

    <a id="_CPPv4N14sdio_op_type_e11SDIO_CMD_OPE"></a>

    <a id="_CPPv3N14sdio_op_type_e11SDIO_CMD_OPE"></a> <a id="_CPPv2N14sdio_op_type_e11SDIO_CMD_OPE"></a> <a id="drv__sdio_8h_1a077a1210e7deb683cbf09337ea47c650ace13565b280f1c543149ec6dfbf53a3c"></a> enumerator SDIO\_CMD\_OP
    :   sdio command operation

    <a id="_CPPv4N14sdio_op_type_e12SDIO_DATA_OPE"></a>

    <a id="_CPPv3N14sdio_op_type_e12SDIO_DATA_OPE"></a> <a id="_CPPv2N14sdio_op_type_e12SDIO_DATA_OPE"></a> <a id="drv__sdio_8h_1a077a1210e7deb683cbf09337ea47c650a23a657696d4cdd0c18129a36cef79822"></a> enumerator SDIO\_DATA\_OP
    :   sdio data operation
