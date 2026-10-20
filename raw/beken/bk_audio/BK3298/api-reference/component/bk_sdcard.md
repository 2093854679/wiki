---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/component/bk_sdcard.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk-sdcard"></a>

# BK\_SDCARD

<a id="bk-sdcard-api-status"></a>

## BK\_SDCARD API Status

| API |
| --- |
| [`bk_sdcard_init()`](#_CPPv414bk_sdcard_initv "bk_sdcard_init") |
| [`bk_sdcard_deinit()`](#_CPPv416bk_sdcard_deinitv "bk_sdcard_deinit") |
| [`bk_sdcard_write_blocks()`](#_CPPv422bk_sdcard_write_blocksPK7uint8_t8uint32_t8uint32_t "bk_sdcard_write_blocks") |
| [`bk_sdcard_read_blocks()`](#_CPPv421bk_sdcard_read_blocksP7uint8_t8uint32_t8uint32_t "bk_sdcard_read_blocks") |
| [`bk_sdcard_erase()`](#_CPPv415bk_sdcard_erase8uint32_t8uint32_t "bk_sdcard_erase") |
| [`bk_sdcard_get_card_state()`](#_CPPv424bk_sdcard_get_card_statev "bk_sdcard_get_card_state") |
| [`bk_sdcard_get_card_size()`](#_CPPv423bk_sdcard_get_card_sizev "bk_sdcard_get_card_size") |
| [`bk_sdcard_get_card_info()`](#_CPPv423bk_sdcard_get_card_infoP13sdcard_info_t "bk_sdcard_get_card_info") |

<a id="bk-sdcard-api-reference"></a>

## BK\_SDCARD API Reference

<a id="header-file"></a>

### Header File

- [component/sdcard/bk\_sdcard.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/component/sdcard/bk_sdcard.h)

<a id="functions"></a>

### Functions

<a id="_CPPv414bk_sdcard_initv"></a>

<a id="_CPPv314bk_sdcard_initv"></a> <a id="_CPPv214bk_sdcard_initv"></a> <a id="bk_sdcard_init__void"></a> <a id="bk__sdcard_8h_1a77ba80693849d77125bbaa8a0d0228e6"></a> int32\_t bk\_sdcard\_init(void)
:   Initializes the sd card.

    This API init the sd card:

    - Initialize SDIO peripheral interface with default configuration
    - Identify card operating voltage
    - Card initialization
    - Set block size for card

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416bk_sdcard_deinitv"></a>

<a id="_CPPv316bk_sdcard_deinitv"></a> <a id="_CPPv216bk_sdcard_deinitv"></a> <a id="bk_sdcard_deinit__void"></a> <a id="bk__sdcard_8h_1a717eee68db270f2933902fd75aaa9afe"></a> int32\_t bk\_sdcard\_deinit(void)
:   Deinit the sd card.

    This API deinit the sdio card:

    - sdio host deinit
    - free related software resource

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422bk_sdcard_write_blocksPK7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv322bk_sdcard_write_blocksPK7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv222bk_sdcard_write_blocksPK7uint8_t8uint32_t8uint32_t"></a> <a id="bk_sdcard_write_blocks__uint8_tCP.uint32_t.uint32_t"></a> <a id="bk__sdcard_8h_1a837e24c11c01c322bc78439075244ed5"></a> int32\_t bk\_sdcard\_write\_blocks(const uint8\_t \*data, uint32\_t block\_addr, uint32\_t block\_num)
:   Write block(s) to a specified address in a card. The data transfer is managed by blocking mode.

    参数:
    :   - **data** – **\[in\]** data pointer to the buffer
        - **block\_addr** – **\[in\]** block\_addr block address where data will be written
        - **block\_num** – **\[in\]** block\_num number of sd blocks to write

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421bk_sdcard_read_blocksP7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv321bk_sdcard_read_blocksP7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv221bk_sdcard_read_blocksP7uint8_t8uint32_t8uint32_t"></a> <a id="bk_sdcard_read_blocks__uint8_tP.uint32_t.uint32_t"></a> <a id="bk__sdcard_8h_1a93fd8815bbaf41a74a7e70d48b47db0a"></a> int32\_t bk\_sdcard\_read\_blocks(uint8\_t \*data, uint32\_t block\_addr, uint32\_t block\_num)
:   Read block(s) from a specified address in a card. The data transfer is managed by blocking mode.

    参数:
    :   - **data** – **\[in\]** data pointer to the buffer
        - **block\_addr** – **\[in\]** block\_addr block address where data will be written
        - **block\_num** – **\[in\]** block\_num number of sd blocks to write

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv415bk_sdcard_erase8uint32_t8uint32_t"></a>

<a id="_CPPv315bk_sdcard_erase8uint32_t8uint32_t"></a> <a id="_CPPv215bk_sdcard_erase8uint32_t8uint32_t"></a> <a id="bk_sdcard_erase__uint32_t.uint32_t"></a> <a id="bk__sdcard_8h_1a077b8bab9c58f1f91b5307ecf11cc1da"></a> int32\_t bk\_sdcard\_erase(uint32\_t start\_block\_addr, uint32\_t end\_block\_addr)
:   Erase the specified memory area of the given sd card.

    详细描述部分，可提供必要的技术细节

    参数:
    :   - **start\_block\_addr** – **\[in\]** start\_block\_addr start block address
        - **end\_block\_addr** – **\[in\]** end\_block\_addr end block address

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424bk_sdcard_get_card_statev"></a>

<a id="_CPPv324bk_sdcard_get_card_statev"></a> <a id="_CPPv224bk_sdcard_get_card_statev"></a> <a id="bk_sdcard_get_card_state__void"></a> <a id="bk__sdcard_8h_1aef4cc6444b2ac17f279761652ca8af52"></a> [sdcard\_state\_e](#_CPPv414sdcard_state_e "sdcard_state_e") bk\_sdcard\_get\_card\_state(void)
:   Get the current sd card data state.

    返回:
    :   card state

<a id="_CPPv423bk_sdcard_get_card_sizev"></a>

<a id="_CPPv323bk_sdcard_get_card_sizev"></a> <a id="_CPPv223bk_sdcard_get_card_sizev"></a> <a id="bk_sdcard_get_card_size__void"></a> <a id="bk__sdcard_8h_1a50b032c6123245f83417add7e76d97fb"></a> uint32\_t bk\_sdcard\_get\_card\_size(void)
:   Get the sd card size which unit is sector size(512Bytes) Compute the sd card size which base on card\_info.csd.

    返回:
    :   - \>0: card size
        - 0: errors.

<a id="_CPPv423bk_sdcard_get_card_infoP13sdcard_info_t"></a>

<a id="_CPPv323bk_sdcard_get_card_infoP13sdcard_info_t"></a> <a id="_CPPv223bk_sdcard_get_card_infoP13sdcard_info_t"></a> <a id="bk_sdcard_get_card_info__sdcard_info_tP"></a> <a id="bk__sdcard_8h_1a877e65e15205a35941d0b3a7bad6d96a"></a> int32\_t bk\_sdcard\_get\_card\_info([sdcard\_info\_t](#_CPPv413sdcard_info_t "sdcard_info_t") \*card\_info)
:   Get the sd card info.

    参数:
    :   **card\_info** – **\[in\]** card\_info pointer to the sd\_card\_info\_t structure that will contains the sd card status information

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv413sdcard_info_t"></a>

<a id="_CPPv313sdcard_info_t"></a> <a id="_CPPv213sdcard_info_t"></a> <a id="sdcard_info_t"></a> <a id="structsdcard__info__t"></a> struct sdcard\_info\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N13sdcard_info_t12card_versionE"></a>

    <a id="_CPPv3N13sdcard_info_t12card_versionE"></a> <a id="_CPPv2N13sdcard_info_t12card_versionE"></a> <a id="sdcard_info_t::card_version__uint32_t"></a> <a id="structsdcard__info__t_1ae71cbd1c974ea80742fde063cad9c5d6"></a> uint32\_t card\_version
    :   the card version

    <a id="_CPPv4N13sdcard_info_t9card_typeE"></a>

    <a id="_CPPv3N13sdcard_info_t9card_typeE"></a> <a id="_CPPv2N13sdcard_info_t9card_typeE"></a> <a id="sdcard_info_t::card_type__uint32_t"></a> <a id="structsdcard__info__t_1ad756fc38a5ca7f425eff8cc901313aaa"></a> uint32\_t card\_type
    :   the card version(SDSC/SDHC/SDXC)

    <a id="_CPPv4N13sdcard_info_t11class_valueE"></a>

    <a id="_CPPv3N13sdcard_info_t11class_valueE"></a> <a id="_CPPv2N13sdcard_info_t11class_valueE"></a> <a id="sdcard_info_t::class_value__uint32_t"></a> <a id="structsdcard__info__t_1ab1f56ccd4d6237233d69a8b8cf88c80a"></a> uint32\_t class\_value
    :   the class of card class

    <a id="_CPPv4N13sdcard_info_t18relative_card_addrE"></a>

    <a id="_CPPv3N13sdcard_info_t18relative_card_addrE"></a> <a id="_CPPv2N13sdcard_info_t18relative_card_addrE"></a> <a id="sdcard_info_t::relative_card_addr__uint32_t"></a> <a id="structsdcard__info__t_1a30acba897f546adea78bb597ce67a99d"></a> uint32\_t relative\_card\_addr
    :   the relaive card address

<a id="_CPPv412sdcard_csd_t"></a>

<a id="_CPPv312sdcard_csd_t"></a> <a id="_CPPv212sdcard_csd_t"></a> <a id="sdcard_csd_t"></a> <a id="structsdcard__csd__t"></a> struct sdcard\_csd\_t
:   the sdcard csd info. \<\<Part1\_Physical\_Layer\_Simplified\_Specification\_Ver7.10\>\> CSD registers are tranferred by SDIO sequence is bit\[127:96\],bit\[95:64\],bit\[63:32\],bit\[31:0\]

<a id="macros"></a>

### Macros

<a id="c.SDCARD_V1_X"></a>

<a id="bk__sdcard_8h_1a2356108702ebe73fc2b9ea033dbf1853"></a> SDCARD\_V1\_X

<a id="c.SDCARD_V2_X"></a>

<a id="bk__sdcard_8h_1a2a735a99037a8086b5f8146dd14f9c1f"></a> SDCARD\_V2\_X

<a id="c.SD_CARD_TYPE_SDSC"></a>

<a id="bk__sdcard_8h_1a7b725b074ff5e5b32e37e8345a2b871a"></a> SD\_CARD\_TYPE\_SDSC

<a id="c.SD_CARD_TYPE_SDHC_SDXC"></a>

<a id="bk__sdcard_8h_1aaeaa404586daf8c3ed63031abdd4fbbb"></a> SD\_CARD\_TYPE\_SDHC\_SDXC

<a id="c.SD_SUPPORT_BASIC_CMD"></a>

<a id="bk__sdcard_8h_1a05303c1b94ee7c12c68fa244d733f76c"></a> SD\_SUPPORT\_BASIC\_CMD

<a id="c.SD_SUPPORT_RESERVED_0_CMD"></a>

<a id="bk__sdcard_8h_1adda3538c093741da3a42b642513f66ea"></a> SD\_SUPPORT\_RESERVED\_0\_CMD

<a id="c.SD_SUPPORT_BLOCK_READ_CMD"></a>

<a id="bk__sdcard_8h_1a219567ca73291d93956913f6576bd591"></a> SD\_SUPPORT\_BLOCK\_READ\_CMD

<a id="c.SD_SUPPORT_RESERVED_1_CMD"></a>

<a id="bk__sdcard_8h_1adb198122b9a80a1f01f2c04ecacaddcd"></a> SD\_SUPPORT\_RESERVED\_1\_CMD

<a id="c.SD_SUPPORT_BLOCK_WRITE_CMD"></a>

<a id="bk__sdcard_8h_1a958d547340149e98319860c48eb73cdf"></a> SD\_SUPPORT\_BLOCK\_WRITE\_CMD

<a id="c.SD_SUPPORT_ERASE_CMD"></a>

<a id="bk__sdcard_8h_1af876341c70214425dfba0a96987967c1"></a> SD\_SUPPORT\_ERASE\_CMD

<a id="c.SD_SUPPORT_WRITE_PROTECTION_CMD"></a>

<a id="bk__sdcard_8h_1a288fd5f4a6f2cbbce7d5b4d882e26f7e"></a> SD\_SUPPORT\_WRITE\_PROTECTION\_CMD

<a id="c.SD_SUPPORT_LOCK_CARD_CMD"></a>

<a id="bk__sdcard_8h_1a2511466e0e899f4b0bd3a388eedd3276"></a> SD\_SUPPORT\_LOCK\_CARD\_CMD

<a id="c.SD_SUPPORT_APPLICATION_CMD"></a>

<a id="bk__sdcard_8h_1ad3556c360663ad05c20d8410ec444871"></a> SD\_SUPPORT\_APPLICATION\_CMD

<a id="c.SD_SUPPORT_RESERVED_2_CMD"></a>

<a id="bk__sdcard_8h_1a0348cb840fac39880b9fa00420474fde"></a> SD\_SUPPORT\_RESERVED\_2\_CMD

<a id="c.SD_BLOCK_SIZE"></a>

<a id="bk__sdcard_8h_1a451aeffb68f3ecfb82eae03c88e9e48c"></a> SD\_BLOCK\_SIZE

<a id="c.SD_CHECK_PATTERN"></a>

<a id="bk__sdcard_8h_1ac37389a0323f1a04aec2b59c905f0f6a"></a> SD\_CHECK\_PATTERN

<a id="c.SD_OCR_BUSY"></a>

<a id="bk__sdcard_8h_1ab3ed1c9973a3c36b666d2994763096a8"></a> SD\_OCR\_BUSY

<a id="c.SD_OCR_HIGH_CAPACITY"></a>

<a id="bk__sdcard_8h_1aedae687596ca0fa079a87bef7909163d"></a> SD\_OCR\_HIGH\_CAPACITY

<a id="c.SD_OCR_VOLTAGE_3_2V_3_3V"></a>

<a id="bk__sdcard_8h_1a26c4f497657c4bbf634390749f8a8c4b"></a> SD\_OCR\_VOLTAGE\_3\_2V\_3\_3V

<a id="c.SD_OCR_VOLTAGE_ALL"></a>

<a id="bk__sdcard_8h_1a918efc1ae0248a5d2cc500f9af03c3fe"></a> SD\_OCR\_VOLTAGE\_ALL

<a id="c.SD_DEFAULT_OCR"></a>

<a id="bk__sdcard_8h_1ae92b69a299f6ca949964e36954d877fd"></a> SD\_DEFAULT\_OCR

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv414sdcard_state_e"></a>

<a id="_CPPv314sdcard_state_e"></a> <a id="_CPPv214sdcard_state_e"></a> <a id="bk__sdcard_8h_1a3911a4d248459b8d83036ecad5ce04b8"></a> enum sdcard\_state\_e
:   current state of card status, refer to Card Status BIT\[12:9\]

    *Values:*

    <a id="_CPPv4N14sdcard_state_e11SDCARD_IDLEE"></a>

    <a id="_CPPv3N14sdcard_state_e11SDCARD_IDLEE"></a> <a id="_CPPv2N14sdcard_state_e11SDCARD_IDLEE"></a> <a id="bk__sdcard_8h_1a3911a4d248459b8d83036ecad5ce04b8a5c3b13ebd186bfb920adbc712241a784"></a> enumerator SDCARD\_IDLE
    :   card state is idle

    <a id="_CPPv4N14sdcard_state_e12SDCARD_READYE"></a>

    <a id="_CPPv3N14sdcard_state_e12SDCARD_READYE"></a> <a id="_CPPv2N14sdcard_state_e12SDCARD_READYE"></a> <a id="bk__sdcard_8h_1a3911a4d248459b8d83036ecad5ce04b8a5e70f2336d91ad7c16cecd1c79c2fbb1"></a> enumerator SDCARD\_READY
    :   card state is ready

    <a id="_CPPv4N14sdcard_state_e21SDCARD_IDENTIFICATIONE"></a>

    <a id="_CPPv3N14sdcard_state_e21SDCARD_IDENTIFICATIONE"></a> <a id="_CPPv2N14sdcard_state_e21SDCARD_IDENTIFICATIONE"></a> <a id="bk__sdcard_8h_1a3911a4d248459b8d83036ecad5ce04b8a522c4d1c30551c50b0c219d8b1b398bf"></a> enumerator SDCARD\_IDENTIFICATION
    :   card is in identification state

    <a id="_CPPv4N14sdcard_state_e14SDCARD_STANDBYE"></a>

    <a id="_CPPv3N14sdcard_state_e14SDCARD_STANDBYE"></a> <a id="_CPPv2N14sdcard_state_e14SDCARD_STANDBYE"></a> <a id="bk__sdcard_8h_1a3911a4d248459b8d83036ecad5ce04b8af8001879b13ab00e01aa441aeb98c1f5"></a> enumerator SDCARD\_STANDBY
    :   card is in standby state

    <a id="_CPPv4N14sdcard_state_e15SDCARD_TRANSFERE"></a>

    <a id="_CPPv3N14sdcard_state_e15SDCARD_TRANSFERE"></a> <a id="_CPPv2N14sdcard_state_e15SDCARD_TRANSFERE"></a> <a id="bk__sdcard_8h_1a3911a4d248459b8d83036ecad5ce04b8ac78499d5779eac555eda32c49233b07d"></a> enumerator SDCARD\_TRANSFER
    :   card is in transfer state

    <a id="_CPPv4N14sdcard_state_e14SDCARD_SENDINGE"></a>

    <a id="_CPPv3N14sdcard_state_e14SDCARD_SENDINGE"></a> <a id="_CPPv2N14sdcard_state_e14SDCARD_SENDINGE"></a> <a id="bk__sdcard_8h_1a3911a4d248459b8d83036ecad5ce04b8a295317b6205f63f4de457dd69688bd57"></a> enumerator SDCARD\_SENDING
    :   card is sending an operation

    <a id="_CPPv4N14sdcard_state_e16SDCARD_RECEIVINGE"></a>

    <a id="_CPPv3N14sdcard_state_e16SDCARD_RECEIVINGE"></a> <a id="_CPPv2N14sdcard_state_e16SDCARD_RECEIVINGE"></a> <a id="bk__sdcard_8h_1a3911a4d248459b8d83036ecad5ce04b8ad497a0b8eba0f00e5154cb3ca40ce308"></a> enumerator SDCARD\_RECEIVING
    :   card is receiving operation information

    <a id="_CPPv4N14sdcard_state_e18SDCARD_PROGRAMMINGE"></a>

    <a id="_CPPv3N14sdcard_state_e18SDCARD_PROGRAMMINGE"></a> <a id="_CPPv2N14sdcard_state_e18SDCARD_PROGRAMMINGE"></a> <a id="bk__sdcard_8h_1a3911a4d248459b8d83036ecad5ce04b8a24125349e4f90fc7b286a59dcb5eb3e7"></a> enumerator SDCARD\_PROGRAMMING
    :   card is in programming state

    <a id="_CPPv4N14sdcard_state_e19SDCARD_DISCONNECTEDE"></a>

    <a id="_CPPv3N14sdcard_state_e19SDCARD_DISCONNECTEDE"></a> <a id="_CPPv2N14sdcard_state_e19SDCARD_DISCONNECTEDE"></a> <a id="bk__sdcard_8h_1a3911a4d248459b8d83036ecad5ce04b8aa4a633259c60095d4b95c725783a5b7f"></a> enumerator SDCARD\_DISCONNECTED
    :   card is disconnected

    <a id="_CPPv4N14sdcard_state_e12SDCARD_ERRORE"></a>

    <a id="_CPPv3N14sdcard_state_e12SDCARD_ERRORE"></a> <a id="_CPPv2N14sdcard_state_e12SDCARD_ERRORE"></a> <a id="bk__sdcard_8h_1a3911a4d248459b8d83036ecad5ce04b8a914c51854ee6be3fbcd43ba4e101c692"></a> enumerator SDCARD\_ERROR
