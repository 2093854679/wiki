---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/btif/lescan_if.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="lescan-interface-functions"></a>

# LESCAN Interface Functions

<a id="lescan-if-api-brief"></a>

## LESCAN\_IF API Brief

| Application | Brief |
| --- | --- |
| [`lescan_if_scan_enable()`](#_CPPv421lescan_if_scan_enableP16lescan_if_para_t "lescan_if_scan_enable") | enable ble scan |
| [`lescan_if_scan_disable()`](#_CPPv422lescan_if_scan_disablev "lescan_if_scan_disable") | disable ble scan |
| [`lescan_if_start_PA_sync()`](#_CPPv423lescan_if_start_PA_syncP24lescan_if_PA_sync_para_t "lescan_if_start_PA_sync") | start sync to PA |
| [`lescan_if_terminate_PA_sync()`](#_CPPv427lescan_if_terminate_PA_sync8uint16_t "lescan_if_terminate_PA_sync") | terminate PA sync link |

<a id="lescan-if-api-reference"></a>

## LESCAN\_IF API Reference

<a id="header-file"></a>

### Header File

- [btif/inc/lescan\_if.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/btif/inc/lescan_if.h)

<a id="functions"></a>

### Functions

<a id="_CPPv421lescan_if_scan_enableP16lescan_if_para_t"></a>

<a id="_CPPv321lescan_if_scan_enableP16lescan_if_para_t"></a> <a id="_CPPv221lescan_if_scan_enableP16lescan_if_para_t"></a> <a id="lescan_if_scan_enable__lescan_if_para_tP"></a> <a id="lescan__if_8h_1a7c0e98a9a25556cfd00d674919a2bba4"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") lescan\_if\_scan\_enable([lescan\_if\_para\_t](#_CPPv416lescan_if_para_t "lescan_if_para_t") \*p\_scan\_param)
:   enable ble scan.

    enable ble scan using the configured parameters

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422lescan_if_scan_disablev"></a>

<a id="_CPPv322lescan_if_scan_disablev"></a> <a id="_CPPv222lescan_if_scan_disablev"></a> <a id="lescan_if_scan_disable__void"></a> <a id="lescan__if_8h_1a3f5d036b6598200ec5c0ab02cc54a69a"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") lescan\_if\_scan\_disable(void)
:   disable ble scan.

    disable ble scan

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv423lescan_if_start_PA_syncP24lescan_if_PA_sync_para_t"></a>

<a id="_CPPv323lescan_if_start_PA_syncP24lescan_if_PA_sync_para_t"></a> <a id="_CPPv223lescan_if_start_PA_syncP24lescan_if_PA_sync_para_t"></a> <a id="lescan_if_start_PA_sync__lescan_if_PA_sync_para_tP"></a> <a id="lescan__if_8h_1a5fe83ee704e1ec9a4ec881778e5d8f64"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") lescan\_if\_start\_PA\_sync([lescan\_if\_PA\_sync\_para\_t](#_CPPv424lescan_if_PA_sync_para_t "lescan_if_PA_sync_para_t") \*p\_PA\_sync\_param)
:   lescan\_if\_start\_PA\_sync brief description

    start sync to PA

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427lescan_if_terminate_PA_sync8uint16_t"></a>

<a id="_CPPv327lescan_if_terminate_PA_sync8uint16_t"></a> <a id="_CPPv227lescan_if_terminate_PA_sync8uint16_t"></a> <a id="lescan_if_terminate_PA_sync__uint16_t"></a> <a id="lescan__if_8h_1a8ae52804d867ae13ecc686818c8853c4"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") lescan\_if\_terminate\_PA\_sync(uint16\_t PA\_handle)
:   lescan\_if\_terminate\_PA\_sync brief description

    terminate PA sync link

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv414root_buff_if_t"></a>

<a id="_CPPv314root_buff_if_t"></a> <a id="_CPPv214root_buff_if_t"></a> <a id="root_buff_if_t"></a> <a id="structroot__buff__if__t"></a> struct root\_buff\_if\_t

<a id="_CPPv418lescan_if_cb_ind_t"></a>

<a id="_CPPv318lescan_if_cb_ind_t"></a> <a id="_CPPv218lescan_if_cb_ind_t"></a> <a id="lescan_if_cb_ind_t"></a> <a id="structlescan__if__cb__ind__t"></a> struct lescan\_if\_cb\_ind\_t
:   LE scan indicate callback data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18lescan_if_cb_ind_t8ind_typeE"></a>

    <a id="_CPPv3N18lescan_if_cb_ind_t8ind_typeE"></a> <a id="_CPPv2N18lescan_if_cb_ind_t8ind_typeE"></a> <a id="lescan_if_cb_ind_t::ind_type__lescan_if_ind_t"></a> <a id="structlescan__if__cb__ind__t_1ad34887819ef8ba68386f21d527466a50"></a> [lescan\_if\_ind\_t](#_CPPv415lescan_if_ind_t "lescan_if_ind_t") ind\_type
    :   index of indicated

    <a id="_CPPv4N18lescan_if_cb_ind_t6statusE"></a>

    <a id="_CPPv3N18lescan_if_cb_ind_t6statusE"></a> <a id="_CPPv2N18lescan_if_cb_ind_t6statusE"></a> <a id="lescan_if_cb_ind_t::status__btif_ret_t"></a> <a id="structlescan__if__cb__ind__t_1a3c67c72d910c43cfdc82f47633507966"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") status
    :   status value

    <a id="_CPPv4N18lescan_if_cb_ind_t6p_dataE"></a>

    <a id="_CPPv3N18lescan_if_cb_ind_t6p_dataE"></a> <a id="_CPPv2N18lescan_if_cb_ind_t6p_dataE"></a> <a id="lescan_if_cb_ind_t::p_data__uint8_tP"></a> <a id="structlescan__if__cb__ind__t_1aca6d7e842cadb97b0765e93c81320846"></a> uint8\_t \*p\_data
    :   pointer indicated data

<a id="_CPPv424lescan_if_adv_rpt_head_t"></a>

<a id="_CPPv324lescan_if_adv_rpt_head_t"></a> <a id="_CPPv224lescan_if_adv_rpt_head_t"></a> <a id="lescan_if_adv_rpt_head_t"></a> <a id="structlescan__if__adv__rpt__head__t"></a> struct lescan\_if\_adv\_rpt\_head\_t
:   LE scan report header data struct definition.

<a id="_CPPv419lescan_if_adv_rpt_t"></a>

<a id="_CPPv319lescan_if_adv_rpt_t"></a> <a id="_CPPv219lescan_if_adv_rpt_t"></a> <a id="lescan_if_adv_rpt_t"></a> <a id="structlescan__if__adv__rpt__t"></a> struct lescan\_if\_adv\_rpt\_t
:   LE scan report data struct definition.

<a id="_CPPv416lescan_if_para_t"></a>

<a id="_CPPv316lescan_if_para_t"></a> <a id="_CPPv216lescan_if_para_t"></a> <a id="lescan_if_para_t"></a> <a id="structlescan__if__para__t"></a> struct lescan\_if\_para\_t
:   LE scan interface parameter struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N16lescan_if_para_t9scan_typeE"></a>

    <a id="_CPPv3N16lescan_if_para_t9scan_typeE"></a> <a id="_CPPv2N16lescan_if_para_t9scan_typeE"></a> <a id="lescan_if_para_t::scan_type__lescan_if_type_t"></a> <a id="structlescan__if__para__t_1a84f3b564ab981e4cfd4aa07abad9384f"></a> [lescan\_if\_type\_t](#_CPPv416lescan_if_type_t "lescan_if_type_t") scan\_type
    :   Passive scan or Active scan

    <a id="_CPPv4N16lescan_if_para_t9scan_intvE"></a>

    <a id="_CPPv3N16lescan_if_para_t9scan_intvE"></a> <a id="_CPPv2N16lescan_if_para_t9scan_intvE"></a> <a id="lescan_if_para_t::scan_intv__uint16_t"></a> <a id="structlescan__if__para__t_1a55e4fcccd9403e00c2c58325e34711e8"></a> uint16\_t scan\_intv
    :   Scan interval (N\* 0.625 ms)

    <a id="_CPPv4N16lescan_if_para_t8scan_winE"></a>

    <a id="_CPPv3N16lescan_if_para_t8scan_winE"></a> <a id="_CPPv2N16lescan_if_para_t8scan_winE"></a> <a id="lescan_if_para_t::scan_win__uint16_t"></a> <a id="structlescan__if__para__t_1a801475e7b4c0982b8261d1fb03249dee"></a> uint16\_t scan\_win
    :   Scan window (N\* 0.625 ms)

    <a id="_CPPv4N16lescan_if_para_t7scan_cbE"></a>

    <a id="_CPPv3N16lescan_if_para_t7scan_cbE"></a> <a id="_CPPv2N16lescan_if_para_t7scan_cbE"></a> <a id="lescan_if_para_t::scan_cb__lescan_if_callback_fp"></a> <a id="structlescan__if__para__t_1a34a8fd965c20cc204013f18e66e44569"></a> [lescan\_if\_callback\_fp](#_CPPv421lescan_if_callback_fp "lescan_if_callback_fp") scan\_cb
    :   Scan timeout (N\* 10 ms), Set zero to disable timeout

<a id="_CPPv426lescan_if_PA_sync_cb_ind_t"></a>

<a id="_CPPv326lescan_if_PA_sync_cb_ind_t"></a> <a id="_CPPv226lescan_if_PA_sync_cb_ind_t"></a> <a id="lescan_if_PA_sync_cb_ind_t"></a> <a id="structlescan__if__PA__sync__cb__ind__t"></a> struct lescan\_if\_PA\_sync\_cb\_ind\_t
:   LE SYNC indicate callback data struct definition.

<a id="_CPPv423lescan_if_pa_rpt_head_t"></a>

<a id="_CPPv323lescan_if_pa_rpt_head_t"></a> <a id="_CPPv223lescan_if_pa_rpt_head_t"></a> <a id="lescan_if_pa_rpt_head_t"></a> <a id="structlescan__if__pa__rpt__head__t"></a> struct lescan\_if\_pa\_rpt\_head\_t
:   LE scan PA report header data struct definition.

<a id="_CPPv418lescan_if_pa_rpt_t"></a>

<a id="_CPPv318lescan_if_pa_rpt_t"></a> <a id="_CPPv218lescan_if_pa_rpt_t"></a> <a id="lescan_if_pa_rpt_t"></a> <a id="structlescan__if__pa__rpt__t"></a> struct lescan\_if\_pa\_rpt\_t
:   LE scan PA report data struct definition.

<a id="_CPPv424lescan_if_PA_sync_para_t"></a>

<a id="_CPPv324lescan_if_PA_sync_para_t"></a> <a id="_CPPv224lescan_if_PA_sync_para_t"></a> <a id="lescan_if_PA_sync_para_t"></a> <a id="structlescan__if__PA__sync__para__t"></a> struct lescan\_if\_PA\_sync\_para\_t
:   LE scan PA sync interface parameter struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N24lescan_if_PA_sync_para_t7adv_sidE"></a>

    <a id="_CPPv3N24lescan_if_PA_sync_para_t7adv_sidE"></a> <a id="_CPPv2N24lescan_if_PA_sync_para_t7adv_sidE"></a> <a id="lescan_if_PA_sync_para_t::adv_sid__uint8_t"></a> <a id="structlescan__if__PA__sync__para__t_1aa77cc46530c642013b902edee4c55e0d"></a> uint8\_t adv\_sid
    :   advertising sid

    <a id="_CPPv4N24lescan_if_PA_sync_para_t7addressE"></a>

    <a id="_CPPv3N24lescan_if_PA_sync_para_t7addressE"></a> <a id="_CPPv2N24lescan_if_PA_sync_para_t7addressE"></a> <a id="lescan_if_PA_sync_para_t::address__btif_le_bd_addr_t"></a> <a id="structlescan__if__PA__sync__para__t_1a547812974b5194352f82d869169905a9"></a> [btif\_le\_bd\_addr\_t](btif_type.md#_CPPv417btif_le_bd_addr_t "btif_le_bd_addr_t") address
    :   advertiser address

<a id="_CPPv423lescan_if_biginfo_rpt_t"></a>

<a id="_CPPv323lescan_if_biginfo_rpt_t"></a> <a id="_CPPv223lescan_if_biginfo_rpt_t"></a> <a id="lescan_if_biginfo_rpt_t"></a> <a id="structlescan__if__biginfo__rpt__t"></a> struct lescan\_if\_biginfo\_rpt\_t
:   LE scan biginfo struct definition.

<a id="macros"></a>

### Macros

<a id="c.LESCAN_IF_IND_START"></a>

<a id="lescan__if_8h_1afdb7831abc5941ebd719f732a0b7f102"></a> LESCAN\_IF\_IND\_START

<a id="c.LESCAN_IF_IND_ENABLE"></a>

<a id="lescan__if_8h_1a33bcd585d0a2bbd90dc000a6a2122648"></a> LESCAN\_IF\_IND\_ENABLE

<a id="c.LESCAN_IF_IND_DISABLE"></a>

<a id="lescan__if_8h_1ad419c3072cb8c148d62fa99d7065c5c7"></a> LESCAN\_IF\_IND\_DISABLE

<a id="c.LESCAN_IF_IND_ADV_RPT"></a>

<a id="lescan__if_8h_1a16f09c770879a60490db7213c6b5de59"></a> LESCAN\_IF\_IND\_ADV\_RPT

<a id="c.LESCAN_IF_PASSIVE_SCAN"></a>

<a id="lescan__if_8h_1abe89a39376914e5ac6118e1fd4c148ea"></a> LESCAN\_IF\_PASSIVE\_SCAN

<a id="c.LESCAN_IF_ACTIVE_SCAN"></a>

<a id="lescan__if_8h_1acaad35b46badb5c3f4106cf5873d29b2"></a> LESCAN\_IF\_ACTIVE\_SCAN

<a id="c.LESCAN_IF_SYNC_IND_CREATE"></a>

<a id="lescan__if_8h_1a9c34f1d8f3aaa764896a7d6d690a825a"></a> LESCAN\_IF\_SYNC\_IND\_CREATE

<a id="c.LESCAN_IF_SYNC_IND_DISC"></a>

<a id="lescan__if_8h_1ad5eb03db1a7013c35dd46044671e2cfa"></a> LESCAN\_IF\_SYNC\_IND\_DISC

<a id="c.LESCAN_IF_SYNC_IND_CANL"></a>

<a id="lescan__if_8h_1adc7b2f60aaeadd89963823feb86b8b39"></a> LESCAN\_IF\_SYNC\_IND\_CANL

<a id="c.LESCAN_IF_SYNC_IND_EN_RPT"></a>

<a id="lescan__if_8h_1acf05c9ed97c86680dd3f7fb6480d9935"></a> LESCAN\_IF\_SYNC\_IND\_EN\_RPT

<a id="c.LESCAN_IF_SYNC_IND_DIS_RPT"></a>

<a id="lescan__if_8h_1a3ac8c2f5caee6e2fd435c78e39a2a294"></a> LESCAN\_IF\_SYNC\_IND\_DIS\_RPT

<a id="c.LESCAN_IF_SYNC_IND_PA_PRT"></a>

<a id="lescan__if_8h_1a7b4af088b3f868746d93c77483b0e6c6"></a> LESCAN\_IF\_SYNC\_IND\_PA\_PRT

<a id="c.LESCAN_IF_SYNC_IND_BIGINFO_RPT"></a>

<a id="lescan__if_8h_1a2762704eefac9e7d06f99b537ec6f733"></a> LESCAN\_IF\_SYNC\_IND\_BIGINFO\_RPT

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv415lescan_if_ind_t"></a>

<a id="_CPPv315lescan_if_ind_t"></a> <a id="_CPPv215lescan_if_ind_t"></a> <a id="lescan_if_ind_t"></a> <a id="lescan__if_8h_1aaf791bb229bb99c9a387527d5a2ca933"></a> typedef uint8\_t lescan\_if\_ind\_t

<a id="_CPPv416lescan_if_type_t"></a>

<a id="_CPPv316lescan_if_type_t"></a> <a id="_CPPv216lescan_if_type_t"></a> <a id="lescan_if_type_t"></a> <a id="lescan__if_8h_1a05d8969fba701500b54fcb64a8468b49"></a> typedef uint8\_t lescan\_if\_type\_t

<a id="_CPPv421lescan_if_callback_fp"></a>

<a id="_CPPv321lescan_if_callback_fp"></a> <a id="_CPPv221lescan_if_callback_fp"></a> <a id="lescan_if_callback_fp"></a> <a id="lescan__if_8h_1ad6b25bd3b9cd6c13e3415bb98cc5d4af"></a> typedef void (\*lescan\_if\_callback\_fp)([lescan\_if\_cb\_ind\_t](#_CPPv418lescan_if_cb_ind_t "lescan_if_cb_ind_t") \*p\_scan\_para)

<a id="_CPPv420lescan_if_sync_ind_t"></a>

<a id="_CPPv320lescan_if_sync_ind_t"></a> <a id="_CPPv220lescan_if_sync_ind_t"></a> <a id="lescan_if_sync_ind_t"></a> <a id="lescan__if_8h_1a761c0971a0d8f835be1193c73d1cb5d5"></a> typedef uint8\_t lescan\_if\_sync\_ind\_t

<a id="_CPPv429lescan_if_PA_sync_callback_fp"></a>

<a id="_CPPv329lescan_if_PA_sync_callback_fp"></a> <a id="_CPPv229lescan_if_PA_sync_callback_fp"></a> <a id="lescan_if_PA_sync_callback_fp"></a> <a id="lescan__if_8h_1a26c64d3f512f4f20853f237dc6ae4ff0"></a> typedef void (\*lescan\_if\_PA\_sync\_callback\_fp)([lescan\_if\_PA\_sync\_cb\_ind\_t](#_CPPv426lescan_if_PA_sync_cb_ind_t "lescan_if_PA_sync_cb_ind_t") \*ind)
