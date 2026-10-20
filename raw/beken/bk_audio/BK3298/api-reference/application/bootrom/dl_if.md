---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/bootrom/dl_if.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="download-interface"></a>

# Download Interface

<a id="dl-if-api-brief"></a>

## DL\_IF API Brief

| Application | Brief |
| --- | --- |
| [`dl_if_register()`](#_CPPv414dl_if_register7dl_if_eP11dl_if_ops_t "dl_if_register") | Registration download interface |
| [`dl_if_active()`](#_CPPv412dl_if_active7dl_if_e "dl_if_active") | Enable the download interface |
| [`dl_if_byte_avaliable()`](#_CPPv420dl_if_byte_avaliablev "dl_if_byte_avaliable") | Get available bytes |
| [`dl_if_read()`](#_CPPv410dl_if_readP7uint8_t8uint16_t "dl_if_read") | Read data from the download interface |
| [`dl_if_write()`](#_CPPv411dl_if_writeP7uint8_t8uint16_t7uint8_t "dl_if_write") | Write data to the download interface |
| [`dl_if_change_baudrate()`](#_CPPv421dl_if_change_baudrate8uint32_t "dl_if_change_baudrate") | Change the baud rate of the download interface |

<a id="dl-if-api-reference"></a>

## DL\_IF API Reference

<a id="header-file"></a>

### Header File

- [bootrom/dl\_if.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/bootrom/dl_if.h)

<a id="functions"></a>

### Functions

<a id="_CPPv414dl_if_register7dl_if_eP11dl_if_ops_t"></a>

<a id="_CPPv314dl_if_register7dl_if_eP11dl_if_ops_t"></a> <a id="_CPPv214dl_if_register7dl_if_eP11dl_if_ops_t"></a> <a id="dl_if_register__dl_if_e.dl_if_ops_tP"></a> <a id="dl__if_8h_1a36c671977402f809bb624437419e3730"></a> int32\_t dl\_if\_register([dl\_if\_e](#_CPPv47dl_if_e "dl_if_e") e\_if, [dl\_if\_ops\_t](#_CPPv411dl_if_ops_t "dl_if_ops_t") \*pt\_ops)
:   Registration download interface.

    Register the download interface operation structure, pointed to by pt\_ops, to the type specified in e\_if.

    参数:
    :   - **e\_if** – **\[in\]** Type of download interface.
        - **pt\_ops** – **\[in\]** A pointer to the download operation structure that needs to be registered.

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv412dl_if_active7dl_if_e"></a>

<a id="_CPPv312dl_if_active7dl_if_e"></a> <a id="_CPPv212dl_if_active7dl_if_e"></a> <a id="dl_if_active__dl_if_e"></a> <a id="dl__if_8h_1a21e17d8a523aee698b6cd4409b5dce57"></a> int32\_t dl\_if\_active([dl\_if\_e](#_CPPv47dl_if_e "dl_if_e") e\_if)
:   Enable the download interface.

    Enable the download interface operation for the type specified by e\_if.

    参数:
    :   **e\_if** – **\[in\]** Type of download interface.

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420dl_if_byte_avaliablev"></a>

<a id="_CPPv320dl_if_byte_avaliablev"></a> <a id="_CPPv220dl_if_byte_avaliablev"></a> <a id="dl_if_byte_avaliable__void"></a> <a id="dl__if_8h_1a9769ec68263d4f6388a4664ae1d68234"></a> uint32\_t dl\_if\_byte\_avaliable(void)
:   Get available bytes.

    Get the bytes of data that the device has received but has not yet processed.

    返回:
    :   available bytes

<a id="_CPPv410dl_if_readP7uint8_t8uint16_t"></a>

<a id="_CPPv310dl_if_readP7uint8_t8uint16_t"></a> <a id="_CPPv210dl_if_readP7uint8_t8uint16_t"></a> <a id="dl_if_read__uint8_tP.uint16_t"></a> <a id="dl__if_8h_1a679ed2ab542dadb5e57fe35860486f48"></a> uint32\_t dl\_if\_read(uint8\_t \*pu1\_buf, uint16\_t read\_size)
:   Read data from the download interface.

    Read data of size read\_size from the download interface into the buffer pointed to by pu1\_buf.

    参数:
    :   - **pu1\_buf** – **\[in\]** A buffer pointer used for receiving data read from the download interface.
        - **read\_size** – **\[in\]** The size of the data to be read from the download interface.

    返回:
    :   read size

<a id="_CPPv411dl_if_writeP7uint8_t8uint16_t7uint8_t"></a>

<a id="_CPPv311dl_if_writeP7uint8_t8uint16_t7uint8_t"></a> <a id="_CPPv211dl_if_writeP7uint8_t8uint16_t7uint8_t"></a> <a id="dl_if_write__uint8_tP.uint16_t.uint8_t"></a> <a id="dl__if_8h_1ac85aeb1722cd66fcba2d671daf9f9e37"></a> int32\_t dl\_if\_write(uint8\_t \*pu1\_buf, uint16\_t write\_size, uint8\_t cmd)
:   Write data to the download interface.

    Write write\_size bytes of data from the buffer pointed to by pu1\_buf to the download interface.

    参数:
    :   - **pu1\_buf** – **\[in\]** A buffer pointer for the data to be written to the download interface.
        - **write\_size** – **\[in\]** The size of the data to be written to the download interface.
        - **cmd** – **\[in\]** Beken debug command.

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421dl_if_change_baudrate8uint32_t"></a>

<a id="_CPPv321dl_if_change_baudrate8uint32_t"></a> <a id="_CPPv221dl_if_change_baudrate8uint32_t"></a> <a id="dl_if_change_baudrate__uint32_t"></a> <a id="dl__if_8h_1ac56f3cbf1671ab06fc2ae1c8f5770f63"></a> int32\_t dl\_if\_change\_baudrate(uint32\_t baudrate)
:   Change the baud rate of the download interface.

    Change the baud rate of the download interface to baudrate.

    参数:
    :   **baudrate** – **\[in\]** Baud rate setting

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail **DL\_IF\_H** EOF

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv412_dl_if_ops_t"></a>

<a id="_CPPv312_dl_if_ops_t"></a> <a id="_CPPv212_dl_if_ops_t"></a> <a id="_dl_if_ops_t"></a> <a id="struct__dl__if__ops__t"></a> struct \_dl\_if\_ops\_t
:   download interface operations struct definition.

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv47dl_if_e"></a>

<a id="_CPPv37dl_if_e"></a> <a id="_CPPv27dl_if_e"></a> <a id="dl_if_e"></a> <a id="dl__if_8h_1a2edbf0651bb4e3b09a62df28759b1ceb"></a> typedef enum [\_dl\_if\_e](#_CPPv48_dl_if_e "_dl_if_e") dl\_if\_e
:   download interface type definition.

<a id="_CPPv411dl_if_ops_t"></a>

<a id="_CPPv311dl_if_ops_t"></a> <a id="_CPPv211dl_if_ops_t"></a> <a id="dl_if_ops_t"></a> <a id="dl__if_8h_1ac7fdc1dfe40d945cbee293b5587cd307"></a> typedef struct [\_dl\_if\_ops\_t](#_CPPv412_dl_if_ops_t "_dl_if_ops_t") dl\_if\_ops\_t
:   download interface operations struct definition.

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv48_dl_if_e"></a>

<a id="_CPPv38_dl_if_e"></a> <a id="_CPPv28_dl_if_e"></a> <a id="dl__if_8h_1acdb342c03243f81b7276edbd81e43ed3"></a> enum \_dl\_if\_e
:   download interface type definition.

    *Values:*

    <a id="_CPPv4N8_dl_if_e9DLIF_NULLE"></a>

    <a id="_CPPv3N8_dl_if_e9DLIF_NULLE"></a> <a id="_CPPv2N8_dl_if_e9DLIF_NULLE"></a> <a id="dl__if_8h_1acdb342c03243f81b7276edbd81e43ed3a1ddf667d88f0a1b0afaa3893cfc36eae"></a> enumerator DLIF\_NULL

    <a id="_CPPv4N8_dl_if_e9DLIF_UARTE"></a>

    <a id="_CPPv3N8_dl_if_e9DLIF_UARTE"></a> <a id="_CPPv2N8_dl_if_e9DLIF_UARTE"></a> <a id="dl__if_8h_1acdb342c03243f81b7276edbd81e43ed3a2bf17306528edccc9459bdd8ac82b98d"></a> enumerator DLIF\_UART

    <a id="_CPPv4N8_dl_if_e8DLIF_DLPE"></a>

    <a id="_CPPv3N8_dl_if_e8DLIF_DLPE"></a> <a id="_CPPv2N8_dl_if_e8DLIF_DLPE"></a> <a id="dl__if_8h_1acdb342c03243f81b7276edbd81e43ed3adf969c6b72d4551a74f3b7a62db0adf3"></a> enumerator DLIF\_DLP

    <a id="_CPPv4N8_dl_if_e8DLIF_MAXE"></a>

    <a id="_CPPv3N8_dl_if_e8DLIF_MAXE"></a> <a id="_CPPv2N8_dl_if_e8DLIF_MAXE"></a> <a id="dl__if_8h_1acdb342c03243f81b7276edbd81e43ed3a018dfc9bfcd1a9d34d9cad3bdcf6e004"></a> enumerator DLIF\_MAX
