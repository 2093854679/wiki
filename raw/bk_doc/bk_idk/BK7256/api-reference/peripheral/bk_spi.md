# SPI[](#spi "永久链接至标题")

[[English]](../../../../en/v1.5/api-reference/peripheral/bk_spi.html "../../../../en/v1.5/api-reference/peripheral/bk_spi.html")


## SPI API Status[](#spi-api-status "永久链接至标题")

| API | BK7256 | BK7256_cp1 |
| --- | --- | --- |
| [`bk_spi_driver_init()`](#_CPPv418bk_spi_driver_initv "bk_spi_driver_init") | Y | Y |
| [`bk_spi_driver_deinit()`](#_CPPv420bk_spi_driver_deinitv "bk_spi_driver_deinit") | Y | Y |
| [`bk_spi_init()`](#_CPPv411bk_spi_init8spi_id_tPK12spi_config_t "bk_spi_init") | Y | Y |
| [`bk_spi_deinit()`](#_CPPv413bk_spi_deinit8spi_id_t "bk_spi_deinit") | Y | Y |
| [`bk_spi_set_mode()`](#_CPPv415bk_spi_set_mode8spi_id_t10spi_mode_t "bk_spi_set_mode") | Y | Y |
| [`bk_spi_set_bit_width()`](#_CPPv420bk_spi_set_bit_width8spi_id_t15spi_bit_width_t "bk_spi_set_bit_width") | Y | Y |
| [`bk_spi_set_wire_mode()`](#_CPPv420bk_spi_set_wire_mode8spi_id_t15spi_wire_mode_t "bk_spi_set_wire_mode") | Y | Y |
| [`bk_spi_set_baud_rate()`](#_CPPv420bk_spi_set_baud_rate8spi_id_t8uint32_t "bk_spi_set_baud_rate") | Y | Y |
| [`bk_spi_set_bit_order()`](#_CPPv420bk_spi_set_bit_order8spi_id_t15spi_bit_order_t "bk_spi_set_bit_order") | Y | Y |
| [`bk_spi_register_rx_isr()`](#_CPPv422bk_spi_register_rx_isr8spi_id_t9spi_isr_tPv "bk_spi_register_rx_isr") | Y | Y |
| [`bk_spi_register_tx_finish_isr()`](#_CPPv429bk_spi_register_tx_finish_isr8spi_id_t9spi_isr_tPv "bk_spi_register_tx_finish_isr") | Y | Y |
| [`bk_spi_write_bytes()`](#_CPPv418bk_spi_write_bytes8spi_id_tPKv8uint32_t "bk_spi_write_bytes") | Y | Y |
| [`bk_spi_read_bytes()`](#_CPPv417bk_spi_read_bytes8spi_id_tPv8uint32_t "bk_spi_read_bytes") | Y | Y |
| [`bk_spi_transmit()`](#_CPPv415bk_spi_transmit8spi_id_tPKv8uint32_tPv8uint32_t "bk_spi_transmit") | Y | Y |
| `bk_spi_dma_write_bytes()` | Y | Y |
| `bk_spi_dma_read_bytes()` | Y | Y |
| `bk_spi_dma_transmit()` | Y | Y |


## SPI UNIT Number[](#spi-unit-number "永久链接至标题")

| Capability | BK7256 | BK7256_cp1 |
| --- | --- | --- |
| UNIT Number | 3 | 3 |


## SPI Pin and GPIO Map[](#spi-pin-and-gpio-map "永久链接至标题")

| SPI Pin | BK7256 | BK7256_cp1 |
| --- | --- | --- |
| SPI0 SCK | 44 | 44 |
| SPI0 CSN | 45 | 45 |
| SPI0 MOSI | 46 | 46 |
| SPI0 MISO | 47 | 47 |
| SPI1 SCK | 2 | 2 |
| SPI1 CSN | 3 | 3 |
| SPI1 MOSI | 4 | 4 |
| SPI1 MISO | 5 | 5 |
| SPI2 SCK | 14 | 14 |
| SPI2 CSN | 15 | 15 |
| SPI2 MOSI | 16 | 16 |
| SPI2 MISO | 17 | 17 |


## SPI API Reference[](#spi-api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [spi.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/spi.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/spi.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_driver_init(void)[](#_CPPv418bk_spi_driver_initv "永久链接至目标")
:   Init the SPI driver.

    This API init the resoure common:


    - Init SPI driver control memory


    **Attention**
    :   1. This API should be called before any other SPI APIs.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_driver_deinit(void)[](#_CPPv420bk_spi_driver_deinitv "永久链接至目标")
:   Deinit the SPI driver.

    This API free all resource related to SPI and disable SPI.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_init([spi_id_t](#_CPPv48spi_id_t "spi_id_t") id, const [spi_config_t](#_CPPv412spi_config_t "spi_config_t") *config)[](#_CPPv411bk_spi_init8spi_id_tPK12spi_config_t "永久链接至目标")
:   Init the SPI id.

    This API init the SPI id:


    - Power up the SPI id

    - Configure the SPI id clock

    - Map the SPI id to dedicated GPIO port

    - Set the SPI parameters

    - Start the SPI id

    参数
    :   - **id** – SPI id

        - **config** – SPI parameter settings

    返回
    :   - BK_OK: succeed

        - BK_ERR_NULL_PARAM: SPI config paramter is NULL

        - BK_ERR_SPI_NOT_INIT: SPI driver not init

        - BK_ERR_SPI_INVALID_ID: SPI id is invalid

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_deinit([spi_id_t](#_CPPv48spi_id_t "spi_id_t") id)[](#_CPPv413bk_spi_deinit8spi_id_t "永久链接至目标")
:   Deinit the SPI id.

    This API deinit the SPI id:


    - Stop the SPI id

    - Disable the SPI id interrupt

    - Power down the SPI id

    参数
    :   **id** – SPI id

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_set_mode([spi_id_t](#_CPPv48spi_id_t "spi_id_t") id, [spi_mode_t](#_CPPv410spi_mode_t "spi_mode_t") mode)[](#_CPPv415bk_spi_set_mode8spi_id_t10spi_mode_t "永久链接至目标")
:   Set the SPI mode.

    参数
    :   - **id** – SPI id

        - **mode** – SPI mode

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_set_bit_width([spi_id_t](#_CPPv48spi_id_t "spi_id_t") id, [spi_bit_width_t](#_CPPv415spi_bit_width_t "spi_bit_width_t") bit_width)[](#_CPPv420bk_spi_set_bit_width8spi_id_t15spi_bit_width_t "永久链接至目标")
:   Set the SPI bit width.

    参数
    :   - **id** – SPI id

        - **bit_width** – SPI bit width

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_set_wire_mode([spi_id_t](#_CPPv48spi_id_t "spi_id_t") id, [spi_wire_mode_t](#_CPPv415spi_wire_mode_t "spi_wire_mode_t") wire_mode)[](#_CPPv420bk_spi_set_wire_mode8spi_id_t15spi_wire_mode_t "永久链接至目标")
:   Set the SPI wire mode.

    参数
    :   - **id** – SPI id

        - **wire_mode** – SPI wire mode

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_set_baud_rate([spi_id_t](#_CPPv48spi_id_t "spi_id_t") id, uint32_t baud_rate)[](#_CPPv420bk_spi_set_baud_rate8spi_id_t8uint32_t "永久链接至目标")
:   Set the SPI baud rate.

    参数
    :   - **id** – SPI id

        - **baud_rate** – SPI baud rate

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_set_bit_order([spi_id_t](#_CPPv48spi_id_t "spi_id_t") id, [spi_bit_order_t](#_CPPv415spi_bit_order_t "spi_bit_order_t") bit_order)[](#_CPPv420bk_spi_set_bit_order8spi_id_t15spi_bit_order_t "永久链接至目标")
:   Set the SPI bit order.

    参数
    :   - **id** – SPI id

        - **bit_order** – SPI bit order

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_register_rx_isr([spi_id_t](#_CPPv48spi_id_t "spi_id_t") id, [spi_isr_t](#_CPPv49spi_isr_t "spi_isr_t") isr, void *param)[](#_CPPv422bk_spi_register_rx_isr8spi_id_t9spi_isr_tPv "永久链接至目标")
:   Register the RX interrupt service routine for SPI id.

    参数
    :   - **id** – spi id

        - **isr** – SPI RX callback

        - **param** – SPI RX callback parameter

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_register_tx_finish_isr([spi_id_t](#_CPPv48spi_id_t "spi_id_t") id, [spi_isr_t](#_CPPv49spi_isr_t "spi_isr_t") isr, void *param)[](#_CPPv429bk_spi_register_tx_finish_isr8spi_id_t9spi_isr_tPv "永久链接至目标")
:   Register the TX finish interrupt service routine for SPI id.

    参数
    :   - **id** – SPi id

        - **isr** – SPI TX finish callback

        - **param** – SPi TX callback parameter

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_write_bytes([spi_id_t](#_CPPv48spi_id_t "spi_id_t") id, const void *data, uint32_t size)[](#_CPPv418bk_spi_write_bytes8spi_id_tPKv8uint32_t "永久链接至目标")
:   Send data to the SPI port from a given buffer and length.

    参数
    :   - **id** – spi id

        - **data** – data buffer address

        - **size** – data length to send

    返回
    :   - BK_OK: succeed

        - BK_ERR_SPI_NOT_INIT: SPI driver not init

        - BK_ERR_SPI_INVALID_ID: SPI id number is invalid

        - BK_ERR_SPI_ID_NOT_INIT: SPI id not init

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_read_bytes([spi_id_t](#_CPPv48spi_id_t "spi_id_t") id, void *data, uint32_t size)[](#_CPPv417bk_spi_read_bytes8spi_id_tPv8uint32_t "永久链接至目标")
:   SPI read bytes from SPI buffer.

    参数
    :   - **id** – SPI id

        - **data** – pointer to the buffer

        - **size** – data length to read

    返回
    :   - BK_OK: succeed

        - BK_ERR_SPI_NOT_INIT: SPI driver not init

        - BK_ERR_SPI_INVALID_ID: SPI id number is invalid

        - BK_ERR_SPI_ID_NOT_INIT: SPI id not init

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_transmit([spi_id_t](#_CPPv48spi_id_t "spi_id_t") id, const void *tx_data, uint32_t tx_size, void *rx_data, uint32_t rx_size)[](#_CPPv415bk_spi_transmit8spi_id_tPKv8uint32_tPv8uint32_t "永久链接至目标")
:   SPI write and read bytes.

    参数
    :   - **id** – SPI id

        - **tx_data** – write data buffer address

        - **tx_size** – data length to read

        - **rx_data** – pointer to the receive buffer

        - **rx_size** – data length to read

        - **timeout_ms** – timeout ms, if set BEKEN_WAIT_FOREVER, read will wait forever

    返回
    :   - BK_OK: succeed

        - BK_ERR_SPI_NOT_INIT: SPI driver not init

        - BK_ERR_SPI_INVALID_ID: SPI id number is invalid

        - BK_ERR_SPI_ID_NOT_INIT: SPI id not init

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_register_rx_finish_isr([spi_id_t](#_CPPv48spi_id_t "spi_id_t") id, [spi_isr_t](#_CPPv49spi_isr_t "spi_isr_t") isr, void *param)[](#_CPPv429bk_spi_register_rx_finish_isr8spi_id_t9spi_isr_tPv "永久链接至目标")
:   Register the RX finish interrupt service routine for SPI id.

    参数
    :   - **id** – spi id

        - **isr** – SPI RX callback

        - **param** – SPI RX callback parameter

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_unregister_rx_isr([spi_id_t](#_CPPv48spi_id_t "spi_id_t") id)[](#_CPPv424bk_spi_unregister_rx_isr8spi_id_t "永久链接至目标")
:   Unregister the RX interrupt service routine for SPI id.

    参数
    :   **id** – spi id

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_unregister_rx_finish_isr([spi_id_t](#_CPPv48spi_id_t "spi_id_t") id)[](#_CPPv431bk_spi_unregister_rx_finish_isr8spi_id_t "永久链接至目标")
:   Unregister the RX finish interrupt service routine for SPI id.

    参数
    :   **id** – spi id

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_unregister_tx_finish_isr([spi_id_t](#_CPPv48spi_id_t "spi_id_t") id)[](#_CPPv431bk_spi_unregister_tx_finish_isr8spi_id_t "永久链接至目标")
:   Unregister the TX finish interrupt service routine for SPI id.

    参数
    :   **id** – spi id

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_write_bytes_async([spi_id_t](#_CPPv48spi_id_t "spi_id_t") id, const void *data, uint32_t size)[](#_CPPv424bk_spi_write_bytes_async8spi_id_tPKv8uint32_t "永久链接至目标")
:   Send data to the SPI port from a given buffer and length in async mode.

    参数
    :   - **id** – spi id

        - **data** – data buffer address

        - **size** – data length to send

    返回
    :   - BK_OK: succeed

        - BK_ERR_SPI_NOT_INIT: SPI driver not init

        - BK_ERR_SPI_INVALID_ID: SPI id number is invalid

        - BK_ERR_SPI_ID_NOT_INIT: SPI id not init

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_spi_read_bytes_async([spi_id_t](#_CPPv48spi_id_t "spi_id_t") id, void *data, uint32_t size)[](#_CPPv423bk_spi_read_bytes_async8spi_id_tPv8uint32_t "永久链接至目标")
:   SPI read bytes from SPI buffer in async mode.

    参数
    :   - **id** – SPI id

        - **data** – pointer to the buffer

        - **size** – data length to read

    返回
    :   - BK_OK: succeed

        - BK_ERR_SPI_NOT_INIT: SPI driver not init

        - BK_ERR_SPI_INVALID_ID: SPI id number is invalid

        - BK_ERR_SPI_ID_NOT_INIT: SPI id not init

        - others: other errors.


## SPI API Typedefs[](#spi-api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [spi_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/spi_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/spi_types.h")


### Structures[](#structures "永久链接至标题")

struct spi_int_config_t[](#_CPPv416spi_int_config_t "永久链接至目标")
:   Public Members

    [spi_id_t](#_CPPv48spi_id_t "spi_id_t") id[](#_CPPv4N16spi_int_config_t2idE "永久链接至目标")
    :   SPI id

    [icu_int_src_t](bk_interrupt.html#_CPPv413icu_int_src_t "icu_int_src_t") int_src[](#_CPPv4N16spi_int_config_t7int_srcE "永久链接至目标")
    :   int source

    int_group_isr_t isr[](#_CPPv4N16spi_int_config_t3isrE "永久链接至目标")
    :   isr function

    [dma_dev_t](bk_dma.html#_CPPv49dma_dev_t "dma_dev_t") dma_dev[](#_CPPv4N16spi_int_config_t7dma_devE "永久链接至目标")
    :   dma device


### Type Definitions[](#type-definitions "永久链接至标题")

typedef void (*spi_isr_t)([spi_id_t](#_CPPv48spi_id_t "spi_id_t") id, void *param)[](#_CPPv49spi_isr_t "永久链接至目标")
:   SPI interrupt service routine


### Header File[](#id2 "永久链接至标题")


- [hal/hal_spi_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hal/hal_spi_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hal/hal_spi_types.h")


### Structures[](#id3 "永久链接至标题")

struct spi_config_t[](#_CPPv412spi_config_t "永久链接至目标")
:   Public Members

    [spi_role_t](#_CPPv410spi_role_t "spi_role_t") role[](#_CPPv4N12spi_config_t4roleE "永久链接至目标")
    :   SPI as master or slave

    [spi_bit_width_t](#_CPPv415spi_bit_width_t "spi_bit_width_t") bit_width[](#_CPPv4N12spi_config_t9bit_widthE "永久链接至目标")
    :   SPI data bit witdth

    [spi_polarity_t](#_CPPv414spi_polarity_t "spi_polarity_t") polarity[](#_CPPv4N12spi_config_t8polarityE "永久链接至目标")
    :   SPI clock polarity

    [spi_phase_t](#_CPPv411spi_phase_t "spi_phase_t") phase[](#_CPPv4N12spi_config_t5phaseE "永久链接至目标")
    :   SPI clock phase

    [spi_wire_mode_t](#_CPPv415spi_wire_mode_t "spi_wire_mode_t") wire_mode[](#_CPPv4N12spi_config_t9wire_modeE "永久链接至目标")
    :   SPI wire mode

    uint32_t baud_rate[](#_CPPv4N12spi_config_t9baud_rateE "永久链接至目标")
    :   SPI transmit and receive SCK clock

    [spi_bit_order_t](#_CPPv415spi_bit_order_t "spi_bit_order_t") bit_order[](#_CPPv4N12spi_config_t9bit_orderE "永久链接至目标")
    :   SPI bit order, MSB/LSB


### Macros[](#macros "永久链接至标题")

BK_ERR_SPI_NOT_INIT[](#c.BK_ERR_SPI_NOT_INIT "永久链接至目标")
:   SPI driver not init

BK_ERR_SPI_INVALID_ID[](#c.BK_ERR_SPI_INVALID_ID "永久链接至目标")
:   SPI id number is invalid

BK_ERR_SPI_ID_NOT_INIT[](#c.BK_ERR_SPI_ID_NOT_INIT "永久链接至目标")
:   SPI ID not init

BK_ERR_SPI_RX_TIMEOUT[](#c.BK_ERR_SPI_RX_TIMEOUT "永久链接至目标")
:   SPI receive data timeout

BK_ERR_SPI_TX_TIMEOUT[](#c.BK_ERR_SPI_TX_TIMEOUT "永久链接至目标")
:   SPI send data timeout

BK_ERR_SPI_FIFO_WR_NOT_READY[](#c.BK_ERR_SPI_FIFO_WR_NOT_READY "永久链接至目标")
:   SPI tx fifo write not ready

BK_ERR_SPI_FIFO_RD_NOT_READY[](#c.BK_ERR_SPI_FIFO_RD_NOT_READY "永久链接至目标")
:   SPI rx fifo read not ready

BK_ERR_SPI_DUPLEX_SIZE_NOT_EQUAL[](#c.BK_ERR_SPI_DUPLEX_SIZE_NOT_EQUAL "永久链接至目标")
:   SPI duplex tx rx size not equal


### Type Definitions[](#id4 "永久链接至标题")

typedef uint8_t spi_unit_t[](#_CPPv410spi_unit_t "永久链接至目标")
:   spi uint id


### Enumerations[](#enumerations "永久链接至标题")

enum spi_id_t[](#_CPPv48spi_id_t "永久链接至目标")
:   *Values:*

    enumerator SPI_ID_0[](#_CPPv4N8spi_id_t8SPI_ID_0E "永久链接至目标")
    :   SPI id 1

    enumerator SPI_ID_MAX[](#_CPPv4N8spi_id_t10SPI_ID_MAXE "永久链接至目标")
    :   SPI id max

enum spi_role_t[](#_CPPv410spi_role_t "永久链接至目标")
:   *Values:*

    enumerator SPI_ROLE_SLAVE[](#_CPPv4N10spi_role_t14SPI_ROLE_SLAVEE "永久链接至目标")
    :   SPI as slave

    enumerator SPI_ROLE_MASTER[](#_CPPv4N10spi_role_t15SPI_ROLE_MASTERE "永久链接至目标")
    :   SPI as master

enum spi_bit_width_t[](#_CPPv415spi_bit_width_t "永久链接至目标")
:   *Values:*

    enumerator SPI_BIT_WIDTH_8BITS[](#_CPPv4N15spi_bit_width_t19SPI_BIT_WIDTH_8BITSE "永久链接至目标")
    :   SPI bit width 8bits

    enumerator SPI_BIT_WIDTH_16BITS[](#_CPPv4N15spi_bit_width_t20SPI_BIT_WIDTH_16BITSE "永久链接至目标")
    :   SPI bit width 16bits

enum spi_polarity_t[](#_CPPv414spi_polarity_t "永久链接至目标")
:   *Values:*

    enumerator SPI_POLARITY_LOW[](#_CPPv4N14spi_polarity_t16SPI_POLARITY_LOWE "永久链接至目标")
    :   SPI clock polarity low

    enumerator SPI_POLARITY_HIGH[](#_CPPv4N14spi_polarity_t17SPI_POLARITY_HIGHE "永久链接至目标")
    :   SPI clock polarity high

enum spi_phase_t[](#_CPPv411spi_phase_t "永久链接至目标")
:   *Values:*

    enumerator SPI_PHASE_1ST_EDGE[](#_CPPv4N11spi_phase_t18SPI_PHASE_1ST_EDGEE "永久链接至目标")
    :   SPI clock phase the first edge

    enumerator SPI_PHASE_2ND_EDGE[](#_CPPv4N11spi_phase_t18SPI_PHASE_2ND_EDGEE "永久链接至目标")
    :   SPI clock phase the second edge

enum spi_mode_t[](#_CPPv410spi_mode_t "永久链接至目标")
:   *Values:*

    enumerator SPI_POL_MODE_0[](#_CPPv4N10spi_mode_t14SPI_POL_MODE_0E "永久链接至目标")
    :   SPI mode 0

    enumerator SPI_POL_MODE_1[](#_CPPv4N10spi_mode_t14SPI_POL_MODE_1E "永久链接至目标")
    :   SPI mode 1

    enumerator SPI_POL_MODE_2[](#_CPPv4N10spi_mode_t14SPI_POL_MODE_2E "永久链接至目标")
    :   SPI mode 2

    enumerator SPI_POL_MODE_3[](#_CPPv4N10spi_mode_t14SPI_POL_MODE_3E "永久链接至目标")
    :   SPI mode 3

enum spi_wire_mode_t[](#_CPPv415spi_wire_mode_t "永久链接至目标")
:   *Values:*

    enumerator SPI_4WIRE_MODE[](#_CPPv4N15spi_wire_mode_t14SPI_4WIRE_MODEE "永久链接至目标")
    :   SPI four wire mode

    enumerator SPI_3WIRE_MODE[](#_CPPv4N15spi_wire_mode_t14SPI_3WIRE_MODEE "永久链接至目标")
    :   SPI three wire mode

enum spi_bit_order_t[](#_CPPv415spi_bit_order_t "永久链接至目标")
:   *Values:*

    enumerator SPI_MSB_FIRST[](#_CPPv4N15spi_bit_order_t13SPI_MSB_FIRSTE "永久链接至目标")
    :   SPI MSB first

    enumerator SPI_LSB_FIRST[](#_CPPv4N15spi_bit_order_t13SPI_LSB_FIRSTE "永久链接至目标")
    :   SPI LSB first

enum spi_fifo_int_level[](#_CPPv418spi_fifo_int_level "永久链接至目标")
:   *Values:*

    enumerator SPI_FIFO_INT_LEVEL_1[](#_CPPv4N18spi_fifo_int_level20SPI_FIFO_INT_LEVEL_1E "永久链接至目标")
    :   SPI fifo int level 1

    enumerator SPI_FIFO_INT_LEVEL_16[](#_CPPv4N18spi_fifo_int_level21SPI_FIFO_INT_LEVEL_16E "永久链接至目标")
    :   SPI fifo int level 16

    enumerator SPI_FIFO_INT_LEVEL_32[](#_CPPv4N18spi_fifo_int_level21SPI_FIFO_INT_LEVEL_32E "永久链接至目标")
    :   SPI fifo int level 32

    enumerator SPI_FIFO_INT_LEVEL_48[](#_CPPv4N18spi_fifo_int_level21SPI_FIFO_INT_LEVEL_48E "永久链接至目标")
    :   SPI fifo int level 48

enum spi_src_clk_t[](#_CPPv413spi_src_clk_t "永久链接至目标")
:   *Values:*

    enumerator SPI_CLK_XTAL[](#_CPPv4N13spi_src_clk_t12SPI_CLK_XTALE "永久链接至目标")

    enumerator SPI_CLK_APLL[](#_CPPv4N13spi_src_clk_t12SPI_CLK_APLLE "永久链接至目标")

    enumerator SPI_CLK_UNKNOW[](#_CPPv4N13spi_src_clk_t14SPI_CLK_UNKNOWE "永久链接至目标")
