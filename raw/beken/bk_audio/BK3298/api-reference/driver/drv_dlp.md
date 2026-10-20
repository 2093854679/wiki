---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_dlp.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-dlp"></a>

# DRV\_DLP

<a id="drv-dlp-api-status"></a>

## DRV\_DLP API Status

| API |
| --- |
| [`drv_dlp_init()`](#_CPPv412drv_dlp_init8uint32_t "drv_dlp_init") |
| [`drv_dlp_deinit()`](#_CPPv414drv_dlp_deinit8uint32_t "drv_dlp_deinit") |
| [`drv_dlp_cfg_param()`](#_CPPv417drv_dlp_cfg_param8uint32_t10dlp_bits_e8uint32_t12dlp_parity_e8uint32_t "drv_dlp_cfg_param") |
| [`drv_dlp_cfg_flow_ctrl()`](#_CPPv421drv_dlp_cfg_flow_ctrl8uint32_t14dlp_polarity_e14dlp_polarity_e "drv_dlp_cfg_flow_ctrl") |
| [`drv_dlp_enable_tx()`](#_CPPv417drv_dlp_enable_tx8uint32_tb "drv_dlp_enable_tx") |
| [`drv_dlp_enable_rx()`](#_CPPv417drv_dlp_enable_rx8uint32_tb "drv_dlp_enable_rx") |
| [`drv_dlp_tx()`](#_CPPv410drv_dlp_tx8uint32_tP7uint8_t8uint32_t "drv_dlp_tx") |
| [`drv_dlp_get_tx_fifo_addr()`](#_CPPv424drv_dlp_get_tx_fifo_addr8uint32_t "drv_dlp_get_tx_fifo_addr") |
| [`drv_dlp_rx()`](#_CPPv410drv_dlp_rx8uint32_tP7uint8_t8uint32_t "drv_dlp_rx") |
| [`drv_dlp_get_rx_fifo_addr()`](#_CPPv424drv_dlp_get_rx_fifo_addr8uint32_t "drv_dlp_get_rx_fifo_addr") |
| [`drv_dlp_rx_async()`](#_CPPv416drv_dlp_rx_async8uint32_tP7uint8_t8uint32_t14pfunc_dlp_cb_t "drv_dlp_rx_async") |
| [`drv_dlp_cfg_rxtimeout_callback()`](#_CPPv430drv_dlp_cfg_rxtimeout_callback8uint32_t21pfunc_dlp_rxtimeout_tPv "drv_dlp_cfg_rxtimeout_callback") |
| [`drv_dlp_input_control()`](#_CPPv421drv_dlp_input_control8uint32_t12dlp_in_ctl_e "drv_dlp_input_control") |
| [`drv_dlp_output_control()`](#_CPPv422drv_dlp_output_control8uint32_t13dlp_out_ctl_e "drv_dlp_output_control") |

<a id="drv-dlp-api-reference"></a>

## DRV\_DLP API Reference

<a id="header-file"></a>

### Header File

- [driver/dlp/drv\_dlp.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/dlp/drv_dlp.h)

<a id="functions"></a>

### Functions

<a id="_CPPv412drv_dlp_init8uint32_t"></a>

<a id="_CPPv312drv_dlp_init8uint32_t"></a> <a id="_CPPv212drv_dlp_init8uint32_t"></a> <a id="drv_dlp_init__uint32_t"></a> <a id="drv__dlp_8h_1af8bbcdf71a6530cb7d3117c50c3ade70"></a> uint32\_t drv\_dlp\_init(uint32\_t dev\_index)
:   init a dlp device.

    初始化dlp设备，在使用dlp功能前需要调用它获取device instance

    参数:
    :   **dev\_index** – **\[in\]** device index, from 0(the first device)

    返回值:
    :   - **0** – fail
        - **other** – success

    返回:
    :   device instance

<a id="_CPPv414drv_dlp_deinit8uint32_t"></a>

<a id="_CPPv314drv_dlp_deinit8uint32_t"></a> <a id="_CPPv214drv_dlp_deinit8uint32_t"></a> <a id="drv_dlp_deinit__uint32_t"></a> <a id="drv__dlp_8h_1a8fe6126a361221066e5576abd96127e0"></a> int32\_t drv\_dlp\_deinit(uint32\_t dev\_instance)
:   deinit a dlp device.

    反初始化dlp设备，对drv\_dlp\_device\_init()进行反向操作

    参数:
    :   **dev\_instance** – **\[in\]** return value of drv\_dlp\_device\_init()

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv417drv_dlp_cfg_param8uint32_t10dlp_bits_e8uint32_t12dlp_parity_e8uint32_t"></a>

<a id="_CPPv317drv_dlp_cfg_param8uint32_t10dlp_bits_e8uint32_t12dlp_parity_e8uint32_t"></a> <a id="_CPPv217drv_dlp_cfg_param8uint32_t10dlp_bits_e8uint32_t12dlp_parity_e8uint32_t"></a> <a id="drv_dlp_cfg_param__uint32_t.dlp_bits_e.uint32_t.dlp_parity_e.uint32_t"></a> <a id="drv__dlp_8h_1acedefd5dd4cb1510d6e03eb14617655f"></a> int32\_t drv\_dlp\_cfg\_param(uint32\_t dev\_instance, [dlp\_bits\_e](#_CPPv410dlp_bits_e "dlp_bits_e") e\_data\_bits, uint32\_t stop\_bits, [dlp\_parity\_e](#_CPPv412dlp_parity_e "dlp_parity_e") e\_parity, uint32\_t baudrate)
:   config dlp parameter.

    配置dlp的常规参数

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_dlp\_device\_init()
        - **e\_data\_bits** – **\[in\]** see dlp\_bits\_e
        - **stop\_bits** – **\[in\]** valid value: 1 and 2
        - **e\_parity** – **\[in\]** see dlp\_parity\_e
        - **baudrate** – **\[in\]** 波特率设置

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421drv_dlp_cfg_flow_ctrl8uint32_t14dlp_polarity_e14dlp_polarity_e"></a>

<a id="_CPPv321drv_dlp_cfg_flow_ctrl8uint32_t14dlp_polarity_e14dlp_polarity_e"></a> <a id="_CPPv221drv_dlp_cfg_flow_ctrl8uint32_t14dlp_polarity_e14dlp_polarity_e"></a> <a id="drv_dlp_cfg_flow_ctrl__uint32_t.dlp_polarity_e.dlp_polarity_e"></a> <a id="drv__dlp_8h_1a3c506f9498fdd9db7a968e89d7c5551f"></a> int32\_t drv\_dlp\_cfg\_flow\_ctrl(uint32\_t dev\_instance, [dlp\_polarity\_e](#_CPPv414dlp_polarity_e "dlp_polarity_e") rts\_pol, [dlp\_polarity\_e](#_CPPv414dlp_polarity_e "dlp_polarity_e") cts\_pol)
:   config dlp polarity.

    流控的CTS、RTS选择

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_dlp\_device\_init()
        - **rts\_pol** – **\[in\]** RTS polarity, see dlp\_polarity\_e
        - **cts\_pol** – **\[in\]** CTS polarity, see dlp\_polarity\_e

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv417drv_dlp_enable_tx8uint32_tb"></a>

<a id="_CPPv317drv_dlp_enable_tx8uint32_tb"></a> <a id="_CPPv217drv_dlp_enable_tx8uint32_tb"></a> <a id="drv_dlp_enable_tx__uint32_t.b"></a> <a id="drv__dlp_8h_1af8242233622ef95c136efc175cab168d"></a> int32\_t drv\_dlp\_enable\_tx(uint32\_t dev\_instance, bool enable)
:   dlp tx enable or not.

    打开或关闭dlp的tx功能

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_dlp\_device\_init()
        - **enable** – **\[in\]** true: enable false: disable

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv417drv_dlp_enable_rx8uint32_tb"></a>

<a id="_CPPv317drv_dlp_enable_rx8uint32_tb"></a> <a id="_CPPv217drv_dlp_enable_rx8uint32_tb"></a> <a id="drv_dlp_enable_rx__uint32_t.b"></a> <a id="drv__dlp_8h_1acae0abee75cb96e80f63c56a2e988001"></a> int32\_t drv\_dlp\_enable\_rx(uint32\_t dev\_instance, bool enable)
:   dlp rx enable or not.

    打开或关闭dlp的rx功能

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_dlp\_device\_init()
        - **enable** – **\[in\]** true: enable false: disable

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv410drv_dlp_tx8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv310drv_dlp_tx8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv210drv_dlp_tx8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_dlp_tx__uint32_t.uint8_tP.uint32_t"></a> <a id="drv__dlp_8h_1aa11792262222bc4a1796a3b27f62a551"></a> int32\_t drv\_dlp\_tx(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size)
:   dlp send.

    dlp 同步发送，直接写TX FIFO，全部数据写完后该函数才返回

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_dlp\_device\_init()
        - **pu1\_buf** – **\[in\]** pointer to the send buffer
        - **size** – **\[in\]** send buffer size

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424drv_dlp_get_tx_fifo_addr8uint32_t"></a>

<a id="_CPPv324drv_dlp_get_tx_fifo_addr8uint32_t"></a> <a id="_CPPv224drv_dlp_get_tx_fifo_addr8uint32_t"></a> <a id="drv_dlp_get_tx_fifo_addr__uint32_t"></a> <a id="drv__dlp_8h_1a1540b22e91b07c759c5e2bbc8ef5eefb"></a> uint32\_t drv\_dlp\_get\_tx\_fifo\_addr(uint32\_t dev\_instance)
:   get dlp tx fifo address.

    获取TX FIFO的地址，通常用来给上层套DMA使用时需要

    参数:
    :   **dev\_instance** – **\[in\]** 参数说明部分

    返回:
    :   tx fifo address

<a id="_CPPv410drv_dlp_rx8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv310drv_dlp_rx8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv210drv_dlp_rx8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_dlp_rx__uint32_t.uint8_tP.uint32_t"></a> <a id="drv__dlp_8h_1a51509d9072178fa0c3b8739cc54711df"></a> int32\_t drv\_dlp\_rx(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size)
:   dlp receive.

    dlp 同步接收，直接读RX FIFO，读够期望的长度该函数才会返回

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_dlp\_device\_init()
        - **pu1\_buf** – **\[in\]** pointer to the send receive
        - **size** – **\[in\]** request rx size

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424drv_dlp_get_rx_fifo_addr8uint32_t"></a>

<a id="_CPPv324drv_dlp_get_rx_fifo_addr8uint32_t"></a> <a id="_CPPv224drv_dlp_get_rx_fifo_addr8uint32_t"></a> <a id="drv_dlp_get_rx_fifo_addr__uint32_t"></a> <a id="drv__dlp_8h_1a87bd891d23155c0ef8ddfeadddc857c5"></a> uint32\_t drv\_dlp\_get\_rx\_fifo\_addr(uint32\_t dev\_instance)
:   get dlp rx fifo address.

    获取RX FIFO的地址，通常用来给上层套DMA使用时需要

    参数:
    :   **dev\_instance** – **\[in\]** 参数说明部分

    返回:
    :   rx fifo address

<a id="_CPPv416drv_dlp_rx_async8uint32_tP7uint8_t8uint32_t14pfunc_dlp_cb_t"></a>

<a id="_CPPv316drv_dlp_rx_async8uint32_tP7uint8_t8uint32_t14pfunc_dlp_cb_t"></a> <a id="_CPPv216drv_dlp_rx_async8uint32_tP7uint8_t8uint32_t14pfunc_dlp_cb_t"></a> <a id="drv_dlp_rx_async__uint32_t.uint8_tP.uint32_t.pfunc_dlp_cb_t"></a> <a id="drv__dlp_8h_1abdfe5bde7573d9d3b1719c2b901a6a7a"></a> int32\_t drv\_dlp\_rx\_async(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size, [pfunc\_dlp\_cb\_t](#_CPPv414pfunc_dlp_cb_t "pfunc_dlp_cb_t") pfn\_cb)
:   dlp receive asynchronously.

    dlp 异步接收，该函数立即，收够期望的长度后再调用 pfn\_cb 通知用户 如果对方一直发送数据，我们这里响应太慢，rx FIFO存在full的可能 需要和对方协商好一次发的数据不要超过FIFO深度。推荐使用dma的方式来接收

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_dlp\_device\_init()
        - **pu1\_buf** – **\[in\]** pointer to the send receive
        - **size** – **\[in\]** request rx size
        - **pfn\_cb** – **\[in\]** callback when rx finish

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv430drv_dlp_cfg_rxtimeout_callback8uint32_t21pfunc_dlp_rxtimeout_tPv"></a>

<a id="_CPPv330drv_dlp_cfg_rxtimeout_callback8uint32_t21pfunc_dlp_rxtimeout_tPv"></a> <a id="_CPPv230drv_dlp_cfg_rxtimeout_callback8uint32_t21pfunc_dlp_rxtimeout_tPv"></a> <a id="drv_dlp_cfg_rxtimeout_callback__uint32_t.pfunc_dlp_rxtimeout_t.voidP"></a> <a id="drv__dlp_8h_1ac7c776c43ea424ce3118fec469015bd9"></a> int32\_t drv\_dlp\_cfg\_rxtimeout\_callback(uint32\_t dev\_instance, [pfunc\_dlp\_rxtimeout\_t](#_CPPv421pfunc_dlp_rxtimeout_t "pfunc_dlp_rxtimeout_t") pfn\_cb, void \*pv\_arg)
:   config dlp rx timeout callback.

    通常是在dlp套DMA使用的时候需要. [drv\_dlp\_rx()](#drv__dlp_8h_1a51509d9072178fa0c3b8739cc54711df)/drv\_dlp\_rx\_async() 这2种收数据的方式不需要配置该回调

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_dlp\_device\_init()
        - **pfn\_cb** – **\[in\]** callback for rx finish
        - **pv\_arg** – **\[in\]** callback parameter

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421drv_dlp_input_control8uint32_t12dlp_in_ctl_e"></a>

<a id="_CPPv321drv_dlp_input_control8uint32_t12dlp_in_ctl_e"></a> <a id="_CPPv221drv_dlp_input_control8uint32_t12dlp_in_ctl_e"></a> <a id="drv_dlp_input_control__uint32_t.dlp_in_ctl_e"></a> <a id="drv__dlp_8h_1adbd01a6c92e24ae9d7e2a55971737275"></a> int32\_t drv\_dlp\_input\_control(uint32\_t dev\_instance, [dlp\_in\_ctl\_e](#_CPPv412dlp_in_ctl_e "dlp_in_ctl_e") e\_ctl\_val)
:   DLP input port control.

    输入端口的控制,当使用手动控制方式时，会禁用输出端口

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_dlp\_device\_init()
        - **e\_ctl\_val** – **\[in\]** see dlp\_in\_ctl\_e

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422drv_dlp_output_control8uint32_t13dlp_out_ctl_e"></a>

<a id="_CPPv322drv_dlp_output_control8uint32_t13dlp_out_ctl_e"></a> <a id="_CPPv222drv_dlp_output_control8uint32_t13dlp_out_ctl_e"></a> <a id="drv_dlp_output_control__uint32_t.dlp_out_ctl_e"></a> <a id="drv__dlp_8h_1a3945ad642eff6d373335527c1c84b441"></a> int32\_t drv\_dlp\_output\_control(uint32\_t dev\_instance, [dlp\_out\_ctl\_e](#_CPPv413dlp_out_ctl_e "dlp_out_ctl_e") e\_ctl\_val)
:   DLP output port control.

    输出端口的控制,当使用手动控制方式时，会禁用输入端口

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_dlp\_device\_init()
        - **e\_ctl\_val** – **\[in\]** see dlp\_out\_ctl\_e

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416drv_dlp_get_byte8uint32_t"></a>

<a id="_CPPv316drv_dlp_get_byte8uint32_t"></a> <a id="_CPPv216drv_dlp_get_byte8uint32_t"></a> <a id="drv_dlp_get_byte__uint32_t"></a> <a id="drv__dlp_8h_1a0b1f5dce4ddeb417b788ddf2cfe08e8e"></a> int32\_t drv\_dlp\_get\_byte(uint32\_t dev\_instance)
:   get rx byte from hw fifo.

    参数:
    :   **dev\_instance** – **\[in\]** return value of drv\_dlp\_device\_init()

    返回值:
    :   - **\>\=0** – success
        - **\<0** – fail

    返回:
    :   result

<a id="_CPPv427drv_dlp_rx_fifo_read_enable8uint32_t8uint32_t"></a>

<a id="_CPPv327drv_dlp_rx_fifo_read_enable8uint32_t8uint32_t"></a> <a id="_CPPv227drv_dlp_rx_fifo_read_enable8uint32_t8uint32_t"></a> <a id="drv_dlp_rx_fifo_read_enable__uint32_t.uint32_t"></a> <a id="drv__dlp_8h_1acb5a0e182f23cf625b6435e49d265055"></a> int32\_t drv\_dlp\_rx\_fifo\_read\_enable(uint32\_t dev\_instance, uint32\_t intr\_level)
:   config rx fifo interrupt.

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_dlp\_device\_init()
        - **intr\_level** – **\[in\]** generate interrupt when rx byte \>\= intr\_level

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="macros"></a>

### Macros

<a id="c.DLP_DEVICE_NUM"></a>

<a id="drv__dlp_8h_1a06ca4fc8d944792a25da09947f1b69fc"></a> DLP\_DEVICE\_NUM

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv410dlp_bits_e"></a>

<a id="_CPPv310dlp_bits_e"></a> <a id="_CPPv210dlp_bits_e"></a> <a id="dlp_bits_e"></a> <a id="drv__dlp_8h_1afc0e8c92f0a81a8f6f75f335e5b91f40"></a> typedef enum [\_dlp\_bits\_e](#_CPPv411_dlp_bits_e "_dlp_bits_e") dlp\_bits\_e

<a id="_CPPv412dlp_parity_e"></a>

<a id="_CPPv312dlp_parity_e"></a> <a id="_CPPv212dlp_parity_e"></a> <a id="dlp_parity_e"></a> <a id="drv__dlp_8h_1a49432ef20e098585fa6eebfbd3b54729"></a> typedef enum [\_dlp\_parity\_e](#_CPPv413_dlp_parity_e "_dlp_parity_e") dlp\_parity\_e

<a id="_CPPv414dlp_polarity_e"></a>

<a id="_CPPv314dlp_polarity_e"></a> <a id="_CPPv214dlp_polarity_e"></a> <a id="dlp_polarity_e"></a> <a id="drv__dlp_8h_1a246078f8349dbdd24194f7f51f85addf"></a> typedef enum [\_dlp\_polarity\_e](#_CPPv415_dlp_polarity_e "_dlp_polarity_e") dlp\_polarity\_e

<a id="_CPPv412dlp_in_ctl_e"></a>

<a id="_CPPv312dlp_in_ctl_e"></a> <a id="_CPPv212dlp_in_ctl_e"></a> <a id="dlp_in_ctl_e"></a> <a id="drv__dlp_8h_1a5ea395695a750dac2d51c8529dca984c"></a> typedef enum [\_dlp\_in\_ctl\_e](#_CPPv413_dlp_in_ctl_e "_dlp_in_ctl_e") dlp\_in\_ctl\_e

<a id="_CPPv413dlp_out_ctl_e"></a>

<a id="_CPPv313dlp_out_ctl_e"></a> <a id="_CPPv213dlp_out_ctl_e"></a> <a id="dlp_out_ctl_e"></a> <a id="drv__dlp_8h_1a90ce8ba600d9a99acafd809c1aa7d7f8"></a> typedef enum [\_dlp\_out\_ctl\_e](#_CPPv414_dlp_out_ctl_e "_dlp_out_ctl_e") dlp\_out\_ctl\_e

<a id="_CPPv414pfunc_dlp_cb_t"></a>

<a id="_CPPv314pfunc_dlp_cb_t"></a> <a id="_CPPv214pfunc_dlp_cb_t"></a> <a id="pfunc_dlp_cb_t"></a> <a id="drv__dlp_8h_1a91f8231eaab3e144968459ad54da2efc"></a> typedef void (\*pfunc\_dlp\_cb\_t)(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint32\_t size)

<a id="_CPPv421pfunc_dlp_rxtimeout_t"></a>

<a id="_CPPv321pfunc_dlp_rxtimeout_t"></a> <a id="_CPPv221pfunc_dlp_rxtimeout_t"></a> <a id="pfunc_dlp_rxtimeout_t"></a> <a id="drv__dlp_8h_1ae242e9d380792761015467872b6681a2"></a> typedef void (\*pfunc\_dlp\_rxtimeout\_t)(uint32\_t dev\_instance, void \*pv\_arg)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv411_dlp_bits_e"></a>

<a id="_CPPv311_dlp_bits_e"></a> <a id="_CPPv211_dlp_bits_e"></a> <a id="drv__dlp_8h_1aaafb1dc064cb449bdc4d122247bf0dce"></a> enum \_dlp\_bits\_e
:   *Values:*

    <a id="_CPPv4N11_dlp_bits_e13DRV_DLP_5BITSE"></a>

    <a id="_CPPv3N11_dlp_bits_e13DRV_DLP_5BITSE"></a> <a id="_CPPv2N11_dlp_bits_e13DRV_DLP_5BITSE"></a> <a id="drv__dlp_8h_1aaafb1dc064cb449bdc4d122247bf0dcea32b78d8086f755e6b7c35829f39dfa3c"></a> enumerator DRV\_DLP\_5BITS

    <a id="_CPPv4N11_dlp_bits_e13DRV_DLP_6BITSE"></a>

    <a id="_CPPv3N11_dlp_bits_e13DRV_DLP_6BITSE"></a> <a id="_CPPv2N11_dlp_bits_e13DRV_DLP_6BITSE"></a> <a id="drv__dlp_8h_1aaafb1dc064cb449bdc4d122247bf0dcea27f7b7d679a4fc2195a7cad8e61febfe"></a> enumerator DRV\_DLP\_6BITS
    :   data length: 5bit

    <a id="_CPPv4N11_dlp_bits_e13DRV_DLP_7BITSE"></a>

    <a id="_CPPv3N11_dlp_bits_e13DRV_DLP_7BITSE"></a> <a id="_CPPv2N11_dlp_bits_e13DRV_DLP_7BITSE"></a> <a id="drv__dlp_8h_1aaafb1dc064cb449bdc4d122247bf0dcea7019e96f9d2d6a0408d52edca33b65ea"></a> enumerator DRV\_DLP\_7BITS
    :   data length: 6bit

    <a id="_CPPv4N11_dlp_bits_e13DRV_DLP_8BITSE"></a>

    <a id="_CPPv3N11_dlp_bits_e13DRV_DLP_8BITSE"></a> <a id="_CPPv2N11_dlp_bits_e13DRV_DLP_8BITSE"></a> <a id="drv__dlp_8h_1aaafb1dc064cb449bdc4d122247bf0dceaf377d159c718f905dc41adbae1b8a355"></a> enumerator DRV\_DLP\_8BITS
    :   data length: 7bit

<a id="_CPPv413_dlp_parity_e"></a>

<a id="_CPPv313_dlp_parity_e"></a> <a id="_CPPv213_dlp_parity_e"></a> <a id="drv__dlp_8h_1ad440064b3b4956702305ceffec336c69"></a> enum \_dlp\_parity\_e
:   *Values:*

    <a id="_CPPv4N13_dlp_parity_e11DRV_DLP_ODDE"></a>

    <a id="_CPPv3N13_dlp_parity_e11DRV_DLP_ODDE"></a> <a id="_CPPv2N13_dlp_parity_e11DRV_DLP_ODDE"></a> <a id="drv__dlp_8h_1ad440064b3b4956702305ceffec336c69afc467e745e9147458a1f5c17518ebfb7"></a> enumerator DRV\_DLP\_ODD

    <a id="_CPPv4N13_dlp_parity_e12DRV_DLP_EVENE"></a>

    <a id="_CPPv3N13_dlp_parity_e12DRV_DLP_EVENE"></a> <a id="_CPPv2N13_dlp_parity_e12DRV_DLP_EVENE"></a> <a id="drv__dlp_8h_1ad440064b3b4956702305ceffec336c69ace92a203cba41d5af3ca92cda05c79f7"></a> enumerator DRV\_DLP\_EVEN
    :   奇校验

    <a id="_CPPv4N13_dlp_parity_e19DRV_DLP_PARITY_NONEE"></a>

    <a id="_CPPv3N13_dlp_parity_e19DRV_DLP_PARITY_NONEE"></a> <a id="_CPPv2N13_dlp_parity_e19DRV_DLP_PARITY_NONEE"></a> <a id="drv__dlp_8h_1ad440064b3b4956702305ceffec336c69a067ce5c3e482f6c6270db82e56c0d7eb"></a> enumerator DRV\_DLP\_PARITY\_NONE
    :   偶校验

        不校验

<a id="_CPPv415_dlp_polarity_e"></a>

<a id="_CPPv315_dlp_polarity_e"></a> <a id="_CPPv215_dlp_polarity_e"></a> <a id="drv__dlp_8h_1a1791fa28882961c1928d527603788dc3"></a> enum \_dlp\_polarity\_e
:   *Values:*

    <a id="_CPPv4N15_dlp_polarity_e23DRV_DLP_POL_HIGH_ACCEPTE"></a>

    <a id="_CPPv3N15_dlp_polarity_e23DRV_DLP_POL_HIGH_ACCEPTE"></a> <a id="_CPPv2N15_dlp_polarity_e23DRV_DLP_POL_HIGH_ACCEPTE"></a> <a id="drv__dlp_8h_1a1791fa28882961c1928d527603788dc3a43cb66137fdc9756407af5871fe16e57"></a> enumerator DRV\_DLP\_POL\_HIGH\_ACCEPT

    <a id="_CPPv4N15_dlp_polarity_e22DRV_DLP_POL_LOW_ACCEPTE"></a>

    <a id="_CPPv3N15_dlp_polarity_e22DRV_DLP_POL_LOW_ACCEPTE"></a> <a id="_CPPv2N15_dlp_polarity_e22DRV_DLP_POL_LOW_ACCEPTE"></a> <a id="drv__dlp_8h_1a1791fa28882961c1928d527603788dc3af4e1a82e2a5fdb97e070bf1d2094ac67"></a> enumerator DRV\_DLP\_POL\_LOW\_ACCEPT
    :   CTS/RTX极性: 高允许，低阻止

    <a id="_CPPv4N15_dlp_polarity_e16DRV_DLP_POL_NONEE"></a>

    <a id="_CPPv3N15_dlp_polarity_e16DRV_DLP_POL_NONEE"></a> <a id="_CPPv2N15_dlp_polarity_e16DRV_DLP_POL_NONEE"></a> <a id="drv__dlp_8h_1a1791fa28882961c1928d527603788dc3a5578f69e664e8d85b981c881dcebc98d"></a> enumerator DRV\_DLP\_POL\_NONE
    :   CTS/RTX极性: 低允许，高阻止

        CTS/RTX极性: 不启用 (常用，需要和对方匹配)

<a id="_CPPv413_dlp_in_ctl_e"></a>

<a id="_CPPv313_dlp_in_ctl_e"></a> <a id="_CPPv213_dlp_in_ctl_e"></a> <a id="drv__dlp_8h_1aa74acf9df8b0e86d2dd142314767ad20"></a> enum \_dlp\_in\_ctl\_e
:   *Values:*

    <a id="_CPPv4N13_dlp_in_ctl_e19DRV_DLP_IN_AUTO_CTLE"></a>

    <a id="_CPPv3N13_dlp_in_ctl_e19DRV_DLP_IN_AUTO_CTLE"></a> <a id="_CPPv2N13_dlp_in_ctl_e19DRV_DLP_IN_AUTO_CTLE"></a> <a id="drv__dlp_8h_1aa74acf9df8b0e86d2dd142314767ad20a44fbf4e4734b5b0306b6429415aad714"></a> enumerator DRV\_DLP\_IN\_AUTO\_CTL

    <a id="_CPPv4N13_dlp_in_ctl_e25DRV_DLP_IN_MANUAL_DISABLEE"></a>

    <a id="_CPPv3N13_dlp_in_ctl_e25DRV_DLP_IN_MANUAL_DISABLEE"></a> <a id="_CPPv2N13_dlp_in_ctl_e25DRV_DLP_IN_MANUAL_DISABLEE"></a> <a id="drv__dlp_8h_1aa74acf9df8b0e86d2dd142314767ad20ad696a65d79c231f3265b74dea4d496b9"></a> enumerator DRV\_DLP\_IN\_MANUAL\_DISABLE
    :   DLP自动控制端口输入使能 (default)

    <a id="_CPPv4N13_dlp_in_ctl_e32DRV_DLP_IN_MANUAL_ENABLE_FORCE_1E"></a>

    <a id="_CPPv3N13_dlp_in_ctl_e32DRV_DLP_IN_MANUAL_ENABLE_FORCE_1E"></a> <a id="_CPPv2N13_dlp_in_ctl_e32DRV_DLP_IN_MANUAL_ENABLE_FORCE_1E"></a> <a id="drv__dlp_8h_1aa74acf9df8b0e86d2dd142314767ad20acff6ea6713d186a555962324e6a633a5"></a> enumerator DRV\_DLP\_IN\_MANUAL\_ENABLE\_FORCE\_1
    :   SW手动控制输入，关闭

    <a id="_CPPv4N13_dlp_in_ctl_e33DRV_DLP_IN_MANUAL_ENABLE_FROM_EXTE"></a>

    <a id="_CPPv3N13_dlp_in_ctl_e33DRV_DLP_IN_MANUAL_ENABLE_FROM_EXTE"></a> <a id="_CPPv2N13_dlp_in_ctl_e33DRV_DLP_IN_MANUAL_ENABLE_FROM_EXTE"></a> <a id="drv__dlp_8h_1aa74acf9df8b0e86d2dd142314767ad20a804c311cf819abaa7e23e5f37b195d2d"></a> enumerator DRV\_DLP\_IN\_MANUAL\_ENABLE\_FROM\_EXT
    :   SW手动控制输入，打开并强制成1.

<a id="_CPPv414_dlp_out_ctl_e"></a>

<a id="_CPPv314_dlp_out_ctl_e"></a> <a id="_CPPv214_dlp_out_ctl_e"></a> <a id="drv__dlp_8h_1ab40e5e06d54168dd277eea26417e9a10"></a> enum \_dlp\_out\_ctl\_e
:   *Values:*

    <a id="_CPPv4N14_dlp_out_ctl_e20DRV_DLP_OUT_AUTO_CTLE"></a>

    <a id="_CPPv3N14_dlp_out_ctl_e20DRV_DLP_OUT_AUTO_CTLE"></a> <a id="_CPPv2N14_dlp_out_ctl_e20DRV_DLP_OUT_AUTO_CTLE"></a> <a id="drv__dlp_8h_1ab40e5e06d54168dd277eea26417e9a10a063ac0a9b0558e71d32e037d6fd823d4"></a> enumerator DRV\_DLP\_OUT\_AUTO\_CTL

    <a id="_CPPv4N14_dlp_out_ctl_e26DRV_DLP_OUT_MANUAL_DISABLEE"></a>

    <a id="_CPPv3N14_dlp_out_ctl_e26DRV_DLP_OUT_MANUAL_DISABLEE"></a> <a id="_CPPv2N14_dlp_out_ctl_e26DRV_DLP_OUT_MANUAL_DISABLEE"></a> <a id="drv__dlp_8h_1ab40e5e06d54168dd277eea26417e9a10aab0b8d6d37e97c05649e022ee2d9f81d"></a> enumerator DRV\_DLP\_OUT\_MANUAL\_DISABLE
    :   DLP自动控制端口输入使能 (default)

    <a id="_CPPv4N14_dlp_out_ctl_e33DRV_DLP_OUT_MANUAL_ENABLE_FORCE_1E"></a>

    <a id="_CPPv3N14_dlp_out_ctl_e33DRV_DLP_OUT_MANUAL_ENABLE_FORCE_1E"></a> <a id="_CPPv2N14_dlp_out_ctl_e33DRV_DLP_OUT_MANUAL_ENABLE_FORCE_1E"></a> <a id="drv__dlp_8h_1ab40e5e06d54168dd277eea26417e9a10a4e2b3d59b310b19face10339d7b1cdb1"></a> enumerator DRV\_DLP\_OUT\_MANUAL\_ENABLE\_FORCE\_1
    :   SW手动控制输入，关闭

    <a id="_CPPv4N14_dlp_out_ctl_e33DRV_DLP_OUT_MANUAL_ENABLE_FORCE_0E"></a>

    <a id="_CPPv3N14_dlp_out_ctl_e33DRV_DLP_OUT_MANUAL_ENABLE_FORCE_0E"></a> <a id="_CPPv2N14_dlp_out_ctl_e33DRV_DLP_OUT_MANUAL_ENABLE_FORCE_0E"></a> <a id="drv__dlp_8h_1ab40e5e06d54168dd277eea26417e9a10ac49d9df95993adda7e25242d7d7a56ac"></a> enumerator DRV\_DLP\_OUT\_MANUAL\_ENABLE\_FORCE\_0
    :   SW手动控制输入，打开并强制成1.

    <a id="_CPPv4N14_dlp_out_ctl_e34DRV_DLP_OUT_MANUAL_ENABLE_FROM_DLPE"></a>

    <a id="_CPPv3N14_dlp_out_ctl_e34DRV_DLP_OUT_MANUAL_ENABLE_FROM_DLPE"></a> <a id="_CPPv2N14_dlp_out_ctl_e34DRV_DLP_OUT_MANUAL_ENABLE_FROM_DLPE"></a> <a id="drv__dlp_8h_1ab40e5e06d54168dd277eea26417e9a10a2908226276a05fadf4b78ab1ef08de26"></a> enumerator DRV\_DLP\_OUT\_MANUAL\_ENABLE\_FROM\_DLP
    :   SW手动控制输入，打开并强制成0.
