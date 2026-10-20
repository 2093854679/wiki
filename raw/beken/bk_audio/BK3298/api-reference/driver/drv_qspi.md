---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_qspi.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-qspi"></a>

# DRV\_QSPI

<a id="drv-qspi-api-status"></a>

## DRV\_QSPI API Status

| API |
| --- |
| [`drv_qspi_init()`](#_CPPv413drv_qspi_init7uint8_t "drv_qspi_init") |
| [`drv_qspi_deinit()`](#_CPPv415drv_qspi_deinit8uint32_t "drv_qspi_deinit") |
| [`drv_qspi_config()`](#_CPPv415drv_qspi_config8uint32_tP13qspi_config_t "drv_qspi_config") |
| [`drv_qspi_write()`](#_CPPv414drv_qspi_write8uint32_tP15qspi_xfer_blk_t15pfunc_qspi_cb_tPv "drv_qspi_write") |
| [`drv_qspi_read()`](#_CPPv413drv_qspi_read8uint32_tP15qspi_xfer_blk_t15pfunc_qspi_cb_tPv "drv_qspi_read") |
| [`drv_qspi_lcd_data_op_config()`](#_CPPv427drv_qspi_lcd_data_op_config8uint32_tP14qspi_lcd_cfg_t "drv_qspi_lcd_data_op_config") |
| [`drv_qspi_dma_data_op_config()`](#_CPPv427drv_qspi_dma_data_op_config8uint32_t16qspi_line_mode_e "drv_qspi_dma_data_op_config") |
| [`drv_qspi_get_write_data_address()`](#_CPPv431drv_qspi_get_write_data_address8uint32_t21qspi_dest_addr_type_e "drv_qspi_get_write_data_address") |
| [`drv_qspi_cs_low_force_enable()`](#_CPPv428drv_qspi_cs_low_force_enable8uint32_t "drv_qspi_cs_low_force_enable") |
| [`drv_qspi_cs_low_force_disable()`](#_CPPv429drv_qspi_cs_low_force_disable8uint32_t "drv_qspi_cs_low_force_disable") |
| [`drv_qspi_cmd_clk_open()`](#_CPPv421drv_qspi_cmd_clk_open8uint32_t "drv_qspi_cmd_clk_open") |
| [`drv_qspi_cmd_clk_close()`](#_CPPv422drv_qspi_cmd_clk_close8uint32_t "drv_qspi_cmd_clk_close") |
| [`drv_qspi_work_mode_set()`](#_CPPv422drv_qspi_work_mode_set8uint32_t16qspi_work_mode_e "drv_qspi_work_mode_set") |

<a id="drv-qspi-unit-number"></a>

## DRV\_QSPI UNIT Number

| Capability | Number |
| --- | --- |
| UNIT Number | 2 |

<a id="drv-qspi-pin-and-gpio-map"></a>

## DRV\_QSPI Pin and GPIO Map

| QSPI Pin | Number |
| --- | --- |
| QSPI0 SCK | 20 |
| QSPI0 CS | 21 |
| QSPI0 DATA\[0\] | 22 |
| QSPI0 DATA\[1\] | 23 |
| QSPI0 DATA\[2\] | 24 |
| QSPI0 DATA\[3\] | 25 |
| QSPI1 SCK | 26 |
| QSPI1 CS | 27 |
| QSPI1 DATA\[0\] | 28 |
| QSPI1 DATA\[1\] | 29 |
| QSPI1 DATA\[2\] | 30 |
| QSPI1 DATA\[3\] | 31 |

<a id="drv-qspi-api-reference"></a>

## DRV\_QSPI API Reference

<a id="header-file"></a>

### Header File

- [driver/qspi/drv\_qspi.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/qspi/drv_qspi.h)

<a id="functions"></a>

### Functions

<a id="_CPPv413drv_qspi_init7uint8_t"></a>

<a id="_CPPv313drv_qspi_init7uint8_t"></a> <a id="_CPPv213drv_qspi_init7uint8_t"></a> <a id="drv_qspi_init__uint8_t"></a> <a id="drv__qspi_8h_1a307f65de17bd73cf9c93c0acd84cf993"></a> uint32\_t drv\_qspi\_init(uint8\_t dev\_index)
:   init a qspi device.

    初始化设备，在使用qspi功能前需要调用它获取device instance

    参数:
    :   **dev\_index** – **\[in\]** 参数说明部分

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv415drv_qspi_deinit8uint32_t"></a>

<a id="_CPPv315drv_qspi_deinit8uint32_t"></a> <a id="_CPPv215drv_qspi_deinit8uint32_t"></a> <a id="drv_qspi_deinit__uint32_t"></a> <a id="drv__qspi_8h_1acc91a83a31c09bc504eee37c22bf67ba"></a> int32\_t drv\_qspi\_deinit(uint32\_t dev\_instance)
:   deinit a qspi device.

    反初始化qspi设备，对drv\_qspi\_init()进行反向操作

    参数:
    :   **dev\_instance** – **\[in\]** 函数drv\_qspi\_init()返回的参数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv415drv_qspi_config8uint32_tP13qspi_config_t"></a>

<a id="_CPPv315drv_qspi_config8uint32_tP13qspi_config_t"></a> <a id="_CPPv215drv_qspi_config8uint32_tP13qspi_config_t"></a> <a id="drv_qspi_config__uint32_t.qspi_config_tP"></a> <a id="drv__qspi_8h_1a9cc19bf8fb2b100e8ece87a185fb25e5"></a> int32\_t drv\_qspi\_config(uint32\_t dev\_instance, [qspi\_config\_t](#_CPPv413qspi_config_t "qspi_config_t") \*p\_param)
:   config qspi parameter.

    对spi设备参数的配置，在配置前需要确保spi处于关闭状态

    参数:
    :   - **dev\_instance** – **\[in\]** 函数drv\_qspi\_init()返回的参数
        - **p\_param** – **\[in\]** 参数结构体指针

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv414drv_qspi_write8uint32_tP15qspi_xfer_blk_t15pfunc_qspi_cb_tPv"></a>

<a id="_CPPv314drv_qspi_write8uint32_tP15qspi_xfer_blk_t15pfunc_qspi_cb_tPv"></a> <a id="_CPPv214drv_qspi_write8uint32_tP15qspi_xfer_blk_t15pfunc_qspi_cb_tPv"></a> <a id="drv_qspi_write__uint32_t.qspi_xfer_blk_tP.pfunc_qspi_cb_t.voidP"></a> <a id="drv__qspi_8h_1a68bc5172944a80aa8770cb3d1ff446f4"></a> int32\_t drv\_qspi\_write(uint32\_t dev\_instance, [qspi\_xfer\_blk\_t](#_CPPv415qspi_xfer_blk_t "qspi_xfer_blk_t") \*p\_blk, [pfunc\_qspi\_cb\_t](#_CPPv415pfunc_qspi_cb_t "pfunc_qspi_cb_t") pfn\_cb, void \*pv\_arg)
:   qspi write

    qspi发送接口 如果pfn\_cb\=\=NULL，则该函数在把数据通过qspi送出去后才会返回 如果pfn\_cb!\=NULL，该函数会立即返回，等数据发送出去后通过 pfn\_cb进行通知

    参数:
    :   - **dev\_instance** – **\[in\]** 函数drv\_qspi\_init()返回的参数
        - **p\_blk** – **\[in\]** 发送结构体，参照结构体qspi\_xfer\_blk\_t
        - **pfn\_cb** – **\[in\]** 回调函数
        - **pv\_arg** – **\[in\]** 用于回调函数携带的参数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv413drv_qspi_read8uint32_tP15qspi_xfer_blk_t15pfunc_qspi_cb_tPv"></a>

<a id="_CPPv313drv_qspi_read8uint32_tP15qspi_xfer_blk_t15pfunc_qspi_cb_tPv"></a> <a id="_CPPv213drv_qspi_read8uint32_tP15qspi_xfer_blk_t15pfunc_qspi_cb_tPv"></a> <a id="drv_qspi_read__uint32_t.qspi_xfer_blk_tP.pfunc_qspi_cb_t.voidP"></a> <a id="drv__qspi_8h_1a7bf1d3ec71b4b88c72f3b100c23da0b4"></a> int32\_t drv\_qspi\_read(uint32\_t dev\_instance, [qspi\_xfer\_blk\_t](#_CPPv415qspi_xfer_blk_t "qspi_xfer_blk_t") \*p\_blk, [pfunc\_qspi\_cb\_t](#_CPPv415pfunc_qspi_cb_t "pfunc_qspi_cb_t") pfn\_cb, void \*pv\_arg)
:   qspi read

    qspi同步接收接口，接收完成才会返回 如果pfn\_cb\=\=NULL，则该函数通过qspi接收指定长度的数据后才会返回 如果pfn\_cb!\=NULL，该函数会立即返回，等数据接收完成后通过 pfn\_cb进行通知

    参数:
    :   - **dev\_instance** – **\[in\]** 函数drv\_qspi\_init()返回的参数
        - **p\_blk** – **\[in\]** 发送结构体，参照结构体qspi\_xfer\_blk\_t
        - **pfn\_cb** – **\[in\]** 回调函数
        - **pv\_arg** – **\[in\]** 用于回调函数携带的参数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427drv_qspi_lcd_data_op_config8uint32_tP14qspi_lcd_cfg_t"></a>

<a id="_CPPv327drv_qspi_lcd_data_op_config8uint32_tP14qspi_lcd_cfg_t"></a> <a id="_CPPv227drv_qspi_lcd_data_op_config8uint32_tP14qspi_lcd_cfg_t"></a> <a id="drv_qspi_lcd_data_op_config__uint32_t.qspi_lcd_cfg_tP"></a> <a id="drv__qspi_8h_1a0ac0ac0f78d3570af801a9fdd162d840"></a> int32\_t drv\_qspi\_lcd\_data\_op\_config(uint32\_t dev\_instance, [qspi\_lcd\_cfg\_t](#_CPPv414qspi_lcd_cfg_t "qspi_lcd_cfg_t") \*p\_config)
:   lcd operation config

    操作lcd设备，需要硬件自动添加头部，需要调用此接口进行配置

    参数:
    :   - **dev\_instance** – **\[in\]** 参数说明部分
        - **p\_config** – **\[in\]** 参数说明部分

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427drv_qspi_dma_data_op_config8uint32_t16qspi_line_mode_e"></a>

<a id="_CPPv327drv_qspi_dma_data_op_config8uint32_t16qspi_line_mode_e"></a> <a id="_CPPv227drv_qspi_dma_data_op_config8uint32_t16qspi_line_mode_e"></a> <a id="drv_qspi_dma_data_op_config__uint32_t.qspi_line_mode_e"></a> <a id="drv__qspi_8h_1acf43a924b07dbbb65d7a68e1850b26d2"></a> int32\_t drv\_qspi\_dma\_data\_op\_config(uint32\_t dev\_instance, [qspi\_line\_mode\_e](#_CPPv416qspi_line_mode_e "qspi_line_mode_e") data\_line\_mode)
:   only data send operation config

    DMA搬运向QPSI映射地址搬运数据的时候只发送用户数据，需要调用此接口进行配置

    参数:
    :   - **dev\_instance** – **\[in\]** 参数说明部分
        - **data\_line\_mode** – **\[in\]** 用户数据用几线发送

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – failban’yu

    返回:
    :   result

<a id="_CPPv431drv_qspi_get_write_data_address8uint32_t21qspi_dest_addr_type_e"></a>

<a id="_CPPv331drv_qspi_get_write_data_address8uint32_t21qspi_dest_addr_type_e"></a> <a id="_CPPv231drv_qspi_get_write_data_address8uint32_t21qspi_dest_addr_type_e"></a> <a id="drv_qspi_get_write_data_address__uint32_t.qspi_dest_addr_type_e"></a> <a id="drv__qspi_8h_1aa3484113506fe028f875a0cfe646318a"></a> uint32\_t drv\_qspi\_get\_write\_data\_address(uint32\_t dev\_instance, [qspi\_dest\_addr\_type\_e](#_CPPv421qspi_dest_addr_type_e "qspi_dest_addr_type_e") addr\_dest\_type)
:   get cpu map address for qpsi

    QSPI同步接收接口，接收完成才会返回

    参数:
    :   - **dev\_instance** – **\[in\]** 函数drv\_qspi\_init()返回的参数
        - **addr\_dest\_type** – **\[in\]** 获得的映射的地址是否使用cache

    返回:
    :   address cpu映射的地址块的首地址

<a id="_CPPv428drv_qspi_cs_low_force_enable8uint32_t"></a>

<a id="_CPPv328drv_qspi_cs_low_force_enable8uint32_t"></a> <a id="_CPPv228drv_qspi_cs_low_force_enable8uint32_t"></a> <a id="drv_qspi_cs_low_force_enable__uint32_t"></a> <a id="drv__qspi_8h_1a505832abac6aa0e8db061f18442e03e9"></a> int32\_t drv\_qspi\_cs\_low\_force\_enable(uint32\_t dev\_instance)
:   force cs low

    强制的把cs拉低

    参数:
    :   **dev\_instance** – **\[in\]** 函数drv\_qspi\_init()返回的参数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv429drv_qspi_cs_low_force_disable8uint32_t"></a>

<a id="_CPPv329drv_qspi_cs_low_force_disable8uint32_t"></a> <a id="_CPPv229drv_qspi_cs_low_force_disable8uint32_t"></a> <a id="drv_qspi_cs_low_force_disable__uint32_t"></a> <a id="drv__qspi_8h_1a1672c6b2ff942e42b76aca66c580c777"></a> int32\_t drv\_qspi\_cs\_low\_force\_disable(uint32\_t dev\_instance)
:   force cs low

    取消强制的把cs拉低

    参数:
    :   **dev\_instance** – **\[in\]** 函数drv\_qspi\_init()返回的参数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421drv_qspi_cmd_clk_open8uint32_t"></a>

<a id="_CPPv321drv_qspi_cmd_clk_open8uint32_t"></a> <a id="_CPPv221drv_qspi_cmd_clk_open8uint32_t"></a> <a id="drv_qspi_cmd_clk_open__uint32_t"></a> <a id="drv__qspi_8h_1a43d2dfb185d2db4c0f6dfa358e843aa5"></a> int32\_t drv\_qspi\_cmd\_clk\_open(uint32\_t dev\_instance)
:   取消QSPI发送cmd字段和address字段时的clk不输出

    参数:
    :   **dev\_instance** – **\[in\]** 函数drv\_qspi\_init()返回的参数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422drv_qspi_cmd_clk_close8uint32_t"></a>

<a id="_CPPv322drv_qspi_cmd_clk_close8uint32_t"></a> <a id="_CPPv222drv_qspi_cmd_clk_close8uint32_t"></a> <a id="drv_qspi_cmd_clk_close__uint32_t"></a> <a id="drv__qspi_8h_1aa8399bfec0b03d30dba2f643b1846183"></a> int32\_t drv\_qspi\_cmd\_clk\_close(uint32\_t dev\_instance)
:   QSPI发送cmd字段和address字段时的clk不输出

    参数:
    :   **dev\_instance** – **\[in\]** 函数drv\_qspi\_init()返回的参数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422drv_qspi_work_mode_set8uint32_t16qspi_work_mode_e"></a>

<a id="_CPPv322drv_qspi_work_mode_set8uint32_t16qspi_work_mode_e"></a> <a id="_CPPv222drv_qspi_work_mode_set8uint32_t16qspi_work_mode_e"></a> <a id="drv_qspi_work_mode_set__uint32_t.qspi_work_mode_e"></a> <a id="drv__qspi_8h_1af649c8b478c65e5ff20727d261b3b8da"></a> int32\_t drv\_qspi\_work\_mode\_set(uint32\_t dev\_instance, [qspi\_work\_mode\_e](#_CPPv416qspi_work_mode_e "qspi_work_mode_e") wire\_mode)
:   设置QSPI的工作模式，是通过IO输出，还是通过地址映射的方式

    IO输出是后续的data是发送fifo当中的数据 地址映射的方式是cpu或者dma对应的地址写数据，QSPI就转换成指定的QSPI协议通信

    参数:
    :   - **dev\_instance** – **\[in\]** 函数drv\_qspi\_init()返回的参数
        - **wire\_mode** – **\[in\]**

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv413qspi_config_t"></a>

<a id="_CPPv313qspi_config_t"></a> <a id="_CPPv213qspi_config_t"></a> <a id="qspi_config_t"></a> <a id="structqspi__config__t"></a> struct qspi\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N13qspi_config_t4cpolE"></a>

    <a id="_CPPv3N13qspi_config_t4cpolE"></a> <a id="_CPPv2N13qspi_config_t4cpolE"></a> <a id="qspi_config_t::cpol__qspi_cpol_e"></a> <a id="structqspi__config__t_1a6b41c64617fdee16de8aee1192b624d5"></a> [qspi\_cpol\_e](#_CPPv411qspi_cpol_e "qspi_cpol_e") cpol
    :   QSPI clock cpol

    <a id="_CPPv4N13qspi_config_t4cphaE"></a>

    <a id="_CPPv3N13qspi_config_t4cphaE"></a> <a id="_CPPv2N13qspi_config_t4cphaE"></a> <a id="qspi_config_t::cpha__qspi_cpha_e"></a> <a id="structqspi__config__t_1af582131845c979ae274e98dd0e2a8596"></a> [qspi\_cpha\_e](#_CPPv411qspi_cpha_e "qspi_cpha_e") cpha
    :   QSPI clock cpha

    <a id="_CPPv4N13qspi_config_t9bit_orderE"></a>

    <a id="_CPPv3N13qspi_config_t9bit_orderE"></a> <a id="_CPPv2N13qspi_config_t9bit_orderE"></a> <a id="qspi_config_t::bit_order__qspi_bit_order_e"></a> <a id="structqspi__config__t_1ab8da55d92d6be33160e6813d8d267873"></a> [qspi\_bit\_order\_e](#_CPPv416qspi_bit_order_e "qspi_bit_order_e") bit\_order
    :   QSPI bit order, MSB/LSB

    <a id="_CPPv4N13qspi_config_t3clkE"></a>

    <a id="_CPPv3N13qspi_config_t3clkE"></a> <a id="_CPPv2N13qspi_config_t3clkE"></a> <a id="qspi_config_t::clk__uint32_t"></a> <a id="structqspi__config__t_1a9753e7e560f33d6e319e0831a572b26d"></a> uint32\_t clk
    :   QSPI clock frequency

    <a id="_CPPv4N13qspi_config_t9baud_rateE"></a>

    <a id="_CPPv3N13qspi_config_t9baud_rateE"></a> <a id="_CPPv2N13qspi_config_t9baud_rateE"></a> <a id="qspi_config_t::baud_rate__uint32_t"></a> <a id="structqspi__config__t_1a250bd7911e26974ab3c021171a215ae2"></a> uint32\_t baud\_rate
    :   QSPI transmit and receive SCK clock

<a id="_CPPv415qspi_xfer_blk_t"></a>

<a id="_CPPv315qspi_xfer_blk_t"></a> <a id="_CPPv215qspi_xfer_blk_t"></a> <a id="qspi_xfer_blk_t"></a> <a id="structqspi__xfer__blk__t"></a> struct qspi\_xfer\_blk\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N15qspi_xfer_blk_t3cmdE"></a>

    <a id="_CPPv3N15qspi_xfer_blk_t3cmdE"></a> <a id="_CPPv2N15qspi_xfer_blk_t3cmdE"></a> <a id="qspi_xfer_blk_t::cmd__uint32_t"></a> <a id="structqspi__xfer__blk__t_1ac7841019eb6504284b21390acef20179"></a> uint32\_t cmd
    :   QSPI command

    <a id="_CPPv4N15qspi_xfer_blk_t7cmd_lenE"></a>

    <a id="_CPPv3N15qspi_xfer_blk_t7cmd_lenE"></a> <a id="_CPPv2N15qspi_xfer_blk_t7cmd_lenE"></a> <a id="qspi_xfer_blk_t::cmd_len__uint8_t"></a> <a id="structqspi__xfer__blk__t_1a58c8461b94e5be2863e152f35d3bf868"></a> uint8\_t cmd\_len
    :   QSPI command length byte 1 \~ 4

    <a id="_CPPv4N15qspi_xfer_blk_t13cmd_line_modeE"></a>

    <a id="_CPPv3N15qspi_xfer_blk_t13cmd_line_modeE"></a> <a id="_CPPv2N15qspi_xfer_blk_t13cmd_line_modeE"></a> <a id="qspi_xfer_blk_t::cmd_line_mode__qspi_line_mode_e"></a> <a id="structqspi__xfer__blk__t_1a758eacf00d06a21660e0508c3d48be7f"></a> [qspi\_line\_mode\_e](#_CPPv416qspi_line_mode_e "qspi_line_mode_e") cmd\_line\_mode
    :   QSPI command line mode

    <a id="_CPPv4N15qspi_xfer_blk_t4addrE"></a>

    <a id="_CPPv3N15qspi_xfer_blk_t4addrE"></a> <a id="_CPPv2N15qspi_xfer_blk_t4addrE"></a> <a id="qspi_xfer_blk_t::addr__uint32_t"></a> <a id="structqspi__xfer__blk__t_1a8f3fc46dc6f117b9ebffba03a4bb7af9"></a> uint32\_t addr
    :   QSPI address

    <a id="_CPPv4N15qspi_xfer_blk_t8addr_lenE"></a>

    <a id="_CPPv3N15qspi_xfer_blk_t8addr_lenE"></a> <a id="_CPPv2N15qspi_xfer_blk_t8addr_lenE"></a> <a id="qspi_xfer_blk_t::addr_len__uint32_t"></a> <a id="structqspi__xfer__blk__t_1a4027c080f5a2eec3c9be39726823e690"></a> uint32\_t addr\_len
    :   QSPI address len byte. normal value is 3

    <a id="_CPPv4N15qspi_xfer_blk_t14addr_line_modeE"></a>

    <a id="_CPPv3N15qspi_xfer_blk_t14addr_line_modeE"></a> <a id="_CPPv2N15qspi_xfer_blk_t14addr_line_modeE"></a> <a id="qspi_xfer_blk_t::addr_line_mode__qspi_line_mode_e"></a> <a id="structqspi__xfer__blk__t_1a19acf9cd2bbb362f1338e7d26048d48b"></a> [qspi\_line\_mode\_e](#_CPPv416qspi_line_mode_e "qspi_line_mode_e") addr\_line\_mode
    :   QSPI address line mode

    <a id="_CPPv4N15qspi_xfer_blk_t8data_lenE"></a>

    <a id="_CPPv3N15qspi_xfer_blk_t8data_lenE"></a> <a id="_CPPv2N15qspi_xfer_blk_t8data_lenE"></a> <a id="qspi_xfer_blk_t::data_len__uint32_t"></a> <a id="structqspi__xfer__blk__t_1a760be7e622972f6e136e2cca5363f500"></a> uint32\_t data\_len
    :   QSPI data length

    <a id="_CPPv4N15qspi_xfer_blk_t14data_line_modeE"></a>

    <a id="_CPPv3N15qspi_xfer_blk_t14data_line_modeE"></a> <a id="_CPPv2N15qspi_xfer_blk_t14data_line_modeE"></a> <a id="qspi_xfer_blk_t::data_line_mode__qspi_line_mode_e"></a> <a id="structqspi__xfer__blk__t_1aac8eeb33bfbb31f6fa74ee445d0612ac"></a> [qspi\_line\_mode\_e](#_CPPv416qspi_line_mode_e "qspi_line_mode_e") data\_line\_mode
    :   QSPI data line mode

    <a id="_CPPv4N15qspi_xfer_blk_t11dummy_cycleE"></a>

    <a id="_CPPv3N15qspi_xfer_blk_t11dummy_cycleE"></a> <a id="_CPPv2N15qspi_xfer_blk_t11dummy_cycleE"></a> <a id="qspi_xfer_blk_t::dummy_cycle__uint32_t"></a> <a id="structqspi__xfer__blk__t_1ace081b24e0d248af7ffd207e391bd0c5"></a> uint32\_t dummy\_cycle
    :   QSPI dummy cycle

<a id="_CPPv414qspi_lcd_cfg_t"></a>

<a id="_CPPv314qspi_lcd_cfg_t"></a> <a id="_CPPv214qspi_lcd_cfg_t"></a> <a id="qspi_lcd_cfg_t"></a> <a id="structqspi__lcd__cfg__t"></a> struct qspi\_lcd\_cfg\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14qspi_lcd_cfg_t13cmd_line_modeE"></a>

    <a id="_CPPv3N14qspi_lcd_cfg_t13cmd_line_modeE"></a> <a id="_CPPv2N14qspi_lcd_cfg_t13cmd_line_modeE"></a> <a id="qspi_lcd_cfg_t::cmd_line_mode__qspi_line_mode_e"></a> <a id="structqspi__lcd__cfg__t_1a5db32a78bc4e2c8404c1066d97d6194b"></a> [qspi\_line\_mode\_e](#_CPPv416qspi_line_mode_e "qspi_line_mode_e") cmd\_line\_mode
    :   QSPI command line mode

    <a id="_CPPv4N14qspi_lcd_cfg_t13reg_line_modeE"></a>

    <a id="_CPPv3N14qspi_lcd_cfg_t13reg_line_modeE"></a> <a id="_CPPv2N14qspi_lcd_cfg_t13reg_line_modeE"></a> <a id="qspi_lcd_cfg_t::reg_line_mode__qspi_line_mode_e"></a> <a id="structqspi__lcd__cfg__t_1abc663526624833e897e56b4c06713eaa"></a> [qspi\_line\_mode\_e](#_CPPv416qspi_line_mode_e "qspi_line_mode_e") reg\_line\_mode
    :   QSPI reg line mode

    <a id="_CPPv4N14qspi_lcd_cfg_t14data_line_modeE"></a>

    <a id="_CPPv3N14qspi_lcd_cfg_t14data_line_modeE"></a> <a id="_CPPv2N14qspi_lcd_cfg_t14data_line_modeE"></a> <a id="qspi_lcd_cfg_t::data_line_mode__qspi_line_mode_e"></a> <a id="structqspi__lcd__cfg__t_1a8212c08c693f8df8e36efa3b5d0da8cf"></a> [qspi\_line\_mode\_e](#_CPPv416qspi_line_mode_e "qspi_line_mode_e") data\_line\_mode
    :   QSPI data line mode

<a id="macros"></a>

### Macros

<a id="c.QSPI_DEVICE_NUM"></a>

<a id="drv__qspi_8h_1af7b9e56e37e1cddc9de13482e5e86d05"></a> QSPI\_DEVICE\_NUM

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv415pfunc_qspi_cb_t"></a>

<a id="_CPPv315pfunc_qspi_cb_t"></a> <a id="_CPPv215pfunc_qspi_cb_t"></a> <a id="pfunc_qspi_cb_t"></a> <a id="drv__qspi_8h_1abce411960079371658d93d98afb08cf3"></a> typedef void (\*pfunc\_qspi\_cb\_t)(uint32\_t dev\_instance, int32\_t err\_code, void \*param)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv411qspi_cpol_e"></a>

<a id="_CPPv311qspi_cpol_e"></a> <a id="_CPPv211qspi_cpol_e"></a> <a id="drv__qspi_8h_1afcdfd5e6263105cd458cb029d0c5efba"></a> enum qspi\_cpol\_e
:   *Values:*

    <a id="_CPPv4N11qspi_cpol_e11QSPI_CPOL_0E"></a>

    <a id="_CPPv3N11qspi_cpol_e11QSPI_CPOL_0E"></a> <a id="_CPPv2N11qspi_cpol_e11QSPI_CPOL_0E"></a> <a id="drv__qspi_8h_1afcdfd5e6263105cd458cb029d0c5efbaa192da8598ec66783dfd009b0208d450a"></a> enumerator QSPI\_CPOL\_0
    :   QSPI clock polarity low

    <a id="_CPPv4N11qspi_cpol_e11QSPI_CPOL_1E"></a>

    <a id="_CPPv3N11qspi_cpol_e11QSPI_CPOL_1E"></a> <a id="_CPPv2N11qspi_cpol_e11QSPI_CPOL_1E"></a> <a id="drv__qspi_8h_1afcdfd5e6263105cd458cb029d0c5efbaaecc24ed897f2ae359c33b643e9f2af20"></a> enumerator QSPI\_CPOL\_1
    :   QSPI clock polarity high

<a id="_CPPv411qspi_cpha_e"></a>

<a id="_CPPv311qspi_cpha_e"></a> <a id="_CPPv211qspi_cpha_e"></a> <a id="drv__qspi_8h_1a4b76038ac81d900553d99d203013a39d"></a> enum qspi\_cpha\_e
:   *Values:*

    <a id="_CPPv4N11qspi_cpha_e11QSPI_CPHA_0E"></a>

    <a id="_CPPv3N11qspi_cpha_e11QSPI_CPHA_0E"></a> <a id="_CPPv2N11qspi_cpha_e11QSPI_CPHA_0E"></a> <a id="drv__qspi_8h_1a4b76038ac81d900553d99d203013a39dacc2423ad9398cefa93dd97e6ab810ef7"></a> enumerator QSPI\_CPHA\_0
    :   QSPI clock phase the first edge

    <a id="_CPPv4N11qspi_cpha_e11QSPI_CPHA_1E"></a>

    <a id="_CPPv3N11qspi_cpha_e11QSPI_CPHA_1E"></a> <a id="_CPPv2N11qspi_cpha_e11QSPI_CPHA_1E"></a> <a id="drv__qspi_8h_1a4b76038ac81d900553d99d203013a39da2b598694085aeddeffb0a2b9ed1c0e75"></a> enumerator QSPI\_CPHA\_1
    :   QSPI clock phase the second edge

<a id="_CPPv416qspi_bit_order_e"></a>

<a id="_CPPv316qspi_bit_order_e"></a> <a id="_CPPv216qspi_bit_order_e"></a> <a id="drv__qspi_8h_1a64a853180dd8d518d2e3fdb035c615f4"></a> enum qspi\_bit\_order\_e
:   *Values:*

    <a id="_CPPv4N16qspi_bit_order_e14QSPI_MSB_FIRSTE"></a>

    <a id="_CPPv3N16qspi_bit_order_e14QSPI_MSB_FIRSTE"></a> <a id="_CPPv2N16qspi_bit_order_e14QSPI_MSB_FIRSTE"></a> <a id="drv__qspi_8h_1a64a853180dd8d518d2e3fdb035c615f4a6c9a263c72f6934e9d48e99fbe93e587"></a> enumerator QSPI\_MSB\_FIRST
    :   QSPI MSB first

    <a id="_CPPv4N16qspi_bit_order_e14QSPI_LSB_FIRSTE"></a>

    <a id="_CPPv3N16qspi_bit_order_e14QSPI_LSB_FIRSTE"></a> <a id="_CPPv2N16qspi_bit_order_e14QSPI_LSB_FIRSTE"></a> <a id="drv__qspi_8h_1a64a853180dd8d518d2e3fdb035c615f4a289b53ead1f2ee8b1d41176f5b5ee5a2"></a> enumerator QSPI\_LSB\_FIRST
    :   QSPI LSB first

<a id="_CPPv416qspi_line_mode_e"></a>

<a id="_CPPv316qspi_line_mode_e"></a> <a id="_CPPv216qspi_line_mode_e"></a> <a id="drv__qspi_8h_1aaf005c8428ea0f518aa2f82d4a2ce69e"></a> enum qspi\_line\_mode\_e
:   *Values:*

    <a id="_CPPv4N16qspi_line_mode_e10QSPI_1WIREE"></a>

    <a id="_CPPv3N16qspi_line_mode_e10QSPI_1WIREE"></a> <a id="_CPPv2N16qspi_line_mode_e10QSPI_1WIREE"></a> <a id="drv__qspi_8h_1aaf005c8428ea0f518aa2f82d4a2ce69eaf10bed27cc009230c45ab5959193c91b"></a> enumerator QSPI\_1WIRE
    :   QSPI 1\_wire mode

    <a id="_CPPv4N16qspi_line_mode_e10QSPI_2WIREE"></a>

    <a id="_CPPv3N16qspi_line_mode_e10QSPI_2WIREE"></a> <a id="_CPPv2N16qspi_line_mode_e10QSPI_2WIREE"></a> <a id="drv__qspi_8h_1aaf005c8428ea0f518aa2f82d4a2ce69ea0b75fa2c084a4ed288a318e865aa1434"></a> enumerator QSPI\_2WIRE
    :   QSPI 2\_wire mode

    <a id="_CPPv4N16qspi_line_mode_e10QSPI_4WIREE"></a>

    <a id="_CPPv3N16qspi_line_mode_e10QSPI_4WIREE"></a> <a id="_CPPv2N16qspi_line_mode_e10QSPI_4WIREE"></a> <a id="drv__qspi_8h_1aaf005c8428ea0f518aa2f82d4a2ce69eab3c2b5a4d440864365e75108d7903472"></a> enumerator QSPI\_4WIRE
    :   QSPI 4\_wire mode

<a id="_CPPv416qspi_data_mode_e"></a>

<a id="_CPPv316qspi_data_mode_e"></a> <a id="_CPPv216qspi_data_mode_e"></a> <a id="drv__qspi_8h_1aee43ca0fe156a9eec7dfd97c577d9267"></a> enum qspi\_data\_mode\_e
:   *Values:*

    <a id="_CPPv4N16qspi_data_mode_e10DATA_PIXELE"></a>

    <a id="_CPPv3N16qspi_data_mode_e10DATA_PIXELE"></a> <a id="_CPPv2N16qspi_data_mode_e10DATA_PIXELE"></a> <a id="drv__qspi_8h_1aee43ca0fe156a9eec7dfd97c577d9267ac26ca0502cd77ea81ae0bb9df0f6ae1a"></a> enumerator DATA\_PIXEL

    <a id="_CPPv4N16qspi_data_mode_e10DATA_FRAMEE"></a>

    <a id="_CPPv3N16qspi_data_mode_e10DATA_FRAMEE"></a> <a id="_CPPv2N16qspi_data_mode_e10DATA_FRAMEE"></a> <a id="drv__qspi_8h_1aee43ca0fe156a9eec7dfd97c577d9267a4e9747725fb8de6f722482aeedfb8cbb"></a> enumerator DATA\_FRAME

<a id="_CPPv421qspi_dest_addr_type_e"></a>

<a id="_CPPv321qspi_dest_addr_type_e"></a> <a id="_CPPv221qspi_dest_addr_type_e"></a> <a id="drv__qspi_8h_1a7980c53ce5169fa67ac00b30ee7fef0e"></a> enum qspi\_dest\_addr\_type\_e
:   *Values:*

    <a id="_CPPv4N21qspi_dest_addr_type_e18QSPI_DEST_NO_CACHEE"></a>

    <a id="_CPPv3N21qspi_dest_addr_type_e18QSPI_DEST_NO_CACHEE"></a> <a id="_CPPv2N21qspi_dest_addr_type_e18QSPI_DEST_NO_CACHEE"></a> <a id="drv__qspi_8h_1a7980c53ce5169fa67ac00b30ee7fef0eae276ad63ae1e03f795ef119ae24aa438"></a> enumerator QSPI\_DEST\_NO\_CACHE

    <a id="_CPPv4N21qspi_dest_addr_type_e15QSPI_DEST_NACHEE"></a>

    <a id="_CPPv3N21qspi_dest_addr_type_e15QSPI_DEST_NACHEE"></a> <a id="_CPPv2N21qspi_dest_addr_type_e15QSPI_DEST_NACHEE"></a> <a id="drv__qspi_8h_1a7980c53ce5169fa67ac00b30ee7fef0eafba5c40f4c8e57faf9bef3f37876b388"></a> enumerator QSPI\_DEST\_NACHE

<a id="_CPPv416qspi_work_mode_e"></a>

<a id="_CPPv316qspi_work_mode_e"></a> <a id="_CPPv216qspi_work_mode_e"></a> <a id="drv__qspi_8h_1a627bf4cbb03d55ba101b785e5ece2596"></a> enum qspi\_work\_mode\_e
:   *Values:*

    <a id="_CPPv4N16qspi_work_mode_e13INDIRECT_MODEE"></a>

    <a id="_CPPv3N16qspi_work_mode_e13INDIRECT_MODEE"></a> <a id="_CPPv2N16qspi_work_mode_e13INDIRECT_MODEE"></a> <a id="drv__qspi_8h_1a627bf4cbb03d55ba101b785e5ece2596a28fc42c46d45b9ccc3545dc27b443a71"></a> enumerator INDIRECT\_MODE

    <a id="_CPPv4N16qspi_work_mode_e18MEMORY_MAPPED_MODEE"></a>

    <a id="_CPPv3N16qspi_work_mode_e18MEMORY_MAPPED_MODEE"></a> <a id="_CPPv2N16qspi_work_mode_e18MEMORY_MAPPED_MODEE"></a> <a id="drv__qspi_8h_1a627bf4cbb03d55ba101b785e5ece2596a1fe6aec6e7850cf0c4a3ef3dd638bd25"></a> enumerator MEMORY\_MAPPED\_MODE
