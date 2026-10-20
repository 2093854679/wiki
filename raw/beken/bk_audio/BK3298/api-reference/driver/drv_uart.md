---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_uart.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-uart"></a>

# DRV\_UART

<a id="drv-uart-api-status"></a>

## DRV\_UART API Status

| API |
| --- |
| [`drv_uart_init()`](#_CPPv413drv_uart_init8uint32_t "drv_uart_init") |
| [`drv_uart_deinit()`](#_CPPv415drv_uart_deinit8uint32_t "drv_uart_deinit") |
| [`drv_uart_cfg_param()`](#_CPPv418drv_uart_cfg_param8uint32_t11uart_bits_e8uint32_t13uart_parity_e8uint32_t "drv_uart_cfg_param") |
| [`drv_uart_cfg_flow_ctrl()`](#_CPPv422drv_uart_cfg_flow_ctrl8uint32_t15uart_polarity_e15uart_polarity_e "drv_uart_cfg_flow_ctrl") |
| [`drv_uart_enable_tx()`](#_CPPv418drv_uart_enable_tx8uint32_tb "drv_uart_enable_tx") |
| [`drv_uart_enable_rx()`](#_CPPv418drv_uart_enable_rx8uint32_tb "drv_uart_enable_rx") |
| [`drv_uart_tx()`](#_CPPv411drv_uart_tx8uint32_tP7uint8_t8uint32_t "drv_uart_tx") |
| [`drv_uart_get_tx_fifo_addr()`](#_CPPv425drv_uart_get_tx_fifo_addr8uint32_t "drv_uart_get_tx_fifo_addr") |
| [`drv_uart_rx()`](#_CPPv411drv_uart_rx8uint32_tP7uint8_t8uint32_t "drv_uart_rx") |
| [`drv_uart_get_rx_fifo_addr()`](#_CPPv425drv_uart_get_rx_fifo_addr8uint32_t "drv_uart_get_rx_fifo_addr") |
| [`drv_uart_rx_async()`](#_CPPv417drv_uart_rx_async8uint32_tP7uint8_t8uint32_t15pfunc_uart_cb_t "drv_uart_rx_async") |
| [`drv_uart_cfg_rxtimeout_callback()`](#_CPPv431drv_uart_cfg_rxtimeout_callback8uint32_t22pfunc_uart_rxtimeout_tPv "drv_uart_cfg_rxtimeout_callback") |
| [`uart_aec_data_dump()`](#_CPPv418uart_aec_data_dumpP7uint8_tP7uint8_tP7uint8_t8uint32_t8uint32_t "uart_aec_data_dump") |

<a id="drv-uart-unit-number"></a>

## DRV\_UART UNIT Number

| Capability | Number |
| --- | --- |
| UNIT Number | 2 |

<a id="drv-uart-pin-and-gpio-map"></a>

## DRV\_UART Pin and GPIO Map

| uart Pin | Number |
| --- | --- |
| uart0\_tx | 0 |
| uart0\_rx | 1 |
| uart1\_tx | 7 |
| uart1\_rx | 8 |

<a id="drv-uart-api-reference"></a>

## DRV\_UART API Reference

<a id="header-file"></a>

### Header File

- [driver/uart/drv\_uart.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/uart/drv_uart.h)

<a id="functions"></a>

### Functions

<a id="_CPPv413drv_uart_init8uint32_t"></a>

<a id="_CPPv313drv_uart_init8uint32_t"></a> <a id="_CPPv213drv_uart_init8uint32_t"></a> <a id="drv_uart_init__uint32_t"></a> <a id="drv__uart_8h_1af08be065cc73388b304af15bfa36dc72"></a> uint32\_t drv\_uart\_init(uint32\_t dev\_index)
:   init a uart device.

    初始化uart设备，在使用uart功能前需要调用它获取device instance

    参数:
    :   **dev\_index** – **\[in\]** device index, from 0(the first device)

    返回值:
    :   - **0** – fail
        - **other** – success

    返回:
    :   device instance

<a id="_CPPv415drv_uart_deinit8uint32_t"></a>

<a id="_CPPv315drv_uart_deinit8uint32_t"></a> <a id="_CPPv215drv_uart_deinit8uint32_t"></a> <a id="drv_uart_deinit__uint32_t"></a> <a id="drv__uart_8h_1aec0fb2b22bf2d7de09ed44884ff831e3"></a> int32\_t drv\_uart\_deinit(uint32\_t dev\_instance)
:   deinit a uart device.

    反初始化uart设备，对drv\_uart\_device\_init()进行反向操作

    参数:
    :   **dev\_instance** – **\[in\]** return value of drv\_uart\_device\_init()

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv418drv_uart_cfg_param8uint32_t11uart_bits_e8uint32_t13uart_parity_e8uint32_t"></a>

<a id="_CPPv318drv_uart_cfg_param8uint32_t11uart_bits_e8uint32_t13uart_parity_e8uint32_t"></a> <a id="_CPPv218drv_uart_cfg_param8uint32_t11uart_bits_e8uint32_t13uart_parity_e8uint32_t"></a> <a id="drv_uart_cfg_param__uint32_t.uart_bits_e.uint32_t.uart_parity_e.uint32_t"></a> <a id="drv__uart_8h_1a7d1d9f7cb53d3398d2bf0c4fee1b5ff4"></a> int32\_t drv\_uart\_cfg\_param(uint32\_t dev\_instance, [uart\_bits\_e](#_CPPv411uart_bits_e "uart_bits_e") e\_data\_bits, uint32\_t stop\_bits, [uart\_parity\_e](#_CPPv413uart_parity_e "uart_parity_e") e\_parity, uint32\_t baudrate)
:   config uart parameter.

    配置uart的常规参数

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_uart\_device\_init()
        - **e\_data\_bits** – **\[in\]** see uart\_bits\_e
        - **stop\_bits** – **\[in\]** valid value: 1 and 2
        - **e\_parity** – **\[in\]** see uart\_parity\_e
        - **baudrate** – **\[in\]** 波特率设置

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422drv_uart_cfg_flow_ctrl8uint32_t15uart_polarity_e15uart_polarity_e"></a>

<a id="_CPPv322drv_uart_cfg_flow_ctrl8uint32_t15uart_polarity_e15uart_polarity_e"></a> <a id="_CPPv222drv_uart_cfg_flow_ctrl8uint32_t15uart_polarity_e15uart_polarity_e"></a> <a id="drv_uart_cfg_flow_ctrl__uint32_t.uart_polarity_e.uart_polarity_e"></a> <a id="drv__uart_8h_1a52ced5382750b92294d463fc0f4e282a"></a> int32\_t drv\_uart\_cfg\_flow\_ctrl(uint32\_t dev\_instance, [uart\_polarity\_e](#_CPPv415uart_polarity_e "uart_polarity_e") rts\_pol, [uart\_polarity\_e](#_CPPv415uart_polarity_e "uart_polarity_e") cts\_pol)
:   config uart polarity.

    流控的CTS、RTS选择

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_uart\_device\_init()
        - **rts\_pol** – **\[in\]** RTS polarity, see uart\_polarity\_e
        - **cts\_pol** – **\[in\]** CTS polarity, see uart\_polarity\_e

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv418drv_uart_enable_tx8uint32_tb"></a>

<a id="_CPPv318drv_uart_enable_tx8uint32_tb"></a> <a id="_CPPv218drv_uart_enable_tx8uint32_tb"></a> <a id="drv_uart_enable_tx__uint32_t.b"></a> <a id="drv__uart_8h_1a0bbb5924834fcdc0752d9183f5af2477"></a> int32\_t drv\_uart\_enable\_tx(uint32\_t dev\_instance, bool enable)
:   uart tx enable or not.

    打开或关闭uart的tx功能

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_uart\_device\_init()
        - **enable** – **\[in\]** true: enable false: disable

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv418drv_uart_enable_rx8uint32_tb"></a>

<a id="_CPPv318drv_uart_enable_rx8uint32_tb"></a> <a id="_CPPv218drv_uart_enable_rx8uint32_tb"></a> <a id="drv_uart_enable_rx__uint32_t.b"></a> <a id="drv__uart_8h_1a23ca11c3f28c93f680a82d2f7a5daca2"></a> int32\_t drv\_uart\_enable\_rx(uint32\_t dev\_instance, bool enable)
:   uart rx enable or not.

    打开或关闭uart的rx功能

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_uart\_device\_init()
        - **enable** – **\[in\]** true: enable false: disable

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv411drv_uart_tx8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv311drv_uart_tx8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv211drv_uart_tx8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_uart_tx__uint32_t.uint8_tP.uint32_t"></a> <a id="drv__uart_8h_1a14dd5a63e1f0a694ba47b48e89ee5032"></a> int32\_t drv\_uart\_tx(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size)
:   uart send.

    uart 同步发送，直接写TX FIFO，全部数据写完后该函数才返回

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_uart\_device\_init()
        - **pu1\_buf** – **\[in\]** pointer to the send buffer
        - **size** – **\[in\]** send buffer size

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425drv_uart_get_tx_fifo_addr8uint32_t"></a>

<a id="_CPPv325drv_uart_get_tx_fifo_addr8uint32_t"></a> <a id="_CPPv225drv_uart_get_tx_fifo_addr8uint32_t"></a> <a id="drv_uart_get_tx_fifo_addr__uint32_t"></a> <a id="drv__uart_8h_1adc77f0627de00f0fa1d4ae103d5a4990"></a> uint32\_t drv\_uart\_get\_tx\_fifo\_addr(uint32\_t dev\_instance)
:   get uart tx fifo address.

    获取TX FIFO的地址，通常用来给上层套DMA使用时需要

    参数:
    :   **dev\_instance** – **\[in\]** 参数说明部分

    返回:
    :   tx fifo address

<a id="_CPPv411drv_uart_rx8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv311drv_uart_rx8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv211drv_uart_rx8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_uart_rx__uint32_t.uint8_tP.uint32_t"></a> <a id="drv__uart_8h_1a155c5783f68310a60ef3c192c767e2ab"></a> int32\_t drv\_uart\_rx(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size)
:   uart receive.

    uart 同步接收，直接读RX FIFO，读够期望的长度该函数才会返回

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_uart\_device\_init()
        - **pu1\_buf** – **\[in\]** pointer to the send receive
        - **size** – **\[in\]** request rx size

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425drv_uart_get_rx_fifo_addr8uint32_t"></a>

<a id="_CPPv325drv_uart_get_rx_fifo_addr8uint32_t"></a> <a id="_CPPv225drv_uart_get_rx_fifo_addr8uint32_t"></a> <a id="drv_uart_get_rx_fifo_addr__uint32_t"></a> <a id="drv__uart_8h_1a111c910ae4b99ff099472af4739c1d3a"></a> uint32\_t drv\_uart\_get\_rx\_fifo\_addr(uint32\_t dev\_instance)
:   get uart rx fifo address.

    获取RX FIFO的地址，通常用来给上层套DMA使用时需要

    参数:
    :   **dev\_instance** – **\[in\]** 参数说明部分

    返回:
    :   rx fifo address

<a id="_CPPv417drv_uart_rx_async8uint32_tP7uint8_t8uint32_t15pfunc_uart_cb_t"></a>

<a id="_CPPv317drv_uart_rx_async8uint32_tP7uint8_t8uint32_t15pfunc_uart_cb_t"></a> <a id="_CPPv217drv_uart_rx_async8uint32_tP7uint8_t8uint32_t15pfunc_uart_cb_t"></a> <a id="drv_uart_rx_async__uint32_t.uint8_tP.uint32_t.pfunc_uart_cb_t"></a> <a id="drv__uart_8h_1a2cac8e35d953f12ef95b67c0c9199e3c"></a> int32\_t drv\_uart\_rx\_async(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size, [pfunc\_uart\_cb\_t](#_CPPv415pfunc_uart_cb_t "pfunc_uart_cb_t") pfn\_cb)
:   uart receive asynchronously.

    uart 异步接收，该函数立即，收够期望的长度后再调用 pfn\_cb 通知用户 如果对方一直发送数据，我们这里响应太慢，rx FIFO存在full的可能 需要和对方协商好一次发的数据不要超过FIFO深度。推荐使用dma的方式来接收

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_uart\_device\_init()
        - **pu1\_buf** – **\[in\]** pointer to the send receive
        - **size** – **\[in\]** request rx size
        - **pfn\_cb** – **\[in\]** callback when rx finish

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv431drv_uart_cfg_rxtimeout_callback8uint32_t22pfunc_uart_rxtimeout_tPv"></a>

<a id="_CPPv331drv_uart_cfg_rxtimeout_callback8uint32_t22pfunc_uart_rxtimeout_tPv"></a> <a id="_CPPv231drv_uart_cfg_rxtimeout_callback8uint32_t22pfunc_uart_rxtimeout_tPv"></a> <a id="drv_uart_cfg_rxtimeout_callback__uint32_t.pfunc_uart_rxtimeout_t.voidP"></a> <a id="drv__uart_8h_1acfc6c33951e5d8f3aeabf192803cc878"></a> int32\_t drv\_uart\_cfg\_rxtimeout\_callback(uint32\_t dev\_instance, [pfunc\_uart\_rxtimeout\_t](#_CPPv422pfunc_uart_rxtimeout_t "pfunc_uart_rxtimeout_t") pfn\_cb, void \*pv\_arg)
:   config uart rx timeout callback.

    通常是在uart套DMA使用的时候需要. [drv\_uart\_rx()](#drv__uart_8h_1a155c5783f68310a60ef3c192c767e2ab)/drv\_uart\_rx\_async() 这2种收数据的方式不需要配置该回调

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_uart\_device\_init()
        - **pfn\_cb** – **\[in\]** callback for rx finish
        - **pv\_arg** – **\[in\]** callback parameter

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv418uart_aec_data_dumpP7uint8_tP7uint8_tP7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv318uart_aec_data_dumpP7uint8_tP7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv218uart_aec_data_dumpP7uint8_tP7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="uart_aec_data_dump__uint8_tP.uint8_tP.uint8_tP.uint32_t.uint32_t"></a> <a id="drv__uart_8h_1ae517e8ba23e76b4943e5fd9116c9e413"></a> void uart\_aec\_data\_dump(uint8\_t \*mic, uint8\_t \*ref, uint8\_t \*out, uint32\_t len, uint32\_t adc\_ch)

<a id="macros"></a>

### Macros

<a id="c.UART_DEVICE_NUM"></a>

<a id="drv__uart_8h_1a456c557baeacbb5b8d5ca0d588aa4e7b"></a> UART\_DEVICE\_NUM

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv411uart_bits_e"></a>

<a id="_CPPv311uart_bits_e"></a> <a id="_CPPv211uart_bits_e"></a> <a id="uart_bits_e"></a> <a id="drv__uart_8h_1a3df9db813835c7a51f1774c8be060608"></a> typedef enum [\_uart\_bits\_e](#_CPPv412_uart_bits_e "_uart_bits_e") uart\_bits\_e

<a id="_CPPv413uart_parity_e"></a>

<a id="_CPPv313uart_parity_e"></a> <a id="_CPPv213uart_parity_e"></a> <a id="uart_parity_e"></a> <a id="drv__uart_8h_1acae27585c636ecda09b5afdca09cfcf9"></a> typedef enum [\_uart\_parity\_e](#_CPPv414_uart_parity_e "_uart_parity_e") uart\_parity\_e

<a id="_CPPv415uart_polarity_e"></a>

<a id="_CPPv315uart_polarity_e"></a> <a id="_CPPv215uart_polarity_e"></a> <a id="uart_polarity_e"></a> <a id="drv__uart_8h_1a6e4acb81c550bf7eca06a370147308f0"></a> typedef enum [\_uart\_polarity\_e](#_CPPv416_uart_polarity_e "_uart_polarity_e") uart\_polarity\_e

<a id="_CPPv415pfunc_uart_cb_t"></a>

<a id="_CPPv315pfunc_uart_cb_t"></a> <a id="_CPPv215pfunc_uart_cb_t"></a> <a id="pfunc_uart_cb_t"></a> <a id="drv__uart_8h_1a81efcd5273e3ced8a5ac17d510b04a8a"></a> typedef void (\*pfunc\_uart\_cb\_t)(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size)

<a id="_CPPv422pfunc_uart_rxtimeout_t"></a>

<a id="_CPPv322pfunc_uart_rxtimeout_t"></a> <a id="_CPPv222pfunc_uart_rxtimeout_t"></a> <a id="pfunc_uart_rxtimeout_t"></a> <a id="drv__uart_8h_1a404160344f3bae2ed6b92508f8dfa754"></a> typedef void (\*pfunc\_uart\_rxtimeout\_t)(uint32\_t dev\_instance, void \*pv\_arg)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv412_uart_bits_e"></a>

<a id="_CPPv312_uart_bits_e"></a> <a id="_CPPv212_uart_bits_e"></a> <a id="drv__uart_8h_1a4ff2fa67cca59b8650496bde8ecd8d78"></a> enum \_uart\_bits\_e
:   *Values:*

    <a id="_CPPv4N12_uart_bits_e14DRV_UART_5BITSE"></a>

    <a id="_CPPv3N12_uart_bits_e14DRV_UART_5BITSE"></a> <a id="_CPPv2N12_uart_bits_e14DRV_UART_5BITSE"></a> <a id="drv__uart_8h_1a4ff2fa67cca59b8650496bde8ecd8d78aac783ee1dfb27db7d085fdb503532405"></a> enumerator DRV\_UART\_5BITS

    <a id="_CPPv4N12_uart_bits_e14DRV_UART_6BITSE"></a>

    <a id="_CPPv3N12_uart_bits_e14DRV_UART_6BITSE"></a> <a id="_CPPv2N12_uart_bits_e14DRV_UART_6BITSE"></a> <a id="drv__uart_8h_1a4ff2fa67cca59b8650496bde8ecd8d78aca2fb86d4fd1acc3c917e3efc655e868"></a> enumerator DRV\_UART\_6BITS
    :   data length: 5bit

    <a id="_CPPv4N12_uart_bits_e14DRV_UART_7BITSE"></a>

    <a id="_CPPv3N12_uart_bits_e14DRV_UART_7BITSE"></a> <a id="_CPPv2N12_uart_bits_e14DRV_UART_7BITSE"></a> <a id="drv__uart_8h_1a4ff2fa67cca59b8650496bde8ecd8d78a1ce633cf68db77f50fc44dff3b5f34c8"></a> enumerator DRV\_UART\_7BITS
    :   data length: 6bit

    <a id="_CPPv4N12_uart_bits_e14DRV_UART_8BITSE"></a>

    <a id="_CPPv3N12_uart_bits_e14DRV_UART_8BITSE"></a> <a id="_CPPv2N12_uart_bits_e14DRV_UART_8BITSE"></a> <a id="drv__uart_8h_1a4ff2fa67cca59b8650496bde8ecd8d78aae737df1e48273f79a95524b1d88a203"></a> enumerator DRV\_UART\_8BITS
    :   data length: 7bit

<a id="_CPPv414_uart_parity_e"></a>

<a id="_CPPv314_uart_parity_e"></a> <a id="_CPPv214_uart_parity_e"></a> <a id="drv__uart_8h_1a5babba3cc08ac86031aa45dc364554bb"></a> enum \_uart\_parity\_e
:   *Values:*

    <a id="_CPPv4N14_uart_parity_e12DRV_UART_ODDE"></a>

    <a id="_CPPv3N14_uart_parity_e12DRV_UART_ODDE"></a> <a id="_CPPv2N14_uart_parity_e12DRV_UART_ODDE"></a> <a id="drv__uart_8h_1a5babba3cc08ac86031aa45dc364554bba8edebc0a3410aa25f07908422d382503"></a> enumerator DRV\_UART\_ODD

    <a id="_CPPv4N14_uart_parity_e13DRV_UART_EVENE"></a>

    <a id="_CPPv3N14_uart_parity_e13DRV_UART_EVENE"></a> <a id="_CPPv2N14_uart_parity_e13DRV_UART_EVENE"></a> <a id="drv__uart_8h_1a5babba3cc08ac86031aa45dc364554bba3b084b0fe9a950da91c4e3109ea8fff1"></a> enumerator DRV\_UART\_EVEN
    :   奇校验

    <a id="_CPPv4N14_uart_parity_e20DRV_UART_PARITY_NONEE"></a>

    <a id="_CPPv3N14_uart_parity_e20DRV_UART_PARITY_NONEE"></a> <a id="_CPPv2N14_uart_parity_e20DRV_UART_PARITY_NONEE"></a> <a id="drv__uart_8h_1a5babba3cc08ac86031aa45dc364554bba280ca18019759626e700baa40a0aef69"></a> enumerator DRV\_UART\_PARITY\_NONE
    :   偶校验

        不校验

<a id="_CPPv416_uart_polarity_e"></a>

<a id="_CPPv316_uart_polarity_e"></a> <a id="_CPPv216_uart_polarity_e"></a> <a id="drv__uart_8h_1a66e4e414b373f3dfb4aa0c4ab33e96e1"></a> enum \_uart\_polarity\_e
:   *Values:*

    <a id="_CPPv4N16_uart_polarity_e24DRV_UART_POL_HIGH_ACCEPTE"></a>

    <a id="_CPPv3N16_uart_polarity_e24DRV_UART_POL_HIGH_ACCEPTE"></a> <a id="_CPPv2N16_uart_polarity_e24DRV_UART_POL_HIGH_ACCEPTE"></a> <a id="drv__uart_8h_1a66e4e414b373f3dfb4aa0c4ab33e96e1a944f4a65251c4eb28a423156a322586b"></a> enumerator DRV\_UART\_POL\_HIGH\_ACCEPT

    <a id="_CPPv4N16_uart_polarity_e23DRV_UART_POL_LOW_ACCEPTE"></a>

    <a id="_CPPv3N16_uart_polarity_e23DRV_UART_POL_LOW_ACCEPTE"></a> <a id="_CPPv2N16_uart_polarity_e23DRV_UART_POL_LOW_ACCEPTE"></a> <a id="drv__uart_8h_1a66e4e414b373f3dfb4aa0c4ab33e96e1abea90f0ccfa4a2c13e507894257d8df3"></a> enumerator DRV\_UART\_POL\_LOW\_ACCEPT
    :   CTS/RTX极性: 高允许，低阻止

    <a id="_CPPv4N16_uart_polarity_e17DRV_UART_POL_NONEE"></a>

    <a id="_CPPv3N16_uart_polarity_e17DRV_UART_POL_NONEE"></a> <a id="_CPPv2N16_uart_polarity_e17DRV_UART_POL_NONEE"></a> <a id="drv__uart_8h_1a66e4e414b373f3dfb4aa0c4ab33e96e1a0bd3ac5636e87d7c4f7fecb802d438a6"></a> enumerator DRV\_UART\_POL\_NONE
    :   CTS/RTX极性: 低允许，高阻止

        CTS/RTX极性: 不启用 (常用，需要和对方匹配)
