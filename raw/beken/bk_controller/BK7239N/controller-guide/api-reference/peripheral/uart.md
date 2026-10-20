---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/api-reference/peripheral/uart.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="uart-api"></a>

# UART API

UART (Universal Asynchronous Receiver/Transmitter) 通用异步收发器API接口。

<a id="header-file"></a>

## Header File

- [uart.h](https://github.com/bekencorp/armino/blob/main/components/uart.h)

<a id="functions"></a>

## Functions

<a id="_CPPv419bk_uart_driver_initv"></a>

<a id="_CPPv319bk_uart_driver_initv"></a> <a id="_CPPv219bk_uart_driver_initv"></a> <a id="bk_uart_driver_init__void"></a> <a id="uart_8h_1abd92212cd1f5b55df632ec5fcc431779"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_driver\_init(void)
:   Init the UART driver.

    This API init the resoure common to all UART id:

    - Init UART driver control memory

    **Attention**
    :   1\. This API should be called before any other UART APIs.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_uart_driver_deinitv"></a>

<a id="_CPPv321bk_uart_driver_deinitv"></a> <a id="_CPPv221bk_uart_driver_deinitv"></a> <a id="bk_uart_driver_deinit__void"></a> <a id="uart_8h_1a2b16b30a29fc09cf5be90835fddcb244"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_driver\_deinit(void)
:   Deinit the UART driver.

    This API free all resource related to UART and power down all UART id.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv418bk_uart_is_in_used9uart_id_t"></a>

<a id="_CPPv318bk_uart_is_in_used9uart_id_t"></a> <a id="_CPPv218bk_uart_is_in_used9uart_id_t"></a> <a id="bk_uart_is_in_used__uart_id_t"></a> <a id="uart_8h_1acc1baf45503e8d325a52a237c65aa08c"></a> int bk\_uart\_is\_in\_used(uart\_id\_t id)
:   Get the UART whether in used.

    参数
    :   **id** – UART id

    返回
    :   - 1: in used
        - 0: not in used

<a id="_CPPv412bk_uart_init9uart_id_tPK13uart_config_t"></a>

<a id="_CPPv312bk_uart_init9uart_id_tPK13uart_config_t"></a> <a id="_CPPv212bk_uart_init9uart_id_tPK13uart_config_t"></a> <a id="bk_uart_init__uart_id_t.uart_config_tCP"></a> <a id="uart_8h_1aa366f9681fc381f97271d0e9ca3dd9d4"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_init(uart\_id\_t id, const uart\_config\_t \*config)
:   Init the UART id.

    This API init the UART id:

    - Power up the UART id
    - Configure the UART id clock
    - Map the UART id to dedicated GPIO port
    - Set the UART baud rate, data bits, parity, stop bits,flow ctrl and source clock
    - Start the UART id

    参数
    :   - **id** – UART id
        - **config** – UART parameter settings

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_UART\_NOT\_INIT: UART driver not init
        - BK\_ERR\_NULL\_PARAM: UART config parameter is NULL
        - BK\_ERR\_UART\_INVALID\_ID: UART id is invalid
        - BK\_ERR\_UART\_BAUD\_RATE\_NOT\_SUPPORT: UART baud rate is not support
        - others: other errors.

<a id="_CPPv414bk_uart_deinit9uart_id_t"></a>

<a id="_CPPv314bk_uart_deinit9uart_id_t"></a> <a id="_CPPv214bk_uart_deinit9uart_id_t"></a> <a id="bk_uart_deinit__uart_id_t"></a> <a id="uart_8h_1a96927d97c084e3c3e5d5f173aca2f5e0"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_deinit(uart\_id\_t id)
:   Deinit the UART id.

    This API deinit the UART id:

    - Stop the UART id
    - Reset all configuration of UART id to default value
    - Disable the UART id interrupt
    - Power down the UART id

    参数
    :   **id** – UART id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_uart_set_baud_rate9uart_id_t8uint32_t"></a>

<a id="_CPPv321bk_uart_set_baud_rate9uart_id_t8uint32_t"></a> <a id="_CPPv221bk_uart_set_baud_rate9uart_id_t8uint32_t"></a> <a id="bk_uart_set_baud_rate__uart_id_t.uint32_t"></a> <a id="uart_8h_1adef7c82ff3defca050d3281eb1b00f32"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_set\_baud\_rate(uart\_id\_t id, uint32\_t baud\_rate)
:   Set the UART baud rate.

    参数
    :   - **id** – UART id
        - **baud\_rate** – UART baud rate

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_uart_set_data_bits9uart_id_t16uart_data_bits_t"></a>

<a id="_CPPv321bk_uart_set_data_bits9uart_id_t16uart_data_bits_t"></a> <a id="_CPPv221bk_uart_set_data_bits9uart_id_t16uart_data_bits_t"></a> <a id="bk_uart_set_data_bits__uart_id_t.uart_data_bits_t"></a> <a id="uart_8h_1a67af278ec4b7f849105a35b675256130"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_set\_data\_bits(uart\_id\_t id, uart\_data\_bits\_t data\_bits)
:   Set the UART data bits.

    参数
    :   - **id** – UART id
        - **data\_bits** – UART data bits

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_uart_set_stop_bits9uart_id_t16uart_stop_bits_t"></a>

<a id="_CPPv321bk_uart_set_stop_bits9uart_id_t16uart_stop_bits_t"></a> <a id="_CPPv221bk_uart_set_stop_bits9uart_id_t16uart_stop_bits_t"></a> <a id="bk_uart_set_stop_bits__uart_id_t.uart_stop_bits_t"></a> <a id="uart_8h_1a24379d32c46e9dbd3f118f92cf2c33b4"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_set\_stop\_bits(uart\_id\_t id, uart\_stop\_bits\_t stop\_bits)
:   Set the UART stop bits.

    参数
    :   - **id** – UART id
        - **stop\_bits** – UART stop bits

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv418bk_uart_set_parity9uart_id_t13uart_parity_t"></a>

<a id="_CPPv318bk_uart_set_parity9uart_id_t13uart_parity_t"></a> <a id="_CPPv218bk_uart_set_parity9uart_id_t13uart_parity_t"></a> <a id="bk_uart_set_parity__uart_id_t.uart_parity_t"></a> <a id="uart_8h_1a5b195b37d59daa3f35058c01cfb28525"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_set\_parity(uart\_id\_t id, uart\_parity\_t partiy)
:   Set the UART partiy.

    参数
    :   - **id** – UART id
        - **partiy** – UART partiy

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_uart_set_hw_flow_ctrl9uart_id_t7uint8_t"></a>

<a id="_CPPv324bk_uart_set_hw_flow_ctrl9uart_id_t7uint8_t"></a> <a id="_CPPv224bk_uart_set_hw_flow_ctrl9uart_id_t7uint8_t"></a> <a id="bk_uart_set_hw_flow_ctrl__uart_id_t.uint8_t"></a> <a id="uart_8h_1a83405465cbd6b6737ba394ccb9a6d8d3"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_set\_hw\_flow\_ctrl(uart\_id\_t id, uint8\_t rx\_threshold)
:   Set the UART hardware flow control.

    参数
    :   - **id** – UART id
        - **rx\_threshold** – Threshold of Hardware RX flow control

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv429bk_uart_set_rx_full_threshold9uart_id_t7uint8_t"></a>

<a id="_CPPv329bk_uart_set_rx_full_threshold9uart_id_t7uint8_t"></a> <a id="_CPPv229bk_uart_set_rx_full_threshold9uart_id_t7uint8_t"></a> <a id="bk_uart_set_rx_full_threshold__uart_id_t.uint8_t"></a> <a id="uart_8h_1a34cd98a7d1edafd54c3aa02fb41e4beb"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_set\_rx\_full\_threshold(uart\_id\_t id, uint8\_t threshold)
:   Set the UART threshold value for RX fifo full.

    参数
    :   - **id** – UART id
        - **threshold** – Threshold value above which RX fifo full interrupt is generated

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv430bk_uart_set_tx_empty_threshold9uart_id_t7uint8_t"></a>

<a id="_CPPv330bk_uart_set_tx_empty_threshold9uart_id_t7uint8_t"></a> <a id="_CPPv230bk_uart_set_tx_empty_threshold9uart_id_t7uint8_t"></a> <a id="bk_uart_set_tx_empty_threshold__uart_id_t.uint8_t"></a> <a id="uart_8h_1a6d2ac43d5689e6de9f211e0395d3a903"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_set\_tx\_empty\_threshold(uart\_id\_t id, uint8\_t threshold)
:   Set the UART threshold value for TX fifo empty.

    参数
    :   - **id** – UART id
        - **threshold** – Threshold value below which TX fifo empty interrupt is generated

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv422bk_uart_set_rx_timeout9uart_id_t26uart_rx_stop_detect_time_t"></a>

<a id="_CPPv322bk_uart_set_rx_timeout9uart_id_t26uart_rx_stop_detect_time_t"></a> <a id="_CPPv222bk_uart_set_rx_timeout9uart_id_t26uart_rx_stop_detect_time_t"></a> <a id="bk_uart_set_rx_timeout__uart_id_t.uart_rx_stop_detect_time_t"></a> <a id="uart_8h_1ae707e4ec262e9d4db0c52d1f532ca3c1"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_set\_rx\_timeout(uart\_id\_t id, uart\_rx\_stop\_detect\_time\_t timeout\_thresh)
:   Set the UART threshold timeout for receive data, unit is bit.

    UART finish receiving data when the periods is more than timeout threshold. If the time is expired, the UART\_RX\_STOP\_END interrupt is triggered.

    参数
    :   - **id** – UART id
        - **timeout\_thresh** – timeout threshold

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv428bk_uart_disable_hw_flow_ctrl9uart_id_t"></a>

<a id="_CPPv328bk_uart_disable_hw_flow_ctrl9uart_id_t"></a> <a id="_CPPv228bk_uart_disable_hw_flow_ctrl9uart_id_t"></a> <a id="bk_uart_disable_hw_flow_ctrl__uart_id_t"></a> <a id="uart_8h_1a5864162dea6439cbf077665c56e25944"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_disable\_hw\_flow\_ctrl(uart\_id\_t id)
:   Disable the UART hardware flow control.

    参数
    :   **id** – UART id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv427bk_uart_enable_tx_interrupt9uart_id_t"></a>

<a id="_CPPv327bk_uart_enable_tx_interrupt9uart_id_t"></a> <a id="_CPPv227bk_uart_enable_tx_interrupt9uart_id_t"></a> <a id="bk_uart_enable_tx_interrupt__uart_id_t"></a> <a id="uart_8h_1a8f56a7d398f07681e458e85e81e648b7"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_enable\_tx\_interrupt(uart\_id\_t id)
:   Enable TX interrupt of UART id.

    参数
    :   **id** – UART id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv428bk_uart_disable_tx_interrupt9uart_id_t"></a>

<a id="_CPPv328bk_uart_disable_tx_interrupt9uart_id_t"></a> <a id="_CPPv228bk_uart_disable_tx_interrupt9uart_id_t"></a> <a id="bk_uart_disable_tx_interrupt__uart_id_t"></a> <a id="uart_8h_1ae03c2472fe40f3030c7ad514bc21077d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_disable\_tx\_interrupt(uart\_id\_t id)
:   Disable TX interrupt of UART id.

    参数
    :   **id** – UART id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv427bk_uart_enable_rx_interrupt9uart_id_t"></a>

<a id="_CPPv327bk_uart_enable_rx_interrupt9uart_id_t"></a> <a id="_CPPv227bk_uart_enable_rx_interrupt9uart_id_t"></a> <a id="bk_uart_enable_rx_interrupt__uart_id_t"></a> <a id="uart_8h_1a1e451bf8b496a126e65daf7c44ac1d7d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_enable\_rx\_interrupt(uart\_id\_t id)
:   Enable RX interrupt of UART id.

    参数
    :   **id** – UART id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv428bk_uart_disable_rx_interrupt9uart_id_t"></a>

<a id="_CPPv328bk_uart_disable_rx_interrupt9uart_id_t"></a> <a id="_CPPv228bk_uart_disable_rx_interrupt9uart_id_t"></a> <a id="bk_uart_disable_rx_interrupt__uart_id_t"></a> <a id="uart_8h_1abeeafeeda3af44fb807755ce56de631a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_disable\_rx\_interrupt(uart\_id\_t id)
:   Disable RX interrupt of UART id.

    参数
    :   **id** – UART id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv423bk_uart_register_rx_isr9uart_id_t10uart_isr_tPv"></a>

<a id="_CPPv323bk_uart_register_rx_isr9uart_id_t10uart_isr_tPv"></a> <a id="_CPPv223bk_uart_register_rx_isr9uart_id_t10uart_isr_tPv"></a> <a id="bk_uart_register_rx_isr__uart_id_t.uart_isr_t.voidP"></a> <a id="uart_8h_1af6e8991d43d98c508a9ae5df41a25f5d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_register\_rx\_isr(uart\_id\_t id, uart\_isr\_t isr, void \*param)
:   Register the RX interrupt service routine for UART id.

    参数
    :   - **id** – UART id
        - **isr** – UART RX callback
        - **param** – UART RX callback parameter

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv423bk_uart_register_tx_isr9uart_id_t10uart_isr_tPv"></a>

<a id="_CPPv323bk_uart_register_tx_isr9uart_id_t10uart_isr_tPv"></a> <a id="_CPPv223bk_uart_register_tx_isr9uart_id_t10uart_isr_tPv"></a> <a id="bk_uart_register_tx_isr__uart_id_t.uart_isr_t.voidP"></a> <a id="uart_8h_1a1df6660b23ed31501eb30a6f19d90613"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_register\_tx\_isr(uart\_id\_t id, uart\_isr\_t isr, void \*param)
:   Register the TX interrupt service routine for UART id.

    参数
    :   - **id** – UART id
        - **isr** – UART TX callback
        - **param** – UART TX callback parameter

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv419bk_uart_write_bytes9uart_id_tPKv8uint32_t"></a>

<a id="_CPPv319bk_uart_write_bytes9uart_id_tPKv8uint32_t"></a> <a id="_CPPv219bk_uart_write_bytes9uart_id_tPKv8uint32_t"></a> <a id="bk_uart_write_bytes__uart_id_t.voidCP.uint32_t"></a> <a id="uart_8h_1a07223aab417c84faf5775a3a8dae91cc"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_write\_bytes(uart\_id\_t id, const void \*data, uint32\_t size)
:   Send data to the UART port from a given buffer and length.

    参数
    :   - **id** – UART id
        - **data** – data buffer address
        - **size** – data length to send

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv418bk_uart_read_bytes9uart_id_tPv8uint32_t8uint32_t"></a>

<a id="_CPPv318bk_uart_read_bytes9uart_id_tPv8uint32_t8uint32_t"></a> <a id="_CPPv218bk_uart_read_bytes9uart_id_tPv8uint32_t8uint32_t"></a> <a id="bk_uart_read_bytes__uart_id_t.voidP.uint32_t.uint32_t"></a> <a id="uart_8h_1a88678d1509683ed85977ff29beeaf4b0"></a> int bk\_uart\_read\_bytes(uart\_id\_t id, void \*data, uint32\_t size, uint32\_t timeout\_ms)
:   UART read bytes from UART buffer.

    参数
    :   - **id** – UART id
        - **data** – pointer to the buffer
        - **size** – data length to read
        - **timeout\_ms** – timeout ms, if set BEKEN\_WAIT\_FOREVER, read will wait forever

    返回
    :   - BK\_ERR\_UART\_NOT\_INIT: UART driver not init
        - BK\_ERR\_UART\_INVALID\_ID: UART id number is invalid
        - BK\_ERR\_UART\_ID\_NOT\_INIT: UART id not init
        - BK\_ERR\_UART\_RX\_TIMEOUT: UART receive data timeout
        - others (\>\=0): The number of bytes read from UART FIFO

<a id="_CPPv418bk_uart_disable_rx9uart_id_t"></a>

<a id="_CPPv318bk_uart_disable_rx9uart_id_t"></a> <a id="_CPPv218bk_uart_disable_rx9uart_id_t"></a> <a id="bk_uart_disable_rx__uart_id_t"></a> <a id="uart_8h_1a4284d274c68eac6d19c5c53fd69dbac7"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_disable\_rx(uart\_id\_t id)
:   Disable UART TX pin and set as GPIO.

    参数
    :   **id** – UART id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv418bk_uart_disable_tx9uart_id_t"></a>

<a id="_CPPv318bk_uart_disable_tx9uart_id_t"></a> <a id="_CPPv218bk_uart_disable_tx9uart_id_t"></a> <a id="bk_uart_disable_tx__uart_id_t"></a> <a id="uart_8h_1a333655ff2c604a3cda4fa417061fada9"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_disable\_tx(uart\_id\_t id)
:   Disable UART TX pin and set as GPIO.

    参数
    :   **id** – UART id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_uart_set_enable_rx9uart_id_tb"></a>

<a id="_CPPv321bk_uart_set_enable_rx9uart_id_tb"></a> <a id="_CPPv221bk_uart_set_enable_rx9uart_id_tb"></a> <a id="bk_uart_set_enable_rx__uart_id_t.b"></a> <a id="uart_8h_1af7875e8bb3d86afd73d4184d07342e00"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_set\_enable\_rx(uart\_id\_t id, bool enable)
:   Just set UART RX enable/disable, doesn’t set pin.

    参数
    :   - **id** – UART id
        - **enable** – true, enable, flase disable

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_uart_set_enable_tx9uart_id_tb"></a>

<a id="_CPPv321bk_uart_set_enable_tx9uart_id_tb"></a> <a id="_CPPv221bk_uart_set_enable_tx9uart_id_tb"></a> <a id="bk_uart_set_enable_tx__uart_id_t.b"></a> <a id="uart_8h_1a3114673fe7d05cc94a39f07d63e8e81e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_set\_enable\_tx(uart\_id\_t id, bool enable)
:   Just set UART TX enable/disable, doesn’t set pin.

    参数
    :   - **id** – UART id
        - **enable** – true, enable, flase disable

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv422bk_uart_enable_sw_fifo9uart_id_t"></a>

<a id="_CPPv322bk_uart_enable_sw_fifo9uart_id_t"></a> <a id="_CPPv222bk_uart_enable_sw_fifo9uart_id_t"></a> <a id="bk_uart_enable_sw_fifo__uart_id_t"></a> <a id="uart_8h_1a4b7066e88d2722ca2fa71d2c00d5f295"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_enable\_sw\_fifo(uart\_id\_t id)
:   Enable UART software fifo.

    参数
    :   **id** – UART id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv423bk_uart_disable_sw_fifo9uart_id_t"></a>

<a id="_CPPv323bk_uart_disable_sw_fifo9uart_id_t"></a> <a id="_CPPv223bk_uart_disable_sw_fifo9uart_id_t"></a> <a id="bk_uart_disable_sw_fifo__uart_id_t"></a> <a id="uart_8h_1a1f32ea1ba2f648b9ef31ccd3cd2538b9"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_disable\_sw\_fifo(uart\_id\_t id)
:   Disable UART software fifo.

    参数
    :   **id** – UART id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv427bk_uart_get_ate_detect_gpiov"></a>

<a id="_CPPv327bk_uart_get_ate_detect_gpiov"></a> <a id="_CPPv227bk_uart_get_ate_detect_gpiov"></a> <a id="bk_uart_get_ate_detect_gpio__void"></a> <a id="uart_8h_1a7d4179e33656db22820efdf4ace65617"></a> uint32\_t bk\_uart\_get\_ate\_detect\_gpio(void)
:   Get the gpio pin when in ate detect.

    返回
    :   the ate detect gpio pin

<a id="_CPPv419bk_uart_take_rx_isr9uart_id_t10uart_isr_tPv"></a>

<a id="_CPPv319bk_uart_take_rx_isr9uart_id_t10uart_isr_tPv"></a> <a id="_CPPv219bk_uart_take_rx_isr9uart_id_t10uart_isr_tPv"></a> <a id="bk_uart_take_rx_isr__uart_id_t.uart_isr_t.voidP"></a> <a id="uart_8h_1a68bb06e73d9d94e83c611d5ab21ad5fe"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_take\_rx\_isr(uart\_id\_t id, uart\_isr\_t isr, void \*param)
:   Register uart rx isr and disable software fifo.

    参数
    :   - **id** – UART id
        - **isr** – UART RX callback
        - **param** – UART RX callback parameter

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv422bk_uart_recover_rx_isr9uart_id_t"></a>

<a id="_CPPv322bk_uart_recover_rx_isr9uart_id_t"></a> <a id="_CPPv222bk_uart_recover_rx_isr9uart_id_t"></a> <a id="bk_uart_recover_rx_isr__uart_id_t"></a> <a id="uart_8h_1a61bcdf6565864f96a7a131a147d47de9"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_recover\_rx\_isr(uart\_id\_t id)
:   Recover uart rx isr.

    参数
    :   **id** – UART id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv418bk_uart_is_tx_over9uart_id_t"></a>

<a id="_CPPv318bk_uart_is_tx_over9uart_id_t"></a> <a id="_CPPv218bk_uart_is_tx_over9uart_id_t"></a> <a id="bk_uart_is_tx_over__uart_id_t"></a> <a id="uart_8h_1a862a267ce05b9190429415ef847bb5bb"></a> bool bk\_uart\_is\_tx\_over(uart\_id\_t id)
:   Get whether the uart tx over(tx fifo empty)

    参数
    :   **id** – UART id

    返回
    :   - true: uart tx over
        - false: uart tx not over

<a id="_CPPv417bk_uart_pm_backup9uart_id_t"></a>

<a id="_CPPv317bk_uart_pm_backup9uart_id_t"></a> <a id="_CPPv217bk_uart_pm_backup9uart_id_t"></a> <a id="bk_uart_pm_backup__uart_id_t"></a> <a id="uart_8h_1ad1f6fec53a9adea02c9a33b7b56c8845"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uart\_pm\_backup(uart\_id\_t id)
:   Backup uart config.

    参数
    :   **id** – UART id

    返回
    :   - BK\_OK: succeed
        - others: other errors.
