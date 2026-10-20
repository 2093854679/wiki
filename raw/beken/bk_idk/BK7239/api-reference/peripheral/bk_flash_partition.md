---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7239/zh_CN/v2.2.1/api-reference/peripheral/bk_flash_partition.html
sdk_family: bk_idk
chip: BK7239
processor: ''
sdk_version: v2.2.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="flash-partition"></a>

# FLASH PARTITION

<a id="flash-partition-api-status"></a>

## FLASH PARTITION API Status

| API | BK7239 | BK7239\_cp1 |
| --- | --- | --- |
| [`bk_flash_partition_get_info()`](#_CPPv427bk_flash_partition_get_info14bk_partition_t "bk_flash_partition_get_info") | Y | Y |
| [`bk_flash_partition_erase()`](#_CPPv424bk_flash_partition_erase14bk_partition_t8uint32_t8uint32_t "bk_flash_partition_erase") | Y | Y |
| [`bk_flash_partition_write()`](#_CPPv424bk_flash_partition_write14bk_partition_tPK7uint8_t8uint32_t8uint32_t "bk_flash_partition_write") | Y | Y |
| [`bk_flash_partition_read()`](#_CPPv423bk_flash_partition_read14bk_partition_tP7uint8_t8uint32_t8uint32_t "bk_flash_partition_read") | Y | Y |

<a id="flash-partition-api-reference"></a>

## FLASH PARTITION API Reference

<a id="header-file"></a>

### Header File

- [flash\_partition.h](https://github.com/bekencorp/armino/blob/main/components/flash_partition.h)

<a id="functions"></a>

### Functions

<a id="_CPPv427bk_flash_partition_get_info14bk_partition_t"></a>

<a id="_CPPv327bk_flash_partition_get_info14bk_partition_t"></a> <a id="_CPPv227bk_flash_partition_get_info14bk_partition_t"></a> <a id="bk_flash_partition_get_info__bk_partition_t"></a> <a id="flash__partition_8h_1a6a40bf54d95fcf7edbd41d996068cf42"></a> [bk\_logic\_partition\_t](#_CPPv420bk_logic_partition_t "bk_logic_partition_t") \*bk\_flash\_partition\_get\_info([bk\_partition\_t](#_CPPv414bk_partition_t "bk_partition_t") partition)
:   Get the infomation of the specified flash area.

    参数
    :   **partition** – The target flash logical partition

    返回
    :   bk flash logic partition struct

<a id="_CPPv424bk_flash_partition_erase14bk_partition_t8uint32_t8uint32_t"></a>

<a id="_CPPv324bk_flash_partition_erase14bk_partition_t8uint32_t8uint32_t"></a> <a id="_CPPv224bk_flash_partition_erase14bk_partition_t8uint32_t8uint32_t"></a> <a id="bk_flash_partition_erase__bk_partition_t.uint32_t.uint32_t"></a> <a id="flash__partition_8h_1a69bd54922de9134d527a2cd597449f18"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_partition\_erase([bk\_partition\_t](#_CPPv414bk_partition_t "bk_partition_t") partition, uint32\_t offset, uint32\_t size)
:   Erase an area on a Flash logical partition.

    备注

    Erase on an address will erase all data on a sector that the address is belonged to, this function does not save data that beyond the address area but in the affected sector, the data will be lost.

    参数
    :   - **partition** – The target flash logical partition which should be erased
        - **offset** – Start address of the erased flash area
        - **size** – Size of the erased flash area

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv432bk_flash_partition_erase_by_namePKc8uint32_t8uint32_t"></a>

<a id="_CPPv332bk_flash_partition_erase_by_namePKc8uint32_t8uint32_t"></a> <a id="_CPPv232bk_flash_partition_erase_by_namePKc8uint32_t8uint32_t"></a> <a id="bk_flash_partition_erase_by_name__cCP.uint32_t.uint32_t"></a> <a id="flash__partition_8h_1a9ba0ad60c05cc6e5058db4242905dfa7"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_partition\_erase\_by\_name(const char \*label, uint32\_t offset, uint32\_t size)
:   Erase an area on a Flash logical partition.

    备注

    Erase on an address will erase all data on a sector that the address is belonged to, this function does not save data that beyond the address area but in the affected sector, the data will be lost.

    参数
    :   - **label** – The target flash logical partition which should be erased
        - **offset** – Start address of the erased flash area
        - **size** – Size of the erased flash area

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv428bk_flash_partition_erase_allPKc"></a>

<a id="_CPPv328bk_flash_partition_erase_allPKc"></a> <a id="_CPPv228bk_flash_partition_erase_allPKc"></a> <a id="bk_flash_partition_erase_all__cCP"></a> <a id="flash__partition_8h_1ab58566c23779dfd5a166c1e324053382"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_partition\_erase\_all(const char \*label)
:   Erase an area on a Flash logical partition.

    备注

    Erase on an address will erase all data on a sector that the address is belonged to, this function does not save data that beyond the address area but in the affected sector, the data will be lost.

    参数
    :   **label** – The target flash logical partition which should be erased all

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv424bk_flash_partition_write14bk_partition_tPK7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv324bk_flash_partition_write14bk_partition_tPK7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv224bk_flash_partition_write14bk_partition_tPK7uint8_t8uint32_t8uint32_t"></a> <a id="bk_flash_partition_write__bk_partition_t.uint8_tCP.uint32_t.uint32_t"></a> <a id="flash__partition_8h_1a0d8277d82a5816e7611cca4c9ba6afa2"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_partition\_write([bk\_partition\_t](#_CPPv414bk_partition_t "bk_partition_t") partition, const uint8\_t \*buffer, uint32\_t offset, uint32\_t buffer\_len)
:   Write data to an area on a Flash logical partition.

    参数
    :   - **partition** – The target flash logical partition which should be written
        - **buffer** – Pointer to the data buffer that will be written to flash
        - **off\_set** – The offset of write address
        - **buffer\_len** – The length of the buffer

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv432bk_flash_partition_write_by_namePKcPK7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv332bk_flash_partition_write_by_namePKcPK7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv232bk_flash_partition_write_by_namePKcPK7uint8_t8uint32_t8uint32_t"></a> <a id="bk_flash_partition_write_by_name__cCP.uint8_tCP.uint32_t.uint32_t"></a> <a id="flash__partition_8h_1af655464391e5bfc3b2c4205e52fdb9c5"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_partition\_write\_by\_name(const char \*label, const uint8\_t \*buffer, uint32\_t offset, uint32\_t buffer\_len)
:   Write data to an area on a Flash logical partition.

    参数
    :   - **label** – The target flash logical partition which should be written
        - **buffer** – Pointer to the data buffer that will be written to flash
        - **off\_set** – The offset of write address
        - **buffer\_len** – The length of the buffer

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv423bk_flash_partition_read14bk_partition_tP7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv323bk_flash_partition_read14bk_partition_tP7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv223bk_flash_partition_read14bk_partition_tP7uint8_t8uint32_t8uint32_t"></a> <a id="bk_flash_partition_read__bk_partition_t.uint8_tP.uint32_t.uint32_t"></a> <a id="flash__partition_8h_1a23fcd8caef7255dc7546f6f96aa3d357"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_partition\_read([bk\_partition\_t](#_CPPv414bk_partition_t "bk_partition_t") partition, uint8\_t \*out\_buffer, uint32\_t offset, uint32\_t buffer\_len)
:   Read data from an area on a Flash to data buffer in RAM.

    参数
    :   - **partition** – The target flash logical partition which should be read
        - **out\_buffer** – Pointer to the data buffer that stores the data read from flash
        - **offsets** – The offset of read address
        - **buffer\_len** – The length of the buffer

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv431bk_flash_partition_read_by_namePKcP7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv331bk_flash_partition_read_by_namePKcP7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv231bk_flash_partition_read_by_namePKcP7uint8_t8uint32_t8uint32_t"></a> <a id="bk_flash_partition_read_by_name__cCP.uint8_tP.uint32_t.uint32_t"></a> <a id="flash__partition_8h_1a05c9c188d7527647e9219b2a1a2b47d6"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_partition\_read\_by\_name(const char \*label, uint8\_t \*out\_buffer, uint32\_t offset, uint32\_t buffer\_len)
:   Read data from an area on a Flash to data buffer in RAM.

    参数
    :   - **label** – The target flash logical partition which should be read
        - **out\_buffer** – Pointer to the data buffer that stores the data read from flash
        - **offsets** – The offset of read address
        - **buffer\_len** – The length of the buffer

    返回
    :   - BK\_OK: succeed
        - others: other errors

<a id="_CPPv428bk_flash_partition_read_cbus14bk_partition_tP7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv328bk_flash_partition_read_cbus14bk_partition_tP7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv228bk_flash_partition_read_cbus14bk_partition_tP7uint8_t8uint32_t8uint32_t"></a> <a id="bk_flash_partition_read_cbus__bk_partition_t.uint8_tP.uint32_t.uint32_t"></a> <a id="flash__partition_8h_1ae21c172e332a3f9c63d6cace716dd0cd"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_partition\_read\_cbus([bk\_partition\_t](#_CPPv414bk_partition_t "bk_partition_t") partition, uint8\_t \*out\_buffer, uint32\_t offset, uint32\_t buffer\_len)

<a id="_CPPv429bk_flash_partition_write_cbus14bk_partition_tPK7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv329bk_flash_partition_write_cbus14bk_partition_tPK7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv229bk_flash_partition_write_cbus14bk_partition_tPK7uint8_t8uint32_t8uint32_t"></a> <a id="bk_flash_partition_write_cbus__bk_partition_t.uint8_tCP.uint32_t.uint32_t"></a> <a id="flash__partition_8h_1ab9c0676ecc0318514d912d08b071a8c7"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_flash\_partition\_write\_cbus([bk\_partition\_t](#_CPPv414bk_partition_t "bk_partition_t") partition, const uint8\_t \*buffer, uint32\_t offset, uint32\_t buffer\_len)
:   Write a block to flash via the control (CBUS) channel.

    参数
    :   - **partition** – Target logical partition.
        - **buffer** – Pointer to source data to be written.
        - **offset** – Offset inside the partition where writing starts.
        - **buffer\_len** – Number of bytes to write.

    返回
    :   - BK\_OK on success
        - other bk\_err\_t codes on failure

<a id="_CPPv426get_partition_info_by_namePKc"></a>

<a id="_CPPv326get_partition_info_by_namePKc"></a> <a id="_CPPv226get_partition_info_by_namePKc"></a> <a id="get_partition_info_by_name__cCP"></a> <a id="flash__partition_8h_1ac8516be549732d6d0f6d131184ec15f5"></a> const [bk\_logic\_partition\_t](#_CPPv420bk_logic_partition_t "bk_logic_partition_t") \*get\_partition\_info\_by\_name(const char \*label)
:   Lookup the logical partition metadata by its name label.

    参数
    :   **label** – Null-terminated name of the desired partition.

    返回
    :   Pointer to partition descriptor or NULL if not found.

<a id="_CPPv418get_partition_info14bk_partition_t"></a>

<a id="_CPPv318get_partition_info14bk_partition_t"></a> <a id="_CPPv218get_partition_info14bk_partition_t"></a> <a id="get_partition_info__bk_partition_t"></a> <a id="flash__partition_8h_1ad20e9d16f0811e8b60b1efcaa599f4ff"></a> const [bk\_logic\_partition\_t](#_CPPv420bk_logic_partition_t "bk_logic_partition_t") \*get\_partition\_info([bk\_partition\_t](#_CPPv414bk_partition_t "bk_partition_t") partition)
:   Retrieve partition metadata from the enum identifier.

    参数
    :   **partition** – Enum value defined in bk\_partition\_t.

    返回
    :   Pointer to matching partition descriptor, or NULL when invalid.

<a id="_CPPv435bk_flash_partition_get_info_by_namePKc"></a>

<a id="_CPPv335bk_flash_partition_get_info_by_namePKc"></a> <a id="_CPPv235bk_flash_partition_get_info_by_namePKc"></a> <a id="bk_flash_partition_get_info_by_name__cCP"></a> <a id="flash__partition_8h_1ac8c79c25fb0bf864fddefc54c3739647"></a> const [bk\_logic\_partition\_t](#_CPPv420bk_logic_partition_t "bk_logic_partition_t") \*bk\_flash\_partition\_get\_info\_by\_name(const char \*label)
:   Redundant helper matching `get_partition_info_by_name`, exported for legacy compatibility.

    参数
    :   **label** – Name of the partition to query.

    返回
    :   Partition descriptor pointer or NULL when not found.

<a id="_CPPv419get_partition_indexPK20bk_logic_partition_t"></a>

<a id="_CPPv319get_partition_indexPK20bk_logic_partition_t"></a> <a id="_CPPv219get_partition_indexPK20bk_logic_partition_t"></a> <a id="get_partition_index__bk_logic_partition_tCP"></a> <a id="flash__partition_8h_1a84d14d34d6284960a1216c26d47c171d"></a> uint32\_t get\_partition\_index(const [bk\_logic\_partition\_t](#_CPPv420bk_logic_partition_t "bk_logic_partition_t") \*partition)
:   Convert a partition descriptor into its table index.

    参数
    :   **partition** – Pointer to the logic partition returned by other helpers.

    返回
    :   Index (0-based) inside the flash partition table.

<a id="_CPPv425bk_spec_flash_write_bytes14bk_partition_tPK7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv325bk_spec_flash_write_bytes14bk_partition_tPK7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv225bk_spec_flash_write_bytes14bk_partition_tPK7uint8_t8uint32_t8uint32_t"></a> <a id="bk_spec_flash_write_bytes__bk_partition_t.uint8_tCP.uint32_t.uint32_t"></a> <a id="flash__partition_8h_1a20dcf931fdefca108317b144f9088ec3"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_spec\_flash\_write\_bytes([bk\_partition\_t](#_CPPv414bk_partition_t "bk_partition_t") partition, const uint8\_t \*user\_buf, uint32\_t size, uint32\_t offset)
:   Write data to flash (only operating 4k flash space)

    参数
    :   - **partition** – partition to write (eg:partition BK\_PARTITION\_SYS\_RF)
        - **user\_buf** – the pointer to data which is to write
        - **size** – size to write
        - **offset** – offset to write

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_FLASH\_ADDR\_OUT\_OF\_RANGE: flash address is out of range
        - others: other errors.

<a id="_CPPv427bk_flash_partition_get_typePK20bk_logic_partition_t"></a>

<a id="_CPPv327bk_flash_partition_get_typePK20bk_logic_partition_t"></a> <a id="_CPPv227bk_flash_partition_get_typePK20bk_logic_partition_t"></a> <a id="bk_flash_partition_get_type__bk_logic_partition_tCP"></a> <a id="flash__partition_8h_1ab1147963634d9cf747d23efb232eac32"></a> static inline uint32\_t bk\_flash\_partition\_get\_type(const [bk\_logic\_partition\_t](#_CPPv420bk_logic_partition_t "bk_logic_partition_t") \*partition)
:   Extract the stored type (first byte) from partition options.

    参数
    :   **partition** – Pointer to the partition descriptor.

    返回
    :   Type field encoded into bits \[31:24\] of partition\_options.

<a id="_CPPv430bk_flash_partition_get_optionsPK20bk_logic_partition_t"></a>

<a id="_CPPv330bk_flash_partition_get_optionsPK20bk_logic_partition_t"></a> <a id="_CPPv230bk_flash_partition_get_optionsPK20bk_logic_partition_t"></a> <a id="bk_flash_partition_get_options__bk_logic_partition_tCP"></a> <a id="flash__partition_8h_1a95e023146746d56dd05947259d1c65f2"></a> static inline uint32\_t bk\_flash\_partition\_get\_options(const [bk\_logic\_partition\_t](#_CPPv420bk_logic_partition_t "bk_logic_partition_t") \*partition)
:   Extract the option flags (lower 24 bits) from partition\_options.

    参数
    :   **partition** – Pointer to the partition descriptor.

    返回
    :   Option bitmap stored in bits \[23:0\] of partition\_options.

<a id="structures"></a>

### Structures

<a id="_CPPv420bk_logic_partition_t"></a>

<a id="_CPPv320bk_logic_partition_t"></a> <a id="_CPPv220bk_logic_partition_t"></a> <a id="bk_logic_partition_t"></a> <a id="structbk__logic__partition__t"></a> struct bk\_logic\_partition\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20bk_logic_partition_t15partition_ownerE"></a>

    <a id="_CPPv3N20bk_logic_partition_t15partition_ownerE"></a> <a id="_CPPv2N20bk_logic_partition_t15partition_ownerE"></a> <a id="bk_logic_partition_t::partition_owner__bk_flash_t"></a> <a id="structbk__logic__partition__t_1a4a84f0f2dc9f7a965d7d474dd2c45fbb"></a> [bk\_flash\_t](#_CPPv410bk_flash_t "bk_flash_t") partition\_owner
    :   flash partition owners

    <a id="_CPPv4N20bk_logic_partition_t21partition_descriptionE"></a>

    <a id="_CPPv3N20bk_logic_partition_t21partition_descriptionE"></a> <a id="_CPPv2N20bk_logic_partition_t21partition_descriptionE"></a> <a id="bk_logic_partition_t::partition_description__cCP"></a> <a id="structbk__logic__partition__t_1a6cc1bc293ee15fedcdc0f7f2313e39cc"></a> const char \*partition\_description
    :   flash partition description

    <a id="_CPPv4N20bk_logic_partition_t20partition_start_addrE"></a>

    <a id="_CPPv3N20bk_logic_partition_t20partition_start_addrE"></a> <a id="_CPPv2N20bk_logic_partition_t20partition_start_addrE"></a> <a id="bk_logic_partition_t::partition_start_addr__uint32_t"></a> <a id="structbk__logic__partition__t_1a406dee3af89af369a3a0e036af3b5bd6"></a> uint32\_t partition\_start\_addr
    :   flash partition start address

    <a id="_CPPv4N20bk_logic_partition_t16partition_lengthE"></a>

    <a id="_CPPv3N20bk_logic_partition_t16partition_lengthE"></a> <a id="_CPPv2N20bk_logic_partition_t16partition_lengthE"></a> <a id="bk_logic_partition_t::partition_length__uint32_t"></a> <a id="structbk__logic__partition__t_1a4fca2a7e34c6b94ca186c6371954bc52"></a> uint32\_t partition\_length
    :   flash partition length

    <a id="_CPPv4N20bk_logic_partition_t17partition_optionsE"></a>

    <a id="_CPPv3N20bk_logic_partition_t17partition_optionsE"></a> <a id="_CPPv2N20bk_logic_partition_t17partition_optionsE"></a> <a id="bk_logic_partition_t::partition_options__uint32_t"></a> <a id="structbk__logic__partition__t_1af56d447fab2e36c000a10033a298b704"></a> uint32\_t partition\_options
    :   flash partition options

<a id="macros"></a>

### Macros

<a id="c.PAR_OPT_READ_POS"></a>

<a id="flash__partition_8h_1ab1e58b6e8ff6f3761bdf24c04478c7f6"></a> PAR\_OPT\_READ\_POS

<a id="c.PAR_OPT_READ_DIS"></a>

<a id="flash__partition_8h_1a4f5a8817f87909dd93f8b655236bfa97"></a> PAR\_OPT\_READ\_DIS

<a id="c.PAR_OPT_READ_EN"></a>

<a id="flash__partition_8h_1ad38fd963b47f4417058bde27626cec60"></a> PAR\_OPT\_READ\_EN

<a id="c.PAR_OPT_WRITE_POS"></a>

<a id="flash__partition_8h_1a68ff33d27eb40be97075ac7acc28b1dc"></a> PAR\_OPT\_WRITE\_POS

<a id="c.PAR_OPT_WRITE_DIS"></a>

<a id="flash__partition_8h_1a2e3aedc128cf4fc5c1962e9229ef00e9"></a> PAR\_OPT\_WRITE\_DIS

<a id="c.PAR_OPT_WRITE_EN"></a>

<a id="flash__partition_8h_1a06797fb3f63772e5b3b7b72edd7ae86b"></a> PAR\_OPT\_WRITE\_EN

<a id="c.PAR_OPT_EXECUTE_POS"></a>

<a id="flash__partition_8h_1a4b859874465b68d0b73f199cb63a6a4e"></a> PAR\_OPT\_EXECUTE\_POS

<a id="c.PAR_OPT_EXECUTE_DIS"></a>

<a id="flash__partition_8h_1af195043b4881e393d9ae1771bfa79141"></a> PAR\_OPT\_EXECUTE\_DIS

<a id="c.PAR_OPT_EXECUTE_EN"></a>

<a id="flash__partition_8h_1ad3cbc9b409aa5a152c6f96e74b207055"></a> PAR\_OPT\_EXECUTE\_EN

<a id="c.PARTITION_FLAGS_DBUS_READ"></a>

<a id="flash__partition_8h_1ae56483e8bf5d385ed782a2690341a32f"></a> PARTITION\_FLAGS\_DBUS\_READ

<a id="c.PARTITION_FLAGS_DBUS_WRITE"></a>

<a id="flash__partition_8h_1aeb959550a18923b4ab4b5376b839d42a"></a> PARTITION\_FLAGS\_DBUS\_WRITE

<a id="c.PARTITION_FLAGS_EXECUTE"></a>

<a id="flash__partition_8h_1a2c740945c48ba8ec89ac609ca658420a"></a> PARTITION\_FLAGS\_EXECUTE

<a id="c.PARTITION_FLAGS_CBUS_READ"></a>

<a id="flash__partition_8h_1af7a89c1cb5145badacbb4377cd7a0983"></a> PARTITION\_FLAGS\_CBUS\_READ

<a id="c.PARTITION_FLAGS_CBUS_WRITE"></a>

<a id="flash__partition_8h_1a04f82eeca397e99b7f6f8c9b9ff513c0"></a> PARTITION\_FLAGS\_CBUS\_WRITE

<a id="c.PARTITION_FLAGS_OTA_WRITE_CBUS"></a>

<a id="flash__partition_8h_1a01d5ac9a5565586c2dcdc64f7551b86b"></a> PARTITION\_FLAGS\_OTA\_WRITE\_CBUS

<a id="c.PARTITION_FLAGS_DOWNLOAD_WRITE_CBUS"></a>

<a id="flash__partition_8h_1a162fd084896a298fd3be8329e37e70c4"></a> PARTITION\_FLAGS\_DOWNLOAD\_WRITE\_CBUS

<a id="c.PARTITION_FLAGS_OTA_READ_CBUS"></a>

<a id="flash__partition_8h_1a4b2f3b6aaedac1befa674cf2361141f3"></a> PARTITION\_FLAGS\_OTA\_READ\_CBUS

<a id="c.PARTITION_FLAGS_CBUS_NS"></a>

<a id="flash__partition_8h_1a48f25e324622b8aab250c50cd6f03425"></a> PARTITION\_FLAGS\_CBUS\_NS

<a id="c.PARTITION_FLAGS_DBUS_NS"></a>

<a id="flash__partition_8h_1a50b521ab848bc3fc69eb42ae7ff40417"></a> PARTITION\_FLAGS\_DBUS\_NS

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv414bk_partition_t"></a>

<a id="_CPPv314bk_partition_t"></a> <a id="_CPPv214bk_partition_t"></a> <a id="bk_partition_t"></a> <a id="flash__partition_8h_1a5ab0512c0b6e9b4e0961aefc9f5465fc"></a> typedef uint32\_t bk\_partition\_t

<a id="_CPPv419bk_partition_type_t"></a>

<a id="_CPPv319bk_partition_type_t"></a> <a id="_CPPv219bk_partition_type_t"></a> <a id="bk_partition_type_t"></a> <a id="flash__partition_8h_1a7e03252ca70ddffff6b19cf181acd620"></a> typedef uint16\_t bk\_partition\_type\_t

<a id="_CPPv422bk_partition_subtype_t"></a>

<a id="_CPPv322bk_partition_subtype_t"></a> <a id="_CPPv222bk_partition_subtype_t"></a> <a id="bk_partition_subtype_t"></a> <a id="flash__partition_8h_1a5263ffe5934a8a64b11d13e4f69b1dd4"></a> typedef uint16\_t bk\_partition\_subtype\_t

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv410bk_flash_t"></a>

<a id="_CPPv310bk_flash_t"></a> <a id="_CPPv210bk_flash_t"></a> <a id="flash__partition_8h_1a4269a42fcd5cccdf95cc910a91c515f8"></a> enum bk\_flash\_t
:   *Values:*

    <a id="_CPPv4N10bk_flash_t17BK_FLASH_EMBEDDEDE"></a>

    <a id="_CPPv3N10bk_flash_t17BK_FLASH_EMBEDDEDE"></a> <a id="_CPPv2N10bk_flash_t17BK_FLASH_EMBEDDEDE"></a> <a id="flash__partition_8h_1a4269a42fcd5cccdf95cc910a91c515f8a18d4385876664c390fb5dd7f411d72db"></a> enumerator BK\_FLASH\_EMBEDDED

    <a id="_CPPv4N10bk_flash_t12BK_FLASH_SPIE"></a>

    <a id="_CPPv3N10bk_flash_t12BK_FLASH_SPIE"></a> <a id="_CPPv2N10bk_flash_t12BK_FLASH_SPIE"></a> <a id="flash__partition_8h_1a4269a42fcd5cccdf95cc910a91c515f8ad29e6e471dea17232cabc86fea92d5d0"></a> enumerator BK\_FLASH\_SPI

    <a id="_CPPv4N10bk_flash_t12BK_FLASH_MAXE"></a>

    <a id="_CPPv3N10bk_flash_t12BK_FLASH_MAXE"></a> <a id="_CPPv2N10bk_flash_t12BK_FLASH_MAXE"></a> <a id="flash__partition_8h_1a4269a42fcd5cccdf95cc910a91c515f8a2dd397b52046e6b78c3aec143626d038"></a> enumerator BK\_FLASH\_MAX

    <a id="_CPPv4N10bk_flash_t13BK_FLASH_NONEE"></a>

    <a id="_CPPv3N10bk_flash_t13BK_FLASH_NONEE"></a> <a id="_CPPv2N10bk_flash_t13BK_FLASH_NONEE"></a> <a id="flash__partition_8h_1a4269a42fcd5cccdf95cc910a91c515f8ab37cc8aea703f16be396c045c6ddf474"></a> enumerator BK\_FLASH\_NONE

<a id="_CPPv4Ut2_23"></a>

<a id="_CPPv3Ut2_23"></a> <a id="flash__partition_8h_1aaf8fd5f0e57d456151c951e0f3715fc4"></a> enum \[anonymous\]
:   *Values:*

    <a id="_CPPv4NUt2_2319PARTITION_TYPE_DATAE"></a>

    <a id="_CPPv3NUt2_2319PARTITION_TYPE_DATAE"></a> <a id="flash__partition_8h_1aaf8fd5f0e57d456151c951e0f3715fc4a7c51027bf447db3863d69aa952d01b90"></a> enumerator PARTITION\_TYPE\_DATA

    <a id="_CPPv4NUt2_2318PARTITION_TYPE_APPE"></a>

    <a id="_CPPv3NUt2_2318PARTITION_TYPE_APPE"></a> <a id="flash__partition_8h_1aaf8fd5f0e57d456151c951e0f3715fc4a3b6c83bec8136d2bbef2ab955f65b493"></a> enumerator PARTITION\_TYPE\_APP

<a id="_CPPv4Ut2_24"></a>

<a id="_CPPv3Ut2_24"></a> <a id="flash__partition_8h_1a94798fdadfbf49a7c658ace669a1d310"></a> enum \[anonymous\]
:   *Values:*

    <a id="_CPPv4NUt2_2425PARTITION_SUBTYPE_DEFAULTE"></a>

    <a id="_CPPv3NUt2_2425PARTITION_SUBTYPE_DEFAULTE"></a> <a id="flash__partition_8h_1a94798fdadfbf49a7c658ace669a1d310a384919437e76a96a6563cf2e9e3801eb"></a> enumerator PARTITION\_SUBTYPE\_DEFAULT

    <a id="_CPPv4NUt2_2427PARTITION_SUBTYPE_OW_ACTIVEE"></a>

    <a id="_CPPv3NUt2_2427PARTITION_SUBTYPE_OW_ACTIVEE"></a> <a id="flash__partition_8h_1a94798fdadfbf49a7c658ace669a1d310a875d9882d68c83a2f0b7f3b278228a7e"></a> enumerator PARTITION\_SUBTYPE\_OW\_ACTIVE

    <a id="_CPPv4NUt2_2424PARTITION_SUBTYPE_OW_OTAE"></a>

    <a id="_CPPv3NUt2_2424PARTITION_SUBTYPE_OW_OTAE"></a> <a id="flash__partition_8h_1a94798fdadfbf49a7c658ace669a1d310ad13f5da01d612ab5c5120adf85301b59"></a> enumerator PARTITION\_SUBTYPE\_OW\_OTA

    <a id="_CPPv4NUt2_2423PARTITION_SUBTYPE_XIP_AE"></a>

    <a id="_CPPv3NUt2_2423PARTITION_SUBTYPE_XIP_AE"></a> <a id="flash__partition_8h_1a94798fdadfbf49a7c658ace669a1d310ad64ae781089e35336e44bf4961131448"></a> enumerator PARTITION\_SUBTYPE\_XIP\_A

    <a id="_CPPv4NUt2_2423PARTITION_SUBTYPE_XIP_BE"></a>

    <a id="_CPPv3NUt2_2423PARTITION_SUBTYPE_XIP_BE"></a> <a id="flash__partition_8h_1a94798fdadfbf49a7c658ace669a1d310ac868335f0a6b7bf8c8bbaaa375eda892"></a> enumerator PARTITION\_SUBTYPE\_XIP\_B

    <a id="_CPPv4NUt2_2433PARTITION_SUBTYPE_MERGE_OVERWRITEE"></a>

    <a id="_CPPv3NUt2_2433PARTITION_SUBTYPE_MERGE_OVERWRITEE"></a> <a id="flash__partition_8h_1a94798fdadfbf49a7c658ace669a1d310ad7ae13a82fb635321e7439c3ee6a4099"></a> enumerator PARTITION\_SUBTYPE\_MERGE\_OVERWRITE

    <a id="_CPPv4NUt2_2429PARTITION_SUBTYPE_MERGE_XIP_AE"></a>

    <a id="_CPPv3NUt2_2429PARTITION_SUBTYPE_MERGE_XIP_AE"></a> <a id="flash__partition_8h_1a94798fdadfbf49a7c658ace669a1d310a9d75ee76a536e29d15ce584606de3d85"></a> enumerator PARTITION\_SUBTYPE\_MERGE\_XIP\_A

    <a id="_CPPv4NUt2_2429PARTITION_SUBTYPE_MERGE_XIP_BE"></a>

    <a id="_CPPv3NUt2_2429PARTITION_SUBTYPE_MERGE_XIP_BE"></a> <a id="flash__partition_8h_1a94798fdadfbf49a7c658ace669a1d310ab478074cfe33a9d8dfd25e18bb73e1db"></a> enumerator PARTITION\_SUBTYPE\_MERGE\_XIP\_B

    <a id="_CPPv4NUt2_2426PARTITION_SUBTYPE_BL1_CTRLE"></a>

    <a id="_CPPv3NUt2_2426PARTITION_SUBTYPE_BL1_CTRLE"></a> <a id="flash__partition_8h_1a94798fdadfbf49a7c658ace669a1d310aa16e27de2a18cff0dbf5d7e1dedb7f0c"></a> enumerator PARTITION\_SUBTYPE\_BL1\_CTRL

    <a id="_CPPv4NUt2_2430PARTITION_SUBTYPE_BL1_MANIFESTE"></a>

    <a id="_CPPv3NUt2_2430PARTITION_SUBTYPE_BL1_MANIFESTE"></a> <a id="flash__partition_8h_1a94798fdadfbf49a7c658ace669a1d310a0f8b35a4f7e15fd2db28afdcb2b0e159"></a> enumerator PARTITION\_SUBTYPE\_BL1\_MANIFEST

    <a id="_CPPv4NUt2_2421PARTITION_SUBTYPE_NVSE"></a>

    <a id="_CPPv3NUt2_2421PARTITION_SUBTYPE_NVSE"></a> <a id="flash__partition_8h_1a94798fdadfbf49a7c658ace669a1d310a4137d2967a6466890ad31f987132b743"></a> enumerator PARTITION\_SUBTYPE\_NVS

    <a id="_CPPv4NUt2_2427PARTITION_SUBTYPE_PARTITIONE"></a>

    <a id="_CPPv3NUt2_2427PARTITION_SUBTYPE_PARTITIONE"></a> <a id="flash__partition_8h_1a94798fdadfbf49a7c658ace669a1d310ac8fd30ba1de26cb16e0705ade693e189"></a> enumerator PARTITION\_SUBTYPE\_PARTITION

    <a id="_CPPv4NUt2_2432PARTITION_SUBTYPE_OW_OTA_CONTROLE"></a>

    <a id="_CPPv3NUt2_2432PARTITION_SUBTYPE_OW_OTA_CONTROLE"></a> <a id="flash__partition_8h_1a94798fdadfbf49a7c658ace669a1d310af210b4f57fe9b94a7ef96fcac897ee3a"></a> enumerator PARTITION\_SUBTYPE\_OW\_OTA\_CONTROL

    <a id="_CPPv4NUt2_2433PARTITION_SUBTYPE_XIP_OTA_CONTROLE"></a>

    <a id="_CPPv3NUt2_2433PARTITION_SUBTYPE_XIP_OTA_CONTROLE"></a> <a id="flash__partition_8h_1a94798fdadfbf49a7c658ace669a1d310a98aee9cda7ae81829deab5d26cd69622"></a> enumerator PARTITION\_SUBTYPE\_XIP\_OTA\_CONTROL
