---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_env/app_tlv.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="tlv-application-functions"></a>

# TLV Application Functions

<a id="app-tlv-api-brief"></a>

## APP\_TLV API Brief

| Application | Brief |
| --- | --- |
| [`app_tlv_get_data()`](#_CPPv416app_tlv_get_dataP7uint8_t7uint8_t "app_tlv_get_data") | used TLV data format get data from flash |
| [`app_tlv_check_data_chip_magic()`](#_CPPv429app_tlv_check_data_chip_magicP7uint8_t7uint8_t "app_tlv_check_data_chip_magic") | check chip magic data from flash to identify tlv data valid or not |
| [`app_tlv_read_flash_data()`](#_CPPv423app_tlv_read_flash_data7uint8_tP7uint8_t8uint32_t8uint32_t "app_tlv_read_flash_data") | Read app\_env data partition from flash |

<a id="app-tlv-api-reference"></a>

## APP\_TLV API Reference

<a id="header-file"></a>

### Header File

- [common/app\_env/app\_tlv.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_env/app_tlv.h)

<a id="functions"></a>

### Functions

<a id="_CPPv416app_tlv_get_dataP7uint8_t7uint8_t"></a>

<a id="_CPPv316app_tlv_get_dataP7uint8_t7uint8_t"></a> <a id="_CPPv216app_tlv_get_dataP7uint8_t7uint8_t"></a> <a id="app_tlv_get_data__uint8_tP.uint8_t"></a> <a id="app__tlv_8h_1aa8cd220ce7d31af6a3b0670c653c353b"></a> void app\_tlv\_get\_data(uint8\_t \*pos, uint8\_t encrypt)
:   app\_tlv\_get\_data brief description

    execute read flash data with the specified position

    参数:
    :   - **pos** – **\[in\]** start address for reading flash data
        - **encrypt** – **\[in\]** enable encrypt or not

    返回:
    :   N/A

<a id="_CPPv429app_tlv_check_data_chip_magicP7uint8_t7uint8_t"></a>

<a id="_CPPv329app_tlv_check_data_chip_magicP7uint8_t7uint8_t"></a> <a id="_CPPv229app_tlv_check_data_chip_magicP7uint8_t7uint8_t"></a> <a id="app_tlv_check_data_chip_magic__uint8_tP.uint8_t"></a> <a id="app__tlv_8h_1a29ad2ffd5d03d0bc8b9ce12712bbf042"></a> uint32\_t app\_tlv\_check\_data\_chip\_magic(uint8\_t \*p\_chip\_magic, uint8\_t encrypt)
:   app\_tlv\_check\_data\_chip\_magic brief description

    compare flash data header with magic words. If the results are the same, data is valid

    参数:
    :   - **p\_chip\_magic** – **\[in\]** data buffer for magic words
        - **encrypt** – **\[in\]** enable encrypt or not

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv423app_tlv_read_flash_data7uint8_tP7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv323app_tlv_read_flash_data7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv223app_tlv_read_flash_data7uint8_tP7uint8_t8uint32_t8uint32_t"></a> <a id="app_tlv_read_flash_data__uint8_t.uint8_tP.uint32_t.uint32_t"></a> <a id="app__tlv_8h_1a6c18d8dd95aa75fd73ef4096582bddea"></a> void app\_tlv\_read\_flash\_data(uint8\_t encrypt, uint8\_t \*p\_dst, uint32\_t flash\_addr, uint32\_t read\_len)
:   app\_tlv\_read\_flash\_data brief description

    get the specified data form flash with starting address and length

    参数:
    :   - **encrypt** – **\[in\]** enable encrypt or not @APP\_ENV\_FLASH\_ENCRYPT
        - **p\_dst** – **\[out\]** data buffer for read from flash
        - **flash\_addr** – **\[in\]** starting address
        - **read\_len** – **\[in\]** read len

    返回:
    :   N/A

<a id="structures"></a>

### Structures

<a id="_CPPv47TLV_TAG"></a>

<a id="_CPPv37TLV_TAG"></a> <a id="_CPPv27TLV_TAG"></a> <a id="TLV_TAG"></a> <a id="structTLV__TAG"></a> struct TLV\_TAG
:   TLV tag data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N7TLV_TAG4typeE"></a>

    <a id="_CPPv3N7TLV_TAG4typeE"></a> <a id="_CPPv2N7TLV_TAG4typeE"></a> <a id="TLV_TAG::type__uint16_t"></a> <a id="structTLV__TAG_1a117fe76b1f0dbec3102408048a8ef91c"></a> uint16\_t type
    :   TLV type @TLV\_TYPE

    <a id="_CPPv4N7TLV_TAG3lenE"></a>

    <a id="_CPPv3N7TLV_TAG3lenE"></a> <a id="_CPPv2N7TLV_TAG3lenE"></a> <a id="TLV_TAG::len__uint16_t"></a> <a id="structTLV__TAG_1a95d7b88a9f8c77ae63469de447045d1a"></a> uint16\_t len
    :   len of value

    <a id="_CPPv4N7TLV_TAG5valueE"></a>

    <a id="_CPPv3N7TLV_TAG5valueE"></a> <a id="_CPPv2N7TLV_TAG5valueE"></a> <a id="TLV_TAG::value__uint8_tA"></a> <a id="structTLV__TAG_1a93f9c43966e69e776345a17bbf3a4906"></a> uint8\_t value\[\]
    :   pointer for TLV data buffer

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv48TLV_TYPE"></a>

<a id="_CPPv38TLV_TYPE"></a> <a id="_CPPv28TLV_TYPE"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0"></a> enum TLV\_TYPE
:   TLV tag value definition.

    *Values:*

    <a id="_CPPv4N8TLV_TYPE17TLV_TYPE_CALI_ENDE"></a>

    <a id="_CPPv3N8TLV_TYPE17TLV_TYPE_CALI_ENDE"></a> <a id="_CPPv2N8TLV_TYPE17TLV_TYPE_CALI_ENDE"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0a36cf1c1604d6e4880ceb8d97db722696"></a> enumerator TLV\_TYPE\_CALI\_END

    <a id="_CPPv4N8TLV_TYPE35TLV_TYPE_CALI_DC_OFFSET_DIFF_DISPGAE"></a>

    <a id="_CPPv3N8TLV_TYPE35TLV_TYPE_CALI_DC_OFFSET_DIFF_DISPGAE"></a> <a id="_CPPv2N8TLV_TYPE35TLV_TYPE_CALI_DC_OFFSET_DIFF_DISPGAE"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0abb6de6924c5528fecc64f336e9e4c57c"></a> enumerator TLV\_TYPE\_CALI\_DC\_OFFSET\_DIFF\_DISPGA

    <a id="_CPPv4N8TLV_TYPE35TLV_TYPE_CALI_DC_OFFSET_SNGL_DISPGAE"></a>

    <a id="_CPPv3N8TLV_TYPE35TLV_TYPE_CALI_DC_OFFSET_SNGL_DISPGAE"></a> <a id="_CPPv2N8TLV_TYPE35TLV_TYPE_CALI_DC_OFFSET_SNGL_DISPGAE"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0a825dbe833b205c908592aa6b884f112e"></a> enumerator TLV\_TYPE\_CALI\_DC\_OFFSET\_SNGL\_DISPGA

    <a id="_CPPv4N8TLV_TYPE34TLV_TYPE_CALI_DC_OFFSET_DIFF_ENPGAE"></a>

    <a id="_CPPv3N8TLV_TYPE34TLV_TYPE_CALI_DC_OFFSET_DIFF_ENPGAE"></a> <a id="_CPPv2N8TLV_TYPE34TLV_TYPE_CALI_DC_OFFSET_DIFF_ENPGAE"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0acc62bbafd4f4959a4ab9d5a3eee40402"></a> enumerator TLV\_TYPE\_CALI\_DC\_OFFSET\_DIFF\_ENPGA

    <a id="_CPPv4N8TLV_TYPE34TLV_TYPE_CALI_DC_OFFSET_SNGL_ENPGAE"></a>

    <a id="_CPPv3N8TLV_TYPE34TLV_TYPE_CALI_DC_OFFSET_SNGL_ENPGAE"></a> <a id="_CPPv2N8TLV_TYPE34TLV_TYPE_CALI_DC_OFFSET_SNGL_ENPGAE"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0aaf3d384381e66c31377733a35ecbc4a1"></a> enumerator TLV\_TYPE\_CALI\_DC\_OFFSET\_SNGL\_ENPGA

    <a id="_CPPv4N8TLV_TYPE20TLV_TYPE_CALI_SARADCE"></a>

    <a id="_CPPv3N8TLV_TYPE20TLV_TYPE_CALI_SARADCE"></a> <a id="_CPPv2N8TLV_TYPE20TLV_TYPE_CALI_SARADCE"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0ad6447070bdb0db98ec5703ea06b78a9c"></a> enumerator TLV\_TYPE\_CALI\_SARADC

    <a id="_CPPv4N8TLV_TYPE21TLV_TYPE_CALI_VOLTAGEE"></a>

    <a id="_CPPv3N8TLV_TYPE21TLV_TYPE_CALI_VOLTAGEE"></a> <a id="_CPPv2N8TLV_TYPE21TLV_TYPE_CALI_VOLTAGEE"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0ae61728fea4ebae3cc694e956c5b49780"></a> enumerator TLV\_TYPE\_CALI\_VOLTAGE

    <a id="_CPPv4N8TLV_TYPE20TLV_TYPE_CALI_CHARGEE"></a>

    <a id="_CPPv3N8TLV_TYPE20TLV_TYPE_CALI_CHARGEE"></a> <a id="_CPPv2N8TLV_TYPE20TLV_TYPE_CALI_CHARGEE"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0aa04d7665b35e42adf87c9b61614c38e6"></a> enumerator TLV\_TYPE\_CALI\_CHARGE

    <a id="_CPPv4N8TLV_TYPE19TLV_TYPE_CALI_TEMPRE"></a>

    <a id="_CPPv3N8TLV_TYPE19TLV_TYPE_CALI_TEMPRE"></a> <a id="_CPPv2N8TLV_TYPE19TLV_TYPE_CALI_TEMPRE"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0a3d4ccf9ac0e1409ca7833582d18bba5f"></a> enumerator TLV\_TYPE\_CALI\_TEMPR

    <a id="_CPPv4N8TLV_TYPE23TLV_TYPE_CALI_ANC_PARAME"></a>

    <a id="_CPPv3N8TLV_TYPE23TLV_TYPE_CALI_ANC_PARAME"></a> <a id="_CPPv2N8TLV_TYPE23TLV_TYPE_CALI_ANC_PARAME"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0a07d8bc8b05290577935f2111e610fe2e"></a> enumerator TLV\_TYPE\_CALI\_ANC\_PARAM

    <a id="_CPPv4N8TLV_TYPE23TLV_TYPE_CALI_ANC_COEFSE"></a>

    <a id="_CPPv3N8TLV_TYPE23TLV_TYPE_CALI_ANC_COEFSE"></a> <a id="_CPPv2N8TLV_TYPE23TLV_TYPE_CALI_ANC_COEFSE"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0a868c38cc8c41ebbd2d80a5004a40a0be"></a> enumerator TLV\_TYPE\_CALI\_ANC\_COEFS

    <a id="_CPPv4N8TLV_TYPE18TLV_TYPE_CFG_TOTALE"></a>

    <a id="_CPPv3N8TLV_TYPE18TLV_TYPE_CFG_TOTALE"></a> <a id="_CPPv2N8TLV_TYPE18TLV_TYPE_CFG_TOTALE"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0a1554b6d48f645890fba150a23957b182"></a> enumerator TLV\_TYPE\_CFG\_TOTAL

    <a id="_CPPv4N8TLV_TYPE20TLV_TYPE_CFG_BT_NAMEE"></a>

    <a id="_CPPv3N8TLV_TYPE20TLV_TYPE_CFG_BT_NAMEE"></a> <a id="_CPPv2N8TLV_TYPE20TLV_TYPE_CFG_BT_NAMEE"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0a680073d8d887cb38c45047d76b34fa0d"></a> enumerator TLV\_TYPE\_CFG\_BT\_NAME

    <a id="_CPPv4N8TLV_TYPE20TLV_TYPE_CFG_BT_ADDRE"></a>

    <a id="_CPPv3N8TLV_TYPE20TLV_TYPE_CFG_BT_ADDRE"></a> <a id="_CPPv2N8TLV_TYPE20TLV_TYPE_CFG_BT_ADDRE"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0ad367b8f8d080eb4de38ba678240b9adf"></a> enumerator TLV\_TYPE\_CFG\_BT\_ADDR

    <a id="_CPPv4N8TLV_TYPE21TLV_TYPE_CFG_SYS_PARAE"></a>

    <a id="_CPPv3N8TLV_TYPE21TLV_TYPE_CFG_SYS_PARAE"></a> <a id="_CPPv2N8TLV_TYPE21TLV_TYPE_CFG_SYS_PARAE"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0ae6a16c4f15e071b7b751e92d05803938"></a> enumerator TLV\_TYPE\_CFG\_SYS\_PARA

    <a id="_CPPv4N8TLV_TYPE20TLV_TYPE_CFG_HFP_FEQE"></a>

    <a id="_CPPv3N8TLV_TYPE20TLV_TYPE_CFG_HFP_FEQE"></a> <a id="_CPPv2N8TLV_TYPE20TLV_TYPE_CFG_HFP_FEQE"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0aae6931eb05ad57cb0fa97ac5f1424454"></a> enumerator TLV\_TYPE\_CFG\_HFP\_FEQ

    <a id="_CPPv4N8TLV_TYPE21TLV_TYPE_FACT_BT_NAMEE"></a>

    <a id="_CPPv3N8TLV_TYPE21TLV_TYPE_FACT_BT_NAMEE"></a> <a id="_CPPv2N8TLV_TYPE21TLV_TYPE_FACT_BT_NAMEE"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0a02ed75f3f1594a4f7c6e5d9d4b1c819e"></a> enumerator TLV\_TYPE\_FACT\_BT\_NAME

    <a id="_CPPv4N8TLV_TYPE21TLV_TYPE_FACT_BT_ADDRE"></a>

    <a id="_CPPv3N8TLV_TYPE21TLV_TYPE_FACT_BT_ADDRE"></a> <a id="_CPPv2N8TLV_TYPE21TLV_TYPE_FACT_BT_ADDRE"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0afb8a391dd0afc6078911c04aac2a76ed"></a> enumerator TLV\_TYPE\_FACT\_BT\_ADDR

    <a id="_CPPv4N8TLV_TYPE18TLV_TYPE_BASE_INFOE"></a>

    <a id="_CPPv3N8TLV_TYPE18TLV_TYPE_BASE_INFOE"></a> <a id="_CPPv2N8TLV_TYPE18TLV_TYPE_BASE_INFOE"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0a79cee10d039b4fa321b7529cd4183bde"></a> enumerator TLV\_TYPE\_BASE\_INFO

    <a id="_CPPv4N8TLV_TYPE18TLV_TYPE_CALI_END2E"></a>

    <a id="_CPPv3N8TLV_TYPE18TLV_TYPE_CALI_END2E"></a> <a id="_CPPv2N8TLV_TYPE18TLV_TYPE_CALI_END2E"></a> <a id="app__tlv_8h_1a73dc891ee7355dfbd84d75fdc004a9e0adb362c4a3b5a823cdf1fc1f219dfcdbc"></a> enumerator TLV\_TYPE\_CALI\_END2

<a id="_CPPv410TLV_SECTOR"></a>

<a id="_CPPv310TLV_SECTOR"></a> <a id="_CPPv210TLV_SECTOR"></a> <a id="app__tlv_8h_1afd723361c1e333bcf39b4f2111b597bb"></a> enum TLV\_SECTOR
:   TLV sector index definition.

    *Values:*

    <a id="_CPPv4N10TLV_SECTOR17TLV_SECTOR_ENVCFGE"></a>

    <a id="_CPPv3N10TLV_SECTOR17TLV_SECTOR_ENVCFGE"></a> <a id="_CPPv2N10TLV_SECTOR17TLV_SECTOR_ENVCFGE"></a> <a id="app__tlv_8h_1afd723361c1e333bcf39b4f2111b597bba4013157890453ca66e81c64575a573d6"></a> enumerator TLV\_SECTOR\_ENVCFG

    <a id="_CPPv4N10TLV_SECTOR18TLV_SECTOR_ENVDATAE"></a>

    <a id="_CPPv3N10TLV_SECTOR18TLV_SECTOR_ENVDATAE"></a> <a id="_CPPv2N10TLV_SECTOR18TLV_SECTOR_ENVDATAE"></a> <a id="app__tlv_8h_1afd723361c1e333bcf39b4f2111b597bba59f993b4c9de87358b9578aa9f22b7e8"></a> enumerator TLV\_SECTOR\_ENVDATA

    <a id="_CPPv4N10TLV_SECTOR18TLV_SECTOR_ENVCALIE"></a>

    <a id="_CPPv3N10TLV_SECTOR18TLV_SECTOR_ENVCALIE"></a> <a id="_CPPv2N10TLV_SECTOR18TLV_SECTOR_ENVCALIE"></a> <a id="app__tlv_8h_1afd723361c1e333bcf39b4f2111b597bbab74fd7820fb070f8313702090e934a96"></a> enumerator TLV\_SECTOR\_ENVCALI

    <a id="_CPPv4N10TLV_SECTOR17TLV_SECTOR_ENVENDE"></a>

    <a id="_CPPv3N10TLV_SECTOR17TLV_SECTOR_ENVENDE"></a> <a id="_CPPv2N10TLV_SECTOR17TLV_SECTOR_ENVENDE"></a> <a id="app__tlv_8h_1afd723361c1e333bcf39b4f2111b597bbaaaac0e38f261596a1714324b618088ed"></a> enumerator TLV\_SECTOR\_ENVEND
