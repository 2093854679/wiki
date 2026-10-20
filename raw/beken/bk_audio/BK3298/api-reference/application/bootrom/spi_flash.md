---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/bootrom/spi_flash.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="spi-flash"></a>

# SPI Flash

<a id="spi-flash-api-brief"></a>

## SPI\_Flash API Brief

| Application | Brief |
| --- | --- |
| [`spi_flash_init()`](#_CPPv414spi_flash_init8uint32_t "spi_flash_init") | Initialize the SPI flash function |
| [`spi_flash_deinit()`](#_CPPv416spi_flash_deinit8uint32_t "spi_flash_deinit") | De-initialize the SPI flash function |
| [`spi_flash_drv_tx()`](#_CPPv416spi_flash_drv_tx8uint32_tP7uint8_t8uint32_t "spi_flash_drv_tx") | Only spi tx |
| [`spi_flash_drv_trx()`](#_CPPv417spi_flash_drv_trx8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t "spi_flash_drv_trx") | tx and rx flash data |
| [`spi_flash_write_enable()`](#_CPPv422spi_flash_write_enable8uint32_tb "spi_flash_write_enable") | Write enable/disable |
| [`spi_flash_erase_sector()`](#_CPPv422spi_flash_erase_sector8uint32_t8uint32_t "spi_flash_erase_sector") | Erase flash a sector |
| [`spi_flash_erase()`](#_CPPv415spi_flash_erase8uint32_t8uint32_t7uint8_t "spi_flash_erase") | Erase flash with user command |
| [`spi_flash_erase_chip()`](#_CPPv420spi_flash_erase_chip8uint32_t8uint32_t "spi_flash_erase_chip") | Erase the whole flash |
| [`spi_flash_write()`](#_CPPv415spi_flash_write8uint32_t8uint32_tP7uint8_t8uint32_t "spi_flash_write") | Write data to flash |
| [`spi_flash_read()`](#_CPPv414spi_flash_read8uint32_t8uint32_tP7uint8_t8uint32_t "spi_flash_read") | Read data from flash |
| [`spi_flash_4K_read()`](#_CPPv417spi_flash_4K_read8uint32_t8uint32_tP7uint8_t8uint32_t "spi_flash_4K_read") | Read SPI flash data less than 4K bytess |
| [`spi_flash_calc_crc()`](#_CPPv418spi_flash_calc_crc8uint32_t8uint32_tP7uint8_t8uint32_t "spi_flash_calc_crc") | Calculate crc value from flash data |
| [`spi_flash_get_boot_timeout()`](#_CPPv426spi_flash_get_boot_timeout8uint32_t "spi_flash_get_boot_timeout") | Get boot timeout from flash |
| [`spi_flash_wait_op_done()`](#_CPPv422spi_flash_wait_op_done8uint32_t8uint32_t "spi_flash_wait_op_done") | Wait spi flash process done |

<a id="spi-flash-api-reference"></a>

## SPI\_Flash API Reference

<a id="header-file"></a>

### Header File

- [bootrom/spi\_flash.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/bootrom/spi_flash.h)

<a id="functions"></a>

### Functions

<a id="_CPPv414spi_flash_init8uint32_t"></a>

<a id="_CPPv314spi_flash_init8uint32_t"></a> <a id="_CPPv214spi_flash_init8uint32_t"></a> <a id="spi_flash_init__uint32_t"></a> <a id="spi__flash_8h_1a570a413f28d27c72a2394d2eff82893b"></a> int32\_t spi\_flash\_init(uint32\_t spi\_dev\_inst)
:   Initialize the SPI flash function.

    Register DMA callback functions for SPI flash tx and rx.

    参数:
    :   **spi\_dev\_inst** – **\[in\]** spi device instance, return value of [drv\_spi\_init()](../../driver/drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416spi_flash_deinit8uint32_t"></a>

<a id="_CPPv316spi_flash_deinit8uint32_t"></a> <a id="_CPPv216spi_flash_deinit8uint32_t"></a> <a id="spi_flash_deinit__uint32_t"></a> <a id="spi__flash_8h_1aff2925b4d40e0948ac284f12cc43750f"></a> int32\_t spi\_flash\_deinit(uint32\_t spi\_dev\_inst)
:   De-initialize the SPI flash function.

    Release DMA callback functions for SPI flash tx and rx.

    参数:
    :   **spi\_dev\_inst** – **\[in\]** spi device instance, return value of [drv\_spi\_init()](../../driver/drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416spi_flash_drv_tx8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv316spi_flash_drv_tx8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv216spi_flash_drv_tx8uint32_tP7uint8_t8uint32_t"></a> <a id="spi_flash_drv_tx__uint32_t.uint8_tP.uint32_t"></a> <a id="spi__flash_8h_1a007b668821dc16a34975fa8c0187faf3"></a> int32\_t spi\_flash\_drv\_tx(uint32\_t spi\_dev\_inst, uint8\_t \*pu1\_buf, uint32\_t size)
:   Only spi tx.

    Only tx flash data goes out.

    参数:
    :   - **spi\_dev\_inst** – **\[in\]** spi device instance, return value of [drv\_spi\_init()](../../driver/drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_buf** – **\[in\]** pointer to the tx buffer
        - **size** – **\[in\]** tx buffer size

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv417spi_flash_drv_trx8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv317spi_flash_drv_trx8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv217spi_flash_drv_trx8uint32_tP7uint8_t8uint32_tP7uint8_t8uint32_t"></a> <a id="spi_flash_drv_trx__uint32_t.uint8_tP.uint32_t.uint8_tP.uint32_t"></a> <a id="spi__flash_8h_1a6820981d8ae544037940615a7d4d1a91"></a> int32\_t spi\_flash\_drv\_trx(uint32\_t spi\_dev\_inst, uint8\_t \*pu1\_tx\_buf, uint32\_t tx\_size, uint8\_t \*pu1\_rx\_buf, uint32\_t rx\_size)
:   tx and rx flash data.

    tx while rx flash data, pu1\_rx\_buf points to receive buffer, content does not need to be offset

    参数:
    :   - **spi\_dev\_inst** – **\[in\]** spi device instance, return value of [drv\_spi\_init()](../../driver/drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **pu1\_tx\_buf** – **\[in\]** pointer to the tx buffer
        - **tx\_size** – **\[in\]** tx buffer size in bytes
        - **pu1\_rx\_buf** – **\[in\]** pointer to the rx buffer
        - **rx\_size** – **\[in\]** rx buffer size in bytes

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422spi_flash_write_enable8uint32_tb"></a>

<a id="_CPPv322spi_flash_write_enable8uint32_tb"></a> <a id="_CPPv222spi_flash_write_enable8uint32_tb"></a> <a id="spi_flash_write_enable__uint32_t.b"></a> <a id="spi__flash_8h_1a75dd52472fb01742c9821e7cd8046a15"></a> int32\_t spi\_flash\_write\_enable(uint32\_t spi\_dev\_inst, bool enable)
:   Write enable/disable.

    Enable or disable writing operations to the SPI Flash.

    参数:
    :   - **spi\_dev\_inst** – **\[in\]** spi device instance, return value of [drv\_spi\_init()](../../driver/drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **enable** – **\[in\]** true: enable write false: disable write

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422spi_flash_erase_sector8uint32_t8uint32_t"></a>

<a id="_CPPv322spi_flash_erase_sector8uint32_t8uint32_t"></a> <a id="_CPPv222spi_flash_erase_sector8uint32_t8uint32_t"></a> <a id="spi_flash_erase_sector__uint32_t.uint32_t"></a> <a id="spi__flash_8h_1a8c4e5f3cea91fefd81f954f6ba236bfa"></a> int32\_t spi\_flash\_erase\_sector(uint32\_t spi\_dev\_inst, uint32\_t addr)
:   Erase flash a sector.

    Erase a sector and addr is automatically aligned to the address of the next sector.

    参数:
    :   - **spi\_dev\_inst** – **\[in\]** spi device instance, return value of [drv\_spi\_init()](../../driver/drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **addr** – **\[in\]** offset address in flash, aligns to sector when erased.

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv415spi_flash_erase8uint32_t8uint32_t7uint8_t"></a>

<a id="_CPPv315spi_flash_erase8uint32_t8uint32_t7uint8_t"></a> <a id="_CPPv215spi_flash_erase8uint32_t8uint32_t7uint8_t"></a> <a id="spi_flash_erase__uint32_t.uint32_t.uint8_t"></a> <a id="spi__flash_8h_1a71b804ffe68c77537d41c152828b981d"></a> int32\_t spi\_flash\_erase(uint32\_t spi\_dev\_inst, uint32\_t addr, uint8\_t erase\_cmd)
:   Erase flash with user command.

    Erase the flash memory using user command.

    参数:
    :   - **spi\_dev\_inst** – **\[in\]** spi device instance, return value of [drv\_spi\_init()](../../driver/drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **addr** – **\[in\]** offset address in flash
        - **erase\_cmd** – **\[in\]** erase command

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420spi_flash_erase_chip8uint32_t8uint32_t"></a>

<a id="_CPPv320spi_flash_erase_chip8uint32_t8uint32_t"></a> <a id="_CPPv220spi_flash_erase_chip8uint32_t8uint32_t"></a> <a id="spi_flash_erase_chip__uint32_t.uint32_t"></a> <a id="spi__flash_8h_1a09de1697223f690135bca221c8a19377"></a> int32\_t spi\_flash\_erase\_chip(uint32\_t spi\_dev\_inst, uint32\_t timeout\_ms)
:   Erase the whole flash.

    Erase the whole flash.

    参数:
    :   - **spi\_dev\_inst** – **\[in\]** spi device instance, return value of [drv\_spi\_init()](../../driver/drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **timeout\_ms** – **\[in\]** tiimeout in ms

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv415spi_flash_write8uint32_t8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv315spi_flash_write8uint32_t8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv215spi_flash_write8uint32_t8uint32_tP7uint8_t8uint32_t"></a> <a id="spi_flash_write__uint32_t.uint32_t.uint8_tP.uint32_t"></a> <a id="spi__flash_8h_1a1cc692849c44d5a3af083f29e443c960"></a> int32\_t spi\_flash\_write(uint32\_t spi\_dev\_inst, uint32\_t addr, uint8\_t \*pu1\_buf, uint32\_t write\_size)
:   Write data to flash.

    Write data to flash. Reserve 4 bytes of memory before the address pointed to by pu1\_buf. The 4Byte will be temporarily occupied in this function, but will not be restored.

    参数:
    :   - **spi\_dev\_inst** – **\[in\]** spi device instance, return value of [drv\_spi\_init()](../../driver/drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **addr** – **\[in\]** offset address in flash
        - **pu1\_buf** – **\[in\]** pointer to the write buffer
        - **write\_size** – **\[in\]** write size

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv414spi_flash_read8uint32_t8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv314spi_flash_read8uint32_t8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv214spi_flash_read8uint32_t8uint32_tP7uint8_t8uint32_t"></a> <a id="spi_flash_read__uint32_t.uint32_t.uint8_tP.uint32_t"></a> <a id="spi__flash_8h_1a49f468eab44718b6bcadfc8b07ba7a7a"></a> int32\_t spi\_flash\_read(uint32\_t spi\_dev\_inst, uint32\_t addr, uint8\_t \*pu1\_buf, uint32\_t read\_size)
:   Read data from flash.

    Read data from flash. Reserve 4 bytes of memory before the address pointed to by pu1\_buf. The 4Byte will be temporarily occupied in this function, but will not be restored.

    参数:
    :   - **spi\_dev\_inst** – **\[in\]** spi device instance, return value of [drv\_spi\_init()](../../driver/drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **addr** – **\[in\]** offset address in flash
        - **pu1\_buf** – **\[in\]** pointer to the read buffer
        - **read\_size** – **\[in\]** read size

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv417spi_flash_4K_read8uint32_t8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv317spi_flash_4K_read8uint32_t8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv217spi_flash_4K_read8uint32_t8uint32_tP7uint8_t8uint32_t"></a> <a id="spi_flash_4K_read__uint32_t.uint32_t.uint8_tP.uint32_t"></a> <a id="spi__flash_8h_1a137c5a8a355f3ca8af29543bac97dad8"></a> int32\_t spi\_flash\_4K\_read(uint32\_t spi\_dev\_inst, uint32\_t addr, uint8\_t \*pu1\_buf, uint32\_t size)
:   Read SPI flash data less than 4K bytess.

    Hardware limitation, the maximum amount of data read at one time is 4K-1 bytes. Reserve 4 bytes of memory before the address pointed to by pu1\_buf. The 4Byte will be temporarily occupied in this function, but will not be restored.

    参数:
    :   - **spi\_dev\_inst** – **\[in\]** spi device instance, return value of [drv\_spi\_init()](../../driver/drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **addr** – **\[in\]** offset address in flash
        - **pu1\_buf** – **\[in\]** pointer to the read buffer
        - **size** – **\[in\]** read size

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv418spi_flash_calc_crc8uint32_t8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv318spi_flash_calc_crc8uint32_t8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv218spi_flash_calc_crc8uint32_t8uint32_tP7uint8_t8uint32_t"></a> <a id="spi_flash_calc_crc__uint32_t.uint32_t.uint8_tP.uint32_t"></a> <a id="spi__flash_8h_1ae29639152cc167d2c246ffb6665db937"></a> uint32\_t spi\_flash\_calc\_crc(uint32\_t spi\_dev\_inst, uint32\_t addr, uint8\_t \*pu1\_buf, uint32\_t size)
:   Calculate crc value from flash data.

    Calculate crc of data in flash. pu1\_buf requires a 4K buffer to temporarily store data.

    参数:
    :   - **spi\_dev\_inst** – **\[in\]** spi device instance, return value of [drv\_spi\_init()](../../driver/drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **addr** – **\[in\]** offset address in flash
        - **pu1\_buf** – **\[in\]** pointer to a 4K buffer for reading data
        - **size** – **\[in\]** calculate size, Can be much larger than 4K.

    返回:
    :   crc value

<a id="_CPPv426spi_flash_get_boot_timeout8uint32_t"></a>

<a id="_CPPv326spi_flash_get_boot_timeout8uint32_t"></a> <a id="_CPPv226spi_flash_get_boot_timeout8uint32_t"></a> <a id="spi_flash_get_boot_timeout__uint32_t"></a> <a id="spi__flash_8h_1ab87883c0977372c39515bf1f7d088053"></a> uint8\_t spi\_flash\_get\_boot\_timeout(uint32\_t spi\_dev\_inst)
:   Get boot timeout from flash.

    Read the ms time value of boot timeout from flash. Returning 0 means that it was not obtained.

    参数:
    :   **spi\_dev\_inst** – **\[in\]** spi device instance, return value of [drv\_spi\_init()](../../driver/drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)

    返回值:
    :   **0** – flash empty or data is invalid

    返回:
    :   boot timeout in ms

<a id="_CPPv422spi_flash_wait_op_done8uint32_t8uint32_t"></a>

<a id="_CPPv322spi_flash_wait_op_done8uint32_t8uint32_t"></a> <a id="_CPPv222spi_flash_wait_op_done8uint32_t8uint32_t"></a> <a id="spi_flash_wait_op_done__uint32_t.uint32_t"></a> <a id="spi__flash_8h_1a020271826e4bdab845e2b2a033ac3901"></a> void spi\_flash\_wait\_op\_done(uint32\_t spi\_dev\_inst, uint32\_t timeout\_ms\_req)
:   Wait spi flash process done.

    Wait for the SPI flash operation to complete or for the time to exceed timeout\_ms\_req.

    参数:
    :   - **spi\_dev\_inst** – **\[in\]** spi device instance, return value of [drv\_spi\_init()](../../driver/drv_spi.md#drv__spi_8h_1a3e1b21f4d0c9552346b7ca2ddf171ad1)
        - **timeout\_ms\_req** – **\[in\]** timeout wait in ms. 0 if don’t known

    返回:
    :   N/A **SPI\_FLASH\_H** EOF
