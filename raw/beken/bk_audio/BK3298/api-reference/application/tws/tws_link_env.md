---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/tws/tws_link_env.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="tws-link-environment-functions"></a>

# TWS Link Environment Functions

<a id="tws-link-env-api-brief"></a>

## TWS\_LINK\_ENV API Brief

| Application | Brief |
| --- | --- |
| [`tws_link_set_scan_type()`](#_CPPv422tws_link_set_scan_typev "tws_link_set_scan_type") | Set scan type |
| [`tws_link_env_init()`](#_CPPv417tws_link_env_initv "tws_link_env_init") | Initialize environment parameters |
| [`tws_link_enter_pairing()`](#_CPPv422tws_link_enter_pairingv "tws_link_enter_pairing") | Enter pairing mode |
| [`tws_link_set_connected()`](#_CPPv422tws_link_set_connectedb "tws_link_set_connected") | Set TWS connection status |
| [`tws_link_set_encrypted()`](#_CPPv422tws_link_set_encryptedb "tws_link_set_encrypted") | Set TWS encryption status |
| [`tws_link_get_encrypted()`](#_CPPv422tws_link_get_encryptedv "tws_link_get_encrypted") | Get TWS encryption status |
| [`tws_link_is_tws_connected()`](#_CPPv425tws_link_is_tws_connectedv "tws_link_is_tws_connected") | Check that TWS is connected |
| [`tws_link_get_tws_handle()`](#_CPPv423tws_link_get_tws_handlev "tws_link_get_tws_handle") | Get TWS connection handle |
| [`tws_link_set_tws_handle()`](#_CPPv423tws_link_set_tws_handle8uint16_t "tws_link_set_tws_handle") | Set TWS connection handle |
| [`tws_link_get_pairing_enabled()`](#_CPPv428tws_link_get_pairing_enabledv "tws_link_get_pairing_enabled") | Get TWS pairing enabled |
| [`tws_link_get_mobile_tws_role()`](#_CPPv428tws_link_get_mobile_tws_role14btif_bd_addr_t "tws_link_get_mobile_tws_role") | Get TWS role |
| [`tws_link_set_mobile_tws_role()`](#_CPPv428tws_link_set_mobile_tws_role14btif_bd_addr_t15btif_tws_role_t "tws_link_set_mobile_tws_role") | Set TWS role |
| [`tws_link_is_snoop_connected()`](#_CPPv427tws_link_is_snoop_connected14btif_bd_addr_t "tws_link_is_snoop_connected") | Check that snoop is connected |
| [`tws_set_mobile_sync_profile()`](#_CPPv427tws_set_mobile_sync_profile14btif_bd_addr_t23btif_sync_prof_status_t "tws_set_mobile_sync_profile") | Set sync profile status |
| [`tws_get_mobile_sync_profile()`](#_CPPv427tws_get_mobile_sync_profile14btif_bd_addr_t "tws_get_mobile_sync_profile") | Get sync profile status |
| [`tws_set_mobile_profile_state()`](#_CPPv428tws_set_mobile_profile_state8uint16_t21btif_profile_bitmap_t "tws_set_mobile_profile_state") | Set mobile profile status |
| [`tws_clear_mobile_profile_state()`](#_CPPv430tws_clear_mobile_profile_state8uint16_t21btif_profile_bitmap_t "tws_clear_mobile_profile_state") | Clear mobile profile status |
| [`tws_get_mobile_profile_state()`](#_CPPv428tws_get_mobile_profile_stateP14btif_bd_addr_t "tws_get_mobile_profile_state") | Get mobile profile set status |
| [`tws_get_mobile_authed()`](#_CPPv421tws_get_mobile_authed14btif_bd_addr_t "tws_get_mobile_authed") | Get mobile authorization status |
| [`tws_set_mobile_authed()`](#_CPPv421tws_set_mobile_authed14btif_bd_addr_tb "tws_set_mobile_authed") | Set mobile authorization status |
| [`tws_get_mobile_encryped()`](#_CPPv423tws_get_mobile_encryped14btif_bd_addr_t "tws_get_mobile_encryped") | Get mobile encryption status |
| [`tws_set_mobile_encryped()`](#_CPPv423tws_set_mobile_encryped14btif_bd_addr_tb "tws_set_mobile_encryped") | Set mobile encryption status |
| [`tws_is_mobile_env_existed()`](#_CPPv425tws_is_mobile_env_existed8uint16_t "tws_is_mobile_env_existed") | Check that mobile environment parameters is existed |
| [`tws_mobile_env_allocate()`](#_CPPv423tws_mobile_env_allocate14btif_bd_addr_t8uint16_t14btif_bt_role_t "tws_mobile_env_allocate") | Allocate mobile environment parameters |
| [`tws_mobile_env_free()`](#_CPPv419tws_mobile_env_free14btif_bd_addr_t8uint16_t "tws_mobile_env_free") | Free mobile environment parameters |
| [`tws_is_any_mobile_connected()`](#_CPPv427tws_is_any_mobile_connectedv "tws_is_any_mobile_connected") | Check that any mobile phones are connected |
| [`tws_is_mobile_idx_connected()`](#_CPPv427tws_is_mobile_idx_connected7uint8_t "tws_is_mobile_idx_connected") | Check that mobile is connected |
| [`tws_is_mobile_connected()`](#_CPPv423tws_is_mobile_connected14btif_bd_addr_t "tws_is_mobile_connected") | Check that mobile is connected |
| [`tws_set_mobile_bt_role()`](#_CPPv422tws_set_mobile_bt_role8uint16_t14btif_bt_role_t "tws_set_mobile_bt_role") | Set mobile BT role |
| [`tws_set_mobile_mode()`](#_CPPv419tws_set_mobile_mode8uint16_t14if_link_mode_t "tws_set_mobile_mode") | Set mobile link mode |
| [`tws_get_mobile_mode()`](#_CPPv419tws_get_mobile_mode8uint16_t "tws_get_mobile_mode") | Get mobile link mode |
| [`tws_is_mobile_tws_switch_allowed()`](#_CPPv432tws_is_mobile_tws_switch_allowed14btif_bd_addr_t "tws_is_mobile_tws_switch_allowed") | Check that TWS switch is allowed |
| [`tws_get_mobile_connected_count()`](#_CPPv430tws_get_mobile_connected_countv "tws_get_mobile_connected_count") | Get mobile connected count |
| [`tws_set_mobile_tws_switch_allowed()`](#_CPPv433tws_set_mobile_tws_switch_allowed14btif_bd_addr_tb "tws_set_mobile_tws_switch_allowed") | Set the TWS switch allowed statue |
| [`tws_delete_lk_handle()`](#_CPPv420tws_delete_lk_handlePK7uint8_t8uint16_t "tws_delete_lk_handle") | Handle delete link key command |
| [`tws_get_mobile_sync_handle()`](#_CPPv426tws_get_mobile_sync_handle14btif_bd_addr_t "tws_get_mobile_sync_handle") | Get mobile SCO sync connection handle |
| [`tws_set_mobile_sync_handle()`](#_CPPv426tws_set_mobile_sync_handle14btif_bd_addr_t8uint16_t "tws_set_mobile_sync_handle") | Set mobile SCO sync connection handle |
| [`tws_link_get_mobile_handle()`](#_CPPv426tws_link_get_mobile_handle14btif_bd_addr_t "tws_link_get_mobile_handle") | Get mobile ACL connection handle |
| [`tws_link_set_mobile_handle()`](#_CPPv426tws_link_set_mobile_handle14btif_bd_addr_t8uint16_t "tws_link_set_mobile_handle") | Set mobile ACL connection handle |
| [`tws_link_get_mobile_addr_by_handle()`](#_CPPv434tws_link_get_mobile_addr_by_handle8uint16_tP14btif_bd_addr_t "tws_link_get_mobile_addr_by_handle") | Get mobile address by ACL connection handle |
| [`tws_link_get_profile_sync_timer()`](#_CPPv431tws_link_get_profile_sync_timerP14btif_bd_addr_t "tws_link_get_profile_sync_timer") | Get profile sync timer |
| [`tws_link_mobile_set_audio_procy()`](#_CPPv431tws_link_mobile_set_audio_procyP14btif_bd_addr_t "tws_link_mobile_set_audio_procy") | Set audio proxy context |
| [`tws_link_mobile_get_audio_procy()`](#_CPPv431tws_link_mobile_get_audio_procyP14btif_bd_addr_t "tws_link_mobile_get_audio_procy") | Get audio proxy context |
| [`tws_link_mobile_get_profile_backup()`](#_CPPv434tws_link_mobile_get_profile_backupP14btif_bd_addr_t "tws_link_mobile_get_profile_backup") | Get profile state backup |
| [`tws_link_mobile_set_profile_backup()`](#_CPPv434tws_link_mobile_set_profile_backupP14btif_bd_addr_t21btif_profile_bitmap_t "tws_link_mobile_set_profile_backup") | Set profile state backup |
| [`tws_link_loss_connect_evt_handle()`](#_CPPv432tws_link_loss_connect_evt_handleP14btif_bd_addr_t7uint8_t "tws_link_loss_connect_evt_handle") | Handle loss connection event |
| [`tws_link_loss_discon_evt_handle()`](#_CPPv431tws_link_loss_discon_evt_handleP14btif_bd_addr_t "tws_link_loss_discon_evt_handle") | Handle loss disconnection event |
| [`tws_link_loss_reset_env()`](#_CPPv423tws_link_loss_reset_envv "tws_link_loss_reset_env") | Reset the reconnection environment parameters |
| [`tws_link_loss_get_reconn_addr()`](#_CPPv429tws_link_loss_get_reconn_addrPP14btif_bd_addr_t "tws_link_loss_get_reconn_addr") | get reconnect address when tws link is lose |
| [`tws_link_update_sch_info()`](#_CPPv424tws_link_update_sch_infov "tws_link_update_sch_info") | Update schedule information |
| [`tws_link_restore_sch_info()`](#_CPPv425tws_link_restore_sch_infov "tws_link_restore_sch_info") | Restore schedule information |
| [`tws_link_get_mobile_num()`](#_CPPv423tws_link_get_mobile_numv "tws_link_get_mobile_num") | Get link mobile number |
| [`tws_link_get_scan_type()`](#_CPPv422tws_link_get_scan_typev "tws_link_get_scan_type") | Get scan type |
| [`tws_link_battery_report()`](#_CPPv423tws_link_battery_report7uint8_t "tws_link_battery_report") | Report battery level |
| [`tws_link_force_sync_profile()`](#_CPPv427tws_link_force_sync_profilev "tws_link_force_sync_profile") | Force sync profile |

<a id="tws-link-env-api-reference"></a>

## TWS\_LINK\_ENV API Reference

<a id="header-file"></a>

### Header File

- [tws/tws\_ux/inc/tws\_link\_env.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/tws/tws_ux/inc/tws_link_env.h)

<a id="functions"></a>

### Functions

<a id="_CPPv422tws_link_set_scan_typev"></a>

<a id="_CPPv322tws_link_set_scan_typev"></a> <a id="_CPPv222tws_link_set_scan_typev"></a> <a id="tws_link_set_scan_type__void"></a> <a id="tws__link__env_8h_1af2ea0a64daf59bd27a1c99e24dcc3039"></a> void tws\_link\_set\_scan\_type(void)
:   Set scan type.

    Set the scan type based on the TWS link environment parameters.

    返回:
    :   N/A

<a id="_CPPv417tws_link_env_initv"></a>

<a id="_CPPv317tws_link_env_initv"></a> <a id="_CPPv217tws_link_env_initv"></a> <a id="tws_link_env_init__void"></a> <a id="tws__link__env_8h_1af82c8cc44cfb4af54b87f7643d88f4ed"></a> void tws\_link\_env\_init(void)
:   Initialize environment parameters.

    Initialize TWS and mobile environment parameters.

    返回:
    :   N/A

<a id="_CPPv422tws_link_enter_pairingv"></a>

<a id="_CPPv322tws_link_enter_pairingv"></a> <a id="_CPPv222tws_link_enter_pairingv"></a> <a id="tws_link_enter_pairing__void"></a> <a id="tws__link__env_8h_1a14923214064821d5a04dc08edcfc08a3"></a> void tws\_link\_enter\_pairing(void)
:   Enter pairing mode.

    Enter pairing mode and enable pairing timeout timer.

    返回:
    :   N/A

<a id="_CPPv422tws_link_set_connectedb"></a>

<a id="_CPPv322tws_link_set_connectedb"></a> <a id="_CPPv222tws_link_set_connectedb"></a> <a id="tws_link_set_connected__b"></a> <a id="tws__link__env_8h_1a65b9e2728a4b2a3c0f2f34f76aa4f5b2"></a> void tws\_link\_set\_connected(bool connected)
:   Set TWS connection status.

    Set the connection status in the TWS environment parameters.

    参数:
    :   **connected** – **\[in\]** TWS connection status. true is connected, false is not connected.

    返回:
    :   N/A

<a id="_CPPv422tws_link_set_encryptedb"></a>

<a id="_CPPv322tws_link_set_encryptedb"></a> <a id="_CPPv222tws_link_set_encryptedb"></a> <a id="tws_link_set_encrypted__b"></a> <a id="tws__link__env_8h_1aa893a492fd179881428e29182bef089c"></a> void tws\_link\_set\_encrypted(bool encrypted)
:   Set TWS encryption status.

    Set the encryption status in the TWS environment parameters.

    参数:
    :   **connected** – **\[in\]** TWS encryption status. true is encrypted, false is unencrypted.

    返回:
    :   N/A

<a id="_CPPv422tws_link_get_encryptedv"></a>

<a id="_CPPv322tws_link_get_encryptedv"></a> <a id="_CPPv222tws_link_get_encryptedv"></a> <a id="tws_link_get_encrypted__void"></a> <a id="tws__link__env_8h_1a17ca96be1463625615c1a6855f33c11b"></a> bool tws\_link\_get\_encrypted(void)
:   Get TWS encryption status.

    Get the encryption status in the TWS environment parameters.

    返回值:
    :   - **true** – encrypted
        - **false** – unencrypted

    返回:
    :   TWS encryption status

<a id="_CPPv425tws_link_is_tws_connectedv"></a>

<a id="_CPPv325tws_link_is_tws_connectedv"></a> <a id="_CPPv225tws_link_is_tws_connectedv"></a> <a id="tws_link_is_tws_connected__void"></a> <a id="tws__link__env_8h_1a4791dcec5810b0c901711cbb50a88e6e"></a> bool tws\_link\_is\_tws\_connected(void)
:   Check that TWS is connected.

    Check that TWS is connected in the TWS environment parameter.

    返回值:
    :   - **true** – connected
        - **false** – not connected

    返回:
    :   TWS connection status

<a id="_CPPv423tws_link_get_tws_handlev"></a>

<a id="_CPPv323tws_link_get_tws_handlev"></a> <a id="_CPPv223tws_link_get_tws_handlev"></a> <a id="tws_link_get_tws_handle__void"></a> <a id="tws__link__env_8h_1a06ed03f11d9afaa6f50109009ece0a1a"></a> uint16\_t tws\_link\_get\_tws\_handle(void)
:   Get TWS connection handle.

    Get TWS connection handle in the TWS environment parameter.

    返回:
    :   connection handle

<a id="_CPPv423tws_link_set_tws_handle8uint16_t"></a>

<a id="_CPPv323tws_link_set_tws_handle8uint16_t"></a> <a id="_CPPv223tws_link_set_tws_handle8uint16_t"></a> <a id="tws_link_set_tws_handle__uint16_t"></a> <a id="tws__link__env_8h_1a0707b72851a3c243612a37c1032de81b"></a> void tws\_link\_set\_tws\_handle(uint16\_t handle)
:   Set TWS connection handle.

    Set TWS connection handle in the TWS environment parameter.

    参数:
    :   **handle** – **\[in\]** connection handle

    返回:
    :   N/A

<a id="_CPPv428tws_link_get_pairing_enabledv"></a>

<a id="_CPPv328tws_link_get_pairing_enabledv"></a> <a id="_CPPv228tws_link_get_pairing_enabledv"></a> <a id="tws_link_get_pairing_enabled__void"></a> <a id="tws__link__env_8h_1aaee8aeb651d838971c25daac2e680850"></a> bool tws\_link\_get\_pairing\_enabled(void)
:   Get TWS pairing enabled.

    Get TWS pairing enabled in the TWS environment parameter.

    返回值:
    :   - **true** – enabled
        - **false** – disabled

    返回:
    :   TWS pairing enabled

<a id="_CPPv428tws_link_get_mobile_tws_role14btif_bd_addr_t"></a>

<a id="_CPPv328tws_link_get_mobile_tws_role14btif_bd_addr_t"></a> <a id="_CPPv228tws_link_get_mobile_tws_role14btif_bd_addr_t"></a> <a id="tws_link_get_mobile_tws_role__btif_bd_addr_t"></a> <a id="tws__link__env_8h_1a10a5ada428d1947dd9f60b68c1891124"></a> [btif\_tws\_role\_t](../../btif/btif_type.md#_CPPv415btif_tws_role_t "btif_tws_role_t") tws\_link\_get\_mobile\_tws\_role([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr)
:   Get TWS role.

    Get the TWS role for connected to the mobile phone with address \[addr\].

    参数:
    :   **addr** – **\[in\]** mobile phone address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回值:
    :   - **0** – unknown \[BTIF\_TWS\_ROLE\_UNKNOWN\]
        - **1** – master \[BTIF\_TWS\_ROLE\_MASTER\]
        - **2** – slave \[BTIF\_TWS\_ROLE\_SLAVE\]

    返回:
    :   TWS role

<a id="_CPPv428tws_link_set_mobile_tws_role14btif_bd_addr_t15btif_tws_role_t"></a>

<a id="_CPPv328tws_link_set_mobile_tws_role14btif_bd_addr_t15btif_tws_role_t"></a> <a id="_CPPv228tws_link_set_mobile_tws_role14btif_bd_addr_t15btif_tws_role_t"></a> <a id="tws_link_set_mobile_tws_role__btif_bd_addr_t.btif_tws_role_t"></a> <a id="tws__link__env_8h_1a4df5f351826b4fb4bff98bd1f44831ea"></a> [btif\_ret\_t](../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") tws\_link\_set\_mobile\_tws\_role([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr, [btif\_tws\_role\_t](../../btif/btif_type.md#_CPPv415btif_tws_role_t "btif_tws_role_t") role)
:   Set TWS role.

    Set the TWS role for connected to the mobile phone with address \[addr\].

    参数:
    :   - **addr** – **\[in\]** mobile phone address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)
        - **role** – **\[in\]** TWS role 0 unknown \[BTIF\_TWS\_ROLE\_UNKNOWN\] 1 master \[BTIF\_TWS\_ROLE\_MASTER\] 2 slave \[BTIF\_TWS\_ROLE\_SLAVE\]

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427tws_link_is_snoop_connected14btif_bd_addr_t"></a>

<a id="_CPPv327tws_link_is_snoop_connected14btif_bd_addr_t"></a> <a id="_CPPv227tws_link_is_snoop_connected14btif_bd_addr_t"></a> <a id="tws_link_is_snoop_connected__btif_bd_addr_t"></a> <a id="tws__link__env_8h_1aa9d8ae0c2992066a6bdcb34ac27ed8a9"></a> bool tws\_link\_is\_snoop\_connected([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr)
:   Check that snoop is connected.

    Check that snoop is connected to the mobile phone with address \[addr\].

    参数:
    :   **addr** – **\[in\]** mobile phone address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回值:
    :   - **true** – snoop is connected
        - **false** – snoop is not connected

    返回:
    :   check results

<a id="_CPPv427tws_set_mobile_sync_profile14btif_bd_addr_t23btif_sync_prof_status_t"></a>

<a id="_CPPv327tws_set_mobile_sync_profile14btif_bd_addr_t23btif_sync_prof_status_t"></a> <a id="_CPPv227tws_set_mobile_sync_profile14btif_bd_addr_t23btif_sync_prof_status_t"></a> <a id="tws_set_mobile_sync_profile__btif_bd_addr_t.btif_sync_prof_status_t"></a> <a id="tws__link__env_8h_1a69056036d863cfb7bfdc6a07dd9a838d"></a> [btif\_ret\_t](../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") tws\_set\_mobile\_sync\_profile([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr, [btif\_sync\_prof\_status\_t](../../btif/btif_type.md#_CPPv423btif_sync_prof_status_t "btif_sync_prof_status_t") sync\_status)
:   Set sync profile status.

    Set the sync profile status for the mobile phone with address \[addr\].

    参数:
    :   - **addr** – **\[in\]** mobile phone address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)
        - **sync\_status** – **\[in\]** sync profile status. see@btif\_sync\_prof\_status\_t

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427tws_get_mobile_sync_profile14btif_bd_addr_t"></a>

<a id="_CPPv327tws_get_mobile_sync_profile14btif_bd_addr_t"></a> <a id="_CPPv227tws_get_mobile_sync_profile14btif_bd_addr_t"></a> <a id="tws_get_mobile_sync_profile__btif_bd_addr_t"></a> <a id="tws__link__env_8h_1a8a3b14b810524f381ff4b72d4e60e32d"></a> [btif\_sync\_prof\_status\_t](../../btif/btif_type.md#_CPPv423btif_sync_prof_status_t "btif_sync_prof_status_t") tws\_get\_mobile\_sync\_profile([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr)
:   Get sync profile status.

    Get the sync profile status for the mobile phone with address \[addr\].

    参数:
    :   **addr** – **\[in\]** mobile phone address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回值:
    :   - **2** – sync done
        - **1** – sync profile ongoing
        - **1** – sync isn’t done

    返回:
    :   sync profile status

<a id="_CPPv428tws_set_mobile_profile_state8uint16_t21btif_profile_bitmap_t"></a>

<a id="_CPPv328tws_set_mobile_profile_state8uint16_t21btif_profile_bitmap_t"></a> <a id="_CPPv228tws_set_mobile_profile_state8uint16_t21btif_profile_bitmap_t"></a> <a id="tws_set_mobile_profile_state__uint16_t.btif_profile_bitmap_t"></a> <a id="tws__link__env_8h_1ac69c470e42662ffe1a6b8737eb256c55"></a> [btif\_ret\_t](../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") tws\_set\_mobile\_profile\_state(uint16\_t handle, [btif\_profile\_bitmap\_t](../../btif/btif_type.md#_CPPv421btif_profile_bitmap_t "btif_profile_bitmap_t") profile\_state)
:   Set mobile profile status.

    Set the profile status for the mobile phone with handle \[handle\].

    参数:
    :   - **handle** – **\[in\]** connection handle
        - **profile\_state** – **\[in\]** profile state of type btif\_profile\_bitmap\_t to set.

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv430tws_clear_mobile_profile_state8uint16_t21btif_profile_bitmap_t"></a>

<a id="_CPPv330tws_clear_mobile_profile_state8uint16_t21btif_profile_bitmap_t"></a> <a id="_CPPv230tws_clear_mobile_profile_state8uint16_t21btif_profile_bitmap_t"></a> <a id="tws_clear_mobile_profile_state__uint16_t.btif_profile_bitmap_t"></a> <a id="tws__link__env_8h_1ade75a6ace1bde15c81c1af3d3b13646d"></a> [btif\_ret\_t](../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") tws\_clear\_mobile\_profile\_state(uint16\_t handle, [btif\_profile\_bitmap\_t](../../btif/btif_type.md#_CPPv421btif_profile_bitmap_t "btif_profile_bitmap_t") profile\_state)
:   Clear mobile profile status.

    Clear the profile status for the mobile phone with handle \[handle\].

    参数:
    :   - **handle** – **\[in\]** connection handle
        - **profile\_state** – **\[in\]** profile state of type btif\_profile\_bitmap\_t to clear.

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv428tws_get_mobile_profile_stateP14btif_bd_addr_t"></a>

<a id="_CPPv328tws_get_mobile_profile_stateP14btif_bd_addr_t"></a> <a id="_CPPv228tws_get_mobile_profile_stateP14btif_bd_addr_t"></a> <a id="tws_get_mobile_profile_state__btif_bd_addr_tP"></a> <a id="tws__link__env_8h_1aa479b460354b5d5a572df0e5fe1a74aa"></a> [btif\_profile\_bitmap\_t](../../btif/btif_type.md#_CPPv421btif_profile_bitmap_t "btif_profile_bitmap_t") tws\_get\_mobile\_profile\_state([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   Get mobile profile set status.

    Get the profile set status for the mobile phone with address \[addr\].

    参数:
    :   **p\_addr** – **\[in\]** pointer to an address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回:
    :   profile status of type btif\_profile\_bitmap\_t.

<a id="_CPPv421tws_get_mobile_authed14btif_bd_addr_t"></a>

<a id="_CPPv321tws_get_mobile_authed14btif_bd_addr_t"></a> <a id="_CPPv221tws_get_mobile_authed14btif_bd_addr_t"></a> <a id="tws_get_mobile_authed__btif_bd_addr_t"></a> <a id="tws__link__env_8h_1a5c62da4e086b8921f15993ff5cf93f91"></a> bool tws\_get\_mobile\_authed([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr)
:   Get mobile authorization status.

    Get the authorization status for the mobile phone with address \[addr\].

    参数:
    :   **addr** – **\[in\]** mobile phone address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回值:
    :   - **true** – authorized
        - **false** – unauthorized

    返回:
    :   authorization status

<a id="_CPPv421tws_set_mobile_authed14btif_bd_addr_tb"></a>

<a id="_CPPv321tws_set_mobile_authed14btif_bd_addr_tb"></a> <a id="_CPPv221tws_set_mobile_authed14btif_bd_addr_tb"></a> <a id="tws_set_mobile_authed__btif_bd_addr_t.b"></a> <a id="tws__link__env_8h_1adf83a4d19bffdca48c4853cf5b5d4ee6"></a> [btif\_ret\_t](../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") tws\_set\_mobile\_authed([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr, bool authed)
:   Set mobile authorization status.

    Set the authorization status for the mobile phone with address \[addr\].

    参数:
    :   - **addr** – **\[in\]** mobile phone address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)
        - **authed** – **\[in\]** authorization status. true is authorized, false is unauthorized.

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv423tws_get_mobile_encryped14btif_bd_addr_t"></a>

<a id="_CPPv323tws_get_mobile_encryped14btif_bd_addr_t"></a> <a id="_CPPv223tws_get_mobile_encryped14btif_bd_addr_t"></a> <a id="tws_get_mobile_encryped__btif_bd_addr_t"></a> <a id="tws__link__env_8h_1a056e60603caf3c01602823ac9892edd7"></a> bool tws\_get\_mobile\_encryped([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr)
:   Get mobile encryption status.

    Get the encryption status for the mobile phone with address \[addr\].

    参数:
    :   **addr** – **\[in\]** mobile phone address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回值:
    :   - **true** – encrypted
        - **false** – not encrypted

    返回:
    :   encryption status

<a id="_CPPv423tws_set_mobile_encryped14btif_bd_addr_tb"></a>

<a id="_CPPv323tws_set_mobile_encryped14btif_bd_addr_tb"></a> <a id="_CPPv223tws_set_mobile_encryped14btif_bd_addr_tb"></a> <a id="tws_set_mobile_encryped__btif_bd_addr_t.b"></a> <a id="tws__link__env_8h_1a045e03af50d7ea45b05f508b65ec7d3f"></a> [btif\_ret\_t](../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") tws\_set\_mobile\_encryped([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr, bool encrypted)
:   Set mobile encryption status.

    Set the encryption status for the mobile phone with address \[addr\].

    参数:
    :   - **addr** – **\[in\]** mobile phone address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)
        - **encrypted** – **\[in\]** encryption status. true is encrypted, false is not encrypted.

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425tws_is_mobile_env_existed8uint16_t"></a>

<a id="_CPPv325tws_is_mobile_env_existed8uint16_t"></a> <a id="_CPPv225tws_is_mobile_env_existed8uint16_t"></a> <a id="tws_is_mobile_env_existed__uint16_t"></a> <a id="tws__link__env_8h_1aaba3ff4bdc270e759fcb85515d723779"></a> bool tws\_is\_mobile\_env\_existed(uint16\_t handle)
:   Check that mobile environment parameters is existed.

    Check that the environment parameters for the mobile phone with handle \[handle\] is existed.

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **true** – existed
        - **false** – not existed

    返回:
    :   check results

<a id="_CPPv423tws_mobile_env_allocate14btif_bd_addr_t8uint16_t14btif_bt_role_t"></a>

<a id="_CPPv323tws_mobile_env_allocate14btif_bd_addr_t8uint16_t14btif_bt_role_t"></a> <a id="_CPPv223tws_mobile_env_allocate14btif_bd_addr_t8uint16_t14btif_bt_role_t"></a> <a id="tws_mobile_env_allocate__btif_bd_addr_t.uint16_t.btif_bt_role_t"></a> <a id="tws__link__env_8h_1a78d926d193f6b6b9e2419059a94bdb27"></a> [btif\_ret\_t](../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") tws\_mobile\_env\_allocate([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr, uint16\_t handle, [btif\_bt\_role\_t](../../btif/btif_type.md#_CPPv414btif_bt_role_t "btif_bt_role_t") bt\_role)
:   Allocate mobile environment parameters.

    Allocate the environment parameters for the mobile phone with address \[addr\].

    参数:
    :   - **addr** – **\[in\]** mobile phone address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)
        - **handle** – **\[in\]** connection handle
        - **bt\_role** – **\[in\]** TWS role of type btif\_bt\_role\_t

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419tws_mobile_env_free14btif_bd_addr_t8uint16_t"></a>

<a id="_CPPv319tws_mobile_env_free14btif_bd_addr_t8uint16_t"></a> <a id="_CPPv219tws_mobile_env_free14btif_bd_addr_t8uint16_t"></a> <a id="tws_mobile_env_free__btif_bd_addr_t.uint16_t"></a> <a id="tws__link__env_8h_1a83c497fb2e7bc93cea0a98b235df5990"></a> [btif\_ret\_t](../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") tws\_mobile\_env\_free([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr, uint16\_t handle)
:   Free mobile environment parameters.

    Free the environment parameters for the mobile phone with address \[addr\].

    参数:
    :   - **addr** – **\[in\]** mobile phone address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)
        - **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427tws_is_any_mobile_connectedv"></a>

<a id="_CPPv327tws_is_any_mobile_connectedv"></a> <a id="_CPPv227tws_is_any_mobile_connectedv"></a> <a id="tws_is_any_mobile_connected__void"></a> <a id="tws__link__env_8h_1a34d2de7125f48858dad9ea582c4b3c49"></a> bool tws\_is\_any\_mobile\_connected(void)
:   Check that any mobile phones are connected.

    Check that any mobile phones are connected.

    返回值:
    :   - **true** – connection exists
        - **false** – no connection

    返回:
    :   check results

<a id="_CPPv427tws_is_mobile_idx_connected7uint8_t"></a>

<a id="_CPPv327tws_is_mobile_idx_connected7uint8_t"></a> <a id="_CPPv227tws_is_mobile_idx_connected7uint8_t"></a> <a id="tws_is_mobile_idx_connected__uint8_t"></a> <a id="tws__link__env_8h_1a179e8d3d8fd973a17fd7a1298d3dfb1a"></a> [btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*tws\_is\_mobile\_idx\_connected(uint8\_t idx)
:   Check that mobile is connected.

    Check that the index \[idx\] mobile phone is connected.

    参数:
    :   **idx** – **\[in\]** index of mobile phone

    返回:
    :   mobile phone address pointer of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

<a id="_CPPv423tws_is_mobile_connected14btif_bd_addr_t"></a>

<a id="_CPPv323tws_is_mobile_connected14btif_bd_addr_t"></a> <a id="_CPPv223tws_is_mobile_connected14btif_bd_addr_t"></a> <a id="tws_is_mobile_connected__btif_bd_addr_t"></a> <a id="tws__link__env_8h_1a14a601145fbdba3aa14694b0d9e1e388"></a> bool tws\_is\_mobile\_connected([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr)
:   Check that mobile is connected.

    Check that the mobile phone with address \[addr\] is connected.

    参数:
    :   **addr** – **\[in\]** mobile phone address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回值:
    :   - **true** – connected
        - **false** – no connected

    返回:
    :   check results

<a id="_CPPv422tws_set_mobile_bt_role8uint16_t14btif_bt_role_t"></a>

<a id="_CPPv322tws_set_mobile_bt_role8uint16_t14btif_bt_role_t"></a> <a id="_CPPv222tws_set_mobile_bt_role8uint16_t14btif_bt_role_t"></a> <a id="tws_set_mobile_bt_role__uint16_t.btif_bt_role_t"></a> <a id="tws__link__env_8h_1a5f9aaabe839c7c80cbcac6bc144e38fb"></a> [btif\_ret\_t](../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") tws\_set\_mobile\_bt\_role(uint16\_t handle, [btif\_bt\_role\_t](../../btif/btif_type.md#_CPPv414btif_bt_role_t "btif_bt_role_t") bt\_role)
:   Set mobile BT role.

    Set BT role for the mobile phone with handle \[handle\].

    参数:
    :   - **handle** – **\[in\]** connection handle
        - **bt\_role** – **\[in\]** BT role of type btif\_bt\_role\_t

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419tws_set_mobile_mode8uint16_t14if_link_mode_t"></a>

<a id="_CPPv319tws_set_mobile_mode8uint16_t14if_link_mode_t"></a> <a id="_CPPv219tws_set_mobile_mode8uint16_t14if_link_mode_t"></a> <a id="tws_set_mobile_mode__uint16_t.if_link_mode_t"></a> <a id="tws__link__env_8h_1a7ba23a3ac63d8927e13dd5e6f9832c81"></a> [btif\_ret\_t](../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") tws\_set\_mobile\_mode(uint16\_t handle, [if\_link\_mode\_t](../../btif/hci_if.md#_CPPv414if_link_mode_t "if_link_mode_t") mode)
:   Set mobile link mode.

    Set link mode for the mobile phone with handle \[handle\].

    参数:
    :   - **handle** – **\[in\]** connection handle
        - **mode** – **\[in\]** link mode of type if\_link\_mode\_t

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419tws_get_mobile_mode8uint16_t"></a>

<a id="_CPPv319tws_get_mobile_mode8uint16_t"></a> <a id="_CPPv219tws_get_mobile_mode8uint16_t"></a> <a id="tws_get_mobile_mode__uint16_t"></a> <a id="tws__link__env_8h_1a458d20cbbcd7e24f1c7497f533c4449b"></a> uint8\_t tws\_get\_mobile\_mode(uint16\_t handle)
:   Get mobile link mode.

    Get link mode for the mobile phone with handle \[handle\].

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – active mode \[IF\_ACTIVE\]
        - **1** – hold mode \[IF\_HOLD\]
        - **2** – sniff mode \[IF\_SNIFF\]
        - **3** – error mode \[IF\_ERROR\_MODE\]

    返回:
    :   link mode of type if\_link\_mode\_t

<a id="_CPPv432tws_is_mobile_tws_switch_allowed14btif_bd_addr_t"></a>

<a id="_CPPv332tws_is_mobile_tws_switch_allowed14btif_bd_addr_t"></a> <a id="_CPPv232tws_is_mobile_tws_switch_allowed14btif_bd_addr_t"></a> <a id="tws_is_mobile_tws_switch_allowed__btif_bd_addr_t"></a> <a id="tws__link__env_8h_1a96995af0dc61ab9c8301080c4512c572"></a> bool tws\_is\_mobile\_tws\_switch\_allowed([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr)
:   Check that TWS switch is allowed.

    Check that TWS switch is allowed for the mobile phone with address \[addr\].

    参数:
    :   **addr** – **\[in\]** mobile phone address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回值:
    :   - **true** – allowed
        - **false** – not allowed

    返回:
    :   check results

<a id="_CPPv430tws_get_mobile_connected_countv"></a>

<a id="_CPPv330tws_get_mobile_connected_countv"></a> <a id="_CPPv230tws_get_mobile_connected_countv"></a> <a id="tws_get_mobile_connected_count__void"></a> <a id="tws__link__env_8h_1a58414cb8593e3ed6b9addae4ba1174d8"></a> uint8\_t tws\_get\_mobile\_connected\_count(void)
:   Get mobile connected count.

    Get the number of connected mobile phones.

    返回:
    :   number of connected mobile phones.

<a id="_CPPv433tws_set_mobile_tws_switch_allowed14btif_bd_addr_tb"></a>

<a id="_CPPv333tws_set_mobile_tws_switch_allowed14btif_bd_addr_tb"></a> <a id="_CPPv233tws_set_mobile_tws_switch_allowed14btif_bd_addr_tb"></a> <a id="tws_set_mobile_tws_switch_allowed__btif_bd_addr_t.b"></a> <a id="tws__link__env_8h_1ac19a059ad6bfb5f3a03094b6c5cdb672"></a> [btif\_ret\_t](../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") tws\_set\_mobile\_tws\_switch\_allowed([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr, bool allowed)
:   Set the TWS switch allowed statue.

    Set the TWS switch allowed statue for the mobile phone with address \[addr\].

    参数:
    :   - **addr** – **\[in\]** mobile phone address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)
        - **allowed** – **\[in\]** allowed statue

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420tws_delete_lk_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv320tws_delete_lk_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv220tws_delete_lk_handlePK7uint8_t8uint16_t"></a> <a id="tws_delete_lk_handle__uint8_tCP.uint16_t"></a> <a id="tws__link__env_8h_1af3b1da25b8c86fcc7a2a6eb3e9f56608"></a> void tws\_delete\_lk\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   Handle delete link key command.

    Handle the delete link key command in TWS private commands

    参数:
    :   - **p\_data** – **\[in\]** pointer to the delete link key command data
        - **length** – **\[in\]** length of the delete link key command data

    返回:
    :   N/A

<a id="_CPPv426tws_get_mobile_sync_handle14btif_bd_addr_t"></a>

<a id="_CPPv326tws_get_mobile_sync_handle14btif_bd_addr_t"></a> <a id="_CPPv226tws_get_mobile_sync_handle14btif_bd_addr_t"></a> <a id="tws_get_mobile_sync_handle__btif_bd_addr_t"></a> <a id="tws__link__env_8h_1a0c6a54bc6c04dd72a913a6f304da8ba0"></a> uint16\_t tws\_get\_mobile\_sync\_handle([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr)
:   Get mobile SCO sync connection handle.

    Get the SCO sync connection handle for the mobile phone with address \[addr\].

    参数:
    :   **addr** – **\[in\]** mobile phone address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回:
    :   SCO sync connection handle

<a id="_CPPv426tws_set_mobile_sync_handle14btif_bd_addr_t8uint16_t"></a>

<a id="_CPPv326tws_set_mobile_sync_handle14btif_bd_addr_t8uint16_t"></a> <a id="_CPPv226tws_set_mobile_sync_handle14btif_bd_addr_t8uint16_t"></a> <a id="tws_set_mobile_sync_handle__btif_bd_addr_t.uint16_t"></a> <a id="tws__link__env_8h_1af86498e8458ed103fe56a413d78b9f79"></a> [btif\_ret\_t](../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") tws\_set\_mobile\_sync\_handle([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr, uint16\_t handle)
:   Set mobile SCO sync connection handle.

    Set the SCO sync connection handle for the mobile phone with address \[addr\].

    参数:
    :   - **addr** – **\[in\]** mobile phone address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)
        - **handle** – **\[in\]** SCO sync connection handle

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426tws_link_get_mobile_handle14btif_bd_addr_t"></a>

<a id="_CPPv326tws_link_get_mobile_handle14btif_bd_addr_t"></a> <a id="_CPPv226tws_link_get_mobile_handle14btif_bd_addr_t"></a> <a id="tws_link_get_mobile_handle__btif_bd_addr_t"></a> <a id="tws__link__env_8h_1a152986e0a25e76390c317d0118b58abe"></a> uint16\_t tws\_link\_get\_mobile\_handle([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr)
:   Get mobile ACL connection handle.

    Get the ACL connection handle for the mobile phone with address \[addr\].

    参数:
    :   **addr** – **\[in\]** mobile phone address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回:
    :   ACL connection handle

<a id="_CPPv426tws_link_set_mobile_handle14btif_bd_addr_t8uint16_t"></a>

<a id="_CPPv326tws_link_set_mobile_handle14btif_bd_addr_t8uint16_t"></a> <a id="_CPPv226tws_link_set_mobile_handle14btif_bd_addr_t8uint16_t"></a> <a id="tws_link_set_mobile_handle__btif_bd_addr_t.uint16_t"></a> <a id="tws__link__env_8h_1aea49bbbcf92d80cf488e967184aee257"></a> [btif\_ret\_t](../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") tws\_link\_set\_mobile\_handle([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr, uint16\_t handle)
:   Set mobile ACL connection handle.

    Set the ACL connection handle for the mobile phone with address \[addr\].

    参数:
    :   - **addr** – **\[in\]** mobile phone address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)
        - **handle** – **\[in\]** ACL connection handle

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv434tws_link_get_mobile_addr_by_handle8uint16_tP14btif_bd_addr_t"></a>

<a id="_CPPv334tws_link_get_mobile_addr_by_handle8uint16_tP14btif_bd_addr_t"></a> <a id="_CPPv234tws_link_get_mobile_addr_by_handle8uint16_tP14btif_bd_addr_t"></a> <a id="tws_link_get_mobile_addr_by_handle__uint16_t.btif_bd_addr_tP"></a> <a id="tws__link__env_8h_1a8716aa733af78396948d68f722217811"></a> [btif\_ret\_t](../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") tws\_link\_get\_mobile\_addr\_by\_handle(uint16\_t acl\_handle, [btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   Get mobile address by ACL connection handle.

    Get the mobile phone address by the ACL connection handle \[acl\_handle\].

    参数:
    :   - **acl\_handle** – **\[in\]** ACL connection handle
        - **p\_addr** – **\[in\]** pointer to an address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv431tws_link_get_profile_sync_timerP14btif_bd_addr_t"></a>

<a id="_CPPv331tws_link_get_profile_sync_timerP14btif_bd_addr_t"></a> <a id="_CPPv231tws_link_get_profile_sync_timerP14btif_bd_addr_t"></a> <a id="tws_link_get_profile_sync_timer__btif_bd_addr_tP"></a> <a id="tws__link__env_8h_1a59287b3f0a3503d6d2a8fe2b63241bdd"></a> [tws\_sync\_timer\_env\_t](#_CPPv420tws_sync_timer_env_t "tws_sync_timer_env_t") \*tws\_link\_get\_profile\_sync\_timer([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   Get profile sync timer.

    Get the profile sync timeout timer for the mobile phone with address \[addr\].

    参数:
    :   **p\_addr** – **\[in\]** pointer to an address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t).

    返回:
    :   sync timeout timer pointer of type [tws\_sync\_timer\_env\_t](#structtws__sync__timer__env__t)

<a id="_CPPv431tws_link_mobile_set_audio_procyP14btif_bd_addr_t"></a>

<a id="_CPPv331tws_link_mobile_set_audio_procyP14btif_bd_addr_t"></a> <a id="_CPPv231tws_link_mobile_set_audio_procyP14btif_bd_addr_t"></a> <a id="tws_link_mobile_set_audio_procy__btif_bd_addr_tP"></a> <a id="tws__link__env_8h_1a32cbbd5fffb1a624fd71cce5100a0a0a"></a> bool tws\_link\_mobile\_set\_audio\_procy([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   Set audio proxy context.

    Set the audio proxy context to the environment parameters for the mobile phone with address \[addr\].

    参数:
    :   **p\_addr** – **\[in\]** pointer to an address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回值:
    :   - **true** – success
        - **false** – fail

    返回:
    :   result

<a id="_CPPv431tws_link_mobile_get_audio_procyP14btif_bd_addr_t"></a>

<a id="_CPPv331tws_link_mobile_get_audio_procyP14btif_bd_addr_t"></a> <a id="_CPPv231tws_link_mobile_get_audio_procyP14btif_bd_addr_t"></a> <a id="tws_link_mobile_get_audio_procy__btif_bd_addr_tP"></a> <a id="tws__link__env_8h_1a18ec8dc6f211195e44b21ddde50ec855"></a> [bt\_audio\_proxy\_ctx\_t](../../bt_audio_proxy/bt_audio_proxy.md#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*tws\_link\_mobile\_get\_audio\_procy([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   Get audio proxy context.

    Get the audio proxy context from the environment parameters for the mobile phone with address \[addr\].

    参数:
    :   **p\_addr** – **\[in\]** pointer to an address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回:
    :   pointer to an audio proxy context of type [bt\_audio\_proxy\_ctx\_t](../../bt_audio_proxy/bt_audio_proxy.md#structbt__audio__proxy__ctx__t).

<a id="_CPPv434tws_link_mobile_get_profile_backupP14btif_bd_addr_t"></a>

<a id="_CPPv334tws_link_mobile_get_profile_backupP14btif_bd_addr_t"></a> <a id="_CPPv234tws_link_mobile_get_profile_backupP14btif_bd_addr_t"></a> <a id="tws_link_mobile_get_profile_backup__btif_bd_addr_tP"></a> <a id="tws__link__env_8h_1ac3e08df859294ec85c5d5340835341c3"></a> [btif\_profile\_bitmap\_t](../../btif/btif_type.md#_CPPv421btif_profile_bitmap_t "btif_profile_bitmap_t") tws\_link\_mobile\_get\_profile\_backup([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   Get profile state backup.

    Get the profile state backup for the mobile phone with address \[addr\].

    参数:
    :   **p\_addr** – **\[in\]** pointer to an address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回:
    :   profile state backup of type btif\_profile\_bitmap\_t

<a id="_CPPv434tws_link_mobile_set_profile_backupP14btif_bd_addr_t21btif_profile_bitmap_t"></a>

<a id="_CPPv334tws_link_mobile_set_profile_backupP14btif_bd_addr_t21btif_profile_bitmap_t"></a> <a id="_CPPv234tws_link_mobile_set_profile_backupP14btif_bd_addr_t21btif_profile_bitmap_t"></a> <a id="tws_link_mobile_set_profile_backup__btif_bd_addr_tP.btif_profile_bitmap_t"></a> <a id="tws__link__env_8h_1ac4c0587a0c5b0b432e8a1c0ab8add24f"></a> bool tws\_link\_mobile\_set\_profile\_backup([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, [btif\_profile\_bitmap\_t](../../btif/btif_type.md#_CPPv421btif_profile_bitmap_t "btif_profile_bitmap_t") profile\_bitmap)
:   Set profile state backup.

    Set the profile state backup for the mobile phone with address \[addr\].

    参数:
    :   - **p\_addr** – **\[in\]** pointer to an address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)
        - **profile\_bitmap** – **\[in\]** profile state backup of type btif\_profile\_bitmap\_t

    返回值:
    :   - **true** – success
        - **false** – fail

    返回:
    :   result

<a id="_CPPv432tws_link_loss_connect_evt_handleP14btif_bd_addr_t7uint8_t"></a>

<a id="_CPPv332tws_link_loss_connect_evt_handleP14btif_bd_addr_t7uint8_t"></a> <a id="_CPPv232tws_link_loss_connect_evt_handleP14btif_bd_addr_t7uint8_t"></a> <a id="tws_link_loss_connect_evt_handle__btif_bd_addr_tP.uint8_t"></a> <a id="tws__link__env_8h_1ab6eec045c88cff051e2ecb2deceb5e92"></a> void tws\_link\_loss\_connect\_evt\_handle([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, uint8\_t status)
:   Handle loss connection event.

    Handle reconnection when the mobile phone with address \[addr\] is connected.

    参数:
    :   - **p\_addr** – **\[in\]** pointer to an address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)
        - **status** – **\[in\]** connection status

    返回:
    :   N/A

<a id="_CPPv431tws_link_loss_discon_evt_handleP14btif_bd_addr_t"></a>

<a id="_CPPv331tws_link_loss_discon_evt_handleP14btif_bd_addr_t"></a> <a id="_CPPv231tws_link_loss_discon_evt_handleP14btif_bd_addr_t"></a> <a id="tws_link_loss_discon_evt_handle__btif_bd_addr_tP"></a> <a id="tws__link__env_8h_1ae23bd5caac6c7909f4cf48c2ab0988dc"></a> void tws\_link\_loss\_discon\_evt\_handle([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   Handle loss disconnection event.

    Handle reconnection when the mobile phone with address \[addr\] is disconnected.

    参数:
    :   **p\_addr** – **\[in\]** pointer to an address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回:
    :   N/A

<a id="_CPPv423tws_link_loss_reset_envv"></a>

<a id="_CPPv323tws_link_loss_reset_envv"></a> <a id="_CPPv223tws_link_loss_reset_envv"></a> <a id="tws_link_loss_reset_env__void"></a> <a id="tws__link__env_8h_1aca9d9830aa3a429c49c7723aab5bee73"></a> void tws\_link\_loss\_reset\_env(void)
:   Reset the reconnection environment parameters.

    Reset the reconnection environment parameters.

    返回:
    :   N/A

<a id="_CPPv429tws_link_loss_get_reconn_addrPP14btif_bd_addr_t"></a>

<a id="_CPPv329tws_link_loss_get_reconn_addrPP14btif_bd_addr_t"></a> <a id="_CPPv229tws_link_loss_get_reconn_addrPP14btif_bd_addr_t"></a> <a id="tws_link_loss_get_reconn_addr__btif_bd_addr_tPP"></a> <a id="tws__link__env_8h_1af3ce0c268c4d254f2eb5ab9a030395eb"></a> [btif\_ret\_t](../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") tws\_link\_loss\_get\_reconn\_addr([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*\*p\_addr)
:   get reconnect address when tws link is lose

    provides p\_addr type pointer for get the reconnect address pointer.

    参数:
    :   **p\_addr** – **\[in\]** pointer to a [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t) type pointer.

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424tws_link_update_sch_infov"></a>

<a id="_CPPv324tws_link_update_sch_infov"></a> <a id="_CPPv224tws_link_update_sch_infov"></a> <a id="tws_link_update_sch_info__void"></a> <a id="tws__link__env_8h_1a6b734c551d49d199977f2ff8ddbeee64"></a> void tws\_link\_update\_sch\_info(void)
:   Update schedule information.

    Send TWS schedule information to the controller.

    返回:
    :   N/A

<a id="_CPPv425tws_link_restore_sch_infov"></a>

<a id="_CPPv325tws_link_restore_sch_infov"></a> <a id="_CPPv225tws_link_restore_sch_infov"></a> <a id="tws_link_restore_sch_info__void"></a> <a id="tws__link__env_8h_1acf3d7aa40280192d2fc2547a1cbef1f1"></a> void tws\_link\_restore\_sch\_info(void)
:   Restore schedule information.

    Send TWS schedule information to the controller.

    返回:
    :   N/A

<a id="_CPPv423tws_link_get_mobile_numv"></a>

<a id="_CPPv323tws_link_get_mobile_numv"></a> <a id="_CPPv223tws_link_get_mobile_numv"></a> <a id="tws_link_get_mobile_num__void"></a> <a id="tws__link__env_8h_1a6710dc2afad00469d3103f10ae9fa3b6"></a> uint8\_t tws\_link\_get\_mobile\_num(void)
:   Get link mobile number.

    Get the number of connected mobile phones.

    返回:
    :   number of connected mobile phones.

<a id="_CPPv422tws_link_get_scan_typev"></a>

<a id="_CPPv322tws_link_get_scan_typev"></a> <a id="_CPPv222tws_link_get_scan_typev"></a> <a id="tws_link_get_scan_type__void"></a> <a id="tws__link__env_8h_1afc30cea28c98b4d888d12302cf4e8a01"></a> uint8\_t tws\_link\_get\_scan\_type(void)
:   Get scan type.

    Get the scan type based on the TWS link environment parameters.

    返回:
    :   scan type of type btif\_enable\_scan\_t

<a id="_CPPv423tws_link_battery_report7uint8_t"></a>

<a id="_CPPv323tws_link_battery_report7uint8_t"></a> <a id="_CPPv223tws_link_battery_report7uint8_t"></a> <a id="tws_link_battery_report__uint8_t"></a> <a id="tws__link__env_8h_1acfeddaaf140824c93b141565393c62ac"></a> void tws\_link\_battery\_report(uint8\_t bat\_level)
:   Report battery level.

    Report the battery level \[bat\_level\] to the mobile phone

    参数:
    :   **bat\_level** – **\[in\]** battery level

    返回:
    :   N/A

<a id="_CPPv427tws_link_force_sync_profilev"></a>

<a id="_CPPv327tws_link_force_sync_profilev"></a> <a id="_CPPv227tws_link_force_sync_profilev"></a> <a id="tws_link_force_sync_profile__void"></a> <a id="tws__link__env_8h_1aa8c80af4ca10044b105b23ab5939a930"></a> void tws\_link\_force\_sync\_profile(void)
:   Force sync profile.

    Force sync profile when the device is wating sync profile

    返回:
    :   N/A **TWS\_LINK\_ENV\_H** EOF

<a id="structures"></a>

### Structures

<a id="_CPPv420tws_sync_timer_env_t"></a>

<a id="_CPPv320tws_sync_timer_env_t"></a> <a id="_CPPv220tws_sync_timer_env_t"></a> <a id="tws_sync_timer_env_t"></a> <a id="structtws__sync__timer__env__t"></a> struct tws\_sync\_timer\_env\_t
:   TWS sync timer structure definition.

<a id="_CPPv421tws_link_reconn_env_t"></a>

<a id="_CPPv321tws_link_reconn_env_t"></a> <a id="_CPPv221tws_link_reconn_env_t"></a> <a id="tws_link_reconn_env_t"></a> <a id="structtws__link__reconn__env__t"></a> struct tws\_link\_reconn\_env\_t
:   TWS link reconnect structure definition.
