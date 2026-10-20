---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/btif/adv_if.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="adv-interface-functions"></a>

# ADV Interface Functions

<a id="adv-if-api-brief"></a>

## ADV\_IF API Brief

| Application | Brief |
| --- | --- |
| [`adv_if_remove_adv()`](#_CPPv417adv_if_remove_adv7uint8_t "adv_if_remove_adv") | remove a adv enviroment |
| [`adv_if_create_adv()`](#_CPPv417adv_if_create_advP8adv_if_t "adv_if_create_adv") | create a adv enviroment |
| [`adv_if_set_adv_data()`](#_CPPv419adv_if_set_adv_data7uint8_tP7uint8_t8uint16_t "adv_if_set_adv_data") | set adv data base on adv idx |
| [`adv_if_adv_enable()`](#_CPPv417adv_if_adv_enable7uint8_t "adv_if_adv_enable") | enable phy layer to enable advertising |
| [`adv_if_adv_disable()`](#_CPPv418adv_if_adv_disable7uint8_t "adv_if_adv_disable") | stop phy layer to disable advertising |
| [`adv_if_set_scan_rsp_data()`](#_CPPv424adv_if_set_scan_rsp_data7uint8_tP7uint8_t8uint16_t "adv_if_set_scan_rsp_data") | set adv scan rsp data base on adv idx |
| [`adv_if_set_PA_data()`](#_CPPv418adv_if_set_PA_data7uint8_tP7uint8_t8uint16_t "adv_if_set_PA_data") | set periodic adv data base on adv idx |

<a id="adv-if-api-reference"></a>

## ADV\_IF API Reference

<a id="header-file"></a>

### Header File

- [btif/inc/adv\_if.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/btif/inc/adv_if.h)

<a id="functions"></a>

### Functions

<a id="_CPPv417adv_if_remove_adv7uint8_t"></a>

<a id="_CPPv317adv_if_remove_adv7uint8_t"></a> <a id="_CPPv217adv_if_remove_adv7uint8_t"></a> <a id="adv_if_remove_adv__uint8_t"></a> <a id="adv__if_8h_1a0a6e4c017d632569358eb1af726a7744"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") adv\_if\_remove\_adv(uint8\_t adv\_idx)
:   remove a adv enviroment.

    when adv is not used, you should remove adv in case of memory leak

    参数:
    :   **adv\_idx** – **\[in\]** index of advertising parameter

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv417adv_if_create_advP8adv_if_t"></a>

<a id="_CPPv317adv_if_create_advP8adv_if_t"></a> <a id="_CPPv217adv_if_create_advP8adv_if_t"></a> <a id="adv_if_create_adv__adv_if_tP"></a> <a id="adv__if_8h_1a6e169d4afa7c0a62370f4ca9cd2f665b"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") adv\_if\_create\_adv([adv\_if\_t](#_CPPv48adv_if_t "adv_if_t") \*p\_adv)
:   create a adv enviroment.

    beofre adv is not used, you should create a adv env firstly

    参数:
    :   **p\_adv** – **\[in\]** pointer for a LE advertising parameter

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419adv_if_set_adv_data7uint8_tP7uint8_t8uint16_t"></a>

<a id="_CPPv319adv_if_set_adv_data7uint8_tP7uint8_t8uint16_t"></a> <a id="_CPPv219adv_if_set_adv_data7uint8_tP7uint8_t8uint16_t"></a> <a id="adv_if_set_adv_data__uint8_t.uint8_tP.uint16_t"></a> <a id="adv__if_8h_1ae490c8a97473a737fe5b62c6683c25e6"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") adv\_if\_set\_adv\_data(uint8\_t adv\_idx, uint8\_t \*p\_adv\_data, uint16\_t len)
:   set adv data base on adv idx.

    set adv data before you enable one adv

    参数:
    :   - **adv\_idx** – **\[in\]** index of advertising parameter
        - **p\_adv\_data** – **\[in\]** pointer for advertising data
        - **len** – **\[in\]** length of p\_adv\_data

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv417adv_if_adv_enable7uint8_t"></a>

<a id="_CPPv317adv_if_adv_enable7uint8_t"></a> <a id="_CPPv217adv_if_adv_enable7uint8_t"></a> <a id="adv_if_adv_enable__uint8_t"></a> <a id="adv__if_8h_1ac8e775314b337879a4f1614540fcc1f8"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") adv\_if\_adv\_enable(uint8\_t adv\_idx)
:   enable phy layer to enable advertising.

    after config data and parameters done, you can enable one adv

    参数:
    :   **adv\_idx** – **\[in\]** index of advertising parameter

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv418adv_if_adv_disable7uint8_t"></a>

<a id="_CPPv318adv_if_adv_disable7uint8_t"></a> <a id="_CPPv218adv_if_adv_disable7uint8_t"></a> <a id="adv_if_adv_disable__uint8_t"></a> <a id="adv__if_8h_1a55be063619abfeba4ea5d8a6aaf760e6"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") adv\_if\_adv\_disable(uint8\_t adv\_idx)
:   stop phy layer to disable advertising.

    call this api to disable advertising

    参数:
    :   **adv\_idx** – **\[in\]** index of advertising parameter

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424adv_if_set_scan_rsp_data7uint8_tP7uint8_t8uint16_t"></a>

<a id="_CPPv324adv_if_set_scan_rsp_data7uint8_tP7uint8_t8uint16_t"></a> <a id="_CPPv224adv_if_set_scan_rsp_data7uint8_tP7uint8_t8uint16_t"></a> <a id="adv_if_set_scan_rsp_data__uint8_t.uint8_tP.uint16_t"></a> <a id="adv__if_8h_1a96c6248eda76aaa66524083451e41526"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") adv\_if\_set\_scan\_rsp\_data(uint8\_t adv\_idx, uint8\_t \*p\_rsp\_data, uint16\_t len)
:   set adv scan rsp data base on adv idx.

    set adv scan rsp data before you enable one adv

    参数:
    :   - **adv\_idx** – **\[in\]** index of advertising parameter
        - **p\_rsp\_data** – **\[in\]** pointer for scan response data
        - **len** – **\[in\]** length of p\_rsp\_data

    返回:
    :   bt\_ret\_t

<a id="_CPPv418adv_if_set_PA_data7uint8_tP7uint8_t8uint16_t"></a>

<a id="_CPPv318adv_if_set_PA_data7uint8_tP7uint8_t8uint16_t"></a> <a id="_CPPv218adv_if_set_PA_data7uint8_tP7uint8_t8uint16_t"></a> <a id="adv_if_set_PA_data__uint8_t.uint8_tP.uint16_t"></a> <a id="adv__if_8h_1a45eee938e91ca2b538bbc28fd45a16b0"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") adv\_if\_set\_PA\_data(uint8\_t adv\_idx, uint8\_t \*p\_pa\_data, uint16\_t len)
:   set periodic adv data base on adv idx.

    set aperiodic adv data before you enable one adv that included periodic adv enable

    参数:
    :   - **adv\_idx** – **\[in\]** index of advertising parameter
        - **p\_pa\_data** – **\[in\]** pointer for aperiodic advertising data
        - **len** – **\[in\]** length of p\_pa\_data

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv48adv_if_t"></a>

<a id="_CPPv38adv_if_t"></a> <a id="_CPPv28adv_if_t"></a> <a id="adv_if_t"></a> <a id="structadv__if__t"></a> struct adv\_if\_t
:   LE advertising parameter data struct.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N8adv_if_t7adv_idxE"></a>

    <a id="_CPPv3N8adv_if_t7adv_idxE"></a> <a id="_CPPv2N8adv_if_t7adv_idxE"></a> <a id="adv_if_t::adv_idx__uint8_t"></a> <a id="structadv__if__t_1af5ba177bded831e583c4d7023e9dbfa0"></a> uint8\_t adv\_idx
    :   index of advertising parameter

    <a id="_CPPv4N8adv_if_t8adv_typeE"></a>

    <a id="_CPPv3N8adv_if_t8adv_typeE"></a> <a id="_CPPv2N8adv_if_t8adv_typeE"></a> <a id="adv_if_t::adv_type__uint8_t"></a> <a id="structadv__if__t_1a8e4508a1c8bfc9d824f52fc3910edae7"></a> uint8\_t adv\_type
    :   advertising type

    <a id="_CPPv4N8adv_if_t9addr_typeE"></a>

    <a id="_CPPv3N8adv_if_t9addr_typeE"></a> <a id="_CPPv2N8adv_if_t9addr_typeE"></a> <a id="adv_if_t::addr_type__uint8_t"></a> <a id="structadv__if__t_1a58e684e673dac6e64dbe3e374d117ec5"></a> uint8\_t addr\_type
    :   advertiser address type 0-public/1-static/2-rpa/3/non-rpa

    <a id="_CPPv4N8adv_if_t10adv_ext_enE"></a>

    <a id="_CPPv3N8adv_if_t10adv_ext_enE"></a> <a id="_CPPv2N8adv_if_t10adv_ext_enE"></a> <a id="adv_if_t::adv_ext_en__b"></a> <a id="structadv__if__t_1ae9cc891ecbd0f6d51da4f4e040aa83ab"></a> bool adv\_ext\_en
    :   enable extended advertising or not

    <a id="_CPPv4N8adv_if_t5pa_enE"></a>

    <a id="_CPPv3N8adv_if_t5pa_enE"></a> <a id="_CPPv2N8adv_if_t5pa_enE"></a> <a id="adv_if_t::pa_en__b"></a> <a id="structadv__if__t_1a33beb945cbe9a1a235938db06c2fbe65"></a> bool pa\_en
    :   enable peridoic advertising or not

    <a id="_CPPv4N8adv_if_t16adv_interval_minE"></a>

    <a id="_CPPv3N8adv_if_t16adv_interval_minE"></a> <a id="_CPPv2N8adv_if_t16adv_interval_minE"></a> <a id="adv_if_t::adv_interval_min__uint32_t"></a> <a id="structadv__if__t_1a05919c1bedb598b146f569926e310cde"></a> uint32\_t adv\_interval\_min
    :   min interval of advertising uint 0.625ms

    <a id="_CPPv4N8adv_if_t16adv_interval_maxE"></a>

    <a id="_CPPv3N8adv_if_t16adv_interval_maxE"></a> <a id="_CPPv2N8adv_if_t16adv_interval_maxE"></a> <a id="adv_if_t::adv_interval_max__uint32_t"></a> <a id="structadv__if__t_1a89a99ca6f235abe866bfa3429a9a771c"></a> uint32\_t adv\_interval\_max
    :   max interval of advertising uint 0.625ms

    <a id="_CPPv4N8adv_if_t15pa_interval_minE"></a>

    <a id="_CPPv3N8adv_if_t15pa_interval_minE"></a> <a id="_CPPv2N8adv_if_t15pa_interval_minE"></a> <a id="adv_if_t::pa_interval_min__uint16_t"></a> <a id="structadv__if__t_1a84d0091d5937f76ab5f01b684c7e6e28"></a> uint16\_t pa\_interval\_min
    :   min interval of peridoic advertising uint 1.25ms

    <a id="_CPPv4N8adv_if_t15pa_interval_maxE"></a>

    <a id="_CPPv3N8adv_if_t15pa_interval_maxE"></a> <a id="_CPPv2N8adv_if_t15pa_interval_maxE"></a> <a id="adv_if_t::pa_interval_max__uint16_t"></a> <a id="structadv__if__t_1a42e045cee366e0c7abc0ba76b07f67c9"></a> uint16\_t pa\_interval\_max
    :   min interval of peridoic advertising uint 1.25ms

<a id="macros"></a>

### Macros

<a id="c.ADV_SCANABLE_TYPE"></a>

<a id="adv__if_8h_1addbd05baacb8aeed63f07b13fe7cfad7"></a> ADV\_SCANABLE\_TYPE

<a id="c.ADV_CONNECTABLE_TYPE"></a>

<a id="adv__if_8h_1a4a0873ea61183bfd33befea8a1425bce"></a> ADV\_CONNECTABLE\_TYPE

<a id="c.ADV_PUBLIC_ADDR"></a>

<a id="adv__if_8h_1a12fc68d5354382c6f0c096193c4690ee"></a> ADV\_PUBLIC\_ADDR

<a id="c.ADV_STATIC_RANDOM_ADDR"></a>

<a id="adv__if_8h_1a49b416b29740df5591db5ee902e724c2"></a> ADV\_STATIC\_RANDOM\_ADDR

<a id="c.ADV_RPA_RANDOM_ADDR"></a>

<a id="adv__if_8h_1ad83dde5729ca698391a8629066e3cdbc"></a> ADV\_RPA\_RANDOM\_ADDR

<a id="c.ADV_NON_RPA_RANDOM_ADDR"></a>

<a id="adv__if_8h_1a570569ab7a23c29f21ae93e600cf9a00"></a> ADV\_NON\_RPA\_RANDOM\_ADDR

<a id="c.ADV_1M_PHY"></a>

<a id="adv__if_8h_1a4e898507173ce798bb6a087d505e16b2"></a> ADV\_1M\_PHY

<a id="c.ADV_2M_PHY"></a>

<a id="adv__if_8h_1a2d177f4edd056d7b6cbdf741ed20a26e"></a> ADV\_2M\_PHY

<a id="c.ADV_CODED_PHY"></a>

<a id="adv__if_8h_1afa6d311d3ca905ae22030c207d2e64cc"></a> ADV\_CODED\_PHY
