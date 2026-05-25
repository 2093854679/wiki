# FLASH PARTITION[](#flash-partition "永久链接至标题")


## FLASH PARTITION API Status[](#flash-partition-api-status "永久链接至标题")

| API | BK7236N |
| --- | --- |
| [`bk_flash_partition_get_info()`](#_CPPv427bk_flash_partition_get_info14bk_partition_t "bk_flash_partition_get_info") | Y |
| [`bk_flash_partition_erase()`](#_CPPv424bk_flash_partition_erase14bk_partition_t8uint32_t8uint32_t "bk_flash_partition_erase") | Y |
| [`bk_flash_partition_write()`](#_CPPv424bk_flash_partition_write14bk_partition_tPK7uint8_t8uint32_t8uint32_t "bk_flash_partition_write") | Y |
| [`bk_flash_partition_read()`](#_CPPv423bk_flash_partition_read14bk_partition_tP7uint8_t8uint32_t8uint32_t "bk_flash_partition_read") | Y |


## FLASH PARTITION API Reference[](#flash-partition-api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [flash_partition.h](https://github.com/bekencorp/armino/blob/main/components/flash_partition.h "https://github.com/bekencorp/armino/blob/main/components/flash_partition.h")


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

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_partition_erase_by_name(const char *label, uint32_t offset, uint32_t size)[](#_CPPv432bk_flash_partition_erase_by_namePKc8uint32_t8uint32_t "永久链接至目标")
:   Erase an area on a Flash logical partition.

    备注

    Erase on an address will erase all data on a sector that the address is belonged to, this function does not save data that beyond the address area but in the affected sector, the data will be lost.

    参数
    :   - **label** – The target flash logical partition which should be erased

        - **offset** – Start address of the erased flash area

        - **size** – Size of the erased flash area

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_partition_erase_all(const char *label)[](#_CPPv428bk_flash_partition_erase_allPKc "永久链接至目标")
:   Erase an area on a Flash logical partition.

    备注

    Erase on an address will erase all data on a sector that the address is belonged to, this function does not save data that beyond the address area but in the affected sector, the data will be lost.

    参数
    :   **label** – The target flash logical partition which should be erased all

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

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_partition_write_by_name(const char *label, const uint8_t *buffer, uint32_t offset, uint32_t buffer_len)[](#_CPPv432bk_flash_partition_write_by_namePKcPK7uint8_t8uint32_t8uint32_t "永久链接至目标")
:   Write data to an area on a Flash logical partition.

    参数
    :   - **label** – The target flash logical partition which should be written

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

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_partition_read_by_name(const char *label, uint8_t *out_buffer, uint32_t offset, uint32_t buffer_len)[](#_CPPv431bk_flash_partition_read_by_namePKcP7uint8_t8uint32_t8uint32_t "永久链接至目标")
:   Read data from an area on a Flash to data buffer in RAM.

    参数
    :   - **label** – The target flash logical partition which should be read

        - **out_buffer** – Pointer to the data buffer that stores the data read from flash

        - **offsets** – The offset of read address

        - **buffer_len** – The length of the buffer

    返回
    :   - BK_OK: succeed

        - others: other errors

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_partition_read_cbus([bk_partition_t](#_CPPv414bk_partition_t "bk_partition_t") partition, uint8_t *out_buffer, uint32_t offset, uint32_t buffer_len)[](#_CPPv428bk_flash_partition_read_cbus14bk_partition_tP7uint8_t8uint32_t8uint32_t "永久链接至目标")

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_flash_partition_write_cbus([bk_partition_t](#_CPPv414bk_partition_t "bk_partition_t") partition, const uint8_t *buffer, uint32_t offset, uint32_t buffer_len)[](#_CPPv429bk_flash_partition_write_cbus14bk_partition_tPK7uint8_t8uint32_t8uint32_t "永久链接至目标")
:   Write a block to flash via the control (CBUS) channel.

    参数
    :   - **partition** – Target logical partition.

        - **buffer** – Pointer to source data to be written.

        - **offset** – Offset inside the partition where writing starts.

        - **buffer_len** – Number of bytes to write.

    返回
    :   - BK_OK on success

        - other bk_err_t codes on failure

const [bk_logic_partition_t](#_CPPv420bk_logic_partition_t "bk_logic_partition_t") *get_partition_info_by_name(const char *label)[](#_CPPv426get_partition_info_by_namePKc "永久链接至目标")
:   Lookup the logical partition metadata by its name label.

    参数
    :   **label** – Null-terminated name of the desired partition.

    返回
    :   Pointer to partition descriptor or NULL if not found.

const [bk_logic_partition_t](#_CPPv420bk_logic_partition_t "bk_logic_partition_t") *get_partition_info([bk_partition_t](#_CPPv414bk_partition_t "bk_partition_t") partition)[](#_CPPv418get_partition_info14bk_partition_t "永久链接至目标")
:   Retrieve partition metadata from the enum identifier.

    参数
    :   **partition** – Enum value defined in bk_partition_t.

    返回
    :   Pointer to matching partition descriptor, or NULL when invalid.

const [bk_logic_partition_t](#_CPPv420bk_logic_partition_t "bk_logic_partition_t") *bk_flash_partition_get_info_by_name(const char *label)[](#_CPPv435bk_flash_partition_get_info_by_namePKc "永久链接至目标")
:   Redundant helper matching `get_partition_info_by_name`, exported for legacy compatibility.

    参数
    :   **label** – Name of the partition to query.

    返回
    :   Partition descriptor pointer or NULL when not found.

uint32_t get_partition_index(const [bk_logic_partition_t](#_CPPv420bk_logic_partition_t "bk_logic_partition_t") *partition)[](#_CPPv419get_partition_indexPK20bk_logic_partition_t "永久链接至目标")
:   Convert a partition descriptor into its table index.

    参数
    :   **partition** – Pointer to the logic partition returned by other helpers.

    返回
    :   Index (0-based) inside the flash partition table.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_spec_flash_write_bytes([bk_partition_t](#_CPPv414bk_partition_t "bk_partition_t") partition, const uint8_t *user_buf, uint32_t size, uint32_t offset)[](#_CPPv425bk_spec_flash_write_bytes14bk_partition_tPK7uint8_t8uint32_t8uint32_t "永久链接至目标")
:   Write data to flash (only operating 4k flash space)

    参数
    :   - **partition** – partition to write (eg:partition BK_PARTITION_SYS_RF)

        - **user_buf** – the pointer to data which is to write

        - **size** – size to write

        - **offset** – offset to write

    返回
    :   - BK_OK: succeed

        - BK_ERR_FLASH_ADDR_OUT_OF_RANGE: flash address is out of range

        - others: other errors.

static inline uint32_t bk_flash_partition_get_type(const [bk_logic_partition_t](#_CPPv420bk_logic_partition_t "bk_logic_partition_t") *partition)[](#_CPPv427bk_flash_partition_get_typePK20bk_logic_partition_t "永久链接至目标")
:   Extract the stored type (first byte) from partition options.

    参数
    :   **partition** – Pointer to the partition descriptor.

    返回
    :   Type field encoded into bits [31:24] of partition_options.

static inline uint32_t bk_flash_partition_get_options(const [bk_logic_partition_t](#_CPPv420bk_logic_partition_t "bk_logic_partition_t") *partition)[](#_CPPv430bk_flash_partition_get_optionsPK20bk_logic_partition_t "永久链接至目标")
:   Extract the option flags (lower 24 bits) from partition_options.

    参数
    :   **partition** – Pointer to the partition descriptor.

    返回
    :   Option bitmap stored in bits [23:0] of partition_options.


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

PARTITION_FLAGS_DBUS_READ[](#c.PARTITION_FLAGS_DBUS_READ "永久链接至目标")

PARTITION_FLAGS_DBUS_WRITE[](#c.PARTITION_FLAGS_DBUS_WRITE "永久链接至目标")

PARTITION_FLAGS_EXECUTE[](#c.PARTITION_FLAGS_EXECUTE "永久链接至目标")

PARTITION_FLAGS_CBUS_READ[](#c.PARTITION_FLAGS_CBUS_READ "永久链接至目标")

PARTITION_FLAGS_CBUS_WRITE[](#c.PARTITION_FLAGS_CBUS_WRITE "永久链接至目标")

PARTITION_FLAGS_OTA_WRITE_CBUS[](#c.PARTITION_FLAGS_OTA_WRITE_CBUS "永久链接至目标")

PARTITION_FLAGS_DOWNLOAD_WRITE_CBUS[](#c.PARTITION_FLAGS_DOWNLOAD_WRITE_CBUS "永久链接至目标")

PARTITION_FLAGS_OTA_READ_CBUS[](#c.PARTITION_FLAGS_OTA_READ_CBUS "永久链接至目标")

PARTITION_FLAGS_CBUS_NS[](#c.PARTITION_FLAGS_CBUS_NS "永久链接至目标")

PARTITION_FLAGS_DBUS_NS[](#c.PARTITION_FLAGS_DBUS_NS "永久链接至目标")


### Type Definitions[](#type-definitions "永久链接至标题")

typedef uint32_t bk_partition_t[](#_CPPv414bk_partition_t "永久链接至目标")

typedef uint16_t bk_partition_type_t[](#_CPPv419bk_partition_type_t "永久链接至目标")

typedef uint16_t bk_partition_subtype_t[](#_CPPv422bk_partition_subtype_t "永久链接至目标")


### Enumerations[](#enumerations "永久链接至标题")

enum bk_flash_t[](#_CPPv410bk_flash_t "永久链接至目标")
:   *Values:*

    enumerator BK_FLASH_EMBEDDED[](#_CPPv4N10bk_flash_t17BK_FLASH_EMBEDDEDE "永久链接至目标")

    enumerator BK_FLASH_SPI[](#_CPPv4N10bk_flash_t12BK_FLASH_SPIE "永久链接至目标")

    enumerator BK_FLASH_MAX[](#_CPPv4N10bk_flash_t12BK_FLASH_MAXE "永久链接至目标")

    enumerator BK_FLASH_NONE[](#_CPPv4N10bk_flash_t13BK_FLASH_NONEE "永久链接至目标")

enum [anonymous][](#_CPPv4Ut2_23 "永久链接至目标")
:   *Values:*

    enumerator PARTITION_TYPE_DATA[](#_CPPv4NUt2_2319PARTITION_TYPE_DATAE "永久链接至目标")

    enumerator PARTITION_TYPE_APP[](#_CPPv4NUt2_2318PARTITION_TYPE_APPE "永久链接至目标")

enum [anonymous][](#_CPPv4Ut2_24 "永久链接至目标")
:   *Values:*

    enumerator PARTITION_SUBTYPE_DEFAULT[](#_CPPv4NUt2_2425PARTITION_SUBTYPE_DEFAULTE "永久链接至目标")

    enumerator PARTITION_SUBTYPE_OW_ACTIVE[](#_CPPv4NUt2_2427PARTITION_SUBTYPE_OW_ACTIVEE "永久链接至目标")

    enumerator PARTITION_SUBTYPE_OW_OTA[](#_CPPv4NUt2_2424PARTITION_SUBTYPE_OW_OTAE "永久链接至目标")

    enumerator PARTITION_SUBTYPE_XIP_A[](#_CPPv4NUt2_2423PARTITION_SUBTYPE_XIP_AE "永久链接至目标")

    enumerator PARTITION_SUBTYPE_XIP_B[](#_CPPv4NUt2_2423PARTITION_SUBTYPE_XIP_BE "永久链接至目标")

    enumerator PARTITION_SUBTYPE_MERGE_OVERWRITE[](#_CPPv4NUt2_2433PARTITION_SUBTYPE_MERGE_OVERWRITEE "永久链接至目标")

    enumerator PARTITION_SUBTYPE_MERGE_XIP_A[](#_CPPv4NUt2_2429PARTITION_SUBTYPE_MERGE_XIP_AE "永久链接至目标")

    enumerator PARTITION_SUBTYPE_MERGE_XIP_B[](#_CPPv4NUt2_2429PARTITION_SUBTYPE_MERGE_XIP_BE "永久链接至目标")

    enumerator PARTITION_SUBTYPE_BL1_CTRL[](#_CPPv4NUt2_2426PARTITION_SUBTYPE_BL1_CTRLE "永久链接至目标")

    enumerator PARTITION_SUBTYPE_BL1_MANIFEST[](#_CPPv4NUt2_2430PARTITION_SUBTYPE_BL1_MANIFESTE "永久链接至目标")

    enumerator PARTITION_SUBTYPE_NVS[](#_CPPv4NUt2_2421PARTITION_SUBTYPE_NVSE "永久链接至目标")

    enumerator PARTITION_SUBTYPE_PARTITION[](#_CPPv4NUt2_2427PARTITION_SUBTYPE_PARTITIONE "永久链接至目标")

    enumerator PARTITION_SUBTYPE_OW_OTA_CONTROL[](#_CPPv4NUt2_2432PARTITION_SUBTYPE_OW_OTA_CONTROLE "永久链接至目标")

    enumerator PARTITION_SUBTYPE_XIP_OTA_CONTROL[](#_CPPv4NUt2_2433PARTITION_SUBTYPE_XIP_OTA_CONTROLE "永久链接至目标")
