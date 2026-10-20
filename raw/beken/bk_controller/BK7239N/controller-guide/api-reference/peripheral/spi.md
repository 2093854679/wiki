---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/api-reference/peripheral/spi.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="spi-api"></a>

# SPI API

SPI (Serial Peripheral Interface) 串行外设接口API接口。

<a id="header-file"></a>

## Header File

- [spi.h](https://github.com/bekencorp/armino/blob/main/components/spi.h)

<a id="functions"></a>

## Functions

<a id="_CPPv418bk_spi_driver_initv"></a>

<a id="_CPPv318bk_spi_driver_initv"></a> <a id="_CPPv218bk_spi_driver_initv"></a> <a id="bk_spi_driver_init__void"></a> <a id="spi_8h_1aad9a9d4f974fa3cbc151d753a36bf944"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_driver\_init(void)
:   Init the SPI driver.

    This API init the resoure common:

    - Init SPI driver control memory

    **Attention**
    :   1\. This API should be called before any other SPI APIs.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_spi_driver_deinitv"></a>

<a id="_CPPv320bk_spi_driver_deinitv"></a> <a id="_CPPv220bk_spi_driver_deinitv"></a> <a id="bk_spi_driver_deinit__void"></a> <a id="spi_8h_1a67161f339fa790324b07af5c3b3d3abb"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_driver\_deinit(void)
:   Deinit the SPI driver.

    This API free all resource related to SPI and disable SPI.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv411bk_spi_init8spi_id_tPK12spi_config_t"></a>

<a id="_CPPv311bk_spi_init8spi_id_tPK12spi_config_t"></a> <a id="_CPPv211bk_spi_init8spi_id_tPK12spi_config_t"></a> <a id="bk_spi_init__spi_id_t.spi_config_tCP"></a> <a id="spi_8h_1a15e4e8c43d7a750b9fc092443fc1f8c2"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_init(spi\_id\_t id, const spi\_config\_t \*config)
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
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: SPI config paramter is NULL
        - BK\_ERR\_SPI\_NOT\_INIT: SPI driver not init
        - BK\_ERR\_SPI\_INVALID\_ID: SPI id is invalid
        - others: other errors.

<a id="_CPPv413bk_spi_deinit8spi_id_t"></a>

<a id="_CPPv313bk_spi_deinit8spi_id_t"></a> <a id="_CPPv213bk_spi_deinit8spi_id_t"></a> <a id="bk_spi_deinit__spi_id_t"></a> <a id="spi_8h_1a96f60bcf20308e16506aa164a1ec292b"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_deinit(spi\_id\_t id)
:   Deinit the SPI id.

    This API deinit the SPI id:

    - Stop the SPI id
    - Disable the SPI id interrupt
    - Power down the SPI id

    参数
    :   **id** – SPI id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv415bk_spi_set_mode8spi_id_t10spi_mode_t"></a>

<a id="_CPPv315bk_spi_set_mode8spi_id_t10spi_mode_t"></a> <a id="_CPPv215bk_spi_set_mode8spi_id_t10spi_mode_t"></a> <a id="bk_spi_set_mode__spi_id_t.spi_mode_t"></a> <a id="spi_8h_1a021d0b93196974058152ef5e7903dfa6"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_set\_mode(spi\_id\_t id, spi\_mode\_t mode)
:   Set the SPI mode.

    参数
    :   - **id** – SPI id
        - **mode** – SPI mode

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_spi_set_bit_width8spi_id_t15spi_bit_width_t"></a>

<a id="_CPPv320bk_spi_set_bit_width8spi_id_t15spi_bit_width_t"></a> <a id="_CPPv220bk_spi_set_bit_width8spi_id_t15spi_bit_width_t"></a> <a id="bk_spi_set_bit_width__spi_id_t.spi_bit_width_t"></a> <a id="spi_8h_1ae69150917075354cb9322704454b9776"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_set\_bit\_width(spi\_id\_t id, spi\_bit\_width\_t bit\_width)
:   Set the SPI bit width.

    参数
    :   - **id** – SPI id
        - **bit\_width** – SPI bit width

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_spi_set_wire_mode8spi_id_t15spi_wire_mode_t"></a>

<a id="_CPPv320bk_spi_set_wire_mode8spi_id_t15spi_wire_mode_t"></a> <a id="_CPPv220bk_spi_set_wire_mode8spi_id_t15spi_wire_mode_t"></a> <a id="bk_spi_set_wire_mode__spi_id_t.spi_wire_mode_t"></a> <a id="spi_8h_1a5e341b3b8a32bd848cd4aa0cf5e7e32b"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_set\_wire\_mode(spi\_id\_t id, spi\_wire\_mode\_t wire\_mode)
:   Set the SPI wire mode.

    参数
    :   - **id** – SPI id
        - **wire\_mode** – SPI wire mode

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_spi_set_baud_rate8spi_id_t8uint32_t"></a>

<a id="_CPPv320bk_spi_set_baud_rate8spi_id_t8uint32_t"></a> <a id="_CPPv220bk_spi_set_baud_rate8spi_id_t8uint32_t"></a> <a id="bk_spi_set_baud_rate__spi_id_t.uint32_t"></a> <a id="spi_8h_1a52b2528e02599fc4d60739b1f182c7c3"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_set\_baud\_rate(spi\_id\_t id, uint32\_t baud\_rate)
:   Set the SPI baud rate.

    参数
    :   - **id** – SPI id
        - **baud\_rate** – SPI baud rate

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_spi_set_bit_order8spi_id_t15spi_bit_order_t"></a>

<a id="_CPPv320bk_spi_set_bit_order8spi_id_t15spi_bit_order_t"></a> <a id="_CPPv220bk_spi_set_bit_order8spi_id_t15spi_bit_order_t"></a> <a id="bk_spi_set_bit_order__spi_id_t.spi_bit_order_t"></a> <a id="spi_8h_1a5bc86c748258f55346b29da30911cfa0"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_set\_bit\_order(spi\_id\_t id, spi\_bit\_order\_t bit\_order)
:   Set the SPI bit order.

    参数
    :   - **id** – SPI id
        - **bit\_order** – SPI bit order

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv422bk_spi_register_rx_isr8spi_id_t9spi_isr_tPv"></a>

<a id="_CPPv322bk_spi_register_rx_isr8spi_id_t9spi_isr_tPv"></a> <a id="_CPPv222bk_spi_register_rx_isr8spi_id_t9spi_isr_tPv"></a> <a id="bk_spi_register_rx_isr__spi_id_t.spi_isr_t.voidP"></a> <a id="spi_8h_1a2d6ebb7fc822810d52250fc02a5ebb15"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_register\_rx\_isr(spi\_id\_t id, spi\_isr\_t isr, void \*param)
:   Register the RX interrupt service routine for SPI id.

    参数
    :   - **id** – spi id
        - **isr** – SPI RX callback
        - **param** – SPI RX callback parameter

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv429bk_spi_register_tx_finish_isr8spi_id_t9spi_isr_tPv"></a>

<a id="_CPPv329bk_spi_register_tx_finish_isr8spi_id_t9spi_isr_tPv"></a> <a id="_CPPv229bk_spi_register_tx_finish_isr8spi_id_t9spi_isr_tPv"></a> <a id="bk_spi_register_tx_finish_isr__spi_id_t.spi_isr_t.voidP"></a> <a id="spi_8h_1ac400893791227c0a66ab1539e63117ca"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_register\_tx\_finish\_isr(spi\_id\_t id, spi\_isr\_t isr, void \*param)
:   Register the TX finish interrupt service routine for SPI id.

    参数
    :   - **id** – SPi id
        - **isr** – SPI TX finish callback
        - **param** – SPi TX callback parameter

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv418bk_spi_write_bytes8spi_id_tPKv8uint32_t"></a>

<a id="_CPPv318bk_spi_write_bytes8spi_id_tPKv8uint32_t"></a> <a id="_CPPv218bk_spi_write_bytes8spi_id_tPKv8uint32_t"></a> <a id="bk_spi_write_bytes__spi_id_t.voidCP.uint32_t"></a> <a id="spi_8h_1a2a3305509c196126c835e783da00da13"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_write\_bytes(spi\_id\_t id, const void \*data, uint32\_t size)
:   Send data to the SPI port from a given buffer and length.

    参数
    :   - **id** – spi id
        - **data** – data buffer address
        - **size** – data length to send

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_SPI\_NOT\_INIT: SPI driver not init
        - BK\_ERR\_SPI\_INVALID\_ID: SPI id number is invalid
        - BK\_ERR\_SPI\_ID\_NOT\_INIT: SPI id not init
        - others: other errors.

<a id="_CPPv417bk_spi_read_bytes8spi_id_tPv8uint32_t"></a>

<a id="_CPPv317bk_spi_read_bytes8spi_id_tPv8uint32_t"></a> <a id="_CPPv217bk_spi_read_bytes8spi_id_tPv8uint32_t"></a> <a id="bk_spi_read_bytes__spi_id_t.voidP.uint32_t"></a> <a id="spi_8h_1a9bf07de51a574ac446771552f811f617"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_read\_bytes(spi\_id\_t id, void \*data, uint32\_t size)
:   SPI read bytes from SPI buffer.

    参数
    :   - **id** – SPI id
        - **data** – pointer to the buffer
        - **size** – data length to read

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_SPI\_NOT\_INIT: SPI driver not init
        - BK\_ERR\_SPI\_INVALID\_ID: SPI id number is invalid
        - BK\_ERR\_SPI\_ID\_NOT\_INIT: SPI id not init
        - others: other errors.

<a id="_CPPv415bk_spi_transmit8spi_id_tPKv8uint32_tPv8uint32_t"></a>

<a id="_CPPv315bk_spi_transmit8spi_id_tPKv8uint32_tPv8uint32_t"></a> <a id="_CPPv215bk_spi_transmit8spi_id_tPKv8uint32_tPv8uint32_t"></a> <a id="bk_spi_transmit__spi_id_t.voidCP.uint32_t.voidP.uint32_t"></a> <a id="spi_8h_1adc27a162d9465944b68cbdd290bba12a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_transmit(spi\_id\_t id, const void \*tx\_data, uint32\_t tx\_size, void \*rx\_data, uint32\_t rx\_size)
:   SPI write and read bytes.

    参数
    :   - **id** – SPI id
        - **tx\_data** – write data buffer address
        - **tx\_size** – data length to read
        - **rx\_data** – pointer to the receive buffer
        - **rx\_size** – data length to read
        - **timeout\_ms** – timeout ms, if set BEKEN\_WAIT\_FOREVER, read will wait forever

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_SPI\_NOT\_INIT: SPI driver not init
        - BK\_ERR\_SPI\_INVALID\_ID: SPI id number is invalid
        - BK\_ERR\_SPI\_ID\_NOT\_INIT: SPI id not init
        - others: other errors.

<a id="_CPPv429bk_spi_register_rx_finish_isr8spi_id_t9spi_isr_tPv"></a>

<a id="_CPPv329bk_spi_register_rx_finish_isr8spi_id_t9spi_isr_tPv"></a> <a id="_CPPv229bk_spi_register_rx_finish_isr8spi_id_t9spi_isr_tPv"></a> <a id="bk_spi_register_rx_finish_isr__spi_id_t.spi_isr_t.voidP"></a> <a id="spi_8h_1a089e304f198c8a694909be1212c8e6cd"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_register\_rx\_finish\_isr(spi\_id\_t id, spi\_isr\_t isr, void \*param)
:   Register the RX finish interrupt service routine for SPI id.

    参数
    :   - **id** – spi id
        - **isr** – SPI RX callback
        - **param** – SPI RX callback parameter

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_spi_unregister_rx_isr8spi_id_t"></a>

<a id="_CPPv324bk_spi_unregister_rx_isr8spi_id_t"></a> <a id="_CPPv224bk_spi_unregister_rx_isr8spi_id_t"></a> <a id="bk_spi_unregister_rx_isr__spi_id_t"></a> <a id="spi_8h_1aa99792f0ad7b80ca1ed797e96c5d0e2b"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_unregister\_rx\_isr(spi\_id\_t id)
:   Unregister the RX interrupt service routine for SPI id.

    参数
    :   **id** – spi id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv431bk_spi_unregister_rx_finish_isr8spi_id_t"></a>

<a id="_CPPv331bk_spi_unregister_rx_finish_isr8spi_id_t"></a> <a id="_CPPv231bk_spi_unregister_rx_finish_isr8spi_id_t"></a> <a id="bk_spi_unregister_rx_finish_isr__spi_id_t"></a> <a id="spi_8h_1a66ff6c686208061a5e2f2a740e69f3f7"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_unregister\_rx\_finish\_isr(spi\_id\_t id)
:   Unregister the RX finish interrupt service routine for SPI id.

    参数
    :   **id** – spi id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv431bk_spi_unregister_tx_finish_isr8spi_id_t"></a>

<a id="_CPPv331bk_spi_unregister_tx_finish_isr8spi_id_t"></a> <a id="_CPPv231bk_spi_unregister_tx_finish_isr8spi_id_t"></a> <a id="bk_spi_unregister_tx_finish_isr__spi_id_t"></a> <a id="spi_8h_1ae9e27ca8feedea37bfb07998ec8033f5"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_unregister\_tx\_finish\_isr(spi\_id\_t id)
:   Unregister the TX finish interrupt service routine for SPI id.

    参数
    :   **id** – spi id

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_spi_write_bytes_async8spi_id_tPKv8uint32_t"></a>

<a id="_CPPv324bk_spi_write_bytes_async8spi_id_tPKv8uint32_t"></a> <a id="_CPPv224bk_spi_write_bytes_async8spi_id_tPKv8uint32_t"></a> <a id="bk_spi_write_bytes_async__spi_id_t.voidCP.uint32_t"></a> <a id="spi_8h_1a9b8323f2507542d3c683494d21cdccb6"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_write\_bytes\_async(spi\_id\_t id, const void \*data, uint32\_t size)
:   Send data to the SPI port from a given buffer and length in async mode.

    参数
    :   - **id** – spi id
        - **data** – data buffer address
        - **size** – data length to send

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_SPI\_NOT\_INIT: SPI driver not init
        - BK\_ERR\_SPI\_INVALID\_ID: SPI id number is invalid
        - BK\_ERR\_SPI\_ID\_NOT\_INIT: SPI id not init
        - others: other errors.

<a id="_CPPv423bk_spi_read_bytes_async8spi_id_tPv8uint32_t"></a>

<a id="_CPPv323bk_spi_read_bytes_async8spi_id_tPv8uint32_t"></a> <a id="_CPPv223bk_spi_read_bytes_async8spi_id_tPv8uint32_t"></a> <a id="bk_spi_read_bytes_async__spi_id_t.voidP.uint32_t"></a> <a id="spi_8h_1affaf6dc6b2e8d571f6d4682c8295afbd"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spi\_read\_bytes\_async(spi\_id\_t id, void \*data, uint32\_t size)
:   SPI read bytes from SPI buffer in async mode.

    参数
    :   - **id** – SPI id
        - **data** – pointer to the buffer
        - **size** – data length to read

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_SPI\_NOT\_INIT: SPI driver not init
        - BK\_ERR\_SPI\_INVALID\_ID: SPI id number is invalid
        - BK\_ERR\_SPI\_ID\_NOT\_INIT: SPI id not init
        - others: other errors.
