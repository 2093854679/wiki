# UART[](#uart "永久链接至标题")

[[English]](../../../../en/v1.5/api-reference/peripheral/bk_uart.html "../../../../en/v1.5/api-reference/peripheral/bk_uart.html")


## UART API Status[](#uart-api-status "永久链接至标题")

| API | BK7256 | BK7256_cp1 |
| --- | --- | --- |
| [`bk_uart_driver_init()`](#_CPPv419bk_uart_driver_initv "bk_uart_driver_init") | Y | Y |
| [`bk_uart_driver_deinit()`](#_CPPv421bk_uart_driver_deinitv "bk_uart_driver_deinit") | Y | Y |
| [`bk_uart_init()`](#_CPPv412bk_uart_init9uart_id_tPK13uart_config_t "bk_uart_init") | Y | Y |
| [`bk_uart_deinit()`](#_CPPv414bk_uart_deinit9uart_id_t "bk_uart_deinit") | Y | Y |
| [`bk_uart_set_baud_rate()`](#_CPPv421bk_uart_set_baud_rate9uart_id_t8uint32_t "bk_uart_set_baud_rate") | Y | Y |
| [`bk_uart_set_data_bits()`](#_CPPv421bk_uart_set_data_bits9uart_id_t16uart_data_bits_t "bk_uart_set_data_bits") | Y | Y |
| [`bk_uart_set_stop_bits()`](#_CPPv421bk_uart_set_stop_bits9uart_id_t16uart_stop_bits_t "bk_uart_set_stop_bits") | Y | Y |
| [`bk_uart_set_parity()`](#_CPPv418bk_uart_set_parity9uart_id_t13uart_parity_t "bk_uart_set_parity") | Y | Y |
| [`bk_uart_set_hw_flow_ctrl()`](#_CPPv424bk_uart_set_hw_flow_ctrl9uart_id_t7uint8_t "bk_uart_set_hw_flow_ctrl") | Y | Y |
| [`bk_uart_set_rx_full_threshold()`](#_CPPv429bk_uart_set_rx_full_threshold9uart_id_t7uint8_t "bk_uart_set_rx_full_threshold") | Y | Y |
| [`bk_uart_set_tx_empty_threshold()`](#_CPPv430bk_uart_set_tx_empty_threshold9uart_id_t7uint8_t "bk_uart_set_tx_empty_threshold") | Y | Y |
| [`bk_uart_set_rx_timeout()`](#_CPPv422bk_uart_set_rx_timeout9uart_id_t26uart_rx_stop_detect_time_t "bk_uart_set_rx_timeout") | Y | Y |
| [`bk_uart_disable_hw_flow_ctrl()`](#_CPPv428bk_uart_disable_hw_flow_ctrl9uart_id_t "bk_uart_disable_hw_flow_ctrl") | Y | Y |
| [`bk_uart_enable_tx_interrupt()`](#_CPPv427bk_uart_enable_tx_interrupt9uart_id_t "bk_uart_enable_tx_interrupt") | Y | Y |
| [`bk_uart_disable_tx_interrupt()`](#_CPPv428bk_uart_disable_tx_interrupt9uart_id_t "bk_uart_disable_tx_interrupt") | Y | Y |
| [`bk_uart_enable_rx_interrupt()`](#_CPPv427bk_uart_enable_rx_interrupt9uart_id_t "bk_uart_enable_rx_interrupt") | Y | Y |
| [`bk_uart_disable_rx_interrupt()`](#_CPPv428bk_uart_disable_rx_interrupt9uart_id_t "bk_uart_disable_rx_interrupt") | Y | Y |
| [`bk_uart_register_rx_isr()`](#_CPPv423bk_uart_register_rx_isr9uart_id_t10uart_isr_tPv "bk_uart_register_rx_isr") | Y | Y |
| [`bk_uart_register_tx_isr()`](#_CPPv423bk_uart_register_tx_isr9uart_id_t10uart_isr_tPv "bk_uart_register_tx_isr") | Y | Y |
| [`bk_uart_write_bytes()`](#_CPPv419bk_uart_write_bytes9uart_id_tPKv8uint32_t "bk_uart_write_bytes") | Y | Y |
| [`bk_uart_read_bytes()`](#_CPPv418bk_uart_read_bytes9uart_id_tPv8uint32_t8uint32_t "bk_uart_read_bytes") | Y | Y |
| [`bk_uart_disable_rx()`](#_CPPv418bk_uart_disable_rx9uart_id_t "bk_uart_disable_rx") | Y | Y |
| [`bk_uart_disable_tx()`](#_CPPv418bk_uart_disable_tx9uart_id_t "bk_uart_disable_tx") | Y | Y |
| [`bk_uart_enable_sw_fifo()`](#_CPPv422bk_uart_enable_sw_fifo9uart_id_t "bk_uart_enable_sw_fifo") | Y | Y |
| [`bk_uart_disable_sw_fifo()`](#_CPPv423bk_uart_disable_sw_fifo9uart_id_t "bk_uart_disable_sw_fifo") | Y | Y |


## UART Port Number[](#uart-port-number "永久链接至标题")

| Capability | BK7256 | BK7256_cp1 |
| --- | --- | --- |
| Port Number | 3 | 3 |


## UART Pin and GPIO Map[](#uart-pin-and-gpio-map "永久链接至标题")

| UART Pin | BK7256 | BK7256_cp1 |
| --- | --- | --- |
| UART1 TX | 11 | 11 |
| UART1 RX | 10 | 10 |
| UART2 TX | 0 | 0 |
| UART2 RX | 1 | 1 |
| UART3 TX | 41 | 41 |
| UART3 RX | 40 | 40 |


## UART API Reference[](#uart-api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [uart.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/uart.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/uart.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_driver_init(void)[](#_CPPv419bk_uart_driver_initv "永久链接至目标")
:   Init the UART driver.

    This API init the resoure common to all UART id:


    - Init UART driver control memory


    **Attention**
    :   1. This API should be called before any other UART APIs.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_driver_deinit(void)[](#_CPPv421bk_uart_driver_deinitv "永久链接至目标")
:   Deinit the UART driver.

    This API free all resource related to UART and power down all UART id.

    返回
    :   - BK_OK: succeed

        - others: other errors.

int bk_uart_is_in_used([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id)[](#_CPPv418bk_uart_is_in_used9uart_id_t "永久链接至目标")
:   Get the UART whether in used.

    参数
    :   **id** – UART id

    返回
    :   - 1: in used

        - 0: not in used

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_init([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id, const [uart_config_t](#_CPPv413uart_config_t "uart_config_t") *config)[](#_CPPv412bk_uart_init9uart_id_tPK13uart_config_t "永久链接至目标")
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
    :   - BK_OK: succeed

        - BK_ERR_UART_NOT_INIT: UART driver not init

        - BK_ERR_NULL_PARAM: UART config parameter is NULL

        - BK_ERR_UART_INVALID_ID: UART id is invalid

        - BK_ERR_UART_BAUD_RATE_NOT_SUPPORT: UART baud rate is not support

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_deinit([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id)[](#_CPPv414bk_uart_deinit9uart_id_t "永久链接至目标")
:   Deinit the UART id.

    This API deinit the UART id:


    - Stop the UART id

    - Reset all configuration of UART id to default value

    - Disable the UART id interrupt

    - Power down the UART id

    参数
    :   **id** – UART id

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_set_baud_rate([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id, uint32_t baud_rate)[](#_CPPv421bk_uart_set_baud_rate9uart_id_t8uint32_t "永久链接至目标")
:   Set the UART baud rate.

    参数
    :   - **id** – UART id

        - **baud_rate** – UART baud rate

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_set_data_bits([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id, [uart_data_bits_t](#_CPPv416uart_data_bits_t "uart_data_bits_t") data_bits)[](#_CPPv421bk_uart_set_data_bits9uart_id_t16uart_data_bits_t "永久链接至目标")
:   Set the UART data bits.

    参数
    :   - **id** – UART id

        - **data_bits** – UART data bits

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_set_stop_bits([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id, [uart_stop_bits_t](#_CPPv416uart_stop_bits_t "uart_stop_bits_t") stop_bits)[](#_CPPv421bk_uart_set_stop_bits9uart_id_t16uart_stop_bits_t "永久链接至目标")
:   Set the UART stop bits.

    参数
    :   - **id** – UART id

        - **stop_bits** – UART stop bits

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_set_parity([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id, [uart_parity_t](#_CPPv413uart_parity_t "uart_parity_t") partiy)[](#_CPPv418bk_uart_set_parity9uart_id_t13uart_parity_t "永久链接至目标")
:   Set the UART partiy.

    参数
    :   - **id** – UART id

        - **partiy** – UART partiy

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_set_hw_flow_ctrl([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id, uint8_t rx_threshold)[](#_CPPv424bk_uart_set_hw_flow_ctrl9uart_id_t7uint8_t "永久链接至目标")
:   Set the UART hardware flow control.

    参数
    :   - **id** – UART id

        - **rx_threshold** – Threshold of Hardware RX flow control

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_set_rx_full_threshold([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id, uint8_t threshold)[](#_CPPv429bk_uart_set_rx_full_threshold9uart_id_t7uint8_t "永久链接至目标")
:   Set the UART threshold value for RX fifo full.

    参数
    :   - **id** – UART id

        - **threshold** – Threshold value above which RX fifo full interrupt is generated

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_set_tx_empty_threshold([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id, uint8_t threshold)[](#_CPPv430bk_uart_set_tx_empty_threshold9uart_id_t7uint8_t "永久链接至目标")
:   Set the UART threshold value for TX fifo empty.

    参数
    :   - **id** – UART id

        - **threshold** – Threshold value below which TX fifo empty interrupt is generated

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_set_rx_timeout([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id, [uart_rx_stop_detect_time_t](#_CPPv426uart_rx_stop_detect_time_t "uart_rx_stop_detect_time_t") timeout_thresh)[](#_CPPv422bk_uart_set_rx_timeout9uart_id_t26uart_rx_stop_detect_time_t "永久链接至目标")
:   Set the UART threshold timeout for receive data, unit is bit.

    UART finish receiving data when the periods is more than timeout threshold. If the time is expired, the UART_RX_STOP_END interrupt is triggered.

    参数
    :   - **id** – UART id

        - **timeout_thresh** – timeout threshold

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_disable_hw_flow_ctrl([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id)[](#_CPPv428bk_uart_disable_hw_flow_ctrl9uart_id_t "永久链接至目标")
:   Disable the UART hardware flow control.

    参数
    :   **id** – UART id

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_enable_tx_interrupt([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id)[](#_CPPv427bk_uart_enable_tx_interrupt9uart_id_t "永久链接至目标")
:   Enable TX interrupt of UART id.

    参数
    :   **id** – UART id

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_disable_tx_interrupt([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id)[](#_CPPv428bk_uart_disable_tx_interrupt9uart_id_t "永久链接至目标")
:   Disable TX interrupt of UART id.

    参数
    :   **id** – UART id

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_enable_rx_interrupt([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id)[](#_CPPv427bk_uart_enable_rx_interrupt9uart_id_t "永久链接至目标")
:   Enable RX interrupt of UART id.

    参数
    :   **id** – UART id

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_disable_rx_interrupt([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id)[](#_CPPv428bk_uart_disable_rx_interrupt9uart_id_t "永久链接至目标")
:   Disable RX interrupt of UART id.

    参数
    :   **id** – UART id

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_register_rx_isr([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id, [uart_isr_t](#_CPPv410uart_isr_t "uart_isr_t") isr, void *param)[](#_CPPv423bk_uart_register_rx_isr9uart_id_t10uart_isr_tPv "永久链接至目标")
:   Register the RX interrupt service routine for UART id.

    参数
    :   - **id** – UART id

        - **isr** – UART RX callback

        - **param** – UART RX callback parameter

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_register_tx_isr([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id, [uart_isr_t](#_CPPv410uart_isr_t "uart_isr_t") isr, void *param)[](#_CPPv423bk_uart_register_tx_isr9uart_id_t10uart_isr_tPv "永久链接至目标")
:   Register the TX interrupt service routine for UART id.

    参数
    :   - **id** – UART id

        - **isr** – UART TX callback

        - **param** – UART TX callback parameter

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_write_bytes([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id, const void *data, uint32_t size)[](#_CPPv419bk_uart_write_bytes9uart_id_tPKv8uint32_t "永久链接至目标")
:   Send data to the UART port from a given buffer and length.

    参数
    :   - **id** – UART id

        - **data** – data buffer address

        - **size** – data length to send

    返回
    :   - BK_OK: succeed

        - others: other errors.

int bk_uart_read_bytes([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id, void *data, uint32_t size, uint32_t timeout_ms)[](#_CPPv418bk_uart_read_bytes9uart_id_tPv8uint32_t8uint32_t "永久链接至目标")
:   UART read bytes from UART buffer.

    参数
    :   - **id** – UART id

        - **data** – pointer to the buffer

        - **size** – data length to read

        - **timeout_ms** – timeout ms, if set BEKEN_WAIT_FOREVER, read will wait forever

    返回
    :   - BK_ERR_UART_NOT_INIT: UART driver not init

        - BK_ERR_UART_INVALID_ID: UART id number is invalid

        - BK_ERR_UART_ID_NOT_INIT: UART id not init

        - BK_ERR_UART_RX_TIMEOUT: UART receive data timeout

        - others (>=0): The number of bytes read from UART FIFO

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_disable_rx([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id)[](#_CPPv418bk_uart_disable_rx9uart_id_t "永久链接至目标")
:   Disable UART TX pin and set as GPIO.

    参数
    :   **id** – UART id

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_disable_tx([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id)[](#_CPPv418bk_uart_disable_tx9uart_id_t "永久链接至目标")
:   Disable UART TX pin and set as GPIO.

    参数
    :   **id** – UART id

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_set_enable_rx([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id, bool enable)[](#_CPPv421bk_uart_set_enable_rx9uart_id_tb "永久链接至目标")
:   Just set UART RX enable/disable, doesn’t set pin.

    参数
    :   - **id** – UART id

        - **enable, :** – true, enable, flase disable

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_set_enable_tx([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id, bool enable)[](#_CPPv421bk_uart_set_enable_tx9uart_id_tb "永久链接至目标")
:   Just set UART TX enable/disable, doesn’t set pin.

    参数
    :   - **id** – UART id

        - **enable, :** – true, enable, flase disable

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_enable_sw_fifo([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id)[](#_CPPv422bk_uart_enable_sw_fifo9uart_id_t "永久链接至目标")
:   Enable UART software fifo.

    参数
    :   **id** – UART id

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_disable_sw_fifo([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id)[](#_CPPv423bk_uart_disable_sw_fifo9uart_id_t "永久链接至目标")
:   Disable UART software fifo.

    参数
    :   **id** – UART id

    返回
    :   - BK_OK: succeed

        - others: other errors.

uint32_t bk_uart_get_ate_detect_gpio(void)[](#_CPPv427bk_uart_get_ate_detect_gpiov "永久链接至目标")
:   Get the gpio pin when in ate detect.

    返回
    :   the ate detect gpio pin

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_take_rx_isr([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id, [uart_isr_t](#_CPPv410uart_isr_t "uart_isr_t") isr, void *param)[](#_CPPv419bk_uart_take_rx_isr9uart_id_t10uart_isr_tPv "永久链接至目标")
:   Register uart rx isr and disable software fifo.

    参数
    :   - **id** – UART id

        - **isr** – UART RX callback

        - **param** – UART RX callback parameter

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uart_recover_rx_isr([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id)[](#_CPPv422bk_uart_recover_rx_isr9uart_id_t "永久链接至目标")
:   Recover uart rx isr.

    参数
    :   **id** – UART id

    返回
    :   - BK_OK: succeed

        - others: other errors.

bool bk_uart_is_tx_over([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id)[](#_CPPv418bk_uart_is_tx_over9uart_id_t "永久链接至目标")
:   Get whether the uart tx over(tx fifo empty)

    参数
    :   **id** – UART id

    返回
    :   - true: uart tx over

        - false: uart tx not over


## UART API Typedefs[](#uart-api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [uart_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/uart_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/uart_types.h")


### Macros[](#macros "永久链接至标题")

BK_ERR_UART_NOT_INIT[](#c.BK_ERR_UART_NOT_INIT "永久链接至目标")
:   UART driver not init

BK_ERR_UART_INVALID_ID[](#c.BK_ERR_UART_INVALID_ID "永久链接至目标")
:   UART id number is invalid

BK_ERR_UART_INVALID_SIZE[](#c.BK_ERR_UART_INVALID_SIZE "永久链接至目标")
:   UART read bytes length is more than fifo length

BK_ERR_UART_RX_TIMEOUT[](#c.BK_ERR_UART_RX_TIMEOUT "永久链接至目标")
:   UART receive data timeout

BK_ERR_UART_BAUD_RATE_NOT_SUPPORT[](#c.BK_ERR_UART_BAUD_RATE_NOT_SUPPORT "永久链接至目标")
:   UART baud rate not support

BK_ERR_UART_ID_NOT_INIT[](#c.BK_ERR_UART_ID_NOT_INIT "永久链接至目标")
:   UART id not init

BK_ERR_UART_MUTEX_INIT[](#c.BK_ERR_UART_MUTEX_INIT "永久链接至目标")
:   UART mutex init failed


### Type Definitions[](#type-definitions "永久链接至标题")

typedef void (*uart_isr_t)([uart_id_t](#_CPPv49uart_id_t "uart_id_t") id, void *param)[](#_CPPv410uart_isr_t "永久链接至目标")
:   UART interrupt service routine.


### Header File[](#id2 "永久链接至标题")


- [hal/hal_uart_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hal/hal_uart_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hal/hal_uart_types.h")


### Structures[](#structures "永久链接至标题")

struct uart_config_t[](#_CPPv413uart_config_t "永久链接至目标")
:   Public Members

    uint32_t baud_rate[](#_CPPv4N13uart_config_t9baud_rateE "永久链接至目标")
    :   UART baud rate

    [uart_data_bits_t](#_CPPv416uart_data_bits_t "uart_data_bits_t") data_bits[](#_CPPv4N13uart_config_t9data_bitsE "永久链接至目标")
    :   UART data bits

    [uart_parity_t](#_CPPv413uart_parity_t "uart_parity_t") parity[](#_CPPv4N13uart_config_t6parityE "永久链接至目标")
    :   UART parity

    [uart_stop_bits_t](#_CPPv416uart_stop_bits_t "uart_stop_bits_t") stop_bits[](#_CPPv4N13uart_config_t9stop_bitsE "永久链接至目标")
    :   UART stop bits

    [uart_flow_control_t](#_CPPv419uart_flow_control_t "uart_flow_control_t") flow_ctrl[](#_CPPv4N13uart_config_t9flow_ctrlE "永久链接至目标")
    :   UART flow control

    [uart_src_clk_t](#_CPPv414uart_src_clk_t "uart_src_clk_t") src_clk[](#_CPPv4N13uart_config_t7src_clkE "永久链接至目标")
    :   UART source clock


### Macros[](#id3 "永久链接至标题")

UART_BAUDRATE_3250000[](#c.UART_BAUDRATE_3250000 "永久链接至目标")

UART_BAUDRATE_2000000[](#c.UART_BAUDRATE_2000000 "永久链接至目标")

UART_BAUDRATE_921600[](#c.UART_BAUDRATE_921600 "永久链接至目标")

UART_BAUDRATE_460800[](#c.UART_BAUDRATE_460800 "永久链接至目标")

UART_BAUDRATE_230400[](#c.UART_BAUDRATE_230400 "永久链接至目标")

UART_BAUDRATE_115200[](#c.UART_BAUDRATE_115200 "永久链接至目标")

UART_BAUDRATE_3000[](#c.UART_BAUDRATE_3000 "永久链接至目标")

UART_BAUDRATE_19200[](#c.UART_BAUDRATE_19200 "永久链接至目标")

UART_BAUDRATE_9600[](#c.UART_BAUDRATE_9600 "永久链接至目标")

UART_BAUD_RATE[](#c.UART_BAUD_RATE "永久链接至目标")

UART_CLOCK_FREQ_10M[](#c.UART_CLOCK_FREQ_10M "永久链接至目标")

UART_CLOCK_FREQ_48M[](#c.UART_CLOCK_FREQ_48M "永久链接至目标")

UART_CLOCK_FREQ_24M[](#c.UART_CLOCK_FREQ_24M "永久链接至目标")

UART_CLOCK_FREQ_26M[](#c.UART_CLOCK_FREQ_26M "永久链接至目标")

UART_CLOCK_FREQ_52M[](#c.UART_CLOCK_FREQ_52M "永久链接至目标")

UART_CLOCK_FREQ_120M[](#c.UART_CLOCK_FREQ_120M "永久链接至目标")

UART_CLOCK[](#c.UART_CLOCK "永久链接至目标")

UART_TX_FIFO_THRESHOLD[](#c.UART_TX_FIFO_THRESHOLD "永久链接至目标")

UART_RX_FIFO_THRESHOLD[](#c.UART_RX_FIFO_THRESHOLD "永久链接至目标")


### Type Definitions[](#id4 "永久链接至标题")

typedef uint8_t uart_unit_t[](#_CPPv411uart_unit_t "永久链接至目标")
:   uart uint id


### Enumerations[](#enumerations "永久链接至标题")

enum uart_id_t[](#_CPPv49uart_id_t "永久链接至目标")
:   *Values:*

    enumerator UART_ID_0[](#_CPPv4N9uart_id_t9UART_ID_0E "永久链接至目标")
    :   UART id 0

    enumerator UART_ID_1[](#_CPPv4N9uart_id_t9UART_ID_1E "永久链接至目标")
    :   UART id 1

    enumerator UART_ID_2[](#_CPPv4N9uart_id_t9UART_ID_2E "永久链接至目标")
    :   UART id 2

    enumerator UART_ID_MAX[](#_CPPv4N9uart_id_t11UART_ID_MAXE "永久链接至目标")
    :   UART id max

enum uart_src_clk_t[](#_CPPv414uart_src_clk_t "永久链接至目标")
:   *Values:*

    enumerator UART_SCLK_DCO[](#_CPPv4N14uart_src_clk_t13UART_SCLK_DCOE "永久链接至目标")
    :   UART source clock dco

    enumerator UART_SCLK_XTAL_26M[](#_CPPv4N14uart_src_clk_t18UART_SCLK_XTAL_26ME "永久链接至目标")
    :   UART source clock xtal 26M

    enumerator UART_SCLK_APLL[](#_CPPv4N14uart_src_clk_t14UART_SCLK_APLLE "永久链接至目标")
    :   UART source clock apll

enum uart_frame_mode_t[](#_CPPv417uart_frame_mode_t "永久链接至目标")
:   *Values:*

    enumerator UART_MODE_UART[](#_CPPv4N17uart_frame_mode_t14UART_MODE_UARTE "永久链接至目标")
    :   UART frame mode uart

    enumerator UART_MODE_IDRA[](#_CPPv4N17uart_frame_mode_t14UART_MODE_IDRAE "永久链接至目标")
    :   UART frame mode idra

enum uart_data_bits_t[](#_CPPv416uart_data_bits_t "永久链接至目标")
:   *Values:*

    enumerator UART_DATA_5_BITS[](#_CPPv4N16uart_data_bits_t16UART_DATA_5_BITSE "永久链接至目标")
    :   UART data bits 5bits

    enumerator UART_DATA_6_BITS[](#_CPPv4N16uart_data_bits_t16UART_DATA_6_BITSE "永久链接至目标")
    :   UART data bits 6bits

    enumerator UART_DATA_7_BITS[](#_CPPv4N16uart_data_bits_t16UART_DATA_7_BITSE "永久链接至目标")
    :   UART data bits 7bits

    enumerator UART_DATA_8_BITS[](#_CPPv4N16uart_data_bits_t16UART_DATA_8_BITSE "永久链接至目标")
    :   UART data bits 8bits

enum uart_parity_t[](#_CPPv413uart_parity_t "永久链接至目标")
:   *Values:*

    enumerator UART_PARITY_NONE[](#_CPPv4N13uart_parity_t16UART_PARITY_NONEE "永久链接至目标")
    :   UART parity none

    enumerator UART_PARITY_ODD[](#_CPPv4N13uart_parity_t15UART_PARITY_ODDE "永久链接至目标")
    :   UART parity odd

    enumerator UART_PARITY_EVEN[](#_CPPv4N13uart_parity_t16UART_PARITY_EVENE "永久链接至目标")
    :   UART parity even

enum uart_stop_bits_t[](#_CPPv416uart_stop_bits_t "永久链接至目标")
:   *Values:*

    enumerator UART_STOP_BITS_1[](#_CPPv4N16uart_stop_bits_t16UART_STOP_BITS_1E "永久链接至目标")
    :   UART stop bits 1bit

    enumerator UART_STOP_BITS_2[](#_CPPv4N16uart_stop_bits_t16UART_STOP_BITS_2E "永久链接至目标")
    :   UART stop bits 2bits

enum uart_flow_control_t[](#_CPPv419uart_flow_control_t "永久链接至目标")
:   *Values:*

    enumerator UART_FLOWCTRL_DISABLE[](#_CPPv4N19uart_flow_control_t21UART_FLOWCTRL_DISABLEE "永久链接至目标")
    :   UART flow control disable

    enumerator UART_FLOWCTRL_CTS_RTS[](#_CPPv4N19uart_flow_control_t21UART_FLOWCTRL_CTS_RTSE "永久链接至目标")
    :   UART flow control cts rts

enum uart_rx_stop_detect_time_t[](#_CPPv426uart_rx_stop_detect_time_t "永久链接至目标")
:   *Values:*

    enumerator UART_RX_STOP_DETECT_TIME_32_BITS[](#_CPPv4N26uart_rx_stop_detect_time_t32UART_RX_STOP_DETECT_TIME_32_BITSE "永久链接至目标")
    :   UART rx stop time 32 bits

    enumerator UART_RX_STOP_DETECT_TIME_64_BITS[](#_CPPv4N26uart_rx_stop_detect_time_t32UART_RX_STOP_DETECT_TIME_64_BITSE "永久链接至目标")
    :   UART rx stop time 64 bits

    enumerator UART_RX_STOP_DETECT_TIME_128_BITS[](#_CPPv4N26uart_rx_stop_detect_time_t33UART_RX_STOP_DETECT_TIME_128_BITSE "永久链接至目标")
    :   UART rx stop time 128 bits

    enumerator UART_RX_STOP_DETECT_TIME_256_BITS[](#_CPPv4N26uart_rx_stop_detect_time_t33UART_RX_STOP_DETECT_TIME_256_BITSE "永久链接至目标")
    :   UART rx stop time 256 bits
