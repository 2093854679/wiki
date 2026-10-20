---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/component/bk_flash.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk-flash"></a>

# BK\_FLASH

<a id="bk-flash-api-status"></a>

## BK\_FLASH API Status

| API |
| --- |
| [`bk_flash_init()`](#_CPPv413bk_flash_initv "bk_flash_init") |
| [`bk_flash_op_start()`](#_CPPv417bk_flash_op_startv "bk_flash_op_start") |
| [`bk_flash_erase_sector()`](#_CPPv421bk_flash_erase_sector8uint32_t19pfunc_bk_flash_cb_tPv "bk_flash_erase_sector") |
| [`bk_flash_write_bytes()`](#_CPPv420bk_flash_write_bytes8uint32_tP7uint8_t8uint32_t19pfunc_bk_flash_cb_tPv "bk_flash_write_bytes") |
| [`bk_flash_read_bytes()`](#_CPPv419bk_flash_read_bytes8uint32_tP7uint8_t8uint32_t19pfunc_bk_flash_cb_tPv "bk_flash_read_bytes") |
| [`bk_flash_erase_block_32k()`](#_CPPv424bk_flash_erase_block_32k8uint32_t19pfunc_bk_flash_cb_tPv "bk_flash_erase_block_32k") |
| [`bk_flash_show_info()`](#_CPPv418bk_flash_show_infov "bk_flash_show_info") |
| [`bk_flash_get_max_work_freq()`](#_CPPv426bk_flash_get_max_work_freqv "bk_flash_get_max_work_freq") |
| `bk_flash_force_reboot()` |

<a id="bk-flash-api-reference"></a>

## BK\_FLASH API Reference

<a id="header-file"></a>

### Header File

- [component/flash/bk\_flash.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/component/flash/bk_flash.h)

<a id="functions"></a>

### Functions

<a id="_CPPv413bk_flash_initv"></a>

<a id="_CPPv313bk_flash_initv"></a> <a id="_CPPv213bk_flash_initv"></a> <a id="bk_flash_init__void"></a> <a id="bk__flash_8h_1a68e0a760884df0e8407c904ae019c815"></a> void bk\_flash\_init(void)
:   sys flash init

    (1)identify flash model (2)if flash support quard I/O fast read(0xEB), then switch to 4 line mode (3)set flash block protect bit, protest flash all block

<a id="_CPPv417bk_flash_op_startv"></a>

<a id="_CPPv317bk_flash_op_startv"></a> <a id="_CPPv217bk_flash_op_startv"></a> <a id="bk_flash_op_start__void"></a> <a id="bk__flash_8h_1ab44434f3874c77d524659adf60af2735"></a> void bk\_flash\_op\_start(void)
:   flash operation(erase/write/read) start

    if user use bk\_flash\_erase\_sector/bk\_flash\_write\_bytes/bk\_flash\_read\_bytes funtion and pfn\_cb!\=NULL should use this funtion to start flash operation

<a id="_CPPv421bk_flash_erase_sector8uint32_t19pfunc_bk_flash_cb_tPv"></a>

<a id="_CPPv321bk_flash_erase_sector8uint32_t19pfunc_bk_flash_cb_tPv"></a> <a id="_CPPv221bk_flash_erase_sector8uint32_t19pfunc_bk_flash_cb_tPv"></a> <a id="bk_flash_erase_sector__uint32_t.pfunc_bk_flash_cb_t.voidP"></a> <a id="bk__flash_8h_1af49174ad983bb5fa141ef5c86d3ebc8a"></a> int32\_t bk\_flash\_erase\_sector(uint32\_t address, [pfunc\_bk\_flash\_cb\_t](#_CPPv419pfunc_bk_flash_cb_t "pfunc_bk_flash_cb_t") pfn\_cb, void \*pv\_arg)
:   flash sector erase

    flash cmd is 0x20 If pfn\_cb\=\=NULL, flash write operate immediately. exit this funtion after the erase operation is completed If pfn\_cb!\=NULL, flash write operate no immediately. Exection pfn\_cb funtion after the erase operation is completed

    参数:
    :   - **address** – **\[in\]** erase address
        - **pfn\_cb** – **\[in\]** callback function for async send. it can be NULL if you do not want async send
        - **pv\_arg** – **\[in\]** user give callback parameter

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420bk_flash_write_bytes8uint32_tP7uint8_t8uint32_t19pfunc_bk_flash_cb_tPv"></a>

<a id="_CPPv320bk_flash_write_bytes8uint32_tP7uint8_t8uint32_t19pfunc_bk_flash_cb_tPv"></a> <a id="_CPPv220bk_flash_write_bytes8uint32_tP7uint8_t8uint32_t19pfunc_bk_flash_cb_tPv"></a> <a id="bk_flash_write_bytes__uint32_t.uint8_tP.uint32_t.pfunc_bk_flash_cb_t.voidP"></a> <a id="bk__flash_8h_1a5342215c60e68f15a98d9b4b0ecbd045"></a> int32\_t bk\_flash\_write\_bytes(uint32\_t address, uint8\_t \*pu1\_buf, uint32\_t size, [pfunc\_bk\_flash\_cb\_t](#_CPPv419pfunc_bk_flash_cb_t "pfunc_bk_flash_cb_t") pfn\_cb, void \*pv\_arg)
:   flash write data

    If pfn\_cb\=\=NULL, flash write operate immediately. exit this funtion after the write operation is completed If pfn\_cb!\=NULL, flash write operate no immediately. Exection pfn\_cb funtion after the write operation is completed

    参数:
    :   - **address** – **\[in\]** write address
        - **pu1\_buf** – **\[in\]** pointer to send data buffer
        - **size** – **\[in\]** send data length
        - **pfn\_cb** – **\[in\]** callback function for async send. it can be NULL if you do not want async send
        - **pv\_arg** – **\[in\]** user give callback parameter

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419bk_flash_read_bytes8uint32_tP7uint8_t8uint32_t19pfunc_bk_flash_cb_tPv"></a>

<a id="_CPPv319bk_flash_read_bytes8uint32_tP7uint8_t8uint32_t19pfunc_bk_flash_cb_tPv"></a> <a id="_CPPv219bk_flash_read_bytes8uint32_tP7uint8_t8uint32_t19pfunc_bk_flash_cb_tPv"></a> <a id="bk_flash_read_bytes__uint32_t.uint8_tP.uint32_t.pfunc_bk_flash_cb_t.voidP"></a> <a id="bk__flash_8h_1a5d3bb16f00caed494190a2a572dfa19f"></a> int32\_t bk\_flash\_read\_bytes(uint32\_t address, uint8\_t \*pu1\_buf, uint32\_t size, [pfunc\_bk\_flash\_cb\_t](#_CPPv419pfunc_bk_flash_cb_t "pfunc_bk_flash_cb_t") pfn\_cb, void \*pv\_arg)
:   flash read data

    flash cmd is 0x20 If pfn\_cb\=\=NULL, flash write operate immediately. exit this funtion after the data operation is completed If pfn\_cb!\=NULL, flash write operate no immediately. Exection pfn\_cb funtion after the data operation is completed

    参数:
    :   - **address** – **\[in\]** read address
        - **pu1\_buf** – **\[in\]** pointer to receive data buffer
        - **size** – **\[in\]** receive data length
        - **pfn\_cb** – **\[in\]** callback function for async send. it can be NULL if you do not want async send
        - **pv\_arg** – **\[in\]** user give callback parameter

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424bk_flash_erase_block_32k8uint32_t19pfunc_bk_flash_cb_tPv"></a>

<a id="_CPPv324bk_flash_erase_block_32k8uint32_t19pfunc_bk_flash_cb_tPv"></a> <a id="_CPPv224bk_flash_erase_block_32k8uint32_t19pfunc_bk_flash_cb_tPv"></a> <a id="bk_flash_erase_block_32k__uint32_t.pfunc_bk_flash_cb_t.voidP"></a> <a id="bk__flash_8h_1af567303a161ec80160c3054a47d1da73"></a> int32\_t bk\_flash\_erase\_block\_32k(uint32\_t address, [pfunc\_bk\_flash\_cb\_t](#_CPPv419pfunc_bk_flash_cb_t "pfunc_bk_flash_cb_t") pfn\_cb, void \*pv\_arg)
:   flash sector erase

    flash cmd is 0x20 If pfn\_cb\=\=NULL, flash write operate immediately. exit this funtion after the erase operation is completed If pfn\_cb!\=NULL, flash write operate no immediately. Exection pfn\_cb funtion after the erase operation is completed

    参数:
    :   - **address** – **\[in\]** erase address
        - **pfn\_cb** – **\[in\]** callback function for async send. it can be NULL if you do not want async send
        - **pv\_arg** – **\[in\]** user give callback parameter

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv418bk_flash_show_infov"></a>

<a id="_CPPv318bk_flash_show_infov"></a> <a id="_CPPv218bk_flash_show_infov"></a> <a id="bk_flash_show_info__void"></a> <a id="bk__flash_8h_1ac66e09501cc96fae03b2c15caf30bb56"></a> void bk\_flash\_show\_info(void)
:   show flash information

    返回:
    :   N/A

<a id="_CPPv426bk_flash_get_max_work_freqv"></a>

<a id="_CPPv326bk_flash_get_max_work_freqv"></a> <a id="_CPPv226bk_flash_get_max_work_freqv"></a> <a id="bk_flash_get_max_work_freq__void"></a> <a id="bk__flash_8h_1a19c4117e44bd3f540cc7f3ee9f1a8b41"></a> uint16\_t bk\_flash\_get\_max\_work\_freq(void)
:   get current flash max work clock in Mhz.

    返回:
    :   max work frequency

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv419pfunc_bk_flash_cb_t"></a>

<a id="_CPPv319pfunc_bk_flash_cb_t"></a> <a id="_CPPv219pfunc_bk_flash_cb_t"></a> <a id="pfunc_bk_flash_cb_t"></a> <a id="bk__flash_8h_1a1de27ec428526f28c515c4fea8d9ad3e"></a> typedef void (\*pfunc\_bk\_flash\_cb\_t)(uint32\_t address, uint8\_t \*pu1\_buf, uint16\_t buf\_len, void \*pv\_arg)
