---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/tws/tws_profile_ctrl.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="tws-profile-control-functions"></a>

# TWS Profile Control Functions

<a id="tws-profile-ctrl-api-brief"></a>

## TWS\_PROFILE\_CTRL API Brief

| Application | Brief |
| --- | --- |
| [`tws_profile_is_reconnecting()`](#_CPPv427tws_profile_is_reconnectingP14btif_bd_addr_t "tws_profile_is_reconnecting") | check that tws profile is reconnecting |
| [`tws_profile_clear_reconnecting()`](#_CPPv430tws_profile_clear_reconnectingP14btif_bd_addr_t "tws_profile_clear_reconnecting") | clear tws profile reconnecting |
| [`tws_profile_connect()`](#_CPPv419tws_profile_connect14btif_bd_addr_t "tws_profile_connect") | connect mobile profile |
| [`tws_profile_sync()`](#_CPPv416tws_profile_syncP14btif_bd_addr_tb "tws_profile_sync") | sync profile |
| [`tws_profile_sync_cmd_handle()`](#_CPPv427tws_profile_sync_cmd_handlePK7uint8_t8uint16_t "tws_profile_sync_cmd_handle") | handle tws profile sync command |
| [`tws_sync_done_cmd_handle()`](#_CPPv424tws_sync_done_cmd_handlePK7uint8_t8uint16_t "tws_sync_done_cmd_handle") | handle tws sync done command |
| [`tws_profile_sync_single_profile()`](#_CPPv431tws_profile_sync_single_profileP14btif_bd_addr_tb14profile_type_t "tws_profile_sync_single_profile") | sync single profile |

<a id="tws-profile-ctrl-api-reference"></a>

## TWS\_PROFILE\_CTRL API Reference

<a id="header-file"></a>

### Header File

- [tws/tws\_ux/inc/tws\_profile\_ctrl.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/tws/tws_ux/inc/tws_profile_ctrl.h)

<a id="functions"></a>

### Functions

<a id="_CPPv427tws_profile_is_reconnectingP14btif_bd_addr_t"></a>

<a id="_CPPv327tws_profile_is_reconnectingP14btif_bd_addr_t"></a> <a id="_CPPv227tws_profile_is_reconnectingP14btif_bd_addr_t"></a> <a id="tws_profile_is_reconnecting__btif_bd_addr_tP"></a> <a id="tws__profile__ctrl_8h_1aadce54ce5579143a34dc6497392f8586"></a> bool tws\_profile\_is\_reconnecting([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   check that tws profile is reconnecting

    check if TWS APP’s reconnecting profile action is on going

    参数:
    :   **\*p\_addr** – **\[in\]** pointer to address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回值:
    :   - **true** – on going
        - **false** – no action

    返回:
    :   result

<a id="_CPPv430tws_profile_clear_reconnectingP14btif_bd_addr_t"></a>

<a id="_CPPv330tws_profile_clear_reconnectingP14btif_bd_addr_t"></a> <a id="_CPPv230tws_profile_clear_reconnectingP14btif_bd_addr_t"></a> <a id="tws_profile_clear_reconnecting__btif_bd_addr_tP"></a> <a id="tws__profile__ctrl_8h_1a3b3415e24ce7fe8cbafaa051bb20a48c"></a> void tws\_profile\_clear\_reconnecting([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   clear tws profile reconnecting

    Clear the reconnecting flag

    参数:
    :   **\*p\_addr** – **\[in\]** pointer to address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回:
    :   N/A

<a id="_CPPv419tws_profile_connect14btif_bd_addr_t"></a>

<a id="_CPPv319tws_profile_connect14btif_bd_addr_t"></a> <a id="_CPPv219tws_profile_connect14btif_bd_addr_t"></a> <a id="tws_profile_connect__btif_bd_addr_t"></a> <a id="tws__profile__ctrl_8h_1ac4e18b42c71ade2ea7e03651b32e4b56"></a> [btif\_ret\_t](../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") tws\_profile\_connect([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr)
:   connect mobile profile

    reconnect mobile profile trigger function

    参数:
    :   **addr** – **\[in\]** address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416tws_profile_syncP14btif_bd_addr_tb"></a>

<a id="_CPPv316tws_profile_syncP14btif_bd_addr_tb"></a> <a id="_CPPv216tws_profile_syncP14btif_bd_addr_tb"></a> <a id="tws_profile_sync__btif_bd_addr_tP.b"></a> <a id="tws__profile__ctrl_8h_1acc999fb58895a4c488792f91a1120c8d"></a> [btif\_ret\_t](../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") tws\_profile\_sync([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, bool force\_sync)
:   sync profile

    sync host stack with peer device

    参数:
    :   - **p\_addr** – **\[in\]** pointer to address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)
        - **force\_sync** – **\[in\]** force sync profile

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427tws_profile_sync_cmd_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv327tws_profile_sync_cmd_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv227tws_profile_sync_cmd_handlePK7uint8_t8uint16_t"></a> <a id="tws_profile_sync_cmd_handle__uint8_tCP.uint16_t"></a> <a id="tws__profile__ctrl_8h_1a438dd4a01e62185bac3b700712eb028f"></a> void tws\_profile\_sync\_cmd\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   handle tws profile sync command

    tws sync profile command handler

    参数:
    :   - **p\_data** – **\[in\]** pointer to profile sync command data
        - **length** – **\[in\]** length of profile sync command data

    返回:
    :   N/A

<a id="_CPPv424tws_sync_done_cmd_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv324tws_sync_done_cmd_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv224tws_sync_done_cmd_handlePK7uint8_t8uint16_t"></a> <a id="tws_sync_done_cmd_handle__uint8_tCP.uint16_t"></a> <a id="tws__profile__ctrl_8h_1a5ced8b38945fe44585fe2794a8a02883"></a> void tws\_sync\_done\_cmd\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   handle tws sync done command

    TWS slave used to notify TWS master that profile sync has been done

    参数:
    :   - **p\_data** – **\[in\]** pointer to profile sync done command data
        - **length** – **\[in\]** length of profile sync done command data

    返回:
    :   N/A

<a id="_CPPv431tws_profile_sync_single_profileP14btif_bd_addr_tb14profile_type_t"></a>

<a id="_CPPv331tws_profile_sync_single_profileP14btif_bd_addr_tb14profile_type_t"></a> <a id="_CPPv231tws_profile_sync_single_profileP14btif_bd_addr_tb14profile_type_t"></a> <a id="tws_profile_sync_single_profile__btif_bd_addr_tP.b.profile_type_t"></a> <a id="tws__profile__ctrl_8h_1aa45e5fc5c7233245895cbc7403ccb4eb"></a> [btif\_ret\_t](../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") tws\_profile\_sync\_single\_profile([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, bool ended, [profile\_type\_t](#_CPPv414profile_type_t "profile_type_t") profile\_type)
:   sync single profile

    only sync \[profile\_type\] profile for the mobile phone with address \[p\_addr\].

    参数:
    :   - **p\_addr** – **\[in\]** pointer to address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)
        - **ended** – **\[in\]** ended status of type bool
        - **profile\_type** – **\[in\]** profile type of type profile\_type\_t

    返回值:
    :   - **0** – success
        - **other** – fail **TWS\_PROFILE\_CTRL\_H** EOF

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv414profile_sync_t"></a>

<a id="_CPPv314profile_sync_t"></a> <a id="_CPPv214profile_sync_t"></a> <a id="profile_sync_t"></a> <a id="structprofile__sync__t"></a> struct profile\_sync\_t
:   profile sync structure definition.

<a id="_CPPv411sync_done_t"></a>

<a id="_CPPv311sync_done_t"></a> <a id="_CPPv211sync_done_t"></a> <a id="sync_done_t"></a> <a id="structsync__done__t"></a> struct sync\_done\_t
:   profile sync done structure definition.

<a id="macros"></a>

### Macros

<a id="c.PROFILE_SYNC_BASIC"></a>

<a id="tws__profile__ctrl_8h_1a332a0858f067c4f6386bd7abf8653f2d"></a> PROFILE\_SYNC\_BASIC

<a id="c.HCI_CONN_PROFILE"></a>

<a id="tws__profile__ctrl_8h_1a424f2a140b366fbf05d6ed2db983eeb0"></a> HCI\_CONN\_PROFILE

<a id="c.A2DP_PROFILE"></a>

<a id="tws__profile__ctrl_8h_1a5d9dd4435c2ac15ff94026d9fcb7df11"></a> A2DP\_PROFILE

<a id="c.HFP_HF_PROFILE"></a>

<a id="tws__profile__ctrl_8h_1a29888c68a1762d4da132d376131255d2"></a> HFP\_HF\_PROFILE

<a id="c.AVRCP_PROFILE"></a>

<a id="tws__profile__ctrl_8h_1ac0b71762e76b8e337eb3d11483a797ee"></a> AVRCP\_PROFILE

<a id="c.SPP_PROFILE"></a>

<a id="tws__profile__ctrl_8h_1a4284f3a655076e6b18d9bc2790518cb0"></a> SPP\_PROFILE

<a id="c.A2DP_PROFILE_ONLY"></a>

<a id="tws__profile__ctrl_8h_1a3cfd5be64296e4a59f1db61b0ebd5f08"></a> A2DP\_PROFILE\_ONLY

<a id="c.HFP_HF_PROFILE_ONLY"></a>

<a id="tws__profile__ctrl_8h_1a89e308b6b0b00877a0baa4f8d364f33e"></a> HFP\_HF\_PROFILE\_ONLY

<a id="c.AVRCP_PROFILE_ONLY"></a>

<a id="tws__profile__ctrl_8h_1a8698b5917cbb32976ebc5993d3e2f74a"></a> AVRCP\_PROFILE\_ONLY

<a id="c.SPP_PROFILE_ONLY"></a>

<a id="tws__profile__ctrl_8h_1aa0578dc9355c612f87c137ba38e0a965"></a> SPP\_PROFILE\_ONLY

<a id="c.INVALID_PROFILE"></a>

<a id="tws__profile__ctrl_8h_1aaee9a8e3d6f896c04f8f9295daf1634e"></a> INVALID\_PROFILE

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv414profile_type_t"></a>

<a id="_CPPv314profile_type_t"></a> <a id="_CPPv214profile_type_t"></a> <a id="profile_type_t"></a> <a id="tws__profile__ctrl_8h_1a30b8bb327464581fd8fcb5f9423fa8d9"></a> typedef uint8\_t profile\_type\_t
:   profile type definition.
