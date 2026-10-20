---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_flashc.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-flashc"></a>

# DRV\_FLASHC

<a id="drv-flashc-api-status"></a>

## DRV\_FLASHC API Status

| API |
| --- |
| [`drv_flashc_reset()`](#_CPPv416drv_flashc_resetv "drv_flashc_reset") |
| [`drv_flashc_read_flash_id()`](#_CPPv424drv_flashc_read_flash_idv "drv_flashc_read_flash_id") |
| [`drv_flashc_set_read_mode()`](#_CPPv424drv_flashc_set_read_mode18flashc_read_mode_e7uint8_t "drv_flashc_set_read_mode") |
| [`drv_flashc_get_line_mode()`](#_CPPv424drv_flashc_get_line_modev "drv_flashc_get_line_mode") |
| [`drv_flashc_erase_sector()`](#_CPPv423drv_flashc_erase_sector8uint32_t "drv_flashc_erase_sector") |
| [`drv_flashc_erase_block_32K()`](#_CPPv426drv_flashc_erase_block_32K8uint32_t "drv_flashc_erase_block_32K") |
| [`drv_flashc_erase_block_64K()`](#_CPPv426drv_flashc_erase_block_64K8uint32_t "drv_flashc_erase_block_64K") |
| [`drv_flashc_erase_chip()`](#_CPPv421drv_flashc_erase_chipv "drv_flashc_erase_chip") |
| [`drv_flashc_deep_power_down()`](#_CPPv426drv_flashc_deep_power_downv "drv_flashc_deep_power_down") |
| [`drv_flashc_release_deep_power_down()`](#_CPPv434drv_flashc_release_deep_power_downv "drv_flashc_release_deep_power_down") |
| [`drv_flashc_read_bytes()`](#_CPPv421drv_flashc_read_bytes8uint32_tP7uint8_t8uint32_t "drv_flashc_read_bytes") |
| [`drv_flashc_write_enable()`](#_CPPv423drv_flashc_write_enablev "drv_flashc_write_enable") |
| [`drv_flashc_write_disable()`](#_CPPv424drv_flashc_write_disablev "drv_flashc_write_disable") |
| [`drv_flashc_write_bytes()`](#_CPPv422drv_flashc_write_bytes8uint32_tPK7uint8_t8uint32_t "drv_flashc_write_bytes") |
| [`drv_flashc_read_status_s0_s7_reg()`](#_CPPv432drv_flashc_read_status_s0_s7_regv "drv_flashc_read_status_s0_s7_reg") |
| [`drv_flashc_read_status_s0_s15_reg()`](#_CPPv433drv_flashc_read_status_s0_s15_regv "drv_flashc_read_status_s0_s15_reg") |
| [`drv_flashc_write_status_s0_s7_reg()`](#_CPPv433drv_flashc_write_status_s0_s7_reg8uint16_t "drv_flashc_write_status_s0_s7_reg") |
| [`drv_flashc_write_status_s0_s15_reg()`](#_CPPv434drv_flashc_write_status_s0_s15_reg8uint16_t "drv_flashc_write_status_s0_s15_reg") |
| [`drv_flashc_set_quadread_cmd()`](#_CPPv427drv_flashc_set_quadread_cmd7uint8_t "drv_flashc_set_quadread_cmd") |
| [`drv_flashc_get_quadread_cmd()`](#_CPPv427drv_flashc_get_quadread_cmdv "drv_flashc_get_quadread_cmd") |
| [`drv_flashc_set_m_value()`](#_CPPv422drv_flashc_set_m_value8uint16_t "drv_flashc_set_m_value") |
| [`drv_flashc_get_m_value()`](#_CPPv422drv_flashc_get_m_valuev "drv_flashc_get_m_value") |

<a id="drv-flashc-api-reference"></a>

## DRV\_FLASHC API Reference

<a id="header-file"></a>

### Header File

- [driver/flashc/drv\_flashc.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/flashc/drv_flashc.h)

<a id="functions"></a>

### Functions

<a id="_CPPv416drv_flashc_resetv"></a>

<a id="_CPPv316drv_flashc_resetv"></a> <a id="_CPPv216drv_flashc_resetv"></a> <a id="drv_flashc_reset__void"></a> <a id="drv__flashc_8h_1acd08dd513a897654f5cade9d8ce866c3"></a> int32\_t drv\_flashc\_reset(void)
:   reset flash

    set 0xff to flash

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424drv_flashc_read_flash_idv"></a>

<a id="_CPPv324drv_flashc_read_flash_idv"></a> <a id="_CPPv224drv_flashc_read_flash_idv"></a> <a id="drv_flashc_read_flash_id__void"></a> <a id="drv__flashc_8h_1aa5b0159970f1945944623ec783a60a6d"></a> uint32\_t drv\_flashc\_read\_flash\_id(void)
:   read flash device id

    返回:
    :   flash id

<a id="_CPPv424drv_flashc_set_read_mode18flashc_read_mode_e7uint8_t"></a>

<a id="_CPPv324drv_flashc_set_read_mode18flashc_read_mode_e7uint8_t"></a> <a id="_CPPv224drv_flashc_set_read_mode18flashc_read_mode_e7uint8_t"></a> <a id="drv_flashc_set_read_mode__flashc_read_mode_e.uint8_t"></a> <a id="drv__flashc_8h_1a85ec6be862a701d3c4c37c9a22006f15"></a> int32\_t drv\_flashc\_set\_read\_mode([flashc\_read\_mode\_e](#_CPPv418flashc_read_mode_e "flashc_read_mode_e") read\_mode, uint8\_t m\_value)
:   set flash controller read line mode

    设置数据读取使用的是几线 2线默认使用的命令是0x03 4线默认使用的命令是0xEB

    参数:
    :   - **read\_mode** – **\[in\]** 参考 flashc\_read\_mode\_e
        - **m\_value** – **\[in\]** 用0xEB与0xBB的线的时候，需要配置此M值,切换成”Continuous Read Mode”

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424drv_flashc_get_line_modev"></a>

<a id="_CPPv324drv_flashc_get_line_modev"></a> <a id="_CPPv224drv_flashc_get_line_modev"></a> <a id="drv_flashc_get_line_mode__void"></a> <a id="drv__flashc_8h_1aa784b2643786b5ddd0828ccb972d3c71"></a> uint8\_t drv\_flashc\_get\_line\_mode(void)
:   get flash controller read line mode

    读取数据使用的是几线

    返回:
    :   line\_mode 参考 flashc\_line\_mode\_e

<a id="_CPPv423drv_flashc_erase_sector8uint32_t"></a>

<a id="_CPPv323drv_flashc_erase_sector8uint32_t"></a> <a id="_CPPv223drv_flashc_erase_sector8uint32_t"></a> <a id="drv_flashc_erase_sector__uint32_t"></a> <a id="drv__flashc_8h_1ac9c3a7a44752441b814a700382e3dcff"></a> int32\_t drv\_flashc\_erase\_sector(uint32\_t address)
:   flash sector erase

    flash擦除命令，发送的flash命令为0x20

    参数:
    :   **address** – **\[in\]** 擦除的首地址

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426drv_flashc_erase_block_32K8uint32_t"></a>

<a id="_CPPv326drv_flashc_erase_block_32K8uint32_t"></a> <a id="_CPPv226drv_flashc_erase_block_32K8uint32_t"></a> <a id="drv_flashc_erase_block_32K__uint32_t"></a> <a id="drv__flashc_8h_1a522932f600ff19e1046d4e3bb97750eb"></a> int32\_t drv\_flashc\_erase\_block\_32K(uint32\_t address)
:   flash erase block 32K

    flash擦除命令，发送的flash命令为0x52

    参数:
    :   **address** – **\[in\]** 擦除的首地址

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426drv_flashc_erase_block_64K8uint32_t"></a>

<a id="_CPPv326drv_flashc_erase_block_64K8uint32_t"></a> <a id="_CPPv226drv_flashc_erase_block_64K8uint32_t"></a> <a id="drv_flashc_erase_block_64K__uint32_t"></a> <a id="drv__flashc_8h_1a7ba5a313d53cc09fb3e4bcc8419f2675"></a> int32\_t drv\_flashc\_erase\_block\_64K(uint32\_t address)
:   flash erase block 64K

    flash擦除命令，发送的flash命令为0xD8

    参数:
    :   **address** – **\[in\]** 擦除的首地址

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421drv_flashc_erase_chipv"></a>

<a id="_CPPv321drv_flashc_erase_chipv"></a> <a id="_CPPv221drv_flashc_erase_chipv"></a> <a id="drv_flashc_erase_chip__void"></a> <a id="drv__flashc_8h_1a60a56c3194efdcfa6c820607435dd50e"></a> int32\_t drv\_flashc\_erase\_chip(void)
:   flash erase chip

    flash擦除命令，发送的flash命令为0xC7

    参数:
    :   **address** – **\[in\]** 擦除的首地址

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426drv_flashc_deep_power_downv"></a>

<a id="_CPPv326drv_flashc_deep_power_downv"></a> <a id="_CPPv226drv_flashc_deep_power_downv"></a> <a id="drv_flashc_deep_power_down__void"></a> <a id="drv__flashc_8h_1a4c651113edbf07c41cd7feecf9fdf40f"></a> int32\_t drv\_flashc\_deep\_power\_down(void)
:   deep power down

    发送的flash命令为0xB9

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv434drv_flashc_release_deep_power_downv"></a>

<a id="_CPPv334drv_flashc_release_deep_power_downv"></a> <a id="_CPPv234drv_flashc_release_deep_power_downv"></a> <a id="drv_flashc_release_deep_power_down__void"></a> <a id="drv__flashc_8h_1a7bb3ed44dbe3dd521379966e33a21895"></a> int32\_t drv\_flashc\_release\_deep\_power\_down(void)
:   release deep power down

    发送的flash命令为0xAB

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421drv_flashc_read_bytes8uint32_tP7uint8_t8uint32_t"></a>

<a id="_CPPv321drv_flashc_read_bytes8uint32_tP7uint8_t8uint32_t"></a> <a id="_CPPv221drv_flashc_read_bytes8uint32_tP7uint8_t8uint32_t"></a> <a id="drv_flashc_read_bytes__uint32_t.uint8_tP.uint32_t"></a> <a id="drv__flashc_8h_1ae90e56df24c77801abb69481c78ce539"></a> int32\_t drv\_flashc\_read\_bytes(uint32\_t address, uint8\_t \*pu1\_buf, uint32\_t size)
:   flash read data

    软件方式向flash中写数据

    参数:
    :   - **address** – **\[in\]** 读数据的目标地址的首地址
        - **pu1\_buf** – **\[in\]** 数据指针
        - **size** – **\[in\]** 数据大小，bytes。小于等于32

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv423drv_flashc_write_enablev"></a>

<a id="_CPPv323drv_flashc_write_enablev"></a> <a id="_CPPv223drv_flashc_write_enablev"></a> <a id="drv_flashc_write_enable__void"></a> <a id="drv__flashc_8h_1abced210db7715f93177c1a90c60ada6e"></a> int32\_t drv\_flashc\_write\_enable(void)
:   flash write enable

    发送0x06命令

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424drv_flashc_write_disablev"></a>

<a id="_CPPv324drv_flashc_write_disablev"></a> <a id="_CPPv224drv_flashc_write_disablev"></a> <a id="drv_flashc_write_disable__void"></a> <a id="drv__flashc_8h_1a788ed73b9c963a815fea8fcb5eb9317f"></a> int32\_t drv\_flashc\_write\_disable(void)
:   flash write disable

    发送0x06命令

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422drv_flashc_write_bytes8uint32_tPK7uint8_t8uint32_t"></a>

<a id="_CPPv322drv_flashc_write_bytes8uint32_tPK7uint8_t8uint32_t"></a> <a id="_CPPv222drv_flashc_write_bytes8uint32_tPK7uint8_t8uint32_t"></a> <a id="drv_flashc_write_bytes__uint32_t.uint8_tCP.uint32_t"></a> <a id="drv__flashc_8h_1ac25387bec44d35ba1cc96008e401fe2e"></a> int32\_t drv\_flashc\_write\_bytes(uint32\_t address, const uint8\_t \*pu1\_buf, uint32\_t size)
:   flash write data

    软件方式向flash中写数据

    参数:
    :   - **address** – **\[in\]** 写数据的目标地址的首地址
        - **pu1\_buf** – **\[in\]** 数据指针
        - **size** – **\[in\]** 数据大小，bytes

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv432drv_flashc_read_status_s0_s7_regv"></a>

<a id="_CPPv332drv_flashc_read_status_s0_s7_regv"></a> <a id="_CPPv232drv_flashc_read_status_s0_s7_regv"></a> <a id="drv_flashc_read_status_s0_s7_reg__void"></a> <a id="drv__flashc_8h_1a02ffa95dc3141e84ac1634f90d6dadbe"></a> uint16\_t drv\_flashc\_read\_status\_s0\_s7\_reg(void)
:   read flash low 8bits register

    发送0x05命令读取寄存器S0\~S7

    返回:
    :   寄存器S0\~S7值

<a id="_CPPv433drv_flashc_read_status_s0_s15_regv"></a>

<a id="_CPPv333drv_flashc_read_status_s0_s15_regv"></a> <a id="_CPPv233drv_flashc_read_status_s0_s15_regv"></a> <a id="drv_flashc_read_status_s0_s15_reg__void"></a> <a id="drv__flashc_8h_1ac6af2c8ae56cf63b9d48ee0779590f61"></a> uint16\_t drv\_flashc\_read\_status\_s0\_s15\_reg(void)
:   read flash low 16bits register

    （1）发送0x05命令读取寄存器S0\~S7 （2）发送0x35命令读取寄存器S8\~S15

    返回:
    :   寄存器S0\~S7值

<a id="_CPPv433drv_flashc_write_status_s0_s7_reg8uint16_t"></a>

<a id="_CPPv333drv_flashc_write_status_s0_s7_reg8uint16_t"></a> <a id="_CPPv233drv_flashc_write_status_s0_s7_reg8uint16_t"></a> <a id="drv_flashc_write_status_s0_s7_reg__uint16_t"></a> <a id="drv__flashc_8h_1a82c7687fd043b19785957f689e6430bd"></a> int32\_t drv\_flashc\_write\_status\_s0\_s7\_reg(uint16\_t status\_reg\_data)
:   read flash low 8bits register

    发送0x01命令写寄存器S0\~S7

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv434drv_flashc_write_status_s0_s15_reg8uint16_t"></a>

<a id="_CPPv334drv_flashc_write_status_s0_s15_reg8uint16_t"></a> <a id="_CPPv234drv_flashc_write_status_s0_s15_reg8uint16_t"></a> <a id="drv_flashc_write_status_s0_s15_reg__uint16_t"></a> <a id="drv__flashc_8h_1ab8519d043d52662e7d4366d7d3cc20a2"></a> int32\_t drv\_flashc\_write\_status\_s0\_s15\_reg(uint16\_t status\_reg\_data)
:   read flash low 16bits register

    发送0x01命令写寄存器S0\~S15

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427drv_flashc_set_quadread_cmd7uint8_t"></a>

<a id="_CPPv327drv_flashc_set_quadread_cmd7uint8_t"></a> <a id="_CPPv227drv_flashc_set_quadread_cmd7uint8_t"></a> <a id="drv_flashc_set_quadread_cmd__uint8_t"></a> <a id="drv__flashc_8h_1a5d6fd4b86dfc19a2355b79fe591047d2"></a> int32\_t drv\_flashc\_set\_quadread\_cmd(uint8\_t modesel)

<a id="_CPPv427drv_flashc_get_quadread_cmdv"></a>

<a id="_CPPv327drv_flashc_get_quadread_cmdv"></a> <a id="_CPPv227drv_flashc_get_quadread_cmdv"></a> <a id="drv_flashc_get_quadread_cmd__void"></a> <a id="drv__flashc_8h_1a1fe6270737762b30b29411f2c54a9dee"></a> uint8\_t drv\_flashc\_get\_quadread\_cmd(void)
:   get cmd use for 4 line

    获取4线模式下与flash通信的命令

    返回:
    :   mode 0:0xEB; 1:0xE7

<a id="_CPPv422drv_flashc_set_m_value8uint16_t"></a>

<a id="_CPPv322drv_flashc_set_m_value8uint16_t"></a> <a id="_CPPv222drv_flashc_set_m_value8uint16_t"></a> <a id="drv_flashc_set_m_value__uint16_t"></a> <a id="drv__flashc_8h_1a89d9a43ee168ce8aadc01ad4f562a1dd"></a> int32\_t drv\_flashc\_set\_m\_value(uint16\_t value)

<a id="_CPPv422drv_flashc_get_m_valuev"></a>

<a id="_CPPv322drv_flashc_get_m_valuev"></a> <a id="_CPPv222drv_flashc_get_m_valuev"></a> <a id="drv_flashc_get_m_value__void"></a> <a id="drv__flashc_8h_1afcb871ab5064d1548e8421df74052ec3"></a> uint8\_t drv\_flashc\_get\_m\_value(void)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv418flashc_read_mode_e"></a>

<a id="_CPPv318flashc_read_mode_e"></a> <a id="_CPPv218flashc_read_mode_e"></a> <a id="drv__flashc_8h_1a98cd358a75ede201f22bea0a5e6a52b6"></a> enum flashc\_read\_mode\_e
:   *Values:*

    <a id="_CPPv4N18flashc_read_mode_e22FLASHC_STD_RD_CMD_0x03E"></a>

    <a id="_CPPv3N18flashc_read_mode_e22FLASHC_STD_RD_CMD_0x03E"></a> <a id="_CPPv2N18flashc_read_mode_e22FLASHC_STD_RD_CMD_0x03E"></a> <a id="drv__flashc_8h_1a98cd358a75ede201f22bea0a5e6a52b6a5f4a453eef90fbad3d7d26c2fb53668b"></a> enumerator FLASHC\_STD\_RD\_CMD\_0x03
    :   flash standard read

    <a id="_CPPv4N18flashc_read_mode_e23FLASHC_DUAL_RD_CMD_0x3BE"></a>

    <a id="_CPPv3N18flashc_read_mode_e23FLASHC_DUAL_RD_CMD_0x3BE"></a> <a id="_CPPv2N18flashc_read_mode_e23FLASHC_DUAL_RD_CMD_0x3BE"></a> <a id="drv__flashc_8h_1a98cd358a75ede201f22bea0a5e6a52b6a089a5ff964474766e715c0544e78ea30"></a> enumerator FLASHC\_DUAL\_RD\_CMD\_0x3B
    :   flash dual read

    <a id="_CPPv4N18flashc_read_mode_e23FLASHC_DUAL_RD_CMD_0xBBE"></a>

    <a id="_CPPv3N18flashc_read_mode_e23FLASHC_DUAL_RD_CMD_0xBBE"></a> <a id="_CPPv2N18flashc_read_mode_e23FLASHC_DUAL_RD_CMD_0xBBE"></a> <a id="drv__flashc_8h_1a98cd358a75ede201f22bea0a5e6a52b6a4eccd1feb33268735a196abf88b8954c"></a> enumerator FLASHC\_DUAL\_RD\_CMD\_0xBB
    :   flash dual read

    <a id="_CPPv4N18flashc_read_mode_e23FLASHC_QUAL_RD_CMD_0xEBE"></a>

    <a id="_CPPv3N18flashc_read_mode_e23FLASHC_QUAL_RD_CMD_0xEBE"></a> <a id="_CPPv2N18flashc_read_mode_e23FLASHC_QUAL_RD_CMD_0xEBE"></a> <a id="drv__flashc_8h_1a98cd358a75ede201f22bea0a5e6a52b6a9be4bd55935f5b9756921e07df00dc2e"></a> enumerator FLASHC\_QUAL\_RD\_CMD\_0xEB
    :   flash qual read
