# FLASH PARTITION[](#flash-partition "永久链接至标题")



## FLASH PARTITION API Status[](#flash-partition-api-status "永久链接至标题")

| API | BK7258 | BK7258_cp1 |
| --- | --- | --- |
| [`bk_flash_partition_get_info()`](#_CPPv427bk_flash_partition_get_info14bk_partition_t "bk_flash_partition_get_info") | Y | Y |
| [`bk_flash_partition_erase()`](#_CPPv424bk_flash_partition_erase14bk_partition_t8uint32_t8uint32_t "bk_flash_partition_erase") | Y | Y |
| [`bk_flash_partition_write()`](#_CPPv424bk_flash_partition_write14bk_partition_tPK7uint8_t8uint32_t8uint32_t "bk_flash_partition_write") | Y | Y |
| [`bk_flash_partition_read()`](#_CPPv423bk_flash_partition_read14bk_partition_tP7uint8_t8uint32_t8uint32_t "bk_flash_partition_read") | Y | Y |


## FLASH PARTITION API Reference[](#flash-partition-api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [flash_partition.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/flash_partition.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/flash_partition.h")


### Functions[](#functions "永久链接至标题")

[bk_logic_partition_t](#_CPPv420bk_logic_partition_t "bk_logic_partition_t") *bk_flash_partition_get_info([bk_partition_t](#_CPPv414bk_partition_t "bk_partition_t") partition)[](#_CPPv427bk_flash_partition_get_info14bk_partition_t "永久链接至目标")
:   Get the infomation of the specified flash area.

    参数
    :   **partition** – The target flash logical partition

    返回
    :   bk flash logic partition struct

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_partition_erase([bk_partition_t](#_CPPv414bk_partition_t "bk_partition_t") partition, uint32_t offset, uint32_t size)[](#_CPPv424bk_flash_partition_erase14bk_partition_t8uint32_t8uint32_t "永久链接至目标")
:   Erase an area on a Flash logical partition.

    备注

    Erase on an address will erase all data on a sector that the address is belonged to, this function does not save data that beyond the address area but in the affected sector, the data will be lost.

    参数
    :   - **partition** – The target flash logical partition which should be erased

        - **offset** – Start address of the erased flash area

        - **size** – Size of the erased flash area

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_partition_write([bk_partition_t](#_CPPv414bk_partition_t "bk_partition_t") partition, const uint8_t *buffer, uint32_t offset, uint32_t buffer_len)[](#_CPPv424bk_flash_partition_write14bk_partition_tPK7uint8_t8uint32_t8uint32_t "永久链接至目标")
:   Write data to an area on a Flash logical partition.

    参数
    :   - **partition** – The target flash logical partition which should be written

        - **buffer** – Pointer to the data buffer that will be written to flash

        - **off_set** – The offset of write address

        - **buffer_len** – The length of the buffer

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_partition_read([bk_partition_t](#_CPPv414bk_partition_t "bk_partition_t") partition, uint8_t *out_buffer, uint32_t offset, uint32_t buffer_len)[](#_CPPv423bk_flash_partition_read14bk_partition_tP7uint8_t8uint32_t8uint32_t "永久链接至目标")
:   Read data from an area on a Flash to data buffer in RAM.

    参数
    :   - **partition** – The target flash logical partition which should be read

        - **out_buffer** – Pointer to the data buffer that stores the data read from flash

        - **offsets** – The offset of read address

        - **buffer_len** – The length of the buffer

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_spec_flash_write_bytes([bk_partition_t](#_CPPv414bk_partition_t "bk_partition_t") partition, const uint8_t *user_buf, uint32_t size, uint32_t offset)[](#_CPPv425bk_spec_flash_write_bytes14bk_partition_tPK7uint8_t8uint32_t8uint32_t "永久链接至目标")
:   Write data to flash (only operating 4k flash space)

    参数
    :   - **partition** – partition to write (eg:partition BK_PARTITION_RF_FIRMWARE)

        - **user_buf** – the pointer to data which is to write

        - **size** – size to write

        - **offset** – offset to write

    返回
    :   - BK_OK: succeed

        - BK_ERR_FLASH_ADDR_OUT_OF_RANGE: flash address is out of range

        - others: other errors.


### Structures[](#structures "永久链接至标题")

struct bk_logic_partition_t[](#_CPPv420bk_logic_partition_t "永久链接至目标")
:   Public Members

    [bk_flash_t](#_CPPv410bk_flash_t "bk_flash_t") partition_owner[](#_CPPv4N20bk_logic_partition_t15partition_ownerE "永久链接至目标")
    :   flash partition owners

    const char *partition_description[](#_CPPv4N20bk_logic_partition_t21partition_descriptionE "永久链接至目标")
    :   flash partition description

    uint32_t partition_start_addr[](#_CPPv4N20bk_logic_partition_t20partition_start_addrE "永久链接至目标")
    :   flash partition start address

    uint32_t partition_length[](#_CPPv4N20bk_logic_partition_t16partition_lengthE "永久链接至目标")
    :   flash partition length

    uint32_t partition_options[](#_CPPv4N20bk_logic_partition_t17partition_optionsE "永久链接至目标")
    :   flash partition options


### Macros[](#macros "永久链接至标题")

PAR_OPT_READ_POS[](#c.PAR_OPT_READ_POS "永久链接至目标")

PAR_OPT_READ_DIS[](#c.PAR_OPT_READ_DIS "永久链接至目标")

PAR_OPT_READ_EN[](#c.PAR_OPT_READ_EN "永久链接至目标")

PAR_OPT_WRITE_POS[](#c.PAR_OPT_WRITE_POS "永久链接至目标")

PAR_OPT_WRITE_DIS[](#c.PAR_OPT_WRITE_DIS "永久链接至目标")

PAR_OPT_WRITE_EN[](#c.PAR_OPT_WRITE_EN "永久链接至目标")

PAR_OPT_EXECUTE_POS[](#c.PAR_OPT_EXECUTE_POS "永久链接至目标")

PAR_OPT_EXECUTE_DIS[](#c.PAR_OPT_EXECUTE_DIS "永久链接至目标")

PAR_OPT_EXECUTE_EN[](#c.PAR_OPT_EXECUTE_EN "永久链接至目标")


### Enumerations[](#enumerations "永久链接至标题")

enum bk_flash_t[](#_CPPv410bk_flash_t "永久链接至目标")
:   *Values:*

    enumerator BK_FLASH_EMBEDDED[](#_CPPv4N10bk_flash_t17BK_FLASH_EMBEDDEDE "永久链接至目标")

    enumerator BK_FLASH_SPI[](#_CPPv4N10bk_flash_t12BK_FLASH_SPIE "永久链接至目标")

    enumerator BK_FLASH_MAX[](#_CPPv4N10bk_flash_t12BK_FLASH_MAXE "永久链接至目标")

    enumerator BK_FLASH_NONE[](#_CPPv4N10bk_flash_t13BK_FLASH_NONEE "永久链接至目标")

enum bk_partition_t[](#_CPPv414bk_partition_t "永久链接至目标")
:   *Values:*

    enumerator BK_PARTITION_BOOTLOADER[](#_CPPv4N14bk_partition_t23BK_PARTITION_BOOTLOADERE "永久链接至目标")

    enumerator BK_PARTITION_APPLICATION[](#_CPPv4N14bk_partition_t24BK_PARTITION_APPLICATIONE "永久链接至目标")

    enumerator BK_PARTITION_OTA[](#_CPPv4N14bk_partition_t16BK_PARTITION_OTAE "永久链接至目标")

    enumerator BK_PARTITION_APPLICATION1[](#_CPPv4N14bk_partition_t25BK_PARTITION_APPLICATION1E "永久链接至目标")

    enumerator BK_PARTITION_MATTER_FLASH[](#_CPPv4N14bk_partition_t25BK_PARTITION_MATTER_FLASHE "永久链接至目标")

    enumerator BK_PARTITION_RF_FIRMWARE[](#_CPPv4N14bk_partition_t24BK_PARTITION_RF_FIRMWAREE "永久链接至目标")

    enumerator BK_PARTITION_NET_PARAM[](#_CPPv4N14bk_partition_t22BK_PARTITION_NET_PARAME "永久链接至目标")

    enumerator BK_PARTITION_USR_CONFIG[](#_CPPv4N14bk_partition_t23BK_PARTITION_USR_CONFIGE "永久链接至目标")

    enumerator BK_PARTITION_OTA_FINA_EXECUTIVE[](#_CPPv4N14bk_partition_t31BK_PARTITION_OTA_FINA_EXECUTIVEE "永久链接至目标")

    enumerator BK_PARTITION_APPLICATION2[](#_CPPv4N14bk_partition_t25BK_PARTITION_APPLICATION2E "永久链接至目标")

    enumerator BK_PARTITION_EASYFLASH[](#_CPPv4N14bk_partition_t22BK_PARTITION_EASYFLASHE "永久链接至目标")

    enumerator BK_PARTITION_MAX[](#_CPPv4N14bk_partition_t16BK_PARTITION_MAXE "永久链接至目标")
