---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/btif/btif_type.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="btif-type-functions"></a>

# BTIF TYPE Functions

<a id="btif-type-api-reference"></a>

## BTIF\_TYPE API Reference

<a id="header-file"></a>

### Header File

- [btif/inc/btif\_type.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/btif/inc/btif_type.h)

<a id="unions"></a>

### Unions

<a id="_CPPv415btif_uuid_val_n"></a>

<a id="_CPPv315btif_uuid_val_n"></a> <a id="_CPPv215btif_uuid_val_n"></a> <a id="unionbtif__uuid__val__n"></a> union btif\_uuid\_val\_n
:   *#include \<btif\_type.h\>*

    union of UUID

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N15btif_uuid_val_n7uuid_16E"></a>

    <a id="_CPPv3N15btif_uuid_val_n7uuid_16E"></a> <a id="_CPPv2N15btif_uuid_val_n7uuid_16E"></a> <a id="btif_uuid_val_n::uuid_16__uint16_t"></a> <a id="unionbtif__uuid__val__n_1a19517e5481a26688432412dfb6602c27"></a> uint16\_t uuid\_16

    <a id="_CPPv4N15btif_uuid_val_n7uuid_32E"></a>

    <a id="_CPPv3N15btif_uuid_val_n7uuid_32E"></a> <a id="_CPPv2N15btif_uuid_val_n7uuid_32E"></a> <a id="btif_uuid_val_n::uuid_32__uint32_t"></a> <a id="unionbtif__uuid__val__n_1a3896dd3c969b4bf3770707ac5f581c3b"></a> uint32\_t uuid\_32

    <a id="_CPPv4N15btif_uuid_val_n8uuid_128E"></a>

    <a id="_CPPv3N15btif_uuid_val_n8uuid_128E"></a> <a id="_CPPv2N15btif_uuid_val_n8uuid_128E"></a> <a id="btif_uuid_val_n::uuid_128__uint8_tA"></a> <a id="unionbtif__uuid__val__n_1a8a12e6fcad497305875cdeba5cb49281"></a> uint8\_t uuid\_128\[16\]

<a id="structures"></a>

### Structures

<a id="_CPPv411btif_uuid_t"></a>

<a id="_CPPv311btif_uuid_t"></a> <a id="_CPPv211btif_uuid_t"></a> <a id="btif_uuid_t"></a> <a id="structbtif__uuid__t"></a> struct btif\_uuid\_t
:   UUID data struct definition.

<a id="_CPPv410btif_clk_t"></a>

<a id="_CPPv310btif_clk_t"></a> <a id="_CPPv210btif_clk_t"></a> <a id="btif_clk_t"></a> <a id="structbtif__clk__t"></a> struct btif\_clk\_t

<a id="_CPPv414btif_bd_addr_t"></a>

<a id="_CPPv314btif_bd_addr_t"></a> <a id="_CPPv214btif_bd_addr_t"></a> <a id="btif_bd_addr_t"></a> <a id="structbtif__bd__addr__t"></a> struct btif\_bd\_addr\_t
:   bluetooth MAC address data struct definition

<a id="_CPPv49btif_lk_t"></a>

<a id="_CPPv39btif_lk_t"></a> <a id="_CPPv29btif_lk_t"></a> <a id="btif_lk_t"></a> <a id="structbtif__lk__t"></a> struct btif\_lk\_t
:   link key data struct definition

<a id="_CPPv416btif_le_lk_ltk_t"></a>

<a id="_CPPv316btif_le_lk_ltk_t"></a> <a id="_CPPv216btif_le_lk_ltk_t"></a> <a id="btif_le_lk_ltk_t"></a> <a id="structbtif__le__lk__ltk__t"></a> struct btif\_le\_lk\_ltk\_t
:   LE long term key data struct defintion.

<a id="_CPPv416btif_le_lk_irk_t"></a>

<a id="_CPPv316btif_le_lk_irk_t"></a> <a id="_CPPv216btif_le_lk_irk_t"></a> <a id="btif_le_lk_irk_t"></a> <a id="structbtif__le__lk__irk__t"></a> struct btif\_le\_lk\_irk\_t
:   LE identity resolving key data struct defintion.

<a id="_CPPv417btif_le_lk_csrk_t"></a>

<a id="_CPPv317btif_le_lk_csrk_t"></a> <a id="_CPPv217btif_le_lk_csrk_t"></a> <a id="btif_le_lk_csrk_t"></a> <a id="structbtif__le__lk__csrk__t"></a> struct btif\_le\_lk\_csrk\_t
:   LE connection signature resolving key data struct definition.

<a id="_CPPv412btif_le_lk_t"></a>

<a id="_CPPv312btif_le_lk_t"></a> <a id="_CPPv212btif_le_lk_t"></a> <a id="btif_le_lk_t"></a> <a id="structbtif__le__lk__t"></a> struct btif\_le\_lk\_t
:   Le link key data struction definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N12btif_le_lk_t8sec_propE"></a>

    <a id="_CPPv3N12btif_le_lk_t8sec_propE"></a> <a id="_CPPv2N12btif_le_lk_t8sec_propE"></a> <a id="btif_le_lk_t::sec_prop__uint8_t"></a> <a id="structbtif__le__lk__t_1abe20db0b61b36ba4772222f843c85dcd"></a> uint8\_t sec\_prop
    :   security Properties

<a id="_CPPv413tws_ux_info_t"></a>

<a id="_CPPv313tws_ux_info_t"></a> <a id="_CPPv213tws_ux_info_t"></a> <a id="tws_ux_info_t"></a> <a id="structtws__ux__info__t"></a> struct tws\_ux\_info\_t
:   TWS UX information data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N13tws_ux_info_t7tws_posE"></a>

    <a id="_CPPv3N13tws_ux_info_t7tws_posE"></a> <a id="_CPPv2N13tws_ux_info_t7tws_posE"></a> <a id="tws_ux_info_t::tws_pos__uint8_t"></a> <a id="structtws__ux__info__t_1ab99e800119785c6a0ccf9f37d893c87d"></a> uint8\_t tws\_pos
    :   TWS position (left or right)

    <a id="_CPPv4N13tws_ux_info_t10aac_enableE"></a>

    <a id="_CPPv3N13tws_ux_info_t10aac_enableE"></a> <a id="_CPPv2N13tws_ux_info_t10aac_enableE"></a> <a id="tws_ux_info_t::aac_enable__uint8_t"></a> <a id="structtws__ux__info__t_1a577009375ce0ca97a4f9c0a6fdd064d2"></a> uint8\_t aac\_enable
    :   value for AAC enable or not

    <a id="_CPPv4N13tws_ux_info_t10tx_pwr_lvlE"></a>

    <a id="_CPPv3N13tws_ux_info_t10tx_pwr_lvlE"></a> <a id="_CPPv2N13tws_ux_info_t10tx_pwr_lvlE"></a> <a id="tws_ux_info_t::tx_pwr_lvl__uint16_t"></a> <a id="structtws__ux__info__t_1ad8d09bff3b60a883f48aff08afe6431c"></a> uint16\_t tx\_pwr\_lvl
    :   TX power level

    <a id="_CPPv4N13tws_ux_info_t8tws_addrE"></a>

    <a id="_CPPv3N13tws_ux_info_t8tws_addrE"></a> <a id="_CPPv2N13tws_ux_info_t8tws_addrE"></a> <a id="tws_ux_info_t::tws_addr__btif_bd_addr_t"></a> <a id="structtws__ux__info__t_1a8dd969129f26386039d822599f60f6ce"></a> [btif\_bd\_addr\_t](#_CPPv414btif_bd_addr_t "btif_bd_addr_t") tws\_addr
    :   TWS paired MAC address

    <a id="_CPPv4N13tws_ux_info_t10local_addrE"></a>

    <a id="_CPPv3N13tws_ux_info_t10local_addrE"></a> <a id="_CPPv2N13tws_ux_info_t10local_addrE"></a> <a id="tws_ux_info_t::local_addr__btif_bd_addr_t"></a> <a id="structtws__ux__info__t_1aaebbbdee20772a679515d517883155cb"></a> [btif\_bd\_addr\_t](#_CPPv414btif_bd_addr_t "btif_bd_addr_t") local\_addr
    :   local BT MAC address

    <a id="_CPPv4N13tws_ux_info_t9p_bt_nameE"></a>

    <a id="_CPPv3N13tws_ux_info_t9p_bt_nameE"></a> <a id="_CPPv2N13tws_ux_info_t9p_bt_nameE"></a> <a id="tws_ux_info_t::p_bt_name__cP"></a> <a id="structtws__ux__info__t_1a88a042b59801a7975d615ebc7764dec3"></a> char \*p\_bt\_name
    :   local BT device name

    <a id="_CPPv4N13tws_ux_info_t23pfunc_bt_task_init_doneE"></a>

    <a id="_CPPv3N13tws_ux_info_t23pfunc_bt_task_init_doneE"></a> <a id="_CPPv2N13tws_ux_info_t23pfunc_bt_task_init_doneE"></a> <a id="tws_ux_info_t::pfunc_bt_task_init_done__task_init_done_callback"></a> <a id="structtws__ux__info__t_1aa612f0bc13746e0b4beb6745f53ae3ff"></a> [task\_init\_done\_callback](#_CPPv423task_init_done_callback "task_init_done_callback") pfunc\_bt\_task\_init\_done
    :   callback function for bt\_task

    <a id="_CPPv4N13tws_ux_info_t24pfunc_tws_task_init_doneE"></a>

    <a id="_CPPv3N13tws_ux_info_t24pfunc_tws_task_init_doneE"></a> <a id="_CPPv2N13tws_ux_info_t24pfunc_tws_task_init_doneE"></a> <a id="tws_ux_info_t::pfunc_tws_task_init_done__task_init_done_callback"></a> <a id="structtws__ux__info__t_1a229cab921d2dfb561675f572be236029"></a> [task\_init\_done\_callback](#_CPPv423task_init_done_callback "task_init_done_callback") pfunc\_tws\_task\_init\_done
    :   callback function for tws\_task

<a id="_CPPv419btif_dip_dev_info_t"></a>

<a id="_CPPv319btif_dip_dev_info_t"></a> <a id="_CPPv219btif_dip_dev_info_t"></a> <a id="btif_dip_dev_info_t"></a> <a id="structbtif__dip__dev__info__t"></a> struct btif\_dip\_dev\_info\_t
:   DIP device information data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19btif_dip_dev_info_t8spec_verE"></a>

    <a id="_CPPv3N19btif_dip_dev_info_t8spec_verE"></a> <a id="_CPPv2N19btif_dip_dev_info_t8spec_verE"></a> <a id="btif_dip_dev_info_t::spec_ver__uint16_t"></a> <a id="structbtif__dip__dev__info__t_1a7c053263b76c1e4b67f00931caa1e359"></a> uint16\_t spec\_ver
    :   Spec version

    <a id="_CPPv4N19btif_dip_dev_info_t3vidE"></a>

    <a id="_CPPv3N19btif_dip_dev_info_t3vidE"></a> <a id="_CPPv2N19btif_dip_dev_info_t3vidE"></a> <a id="btif_dip_dev_info_t::vid__uint16_t"></a> <a id="structbtif__dip__dev__info__t_1a2cef20b0acd290a8bde1c4ae2f7fa4fe"></a> uint16\_t vid
    :   Vendor ID

    <a id="_CPPv4N19btif_dip_dev_info_t3pidE"></a>

    <a id="_CPPv3N19btif_dip_dev_info_t3pidE"></a> <a id="_CPPv2N19btif_dip_dev_info_t3pidE"></a> <a id="btif_dip_dev_info_t::pid__uint16_t"></a> <a id="structbtif__dip__dev__info__t_1af49a354bd82bb3483d05e3d884e9f10f"></a> uint16\_t pid
    :   Product ID

    <a id="_CPPv4N19btif_dip_dev_info_t8prod_verE"></a>

    <a id="_CPPv3N19btif_dip_dev_info_t8prod_verE"></a> <a id="_CPPv2N19btif_dip_dev_info_t8prod_verE"></a> <a id="btif_dip_dev_info_t::prod_ver__uint16_t"></a> <a id="structbtif__dip__dev__info__t_1af8d2e1f37c75fd188c0e3e6853820ade"></a> uint16\_t prod\_ver
    :   Product Version

    <a id="_CPPv4N19btif_dip_dev_info_t8prim_recE"></a>

    <a id="_CPPv3N19btif_dip_dev_info_t8prim_recE"></a> <a id="_CPPv2N19btif_dip_dev_info_t8prim_recE"></a> <a id="btif_dip_dev_info_t::prim_rec__uint8_t"></a> <a id="structbtif__dip__dev__info__t_1a05236c54efcaaaadf1508d19d9672e29"></a> uint8\_t prim\_rec
    :   Primary record

    <a id="_CPPv4N19btif_dip_dev_info_t10vid_sourceE"></a>

    <a id="_CPPv3N19btif_dip_dev_info_t10vid_sourceE"></a> <a id="_CPPv2N19btif_dip_dev_info_t10vid_sourceE"></a> <a id="btif_dip_dev_info_t::vid_source__uint16_t"></a> <a id="structbtif__dip__dev__info__t_1a62c93eb3cf8219712d12f0b7458cdd8d"></a> uint16\_t vid\_source
    :   Vendor ID Source

<a id="_CPPv418btif_bt_dev_info_t"></a>

<a id="_CPPv318btif_bt_dev_info_t"></a> <a id="_CPPv218btif_bt_dev_info_t"></a> <a id="btif_bt_dev_info_t"></a> <a id="structbtif__bt__dev__info__t"></a> struct btif\_bt\_dev\_info\_t
:   BT device information data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18btif_bt_dev_info_t7bd_addrE"></a>

    <a id="_CPPv3N18btif_bt_dev_info_t7bd_addrE"></a> <a id="_CPPv2N18btif_bt_dev_info_t7bd_addrE"></a> <a id="btif_bt_dev_info_t::bd_addr__btif_bd_addr_t"></a> <a id="structbtif__bt__dev__info__t_1a0ca180a5cb991c25e37fe3c61002e472"></a> [btif\_bd\_addr\_t](#_CPPv414btif_bd_addr_t "btif_bd_addr_t") bd\_addr
    :   device MAC address

    <a id="_CPPv4N18btif_bt_dev_info_t2lkE"></a>

    <a id="_CPPv3N18btif_bt_dev_info_t2lkE"></a> <a id="_CPPv2N18btif_bt_dev_info_t2lkE"></a> <a id="btif_bt_dev_info_t::lk__btif_lk_t"></a> <a id="structbtif__bt__dev__info__t_1abe83806ae5c42b40ff1b4565e9deba45"></a> [btif\_lk\_t](#_CPPv49btif_lk_t "btif_lk_t") lk
    :   link key data struct

    <a id="_CPPv4N18btif_bt_dev_info_t8a2dp_volE"></a>

    <a id="_CPPv3N18btif_bt_dev_info_t8a2dp_volE"></a> <a id="_CPPv2N18btif_bt_dev_info_t8a2dp_volE"></a> <a id="btif_bt_dev_info_t::a2dp_vol__uint8_t"></a> <a id="structbtif__bt__dev__info__t_1ad22475ccc32da5b70a47ba7258722fad"></a> uint8\_t a2dp\_vol
    :   volume value of A2DP

    <a id="_CPPv4N18btif_bt_dev_info_t7hfp_volE"></a>

    <a id="_CPPv3N18btif_bt_dev_info_t7hfp_volE"></a> <a id="_CPPv2N18btif_bt_dev_info_t7hfp_volE"></a> <a id="btif_bt_dev_info_t::hfp_vol__uint8_t"></a> <a id="structbtif__bt__dev__info__t_1a469703e812322923f18976d9230ad6b6"></a> uint8\_t hfp\_vol
    :   volume value of HFP

    <a id="_CPPv4N18btif_bt_dev_info_t15a2dp_codec_typeE"></a>

    <a id="_CPPv3N18btif_bt_dev_info_t15a2dp_codec_typeE"></a> <a id="_CPPv2N18btif_bt_dev_info_t15a2dp_codec_typeE"></a> <a id="btif_bt_dev_info_t::a2dp_codec_type__uint8_t"></a> <a id="structbtif__bt__dev__info__t_1a3da211327c289d82a199ed1447d2f5c7"></a> uint8\_t a2dp\_codec\_type
    :   using codec for A2DP

    <a id="_CPPv4N18btif_bt_dev_info_t8dip_infoE"></a>

    <a id="_CPPv3N18btif_bt_dev_info_t8dip_infoE"></a> <a id="_CPPv2N18btif_bt_dev_info_t8dip_infoE"></a> <a id="btif_bt_dev_info_t::dip_info__btif_dip_dev_info_t"></a> <a id="structbtif__bt__dev__info__t_1a81b8f8f085c6b08e52c3b4afe4d7ec87"></a> [btif\_dip\_dev\_info\_t](#_CPPv419btif_dip_dev_info_t "btif_dip_dev_info_t") dip\_info
    :   device information data struct

    <a id="_CPPv4N18btif_bt_dev_info_t8psr_modeE"></a>

    <a id="_CPPv3N18btif_bt_dev_info_t8psr_modeE"></a> <a id="_CPPv2N18btif_bt_dev_info_t8psr_modeE"></a> <a id="btif_bt_dev_info_t::psr_mode__uint8_t"></a> <a id="structbtif__bt__dev__info__t_1aab08bb8034d62f78059f62667639f47b"></a> uint8\_t psr\_mode
    :   psr mode

<a id="_CPPv419btif_ble_dev_info_t"></a>

<a id="_CPPv319btif_ble_dev_info_t"></a> <a id="_CPPv219btif_ble_dev_info_t"></a> <a id="btif_ble_dev_info_t"></a> <a id="structbtif__ble__dev__info__t"></a> struct btif\_ble\_dev\_info\_t
:   BLE device information data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19btif_ble_dev_info_t7bd_addrE"></a>

    <a id="_CPPv3N19btif_ble_dev_info_t7bd_addrE"></a> <a id="_CPPv2N19btif_ble_dev_info_t7bd_addrE"></a> <a id="btif_ble_dev_info_t::bd_addr__btif_bd_addr_t"></a> <a id="structbtif__ble__dev__info__t_1a56dd169462a58456d3daa9ae62b333d7"></a> [btif\_bd\_addr\_t](#_CPPv414btif_bd_addr_t "btif_bd_addr_t") bd\_addr
    :   devie MAC address

    <a id="_CPPv4N19btif_ble_dev_info_t5le_lkE"></a>

    <a id="_CPPv3N19btif_ble_dev_info_t5le_lkE"></a> <a id="_CPPv2N19btif_ble_dev_info_t5le_lkE"></a> <a id="btif_ble_dev_info_t::le_lk__btif_le_lk_t"></a> <a id="structbtif__ble__dev__info__t_1a5a6e3f6e98419773e3fb307ff984389a"></a> [btif\_le\_lk\_t](#_CPPv412btif_le_lk_t "btif_le_lk_t") le\_lk
    :   LE link key data struct

<a id="_CPPv417btif_le_bd_addr_t"></a>

<a id="_CPPv317btif_le_bd_addr_t"></a> <a id="_CPPv217btif_le_bd_addr_t"></a> <a id="btif_le_bd_addr_t"></a> <a id="structbtif__le__bd__addr__t"></a> struct btif\_le\_bd\_addr\_t
:   LE MAC address data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17btif_le_bd_addr_t4typeE"></a>

    <a id="_CPPv3N17btif_le_bd_addr_t4typeE"></a> <a id="_CPPv2N17btif_le_bd_addr_t4typeE"></a> <a id="btif_le_bd_addr_t::type__btif_le_addr_type_t"></a> <a id="structbtif__le__bd__addr__t_1a8e9b81e6d0e1de05cd40960ec1547798"></a> [btif\_le\_addr\_type\_t](#_CPPv419btif_le_addr_type_t "btif_le_addr_type_t") type
    :   type of LE MAC address

    <a id="_CPPv4N17btif_le_bd_addr_t4addrE"></a>

    <a id="_CPPv3N17btif_le_bd_addr_t4addrE"></a> <a id="_CPPv2N17btif_le_bd_addr_t4addrE"></a> <a id="btif_le_bd_addr_t::addr__btif_bd_addr_t"></a> <a id="structbtif__le__bd__addr__t_1ab0b7c763ae1c53049241a1bd6f8e088a"></a> [btif\_bd\_addr\_t](#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr
    :   MAC address data buffer

<a id="_CPPv413btif_uuid16_t"></a>

<a id="_CPPv313btif_uuid16_t"></a> <a id="_CPPv213btif_uuid16_t"></a> <a id="btif_uuid16_t"></a> <a id="structbtif__uuid16__t"></a> struct btif\_uuid16\_t
:   UUID16 data struct.

<a id="_CPPv413btif_uuid32_t"></a>

<a id="_CPPv313btif_uuid32_t"></a> <a id="_CPPv213btif_uuid32_t"></a> <a id="btif_uuid32_t"></a> <a id="structbtif__uuid32__t"></a> struct btif\_uuid32\_t
:   UUID32 data struct.

<a id="_CPPv414btif_uuid128_t"></a>

<a id="_CPPv314btif_uuid128_t"></a> <a id="_CPPv214btif_uuid128_t"></a> <a id="btif_uuid128_t"></a> <a id="structbtif__uuid128__t"></a> struct btif\_uuid128\_t
:   UUID128 data struct.

<a id="_CPPv413btif_ad_ltv_t"></a>

<a id="_CPPv313btif_ad_ltv_t"></a> <a id="_CPPv213btif_ad_ltv_t"></a> <a id="btif_ad_ltv_t"></a> <a id="structbtif__ad__ltv__t"></a> struct btif\_ad\_ltv\_t

<a id="_CPPv418btif_rmt_version_t"></a>

<a id="_CPPv318btif_rmt_version_t"></a> <a id="_CPPv218btif_rmt_version_t"></a> <a id="btif_rmt_version_t"></a> <a id="structbtif__rmt__version__t"></a> struct btif\_rmt\_version\_t
:   retmote device LMP version data struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18btif_rmt_version_t11lmp_versionE"></a>

    <a id="_CPPv3N18btif_rmt_version_t11lmp_versionE"></a> <a id="_CPPv2N18btif_rmt_version_t11lmp_versionE"></a> <a id="btif_rmt_version_t::lmp_version__uint8_t"></a> <a id="structbtif__rmt__version__t_1a295f522e555066970087853f9b498680"></a> uint8\_t lmp\_version
    :   LMP version

    <a id="_CPPv4N18btif_rmt_version_t11manufactureE"></a>

    <a id="_CPPv3N18btif_rmt_version_t11manufactureE"></a> <a id="_CPPv2N18btif_rmt_version_t11manufactureE"></a> <a id="btif_rmt_version_t::manufacture__uint16_t"></a> <a id="structbtif__rmt__version__t_1a4f16b52a2d91f6faa793db515404c98c"></a> uint16\_t manufacture
    :   manufacture ID

    <a id="_CPPv4N18btif_rmt_version_t14lmp_subversionE"></a>

    <a id="_CPPv3N18btif_rmt_version_t14lmp_subversionE"></a> <a id="_CPPv2N18btif_rmt_version_t14lmp_subversionE"></a> <a id="btif_rmt_version_t::lmp_subversion__uint16_t"></a> <a id="structbtif__rmt__version__t_1a0208358e1fb6853448b0cdd795f0d4ba"></a> uint16\_t lmp\_subversion
    :   LMP subversion

<a id="_CPPv414btif_a2dp_cp_t"></a>

<a id="_CPPv314btif_a2dp_cp_t"></a> <a id="_CPPv214btif_a2dp_cp_t"></a> <a id="btif_a2dp_cp_t"></a> <a id="structbtif__a2dp__cp__t"></a> struct btif\_a2dp\_cp\_t
:   A2DP content protection data struct definition.

<a id="_CPPv418le_audio_if_para_t"></a>

<a id="_CPPv318le_audio_if_para_t"></a> <a id="_CPPv218le_audio_if_para_t"></a> <a id="le_audio_if_para_t"></a> <a id="structle__audio__if__para__t"></a> struct le\_audio\_if\_para\_t
:   LE audio paramster data struct.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18le_audio_if_para_t9csip_sirkE"></a>

    <a id="_CPPv3N18le_audio_if_para_t9csip_sirkE"></a> <a id="_CPPv2N18le_audio_if_para_t9csip_sirkE"></a> <a id="le_audio_if_para_t::csip_sirk__uint8_tA"></a> <a id="structle__audio__if__para__t_1a94ba79bed03cff6274e5b4d723b3fd7f"></a> uint8\_t csip\_sirk\[16\]
    :   CSIP SIRK

    <a id="_CPPv4N18le_audio_if_para_t26pref_max_transport_latencyE"></a>

    <a id="_CPPv3N18le_audio_if_para_t26pref_max_transport_latencyE"></a> <a id="_CPPv2N18le_audio_if_para_t26pref_max_transport_latencyE"></a> <a id="le_audio_if_para_t::pref_max_transport_latency__uint16_t"></a> <a id="structle__audio__if__para__t_1a0afaafd2b271371f91d90dc334a21a4f"></a> uint16\_t pref\_max\_transport\_latency
    :   max tranport lantency

    <a id="_CPPv4N18le_audio_if_para_t27pref_presentation_delay_minE"></a>

    <a id="_CPPv3N18le_audio_if_para_t27pref_presentation_delay_minE"></a> <a id="_CPPv2N18le_audio_if_para_t27pref_presentation_delay_minE"></a> <a id="le_audio_if_para_t::pref_presentation_delay_min__uint32_t"></a> <a id="structle__audio__if__para__t_1ad6eaa9ee7968d7d4f61a6aa15842e993"></a> uint32\_t pref\_presentation\_delay\_min
    :   pref pd min

    <a id="_CPPv4N18le_audio_if_para_t27pref_presentation_delay_maxE"></a>

    <a id="_CPPv3N18le_audio_if_para_t27pref_presentation_delay_maxE"></a> <a id="_CPPv2N18le_audio_if_para_t27pref_presentation_delay_maxE"></a> <a id="le_audio_if_para_t::pref_presentation_delay_max__uint32_t"></a> <a id="structle__audio__if__para__t_1ab4e1cede1448005ee7d9ed51e4dc1bdd"></a> uint32\_t pref\_presentation\_delay\_max
    :   pref pd max

    <a id="_CPPv4N18le_audio_if_para_t27supp_presentation_delay_minE"></a>

    <a id="_CPPv3N18le_audio_if_para_t27supp_presentation_delay_minE"></a> <a id="_CPPv2N18le_audio_if_para_t27supp_presentation_delay_minE"></a> <a id="le_audio_if_para_t::supp_presentation_delay_min__uint32_t"></a> <a id="structle__audio__if__para__t_1a6a99a776ab925fac6fbc317c7739e6d5"></a> uint32\_t supp\_presentation\_delay\_min
    :   support pd min

    <a id="_CPPv4N18le_audio_if_para_t27supp_presentation_delay_maxE"></a>

    <a id="_CPPv3N18le_audio_if_para_t27supp_presentation_delay_maxE"></a> <a id="_CPPv2N18le_audio_if_para_t27supp_presentation_delay_maxE"></a> <a id="le_audio_if_para_t::supp_presentation_delay_max__uint32_t"></a> <a id="structle__audio__if__para__t_1a743a2f1f6a7a9abc3bb86a30ae65d85b"></a> uint32\_t supp\_presentation\_delay\_max
    :   support pd max

<a id="_CPPv416le_if_cfg_para_t"></a>

<a id="_CPPv316le_if_cfg_para_t"></a> <a id="_CPPv216le_if_cfg_para_t"></a> <a id="le_if_cfg_para_t"></a> <a id="structle__if__cfg__para__t"></a> struct le\_if\_cfg\_para\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N16le_if_cfg_para_t11public_addrE"></a>

    <a id="_CPPv3N16le_if_cfg_para_t11public_addrE"></a> <a id="_CPPv2N16le_if_cfg_para_t11public_addrE"></a> <a id="le_if_cfg_para_t::public_addr__btif_bd_addr_t"></a> <a id="structle__if__cfg__para__t_1a1fcadb8e8a1f467de87f3973d5c55aaf"></a> [btif\_bd\_addr\_t](#_CPPv414btif_bd_addr_t "btif_bd_addr_t") public\_addr
    :   BLE public address

    <a id="_CPPv4N16le_if_cfg_para_t11static_addrE"></a>

    <a id="_CPPv3N16le_if_cfg_para_t11static_addrE"></a> <a id="_CPPv2N16le_if_cfg_para_t11static_addrE"></a> <a id="le_if_cfg_para_t::static_addr__btif_bd_addr_t"></a> <a id="structle__if__cfg__para__t_1ae896eacf8cff2766ffbdd6afc652677b"></a> [btif\_bd\_addr\_t](#_CPPv414btif_bd_addr_t "btif_bd_addr_t") static\_addr
    :   BLE static address

    <a id="_CPPv4N16le_if_cfg_para_t8dev_nameE"></a>

    <a id="_CPPv3N16le_if_cfg_para_t8dev_nameE"></a> <a id="_CPPv2N16le_if_cfg_para_t8dev_nameE"></a> <a id="le_if_cfg_para_t::dev_name__cA"></a> <a id="structle__if__cfg__para__t_1a8efc3c60bf8a86be6e63627175396781"></a> char dev\_name\[32\]
    :   BLE name

    <a id="_CPPv4N16le_if_cfg_para_t12adv_intervalE"></a>

    <a id="_CPPv3N16le_if_cfg_para_t12adv_intervalE"></a> <a id="_CPPv2N16le_if_cfg_para_t12adv_intervalE"></a> <a id="le_if_cfg_para_t::adv_interval__uint16_t"></a> <a id="structle__if__cfg__para__t_1ad427f82ff4c696be8572fe2bb4691e25"></a> uint16\_t adv\_interval
    :   ADV interval(adv\_interval \* 1.25ms)

    <a id="_CPPv4N16le_if_cfg_para_t22conn_update_delay_timeE"></a>

    <a id="_CPPv3N16le_if_cfg_para_t22conn_update_delay_timeE"></a> <a id="_CPPv2N16le_if_cfg_para_t22conn_update_delay_timeE"></a> <a id="le_if_cfg_para_t::conn_update_delay_time__uint16_t"></a> <a id="structle__if__cfg__para__t_1a83138ee870eb8dfbdcab25c2bd2a3274"></a> uint16\_t conn\_update\_delay\_time
    :   connection update delay time (unit:s)

    <a id="_CPPv4N16le_if_cfg_para_t17conn_interval_minE"></a>

    <a id="_CPPv3N16le_if_cfg_para_t17conn_interval_minE"></a> <a id="_CPPv2N16le_if_cfg_para_t17conn_interval_minE"></a> <a id="le_if_cfg_para_t::conn_interval_min__uint16_t"></a> <a id="structle__if__cfg__para__t_1a6e57bc94f14e943fad4fe8326181d6c8"></a> uint16\_t conn\_interval\_min
    :   MIN connect interval(conn\_interval\_min \* 1.25ms)

    <a id="_CPPv4N16le_if_cfg_para_t17conn_interval_maxE"></a>

    <a id="_CPPv3N16le_if_cfg_para_t17conn_interval_maxE"></a> <a id="_CPPv2N16le_if_cfg_para_t17conn_interval_maxE"></a> <a id="le_if_cfg_para_t::conn_interval_max__uint16_t"></a> <a id="structle__if__cfg__para__t_1a51bd07e65b74a8ede3297d2b7219eeb2"></a> uint16\_t conn\_interval\_max
    :   MAX connect interval(conn\_interval\_max \* 1.25ms)

    <a id="_CPPv4N16le_if_cfg_para_t13le_audio_paraE"></a>

    <a id="_CPPv3N16le_if_cfg_para_t13le_audio_paraE"></a> <a id="_CPPv2N16le_if_cfg_para_t13le_audio_paraE"></a> <a id="le_if_cfg_para_t::le_audio_para__le_audio_if_para_t"></a> <a id="structle__if__cfg__para__t_1a54b9139f9aa267f671b3bc0b61ee857e"></a> [le\_audio\_if\_para\_t](#_CPPv418le_audio_if_para_t "le_audio_if_para_t") le\_audio\_para
    :   LE audio parameter

<a id="macros"></a>

### Macros

<a id="c.TWS_ASSERT"></a>

<a id="btif__type_8h_1a913b9bcb0e58275bc38999414d0991b1"></a> TWS\_ASSERT(exp)

<a id="c.BTIF_BD_ADDR_LEN"></a>

<a id="btif__type_8h_1aed87d1893675bced32672acb36c96914"></a> BTIF\_BD\_ADDR\_LEN

<a id="c.BTIF_LINK_KEY_LEN"></a>

<a id="btif__type_8h_1af348c49b4f47b6940e949042d7c1f4aa"></a> BTIF\_LINK\_KEY\_LEN

<a id="c.BTIF_INVALID_HANDLE"></a>

<a id="btif__type_8h_1a6a3e51a89500f053d9a94177b1f7d2f9"></a> BTIF\_INVALID\_HANDLE

<a id="c.BTIF_INVALID_CID"></a>

<a id="btif__type_8h_1aded01ac61449a1073c62948314e8b4c1"></a> BTIF\_INVALID\_CID

<a id="c.BTIF_INVALID_PD_TIME"></a>

<a id="btif__type_8h_1a2d8b743fd882b5361093fe2e8069460e"></a> BTIF\_INVALID\_PD\_TIME

<a id="c.BTIF_INVALID_VOL"></a>

<a id="btif__type_8h_1a05f23d3cc08c6100170e509f07da36e4"></a> BTIF\_INVALID\_VOL

<a id="c.BTIF_LE_BASE_HANDLE"></a>

<a id="btif__type_8h_1a5e3e7c19a75a7520e066270231ab9e8f"></a> BTIF\_LE\_BASE\_HANDLE

<a id="c.BTIF_BT_BASE_HANDLE"></a>

<a id="btif__type_8h_1ad027c4cf5e097bdd65b2b2fb270106f3"></a> BTIF\_BT\_BASE\_HANDLE

<a id="c.BTIF_BT_SCO_BASE_HANDLE"></a>

<a id="btif__type_8h_1ad002f2c0070268d03a3dd58e426cfc9f"></a> BTIF\_BT\_SCO\_BASE\_HANDLE

<a id="c.BTIF_CIS_BASE_HANDLE"></a>

<a id="btif__type_8h_1aae02b0ab1f0cca83db0e0a6e55ab0b99"></a> BTIF\_CIS\_BASE\_HANDLE

<a id="c.BTIF_BIS_BASE_HANDLE"></a>

<a id="btif__type_8h_1abd1b376b48e8d018fbe9c43a09419afe"></a> BTIF\_BIS\_BASE\_HANDLE

<a id="c._is_btif_bt_handle"></a>

<a id="btif__type_8h_1a41e784d5c74ca0d27b822a2ec7d8ec59"></a> \_is\_btif\_bt\_handle(handle)

<a id="c._is_btif_le_handle"></a>

<a id="btif__type_8h_1a7872b872f28f2cf6ad652cfd200328cf"></a> \_is\_btif\_le\_handle(handle)

<a id="c._is_btif_cis_handle"></a>

<a id="btif__type_8h_1ac182b12a6b74a8ac7d5bd0e82f01af42"></a> \_is\_btif\_cis\_handle(handle)

<a id="c.FUNC_POSSIBLE_UNUSED"></a>

<a id="btif__type_8h_1a03fd9ff92a96ce2fa8d77316bed6360c"></a> FUNC\_POSSIBLE\_UNUSED

<a id="c.SPP_CONN_MAX_PER_LINK"></a>

<a id="btif__type_8h_1a6010db2bf2ffbf882753c07348bed0fd"></a> SPP\_CONN\_MAX\_PER\_LINK

<a id="c.LE_PUBLIC_ADDR"></a>

<a id="btif__type_8h_1a210e27c2372667cd681445ffb074a508"></a> LE\_PUBLIC\_ADDR
:   Public Device Address (default)

<a id="c.LE_RANDOM_ADDR"></a>

<a id="btif__type_8h_1a4e6327fa79ff1361ae0b7792ac55f0fc"></a> LE\_RANDOM\_ADDR
:   Random Device Address

<a id="c.LE_RPA_OR_PUBLIC_ADDR"></a>

<a id="btif__type_8h_1abfafc76c6a324884a485617e2cb5139b"></a> LE\_RPA\_OR\_PUBLIC\_ADDR
:   Public Identity Address (Corresponds to Resolved Private Address)

<a id="c.LE_RPA_OR_RANDOM_ADDR"></a>

<a id="btif__type_8h_1a392aa46f8c9a1d270413b6b3014fff2c"></a> LE\_RPA\_OR\_RANDOM\_ADDR
:   Random (Static) Identity Address (Corresponds to Resolved Private Address)

<a id="c.BTIF_ATT_ERR_SUCCESS"></a>

<a id="btif__type_8h_1a3299e0ea3b559afcdc46114247e8f4ac"></a> BTIF\_ATT\_ERR\_SUCCESS

<a id="c.BTIF_ATT_ERR_INVALID_HANDLE"></a>

<a id="btif__type_8h_1a7cfb6b1599cea149db6510ed921665c3"></a> BTIF\_ATT\_ERR\_INVALID\_HANDLE

<a id="c.BTIF_ATT_ERR_READ_NOT_PERMITTED"></a>

<a id="btif__type_8h_1aa8c91179a61e42623f7e74a783a79083"></a> BTIF\_ATT\_ERR\_READ\_NOT\_PERMITTED

<a id="c.BTIF_ATT_NOT_PERMITTED"></a>

<a id="btif__type_8h_1a77042395e650f97c52348a1d3e3660d7"></a> BTIF\_ATT\_NOT\_PERMITTED

<a id="c.BTIF_ATT_ERR_INVALID_PDU"></a>

<a id="btif__type_8h_1aff196d10e6d7e538de89188f380ab3f4"></a> BTIF\_ATT\_ERR\_INVALID\_PDU

<a id="c.BTIF_ATT_ERR_AUTHENTICATION"></a>

<a id="btif__type_8h_1abe19942bd07633145dc0775c48c110da"></a> BTIF\_ATT\_ERR\_AUTHENTICATION

<a id="c.BTIF_ATT_ERR_NOT_SUPPORTED"></a>

<a id="btif__type_8h_1a86f588a980e42932f35ac8453e5db010"></a> BTIF\_ATT\_ERR\_NOT\_SUPPORTED

<a id="c.BTIF_ATT_ERR_INVALID_OFFSET"></a>

<a id="btif__type_8h_1a270db0e32a8e13be6dc2c6e3bdbab293"></a> BTIF\_ATT\_ERR\_INVALID\_OFFSET

<a id="c.BTIF_ATT_ERR_AUTHORIZATION"></a>

<a id="btif__type_8h_1afae27ee94f27b527f7ac9d039152ba95"></a> BTIF\_ATT\_ERR\_AUTHORIZATION

<a id="c.BTIF_ATT_ERR_PREPARE_QUEUE_FULL"></a>

<a id="btif__type_8h_1a819a7dcfe0211b83ba00fb9fbce00dc6"></a> BTIF\_ATT\_ERR\_PREPARE\_QUEUE\_FULL

<a id="c.BTIF_ATT_ERR_ATTRIBUTE_NOT_FOUND"></a>

<a id="btif__type_8h_1a88e953feb4119b35f4e7c3201b6806b3"></a> BTIF\_ATT\_ERR\_ATTRIBUTE\_NOT\_FOUND

<a id="c.BTIF_ATT_ERR_ATTRIBUTE_NOT_LONG"></a>

<a id="btif__type_8h_1a72f671447c746b7d079762e1f147251c"></a> BTIF\_ATT\_ERR\_ATTRIBUTE\_NOT\_LONG

<a id="c.BTIF_ATT_ERR_ENCRYPTION_KEY_SIZE"></a>

<a id="btif__type_8h_1a869d4699f95af99384c67948d52e24a5"></a> BTIF\_ATT\_ERR\_ENCRYPTION\_KEY\_SIZE

<a id="c.BTIF_ATT_ERR_INVALID_ATTRIBUTE_LEN"></a>

<a id="btif__type_8h_1a61151f7000bfa1671ee01419fe66f7e2"></a> BTIF\_ATT\_ERR\_INVALID\_ATTRIBUTE\_LEN

<a id="c.BTIF_ATT_ERR_UNLIKELY"></a>

<a id="btif__type_8h_1abfe07b39ad82b381c31a4eb0a546dbb6"></a> BTIF\_ATT\_ERR\_UNLIKELY

<a id="c.BTIF_ATT_ERR_INSUFFICIENT_ENCRYPTION"></a>

<a id="btif__type_8h_1a7051a7b8e8bbf1f37aec019aa2e170ce"></a> BTIF\_ATT\_ERR\_INSUFFICIENT\_ENCRYPTION

<a id="c.BTIF_ATT_ERR_UNSUPPORTED_GROUP_TYPE"></a>

<a id="btif__type_8h_1a052b00c27c6ee7ebcb6f8f41660b515a"></a> BTIF\_ATT\_ERR\_UNSUPPORTED\_GROUP\_TYPE

<a id="c.BTIF_ATT_ERR_INSUFFICIENT_RESOURCES"></a>

<a id="btif__type_8h_1a11436e184b00454585d9c86cf519ffad"></a> BTIF\_ATT\_ERR\_INSUFFICIENT\_RESOURCES

<a id="c.BTIF_ATT_ERR_DB_OUT_OF_SYNC"></a>

<a id="btif__type_8h_1a8225c78a62dd1693ce0ca5d374185b41"></a> BTIF\_ATT\_ERR\_DB\_OUT\_OF\_SYNC

<a id="c.BTIF_ATT_ERR_VALUE_NOT_ALLOWED"></a>

<a id="btif__type_8h_1a55c08563244e7da7291ae9cf7c799a21"></a> BTIF\_ATT\_ERR\_VALUE\_NOT\_ALLOWED

<a id="c.BTIF_UUID_BASIC_AUDIO_ANC_SVC"></a>

<a id="btif__type_8h_1a09fc791cd903c78fa280345c28e0b7bc"></a> BTIF\_UUID\_BASIC\_AUDIO\_ANC\_SVC

<a id="c.BTIF_UUID_BRDCST_AUDIO_ANC_SVC"></a>

<a id="btif__type_8h_1a7a97a626e00e0c135a7b8115edbb5366"></a> BTIF\_UUID\_BRDCST\_AUDIO\_ANC\_SVC

<a id="c.BTIF_UUID_PUB_BRDCST_ANC_SVC"></a>

<a id="btif__type_8h_1aa0633f38d834422768e1fe35606506a4"></a> BTIF\_UUID\_PUB\_BRDCST\_ANC\_SVC

<a id="c.BTIF_UUID16_INIT"></a>

<a id="btif__type_8h_1a18bb59d0a92c5b83a713203189ab13f6"></a> BTIF\_UUID16\_INIT(value)

<a id="c.BTIF_UUID32_INIT"></a>

<a id="btif__type_8h_1ae7cd72b289ca869e67fb1fbac06a25ae"></a> BTIF\_UUID32\_INIT(value)

<a id="c.BTIF_UUID128_INIT"></a>

<a id="btif__type_8h_1aa40e1d5f1b35685fe6676cea25c68d89"></a> BTIF\_UUID128\_INIT(value...)

<a id="c.BTIF_UUID_DECLARE_16"></a>

<a id="btif__type_8h_1a2eaa6b058f780edfc43afc232149ca55"></a> BTIF\_UUID\_DECLARE\_16(value)

<a id="c.BTIF_UUID_DECLARE_32"></a>

<a id="btif__type_8h_1a8e9e64bcf392aaf2f8d48f0ea6dcf273"></a> BTIF\_UUID\_DECLARE\_32(value)

<a id="c.BTIF_UUID_DECLARE_128"></a>

<a id="btif__type_8h_1ae9694695503ce51d3d0b318611453922"></a> BTIF\_UUID\_DECLARE\_128(value...)

<a id="c.BTIF_EXIT_SUCCESS"></a>

<a id="btif__type_8h_1a7685752d0663fbca26e1aa08caef2475"></a> BTIF\_EXIT\_SUCCESS

<a id="c.BTIF_EXIT_FAIL"></a>

<a id="btif__type_8h_1abab9e55b6ae9a298ef1c84fd8099114f"></a> BTIF\_EXIT\_FAIL

<a id="c.BTIF_EXIT_REPEAT_SET"></a>

<a id="btif__type_8h_1a2c8f94e3bcdad53e8544e791dd6eabc7"></a> BTIF\_EXIT\_REPEAT\_SET

<a id="c.BTIF_BT_ROLE_MASTER"></a>

<a id="btif__type_8h_1a1bd5b90618dab6daf8ce8be189400995"></a> BTIF\_BT\_ROLE\_MASTER

<a id="c.BTIF_BT_ROLE_SLAVE"></a>

<a id="btif__type_8h_1af7bb1d768481e14eac94c08a24f860db"></a> BTIF\_BT\_ROLE\_SLAVE

<a id="c.BTIF_BT_ROLE_UNKNOWN"></a>

<a id="btif__type_8h_1a3fef65017871b4068778b28971e76ec5"></a> BTIF\_BT\_ROLE\_UNKNOWN

<a id="c.BTIF_TWS_ROLE_UNKNOWN"></a>

<a id="btif__type_8h_1aa0b378642f0ff0a25092a6084f23e206"></a> BTIF\_TWS\_ROLE\_UNKNOWN

<a id="c.BTIF_TWS_ROLE_MASTER"></a>

<a id="btif__type_8h_1a547ac4df1cbdb2a3f1bcdc61eff458f9"></a> BTIF\_TWS\_ROLE\_MASTER

<a id="c.BTIF_TWS_ROLE_SLAVE"></a>

<a id="btif__type_8h_1a0dff2c4c218a3246e12ff80a2b6446fe"></a> BTIF\_TWS\_ROLE\_SLAVE

<a id="c.BTIF_SYNC_PROF_IDLE"></a>

<a id="btif__type_8h_1aacf093d131aebe26f5a0a49f2b0885de"></a> BTIF\_SYNC\_PROF\_IDLE

<a id="c.BTIF_SYNC_PROF_ONGOING"></a>

<a id="btif__type_8h_1a9618ed5a3d276e8d5a0ec305687d7497"></a> BTIF\_SYNC\_PROF\_ONGOING

<a id="c.BTIF_SYNC_PROF_DONE"></a>

<a id="btif__type_8h_1aa0cd2a311358f446632172b2a0cbf05c"></a> BTIF\_SYNC\_PROF\_DONE

<a id="c.BTIF_ENABLE_NONE_SCAN"></a>

<a id="btif__type_8h_1aa4a44eae28f6cf899c607a704826af38"></a> BTIF\_ENABLE\_NONE\_SCAN

<a id="c.BTIF_ENABLE_ISCAN"></a>

<a id="btif__type_8h_1ac741b41b6761cf6a71002042e2b58cca"></a> BTIF\_ENABLE\_ISCAN

<a id="c.BTIF_ENABLE_PSCAN"></a>

<a id="btif__type_8h_1aea3a7818794b74930e6abf66c1d81f49"></a> BTIF\_ENABLE\_PSCAN

<a id="c.BTIF_ENABLE_BOTH_SCAN"></a>

<a id="btif__type_8h_1a6dde2d299cb74ecd49461a982304ddbb"></a> BTIF\_ENABLE\_BOTH\_SCAN

<a id="c.BTIF_PROFILE_NONE"></a>

<a id="btif__type_8h_1ae10d1984690b524ccedf6a265caf179a"></a> BTIF\_PROFILE\_NONE

<a id="c.BTIF_PROFILE_A2DP_SIG"></a>

<a id="btif__type_8h_1ac770f3575c9d4ce9fb2a5d1f0f56a5e5"></a> BTIF\_PROFILE\_A2DP\_SIG

<a id="c.BTIF_PROFILE_A2DP_MEDIA"></a>

<a id="btif__type_8h_1a4ea08e89f52a5b53c0b0f6f6f30c5553"></a> BTIF\_PROFILE\_A2DP\_MEDIA

<a id="c.BTIF_PROFILE_AVRCP"></a>

<a id="btif__type_8h_1a9819a1e4681f62249ad238b382ee7d31"></a> BTIF\_PROFILE\_AVRCP

<a id="c.BTIF_PROFILE_HFP"></a>

<a id="btif__type_8h_1abae13a5ebb1eae3dd63c46da77feb9c1"></a> BTIF\_PROFILE\_HFP

<a id="c.BTIF_PROFILE_ACL"></a>

<a id="btif__type_8h_1a0dd30fa7829176024331030c6a3c611f"></a> BTIF\_PROFILE\_ACL

<a id="c.BTIF_PROFILE_SPP"></a>

<a id="btif__type_8h_1a06a1c45e6ee723b1161e240196ff718f"></a> BTIF\_PROFILE\_SPP

<a id="c.BTIF_PROFILE_GATT_OVER_BREDR"></a>

<a id="btif__type_8h_1a805bcb98508bbc7e11183316c32fb1b4"></a> BTIF\_PROFILE\_GATT\_OVER\_BREDR

<a id="c.BTIF_PROFILE_HID"></a>

<a id="btif__type_8h_1a2a3b71a3f9ab999270b98bfa1b589ea6"></a> BTIF\_PROFILE\_HID

<a id="c.ERROR_UNKNOWN_HCI_COMMAND"></a>

<a id="btif__type_8h_1a0628b71cfb3e12f267b7b5b38768db13"></a> ERROR\_UNKNOWN\_HCI\_COMMAND

<a id="c.ERROR_UNKNOWN_CONNECTION_IDENTIFIER"></a>

<a id="btif__type_8h_1a14651710008ee1725e12346dc9e3a309"></a> ERROR\_UNKNOWN\_CONNECTION\_IDENTIFIER

<a id="c.ERROR_HARDWARE_FAILURE"></a>

<a id="btif__type_8h_1a9da2f1805d91fd112ba8c4fc70148558"></a> ERROR\_HARDWARE\_FAILURE

<a id="c.ERROR_PAGE_TIMEOUT"></a>

<a id="btif__type_8h_1a580dcc10fa425a8a96a66cf16bd46c21"></a> ERROR\_PAGE\_TIMEOUT

<a id="c.ERROR_AUTHENTICATION_FAILURE"></a>

<a id="btif__type_8h_1aabc5f2ac1d63d2cb9735803c60d1c248"></a> ERROR\_AUTHENTICATION\_FAILURE

<a id="c.ERROR_PIN_OR_KEY_MISSING"></a>

<a id="btif__type_8h_1acc2ed31f46e7bdaa2b6f7a8ab59fdd18"></a> ERROR\_PIN\_OR\_KEY\_MISSING

<a id="c.ERROR_MEMORY_CAPACITY_EXCEEDED"></a>

<a id="btif__type_8h_1a522fe909587d4cd33f0d53d76635d6c5"></a> ERROR\_MEMORY\_CAPACITY\_EXCEEDED

<a id="c.ERROR_CONNECTION_TIMEOUT"></a>

<a id="btif__type_8h_1ae932f01f8afd52ff73991fda343d56fd"></a> ERROR\_CONNECTION\_TIMEOUT

<a id="c.ERROR_CONNECTION_LIMIT_EXCEEDED"></a>

<a id="btif__type_8h_1afbd8677465622fc07498b0239b540cfa"></a> ERROR\_CONNECTION\_LIMIT\_EXCEEDED

<a id="c.ERROR_SYNCHRONOUS_CONNECTION_LIMIT_TO_A_DEVICE_EXCEEDED"></a>

<a id="btif__type_8h_1aee6755349b386f281f100af5e5a33536"></a> ERROR\_SYNCHRONOUS\_CONNECTION\_LIMIT\_TO\_A\_DEVICE\_EXCEEDED

<a id="c.ERROR_ACL_CONNECTION_ALREADY_EXISTS"></a>

<a id="btif__type_8h_1ae698addfa8f14ffbaa90c683667f7bea"></a> ERROR\_ACL\_CONNECTION\_ALREADY\_EXISTS

<a id="c.ERROR_COMMAND_DISALLOWED"></a>

<a id="btif__type_8h_1adac96f86c56da66f2df301d326c2209e"></a> ERROR\_COMMAND\_DISALLOWED

<a id="c.ERROR_CONNECTION_REJECTED_DUE_TO_LIMITED_RESOURCES"></a>

<a id="btif__type_8h_1ac4180520049989693a30dc608299dacb"></a> ERROR\_CONNECTION\_REJECTED\_DUE\_TO\_LIMITED\_RESOURCES

<a id="c.ERROR_CONNECTION_REJECTED_DUE_TO_SECURITY_REASONS"></a>

<a id="btif__type_8h_1ad08fd1258d9a26a53f57c8da98bbf33d"></a> ERROR\_CONNECTION\_REJECTED\_DUE\_TO\_SECURITY\_REASONS

<a id="c.ERROR_CONNECTION_REJECTED_DUE_TO_UNACCEPTABLE_BD_ADDR"></a>

<a id="btif__type_8h_1a5f393ffd06dfd01de6b7a19570467566"></a> ERROR\_CONNECTION\_REJECTED\_DUE\_TO\_UNACCEPTABLE\_BD\_ADDR

<a id="c.ERROR_CONNECTION_ACCEPT_TIMEOUT_EXCEEDED"></a>

<a id="btif__type_8h_1a6b07838e174e43aea43f18c4671e9d39"></a> ERROR\_CONNECTION\_ACCEPT\_TIMEOUT\_EXCEEDED

<a id="c.ERROR_UNSUPPORTED_FEATURE_OR_PARAMETER_VALUE"></a>

<a id="btif__type_8h_1a05fa913a1bda51805b824fc77bbb33e9"></a> ERROR\_UNSUPPORTED\_FEATURE\_OR\_PARAMETER\_VALUE

<a id="c.ERROR_INVALID_HCI_COMMAND_PARAMETERS"></a>

<a id="btif__type_8h_1a61d779e38753a18c4362b1ada07b6ca6"></a> ERROR\_INVALID\_HCI\_COMMAND\_PARAMETERS

<a id="c.ERROR_REMOTE_USER_TERMINATED_CONNECTION"></a>

<a id="btif__type_8h_1af5b2278f7da7ecbc9c55f71d82f1883a"></a> ERROR\_REMOTE\_USER\_TERMINATED\_CONNECTION

<a id="c.ERROR_REMOTE_DEVICE_TERMINATED_CONNECTION_DUE_TO_LOW_RESOURCES"></a>

<a id="btif__type_8h_1a8e803a5a87e2023b08b031e37b483de9"></a> ERROR\_REMOTE\_DEVICE\_TERMINATED\_CONNECTION\_DUE\_TO\_LOW\_RESOURCES

<a id="c.ERROR_REMOTE_DEVICE_TERMINATED_CONNECTION_DUE_TO_POWER_OFF"></a>

<a id="btif__type_8h_1aab6e9e3792a030168695337d74db4182"></a> ERROR\_REMOTE\_DEVICE\_TERMINATED\_CONNECTION\_DUE\_TO\_POWER\_OFF

<a id="c.ERROR_CONNECTION_TERMINATED_BY_LOCAL_HOST"></a>

<a id="btif__type_8h_1ab1e125f16ec30f80f71d5083c7c65406"></a> ERROR\_CONNECTION\_TERMINATED\_BY\_LOCAL\_HOST

<a id="c.ERROR_REPEATED_ATTEMPTS"></a>

<a id="btif__type_8h_1aa9f36e5a0cc2e8605a77d7d30414b6f7"></a> ERROR\_REPEATED\_ATTEMPTS

<a id="c.ERROR_PAIRING_NOT_ALLOWED"></a>

<a id="btif__type_8h_1aac2cb51b9024f912cfa243b2297cb9dc"></a> ERROR\_PAIRING\_NOT\_ALLOWED

<a id="c.ERROR_UNKNOWN_LMP_PDU"></a>

<a id="btif__type_8h_1a26f925955713b8b38f5de5e029e23ea1"></a> ERROR\_UNKNOWN\_LMP\_PDU

<a id="c.ERROR_UNSUPPORTED_REMOTE_FEATURE_UNSUPPORTED_LMP_FEATURE"></a>

<a id="btif__type_8h_1ab22e7037de3f502c6a2e50d6e4117b0b"></a> ERROR\_UNSUPPORTED\_REMOTE\_FEATURE\_UNSUPPORTED\_LMP\_FEATURE

<a id="c.ERROR_SCO_OFFSET_REJECTED"></a>

<a id="btif__type_8h_1a27cee862079f3aa91cb6c77e928392d6"></a> ERROR\_SCO\_OFFSET\_REJECTED

<a id="c.ERROR_SCO_INTERVAL_REJECTED"></a>

<a id="btif__type_8h_1a4a1b27708f6797afcb26a7aa3844d208"></a> ERROR\_SCO\_INTERVAL\_REJECTED

<a id="c.ERROR_SCO_AIR_MODE_REJECTED"></a>

<a id="btif__type_8h_1ade2995dd7dc4a3c5296d0247bd235e4b"></a> ERROR\_SCO\_AIR\_MODE\_REJECTED

<a id="c.ERROR_INVALID_LMP_PARAMETERS_INVALID_LL_PARAMETERS"></a>

<a id="btif__type_8h_1a48c3a6925bd3a2a6c4e3b6161c0e6ace"></a> ERROR\_INVALID\_LMP\_PARAMETERS\_INVALID\_LL\_PARAMETERS

<a id="c.ERROR_UNSPECIFIED_ERROR"></a>

<a id="btif__type_8h_1a4c6b048ea6088e1533f4629a31f7ea84"></a> ERROR\_UNSPECIFIED\_ERROR

<a id="c.ERROR_UNSUPPORTED_LMP_PARAMETER_VALUE_UNSUPPORTED_LL_PARAMETER_VALUE"></a>

<a id="btif__type_8h_1a3db870e94f8038ff98f6f97c7c41fef6"></a> ERROR\_UNSUPPORTED\_LMP\_PARAMETER\_VALUE\_UNSUPPORTED\_LL\_PARAMETER\_VALUE

<a id="c.ERROR_ROLE_CHANGE_NOT_ALLOWED"></a>

<a id="btif__type_8h_1a5138027912bfc4a5a8a68b4b5d8ffb73"></a> ERROR\_ROLE\_CHANGE\_NOT\_ALLOWED

<a id="c.ERROR_LMP_RESPONSE_TIMEOUT_LL_RESPONSE_TIMEOUT"></a>

<a id="btif__type_8h_1a250555236df2c9d04211b3044df0adca"></a> ERROR\_LMP\_RESPONSE\_TIMEOUT\_LL\_RESPONSE\_TIMEOUT

<a id="c.ERROR_LMP_ERROR_TRANSACTION_COLLISION"></a>

<a id="btif__type_8h_1a33630993a8ac398a811ca3491cdb57dd"></a> ERROR\_LMP\_ERROR\_TRANSACTION\_COLLISION

<a id="c.ERROR_LMP_PDU_NOT_ALLOWED"></a>

<a id="btif__type_8h_1adf82e94d9164e0bef77af14b5fabb74e"></a> ERROR\_LMP\_PDU\_NOT\_ALLOWED

<a id="c.ERROR_ENCRYPTION_MODE_NOT_ACCEPTABLE"></a>

<a id="btif__type_8h_1ae949788c8a4ac829d218ba486542cb7e"></a> ERROR\_ENCRYPTION\_MODE\_NOT\_ACCEPTABLE

<a id="c.ERROR_LINK_KEY_CANNOT_BE_CHANGED"></a>

<a id="btif__type_8h_1a9be8b646798ea406d2c7f06663f7bee4"></a> ERROR\_LINK\_KEY\_CANNOT\_BE\_CHANGED

<a id="c.ERROR_REQUESTED_QOS_NOT_SUPPORTED"></a>

<a id="btif__type_8h_1a4c257144807cd97aebb5df07eff7ac64"></a> ERROR\_REQUESTED\_QOS\_NOT\_SUPPORTED

<a id="c.ERROR_INSTANT_PASSED"></a>

<a id="btif__type_8h_1abbd49858b4a8fdaaba6a0d0ae2524d67"></a> ERROR\_INSTANT\_PASSED

<a id="c.ERROR_PAIRING_WITH_UNIT_KEY_NOT_SUPPORTED"></a>

<a id="btif__type_8h_1a7827fbc2599d99100407a77630c00fb5"></a> ERROR\_PAIRING\_WITH\_UNIT\_KEY\_NOT\_SUPPORTED

<a id="c.ERROR_DIFFERENT_TRANSACTION_COLLISION"></a>

<a id="btif__type_8h_1aa01515a1a49c24006f72477321d21524"></a> ERROR\_DIFFERENT\_TRANSACTION\_COLLISION

<a id="c.ERROR_RESERVED"></a>

<a id="btif__type_8h_1a1bbdf5f1293ddf2a333be5545f92db96"></a> ERROR\_RESERVED

<a id="c.ERROR_QOS_UNACCEPTABLE_PARAMETER"></a>

<a id="btif__type_8h_1a2acdf9d03699a2694d300f50d2234454"></a> ERROR\_QOS\_UNACCEPTABLE\_PARAMETER

<a id="c.ERROR_QOS_REJECTED"></a>

<a id="btif__type_8h_1a81f6ef844ec6ccf4f89bc6a5abd6c285"></a> ERROR\_QOS\_REJECTED

<a id="c.ERROR_CHANNEL_CLASSIFICATION_NOT_SUPPORTED"></a>

<a id="btif__type_8h_1a7d48a3c5790feb93b56d5ad7660b05e1"></a> ERROR\_CHANNEL\_CLASSIFICATION\_NOT\_SUPPORTED

<a id="c.ERROR_INSUFFICIENT_SECURITY"></a>

<a id="btif__type_8h_1a2bce139579c9240564e6595bc47229b7"></a> ERROR\_INSUFFICIENT\_SECURITY

<a id="c.ERROR_PARAMETER_OUT_OF_MANDATORY_RANGE"></a>

<a id="btif__type_8h_1a698eece4eb2df800435d6ab38806862f"></a> ERROR\_PARAMETER\_OUT\_OF\_MANDATORY\_RANGE

<a id="c.ERROR_ROLE_SWITCH_PENDING"></a>

<a id="btif__type_8h_1a27ddc663903283e59779825e46296ee1"></a> ERROR\_ROLE\_SWITCH\_PENDING

<a id="c.ERROR_RESERVED_SLOT_VIOLATION"></a>

<a id="btif__type_8h_1ae63030d241c6cc9e88398d79713183b2"></a> ERROR\_RESERVED\_SLOT\_VIOLATION

<a id="c.ERROR_ROLE_SWITCH_FAILED"></a>

<a id="btif__type_8h_1ae3939017541f044fe0d490fe347b93d9"></a> ERROR\_ROLE\_SWITCH\_FAILED

<a id="c.ERROR_EXTENDED_INQUIRY_RESPONSE_TOO_LARGE"></a>

<a id="btif__type_8h_1a22aabc607cb5db5d5f4778022f47ccc1"></a> ERROR\_EXTENDED\_INQUIRY\_RESPONSE\_TOO\_LARGE

<a id="c.ERROR_SECURE_SIMPLE_PAIRING_NOT_SUPPORTED_BY_HOST"></a>

<a id="btif__type_8h_1ab9b2d55d23608de86f78244c705fab5d"></a> ERROR\_SECURE\_SIMPLE\_PAIRING\_NOT\_SUPPORTED\_BY\_HOST

<a id="c.ERROR_HOST_BUSY_PAIRING"></a>

<a id="btif__type_8h_1a8baf0b3bf6576bc2f2025d0c671653b6"></a> ERROR\_HOST\_BUSY\_PAIRING

<a id="c.ERROR_CONNECTION_REJECTED_DUE_TO_NO_SUITABLE_CHANNEL_FOUND"></a>

<a id="btif__type_8h_1a2b498c4229de5579ceaa8fa5e4904a8c"></a> ERROR\_CONNECTION\_REJECTED\_DUE\_TO\_NO\_SUITABLE\_CHANNEL\_FOUND

<a id="c.ERROR_CONTROLLER_BUSY"></a>

<a id="btif__type_8h_1aba36aa11837eac5ee75ff264f3790310"></a> ERROR\_CONTROLLER\_BUSY

<a id="c.ERROR_UNACCEPTABLE_CONNECTION_PARAMETERS"></a>

<a id="btif__type_8h_1a4bcbe3508139820ce94799291e64afe8"></a> ERROR\_UNACCEPTABLE\_CONNECTION\_PARAMETERS

<a id="c.ERROR_DIRECTED_ADVERTISING_TIMEOUT"></a>

<a id="btif__type_8h_1a6aafc15ae72424bb50b9ae678946a72b"></a> ERROR\_DIRECTED\_ADVERTISING\_TIMEOUT

<a id="c.ERROR_CONNECTION_TERMINATED_DUE_TO_MIC_FAILURE"></a>

<a id="btif__type_8h_1a589e175a8c51daa26b03980fdc7984cf"></a> ERROR\_CONNECTION\_TERMINATED\_DUE\_TO\_MIC\_FAILURE

<a id="c.ERROR_CONNECTION_FAILED_TO_BE_ESTABLISHED"></a>

<a id="btif__type_8h_1afe9347d0f0b5f161a90e79dda2738004"></a> ERROR\_CONNECTION\_FAILED\_TO\_BE\_ESTABLISHED

<a id="c.ERROR_MAC_CONNECTION_FAILED"></a>

<a id="btif__type_8h_1a8230404b4eb666b2a6c277a725e15aea"></a> ERROR\_MAC\_CONNECTION\_FAILED

<a id="c.ERROR_COARSE_CLOCK_ADJUSTMENT_REJECTED_BUT_WILL_TRY_TO_ADJUST_USING_CLOCK_DRAGGING"></a>

<a id="btif__type_8h_1affd248b11ea6dc7dff1ec3331b5bfa34"></a> ERROR\_COARSE\_CLOCK\_ADJUSTMENT\_REJECTED\_BUT\_WILL\_TRY\_TO\_ADJUST\_USING\_CLOCK\_DRAGGING

<a id="c.ERROR_RESTORE_ONGOING"></a>

<a id="btif__type_8h_1a708404a1197bcc35904bbe2c17fb4178"></a> ERROR\_RESTORE\_ONGOING

<a id="c.ERROR_PAGE_CANCEL_BY_BTC"></a>

<a id="btif__type_8h_1aa742eba2f2d4d9cb8ecc75ef8414d40e"></a> ERROR\_PAGE\_CANCEL\_BY\_BTC

<a id="c.ERROR_SP_DISC_DUE_TO_TWS_DISC"></a>

<a id="btif__type_8h_1a2276f2a73553262b3698e4f1f0e8fe17"></a> ERROR\_SP\_DISC\_DUE\_TO\_TWS\_DISC

<a id="c.ERROR_SP_DISC_DUE_TO_TWS_TO"></a>

<a id="btif__type_8h_1a618eeaa466a2aebf0b52202dfa2e9d0c"></a> ERROR\_SP\_DISC\_DUE\_TO\_TWS\_TO

<a id="c.ERROR_DISC_DUE_TO_FORCE_STOP"></a>

<a id="btif__type_8h_1a0fc305e8f8bd9cd48d04feb6954a2276"></a> ERROR\_DISC\_DUE\_TO\_FORCE\_STOP

<a id="c.ERROR_VENDOR_RESTORE_DISCONNECT"></a>

<a id="btif__type_8h_1a7b790e6e3418714c43d0536be16b492d"></a> ERROR\_VENDOR\_RESTORE\_DISCONNECT

<a id="c.BTIF_AD_TYPE_FLAGS"></a>

<a id="btif__type_8h_1a129358b17c5bbf2b9e9132c15af30b9c"></a> BTIF\_AD\_TYPE\_FLAGS

<a id="c.BTIF_AD_TYPE_INCOMPLETE_LIST_OF_16_BIT_SERVICE_CLASS_UUIDS"></a>

<a id="btif__type_8h_1a7550d144fd8107e6f70ad244923e8896"></a> BTIF\_AD\_TYPE\_INCOMPLETE\_LIST\_OF\_16\_BIT\_SERVICE\_CLASS\_UUIDS

<a id="c.BTIF_AD_TYPE_COMPLETE_LIST_OF_16_BIT_SERVICE_CLASS_UUIDS"></a>

<a id="btif__type_8h_1a49c0a456b143c1b2cc14849570a39199"></a> BTIF\_AD\_TYPE\_COMPLETE\_LIST\_OF\_16\_BIT\_SERVICE\_CLASS\_UUIDS

<a id="c.BTIF_AD_TYPE_INCOMPLETE_LIST_OF_32_BIT_SERVICE_CLASS_UUIDS"></a>

<a id="btif__type_8h_1a537b4b621c8b6382f79f60931eda8403"></a> BTIF\_AD\_TYPE\_INCOMPLETE\_LIST\_OF\_32\_BIT\_SERVICE\_CLASS\_UUIDS

<a id="c.BTIF_AD_TYPE_COMPLETE_LIST_OF_32_BIT_SERVICE_CLASS_UUIDS"></a>

<a id="btif__type_8h_1ad3a06dd3c89eb9d5741fccf1ef879b03"></a> BTIF\_AD\_TYPE\_COMPLETE\_LIST\_OF\_32\_BIT\_SERVICE\_CLASS\_UUIDS

<a id="c.BTIF_AD_TYPE_INCOMPLETE_LIST_OF_128_BIT_SERVICE_CLASS_UUIDS"></a>

<a id="btif__type_8h_1a2431b7e605aed8a1e4da4f2cdeced336"></a> BTIF\_AD\_TYPE\_INCOMPLETE\_LIST\_OF\_128\_BIT\_SERVICE\_CLASS\_UUIDS

<a id="c.BTIF_AD_TYPE_COMPLETE_LIST_OF_128_BIT_SERVICE_CLASS_UUIDS"></a>

<a id="btif__type_8h_1add540d52cc54a286cbfc68eb7873dbf2"></a> BTIF\_AD\_TYPE\_COMPLETE\_LIST\_OF\_128\_BIT\_SERVICE\_CLASS\_UUIDS

<a id="c.BTIF_AD_TYPE_SHORTENED_LOCAL_NAME"></a>

<a id="btif__type_8h_1a80fb3f8cfa7e51cb90f543e461f9b0b0"></a> BTIF\_AD\_TYPE\_SHORTENED\_LOCAL\_NAME

<a id="c.BTIF_AD_TYPE_COMPLETE_LOCAL_NAME"></a>

<a id="btif__type_8h_1a0568749599d87cd9d22e498a02d19bc2"></a> BTIF\_AD\_TYPE\_COMPLETE\_LOCAL\_NAME

<a id="c.BTIF_AD_TYPE_TX_POWER_LEVEL"></a>

<a id="btif__type_8h_1a4d4b33e6e6575142b777ed1c6b7bcc44"></a> BTIF\_AD\_TYPE\_TX\_POWER\_LEVEL

<a id="c.BTIF_AD_TYPE_CLASS_OF_DEVICE"></a>

<a id="btif__type_8h_1ab3344dd42dc90138082a2ed8339ce886"></a> BTIF\_AD\_TYPE\_CLASS\_OF\_DEVICE

<a id="c.BTIF_AD_TYPE_SIMPLE_PAIRING_HASH_C"></a>

<a id="btif__type_8h_1ac1e6b256d7d28685f3399a0944222489"></a> BTIF\_AD\_TYPE\_SIMPLE\_PAIRING\_HASH\_C

<a id="c.BTIF_AD_TYPE_SIMPLE_PAIRING_HASH_C_192"></a>

<a id="btif__type_8h_1a0559964aad2667e95941810bf3d8d63d"></a> BTIF\_AD\_TYPE\_SIMPLE\_PAIRING\_HASH\_C\_192

<a id="c.BTIF_AD_TYPE_SIMPLE_PAIRING_RANDOMIZER_R"></a>

<a id="btif__type_8h_1a30bfcd17a945140c1b9b8aa0249f78bd"></a> BTIF\_AD\_TYPE\_SIMPLE\_PAIRING\_RANDOMIZER\_R

<a id="c.BTIF_AD_TYPE_SIMPLE_PAIRING_RANDOMIZER_R_192"></a>

<a id="btif__type_8h_1a206ba3407c9bfe46370afdf23dbd3306"></a> BTIF\_AD\_TYPE\_SIMPLE\_PAIRING\_RANDOMIZER\_R\_192

<a id="c.BTIF_AD_TYPE_DEVICE_ID"></a>

<a id="btif__type_8h_1aac9f90443999bf56d458fc466a8c3249"></a> BTIF\_AD\_TYPE\_DEVICE\_ID

<a id="c.BTIF_AD_TYPE_SECURITY_MANAGER_TK_VALUE"></a>

<a id="btif__type_8h_1a07a3ef1b2b68199688d3f0c13dc20a44"></a> BTIF\_AD\_TYPE\_SECURITY\_MANAGER\_TK\_VALUE

<a id="c.BTIF_AD_TYPE_SECURITY_MANAGER_OUT_OF_BAND_FLAGS"></a>

<a id="btif__type_8h_1a78989b7d6cd014d6e49944bdd809ae1d"></a> BTIF\_AD\_TYPE\_SECURITY\_MANAGER\_OUT\_OF\_BAND\_FLAGS

<a id="c.BTIF_AD_TYPE_SLAVE_CONNECTION_INTERVAL_RANGE"></a>

<a id="btif__type_8h_1a8ed5c231c7ead69ebef4f82797f11674"></a> BTIF\_AD\_TYPE\_SLAVE\_CONNECTION\_INTERVAL\_RANGE

<a id="c.BTIF_AD_TYPE_LIST_OF_16_BIT_SERVICE_SOLICITATION_UUIDS"></a>

<a id="btif__type_8h_1a20b3bec0170ed262f6f4ba68d4988fa3"></a> BTIF\_AD\_TYPE\_LIST\_OF\_16\_BIT\_SERVICE\_SOLICITATION\_UUIDS

<a id="c.BTIF_AD_TYPE_LIST_OF_128_BIT_SERVICE_SOLICITATION_UUIDS"></a>

<a id="btif__type_8h_1a59c108f6661bb8bb7a99d3feb23bc1b2"></a> BTIF\_AD\_TYPE\_LIST\_OF\_128\_BIT\_SERVICE\_SOLICITATION\_UUIDS

<a id="c.BTIF_AD_TYPE_SERVICE_DATA"></a>

<a id="btif__type_8h_1a8bbd3335260314811b4ce57e4ef7dd85"></a> BTIF\_AD\_TYPE\_SERVICE\_DATA

<a id="c.BTIF_AD_TYPE_SERVICE_DATA_16_BIT_UUID"></a>

<a id="btif__type_8h_1a7b379b3715e9ed6c7261664e5ead76c0"></a> BTIF\_AD\_TYPE\_SERVICE\_DATA\_16\_BIT\_UUID

<a id="c.BTIF_AD_TYPE_PUBLIC_TARGET_ADDRESS"></a>

<a id="btif__type_8h_1aa5310609650169be30e96636220397f8"></a> BTIF\_AD\_TYPE\_PUBLIC\_TARGET\_ADDRESS

<a id="c.BTIF_AD_TYPE_RANDOM_TARGET_ADDRESS"></a>

<a id="btif__type_8h_1a830967a993789a9c0a45166fe38006dd"></a> BTIF\_AD\_TYPE\_RANDOM\_TARGET\_ADDRESS

<a id="c.BTIF_AD_TYPE_APPEARANCE"></a>

<a id="btif__type_8h_1a78a4800f9b6b763129be2e3b2b7fb931"></a> BTIF\_AD\_TYPE\_APPEARANCE

<a id="c.BTIF_AD_TYPE_ADVERTISING_INTERVAL"></a>

<a id="btif__type_8h_1a00cab2ef162376249b31c9db502c0c3a"></a> BTIF\_AD\_TYPE\_ADVERTISING\_INTERVAL

<a id="c.BTIF_AD_TYPE_LE_BLUETOOTH_DEVICE_ADDRESS"></a>

<a id="btif__type_8h_1aa68d63a6453b0cb5955b7e78eb3d4e07"></a> BTIF\_AD\_TYPE\_LE\_BLUETOOTH\_DEVICE\_ADDRESS

<a id="c.BTIF_AD_TYPE_LE_ROLE"></a>

<a id="btif__type_8h_1a83113ed3d587114de99a6e3d364bde06"></a> BTIF\_AD\_TYPE\_LE\_ROLE

<a id="c.BTIF_AD_TYPE_SIMPLE_PAIRING_HASH_C_256"></a>

<a id="btif__type_8h_1a3ba5bf8da07eac521cbbbe5c866d7751"></a> BTIF\_AD\_TYPE\_SIMPLE\_PAIRING\_HASH\_C\_256

<a id="c.BTIF_AD_TYPE_SIMPLE_PAIRING_RANDOMIZER_R_256"></a>

<a id="btif__type_8h_1aee809edb85a14ee085295f9681544872"></a> BTIF\_AD\_TYPE\_SIMPLE\_PAIRING\_RANDOMIZER\_R\_256

<a id="c.BTIF_AD_TYPE_LIST_OF_32_BIT_SERVICE_SOLICITATION_UUIDS"></a>

<a id="btif__type_8h_1ad07859f8daccb61598831fdeb6a425ac"></a> BTIF\_AD\_TYPE\_LIST\_OF\_32\_BIT\_SERVICE\_SOLICITATION\_UUIDS

<a id="c.BTIF_AD_TYPE_SERVICE_DATA_32_BIT_UUID"></a>

<a id="btif__type_8h_1a9553e36918f0218ae25b50a7a29ad806"></a> BTIF\_AD\_TYPE\_SERVICE\_DATA\_32\_BIT\_UUID

<a id="c.BTIF_AD_TYPE_SERVICE_DATA_128_BIT_UUID"></a>

<a id="btif__type_8h_1a695e8c85fdb84c8bff0f2c31251e3de1"></a> BTIF\_AD\_TYPE\_SERVICE\_DATA\_128\_BIT\_UUID

<a id="c.BTIF_AD_TYPE_LE_SECURE_CONNECTIONS_CONFIRMATION_VALUE"></a>

<a id="btif__type_8h_1a9ffde1c5b0d9369bcd00f5cbf54f2139"></a> BTIF\_AD\_TYPE\_LE\_SECURE\_CONNECTIONS\_CONFIRMATION\_VALUE

<a id="c.BTIF_AD_TYPE_LE_SECURE_CONNECTIONS_RANDOM_VALUE"></a>

<a id="btif__type_8h_1a41b1b886097501117df051d81fb959b1"></a> BTIF\_AD\_TYPE\_LE\_SECURE\_CONNECTIONS\_RANDOM\_VALUE

<a id="c.BTIF_AD_TYPE_URI"></a>

<a id="btif__type_8h_1a849f0c4d24e4391a154d7d7a9a477efe"></a> BTIF\_AD\_TYPE\_URI

<a id="c.BTIF_AD_TYPE_INDOOR_POSITIONING"></a>

<a id="btif__type_8h_1a9be61e72c4967de5aef35efc94eb2e31"></a> BTIF\_AD\_TYPE\_INDOOR\_POSITIONING

<a id="c.BTIF_AD_TYPE_TRANSPORT_DISCOVERY_DATA"></a>

<a id="btif__type_8h_1a82926331797faa98875eb2b390ba7252"></a> BTIF\_AD\_TYPE\_TRANSPORT\_DISCOVERY\_DATA

<a id="c.BTIF_AD_TYPE_LE_SUPPORTED_FEATURES"></a>

<a id="btif__type_8h_1aa2f3f770e414183e57b6ec2e98ea19c3"></a> BTIF\_AD\_TYPE\_LE\_SUPPORTED\_FEATURES

<a id="c.BTIF_AD_TYPE_CHANNEL_MAP_UPDATE_INDICATION"></a>

<a id="btif__type_8h_1a32de75baab871d985874c290b283817a"></a> BTIF\_AD\_TYPE\_CHANNEL\_MAP\_UPDATE\_INDICATION

<a id="c.BTIF_AD_TYPE_PB_ADV"></a>

<a id="btif__type_8h_1afad88c294dcc6b87678bc0eb0bc47937"></a> BTIF\_AD\_TYPE\_PB\_ADV

<a id="c.BTIF_AD_TYPE_BROADCAST_NAME"></a>

<a id="btif__type_8h_1a34a144262ab190518c4a447eac820c67"></a> BTIF\_AD\_TYPE\_BROADCAST\_NAME

<a id="c.BTIF_AD_TYPE_MESH_MESSAGE"></a>

<a id="btif__type_8h_1a96c843a3779030afa09c38769239c0c2"></a> BTIF\_AD\_TYPE\_MESH\_MESSAGE

<a id="c.BTIF_AD_TYPE_MESH_BEACON"></a>

<a id="btif__type_8h_1aa4e2d06a40c0a861fab276b7b33fa379"></a> BTIF\_AD\_TYPE\_MESH\_BEACON

<a id="c.BTIF_AD_TYPE_CSIS_RSI"></a>

<a id="btif__type_8h_1a887be52dede8f7a8facc8f2ab7cdb9cf"></a> BTIF\_AD\_TYPE\_CSIS\_RSI

<a id="c.BTIF_AD_TYPE_3D_INFORMATION_DATA"></a>

<a id="btif__type_8h_1a4dbe506729684e52e4e9bf161e8cad93"></a> BTIF\_AD\_TYPE\_3D\_INFORMATION\_DATA

<a id="c.BTIF_AD_TYPE_MANUFACTURER_SPECIFIC_DATA"></a>

<a id="btif__type_8h_1aa9e8bd223e2dfa008b7af72878f9c14d"></a> BTIF\_AD\_TYPE\_MANUFACTURER\_SPECIFIC\_DATA

<a id="c.BTIF_AD_LEN_LEN"></a>

<a id="btif__type_8h_1abed1e97e2e7d4db77998e5ffebbafd80"></a> BTIF\_AD\_LEN\_LEN

<a id="c.BTIF_AD_TYPE_LEN"></a>

<a id="btif__type_8h_1ab2d0ba2b255884dec9ef96d484962325"></a> BTIF\_AD\_TYPE\_LEN

<a id="c.BTIF_HFP_CODEC_CVSD"></a>

<a id="btif__type_8h_1a6c70678e1d880f68d27995b5004c1796"></a> BTIF\_HFP\_CODEC\_CVSD

<a id="c.BTIF_HFP_CODEC_MSBC"></a>

<a id="btif__type_8h_1a9917ef4e2265af9422e9c61079a9817e"></a> BTIF\_HFP\_CODEC\_MSBC

<a id="c.BTIF_HFP_INDICATOR_SERVICE"></a>

<a id="btif__type_8h_1a89c630f494b497dd62c7ddd141f991af"></a> BTIF\_HFP\_INDICATOR\_SERVICE

<a id="c.BTIF_HFP_INDICATOR_CALL"></a>

<a id="btif__type_8h_1a369767adc1bd1e1a040898c13ea8c00f"></a> BTIF\_HFP\_INDICATOR\_CALL

<a id="c.BTIF_HFP_INDICATOR_CALLSETUP"></a>

<a id="btif__type_8h_1a8190c25ade4ed7c062f564c8a48e943f"></a> BTIF\_HFP\_INDICATOR\_CALLSETUP

<a id="c.BTIF_HFP_INDICATOR_CALLHELD"></a>

<a id="btif__type_8h_1a6055b29ec390a3ff27609eb4f372bfe6"></a> BTIF\_HFP\_INDICATOR\_CALLHELD

<a id="c.BTIF_HFP_INDICATOR_SIGNAL"></a>

<a id="btif__type_8h_1a695d43915549556d0ffca1f307a312f0"></a> BTIF\_HFP\_INDICATOR\_SIGNAL

<a id="c.BTIF_HFP_INDICATOR_ROAM"></a>

<a id="btif__type_8h_1aa7b8616112b9b5e8a799911afc1ffd7f"></a> BTIF\_HFP\_INDICATOR\_ROAM

<a id="c.BTIF_HFP_INDICATOR_BATTCHG"></a>

<a id="btif__type_8h_1a19ae10d8888920ff39dd36199dd9d810"></a> BTIF\_HFP\_INDICATOR\_BATTCHG

<a id="c.BTIF_HFP_INDICATOR_LAST"></a>

<a id="btif__type_8h_1a6e116bc1b17292272bee9d082c78a176"></a> BTIF\_HFP\_INDICATOR\_LAST

<a id="c.BTIF_HFP_CALLSETUP_NO_CALL"></a>

<a id="btif__type_8h_1a4edc07240365fb27cfbf0e1b9275c1c7"></a> BTIF\_HFP\_CALLSETUP\_NO\_CALL

<a id="c.BTIF_HFP_CALLSETUP_INCOMING_CALL"></a>

<a id="btif__type_8h_1a34e745a2c633b503e294c6d39a6cd4c8"></a> BTIF\_HFP\_CALLSETUP\_INCOMING\_CALL

<a id="c.BTIF_HFP_CALLSETUP_OUTGOING_CALL_DIALING"></a>

<a id="btif__type_8h_1ac40c96db8c1d6db804a8818963b6d3bb"></a> BTIF\_HFP\_CALLSETUP\_OUTGOING\_CALL\_DIALING

<a id="c.BTIF_HFP_CALLSETUP_OUTGOING_CALL_ALERTING"></a>

<a id="btif__type_8h_1a0f9139c120a2df450bbb934c3bce0ca0"></a> BTIF\_HFP\_CALLSETUP\_OUTGOING\_CALL\_ALERTING

<a id="c.BTIF_HFP_CALL_NO_HELD_OR_ACTIVE"></a>

<a id="btif__type_8h_1a1092a388c39a24e74291c766a68ebf71"></a> BTIF\_HFP\_CALL\_NO\_HELD\_OR\_ACTIVE

<a id="c.BTIF_HFP_CALL_ACTIVE_OR_HELD_CALL"></a>

<a id="btif__type_8h_1a08b472946ba2b51c1b6762f1cc0a442f"></a> BTIF\_HFP\_CALL\_ACTIVE\_OR\_HELD\_CALL

<a id="c.BTIF_HFP_CHELD_NO_CALL"></a>

<a id="btif__type_8h_1a16b8028cf42c1286da40684849877411"></a> BTIF\_HFP\_CHELD\_NO\_CALL

<a id="c.BTIF_HFP_CHELD_CALL_ON_HOLD_OR_SWAPPED"></a>

<a id="btif__type_8h_1a9bbcd51bf8cabd5f2c5a75db29025790"></a> BTIF\_HFP\_CHELD\_CALL\_ON\_HOLD\_OR\_SWAPPED

<a id="c.BTIF_HFP_CHELD_CALL_ON_HOLD_AND_NO_ACTIVE_CALLS"></a>

<a id="btif__type_8h_1a8f875803f760764c4d8a4a1fbd152325"></a> BTIF\_HFP\_CHELD\_CALL\_ON\_HOLD\_AND\_NO\_ACTIVE\_CALLS

<a id="c.BTIF_A2DP_SONY_ID"></a>

<a id="btif__type_8h_1a1584a2635ebb733e432236fb8ce7298d"></a> BTIF\_A2DP\_SONY\_ID

<a id="c.BTIF_A2DP_LDAC_ID"></a>

<a id="btif__type_8h_1a29286104482a695a2fdd27b543410508"></a> BTIF\_A2DP\_LDAC\_ID

<a id="c.BTIF_A2DP_CP_VALUE_LEN_MAX"></a>

<a id="btif__type_8h_1a89b2d2235bf420b34db88326063c8e01"></a> BTIF\_A2DP\_CP\_VALUE\_LEN\_MAX

<a id="c.BTIF_A2DP_SBC_CODEC_INFO_LEN"></a>

<a id="btif__type_8h_1acd3646bfb95a1ab3ce8e0dac066f3e18"></a> BTIF\_A2DP\_SBC\_CODEC\_INFO\_LEN

<a id="c.BTIF_A2DP_AAC_CODEC_INFO_LEN"></a>

<a id="btif__type_8h_1a3294e2ca22f193ff91bbbd3fc971dba9"></a> BTIF\_A2DP\_AAC\_CODEC\_INFO\_LEN

<a id="c.BTIF_A2DP_LDAC_CODEC_INFO_LEN"></a>

<a id="btif__type_8h_1af70748f9c62dc7afc8c502a081b799b2"></a> BTIF\_A2DP\_LDAC\_CODEC\_INFO\_LEN

<a id="c.BTIF_A2DP_AUDIO"></a>

<a id="btif__type_8h_1ac3c9bdd45d057896e8e6893d26495a39"></a> BTIF\_A2DP\_AUDIO

<a id="c.BTIF_A2DP_VIDEO"></a>

<a id="btif__type_8h_1aff78a20db98d6023da3483b975e5f63a"></a> BTIF\_A2DP\_VIDEO

<a id="c.BTIF_A2DP_MULTIMEDIA"></a>

<a id="btif__type_8h_1a881792f1aa51b60e578ba342622615fa"></a> BTIF\_A2DP\_MULTIMEDIA

<a id="c.BTIF_A2DP_CODEC_SBC"></a>

<a id="btif__type_8h_1aeb10842ccdbcd9fad71b1c5e1be537e9"></a> BTIF\_A2DP\_CODEC\_SBC

<a id="c.BTIF_A2DP_CODEC_MPEG_1_2_AUDIO"></a>

<a id="btif__type_8h_1a1ceaea578da93c97ef7024c45546c1dc"></a> BTIF\_A2DP\_CODEC\_MPEG\_1\_2\_AUDIO

<a id="c.BTIF_A2DP_CODEC_MPEG_2_4_AAC"></a>

<a id="btif__type_8h_1ac7521806519e9d4dc1b188781927274d"></a> BTIF\_A2DP\_CODEC\_MPEG\_2\_4\_AAC

<a id="c.BTIF_A2DP_CODEC_ATRAC_FAMILY"></a>

<a id="btif__type_8h_1af48440f67b6addff630f6252ef3949be"></a> BTIF\_A2DP\_CODEC\_ATRAC\_FAMILY

<a id="c.BTIF_A2DP_CODEC_MPEG_D_USAC"></a>

<a id="btif__type_8h_1adc737c89c3d3a3d3b9d16161770dcf29"></a> BTIF\_A2DP\_CODEC\_MPEG\_D\_USAC

<a id="c.BTIF_A2DP_CODEC_VENDOR_A2DP"></a>

<a id="btif__type_8h_1a2392f55c7aa5b82cc07cec05718495bd"></a> BTIF\_A2DP\_CODEC\_VENDOR\_A2DP

<a id="c.BTIF_A2DP_CODEC_LDAC"></a>

<a id="btif__type_8h_1a84d3556440feac066aa6e86821966eac"></a> BTIF\_A2DP\_CODEC\_LDAC

<a id="c.BTIF_A2DP_CODEC_LC3"></a>

<a id="btif__type_8h_1aebc9302bbbd0144cf39d4f3a6286a58d"></a> BTIF\_A2DP\_CODEC\_LC3

<a id="c.BTIF_PCM"></a>

<a id="btif__type_8h_1a0be169854349bbb20550c705fe1173cd"></a> BTIF\_PCM

<a id="c.BTIF_A2DP_CP_UNSUPP"></a>

<a id="btif__type_8h_1a2d87b99189e3681816be6f9d4fa58a06"></a> BTIF\_A2DP\_CP\_UNSUPP

<a id="c.BTIF_A2DP_CP_DTCP"></a>

<a id="btif__type_8h_1ad957248cde517164701d50bae34dff12"></a> BTIF\_A2DP\_CP\_DTCP

<a id="c.BTIF_A2DP_CP_SCMS_T"></a>

<a id="btif__type_8h_1a3e20bd8f3c2e13f676b5616d1836abfc"></a> BTIF\_A2DP\_CP\_SCMS\_T

<a id="c.BTIF_A2DP_CP_UNSUPPORTED"></a>

<a id="btif__type_8h_1a65d298733976c7d398d71e4592bd9090"></a> BTIF\_A2DP\_CP\_UNSUPPORTED

<a id="c.BTIF_A2DP_CP_CFG"></a>

<a id="btif__type_8h_1a5db5bcf07f985d796bb8a5f612b11ddc"></a> BTIF\_A2DP\_CP\_CFG

<a id="c.BTIF_A2DP_CP_SEC_CTRL"></a>

<a id="btif__type_8h_1ad5fc47dbcf912e06d59261e6ff08aa96"></a> BTIF\_A2DP\_CP\_SEC\_CTRL

<a id="c.CCP_IF_CP_OPCODE_ACCEPT"></a>

<a id="btif__type_8h_1a91aefc8fb756f19aca69bc0fa4dc595e"></a> CCP\_IF\_CP\_OPCODE\_ACCEPT
:   Accept

<a id="c.CCP_IF_CP_OPCODE_TERMINATE"></a>

<a id="btif__type_8h_1aae8c2db18daa72eaf8e5790da5bc93c2"></a> CCP\_IF\_CP\_OPCODE\_TERMINATE
:   Terminate

<a id="c.CCP_IF_CP_OPCODE_HOLD"></a>

<a id="btif__type_8h_1aa199ffd647898015bb08b6bc40f9b4c2"></a> CCP\_IF\_CP\_OPCODE\_HOLD
:   Hold

<a id="c.CCP_IF_CP_OPCODE_RETRIEVE"></a>

<a id="btif__type_8h_1a24ca4c5502450100e30144f6dba0683f"></a> CCP\_IF\_CP\_OPCODE\_RETRIEVE
:   Retrieve

<a id="c.CCP_IF_CP_OPCODE_ORIGINATE"></a>

<a id="btif__type_8h_1a1517cdc3ad84f5a92f5ccf6715623ea0"></a> CCP\_IF\_CP\_OPCODE\_ORIGINATE
:   Originate

<a id="c.CCP_IF_CP_OPCODE_JOIN"></a>

<a id="btif__type_8h_1a01d97054db2a07fcbab2f023ffca62f9"></a> CCP\_IF\_CP\_OPCODE\_JOIN
:   Join

<a id="c.CCP_IF_CALL_FLAG_OUTGOING_FLAG"></a>

<a id="btif__type_8h_1a4193f32620ce6a605ea8a99e83c71671"></a> CCP\_IF\_CALL\_FLAG\_OUTGOING\_FLAG
:   1 \= Call is an outgoing call 0:Call is an incoming call

<a id="c.CCP_IF_CALL_FLAG_WITHHELD_FLAG"></a>

<a id="btif__type_8h_1a64ceea28d242cc9b1e7b38e4ae83d204"></a> CCP\_IF\_CALL\_FLAG\_WITHHELD\_FLAG
:   1 \= Withheld 0 \= Not withheld

<a id="c.CCP_IF_CALL_FLAG_WITHHELD_BY_NET_FLAG"></a>

<a id="btif__type_8h_1a6c33d1b1a7210efc0069717cf66ee4d7"></a> CCP\_IF\_CALL\_FLAG\_WITHHELD\_BY\_NET\_FLAG
:   1 \= Withheld by network 0 \= Provided by network

<a id="c.CCP_IF_CALL_STATE_STATE_INCOMING"></a>

<a id="btif__type_8h_1a4bac6dea9ffb4f0b1deb29f9f43f2fa0"></a> CCP\_IF\_CALL\_STATE\_STATE\_INCOMING
:   Incoming

<a id="c.CCP_IF_CALL_STATE_STATE_DIALING"></a>

<a id="btif__type_8h_1aca060073880316e0d5b64db2ec5b4085"></a> CCP\_IF\_CALL\_STATE\_STATE\_DIALING
:   Dialing

<a id="c.CCP_IF_CALL_STATE_STATE_ALERTING"></a>

<a id="btif__type_8h_1aecf8ced4c27f0b2c702240b0a4a35667"></a> CCP\_IF\_CALL\_STATE\_STATE\_ALERTING
:   Alerting

<a id="c.CCP_IF_CALL_STATE_STATE_ACTIVE"></a>

<a id="btif__type_8h_1a45c60a878f8edc2c16920265ffbbc930"></a> CCP\_IF\_CALL\_STATE\_STATE\_ACTIVE
:   Active

<a id="c.CCP_IF_CALL_STATE_STATE_LOC_HELD"></a>

<a id="btif__type_8h_1a761926f64875270cbc5190842f7cf900"></a> CCP\_IF\_CALL\_STATE\_STATE\_LOC\_HELD
:   Locally Held

<a id="c.CCP_IF_CALL_STATE_STATE_REMOTE_HELD"></a>

<a id="btif__type_8h_1a3de4820f90543d43672e32eff20dc031"></a> CCP\_IF\_CALL\_STATE\_STATE\_REMOTE\_HELD
:   Remotely Held

<a id="c.CCP_IF_CALL_STATE_STATE_LOC_REMOTE_HELD"></a>

<a id="btif__type_8h_1a23045d8ad9b6ff7d94303a5ac916adb7"></a> CCP\_IF\_CALL\_STATE\_STATE\_LOC\_REMOTE\_HELD
:   Locally and Remotely Held

<a id="c.CCP_IF_CALL_STATE_STATE_INVALID"></a>

<a id="btif__type_8h_1a6f0d2e6a1a31262470e252c0f96e12d5"></a> CCP\_IF\_CALL\_STATE\_STATE\_INVALID
:   Invalid state

<a id="c.MCP_IF_CP_OPCODE_PLAY"></a>

<a id="btif__type_8h_1a8b4c893a4a10761702de2d972ad387ca"></a> MCP\_IF\_CP\_OPCODE\_PLAY

<a id="c.MCP_IF_CP_OPCODE_PAUSE"></a>

<a id="btif__type_8h_1a8c6a08485f566c45176910a5049614ed"></a> MCP\_IF\_CP\_OPCODE\_PAUSE

<a id="c.MCP_IF_CP_OPCODE_FAST_REWIND"></a>

<a id="btif__type_8h_1ae118065ebe1667ee8a44b1522a981867"></a> MCP\_IF\_CP\_OPCODE\_FAST\_REWIND

<a id="c.MCP_IF_CP_OPCODE_FAST_FORWARD"></a>

<a id="btif__type_8h_1a15c087fdf042f1f2cbeb64246653ca3a"></a> MCP\_IF\_CP\_OPCODE\_FAST\_FORWARD

<a id="c.MCP_IF_CP_OPCODE_STOP"></a>

<a id="btif__type_8h_1a1a8d8c8d1041061fdaf67bb684506134"></a> MCP\_IF\_CP\_OPCODE\_STOP

<a id="c.MCP_IF_CP_OPCODE_MOVE_RELATIVE"></a>

<a id="btif__type_8h_1a4bcbfc145b59ab504c35b96c7130c7e8"></a> MCP\_IF\_CP\_OPCODE\_MOVE\_RELATIVE

<a id="c.MCP_IF_CP_OPCODE_PREVIOUS_SEGMENT"></a>

<a id="btif__type_8h_1ab261c69b15cdb841fffec1c6a3de6807"></a> MCP\_IF\_CP\_OPCODE\_PREVIOUS\_SEGMENT

<a id="c.MCP_IF_CP_OPCODE_NEXT_SEGMENT"></a>

<a id="btif__type_8h_1a77ff4fa15fb10a614dad4f6a941571db"></a> MCP\_IF\_CP\_OPCODE\_NEXT\_SEGMENT

<a id="c.MCP_IF_CP_OPCODE_FIRST_SEGMENT"></a>

<a id="btif__type_8h_1a72d806354386e1240875221fbe9c204b"></a> MCP\_IF\_CP\_OPCODE\_FIRST\_SEGMENT

<a id="c.MCP_IF_CP_OPCODE_LAST_SEGMENT"></a>

<a id="btif__type_8h_1a2acc57c45cbdb5d61c8dbff8be841772"></a> MCP\_IF\_CP\_OPCODE\_LAST\_SEGMENT

<a id="c.MCP_IF_CP_OPCODE_GOTO_SEGMENT"></a>

<a id="btif__type_8h_1ae35bf05502cad43d017c3ad809b5f154"></a> MCP\_IF\_CP\_OPCODE\_GOTO\_SEGMENT

<a id="c.MCP_IF_CP_OPCODE_PREVIOUS_TRACK"></a>

<a id="btif__type_8h_1ac72bf6381b8da5f9d9fa7435cd3f5c4b"></a> MCP\_IF\_CP\_OPCODE\_PREVIOUS\_TRACK

<a id="c.MCP_IF_CP_OPCODE_NEXT_TRACK"></a>

<a id="btif__type_8h_1a58eefb43645c09423a0abbcc129cadff"></a> MCP\_IF\_CP\_OPCODE\_NEXT\_TRACK

<a id="c.MCP_IF_CP_OPCODE_FIRST_TRACK"></a>

<a id="btif__type_8h_1afcd1a2cea043caea56026fcd79b52f98"></a> MCP\_IF\_CP\_OPCODE\_FIRST\_TRACK

<a id="c.MCP_IF_CP_OPCODE_LAST_TRACK"></a>

<a id="btif__type_8h_1a1fc897792b7fd7e853d4a445a9cd3c0b"></a> MCP\_IF\_CP\_OPCODE\_LAST\_TRACK

<a id="c.MCP_IF_CP_OPCODE_GOTO_TRACK"></a>

<a id="btif__type_8h_1a1f061baa9a0d51a42a7d851185e02f7f"></a> MCP\_IF\_CP\_OPCODE\_GOTO\_TRACK

<a id="c.MCP_IF_CP_OPCODE_PREVIOUS_GROUP"></a>

<a id="btif__type_8h_1a98ea90f3bcdf147ea11841496a30a18e"></a> MCP\_IF\_CP\_OPCODE\_PREVIOUS\_GROUP

<a id="c.MCP_IF_CP_OPCODE_NEXT_GROUP"></a>

<a id="btif__type_8h_1a041af2180dadf0f7027d0dd5cee71061"></a> MCP\_IF\_CP\_OPCODE\_NEXT\_GROUP

<a id="c.MCP_IF_CP_OPCODE_FIRST_GROUP"></a>

<a id="btif__type_8h_1afc40a71ef537d9c526f076956fcc2212"></a> MCP\_IF\_CP\_OPCODE\_FIRST\_GROUP

<a id="c.MCP_IF_CP_OPCODE_LAST_GROUP"></a>

<a id="btif__type_8h_1a02f64fbd9df9f4ac3f26f1e4efe42fd6"></a> MCP\_IF\_CP\_OPCODE\_LAST\_GROUP

<a id="c.MCP_IF_CP_OPCODE_GOTO_GROUP"></a>

<a id="btif__type_8h_1a21fe35603a53515fd2c005ecc4e85f59"></a> MCP\_IF\_CP\_OPCODE\_GOTO\_GROUP

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv417btif_le_lk_type_t"></a>

<a id="_CPPv317btif_le_lk_type_t"></a> <a id="_CPPv217btif_le_lk_type_t"></a> <a id="btif_le_lk_type_t"></a> <a id="btif__type_8h_1aba65422ca6d8f91917ac64404d30c90d"></a> typedef uint8\_t btif\_le\_lk\_type\_t

<a id="_CPPv423task_init_done_callback"></a>

<a id="_CPPv323task_init_done_callback"></a> <a id="_CPPv223task_init_done_callback"></a> <a id="task_init_done_callback"></a> <a id="btif__type_8h_1a2177f678e26c9de798eb23b2e903c2b2"></a> typedef void (\*task\_init\_done\_callback)(void)

<a id="_CPPv419btif_le_addr_type_t"></a>

<a id="_CPPv319btif_le_addr_type_t"></a> <a id="_CPPv219btif_le_addr_type_t"></a> <a id="btif_le_addr_type_t"></a> <a id="btif__type_8h_1aa02c8d729534132b6ee4653e695f9be3"></a> typedef uint8\_t btif\_le\_addr\_type\_t
:   LE MAC address type definition.

<a id="_CPPv410btif_ret_t"></a>

<a id="_CPPv310btif_ret_t"></a> <a id="_CPPv210btif_ret_t"></a> <a id="btif_ret_t"></a> <a id="btif__type_8h_1ad2ecdb51bfc88c5484e6f0d0c913e05e"></a> typedef int32\_t btif\_ret\_t

<a id="_CPPv414btif_bt_role_t"></a>

<a id="_CPPv314btif_bt_role_t"></a> <a id="_CPPv214btif_bt_role_t"></a> <a id="btif_bt_role_t"></a> <a id="btif__type_8h_1af84920feae480cd0821cc26d4cc0e232"></a> typedef uint8\_t btif\_bt\_role\_t
:   BT role type definiion.

<a id="_CPPv415btif_tws_role_t"></a>

<a id="_CPPv315btif_tws_role_t"></a> <a id="_CPPv215btif_tws_role_t"></a> <a id="btif_tws_role_t"></a> <a id="btif__type_8h_1a7021a79806ffd20750efa0100763583a"></a> typedef uint8\_t btif\_tws\_role\_t
:   TWS role type definition.

<a id="_CPPv423btif_sync_prof_status_t"></a>

<a id="_CPPv323btif_sync_prof_status_t"></a> <a id="_CPPv223btif_sync_prof_status_t"></a> <a id="btif_sync_prof_status_t"></a> <a id="btif__type_8h_1ad713f77664aa7f3230973d5bbe05bc34"></a> typedef uint8\_t btif\_sync\_prof\_status\_t
:   TWS sync profile status definition.

<a id="_CPPv418btif_enable_scan_t"></a>

<a id="_CPPv318btif_enable_scan_t"></a> <a id="_CPPv218btif_enable_scan_t"></a> <a id="btif_enable_scan_t"></a> <a id="btif__type_8h_1a60b72d90f4841013e7d4be17a13937d9"></a> typedef uint8\_t btif\_enable\_scan\_t
:   bluetooth scan type definition

<a id="_CPPv421btif_profile_bitmap_t"></a>

<a id="_CPPv321btif_profile_bitmap_t"></a> <a id="_CPPv221btif_profile_bitmap_t"></a> <a id="btif_profile_bitmap_t"></a> <a id="btif__type_8h_1a7686100aea963f3a607732b92b69deb0"></a> typedef uint16\_t btif\_profile\_bitmap\_t
:   bluetooth profile bitmap definition

<a id="_CPPv416btif_sco_codec_t"></a>

<a id="_CPPv316btif_sco_codec_t"></a> <a id="_CPPv216btif_sco_codec_t"></a> <a id="btif_sco_codec_t"></a> <a id="btif__type_8h_1a3e08e55f0356dad9d8c20e554b520d7c"></a> typedef uint8\_t btif\_sco\_codec\_t
:   HFP codec type definition.

<a id="_CPPv413btif_hf_ind_t"></a>

<a id="_CPPv313btif_hf_ind_t"></a> <a id="_CPPv213btif_hf_ind_t"></a> <a id="btif_hf_ind_t"></a> <a id="btif__type_8h_1a034d7b0000db85bb5cf0e8a1ca3f07af"></a> typedef uint8\_t btif\_hf\_ind\_t
:   HFP indicated type definition.

<a id="_CPPv420btif_hfp_callsetup_t"></a>

<a id="_CPPv320btif_hfp_callsetup_t"></a> <a id="_CPPv220btif_hfp_callsetup_t"></a> <a id="btif_hfp_callsetup_t"></a> <a id="btif__type_8h_1a7431b756ca6533d3fd8a257fae6bdca6"></a> typedef uint8\_t btif\_hfp\_callsetup\_t
:   HFP call setup status definition.

<a id="_CPPv415btif_hfp_call_t"></a>

<a id="_CPPv315btif_hfp_call_t"></a> <a id="_CPPv215btif_hfp_call_t"></a> <a id="btif_hfp_call_t"></a> <a id="btif__type_8h_1abcb2253ee4744952dcb81565b26c4797"></a> typedef uint8\_t btif\_hfp\_call\_t
:   HFP call status definition.

<a id="_CPPv419btif_hfp_callheld_t"></a>

<a id="_CPPv319btif_hfp_callheld_t"></a> <a id="_CPPv219btif_hfp_callheld_t"></a> <a id="btif_hfp_callheld_t"></a> <a id="btif__type_8h_1a17afc87b3a934d3f43079d4ca4cdeca6"></a> typedef uint8\_t btif\_hfp\_callheld\_t
:   HFP call hold status definition.

<a id="_CPPv422btif_a2dp_media_type_t"></a>

<a id="_CPPv322btif_a2dp_media_type_t"></a> <a id="_CPPv222btif_a2dp_media_type_t"></a> <a id="btif_a2dp_media_type_t"></a> <a id="btif__type_8h_1a0dd84eac9f6d73ee8458c7cd15e4c287"></a> typedef uint8\_t btif\_a2dp\_media\_type\_t
:   A2DP media type definition.

<a id="_CPPv422btif_a2dp_codec_type_t"></a>

<a id="_CPPv322btif_a2dp_codec_type_t"></a> <a id="_CPPv222btif_a2dp_codec_type_t"></a> <a id="btif_a2dp_codec_type_t"></a> <a id="btif__type_8h_1a77726b9d0e30f3bb4ccb4949be12f401"></a> typedef uint8\_t btif\_a2dp\_codec\_type\_t
:   A2DP codec type definition.

<a id="_CPPv419btif_a2dp_cp_type_t"></a>

<a id="_CPPv319btif_a2dp_cp_type_t"></a> <a id="_CPPv219btif_a2dp_cp_type_t"></a> <a id="btif_a2dp_cp_type_t"></a> <a id="btif__type_8h_1a21554e6b93c035c1193b5cdb4afeb986"></a> typedef uint16\_t btif\_a2dp\_cp\_type\_t
:   A2DP content protection type definition.

<a id="_CPPv421btif_a2dp_cp_status_t"></a>

<a id="_CPPv321btif_a2dp_cp_status_t"></a> <a id="_CPPv221btif_a2dp_cp_status_t"></a> <a id="btif_a2dp_cp_status_t"></a> <a id="btif__type_8h_1ab515996e383615fddcbda2dbdf0953a8"></a> typedef uint16\_t btif\_a2dp\_cp\_status\_t
:   A2DP content protection status defintion.

<a id="_CPPv418ccp_if_cp_opcode_t"></a>

<a id="_CPPv318ccp_if_cp_opcode_t"></a> <a id="_CPPv218ccp_if_cp_opcode_t"></a> <a id="ccp_if_cp_opcode_t"></a> <a id="btif__type_8h_1a73496f5a2593e1b83ac33b2e382efa84"></a> typedef uint8\_t ccp\_if\_cp\_opcode\_t
:   CCP opcode definition.

<a id="_CPPv419ccp_if_call_state_t"></a>

<a id="_CPPv319ccp_if_call_state_t"></a> <a id="_CPPv219ccp_if_call_state_t"></a> <a id="ccp_if_call_state_t"></a> <a id="btif__type_8h_1a83a008b762377d34b950459f53c41f06"></a> typedef uint8\_t ccp\_if\_call\_state\_t
:   CCP call state definition.

<a id="_CPPv418mcp_if_cp_opcode_t"></a>

<a id="_CPPv318mcp_if_cp_opcode_t"></a> <a id="_CPPv218mcp_if_cp_opcode_t"></a> <a id="mcp_if_cp_opcode_t"></a> <a id="btif__type_8h_1a6076ddda9bd773ba2b665cf89fe5be02"></a> typedef uint8\_t mcp\_if\_cp\_opcode\_t
:   MCP opcode definition.

<a id="_CPPv424btif_a2dp_event_callback"></a>

<a id="_CPPv324btif_a2dp_event_callback"></a> <a id="_CPPv224btif_a2dp_event_callback"></a> <a id="btif_a2dp_event_callback"></a> <a id="btif__type_8h_1a545135b21f956bf6913f3eae2f299c9e"></a> typedef void (\*btif\_a2dp\_event\_callback)(const void \*p\_cb\_param, uint16\_t len)

<a id="_CPPv425btif_avrcp_event_callback"></a>

<a id="_CPPv325btif_avrcp_event_callback"></a> <a id="_CPPv225btif_avrcp_event_callback"></a> <a id="btif_avrcp_event_callback"></a> <a id="btif__type_8h_1a34b0988412c9757d53eef26e65a22f01"></a> typedef void (\*btif\_avrcp\_event\_callback)(const void \*p\_cb\_param, uint16\_t len)

<a id="_CPPv423btif_hfp_event_callback"></a>

<a id="_CPPv323btif_hfp_event_callback"></a> <a id="_CPPv223btif_hfp_event_callback"></a> <a id="btif_hfp_event_callback"></a> <a id="btif__type_8h_1a7999ebee652cfb9862afe4bbf1c211d1"></a> typedef void (\*btif\_hfp\_event\_callback)(uint8\_t \*p\_data, uint16\_t size)

<a id="_CPPv423btif_hci_event_callback"></a>

<a id="_CPPv323btif_hci_event_callback"></a> <a id="_CPPv223btif_hci_event_callback"></a> <a id="btif_hci_event_callback"></a> <a id="btif__type_8h_1ad1f3e3c9418afcada59c91e6aa0f89f0"></a> typedef void (\*btif\_hci\_event\_callback)(uint8\_t \*p\_data, uint16\_t length)

<a id="_CPPv426btif_hci_conn_req_callback"></a>

<a id="_CPPv326btif_hci_conn_req_callback"></a> <a id="_CPPv226btif_hci_conn_req_callback"></a> <a id="btif_hci_conn_req_callback"></a> <a id="btif__type_8h_1af9b0dbe32bb9fd7545c548c471893732"></a> typedef void (\*btif\_hci\_conn\_req\_callback)([btif\_bd\_addr\_t](#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr)

<a id="_CPPv421btif_p_connection_req"></a>

<a id="_CPPv321btif_p_connection_req"></a> <a id="_CPPv221btif_p_connection_req"></a> <a id="btif_p_connection_req"></a> <a id="btif__type_8h_1a124828a17d93b6926457c1da4e4e1757"></a> typedef uint8\_t (\*btif\_p\_connection\_req)(void \*p\_addr)

<a id="_CPPv423btif_ccp_event_callback"></a>

<a id="_CPPv323btif_ccp_event_callback"></a> <a id="_CPPv223btif_ccp_event_callback"></a> <a id="btif_ccp_event_callback"></a> <a id="btif__type_8h_1a83e24e0ee03d2f499f07a2b99d1788d2"></a> typedef void (\*btif\_ccp\_event\_callback)(uint16\_t handle, uint8\_t \*p\_data, uint16\_t size)

<a id="_CPPv423btif_mcp_event_callback"></a>

<a id="_CPPv323btif_mcp_event_callback"></a> <a id="_CPPv223btif_mcp_event_callback"></a> <a id="btif_mcp_event_callback"></a> <a id="btif__type_8h_1a20f9a9e24604203f5e2eefdd03e59443"></a> typedef void (\*btif\_mcp\_event\_callback)(uint16\_t handle, uint8\_t \*p\_data, uint16\_t size)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv416btif_uuid_type_m"></a>

<a id="_CPPv316btif_uuid_type_m"></a> <a id="_CPPv216btif_uuid_type_m"></a> <a id="btif__type_8h_1a2a98e9f80a801c82a0564d3a7ce3b554"></a> enum btif\_uuid\_type\_m
:   UUID type definition.

    *Values:*

    <a id="_CPPv4N16btif_uuid_type_m17BTIF_UUID_TYPE_16E"></a>

    <a id="_CPPv3N16btif_uuid_type_m17BTIF_UUID_TYPE_16E"></a> <a id="_CPPv2N16btif_uuid_type_m17BTIF_UUID_TYPE_16E"></a> <a id="btif__type_8h_1a2a98e9f80a801c82a0564d3a7ce3b554acda3cd959fecb014a1d9b72f982992ba"></a> enumerator BTIF\_UUID\_TYPE\_16

    <a id="_CPPv4N16btif_uuid_type_m17BTIF_UUID_TYPE_32E"></a>

    <a id="_CPPv3N16btif_uuid_type_m17BTIF_UUID_TYPE_32E"></a> <a id="_CPPv2N16btif_uuid_type_m17BTIF_UUID_TYPE_32E"></a> <a id="btif__type_8h_1a2a98e9f80a801c82a0564d3a7ce3b554ae6612efc5291aa0b43aa021e6a93d482"></a> enumerator BTIF\_UUID\_TYPE\_32

    <a id="_CPPv4N16btif_uuid_type_m18BTIF_UUID_TYPE_128E"></a>

    <a id="_CPPv3N16btif_uuid_type_m18BTIF_UUID_TYPE_128E"></a> <a id="_CPPv2N16btif_uuid_type_m18BTIF_UUID_TYPE_128E"></a> <a id="btif__type_8h_1a2a98e9f80a801c82a0564d3a7ce3b554aeefa4cdf322e6fbe7cbf93178817858d"></a> enumerator BTIF\_UUID\_TYPE\_128

    <a id="_CPPv4N16btif_uuid_type_m17BTIF_UUID_INVAILDE"></a>

    <a id="_CPPv3N16btif_uuid_type_m17BTIF_UUID_INVAILDE"></a> <a id="_CPPv2N16btif_uuid_type_m17BTIF_UUID_INVAILDE"></a> <a id="btif__type_8h_1a2a98e9f80a801c82a0564d3a7ce3b554ae164f34b0628a747ed254ceaa39baed3"></a> enumerator BTIF\_UUID\_INVAILD

<a id="_CPPv418if_link_key_type_t"></a>

<a id="_CPPv318if_link_key_type_t"></a> <a id="_CPPv218if_link_key_type_t"></a> <a id="btif__type_8h_1aaae1db8274126eb3822467ba1427d263"></a> enum if\_link\_key\_type\_t
:   link key type defintion

    *Values:*

    <a id="_CPPv4N18if_link_key_type_t18IF_COMBINATION_KEYE"></a>

    <a id="_CPPv3N18if_link_key_type_t18IF_COMBINATION_KEYE"></a> <a id="_CPPv2N18if_link_key_type_t18IF_COMBINATION_KEYE"></a> <a id="btif__type_8h_1aaae1db8274126eb3822467ba1427d263a1a3a116749290e88aaf04a3379cda8c8"></a> enumerator IF\_COMBINATION\_KEY
    :   standard pairing

    <a id="_CPPv4N18if_link_key_type_t17IF_LOCAL_UNIT_KEYE"></a>

    <a id="_CPPv3N18if_link_key_type_t17IF_LOCAL_UNIT_KEYE"></a> <a id="_CPPv2N18if_link_key_type_t17IF_LOCAL_UNIT_KEYE"></a> <a id="btif__type_8h_1aaae1db8274126eb3822467ba1427d263ab6a55d3a0169491dbde4140f7f4031b7"></a> enumerator IF\_LOCAL\_UNIT\_KEY
    :   not used in spec

    <a id="_CPPv4N18if_link_key_type_t18IF_REMOTE_UNIT_KEYE"></a>

    <a id="_CPPv3N18if_link_key_type_t18IF_REMOTE_UNIT_KEYE"></a> <a id="_CPPv2N18if_link_key_type_t18IF_REMOTE_UNIT_KEYE"></a> <a id="btif__type_8h_1aaae1db8274126eb3822467ba1427d263a279b76fedacada621a7bf26b51fabddc"></a> enumerator IF\_REMOTE\_UNIT\_KEY
    :   not used in spec

    <a id="_CPPv4N18if_link_key_type_t24IF_DEBUG_COMBINATION_KEYE"></a>

    <a id="_CPPv3N18if_link_key_type_t24IF_DEBUG_COMBINATION_KEYE"></a> <a id="_CPPv2N18if_link_key_type_t24IF_DEBUG_COMBINATION_KEYE"></a> <a id="btif__type_8h_1aaae1db8274126eb3822467ba1427d263a1409e99623252c938eda475613aedfe4"></a> enumerator IF\_DEBUG\_COMBINATION\_KEY
    :   SSP with debug

    <a id="_CPPv4N18if_link_key_type_t20IF_UCK_GEN_FROM_P192E"></a>

    <a id="_CPPv3N18if_link_key_type_t20IF_UCK_GEN_FROM_P192E"></a> <a id="_CPPv2N18if_link_key_type_t20IF_UCK_GEN_FROM_P192E"></a> <a id="btif__type_8h_1aaae1db8274126eb3822467ba1427d263a958ec999459e5c9bf2ef47e2f697ed2e"></a> enumerator IF\_UCK\_GEN\_FROM\_P192
    :   SSP Simple Pairing

    <a id="_CPPv4N18if_link_key_type_t52IF_AUTHENTICATED_COMBINATION_KEY_GENERATED_FROM_P192E"></a>

    <a id="_CPPv3N18if_link_key_type_t52IF_AUTHENTICATED_COMBINATION_KEY_GENERATED_FROM_P192E"></a> <a id="_CPPv2N18if_link_key_type_t52IF_AUTHENTICATED_COMBINATION_KEY_GENERATED_FROM_P192E"></a> <a id="btif__type_8h_1aaae1db8274126eb3822467ba1427d263a6389b1f43d29e566553340e21ef10efd"></a> enumerator IF\_AUTHENTICATED\_COMBINATION\_KEY\_GENERATED\_FROM\_P192
    :   SSP Passkey, Number confirm, OOB

    <a id="_CPPv4N18if_link_key_type_t26IF_CHANGED_COMBINATION_KEYE"></a>

    <a id="_CPPv3N18if_link_key_type_t26IF_CHANGED_COMBINATION_KEYE"></a> <a id="_CPPv2N18if_link_key_type_t26IF_CHANGED_COMBINATION_KEYE"></a> <a id="btif__type_8h_1aaae1db8274126eb3822467ba1427d263a95ce903830d285a5975e8a9f9f6435c1"></a> enumerator IF\_CHANGED\_COMBINATION\_KEY
    :   Link key changed using Change Connection Lnk Key

    <a id="_CPPv4N18if_link_key_type_t20IF_UCK_GEN_FROM_P256E"></a>

    <a id="_CPPv3N18if_link_key_type_t20IF_UCK_GEN_FROM_P256E"></a> <a id="_CPPv2N18if_link_key_type_t20IF_UCK_GEN_FROM_P256E"></a> <a id="btif__type_8h_1aaae1db8274126eb3822467ba1427d263a3028468a6f807ceee079499cf6ddc4fb"></a> enumerator IF\_UCK\_GEN\_FROM\_P256
    :   SSP Simpe Pairing

    <a id="_CPPv4N18if_link_key_type_t52IF_AUTHENTICATED_COMBINATION_KEY_GENERATED_FROM_P256E"></a>

    <a id="_CPPv3N18if_link_key_type_t52IF_AUTHENTICATED_COMBINATION_KEY_GENERATED_FROM_P256E"></a> <a id="_CPPv2N18if_link_key_type_t52IF_AUTHENTICATED_COMBINATION_KEY_GENERATED_FROM_P256E"></a> <a id="btif__type_8h_1aaae1db8274126eb3822467ba1427d263a61c2d84a21c487870d12e7990c33d357"></a> enumerator IF\_AUTHENTICATED\_COMBINATION\_KEY\_GENERATED\_FROM\_P256
    :   SSP Passkey, Number confirm, OOB

<a id="_CPPv4Ut2_10"></a>

<a id="_CPPv3Ut2_10"></a> <a id="btif__type_8h_1a385c44f6fb256e5716a2302a5b940388"></a> enum \[anonymous\]
:   GATT Permission Bit field values definition.

    *Values:*

    <a id="_CPPv4NUt2_1019BTIF_GATT_PERM_NONEE"></a>

    <a id="_CPPv3NUt2_1019BTIF_GATT_PERM_NONEE"></a> <a id="btif__type_8h_1a385c44f6fb256e5716a2302a5b940388af19ccc3ba12302243a1371b16a2ea12a"></a> enumerator BTIF\_GATT\_PERM\_NONE

    <a id="_CPPv4NUt2_1019BTIF_GATT_PERM_READE"></a>

    <a id="_CPPv3NUt2_1019BTIF_GATT_PERM_READE"></a> <a id="btif__type_8h_1a385c44f6fb256e5716a2302a5b940388a356a2a46ec2a6ff32bf31c10feac328e"></a> enumerator BTIF\_GATT\_PERM\_READ

    <a id="_CPPv4NUt2_1020BTIF_GATT_PERM_WRITEE"></a>

    <a id="_CPPv3NUt2_1020BTIF_GATT_PERM_WRITEE"></a> <a id="btif__type_8h_1a385c44f6fb256e5716a2302a5b940388acd763d6eec84b6e7c3cd3cfb4e59bdb6"></a> enumerator BTIF\_GATT\_PERM\_WRITE

    <a id="_CPPv4NUt2_1027BTIF_GATT_PERM_READ_ENCRYPTE"></a>

    <a id="_CPPv3NUt2_1027BTIF_GATT_PERM_READ_ENCRYPTE"></a> <a id="btif__type_8h_1a385c44f6fb256e5716a2302a5b940388ad0254fcfa2ad8336265cc001dbc7974a"></a> enumerator BTIF\_GATT\_PERM\_READ\_ENCRYPT

    <a id="_CPPv4NUt2_1028BTIF_GATT_PERM_WRITE_ENCRYPTE"></a>

    <a id="_CPPv3NUt2_1028BTIF_GATT_PERM_WRITE_ENCRYPTE"></a> <a id="btif__type_8h_1a385c44f6fb256e5716a2302a5b940388a02a9b3d652fdf8bdc894d14240d06196"></a> enumerator BTIF\_GATT\_PERM\_WRITE\_ENCRYPT

    <a id="_CPPv4NUt2_1026BTIF_GATT_PERM_READ_AUTHENE"></a>

    <a id="_CPPv3NUt2_1026BTIF_GATT_PERM_READ_AUTHENE"></a> <a id="btif__type_8h_1a385c44f6fb256e5716a2302a5b940388abe9414ef95fcdbe6b2a478ae1f178ae1"></a> enumerator BTIF\_GATT\_PERM\_READ\_AUTHEN

    <a id="_CPPv4NUt2_1027BTIF_GATT_PERM_WRITE_AUTHENE"></a>

    <a id="_CPPv3NUt2_1027BTIF_GATT_PERM_WRITE_AUTHENE"></a> <a id="btif__type_8h_1a385c44f6fb256e5716a2302a5b940388a51eca10d0a4056a9136c2edb8474f92b"></a> enumerator BTIF\_GATT\_PERM\_WRITE\_AUTHEN

    <a id="_CPPv4NUt2_1028BTIF_GATT_PERM_PREPARE_WRITEE"></a>

    <a id="_CPPv3NUt2_1028BTIF_GATT_PERM_PREPARE_WRITEE"></a> <a id="btif__type_8h_1a385c44f6fb256e5716a2302a5b940388ae456e543bc27a7abc3c40cd0bd26f7cf"></a> enumerator BTIF\_GATT\_PERM\_PREPARE\_WRITE

    <a id="_CPPv4NUt2_1027BTIF_GATT_PERM_PTS_KEY_SIZEE"></a>

    <a id="_CPPv3NUt2_1027BTIF_GATT_PERM_PTS_KEY_SIZEE"></a> <a id="btif__type_8h_1a385c44f6fb256e5716a2302a5b940388a1b1d679d3fedd18defdb66678ec24a19"></a> enumerator BTIF\_GATT\_PERM\_PTS\_KEY\_SIZE

<a id="_CPPv4Ut2_11"></a>

<a id="_CPPv3Ut2_11"></a> <a id="btif__type_8h_1abc5c98fcc1211af2b80116dd6e0a035d"></a> enum \[anonymous\]
:   GATT Characteristic Properties Bit field values definition.

    *Values:*

    <a id="_CPPv4NUt2_1124BTIF_GATT_CHRC_BROADCASTE"></a>

    <a id="_CPPv3NUt2_1124BTIF_GATT_CHRC_BROADCASTE"></a> <a id="btif__type_8h_1abc5c98fcc1211af2b80116dd6e0a035da1c1ab6f3d3b786971dad269f8103a405"></a> enumerator BTIF\_GATT\_CHRC\_BROADCAST

    <a id="_CPPv4NUt2_1119BTIF_GATT_CHRC_READE"></a>

    <a id="_CPPv3NUt2_1119BTIF_GATT_CHRC_READE"></a> <a id="btif__type_8h_1abc5c98fcc1211af2b80116dd6e0a035dae4d3e473110444f9e60fc8afc083bb82"></a> enumerator BTIF\_GATT\_CHRC\_READ

    <a id="_CPPv4NUt2_1133BTIF_GATT_CHRC_WRITE_WITHOUT_RESPE"></a>

    <a id="_CPPv3NUt2_1133BTIF_GATT_CHRC_WRITE_WITHOUT_RESPE"></a> <a id="btif__type_8h_1abc5c98fcc1211af2b80116dd6e0a035da73e4a5b5b921977780a33dbbf651ae4b"></a> enumerator BTIF\_GATT\_CHRC\_WRITE\_WITHOUT\_RESP

    <a id="_CPPv4NUt2_1120BTIF_GATT_CHRC_WRITEE"></a>

    <a id="_CPPv3NUt2_1120BTIF_GATT_CHRC_WRITEE"></a> <a id="btif__type_8h_1abc5c98fcc1211af2b80116dd6e0a035daec263528e13d5ba83f8679ba13a0936b"></a> enumerator BTIF\_GATT\_CHRC\_WRITE

    <a id="_CPPv4NUt2_1121BTIF_GATT_CHRC_NOTIFYE"></a>

    <a id="_CPPv3NUt2_1121BTIF_GATT_CHRC_NOTIFYE"></a> <a id="btif__type_8h_1abc5c98fcc1211af2b80116dd6e0a035da099aea8adaef50f927b0c86e3fb7b80b"></a> enumerator BTIF\_GATT\_CHRC\_NOTIFY

    <a id="_CPPv4NUt2_1123BTIF_GATT_CHRC_INDICATEE"></a>

    <a id="_CPPv3NUt2_1123BTIF_GATT_CHRC_INDICATEE"></a> <a id="btif__type_8h_1abc5c98fcc1211af2b80116dd6e0a035da6760f087f75998ad256cb8f4284b1855"></a> enumerator BTIF\_GATT\_CHRC\_INDICATE

    <a id="_CPPv4NUt2_1119BTIF_GATT_CHRC_AUTHE"></a>

    <a id="_CPPv3NUt2_1119BTIF_GATT_CHRC_AUTHE"></a> <a id="btif__type_8h_1abc5c98fcc1211af2b80116dd6e0a035da0800a135aa682fbe427c76985bd65ae0"></a> enumerator BTIF\_GATT\_CHRC\_AUTH

    <a id="_CPPv4NUt2_1123BTIF_GATT_CHRC_EXT_PROPE"></a>

    <a id="_CPPv3NUt2_1123BTIF_GATT_CHRC_EXT_PROPE"></a> <a id="btif__type_8h_1abc5c98fcc1211af2b80116dd6e0a035da20fadb90b2cf6db2b7bcb43dda7c821e"></a> enumerator BTIF\_GATT\_CHRC\_EXT\_PROP

<a id="_CPPv420btif_avrcp_oper_id_t"></a>

<a id="_CPPv320btif_avrcp_oper_id_t"></a> <a id="_CPPv220btif_avrcp_oper_id_t"></a> <a id="btif__type_8h_1a813bbc750789175d9d4bb14470cedf98"></a> enum btif\_avrcp\_oper\_id\_t
:   AVRCP operation ID definition.

    *Values:*

    <a id="_CPPv4N20btif_avrcp_oper_id_t28BTIF_AVRCP_OPER_ID_VOLUME_UPE"></a>

    <a id="_CPPv3N20btif_avrcp_oper_id_t28BTIF_AVRCP_OPER_ID_VOLUME_UPE"></a> <a id="_CPPv2N20btif_avrcp_oper_id_t28BTIF_AVRCP_OPER_ID_VOLUME_UPE"></a> <a id="btif__type_8h_1a813bbc750789175d9d4bb14470cedf98ab73e2bb41a7436f8752aef989014e1a0"></a> enumerator BTIF\_AVRCP\_OPER\_ID\_VOLUME\_UP

    <a id="_CPPv4N20btif_avrcp_oper_id_t30BTIF_AVRCP_OPER_ID_VOLUME_DOWNE"></a>

    <a id="_CPPv3N20btif_avrcp_oper_id_t30BTIF_AVRCP_OPER_ID_VOLUME_DOWNE"></a> <a id="_CPPv2N20btif_avrcp_oper_id_t30BTIF_AVRCP_OPER_ID_VOLUME_DOWNE"></a> <a id="btif__type_8h_1a813bbc750789175d9d4bb14470cedf98ac97617c1b8433c2dac236a8452551bfb"></a> enumerator BTIF\_AVRCP\_OPER\_ID\_VOLUME\_DOWN

    <a id="_CPPv4N20btif_avrcp_oper_id_t23BTIF_AVRCP_OPER_ID_PLAYE"></a>

    <a id="_CPPv3N20btif_avrcp_oper_id_t23BTIF_AVRCP_OPER_ID_PLAYE"></a> <a id="_CPPv2N20btif_avrcp_oper_id_t23BTIF_AVRCP_OPER_ID_PLAYE"></a> <a id="btif__type_8h_1a813bbc750789175d9d4bb14470cedf98a7de91a36d59f3cc4116a1698b3da797d"></a> enumerator BTIF\_AVRCP\_OPER\_ID\_PLAY

    <a id="_CPPv4N20btif_avrcp_oper_id_t23BTIF_AVRCP_OPER_ID_STOPE"></a>

    <a id="_CPPv3N20btif_avrcp_oper_id_t23BTIF_AVRCP_OPER_ID_STOPE"></a> <a id="_CPPv2N20btif_avrcp_oper_id_t23BTIF_AVRCP_OPER_ID_STOPE"></a> <a id="btif__type_8h_1a813bbc750789175d9d4bb14470cedf98a2c710339a9a06703479a6a705ca6d100"></a> enumerator BTIF\_AVRCP\_OPER\_ID\_STOP

    <a id="_CPPv4N20btif_avrcp_oper_id_t24BTIF_AVRCP_OPER_ID_PAUSEE"></a>

    <a id="_CPPv3N20btif_avrcp_oper_id_t24BTIF_AVRCP_OPER_ID_PAUSEE"></a> <a id="_CPPv2N20btif_avrcp_oper_id_t24BTIF_AVRCP_OPER_ID_PAUSEE"></a> <a id="btif__type_8h_1a813bbc750789175d9d4bb14470cedf98ad5cab4c8436f531f81618786cab46a24"></a> enumerator BTIF\_AVRCP\_OPER\_ID\_PAUSE

    <a id="_CPPv4N20btif_avrcp_oper_id_t25BTIF_AVRCP_OPER_ID_REWINDE"></a>

    <a id="_CPPv3N20btif_avrcp_oper_id_t25BTIF_AVRCP_OPER_ID_REWINDE"></a> <a id="_CPPv2N20btif_avrcp_oper_id_t25BTIF_AVRCP_OPER_ID_REWINDE"></a> <a id="btif__type_8h_1a813bbc750789175d9d4bb14470cedf98ae6a2fb6b1de4748df3210bb92f49938e"></a> enumerator BTIF\_AVRCP\_OPER\_ID\_REWIND

    <a id="_CPPv4N20btif_avrcp_oper_id_t31BTIF_AVRCP_OPER_ID_FAST_FORWARDE"></a>

    <a id="_CPPv3N20btif_avrcp_oper_id_t31BTIF_AVRCP_OPER_ID_FAST_FORWARDE"></a> <a id="_CPPv2N20btif_avrcp_oper_id_t31BTIF_AVRCP_OPER_ID_FAST_FORWARDE"></a> <a id="btif__type_8h_1a813bbc750789175d9d4bb14470cedf98acd6b6f5620ebb7f5e01e799e98482737"></a> enumerator BTIF\_AVRCP\_OPER\_ID\_FAST\_FORWARD

    <a id="_CPPv4N20btif_avrcp_oper_id_t26BTIF_AVRCP_OPER_ID_FORWARDE"></a>

    <a id="_CPPv3N20btif_avrcp_oper_id_t26BTIF_AVRCP_OPER_ID_FORWARDE"></a> <a id="_CPPv2N20btif_avrcp_oper_id_t26BTIF_AVRCP_OPER_ID_FORWARDE"></a> <a id="btif__type_8h_1a813bbc750789175d9d4bb14470cedf98ac5f88bc5dfd778bfe8153a8d20d372c5"></a> enumerator BTIF\_AVRCP\_OPER\_ID\_FORWARD

    <a id="_CPPv4N20btif_avrcp_oper_id_t27BTIF_AVRCP_OPER_ID_BACKWARDE"></a>

    <a id="_CPPv3N20btif_avrcp_oper_id_t27BTIF_AVRCP_OPER_ID_BACKWARDE"></a> <a id="_CPPv2N20btif_avrcp_oper_id_t27BTIF_AVRCP_OPER_ID_BACKWARDE"></a> <a id="btif__type_8h_1a813bbc750789175d9d4bb14470cedf98a75a0c088cf842137b22484aa612c7e41"></a> enumerator BTIF\_AVRCP\_OPER\_ID\_BACKWARD

    <a id="_CPPv4N20btif_avrcp_oper_id_t28BTIF_AVRCP_OPER_ID_UNDEFINEDE"></a>

    <a id="_CPPv3N20btif_avrcp_oper_id_t28BTIF_AVRCP_OPER_ID_UNDEFINEDE"></a> <a id="_CPPv2N20btif_avrcp_oper_id_t28BTIF_AVRCP_OPER_ID_UNDEFINEDE"></a> <a id="btif__type_8h_1a813bbc750789175d9d4bb14470cedf98a0419fe6cf8f0ee980d1c9c5cdd21f05d"></a> enumerator BTIF\_AVRCP\_OPER\_ID\_UNDEFINED

<a id="_CPPv421btif_avrcp_play_sts_t"></a>

<a id="_CPPv321btif_avrcp_play_sts_t"></a> <a id="_CPPv221btif_avrcp_play_sts_t"></a> <a id="btif__type_8h_1a8e96ba413a3cc7447731506d866348da"></a> enum btif\_avrcp\_play\_sts\_t
:   AVRCP play status definition.

    *Values:*

    <a id="_CPPv4N21btif_avrcp_play_sts_t18BTIF_AVRCP_STOPPEDE"></a>

    <a id="_CPPv3N21btif_avrcp_play_sts_t18BTIF_AVRCP_STOPPEDE"></a> <a id="_CPPv2N21btif_avrcp_play_sts_t18BTIF_AVRCP_STOPPEDE"></a> <a id="btif__type_8h_1a8e96ba413a3cc7447731506d866348daae367b178b7c3821d29881370b21973df"></a> enumerator BTIF\_AVRCP\_STOPPED

    <a id="_CPPv4N21btif_avrcp_play_sts_t18BTIF_AVRCP_PLAYINGE"></a>

    <a id="_CPPv3N21btif_avrcp_play_sts_t18BTIF_AVRCP_PLAYINGE"></a> <a id="_CPPv2N21btif_avrcp_play_sts_t18BTIF_AVRCP_PLAYINGE"></a> <a id="btif__type_8h_1a8e96ba413a3cc7447731506d866348daabee2334779046eb6ac6075d81c207dca"></a> enumerator BTIF\_AVRCP\_PLAYING

    <a id="_CPPv4N21btif_avrcp_play_sts_t17BTIF_AVRCP_PAUSEDE"></a>

    <a id="_CPPv3N21btif_avrcp_play_sts_t17BTIF_AVRCP_PAUSEDE"></a> <a id="_CPPv2N21btif_avrcp_play_sts_t17BTIF_AVRCP_PAUSEDE"></a> <a id="btif__type_8h_1a8e96ba413a3cc7447731506d866348daa7bdc4714ff9dd6eb3c60b457871d9f26"></a> enumerator BTIF\_AVRCP\_PAUSED

    <a id="_CPPv4N21btif_avrcp_play_sts_t19BTIF_AVRCP_FWD_SEEKE"></a>

    <a id="_CPPv3N21btif_avrcp_play_sts_t19BTIF_AVRCP_FWD_SEEKE"></a> <a id="_CPPv2N21btif_avrcp_play_sts_t19BTIF_AVRCP_FWD_SEEKE"></a> <a id="btif__type_8h_1a8e96ba413a3cc7447731506d866348daa50b158feb5a410d57625043ebd96a276"></a> enumerator BTIF\_AVRCP\_FWD\_SEEK

    <a id="_CPPv4N21btif_avrcp_play_sts_t19BTIF_AVRCP_REV_SEEKE"></a>

    <a id="_CPPv3N21btif_avrcp_play_sts_t19BTIF_AVRCP_REV_SEEKE"></a> <a id="_CPPv2N21btif_avrcp_play_sts_t19BTIF_AVRCP_REV_SEEKE"></a> <a id="btif__type_8h_1a8e96ba413a3cc7447731506d866348daa0ac6b3f24c4ab7b45854284ee792c4e3"></a> enumerator BTIF\_AVRCP\_REV\_SEEK

    <a id="_CPPv4N21btif_avrcp_play_sts_t16BTIF_AVRCP_ERRORE"></a>

    <a id="_CPPv3N21btif_avrcp_play_sts_t16BTIF_AVRCP_ERRORE"></a> <a id="_CPPv2N21btif_avrcp_play_sts_t16BTIF_AVRCP_ERRORE"></a> <a id="btif__type_8h_1a8e96ba413a3cc7447731506d866348daa26fbb28bbb95aa9566556db57292f0ba"></a> enumerator BTIF\_AVRCP\_ERROR

<a id="_CPPv423btif_avrcp_ntf_evt_id_t"></a>

<a id="_CPPv323btif_avrcp_ntf_evt_id_t"></a> <a id="_CPPv223btif_avrcp_ntf_evt_id_t"></a> <a id="btif__type_8h_1a3ad7bf3a59014e0adbb03afc7dabfaf6"></a> enum btif\_avrcp\_ntf\_evt\_id\_t
:   AVRCP notify event ID definition.

    *Values:*

    <a id="_CPPv4N23btif_avrcp_ntf_evt_id_t28BTIF_AVRCP_NTF_EVT_MIN_VALUEE"></a>

    <a id="_CPPv3N23btif_avrcp_ntf_evt_id_t28BTIF_AVRCP_NTF_EVT_MIN_VALUEE"></a> <a id="_CPPv2N23btif_avrcp_ntf_evt_id_t28BTIF_AVRCP_NTF_EVT_MIN_VALUEE"></a> <a id="btif__type_8h_1a3ad7bf3a59014e0adbb03afc7dabfaf6a9ffd4f68d5b9326d8675bdd0860d9114"></a> enumerator BTIF\_AVRCP\_NTF\_EVT\_MIN\_VALUE

    <a id="_CPPv4N23btif_avrcp_ntf_evt_id_t42BTIF_AVRCP_NTF_EVT_PLAYBACK_STATUS_CHANGEDE"></a>

    <a id="_CPPv3N23btif_avrcp_ntf_evt_id_t42BTIF_AVRCP_NTF_EVT_PLAYBACK_STATUS_CHANGEDE"></a> <a id="_CPPv2N23btif_avrcp_ntf_evt_id_t42BTIF_AVRCP_NTF_EVT_PLAYBACK_STATUS_CHANGEDE"></a> <a id="btif__type_8h_1a3ad7bf3a59014e0adbb03afc7dabfaf6ac868c3d19508ea1edeb338e3fe34ed48"></a> enumerator BTIF\_AVRCP\_NTF\_EVT\_PLAYBACK\_STATUS\_CHANGED

    <a id="_CPPv4N23btif_avrcp_ntf_evt_id_t32BTIF_AVRCP_NTF_EVT_TRACK_CHANGEDE"></a>

    <a id="_CPPv3N23btif_avrcp_ntf_evt_id_t32BTIF_AVRCP_NTF_EVT_TRACK_CHANGEDE"></a> <a id="_CPPv2N23btif_avrcp_ntf_evt_id_t32BTIF_AVRCP_NTF_EVT_TRACK_CHANGEDE"></a> <a id="btif__type_8h_1a3ad7bf3a59014e0adbb03afc7dabfaf6ad2293ea05c473cb1ccdb99b61c8b9c79"></a> enumerator BTIF\_AVRCP\_NTF\_EVT\_TRACK\_CHANGED

    <a id="_CPPv4N23btif_avrcp_ntf_evt_id_t36BTIF_AVRCP_NTF_EVT_TRACK_REACHED_ENDE"></a>

    <a id="_CPPv3N23btif_avrcp_ntf_evt_id_t36BTIF_AVRCP_NTF_EVT_TRACK_REACHED_ENDE"></a> <a id="_CPPv2N23btif_avrcp_ntf_evt_id_t36BTIF_AVRCP_NTF_EVT_TRACK_REACHED_ENDE"></a> <a id="btif__type_8h_1a3ad7bf3a59014e0adbb03afc7dabfaf6a301e1bae9465f4a7d8bfef5112e5d372"></a> enumerator BTIF\_AVRCP\_NTF\_EVT\_TRACK\_REACHED\_END

    <a id="_CPPv4N23btif_avrcp_ntf_evt_id_t38BTIF_AVRCP_NTF_EVT_TRACK_REACHED_STARTE"></a>

    <a id="_CPPv3N23btif_avrcp_ntf_evt_id_t38BTIF_AVRCP_NTF_EVT_TRACK_REACHED_STARTE"></a> <a id="_CPPv2N23btif_avrcp_ntf_evt_id_t38BTIF_AVRCP_NTF_EVT_TRACK_REACHED_STARTE"></a> <a id="btif__type_8h_1a3ad7bf3a59014e0adbb03afc7dabfaf6a17d082134514eb3cb3a5c9e5d1fde2f5"></a> enumerator BTIF\_AVRCP\_NTF\_EVT\_TRACK\_REACHED\_START

    <a id="_CPPv4N23btif_avrcp_ntf_evt_id_t39BTIF_AVRCP_NTF_EVT_PLAYBACK_POS_CHANGEDE"></a>

    <a id="_CPPv3N23btif_avrcp_ntf_evt_id_t39BTIF_AVRCP_NTF_EVT_PLAYBACK_POS_CHANGEDE"></a> <a id="_CPPv2N23btif_avrcp_ntf_evt_id_t39BTIF_AVRCP_NTF_EVT_PLAYBACK_POS_CHANGEDE"></a> <a id="btif__type_8h_1a3ad7bf3a59014e0adbb03afc7dabfaf6a4bcbc95662194ac92065eaf3deeefa56"></a> enumerator BTIF\_AVRCP\_NTF\_EVT\_PLAYBACK\_POS\_CHANGED

    <a id="_CPPv4N23btif_avrcp_ntf_evt_id_t38BTIF_AVRCP_NTF_EVT_BATT_STATUS_CHANGEDE"></a>

    <a id="_CPPv3N23btif_avrcp_ntf_evt_id_t38BTIF_AVRCP_NTF_EVT_BATT_STATUS_CHANGEDE"></a> <a id="_CPPv2N23btif_avrcp_ntf_evt_id_t38BTIF_AVRCP_NTF_EVT_BATT_STATUS_CHANGEDE"></a> <a id="btif__type_8h_1a3ad7bf3a59014e0adbb03afc7dabfaf6a957e732e5871b4da77875eac12feb3f1"></a> enumerator BTIF\_AVRCP\_NTF\_EVT\_BATT\_STATUS\_CHANGED

    <a id="_CPPv4N23btif_avrcp_ntf_evt_id_t40BTIF_AVRCP_NTF_EVT_SYSTEM_STATUS_CHANGEDE"></a>

    <a id="_CPPv3N23btif_avrcp_ntf_evt_id_t40BTIF_AVRCP_NTF_EVT_SYSTEM_STATUS_CHANGEDE"></a> <a id="_CPPv2N23btif_avrcp_ntf_evt_id_t40BTIF_AVRCP_NTF_EVT_SYSTEM_STATUS_CHANGEDE"></a> <a id="btif__type_8h_1a3ad7bf3a59014e0adbb03afc7dabfaf6aca3c03d6d11bb653934eebfd1a3fa3cf"></a> enumerator BTIF\_AVRCP\_NTF\_EVT\_SYSTEM\_STATUS\_CHANGED

    <a id="_CPPv4N23btif_avrcp_ntf_evt_id_t53BTIF_AVRCP_NTF_EVT_PLAYER_APPLICATION_SETTING_CHANGEDE"></a>

    <a id="_CPPv3N23btif_avrcp_ntf_evt_id_t53BTIF_AVRCP_NTF_EVT_PLAYER_APPLICATION_SETTING_CHANGEDE"></a> <a id="_CPPv2N23btif_avrcp_ntf_evt_id_t53BTIF_AVRCP_NTF_EVT_PLAYER_APPLICATION_SETTING_CHANGEDE"></a> <a id="btif__type_8h_1a3ad7bf3a59014e0adbb03afc7dabfaf6a10f956352f8d7b537069950a07d1d1e6"></a> enumerator BTIF\_AVRCP\_NTF\_EVT\_PLAYER\_APPLICATION\_SETTING\_CHANGED

    <a id="_CPPv4N23btif_avrcp_ntf_evt_id_t46BTIF_AVRCP_NTF_EVT_NOW_PLAYING_CONTENT_CHANGEDE"></a>

    <a id="_CPPv3N23btif_avrcp_ntf_evt_id_t46BTIF_AVRCP_NTF_EVT_NOW_PLAYING_CONTENT_CHANGEDE"></a> <a id="_CPPv2N23btif_avrcp_ntf_evt_id_t46BTIF_AVRCP_NTF_EVT_NOW_PLAYING_CONTENT_CHANGEDE"></a> <a id="btif__type_8h_1a3ad7bf3a59014e0adbb03afc7dabfaf6a15b8b6b61b5448822bccd2d08b30c994"></a> enumerator BTIF\_AVRCP\_NTF\_EVT\_NOW\_PLAYING\_CONTENT\_CHANGED

    <a id="_CPPv4N23btif_avrcp_ntf_evt_id_t44BTIF_AVRCP_NTF_EVT_AVAILABLE_PLAYERS_CHANGEDE"></a>

    <a id="_CPPv3N23btif_avrcp_ntf_evt_id_t44BTIF_AVRCP_NTF_EVT_AVAILABLE_PLAYERS_CHANGEDE"></a> <a id="_CPPv2N23btif_avrcp_ntf_evt_id_t44BTIF_AVRCP_NTF_EVT_AVAILABLE_PLAYERS_CHANGEDE"></a> <a id="btif__type_8h_1a3ad7bf3a59014e0adbb03afc7dabfaf6aece165d6db18d8e5993d297d9b1ea447"></a> enumerator BTIF\_AVRCP\_NTF\_EVT\_AVAILABLE\_PLAYERS\_CHANGED

    <a id="_CPPv4N23btif_avrcp_ntf_evt_id_t43BTIF_AVRCP_NTF_EVT_ADDRESSED_PLAYER_CHANGEDE"></a>

    <a id="_CPPv3N23btif_avrcp_ntf_evt_id_t43BTIF_AVRCP_NTF_EVT_ADDRESSED_PLAYER_CHANGEDE"></a> <a id="_CPPv2N23btif_avrcp_ntf_evt_id_t43BTIF_AVRCP_NTF_EVT_ADDRESSED_PLAYER_CHANGEDE"></a> <a id="btif__type_8h_1a3ad7bf3a59014e0adbb03afc7dabfaf6ab823b76d68661056379f0172b07d8e96"></a> enumerator BTIF\_AVRCP\_NTF\_EVT\_ADDRESSED\_PLAYER\_CHANGED

    <a id="_CPPv4N23btif_avrcp_ntf_evt_id_t31BTIF_AVRCP_NTF_EVT_UIDS_CHANGEDE"></a>

    <a id="_CPPv3N23btif_avrcp_ntf_evt_id_t31BTIF_AVRCP_NTF_EVT_UIDS_CHANGEDE"></a> <a id="_CPPv2N23btif_avrcp_ntf_evt_id_t31BTIF_AVRCP_NTF_EVT_UIDS_CHANGEDE"></a> <a id="btif__type_8h_1a3ad7bf3a59014e0adbb03afc7dabfaf6a3d256b47a8f7f7ab2e4e0716e84953a5"></a> enumerator BTIF\_AVRCP\_NTF\_EVT\_UIDS\_CHANGED

    <a id="_CPPv4N23btif_avrcp_ntf_evt_id_t33BTIF_AVRCP_NTF_EVT_VOLUME_CHANGEDE"></a>

    <a id="_CPPv3N23btif_avrcp_ntf_evt_id_t33BTIF_AVRCP_NTF_EVT_VOLUME_CHANGEDE"></a> <a id="_CPPv2N23btif_avrcp_ntf_evt_id_t33BTIF_AVRCP_NTF_EVT_VOLUME_CHANGEDE"></a> <a id="btif__type_8h_1a3ad7bf3a59014e0adbb03afc7dabfaf6a01c3c316be132900f20720aca81accd4"></a> enumerator BTIF\_AVRCP\_NTF\_EVT\_VOLUME\_CHANGED

    <a id="_CPPv4N23btif_avrcp_ntf_evt_id_t28BTIF_AVRCP_NTF_EVT_MAX_VALUEE"></a>

    <a id="_CPPv3N23btif_avrcp_ntf_evt_id_t28BTIF_AVRCP_NTF_EVT_MAX_VALUEE"></a> <a id="_CPPv2N23btif_avrcp_ntf_evt_id_t28BTIF_AVRCP_NTF_EVT_MAX_VALUEE"></a> <a id="btif__type_8h_1a3ad7bf3a59014e0adbb03afc7dabfaf6a99c0b0e0f849e8a7ac8ea4488d9d67c0"></a> enumerator BTIF\_AVRCP\_NTF\_EVT\_MAX\_VALUE

<a id="_CPPv421btif_avrcp_cmd_type_t"></a>

<a id="_CPPv321btif_avrcp_cmd_type_t"></a> <a id="_CPPv221btif_avrcp_cmd_type_t"></a> <a id="btif__type_8h_1a33171c7e6fd97156bd0c0edb274625e7"></a> enum btif\_avrcp\_cmd\_type\_t
:   AVRCP command type definition.

    *Values:*

    <a id="_CPPv4N21btif_avrcp_cmd_type_t27BTIF_AVRCP_CMD_TYPE_CONTROLE"></a>

    <a id="_CPPv3N21btif_avrcp_cmd_type_t27BTIF_AVRCP_CMD_TYPE_CONTROLE"></a> <a id="_CPPv2N21btif_avrcp_cmd_type_t27BTIF_AVRCP_CMD_TYPE_CONTROLE"></a> <a id="btif__type_8h_1a33171c7e6fd97156bd0c0edb274625e7a4a684cd0e12149459b0f79e8daddd916"></a> enumerator BTIF\_AVRCP\_CMD\_TYPE\_CONTROL

    <a id="_CPPv4N21btif_avrcp_cmd_type_t26BTIF_AVRCP_CMD_TYPE_STATUSE"></a>

    <a id="_CPPv3N21btif_avrcp_cmd_type_t26BTIF_AVRCP_CMD_TYPE_STATUSE"></a> <a id="_CPPv2N21btif_avrcp_cmd_type_t26BTIF_AVRCP_CMD_TYPE_STATUSE"></a> <a id="btif__type_8h_1a33171c7e6fd97156bd0c0edb274625e7ae5acffedec7ebd76ea19fc6546dd20aa"></a> enumerator BTIF\_AVRCP\_CMD\_TYPE\_STATUS

    <a id="_CPPv4N21btif_avrcp_cmd_type_t36BTIF_AVRCP_CMD_TYPE_SPECIFIC_INQUIRYE"></a>

    <a id="_CPPv3N21btif_avrcp_cmd_type_t36BTIF_AVRCP_CMD_TYPE_SPECIFIC_INQUIRYE"></a> <a id="_CPPv2N21btif_avrcp_cmd_type_t36BTIF_AVRCP_CMD_TYPE_SPECIFIC_INQUIRYE"></a> <a id="btif__type_8h_1a33171c7e6fd97156bd0c0edb274625e7add1c452f6501b01aba542c2f647f2c2a"></a> enumerator BTIF\_AVRCP\_CMD\_TYPE\_SPECIFIC\_INQUIRY

    <a id="_CPPv4N21btif_avrcp_cmd_type_t26BTIF_AVRCP_CMD_TYPE_NOTIFYE"></a>

    <a id="_CPPv3N21btif_avrcp_cmd_type_t26BTIF_AVRCP_CMD_TYPE_NOTIFYE"></a> <a id="_CPPv2N21btif_avrcp_cmd_type_t26BTIF_AVRCP_CMD_TYPE_NOTIFYE"></a> <a id="btif__type_8h_1a33171c7e6fd97156bd0c0edb274625e7aa83f6b58c84fb9b97312d8a32ad7e0ef"></a> enumerator BTIF\_AVRCP\_CMD\_TYPE\_NOTIFY

    <a id="_CPPv4N21btif_avrcp_cmd_type_t35BTIF_AVRCP_CMD_TYPE_GENERAL_INQUIRYE"></a>

    <a id="_CPPv3N21btif_avrcp_cmd_type_t35BTIF_AVRCP_CMD_TYPE_GENERAL_INQUIRYE"></a> <a id="_CPPv2N21btif_avrcp_cmd_type_t35BTIF_AVRCP_CMD_TYPE_GENERAL_INQUIRYE"></a> <a id="btif__type_8h_1a33171c7e6fd97156bd0c0edb274625e7a714b12a5706757d655f42c983cfef81f"></a> enumerator BTIF\_AVRCP\_CMD\_TYPE\_GENERAL\_INQUIRY

    <a id="_CPPv4N21btif_avrcp_cmd_type_t29BTIF_AVRCP_CMD_TYPE_RESERVED5E"></a>

    <a id="_CPPv3N21btif_avrcp_cmd_type_t29BTIF_AVRCP_CMD_TYPE_RESERVED5E"></a> <a id="_CPPv2N21btif_avrcp_cmd_type_t29BTIF_AVRCP_CMD_TYPE_RESERVED5E"></a> <a id="btif__type_8h_1a33171c7e6fd97156bd0c0edb274625e7a5e9e5f91ef2a10eb351db01184df5458"></a> enumerator BTIF\_AVRCP\_CMD\_TYPE\_RESERVED5

    <a id="_CPPv4N21btif_avrcp_cmd_type_t29BTIF_AVRCP_CMD_TYPE_RESERVED6E"></a>

    <a id="_CPPv3N21btif_avrcp_cmd_type_t29BTIF_AVRCP_CMD_TYPE_RESERVED6E"></a> <a id="_CPPv2N21btif_avrcp_cmd_type_t29BTIF_AVRCP_CMD_TYPE_RESERVED6E"></a> <a id="btif__type_8h_1a33171c7e6fd97156bd0c0edb274625e7ae683ec8651bed9f55d743dfe9aa990e5"></a> enumerator BTIF\_AVRCP\_CMD\_TYPE\_RESERVED6

    <a id="_CPPv4N21btif_avrcp_cmd_type_t29BTIF_AVRCP_CMD_TYPE_RESERVED7E"></a>

    <a id="_CPPv3N21btif_avrcp_cmd_type_t29BTIF_AVRCP_CMD_TYPE_RESERVED7E"></a> <a id="_CPPv2N21btif_avrcp_cmd_type_t29BTIF_AVRCP_CMD_TYPE_RESERVED7E"></a> <a id="btif__type_8h_1a33171c7e6fd97156bd0c0edb274625e7a8c41e0f89ee970f6d3f54f514708bd4e"></a> enumerator BTIF\_AVRCP\_CMD\_TYPE\_RESERVED7

    <a id="_CPPv4N21btif_avrcp_cmd_type_t39BTIF_AVRCP_CMD_TYPE_RSP_NOT_IMPLEMENTEDE"></a>

    <a id="_CPPv3N21btif_avrcp_cmd_type_t39BTIF_AVRCP_CMD_TYPE_RSP_NOT_IMPLEMENTEDE"></a> <a id="_CPPv2N21btif_avrcp_cmd_type_t39BTIF_AVRCP_CMD_TYPE_RSP_NOT_IMPLEMENTEDE"></a> <a id="btif__type_8h_1a33171c7e6fd97156bd0c0edb274625e7a80db6097651b4ed9819c27d4e4587b69"></a> enumerator BTIF\_AVRCP\_CMD\_TYPE\_RSP\_NOT\_IMPLEMENTED

    <a id="_CPPv4N21btif_avrcp_cmd_type_t32BTIF_AVRCP_CMD_TYPE_RSP_ACCEPTEDE"></a>

    <a id="_CPPv3N21btif_avrcp_cmd_type_t32BTIF_AVRCP_CMD_TYPE_RSP_ACCEPTEDE"></a> <a id="_CPPv2N21btif_avrcp_cmd_type_t32BTIF_AVRCP_CMD_TYPE_RSP_ACCEPTEDE"></a> <a id="btif__type_8h_1a33171c7e6fd97156bd0c0edb274625e7a1de069173807dbab061f1146e308a5f5"></a> enumerator BTIF\_AVRCP\_CMD\_TYPE\_RSP\_ACCEPTED

    <a id="_CPPv4N21btif_avrcp_cmd_type_t32BTIF_AVRCP_CMD_TYPE_RSP_REJECTEDE"></a>

    <a id="_CPPv3N21btif_avrcp_cmd_type_t32BTIF_AVRCP_CMD_TYPE_RSP_REJECTEDE"></a> <a id="_CPPv2N21btif_avrcp_cmd_type_t32BTIF_AVRCP_CMD_TYPE_RSP_REJECTEDE"></a> <a id="btif__type_8h_1a33171c7e6fd97156bd0c0edb274625e7a0e2b3b94489876c1698b70f4d9dec22c"></a> enumerator BTIF\_AVRCP\_CMD\_TYPE\_RSP\_REJECTED

    <a id="_CPPv4N21btif_avrcp_cmd_type_t37BTIF_AVRCP_CMD_TYPE_RSP_IN_TRANSITIONE"></a>

    <a id="_CPPv3N21btif_avrcp_cmd_type_t37BTIF_AVRCP_CMD_TYPE_RSP_IN_TRANSITIONE"></a> <a id="_CPPv2N21btif_avrcp_cmd_type_t37BTIF_AVRCP_CMD_TYPE_RSP_IN_TRANSITIONE"></a> <a id="btif__type_8h_1a33171c7e6fd97156bd0c0edb274625e7a1b025324ce493eba3bf162242546fcde"></a> enumerator BTIF\_AVRCP\_CMD\_TYPE\_RSP\_IN\_TRANSITION

    <a id="_CPPv4N21btif_avrcp_cmd_type_t42BTIF_AVRCP_CMD_TYPE_RSP_IMPLEMENTED_STABLEE"></a>

    <a id="_CPPv3N21btif_avrcp_cmd_type_t42BTIF_AVRCP_CMD_TYPE_RSP_IMPLEMENTED_STABLEE"></a> <a id="_CPPv2N21btif_avrcp_cmd_type_t42BTIF_AVRCP_CMD_TYPE_RSP_IMPLEMENTED_STABLEE"></a> <a id="btif__type_8h_1a33171c7e6fd97156bd0c0edb274625e7a8ba075ef0de510cba1dc206b676f0ac1"></a> enumerator BTIF\_AVRCP\_CMD\_TYPE\_RSP\_IMPLEMENTED\_STABLE

    <a id="_CPPv4N21btif_avrcp_cmd_type_t38BTIF_AVRCP_CMD_TYPE_RSP_CHANGED_STABLEE"></a>

    <a id="_CPPv3N21btif_avrcp_cmd_type_t38BTIF_AVRCP_CMD_TYPE_RSP_CHANGED_STABLEE"></a> <a id="_CPPv2N21btif_avrcp_cmd_type_t38BTIF_AVRCP_CMD_TYPE_RSP_CHANGED_STABLEE"></a> <a id="btif__type_8h_1a33171c7e6fd97156bd0c0edb274625e7a3a4e182d50f9c42a283ef1f6c70bfb21"></a> enumerator BTIF\_AVRCP\_CMD\_TYPE\_RSP\_CHANGED\_STABLE

    <a id="_CPPv4N21btif_avrcp_cmd_type_t32BTIF_AVRCP_CMD_TYPE_RSP_RESERVEDE"></a>

    <a id="_CPPv3N21btif_avrcp_cmd_type_t32BTIF_AVRCP_CMD_TYPE_RSP_RESERVEDE"></a> <a id="_CPPv2N21btif_avrcp_cmd_type_t32BTIF_AVRCP_CMD_TYPE_RSP_RESERVEDE"></a> <a id="btif__type_8h_1a33171c7e6fd97156bd0c0edb274625e7abb7a37d244300c3ab91cf7adc167fea8"></a> enumerator BTIF\_AVRCP\_CMD\_TYPE\_RSP\_RESERVED

    <a id="_CPPv4N21btif_avrcp_cmd_type_t31BTIF_AVRCP_CMD_TYPE_RSP_INTERIME"></a>

    <a id="_CPPv3N21btif_avrcp_cmd_type_t31BTIF_AVRCP_CMD_TYPE_RSP_INTERIME"></a> <a id="_CPPv2N21btif_avrcp_cmd_type_t31BTIF_AVRCP_CMD_TYPE_RSP_INTERIME"></a> <a id="btif__type_8h_1a33171c7e6fd97156bd0c0edb274625e7a78a51cc1af87cf3796fc38c9d159678d"></a> enumerator BTIF\_AVRCP\_CMD\_TYPE\_RSP\_INTERIM

<a id="_CPPv420btif_avrcp_cmd_sts_t"></a>

<a id="_CPPv320btif_avrcp_cmd_sts_t"></a> <a id="_CPPv220btif_avrcp_cmd_sts_t"></a> <a id="btif__type_8h_1a8658589a2c22d69405a661777d9c2d33"></a> enum btif\_avrcp\_cmd\_sts\_t
:   AVRCP command status definition.

    *Values:*

    <a id="_CPPv4N20btif_avrcp_cmd_sts_t30BTIF_AVRCP_COMMAND_STATUS_IDLEE"></a>

    <a id="_CPPv3N20btif_avrcp_cmd_sts_t30BTIF_AVRCP_COMMAND_STATUS_IDLEE"></a> <a id="_CPPv2N20btif_avrcp_cmd_sts_t30BTIF_AVRCP_COMMAND_STATUS_IDLEE"></a> <a id="btif__type_8h_1a8658589a2c22d69405a661777d9c2d33ada560b9487fe6f4c90c25de6e414de3b"></a> enumerator BTIF\_AVRCP\_COMMAND\_STATUS\_IDLE

    <a id="_CPPv4N20btif_avrcp_cmd_sts_t29BTIF_AVRCP_SEND_PRESS_COMMANDE"></a>

    <a id="_CPPv3N20btif_avrcp_cmd_sts_t29BTIF_AVRCP_SEND_PRESS_COMMANDE"></a> <a id="_CPPv2N20btif_avrcp_cmd_sts_t29BTIF_AVRCP_SEND_PRESS_COMMANDE"></a> <a id="btif__type_8h_1a8658589a2c22d69405a661777d9c2d33a6da48a3f894b2a82ee150ca3b819fd5a"></a> enumerator BTIF\_AVRCP\_SEND\_PRESS\_COMMAND

    <a id="_CPPv4N20btif_avrcp_cmd_sts_t31BTIF_AVRCP_SEND_RELEASE_COMMANDE"></a>

    <a id="_CPPv3N20btif_avrcp_cmd_sts_t31BTIF_AVRCP_SEND_RELEASE_COMMANDE"></a> <a id="_CPPv2N20btif_avrcp_cmd_sts_t31BTIF_AVRCP_SEND_RELEASE_COMMANDE"></a> <a id="btif__type_8h_1a8658589a2c22d69405a661777d9c2d33a6447ed84c1ac5b0aa3e1039f1959ebd0"></a> enumerator BTIF\_AVRCP\_SEND\_RELEASE\_COMMAND

    <a id="_CPPv4N20btif_avrcp_cmd_sts_t24BTIF_AVRCP_SEND_RESPONSEE"></a>

    <a id="_CPPv3N20btif_avrcp_cmd_sts_t24BTIF_AVRCP_SEND_RESPONSEE"></a> <a id="_CPPv2N20btif_avrcp_cmd_sts_t24BTIF_AVRCP_SEND_RESPONSEE"></a> <a id="btif__type_8h_1a8658589a2c22d69405a661777d9c2d33afd152279faa40d160ad4578d795435fa"></a> enumerator BTIF\_AVRCP\_SEND\_RESPONSE

    <a id="_CPPv4N20btif_avrcp_cmd_sts_t34BTIF_AVRCP_RECEIVED_PRESS_RESPONSEE"></a>

    <a id="_CPPv3N20btif_avrcp_cmd_sts_t34BTIF_AVRCP_RECEIVED_PRESS_RESPONSEE"></a> <a id="_CPPv2N20btif_avrcp_cmd_sts_t34BTIF_AVRCP_RECEIVED_PRESS_RESPONSEE"></a> <a id="btif__type_8h_1a8658589a2c22d69405a661777d9c2d33a0f76c79bb80da94e573629d3046da95e"></a> enumerator BTIF\_AVRCP\_RECEIVED\_PRESS\_RESPONSE

    <a id="_CPPv4N20btif_avrcp_cmd_sts_t36BTIF_AVRCP_RECEIVED_RELEASE_RESPONSEE"></a>

    <a id="_CPPv3N20btif_avrcp_cmd_sts_t36BTIF_AVRCP_RECEIVED_RELEASE_RESPONSEE"></a> <a id="_CPPv2N20btif_avrcp_cmd_sts_t36BTIF_AVRCP_RECEIVED_RELEASE_RESPONSEE"></a> <a id="btif__type_8h_1a8658589a2c22d69405a661777d9c2d33abd90686c026a84f3c1aa4bc1841e55f0"></a> enumerator BTIF\_AVRCP\_RECEIVED\_RELEASE\_RESPONSE

<a id="_CPPv425btif_a2dp_sbc_chan_mode_t"></a>

<a id="_CPPv325btif_a2dp_sbc_chan_mode_t"></a> <a id="_CPPv225btif_a2dp_sbc_chan_mode_t"></a> <a id="btif__type_8h_1acd70bfeed1fac3958b6f3217f906ab67"></a> enum btif\_a2dp\_sbc\_chan\_mode\_t
:   SBC channel mode deinfition.

    *Values:*

    <a id="_CPPv4N25btif_a2dp_sbc_chan_mode_t26BTIF_A2DP_SBC_JOINT_STEREOE"></a>

    <a id="_CPPv3N25btif_a2dp_sbc_chan_mode_t26BTIF_A2DP_SBC_JOINT_STEREOE"></a> <a id="_CPPv2N25btif_a2dp_sbc_chan_mode_t26BTIF_A2DP_SBC_JOINT_STEREOE"></a> <a id="btif__type_8h_1acd70bfeed1fac3958b6f3217f906ab67a14ce635ddb1297991ca46c48fdd6669d"></a> enumerator BTIF\_A2DP\_SBC\_JOINT\_STEREO

    <a id="_CPPv4N25btif_a2dp_sbc_chan_mode_t20BTIF_A2DP_SBC_STEREOE"></a>

    <a id="_CPPv3N25btif_a2dp_sbc_chan_mode_t20BTIF_A2DP_SBC_STEREOE"></a> <a id="_CPPv2N25btif_a2dp_sbc_chan_mode_t20BTIF_A2DP_SBC_STEREOE"></a> <a id="btif__type_8h_1acd70bfeed1fac3958b6f3217f906ab67aa74205ffe38c8033d0ddfb250a2a23dc"></a> enumerator BTIF\_A2DP\_SBC\_STEREO

    <a id="_CPPv4N25btif_a2dp_sbc_chan_mode_t26BTIF_A2DP_SBC_DUAL_CHANNELE"></a>

    <a id="_CPPv3N25btif_a2dp_sbc_chan_mode_t26BTIF_A2DP_SBC_DUAL_CHANNELE"></a> <a id="_CPPv2N25btif_a2dp_sbc_chan_mode_t26BTIF_A2DP_SBC_DUAL_CHANNELE"></a> <a id="btif__type_8h_1acd70bfeed1fac3958b6f3217f906ab67aa4536fe82f6338d59e7cc4ba2069d5d3"></a> enumerator BTIF\_A2DP\_SBC\_DUAL\_CHANNEL

    <a id="_CPPv4N25btif_a2dp_sbc_chan_mode_t18BTIF_A2DP_SBC_MONOE"></a>

    <a id="_CPPv3N25btif_a2dp_sbc_chan_mode_t18BTIF_A2DP_SBC_MONOE"></a> <a id="_CPPv2N25btif_a2dp_sbc_chan_mode_t18BTIF_A2DP_SBC_MONOE"></a> <a id="btif__type_8h_1acd70bfeed1fac3958b6f3217f906ab67adecc855cf077fe6fd0b1a145654cfcc3"></a> enumerator BTIF\_A2DP\_SBC\_MONO

<a id="_CPPv429btif_a2dp_sbc_sampling_freq_t"></a>

<a id="_CPPv329btif_a2dp_sbc_sampling_freq_t"></a> <a id="_CPPv229btif_a2dp_sbc_sampling_freq_t"></a> <a id="btif__type_8h_1a5da6ca0520253744c579ce6daa5f4766"></a> enum btif\_a2dp\_sbc\_sampling\_freq\_t
:   SBC sampling frequency definition.

    *Values:*

    <a id="_CPPv4N29btif_a2dp_sbc_sampling_freq_t24BTIF_A2DP_SBC_FREQ_48000E"></a>

    <a id="_CPPv3N29btif_a2dp_sbc_sampling_freq_t24BTIF_A2DP_SBC_FREQ_48000E"></a> <a id="_CPPv2N29btif_a2dp_sbc_sampling_freq_t24BTIF_A2DP_SBC_FREQ_48000E"></a> <a id="btif__type_8h_1a5da6ca0520253744c579ce6daa5f4766adf56b4db4ae5ddb0da985f17dd5edefc"></a> enumerator BTIF\_A2DP\_SBC\_FREQ\_48000

    <a id="_CPPv4N29btif_a2dp_sbc_sampling_freq_t24BTIF_A2DP_SBC_FREQ_44100E"></a>

    <a id="_CPPv3N29btif_a2dp_sbc_sampling_freq_t24BTIF_A2DP_SBC_FREQ_44100E"></a> <a id="_CPPv2N29btif_a2dp_sbc_sampling_freq_t24BTIF_A2DP_SBC_FREQ_44100E"></a> <a id="btif__type_8h_1a5da6ca0520253744c579ce6daa5f4766a9b720d4761cfe1aabccfdc5698717768"></a> enumerator BTIF\_A2DP\_SBC\_FREQ\_44100

    <a id="_CPPv4N29btif_a2dp_sbc_sampling_freq_t24BTIF_A2DP_SBC_FREQ_32000E"></a>

    <a id="_CPPv3N29btif_a2dp_sbc_sampling_freq_t24BTIF_A2DP_SBC_FREQ_32000E"></a> <a id="_CPPv2N29btif_a2dp_sbc_sampling_freq_t24BTIF_A2DP_SBC_FREQ_32000E"></a> <a id="btif__type_8h_1a5da6ca0520253744c579ce6daa5f4766ad03d5e0856d9746e3cea3938aba9e174"></a> enumerator BTIF\_A2DP\_SBC\_FREQ\_32000

    <a id="_CPPv4N29btif_a2dp_sbc_sampling_freq_t24BTIF_A2DP_SBC_FREQ_16000E"></a>

    <a id="_CPPv3N29btif_a2dp_sbc_sampling_freq_t24BTIF_A2DP_SBC_FREQ_16000E"></a> <a id="_CPPv2N29btif_a2dp_sbc_sampling_freq_t24BTIF_A2DP_SBC_FREQ_16000E"></a> <a id="btif__type_8h_1a5da6ca0520253744c579ce6daa5f4766af8ee16706cab667c4e08834655d89f65"></a> enumerator BTIF\_A2DP\_SBC\_FREQ\_16000

<a id="_CPPv425btif_a2dp_sbc_block_len_t"></a>

<a id="_CPPv325btif_a2dp_sbc_block_len_t"></a> <a id="_CPPv225btif_a2dp_sbc_block_len_t"></a> <a id="btif__type_8h_1a55e34afb53d0aa87bc8cb7551005e6e1"></a> enum btif\_a2dp\_sbc\_block\_len\_t
:   SBC block length definition.

    *Values:*

    <a id="_CPPv4N25btif_a2dp_sbc_block_len_t29BTIF_A2DP_SBC_BLOCK_LENGTH_16E"></a>

    <a id="_CPPv3N25btif_a2dp_sbc_block_len_t29BTIF_A2DP_SBC_BLOCK_LENGTH_16E"></a> <a id="_CPPv2N25btif_a2dp_sbc_block_len_t29BTIF_A2DP_SBC_BLOCK_LENGTH_16E"></a> <a id="btif__type_8h_1a55e34afb53d0aa87bc8cb7551005e6e1a62bf26d850a69db7da35def63694c109"></a> enumerator BTIF\_A2DP\_SBC\_BLOCK\_LENGTH\_16

    <a id="_CPPv4N25btif_a2dp_sbc_block_len_t29BTIF_A2DP_SBC_BLOCK_LENGTH_12E"></a>

    <a id="_CPPv3N25btif_a2dp_sbc_block_len_t29BTIF_A2DP_SBC_BLOCK_LENGTH_12E"></a> <a id="_CPPv2N25btif_a2dp_sbc_block_len_t29BTIF_A2DP_SBC_BLOCK_LENGTH_12E"></a> <a id="btif__type_8h_1a55e34afb53d0aa87bc8cb7551005e6e1a4fd4de765a41e528c61caba97c3ddb81"></a> enumerator BTIF\_A2DP\_SBC\_BLOCK\_LENGTH\_12

    <a id="_CPPv4N25btif_a2dp_sbc_block_len_t28BTIF_A2DP_SBC_BLOCK_LENGTH_8E"></a>

    <a id="_CPPv3N25btif_a2dp_sbc_block_len_t28BTIF_A2DP_SBC_BLOCK_LENGTH_8E"></a> <a id="_CPPv2N25btif_a2dp_sbc_block_len_t28BTIF_A2DP_SBC_BLOCK_LENGTH_8E"></a> <a id="btif__type_8h_1a55e34afb53d0aa87bc8cb7551005e6e1aca37f99c40c65d981ad5c9f869d0d3bd"></a> enumerator BTIF\_A2DP\_SBC\_BLOCK\_LENGTH\_8

    <a id="_CPPv4N25btif_a2dp_sbc_block_len_t28BTIF_A2DP_SBC_BLOCK_LENGTH_4E"></a>

    <a id="_CPPv3N25btif_a2dp_sbc_block_len_t28BTIF_A2DP_SBC_BLOCK_LENGTH_4E"></a> <a id="_CPPv2N25btif_a2dp_sbc_block_len_t28BTIF_A2DP_SBC_BLOCK_LENGTH_4E"></a> <a id="btif__type_8h_1a55e34afb53d0aa87bc8cb7551005e6e1a61c28de92fcd59e84ec8566cfe486311"></a> enumerator BTIF\_A2DP\_SBC\_BLOCK\_LENGTH\_4

<a id="_CPPv424btif_a2dp_sbc_subbands_t"></a>

<a id="_CPPv324btif_a2dp_sbc_subbands_t"></a> <a id="_CPPv224btif_a2dp_sbc_subbands_t"></a> <a id="btif__type_8h_1ad490036251e186cbdf5ac770c1802b1a"></a> enum btif\_a2dp\_sbc\_subbands\_t
:   SBC subbands definition.

    *Values:*

    <a id="_CPPv4N24btif_a2dp_sbc_subbands_t24BTIF_A2DP_SBC_SUBBANDS_8E"></a>

    <a id="_CPPv3N24btif_a2dp_sbc_subbands_t24BTIF_A2DP_SBC_SUBBANDS_8E"></a> <a id="_CPPv2N24btif_a2dp_sbc_subbands_t24BTIF_A2DP_SBC_SUBBANDS_8E"></a> <a id="btif__type_8h_1ad490036251e186cbdf5ac770c1802b1aa1cb77a46ed859ce72d37e4d22eb1d4f1"></a> enumerator BTIF\_A2DP\_SBC\_SUBBANDS\_8

    <a id="_CPPv4N24btif_a2dp_sbc_subbands_t24BTIF_A2DP_SBC_SUBBANDS_4E"></a>

    <a id="_CPPv3N24btif_a2dp_sbc_subbands_t24BTIF_A2DP_SBC_SUBBANDS_4E"></a> <a id="_CPPv2N24btif_a2dp_sbc_subbands_t24BTIF_A2DP_SBC_SUBBANDS_4E"></a> <a id="btif__type_8h_1ad490036251e186cbdf5ac770c1802b1aa5000f92cca4f5cdb1f675d0977c263d7"></a> enumerator BTIF\_A2DP\_SBC\_SUBBANDS\_4

<a id="_CPPv433btif_a2dp_sbc_allocation_method_t"></a>

<a id="_CPPv333btif_a2dp_sbc_allocation_method_t"></a> <a id="_CPPv233btif_a2dp_sbc_allocation_method_t"></a> <a id="btif__type_8h_1a320d2d46a28a3fa0ec23f2f1efa73a5f"></a> enum btif\_a2dp\_sbc\_allocation\_method\_t
:   *Values:*

    <a id="_CPPv4N33btif_a2dp_sbc_allocation_method_t40BTIF_A2DP_SBC_ALLOCATION_METHOD_LOUDNESSE"></a>

    <a id="_CPPv3N33btif_a2dp_sbc_allocation_method_t40BTIF_A2DP_SBC_ALLOCATION_METHOD_LOUDNESSE"></a> <a id="_CPPv2N33btif_a2dp_sbc_allocation_method_t40BTIF_A2DP_SBC_ALLOCATION_METHOD_LOUDNESSE"></a> <a id="btif__type_8h_1a320d2d46a28a3fa0ec23f2f1efa73a5fa909014ae1676114346b855e4fb4df545"></a> enumerator BTIF\_A2DP\_SBC\_ALLOCATION\_METHOD\_LOUDNESS

    <a id="_CPPv4N33btif_a2dp_sbc_allocation_method_t35BTIF_A2DP_SBC_ALLOCATION_METHOD_SNRE"></a>

    <a id="_CPPv3N33btif_a2dp_sbc_allocation_method_t35BTIF_A2DP_SBC_ALLOCATION_METHOD_SNRE"></a> <a id="_CPPv2N33btif_a2dp_sbc_allocation_method_t35BTIF_A2DP_SBC_ALLOCATION_METHOD_SNRE"></a> <a id="btif__type_8h_1a320d2d46a28a3fa0ec23f2f1efa73a5fa0071f7c05b9ff8ab826d151380dc1a7d"></a> enumerator BTIF\_A2DP\_SBC\_ALLOCATION\_METHOD\_SNR

<a id="_CPPv427btif_a2dp_aac_object_type_t"></a>

<a id="_CPPv327btif_a2dp_aac_object_type_t"></a> <a id="_CPPv227btif_a2dp_aac_object_type_t"></a> <a id="btif__type_8h_1a08d79501e0f1208e2b5fd150b65bcfd4"></a> enum btif\_a2dp\_aac\_object\_type\_t
:   A2DP AAC object type definition.

    *Values:*

    <a id="_CPPv4N27btif_a2dp_aac_object_type_t41BTIF_A2DP_AAC_OBJ_TYPE_MPEG4_AAC_SCALABLEE"></a>

    <a id="_CPPv3N27btif_a2dp_aac_object_type_t41BTIF_A2DP_AAC_OBJ_TYPE_MPEG4_AAC_SCALABLEE"></a> <a id="_CPPv2N27btif_a2dp_aac_object_type_t41BTIF_A2DP_AAC_OBJ_TYPE_MPEG4_AAC_SCALABLEE"></a> <a id="btif__type_8h_1a08d79501e0f1208e2b5fd150b65bcfd4af5826865908a501a3c374a29f2aa226d"></a> enumerator BTIF\_A2DP\_AAC\_OBJ\_TYPE\_MPEG4\_AAC\_SCALABLE

    <a id="_CPPv4N27btif_a2dp_aac_object_type_t36BTIF_A2DP_AAC_OBJ_TYPE_MPEG4_AAC_LTPE"></a>

    <a id="_CPPv3N27btif_a2dp_aac_object_type_t36BTIF_A2DP_AAC_OBJ_TYPE_MPEG4_AAC_LTPE"></a> <a id="_CPPv2N27btif_a2dp_aac_object_type_t36BTIF_A2DP_AAC_OBJ_TYPE_MPEG4_AAC_LTPE"></a> <a id="btif__type_8h_1a08d79501e0f1208e2b5fd150b65bcfd4ac2cda2fce5c2beeeeecf059107a14441"></a> enumerator BTIF\_A2DP\_AAC\_OBJ\_TYPE\_MPEG4\_AAC\_LTP

    <a id="_CPPv4N27btif_a2dp_aac_object_type_t35BTIF_A2DP_AAC_OBJ_TYPE_MPEG4_AAC_LCE"></a>

    <a id="_CPPv3N27btif_a2dp_aac_object_type_t35BTIF_A2DP_AAC_OBJ_TYPE_MPEG4_AAC_LCE"></a> <a id="_CPPv2N27btif_a2dp_aac_object_type_t35BTIF_A2DP_AAC_OBJ_TYPE_MPEG4_AAC_LCE"></a> <a id="btif__type_8h_1a08d79501e0f1208e2b5fd150b65bcfd4a0885ff57fabf10fc0912830814806885"></a> enumerator BTIF\_A2DP\_AAC\_OBJ\_TYPE\_MPEG4\_AAC\_LC

    <a id="_CPPv4N27btif_a2dp_aac_object_type_t35BTIF_A2DP_AAC_OBJ_TYPE_MPEG2_AAC_LCE"></a>

    <a id="_CPPv3N27btif_a2dp_aac_object_type_t35BTIF_A2DP_AAC_OBJ_TYPE_MPEG2_AAC_LCE"></a> <a id="_CPPv2N27btif_a2dp_aac_object_type_t35BTIF_A2DP_AAC_OBJ_TYPE_MPEG2_AAC_LCE"></a> <a id="btif__type_8h_1a08d79501e0f1208e2b5fd150b65bcfd4ad7e530e08bb911f0017f253309ee9746"></a> enumerator BTIF\_A2DP\_AAC\_OBJ\_TYPE\_MPEG2\_AAC\_LC

<a id="_CPPv429btif_a2dp_aac_sampling_freq_t"></a>

<a id="_CPPv329btif_a2dp_aac_sampling_freq_t"></a> <a id="_CPPv229btif_a2dp_aac_sampling_freq_t"></a> <a id="btif__type_8h_1ac00513db80e3dfadab32ef1df0e9909e"></a> enum btif\_a2dp\_aac\_sampling\_freq\_t
:   AAC Sampling Frequency definition 2Bytes Byte0: bit7 \- bit0 Byte1: bit7 \- bit4.

    *Values:*

    <a id="_CPPv4N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_44100E"></a>

    <a id="_CPPv3N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_44100E"></a> <a id="_CPPv2N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_44100E"></a> <a id="btif__type_8h_1ac00513db80e3dfadab32ef1df0e9909ea4bf4fda0ca8ae79b71389b8f2644214e"></a> enumerator BTIF\_A2DP\_AAC\_FREQ\_44100

    <a id="_CPPv4N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_32000E"></a>

    <a id="_CPPv3N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_32000E"></a> <a id="_CPPv2N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_32000E"></a> <a id="btif__type_8h_1ac00513db80e3dfadab32ef1df0e9909ea82bc2befc0e0fc8d89d628ac01c7990a"></a> enumerator BTIF\_A2DP\_AAC\_FREQ\_32000

    <a id="_CPPv4N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_24000E"></a>

    <a id="_CPPv3N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_24000E"></a> <a id="_CPPv2N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_24000E"></a> <a id="btif__type_8h_1ac00513db80e3dfadab32ef1df0e9909eafbd402600b26295ebedd30b1c92cab5c"></a> enumerator BTIF\_A2DP\_AAC\_FREQ\_24000

    <a id="_CPPv4N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_22050E"></a>

    <a id="_CPPv3N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_22050E"></a> <a id="_CPPv2N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_22050E"></a> <a id="btif__type_8h_1ac00513db80e3dfadab32ef1df0e9909eae10836844856aa4f004dbdcf9568504e"></a> enumerator BTIF\_A2DP\_AAC\_FREQ\_22050

    <a id="_CPPv4N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_16000E"></a>

    <a id="_CPPv3N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_16000E"></a> <a id="_CPPv2N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_16000E"></a> <a id="btif__type_8h_1ac00513db80e3dfadab32ef1df0e9909ea0f967e7eada8ab6da93561d6b8588907"></a> enumerator BTIF\_A2DP\_AAC\_FREQ\_16000

    <a id="_CPPv4N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_12000E"></a>

    <a id="_CPPv3N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_12000E"></a> <a id="_CPPv2N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_12000E"></a> <a id="btif__type_8h_1ac00513db80e3dfadab32ef1df0e9909ea16170688345d61aaddf4bb741ad3e128"></a> enumerator BTIF\_A2DP\_AAC\_FREQ\_12000

    <a id="_CPPv4N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_11025E"></a>

    <a id="_CPPv3N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_11025E"></a> <a id="_CPPv2N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_11025E"></a> <a id="btif__type_8h_1ac00513db80e3dfadab32ef1df0e9909ea88f1da4a36e1b52f18dd2233aeb69429"></a> enumerator BTIF\_A2DP\_AAC\_FREQ\_11025

    <a id="_CPPv4N29btif_a2dp_aac_sampling_freq_t23BTIF_A2DP_AAC_FREQ_8000E"></a>

    <a id="_CPPv3N29btif_a2dp_aac_sampling_freq_t23BTIF_A2DP_AAC_FREQ_8000E"></a> <a id="_CPPv2N29btif_a2dp_aac_sampling_freq_t23BTIF_A2DP_AAC_FREQ_8000E"></a> <a id="btif__type_8h_1ac00513db80e3dfadab32ef1df0e9909ea2b4ee5c1fdf4ba6da54ec941e5d74bbd"></a> enumerator BTIF\_A2DP\_AAC\_FREQ\_8000

    <a id="_CPPv4N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_96000E"></a>

    <a id="_CPPv3N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_96000E"></a> <a id="_CPPv2N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_96000E"></a> <a id="btif__type_8h_1ac00513db80e3dfadab32ef1df0e9909ea306a45e9fb69b65fb6bb0d61dba09c9a"></a> enumerator BTIF\_A2DP\_AAC\_FREQ\_96000

    <a id="_CPPv4N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_88200E"></a>

    <a id="_CPPv3N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_88200E"></a> <a id="_CPPv2N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_88200E"></a> <a id="btif__type_8h_1ac00513db80e3dfadab32ef1df0e9909ea90f0a7a97d98e8c395a0dc77a98332bc"></a> enumerator BTIF\_A2DP\_AAC\_FREQ\_88200

    <a id="_CPPv4N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_64000E"></a>

    <a id="_CPPv3N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_64000E"></a> <a id="_CPPv2N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_64000E"></a> <a id="btif__type_8h_1ac00513db80e3dfadab32ef1df0e9909ea268a94ef42648169be729de4153d6760"></a> enumerator BTIF\_A2DP\_AAC\_FREQ\_64000

    <a id="_CPPv4N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_48000E"></a>

    <a id="_CPPv3N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_48000E"></a> <a id="_CPPv2N29btif_a2dp_aac_sampling_freq_t24BTIF_A2DP_AAC_FREQ_48000E"></a> <a id="btif__type_8h_1ac00513db80e3dfadab32ef1df0e9909ea6bb1f0ac3743b42a2a78bff0e58f68ab"></a> enumerator BTIF\_A2DP\_AAC\_FREQ\_48000

<a id="_CPPv428btif_a2dp_aac_channel_mode_t"></a>

<a id="_CPPv328btif_a2dp_aac_channel_mode_t"></a> <a id="_CPPv228btif_a2dp_aac_channel_mode_t"></a> <a id="btif__type_8h_1a92bcc2d466bd052f3c4f91ad4937b135"></a> enum btif\_a2dp\_aac\_channel\_mode\_t
:   AAC channel Bitmap definition bit0 \- bit4.

    *Values:*

    <a id="_CPPv4N28btif_a2dp_aac_channel_mode_t20BTIF_A2DP_AAC_CHAN_1E"></a>

    <a id="_CPPv3N28btif_a2dp_aac_channel_mode_t20BTIF_A2DP_AAC_CHAN_1E"></a> <a id="_CPPv2N28btif_a2dp_aac_channel_mode_t20BTIF_A2DP_AAC_CHAN_1E"></a> <a id="btif__type_8h_1a92bcc2d466bd052f3c4f91ad4937b135a13cc37cce835a322ae6af8e1695fb739"></a> enumerator BTIF\_A2DP\_AAC\_CHAN\_1

    <a id="_CPPv4N28btif_a2dp_aac_channel_mode_t20BTIF_A2DP_AAC_CHAN_2E"></a>

    <a id="_CPPv3N28btif_a2dp_aac_channel_mode_t20BTIF_A2DP_AAC_CHAN_2E"></a> <a id="_CPPv2N28btif_a2dp_aac_channel_mode_t20BTIF_A2DP_AAC_CHAN_2E"></a> <a id="btif__type_8h_1a92bcc2d466bd052f3c4f91ad4937b135adff568a19f3f5c785dea59229f427e7e"></a> enumerator BTIF\_A2DP\_AAC\_CHAN\_2

    <a id="_CPPv4N28btif_a2dp_aac_channel_mode_t20BTIF_A2DP_AAC_CHAN_6E"></a>

    <a id="_CPPv3N28btif_a2dp_aac_channel_mode_t20BTIF_A2DP_AAC_CHAN_6E"></a> <a id="_CPPv2N28btif_a2dp_aac_channel_mode_t20BTIF_A2DP_AAC_CHAN_6E"></a> <a id="btif__type_8h_1a92bcc2d466bd052f3c4f91ad4937b135ac5ced5a9de9b25db43e983c43eeb0fa3"></a> enumerator BTIF\_A2DP\_AAC\_CHAN\_6

    <a id="_CPPv4N28btif_a2dp_aac_channel_mode_t20BTIF_A2DP_AAC_CHAN_8E"></a>

    <a id="_CPPv3N28btif_a2dp_aac_channel_mode_t20BTIF_A2DP_AAC_CHAN_8E"></a> <a id="_CPPv2N28btif_a2dp_aac_channel_mode_t20BTIF_A2DP_AAC_CHAN_8E"></a> <a id="btif__type_8h_1a92bcc2d466bd052f3c4f91ad4937b135a850d5a2ef7c05d5a54b6bb5ecb3ae3bb"></a> enumerator BTIF\_A2DP\_AAC\_CHAN\_8

<a id="_CPPv419btif_a2dp_aac_vbr_t"></a>

<a id="_CPPv319btif_a2dp_aac_vbr_t"></a> <a id="_CPPv219btif_a2dp_aac_vbr_t"></a> <a id="btif__type_8h_1ac43011ea83f5ec9abeb4fbf79a17d8dd"></a> enum btif\_a2dp\_aac\_vbr\_t
:   AAC VBR definition bit7.

    *Values:*

    <a id="_CPPv4N19btif_a2dp_aac_vbr_t31BTIF_A2DP_AAC_VBR_NOT_SUPPORTEDE"></a>

    <a id="_CPPv3N19btif_a2dp_aac_vbr_t31BTIF_A2DP_AAC_VBR_NOT_SUPPORTEDE"></a> <a id="_CPPv2N19btif_a2dp_aac_vbr_t31BTIF_A2DP_AAC_VBR_NOT_SUPPORTEDE"></a> <a id="btif__type_8h_1ac43011ea83f5ec9abeb4fbf79a17d8dda7e1586e9269357f2655f6112df28a8fe"></a> enumerator BTIF\_A2DP\_AAC\_VBR\_NOT\_SUPPORTED

    <a id="_CPPv4N19btif_a2dp_aac_vbr_t27BTIF_A2DP_AAC_VBR_SUPPORTEDE"></a>

    <a id="_CPPv3N19btif_a2dp_aac_vbr_t27BTIF_A2DP_AAC_VBR_SUPPORTEDE"></a> <a id="_CPPv2N19btif_a2dp_aac_vbr_t27BTIF_A2DP_AAC_VBR_SUPPORTEDE"></a> <a id="btif__type_8h_1ac43011ea83f5ec9abeb4fbf79a17d8ddaea56d980ca7bbbe3d46855a52142154b"></a> enumerator BTIF\_A2DP\_AAC\_VBR\_SUPPORTED

<a id="_CPPv430btif_a2dp_ldac_sampling_freq_t"></a>

<a id="_CPPv330btif_a2dp_ldac_sampling_freq_t"></a> <a id="_CPPv230btif_a2dp_ldac_sampling_freq_t"></a> <a id="btif__type_8h_1abe74371c6557fdd6cb74ec5d41cf118e"></a> enum btif\_a2dp\_ldac\_sampling\_freq\_t
:   LDAC sampling frequency definition.

    *Values:*

    <a id="_CPPv4N30btif_a2dp_ldac_sampling_freq_t26BTIF_A2DP_LDAC_FREQ_192000E"></a>

    <a id="_CPPv3N30btif_a2dp_ldac_sampling_freq_t26BTIF_A2DP_LDAC_FREQ_192000E"></a> <a id="_CPPv2N30btif_a2dp_ldac_sampling_freq_t26BTIF_A2DP_LDAC_FREQ_192000E"></a> <a id="btif__type_8h_1abe74371c6557fdd6cb74ec5d41cf118ea7219b465db880bc88d1aaa7f55debb57"></a> enumerator BTIF\_A2DP\_LDAC\_FREQ\_192000

    <a id="_CPPv4N30btif_a2dp_ldac_sampling_freq_t26BTIF_A2DP_LDAC_FREQ_176400E"></a>

    <a id="_CPPv3N30btif_a2dp_ldac_sampling_freq_t26BTIF_A2DP_LDAC_FREQ_176400E"></a> <a id="_CPPv2N30btif_a2dp_ldac_sampling_freq_t26BTIF_A2DP_LDAC_FREQ_176400E"></a> <a id="btif__type_8h_1abe74371c6557fdd6cb74ec5d41cf118ea5d6e8497b37c9268a27751bd48385998"></a> enumerator BTIF\_A2DP\_LDAC\_FREQ\_176400

    <a id="_CPPv4N30btif_a2dp_ldac_sampling_freq_t25BTIF_A2DP_LDAC_FREQ_96000E"></a>

    <a id="_CPPv3N30btif_a2dp_ldac_sampling_freq_t25BTIF_A2DP_LDAC_FREQ_96000E"></a> <a id="_CPPv2N30btif_a2dp_ldac_sampling_freq_t25BTIF_A2DP_LDAC_FREQ_96000E"></a> <a id="btif__type_8h_1abe74371c6557fdd6cb74ec5d41cf118ea3bc02eb7ed9b25fe5506f7590cdcd75e"></a> enumerator BTIF\_A2DP\_LDAC\_FREQ\_96000

    <a id="_CPPv4N30btif_a2dp_ldac_sampling_freq_t25BTIF_A2DP_LDAC_FREQ_88200E"></a>

    <a id="_CPPv3N30btif_a2dp_ldac_sampling_freq_t25BTIF_A2DP_LDAC_FREQ_88200E"></a> <a id="_CPPv2N30btif_a2dp_ldac_sampling_freq_t25BTIF_A2DP_LDAC_FREQ_88200E"></a> <a id="btif__type_8h_1abe74371c6557fdd6cb74ec5d41cf118ea0ec3deb4d4d4ecd94b11cf7539e72df3"></a> enumerator BTIF\_A2DP\_LDAC\_FREQ\_88200

    <a id="_CPPv4N30btif_a2dp_ldac_sampling_freq_t25BTIF_A2DP_LDAC_FREQ_48000E"></a>

    <a id="_CPPv3N30btif_a2dp_ldac_sampling_freq_t25BTIF_A2DP_LDAC_FREQ_48000E"></a> <a id="_CPPv2N30btif_a2dp_ldac_sampling_freq_t25BTIF_A2DP_LDAC_FREQ_48000E"></a> <a id="btif__type_8h_1abe74371c6557fdd6cb74ec5d41cf118ea693ad445b06bffe10e3817c48a30202f"></a> enumerator BTIF\_A2DP\_LDAC\_FREQ\_48000

    <a id="_CPPv4N30btif_a2dp_ldac_sampling_freq_t25BTIF_A2DP_LDAC_FREQ_44100E"></a>

    <a id="_CPPv3N30btif_a2dp_ldac_sampling_freq_t25BTIF_A2DP_LDAC_FREQ_44100E"></a> <a id="_CPPv2N30btif_a2dp_ldac_sampling_freq_t25BTIF_A2DP_LDAC_FREQ_44100E"></a> <a id="btif__type_8h_1abe74371c6557fdd6cb74ec5d41cf118ea5d531822c034a06d458bb981acaf4343"></a> enumerator BTIF\_A2DP\_LDAC\_FREQ\_44100

<a id="_CPPv426btif_a2dp_ldac_chan_mode_t"></a>

<a id="_CPPv326btif_a2dp_ldac_chan_mode_t"></a> <a id="_CPPv226btif_a2dp_ldac_chan_mode_t"></a> <a id="btif__type_8h_1a48b671a9c0a82e951ca99018c0c02712"></a> enum btif\_a2dp\_ldac\_chan\_mode\_t
:   LDAC channel mode definition.

    *Values:*

    <a id="_CPPv4N26btif_a2dp_ldac_chan_mode_t29BTIF_A2DP_LDAC_STEREO_CHANNELE"></a>

    <a id="_CPPv3N26btif_a2dp_ldac_chan_mode_t29BTIF_A2DP_LDAC_STEREO_CHANNELE"></a> <a id="_CPPv2N26btif_a2dp_ldac_chan_mode_t29BTIF_A2DP_LDAC_STEREO_CHANNELE"></a> <a id="btif__type_8h_1a48b671a9c0a82e951ca99018c0c02712a7fc5be2c9f2d6e7b6f17807e33e0682e"></a> enumerator BTIF\_A2DP\_LDAC\_STEREO\_CHANNEL

    <a id="_CPPv4N26btif_a2dp_ldac_chan_mode_t27BTIF_A2DP_LDAC_DUAL_CHANNELE"></a>

    <a id="_CPPv3N26btif_a2dp_ldac_chan_mode_t27BTIF_A2DP_LDAC_DUAL_CHANNELE"></a> <a id="_CPPv2N26btif_a2dp_ldac_chan_mode_t27BTIF_A2DP_LDAC_DUAL_CHANNELE"></a> <a id="btif__type_8h_1a48b671a9c0a82e951ca99018c0c02712a43dd5d0bf7c06171940b5c6ec3de49db"></a> enumerator BTIF\_A2DP\_LDAC\_DUAL\_CHANNEL

    <a id="_CPPv4N26btif_a2dp_ldac_chan_mode_t27BTIF_A2DP_LDAC_MONO_CHANNELE"></a>

    <a id="_CPPv3N26btif_a2dp_ldac_chan_mode_t27BTIF_A2DP_LDAC_MONO_CHANNELE"></a> <a id="_CPPv2N26btif_a2dp_ldac_chan_mode_t27BTIF_A2DP_LDAC_MONO_CHANNELE"></a> <a id="btif__type_8h_1a48b671a9c0a82e951ca99018c0c02712a734943b5338c3b9826c44ed994ebfec8"></a> enumerator BTIF\_A2DP\_LDAC\_MONO\_CHANNEL
