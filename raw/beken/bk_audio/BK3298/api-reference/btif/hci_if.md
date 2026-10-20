---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/btif/hci_if.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="hci-interface-functions"></a>

# HCI Interface Functions

<a id="hci-if-api-brief"></a>

## HCI\_IF API Brief

| Application | Brief |
| --- | --- |
| [`hci_if_find_handle_by_addr()`](#_CPPv426hci_if_find_handle_by_addrP14btif_bd_addr_t "hci_if_find_handle_by_addr") | find connection handle by mobile addr |
| [`hci_if_find_addr_by_handle()`](#_CPPv426hci_if_find_addr_by_handle8uint16_t "hci_if_find_addr_by_handle") | find mobile addr by HCI connection handle |
| [`hci_if_send_command()`](#_CPPv419hci_if_send_command19hci_if_cmd_opcode_tP7uint8_t7uint8_t "hci_if_send_command") | app used to send HCI command |
| [`hci_if_conn_set_tws_role()`](#_CPPv424hci_if_conn_set_tws_role8uint16_t15btif_tws_role_t "hci_if_conn_set_tws_role") | app used to update TWS role |
| [`hci_if_conn_set_profile_sync_done()`](#_CPPv433hci_if_conn_set_profile_sync_done8uint16_t23btif_sync_prof_status_t "hci_if_conn_set_profile_sync_done") | app used to update profile sync state done to host stack |
| [`hci_if_conn_get_profile_sync_done()`](#_CPPv433hci_if_conn_get_profile_sync_done8uint16_t "hci_if_conn_get_profile_sync_done") | App other module used to get the profile sync state done flag |
| [`hci_if_register_TSS_or_sync_profile_done_cb()`](#_CPPv443hci_if_register_TSS_or_sync_profile_done_cb37hci_if_sync_profile_or_TSS_done_cb_fp "hci_if_register_TSS_or_sync_profile_done_cb") | Register tws switch or sync profile done callback handler |
| [`hci_if_get_sync_len()`](#_CPPv419hci_if_get_sync_lenP14btif_bd_addr_t "hci_if_get_sync_len") | return the HCI layer profile sync max len |
| [`hci_if_conn_sync()`](#_CPPv416hci_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t "hci_if_conn_sync") | TWS master used to sync profile to TWS slave |
| [`hci_if_conn_restore()`](#_CPPv419hci_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t "hci_if_conn_restore") | TWS slave used to receive profile to rebuild its host stack |
| [`hci_if_conn_restore_specific()`](#_CPPv428hci_if_conn_restore_specificP14btif_bd_addr_t8uint16_t8uint16_t "hci_if_conn_restore_specific") | TWS slave update connection handle and recover relevant settings |
| [`hci_if_get_conn_bt_role()`](#_CPPv423hci_if_get_conn_bt_role8uint16_t "hci_if_get_conn_bt_role") | app used to get the bt role of the current link |
| [`hci_if_get_conn_dir()`](#_CPPv419hci_if_get_conn_dir8uint16_t "hci_if_get_conn_dir") | app used to get the current link direction |
| [`hci_if_get_conn_mode()`](#_CPPv420hci_if_get_conn_mode8uint16_t "hci_if_get_conn_mode") | app used to the link’s ACL mode |
| [`hci_if_set_tx_data_allowed()`](#_CPPv426hci_if_set_tx_data_allowed8uint16_tb "hci_if_set_tx_data_allowed") | App used to set if data is TX allowed, when is TSS procedure |
| [`hci_if_get_tx_data_allowed()`](#_CPPv426hci_if_get_tx_data_allowed8uint16_t "hci_if_get_tx_data_allowed") | bt audio interface used to get IF data is TX allowed |
| [`hci_if_create_connection()`](#_CPPv424hci_if_create_connectionP14btif_bd_addr_t "hci_if_create_connection") | APP used to create one ACL connection |
| [`hci_if_register_event_callback()`](#_CPPv430hci_if_register_event_callbackP19btif_hci_register_t21btif_p_connection_req "hci_if_register_event_callback") | APP used to register event callback |
| [`bth_init()`](#_CPPv48bth_initP13tws_ux_info_t "bth_init") | hci layer initialise function API |
| [`hci_if_get_bt_last_two_record()`](#_CPPv429hci_if_get_bt_last_two_recordP18btif_bt_dev_info_tP18btif_bt_dev_info_t "hci_if_get_bt_last_two_record") | get last two device informaion |
| [`hci_if_get_conn_lk()`](#_CPPv418hci_if_get_conn_lkP14btif_bd_addr_tP9btif_lk_t "hci_if_get_conn_lk") | get dedicated bd\_addr link key |
| [`hci_if_add_conn_lk()`](#_CPPv418hci_if_add_conn_lkP14btif_bd_addr_tP9btif_lk_t18if_link_key_type_t "hci_if_add_conn_lk") | updata link key of target devcie |
| [`hci_if_delete_conn_lk()`](#_CPPv421hci_if_delete_conn_lkP14btif_bd_addr_t "hci_if_delete_conn_lk") | remove link key of target device |
| [`hci_if_register_lk_ctrl()`](#_CPPv423hci_if_register_lk_ctrlP18if_link_key_ctrl_t "hci_if_register_lk_ctrl") | register the link key ctrl function |
| [`hci_if_register_le_lk_ctrl()`](#_CPPv426hci_if_register_le_lk_ctrlP21if_le_link_key_ctrl_t "hci_if_register_le_lk_ctrl") | register the LE link key ctrl function |
| [`hci_if_write_scan_type()`](#_CPPv422hci_if_write_scan_type7uint8_t "hci_if_write_scan_type") | set scan type |
| [`hci_if_get_local_addr()`](#_CPPv421hci_if_get_local_addrv "hci_if_get_local_addr") | get local BT address |
| [`hci_if_get_dev_info_ptr()`](#_CPPv423hci_if_get_dev_info_ptrP14btif_bd_addr_tPP18btif_bt_dev_info_t "hci_if_get_dev_info_ptr") | get remote device information |
| [`hci_if_disconnect_all_link()`](#_CPPv426hci_if_disconnect_all_linkv "hci_if_disconnect_all_link") | disconnect all link befor the system shutdown |
| [`hci_if_enter_dut_mode()`](#_CPPv421hci_if_enter_dut_modev "hci_if_enter_dut_mode") | Enter DUT mode |
| [`hci_if_enter_pair_mode()`](#_CPPv422hci_if_enter_pair_modev "hci_if_enter_pair_mode") | BT module into pair mode |
| [`hci_if_is_le_handle()`](#_CPPv419hci_if_is_le_handle8uint16_t "hci_if_is_le_handle") | check handle is BLE or not |
| [`hci_if_get_le_conn_interval()`](#_CPPv427hci_if_get_le_conn_interval8uint16_t "hci_if_get_le_conn_interval") | get LE connection interval value by connection handle |
| [`hci_if_le_para_cfg()`](#_CPPv418hci_if_le_para_cfgP16le_if_cfg_para_t "hci_if_le_para_cfg") | set LE relevant configure into system |
| [`hci_if_get_mobile_link_cnt()`](#_CPPv426hci_if_get_mobile_link_cntv "hci_if_get_mobile_link_cnt") | get connected mobile link count |
| [`hci_if_get_conn_state()`](#_CPPv421hci_if_get_conn_state8uint16_t "hci_if_get_conn_state") | get connect state by using conneciotn handle |
| [`hci_if_send_temperature()`](#_CPPv423hci_if_send_temperaturev "hci_if_send_temperature") | tell BT controller that the temperature is changed. |
| [`hci_if_set_local_addr()`](#_CPPv421hci_if_set_local_addrP14btif_bd_addr_t "hci_if_set_local_addr") | update local MAC address |
| [`hci_if_set_psr_mode()`](#_CPPv419hci_if_set_psr_modeP14btif_bd_addr_t7uint8_t "hci_if_set_psr_mode") | set psr mode |
| [`hci_if_get_psr_mode()`](#_CPPv419hci_if_get_psr_modeP14btif_bd_addr_t "hci_if_get_psr_mode") | get psr mode |
| [`hci_if_get_local_EIR()`](#_CPPv420hci_if_get_local_EIRv "hci_if_get_local_EIR") | get local EIR |

<a id="hci-if-api-reference"></a>

## HCI\_IF API Reference

<a id="header-file"></a>

### Header File

- [btif/inc/hci\_if.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/btif/inc/hci_if.h)

<a id="functions"></a>

### Functions

<a id="_CPPv426hci_if_find_handle_by_addrP14btif_bd_addr_t"></a>

<a id="_CPPv326hci_if_find_handle_by_addrP14btif_bd_addr_t"></a> <a id="_CPPv226hci_if_find_handle_by_addrP14btif_bd_addr_t"></a> <a id="hci_if_find_handle_by_addr__btif_bd_addr_tP"></a> <a id="hci__if_8h_1ad7a91134324ba3d0ef4470af573049ea"></a> uint16\_t hci\_if\_find\_handle\_by\_addr([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   hci\_if\_find\_handle\_by\_addr brief description

    find connection handle by mobile addr

    参数:
    :   **p\_addr** – **\[in\]** remote MAC address

    返回值:
    :   - **0xFFFF** – not found
        - **other** – connection handle

    返回:
    :   connection handle

<a id="_CPPv426hci_if_find_addr_by_handle8uint16_t"></a>

<a id="_CPPv326hci_if_find_addr_by_handle8uint16_t"></a> <a id="_CPPv226hci_if_find_addr_by_handle8uint16_t"></a> <a id="hci_if_find_addr_by_handle__uint16_t"></a> <a id="hci__if_8h_1abedb21431466dd48166dfdc4e08eed2f"></a> [btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*hci\_if\_find\_addr\_by\_handle(uint16\_t handle)
:   hci\_if\_find\_addr\_by\_handle brief description

    find mobile addr by HCI connection handle

    参数:
    :   **handle** – **\[in\]** connection handle

    返回:
    :   Pointer of device address

<a id="_CPPv419hci_if_send_command19hci_if_cmd_opcode_tP7uint8_t7uint8_t"></a>

<a id="_CPPv319hci_if_send_command19hci_if_cmd_opcode_tP7uint8_t7uint8_t"></a> <a id="_CPPv219hci_if_send_command19hci_if_cmd_opcode_tP7uint8_t7uint8_t"></a> <a id="hci_if_send_command__hci_if_cmd_opcode_t.uint8_tP.uint8_t"></a> <a id="hci__if_8h_1a3f6b172720142721d2f97e09e8544054"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hci\_if\_send\_command([hci\_if\_cmd\_opcode\_t](#_CPPv419hci_if_cmd_opcode_t "hci_if_cmd_opcode_t") cmd\_opcode, uint8\_t \*p\_cmd, uint8\_t cmd\_len)
:   hci\_if\_send\_command brief description

    app used to send HCI command

    参数:
    :   - **cmd\_opcode** – **\[in\]** HCI command opcode
        - **p\_cmd** – **\[in\]** data buffer for HCI command
        - **cmd\_len** – **\[in\]** data length for p\_cmd

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424hci_if_conn_set_tws_role8uint16_t15btif_tws_role_t"></a>

<a id="_CPPv324hci_if_conn_set_tws_role8uint16_t15btif_tws_role_t"></a> <a id="_CPPv224hci_if_conn_set_tws_role8uint16_t15btif_tws_role_t"></a> <a id="hci_if_conn_set_tws_role__uint16_t.btif_tws_role_t"></a> <a id="hci__if_8h_1a8b66f6c97711d407761fad099904113e"></a> void hci\_if\_conn\_set\_tws\_role(uint16\_t handle, [btif\_tws\_role\_t](btif_type.md#_CPPv415btif_tws_role_t "btif_tws_role_t") tws\_role)
:   hci\_if\_conn\_set\_tws\_role brief description

    app used to update TWS role

    参数:
    :   - **handle** – **\[in\]** conndetion handle
        - **tws\_role** – **\[in\]** TWS role value

    返回:
    :   N/A

<a id="_CPPv433hci_if_conn_set_profile_sync_done8uint16_t23btif_sync_prof_status_t"></a>

<a id="_CPPv333hci_if_conn_set_profile_sync_done8uint16_t23btif_sync_prof_status_t"></a> <a id="_CPPv233hci_if_conn_set_profile_sync_done8uint16_t23btif_sync_prof_status_t"></a> <a id="hci_if_conn_set_profile_sync_done__uint16_t.btif_sync_prof_status_t"></a> <a id="hci__if_8h_1aaffded460b6decd887f61dab36fb8fd1"></a> void hci\_if\_conn\_set\_profile\_sync\_done(uint16\_t handle, [btif\_sync\_prof\_status\_t](btif_type.md#_CPPv423btif_sync_prof_status_t "btif_sync_prof_status_t") sync\_status)
:   hci\_if\_conn\_set\_profile\_sync\_done brief description

    app used to update profile sync state done to host stack

    参数:
    :   - **handle** – **\[in\]** connection handle
        - **sync\_status** – **\[in\]** sync status

    返回:
    :   N/A

<a id="_CPPv433hci_if_conn_get_profile_sync_done8uint16_t"></a>

<a id="_CPPv333hci_if_conn_get_profile_sync_done8uint16_t"></a> <a id="_CPPv233hci_if_conn_get_profile_sync_done8uint16_t"></a> <a id="hci_if_conn_get_profile_sync_done__uint16_t"></a> <a id="hci__if_8h_1a8792bcd9bff99a4597a8c4703b95286e"></a> [btif\_sync\_prof\_status\_t](btif_type.md#_CPPv423btif_sync_prof_status_t "btif_sync_prof_status_t") hci\_if\_conn\_get\_profile\_sync\_done(uint16\_t handle)
:   hci\_if\_conn\_get\_profile\_sync\_done brief description

    App other module used to get the profile sync state done flag

    参数:
    :   **handle** – **\[in\]** connection handle

    返回:
    :   sync profile status, see@btif\_sync\_prof\_status\_t

<a id="_CPPv443hci_if_register_TSS_or_sync_profile_done_cb37hci_if_sync_profile_or_TSS_done_cb_fp"></a>

<a id="_CPPv343hci_if_register_TSS_or_sync_profile_done_cb37hci_if_sync_profile_or_TSS_done_cb_fp"></a> <a id="_CPPv243hci_if_register_TSS_or_sync_profile_done_cb37hci_if_sync_profile_or_TSS_done_cb_fp"></a> <a id="hci_if_register_TSS_or_sync_profile_done_cb__hci_if_sync_profile_or_TSS_done_cb_fp"></a> <a id="hci__if_8h_1a3308743080e2f45233a19710ece86286"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hci\_if\_register\_TSS\_or\_sync\_profile\_done\_cb([hci\_if\_sync\_profile\_or\_TSS\_done\_cb\_fp](#_CPPv437hci_if_sync_profile_or_TSS_done_cb_fp "hci_if_sync_profile_or_TSS_done_cb_fp") cb)
:   hci\_if\_register\_TSS\_or\_sync\_profile\_done\_cb brief description

    Register tws switch or sync profile done callback handler

    参数:
    :   **cb** – **\[in\]** callback function

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419hci_if_get_sync_lenP14btif_bd_addr_t"></a>

<a id="_CPPv319hci_if_get_sync_lenP14btif_bd_addr_t"></a> <a id="_CPPv219hci_if_get_sync_lenP14btif_bd_addr_t"></a> <a id="hci_if_get_sync_len__btif_bd_addr_tP"></a> <a id="hci__if_8h_1a23c73d7167a5ee74d39785deeb2e4fb5"></a> uint16\_t hci\_if\_get\_sync\_len([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   hci\_if\_get\_sync\_len brief description

    return the HCI layer profile sync max len

    参数:
    :   **addr** – **\[in\]** remote MAC address

    返回:
    :   data length

<a id="_CPPv416hci_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t"></a>

<a id="_CPPv316hci_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t"></a> <a id="_CPPv216hci_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t"></a> <a id="hci_if_conn_sync__btif_bd_addr_tP.uint8_tP.uint16_t.uint16_tP"></a> <a id="hci__if_8h_1a68a0152950b6f6192d16467c78975a11"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hci\_if\_conn\_sync([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, uint8\_t \*p\_buff, uint16\_t buff\_len, uint16\_t \*p\_length)
:   hci\_if\_conn\_sync brief description

    TWS master used to sync profile to TWS slave

    参数:
    :   - **p\_addr** – **\[in\]** remote MAC addresss
        - **p\_buff** – **\[in\]** buffer used to sync profile data
        - **buff\_len** – **\[in\]** p\_buff allocated length
        - **p\_length** – **\[in\]** sync profile data length will be sent

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419hci_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t"></a>

<a id="_CPPv319hci_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t"></a> <a id="_CPPv219hci_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t"></a> <a id="hci_if_conn_restore__btif_bd_addr_tP.uint8_tP.uint16_t"></a> <a id="hci__if_8h_1a89472e61485c24acd25453bee5599194"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hci\_if\_conn\_restore([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, uint8\_t \*p\_buff, uint16\_t length)
:   hci\_if\_conn\_restore brief description

    TWS slave used to receive profile to rebuild its host stack

    参数:
    :   - **p\_addr** – **\[in\]** remote MAC address
        - **p\_buff** – **\[in\]** sync profile data
        - **length** – **\[in\]** p\_buff data length

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv428hci_if_conn_restore_specificP14btif_bd_addr_t8uint16_t8uint16_t"></a>

<a id="_CPPv328hci_if_conn_restore_specificP14btif_bd_addr_t8uint16_t8uint16_t"></a> <a id="_CPPv228hci_if_conn_restore_specificP14btif_bd_addr_t8uint16_t8uint16_t"></a> <a id="hci_if_conn_restore_specific__btif_bd_addr_tP.uint16_t.uint16_t"></a> <a id="hci__if_8h_1a2407160395ed271fe832f91e44496bdc"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hci\_if\_conn\_restore\_specific([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, uint16\_t handle, uint16\_t sync\_handle)
:   hci\_if\_conn\_restore\_specific brief description

    TWS slave update connection handle and recover relevant settings

    参数:
    :   - **p\_addr** – **\[in\]** remote MAC address
        - **handle** – **\[in\]** connection handle of ACL
        - **sync\_handle** – **\[in\]** connection handle of SCO

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv423hci_if_get_conn_bt_role8uint16_t"></a>

<a id="_CPPv323hci_if_get_conn_bt_role8uint16_t"></a> <a id="_CPPv223hci_if_get_conn_bt_role8uint16_t"></a> <a id="hci_if_get_conn_bt_role__uint16_t"></a> <a id="hci__if_8h_1aaec43bb45c8b381a9fabddc7a4ee51c1"></a> [btif\_bt\_role\_t](btif_type.md#_CPPv414btif_bt_role_t "btif_bt_role_t") hci\_if\_get\_conn\_bt\_role(uint16\_t handle)
:   hci\_if\_get\_conn\_bt\_role brief description

    app used to get the bt role of the current link

    参数:
    :   **handle** – **\[in\]** connection handle

    返回:
    :   role of conneciotn link

<a id="_CPPv419hci_if_get_conn_dir8uint16_t"></a>

<a id="_CPPv319hci_if_get_conn_dir8uint16_t"></a> <a id="_CPPv219hci_if_get_conn_dir8uint16_t"></a> <a id="hci_if_get_conn_dir__uint16_t"></a> <a id="hci__if_8h_1a783e8ab544612ac94957df2d78873ad2"></a> [if\_link\_dir\_t](#_CPPv413if_link_dir_t "if_link_dir_t") hci\_if\_get\_conn\_dir(uint16\_t handle)
:   hci\_if\_get\_conn\_dir brief description

    app used to get the current link direction

    参数:
    :   **handle** – **\[in\]** connection handle

    返回:
    :   direction of link

<a id="_CPPv420hci_if_get_conn_mode8uint16_t"></a>

<a id="_CPPv320hci_if_get_conn_mode8uint16_t"></a> <a id="_CPPv220hci_if_get_conn_mode8uint16_t"></a> <a id="hci_if_get_conn_mode__uint16_t"></a> <a id="hci__if_8h_1acc1faf2322cb1660375be99dfbb6164d"></a> [if\_link\_mode\_t](#_CPPv414if_link_mode_t "if_link_mode_t") hci\_if\_get\_conn\_mode(uint16\_t handle)
:   hci\_if\_get\_conn\_mode brief description

    app used to the link’s ACL mode

    参数:
    :   **handle** – **\[in\]** connection handle

    返回:
    :   mode type @if\_link\_mode\_t

<a id="_CPPv426hci_if_set_tx_data_allowed8uint16_tb"></a>

<a id="_CPPv326hci_if_set_tx_data_allowed8uint16_tb"></a> <a id="_CPPv226hci_if_set_tx_data_allowed8uint16_tb"></a> <a id="hci_if_set_tx_data_allowed__uint16_t.b"></a> <a id="hci__if_8h_1a1056c8b4c31c089f6a362c1d0080184e"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hci\_if\_set\_tx\_data\_allowed(uint16\_t handle, bool allowed)
:   hci\_if\_set\_tx\_data\_allowed brief description

    App used to set if data is TX allowed, when is TSS procedure

    参数:
    :   - **handle** – **\[in\]** connection handle
        - **allowed** – **\[in\]** allow / deny

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426hci_if_get_tx_data_allowed8uint16_t"></a>

<a id="_CPPv326hci_if_get_tx_data_allowed8uint16_t"></a> <a id="_CPPv226hci_if_get_tx_data_allowed8uint16_t"></a> <a id="hci_if_get_tx_data_allowed__uint16_t"></a> <a id="hci__if_8h_1a890f9e1456760945e8ba367d4ea9aed3"></a> bool hci\_if\_get\_tx\_data\_allowed(uint16\_t handle)
:   hci\_if\_get\_tx\_data\_allowed brief description

    bt audio interface used to get IF data is TX allowed

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **true** – allow
        - **fail** – deny

    返回:
    :   bool

<a id="_CPPv424hci_if_create_connectionP14btif_bd_addr_t"></a>

<a id="_CPPv324hci_if_create_connectionP14btif_bd_addr_t"></a> <a id="_CPPv224hci_if_create_connectionP14btif_bd_addr_t"></a> <a id="hci_if_create_connection__btif_bd_addr_tP"></a> <a id="hci__if_8h_1ad7f6b54c4948601cf761a5f0095031e2"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hci\_if\_create\_connection([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   hci\_if\_create\_connection brief description

    APP used to create one ACL connection

    参数:
    :   **p\_addr** – **\[in\]** remote MAC address

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv430hci_if_register_event_callbackP19btif_hci_register_t21btif_p_connection_req"></a>

<a id="_CPPv330hci_if_register_event_callbackP19btif_hci_register_t21btif_p_connection_req"></a> <a id="_CPPv230hci_if_register_event_callbackP19btif_hci_register_t21btif_p_connection_req"></a> <a id="hci_if_register_event_callback__btif_hci_register_tP.btif_p_connection_req"></a> <a id="hci__if_8h_1a52e46837d37383ddcee973c0f443df5c"></a> void hci\_if\_register\_event\_callback([btif\_hci\_register\_t](#_CPPv419btif_hci_register_t "btif_hci_register_t") \*p\_callback, [btif\_p\_connection\_req](btif_type.md#_CPPv421btif_p_connection_req "btif_p_connection_req") conn\_req)
:   hci\_if\_register\_event\_callback brief description

    APP used to register event callback

    参数:
    :   - **p\_callback** – **\[in\]** hci event callback struct
        - **conn\_req** – **\[in\]** connection request event callback function

    返回:
    :   N/A

<a id="_CPPv48bth_initP13tws_ux_info_t"></a>

<a id="_CPPv38bth_initP13tws_ux_info_t"></a> <a id="_CPPv28bth_initP13tws_ux_info_t"></a> <a id="bth_init__tws_ux_info_tP"></a> <a id="hci__if_8h_1a721241b252373f2cef10062c1ce6ceec"></a> void bth\_init([tws\_ux\_info\_t](btif_type.md#_CPPv413tws_ux_info_t "tws_ux_info_t") \*p\_tws\_ux\_info)
:   bth\_init brief description

    hci layer initialise function API

    返回:
    :   N/A

<a id="_CPPv429hci_if_get_bt_last_two_recordP18btif_bt_dev_info_tP18btif_bt_dev_info_t"></a>

<a id="_CPPv329hci_if_get_bt_last_two_recordP18btif_bt_dev_info_tP18btif_bt_dev_info_t"></a> <a id="_CPPv229hci_if_get_bt_last_two_recordP18btif_bt_dev_info_tP18btif_bt_dev_info_t"></a> <a id="hci_if_get_bt_last_two_record__btif_bt_dev_info_tP.btif_bt_dev_info_tP"></a> <a id="hci__if_8h_1a7816cbde9151825fa192f9928dcc2032"></a> uint8\_t hci\_if\_get\_bt\_last\_two\_record([btif\_bt\_dev\_info\_t](btif_type.md#_CPPv418btif_bt_dev_info_t "btif_bt_dev_info_t") \*p\_dev\_info1, [btif\_bt\_dev\_info\_t](btif_type.md#_CPPv418btif_bt_dev_info_t "btif_bt_dev_info_t") \*p\_dev\_info2)
:   hci\_if\_get\_bt\_last\_two\_record brief description

    get last two device informaion

    参数:
    :   - **p\_dev\_info1** – **\[out\]** information for device one
        - **p\_dev\_info2** – **\[out\]** information for device two

    返回:
    :   Found record count

<a id="_CPPv418hci_if_get_conn_lkP14btif_bd_addr_tP9btif_lk_t"></a>

<a id="_CPPv318hci_if_get_conn_lkP14btif_bd_addr_tP9btif_lk_t"></a> <a id="_CPPv218hci_if_get_conn_lkP14btif_bd_addr_tP9btif_lk_t"></a> <a id="hci_if_get_conn_lk__btif_bd_addr_tP.btif_lk_tP"></a> <a id="hci__if_8h_1ad1e723787b07ce5a36015b5ade583e5c"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hci\_if\_get\_conn\_lk([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*addr, [btif\_lk\_t](btif_type.md#_CPPv49btif_lk_t "btif_lk_t") \*p\_lk)
:   hci\_if\_get\_conn\_lk brief description

    get dedicated bd\_addr link key

    参数:
    :   - **addr** – **\[in\]** remote MAC address
        - **p\_lk** – **\[out\]** link key value

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv418hci_if_add_conn_lkP14btif_bd_addr_tP9btif_lk_t18if_link_key_type_t"></a>

<a id="_CPPv318hci_if_add_conn_lkP14btif_bd_addr_tP9btif_lk_t18if_link_key_type_t"></a> <a id="_CPPv218hci_if_add_conn_lkP14btif_bd_addr_tP9btif_lk_t18if_link_key_type_t"></a> <a id="hci_if_add_conn_lk__btif_bd_addr_tP.btif_lk_tP.if_link_key_type_t"></a> <a id="hci__if_8h_1a722f49760eadba362ba9adeddc858b10"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hci\_if\_add\_conn\_lk([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, [btif\_lk\_t](btif_type.md#_CPPv49btif_lk_t "btif_lk_t") \*p\_lk, [if\_link\_key\_type\_t](btif_type.md#_CPPv418if_link_key_type_t "if_link_key_type_t") key\_type)
:   hci\_if\_add\_conn\_lk brief description

    updata link key of target devcie

    参数:
    :   - **p\_addr** – **\[in\]** remote MAC
        - **p\_lk** – **\[in\]** link key value
        - **key\_type** – **\[in\]** link key type

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421hci_if_delete_conn_lkP14btif_bd_addr_t"></a>

<a id="_CPPv321hci_if_delete_conn_lkP14btif_bd_addr_t"></a> <a id="_CPPv221hci_if_delete_conn_lkP14btif_bd_addr_t"></a> <a id="hci_if_delete_conn_lk__btif_bd_addr_tP"></a> <a id="hci__if_8h_1a9bfe9010a410edb99b7baca63ce6a203"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hci\_if\_delete\_conn\_lk([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   hci\_if\_delete\_conn\_lk brief description

    remove link key of target device

    参数:
    :   **p\_addr** – **\[in\]** remote MAC address

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv423hci_if_register_lk_ctrlP18if_link_key_ctrl_t"></a>

<a id="_CPPv323hci_if_register_lk_ctrlP18if_link_key_ctrl_t"></a> <a id="_CPPv223hci_if_register_lk_ctrlP18if_link_key_ctrl_t"></a> <a id="hci_if_register_lk_ctrl__if_link_key_ctrl_tP"></a> <a id="hci__if_8h_1a1d7953cc3b14e3a4b8152246e2bcad00"></a> void hci\_if\_register\_lk\_ctrl([if\_link\_key\_ctrl\_t](#_CPPv418if_link_key_ctrl_t "if_link_key_ctrl_t") \*p\_lk\_ctrl)
:   hci\_if\_register\_lk\_ctrl brief description

    register the link key ctrl function

    参数:
    :   **p\_lk\_ctrl** – **\[in\]** link key control function struct

    返回:
    :   N/A

<a id="_CPPv426hci_if_register_le_lk_ctrlP21if_le_link_key_ctrl_t"></a>

<a id="_CPPv326hci_if_register_le_lk_ctrlP21if_le_link_key_ctrl_t"></a> <a id="_CPPv226hci_if_register_le_lk_ctrlP21if_le_link_key_ctrl_t"></a> <a id="hci_if_register_le_lk_ctrl__if_le_link_key_ctrl_tP"></a> <a id="hci__if_8h_1a9d081f9745c86cfc2d89317f8c483fca"></a> void hci\_if\_register\_le\_lk\_ctrl([if\_le\_link\_key\_ctrl\_t](#_CPPv421if_le_link_key_ctrl_t "if_le_link_key_ctrl_t") \*p\_lk\_ctrl)
:   hci\_if\_register\_le\_lk\_ctrl brief description

    register the LE link key ctrl function

    参数:
    :   **p\_lk\_ctrl** – **\[in\]** link key control function struct

    返回:
    :   N/A

<a id="_CPPv422hci_if_write_scan_type7uint8_t"></a>

<a id="_CPPv322hci_if_write_scan_type7uint8_t"></a> <a id="_CPPv222hci_if_write_scan_type7uint8_t"></a> <a id="hci_if_write_scan_type__uint8_t"></a> <a id="hci__if_8h_1a907adb4fc00117bf9188b4e0de36d4ba"></a> void hci\_if\_write\_scan\_type(uint8\_t scan\_type)
:   hci\_if\_write\_scan\_type brief description

    set scan type

    参数:
    :   **scan\_type** – **\[in\]** scan type value

    返回:
    :   N/A

<a id="_CPPv421hci_if_get_local_addrv"></a>

<a id="_CPPv321hci_if_get_local_addrv"></a> <a id="_CPPv221hci_if_get_local_addrv"></a> <a id="hci_if_get_local_addr__void"></a> <a id="hci__if_8h_1a11cd28069f4eb4cf9302f0cbcf66f292"></a> [btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*hci\_if\_get\_local\_addr(void)
:   hci\_if\_get\_local\_addr brief description

    get local BT address

    返回:
    :   local BT MAC address

<a id="_CPPv423hci_if_get_dev_info_ptrP14btif_bd_addr_tPP18btif_bt_dev_info_t"></a>

<a id="_CPPv323hci_if_get_dev_info_ptrP14btif_bd_addr_tPP18btif_bt_dev_info_t"></a> <a id="_CPPv223hci_if_get_dev_info_ptrP14btif_bd_addr_tPP18btif_bt_dev_info_t"></a> <a id="hci_if_get_dev_info_ptr__btif_bd_addr_tP.btif_bt_dev_info_tPP"></a> <a id="hci__if_8h_1ad3ad2dd9a547ef2941dbfd274402b1d9"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hci\_if\_get\_dev\_info\_ptr([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, [btif\_bt\_dev\_info\_t](btif_type.md#_CPPv418btif_bt_dev_info_t "btif_bt_dev_info_t") \*\*p\_dev\_info)
:   hci\_if\_get\_dev\_info\_ptr brief description

    get remote device information

    参数:
    :   - **p\_addr** – **\[in\]** remote MAC address
        - **p\_dev\_info** – **\[out\]** remote device information data struct

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426hci_if_disconnect_all_linkv"></a>

<a id="_CPPv326hci_if_disconnect_all_linkv"></a> <a id="_CPPv226hci_if_disconnect_all_linkv"></a> <a id="hci_if_disconnect_all_link__void"></a> <a id="hci__if_8h_1a8dfc52576a09effa1f9f038190bfb1ce"></a> void hci\_if\_disconnect\_all\_link(void)
:   hci\_if\_disconnect\_all\_link brief description

    disconnect all link befor the system shutdown

    返回:
    :   N/A

<a id="_CPPv421hci_if_enter_dut_modev"></a>

<a id="_CPPv321hci_if_enter_dut_modev"></a> <a id="_CPPv221hci_if_enter_dut_modev"></a> <a id="hci_if_enter_dut_mode__void"></a> <a id="hci__if_8h_1a43ef0a2449bef1e1acc14bc71030840b"></a> void hci\_if\_enter\_dut\_mode(void)
:   hci\_if\_enter\_dut\_mode brief description

    Enter DUT mode

    返回:
    :   N/A

<a id="_CPPv422hci_if_enter_pair_modev"></a>

<a id="_CPPv322hci_if_enter_pair_modev"></a> <a id="_CPPv222hci_if_enter_pair_modev"></a> <a id="hci_if_enter_pair_mode__void"></a> <a id="hci__if_8h_1acbfed41bebf37f4c8e6de9a506f9fbc4"></a> void hci\_if\_enter\_pair\_mode(void)
:   hci\_if\_enter\_pair\_mode brief description

    BT module into pair mode

    返回:
    :   N/A

<a id="_CPPv419hci_if_is_le_handle8uint16_t"></a>

<a id="_CPPv319hci_if_is_le_handle8uint16_t"></a> <a id="_CPPv219hci_if_is_le_handle8uint16_t"></a> <a id="hci_if_is_le_handle__uint16_t"></a> <a id="hci__if_8h_1a1d0df838d97ec583857b2e1b26851175"></a> bool hci\_if\_is\_le\_handle(uint16\_t handle)
:   hci\_if\_is\_le\_handle brief description

    check handle is BLE or not

    返回值:
    :   - **true** – a LE conneciton handle
        - **fail** – not a LE conneciton handle

    返回:
    :   bool

<a id="_CPPv427hci_if_get_le_conn_interval8uint16_t"></a>

<a id="_CPPv327hci_if_get_le_conn_interval8uint16_t"></a> <a id="_CPPv227hci_if_get_le_conn_interval8uint16_t"></a> <a id="hci_if_get_le_conn_interval__uint16_t"></a> <a id="hci__if_8h_1a128ebab08bb423aa47ece597d545706d"></a> uint16\_t hci\_if\_get\_le\_conn\_interval(uint16\_t handle)
:   hci\_if\_get\_le\_conn\_interval brief description

    get LE connection interval value by connection handle

    参数:
    :   **handle** – **\[in\]** connection handle

    返回:
    :   value

<a id="_CPPv418hci_if_le_para_cfgP16le_if_cfg_para_t"></a>

<a id="_CPPv318hci_if_le_para_cfgP16le_if_cfg_para_t"></a> <a id="_CPPv218hci_if_le_para_cfgP16le_if_cfg_para_t"></a> <a id="hci_if_le_para_cfg__le_if_cfg_para_tP"></a> <a id="hci__if_8h_1a107f245fa34e1699942e71bfbd00ad63"></a> void hci\_if\_le\_para\_cfg([le\_if\_cfg\_para\_t](btif_type.md#_CPPv416le_if_cfg_para_t "le_if_cfg_para_t") \*p\_le\_cfg)
:   hci\_if\_le\_para\_cfg brief description

    set LE relevant configure into system

    参数:
    :   **p\_le\_cfg** – **\[in\]** LE relevant configured parameter

    返回:
    :   N/A

<a id="_CPPv426hci_if_get_mobile_link_cntv"></a>

<a id="_CPPv326hci_if_get_mobile_link_cntv"></a> <a id="_CPPv226hci_if_get_mobile_link_cntv"></a> <a id="hci_if_get_mobile_link_cnt__void"></a> <a id="hci__if_8h_1ab45c1103f2dc99dcb97866743d41e3e8"></a> uint8\_t hci\_if\_get\_mobile\_link\_cnt(void)
:   hci\_if\_get\_mobile\_link\_cnt brief description

    get connected mobile link count

    返回:
    :   mobile count

<a id="_CPPv421hci_if_get_conn_state8uint16_t"></a>

<a id="_CPPv321hci_if_get_conn_state8uint16_t"></a> <a id="_CPPv221hci_if_get_conn_state8uint16_t"></a> <a id="hci_if_get_conn_state__uint16_t"></a> <a id="hci__if_8h_1a7f6942e59f407b63adb90d631599ac85"></a> [btif\_conn\_state\_t](#_CPPv417btif_conn_state_t "btif_conn_state_t") hci\_if\_get\_conn\_state(uint16\_t handle)
:   hci\_if\_get\_conn\_state brief description

    get connect state by using conneciotn handle

    参数:
    :   **handle** – **\[in\]** connection handle

    返回:
    :   connection state @btif\_conn\_state\_t

<a id="_CPPv423hci_if_send_temperaturev"></a>

<a id="_CPPv323hci_if_send_temperaturev"></a> <a id="_CPPv223hci_if_send_temperaturev"></a> <a id="hci_if_send_temperature__void"></a> <a id="hci__if_8h_1aea9df2ce2ae848005a3747c5c6444c83"></a> void hci\_if\_send\_temperature(void)
:   hci\_if\_send\_temperature brief description

    tell BT controller that the temperature is changed.

    返回:
    :   N/A

<a id="_CPPv421hci_if_set_local_addrP14btif_bd_addr_t"></a>

<a id="_CPPv321hci_if_set_local_addrP14btif_bd_addr_t"></a> <a id="_CPPv221hci_if_set_local_addrP14btif_bd_addr_t"></a> <a id="hci_if_set_local_addr__btif_bd_addr_tP"></a> <a id="hci__if_8h_1a14b5812b73166a8e8d75c09bc775ac30"></a> void hci\_if\_set\_local\_addr([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   hci\_if\_set\_local\_addr brief description

    update local MAC address

    参数:
    :   **p\_addr** – **\[in\]** local MAC address

    返回:
    :   N/A

<a id="_CPPv419hci_if_set_psr_modeP14btif_bd_addr_t7uint8_t"></a>

<a id="_CPPv319hci_if_set_psr_modeP14btif_bd_addr_t7uint8_t"></a> <a id="_CPPv219hci_if_set_psr_modeP14btif_bd_addr_t7uint8_t"></a> <a id="hci_if_set_psr_mode__btif_bd_addr_tP.uint8_t"></a> <a id="hci__if_8h_1aa78edfcaffb32d54f1c453e10e29fbe0"></a> void hci\_if\_set\_psr\_mode([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, uint8\_t psr\_mode)
:   hci\_if\_set\_psr\_mode brief description

    参数:
    :   **p\_addr** – **\[in\]** local MAC address

    Param :

<a id="_CPPv419hci_if_get_psr_modeP14btif_bd_addr_t"></a>

<a id="_CPPv319hci_if_get_psr_modeP14btif_bd_addr_t"></a> <a id="_CPPv219hci_if_get_psr_modeP14btif_bd_addr_t"></a> <a id="hci_if_get_psr_mode__btif_bd_addr_tP"></a> <a id="hci__if_8h_1a38309388c72144d6e434ed80de8eda31"></a> uint8\_t hci\_if\_get\_psr\_mode([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   hci\_if\_get\_psr\_mode brief description

    参数:
    :   **p\_addr** – **\[in\]** local MAC address

    返回:
    :   psr mode

<a id="_CPPv420hci_if_get_local_EIRv"></a>

<a id="_CPPv320hci_if_get_local_EIRv"></a> <a id="_CPPv220hci_if_get_local_EIRv"></a> <a id="hci_if_get_local_EIR__void"></a> <a id="hci__if_8h_1a8cf396d1434925ab176056d7d0a83c29"></a> uint8\_t \*hci\_if\_get\_local\_EIR(void)
:   hci\_if\_get\_local\_EIR brief description

    参数:
    :   **NA** – **\[in\]**

    返回:
    :   local EIR pointer

<a id="structures"></a>

### Structures

<a id="_CPPv419btif_hci_register_t"></a>

<a id="_CPPv319btif_hci_register_t"></a> <a id="_CPPv219btif_hci_register_t"></a> <a id="btif_hci_register_t"></a> <a id="structbtif__hci__register__t"></a> struct btif\_hci\_register\_t

<a id="_CPPv410inq_mode_t"></a>

<a id="_CPPv310inq_mode_t"></a> <a id="_CPPv210inq_mode_t"></a> <a id="inq_mode_t"></a> <a id="structinq__mode__t"></a> struct inq\_mode\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N10inq_mode_t8inq_modeE"></a>

    <a id="_CPPv3N10inq_mode_t8inq_modeE"></a> <a id="_CPPv2N10inq_mode_t8inq_modeE"></a> <a id="inq_mode_t::inq_mode__uint8_t"></a> <a id="structinq__mode__t_1af76fe1deb3827af70b1173d92e66be50"></a> uint8\_t inq\_mode
    :   inquiry mode

<a id="_CPPv431if_le_set_pref_slave_duration_t"></a>

<a id="_CPPv331if_le_set_pref_slave_duration_t"></a> <a id="_CPPv231if_le_set_pref_slave_duration_t"></a> <a id="if_le_set_pref_slave_duration_t"></a> <a id="structif__le__set__pref__slave__duration__t"></a> struct if\_le\_set\_pref\_slave\_duration\_t
:   LE set preference slave duration data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N31if_le_set_pref_slave_duration_t6conhdlE"></a>

    <a id="_CPPv3N31if_le_set_pref_slave_duration_t6conhdlE"></a> <a id="_CPPv2N31if_le_set_pref_slave_duration_t6conhdlE"></a> <a id="if_le_set_pref_slave_duration_t::conhdl__uint16_t"></a> <a id="structif__le__set__pref__slave__duration__t_1a51614445b64c39738fed57c78713495a"></a> uint16\_t conhdl
    :   Connection handle

    <a id="_CPPv4N31if_le_set_pref_slave_duration_t8durationE"></a>

    <a id="_CPPv3N31if_le_set_pref_slave_duration_t8durationE"></a> <a id="_CPPv2N31if_le_set_pref_slave_duration_t8durationE"></a> <a id="if_le_set_pref_slave_duration_t::duration__uint16_t"></a> <a id="structif__le__set__pref__slave__duration__t_1a16eecce121a2af7689b5718dc40953f5"></a> uint16\_t duration
    :   Preferred event duration (N \* 0.625 ms)

    <a id="_CPPv4N31if_le_set_pref_slave_duration_t9single_txE"></a>

    <a id="_CPPv3N31if_le_set_pref_slave_duration_t9single_txE"></a> <a id="_CPPv2N31if_le_set_pref_slave_duration_t9single_txE"></a> <a id="if_le_set_pref_slave_duration_t::single_tx__uint8_t"></a> <a id="structif__le__set__pref__slave__duration__t_1a979850cf5e8237bf59978b3835784abd"></a> uint8\_t single\_tx
    :   Slave transmits a single packet per connection event (False/True)

<a id="_CPPv420if_auto_accept_tws_t"></a>

<a id="_CPPv320if_auto_accept_tws_t"></a> <a id="_CPPv220if_auto_accept_tws_t"></a> <a id="if_auto_accept_tws_t"></a> <a id="structif__auto__accept__tws__t"></a> struct if\_auto\_accept\_tws\_t
:   TWS paired auto accept connection data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20if_auto_accept_tws_t11filter_typeE"></a>

    <a id="_CPPv3N20if_auto_accept_tws_t11filter_typeE"></a> <a id="_CPPv2N20if_auto_accept_tws_t11filter_typeE"></a> <a id="if_auto_accept_tws_t::filter_type__uint8_t"></a> <a id="structif__auto__accept__tws__t_1a196aecd2f138eb98867b7539f8a049bb"></a> uint8\_t filter\_type
    :   02 connection setup

    <a id="_CPPv4N20if_auto_accept_tws_t16filter_conditionE"></a>

    <a id="_CPPv3N20if_auto_accept_tws_t16filter_conditionE"></a> <a id="_CPPv2N20if_auto_accept_tws_t16filter_conditionE"></a> <a id="if_auto_accept_tws_t::filter_condition__uint8_t"></a> <a id="structif__auto__accept__tws__t_1aa7e2897b804a36963867ed01a87bf452"></a> uint8\_t filter\_condition
    :   0x02 auto accept

    <a id="_CPPv4N20if_auto_accept_tws_t4addrE"></a>

    <a id="_CPPv3N20if_auto_accept_tws_t4addrE"></a> <a id="_CPPv2N20if_auto_accept_tws_t4addrE"></a> <a id="if_auto_accept_tws_t::addr__btif_bd_addr_t"></a> <a id="structif__auto__accept__tws__t_1a26dce262371c112cea9639f19cfeb416"></a> [btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr
    :   auto accept addr

    <a id="_CPPv4N20if_auto_accept_tws_t16auto_accept_flagE"></a>

    <a id="_CPPv3N20if_auto_accept_tws_t16auto_accept_flagE"></a> <a id="_CPPv2N20if_auto_accept_tws_t16auto_accept_flagE"></a> <a id="if_auto_accept_tws_t::auto_accept_flag__uint8_t"></a> <a id="structif__auto__accept__tws__t_1a16bc44fca8055942ab9f5a1f9fcd7334"></a> uint8\_t auto\_accept\_flag
    :   02 auto accept and role switch disabled

<a id="_CPPv421if_set_conn_encrypt_t"></a>

<a id="_CPPv321if_set_conn_encrypt_t"></a> <a id="_CPPv221if_set_conn_encrypt_t"></a> <a id="if_set_conn_encrypt_t"></a> <a id="structif__set__conn__encrypt__t"></a> struct if\_set\_conn\_encrypt\_t
:   set connect encrypt command data struct defintion

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N21if_set_conn_encrypt_t6handleE"></a>

    <a id="_CPPv3N21if_set_conn_encrypt_t6handleE"></a> <a id="_CPPv2N21if_set_conn_encrypt_t6handleE"></a> <a id="if_set_conn_encrypt_t::handle__uint16_t"></a> <a id="structif__set__conn__encrypt__t_1a70c0fc990fdb6eb17cdbafcc5a683a4b"></a> uint16\_t handle
    :   connection handle

    <a id="_CPPv4N21if_set_conn_encrypt_t7encryptE"></a>

    <a id="_CPPv3N21if_set_conn_encrypt_t7encryptE"></a> <a id="_CPPv2N21if_set_conn_encrypt_t7encryptE"></a> <a id="if_set_conn_encrypt_t::encrypt__uint8_t"></a> <a id="structif__set__conn__encrypt__t_1acc2ae613f1f46ca96d256df0eff3615c"></a> uint8\_t encrypt
    :   true or false for enable or disable

<a id="_CPPv414if_hci_event_t"></a>

<a id="_CPPv314if_hci_event_t"></a> <a id="_CPPv214if_hci_event_t"></a> <a id="if_hci_event_t"></a> <a id="structif__hci__event__t"></a> struct if\_hci\_event\_t
:   HCI event header data struct defintion.

<a id="_CPPv426if_pscan_rep_mode_change_t"></a>

<a id="_CPPv326if_pscan_rep_mode_change_t"></a> <a id="_CPPv226if_pscan_rep_mode_change_t"></a> <a id="if_pscan_rep_mode_change_t"></a> <a id="structif__pscan__rep__mode__change__t"></a> struct if\_pscan\_rep\_mode\_change\_t
:   pscan repetation mode change data struct definition

<a id="_CPPv412if_cmd_cmp_t"></a>

<a id="_CPPv312if_cmd_cmp_t"></a> <a id="_CPPv212if_cmd_cmp_t"></a> <a id="if_cmd_cmp_t"></a> <a id="structif__cmd__cmp__t"></a> struct if\_cmd\_cmp\_t
:   command complete event data struct definition

<a id="_CPPv419if_setprofile_cmp_t"></a>

<a id="_CPPv319if_setprofile_cmp_t"></a> <a id="_CPPv219if_setprofile_cmp_t"></a> <a id="if_setprofile_cmp_t"></a> <a id="structif__setprofile__cmp__t"></a> struct if\_setprofile\_cmp\_t
:   TWS private set profile complete event data struct definition.

<a id="_CPPv419if_role_discovery_t"></a>

<a id="_CPPv319if_role_discovery_t"></a> <a id="_CPPv219if_role_discovery_t"></a> <a id="if_role_discovery_t"></a> <a id="structif__role__discovery__t"></a> struct if\_role\_discovery\_t
:   role discovery event data struct definition

<a id="_CPPv422if_local_feature_cmp_t"></a>

<a id="_CPPv322if_local_feature_cmp_t"></a> <a id="_CPPv222if_local_feature_cmp_t"></a> <a id="if_local_feature_cmp_t"></a> <a id="structif__local__feature__cmp__t"></a> struct if\_local\_feature\_cmp\_t
:   read local supported features complete event data struct definition

<a id="_CPPv420if_ext_feature_cmp_t"></a>

<a id="_CPPv320if_ext_feature_cmp_t"></a> <a id="_CPPv220if_ext_feature_cmp_t"></a> <a id="if_ext_feature_cmp_t"></a> <a id="structif__ext__feature__cmp__t"></a> struct if\_ext\_feature\_cmp\_t
:   read local extended features event data struct definition

<a id="_CPPv420if_btc_buffer_size_t"></a>

<a id="_CPPv320if_btc_buffer_size_t"></a> <a id="_CPPv220if_btc_buffer_size_t"></a> <a id="if_btc_buffer_size_t"></a> <a id="structif__btc__buffer__size__t"></a> struct if\_btc\_buffer\_size\_t
:   set host buffer size command data struct definition

<a id="_CPPv413if_inq_info_t"></a>

<a id="_CPPv313if_inq_info_t"></a> <a id="_CPPv213if_inq_info_t"></a> <a id="if_inq_info_t"></a> <a id="structif__inq__info__t"></a> struct if\_inq\_info\_t
:   inquiry result event data struct definition

<a id="_CPPv418if_conn_complete_t"></a>

<a id="_CPPv318if_conn_complete_t"></a> <a id="_CPPv218if_conn_complete_t"></a> <a id="if_conn_complete_t"></a> <a id="structif__conn__complete__t"></a> struct if\_conn\_complete\_t
:   connection complete event data struct definition

<a id="_CPPv413if_conn_req_t"></a>

<a id="_CPPv313if_conn_req_t"></a> <a id="_CPPv213if_conn_req_t"></a> <a id="if_conn_req_t"></a> <a id="structif__conn__req__t"></a> struct if\_conn\_req\_t
:   connection request event data struct definition

<a id="_CPPv418if_disc_complete_t"></a>

<a id="_CPPv318if_disc_complete_t"></a> <a id="_CPPv218if_disc_complete_t"></a> <a id="if_disc_complete_t"></a> <a id="structif__disc__complete__t"></a> struct if\_disc\_complete\_t
:   connection disconnect event data struct defintion

<a id="_CPPv418if_auth_complete_t"></a>

<a id="_CPPv318if_auth_complete_t"></a> <a id="_CPPv218if_auth_complete_t"></a> <a id="if_auth_complete_t"></a> <a id="structif__auth__complete__t"></a> struct if\_auth\_complete\_t
:   authentication complete event data struct definition

<a id="_CPPv417if_rnr_complete_t"></a>

<a id="_CPPv317if_rnr_complete_t"></a> <a id="_CPPv217if_rnr_complete_t"></a> <a id="if_rnr_complete_t"></a> <a id="structif__rnr__complete__t"></a> struct if\_rnr\_complete\_t
:   remote name request complete event data struct definition

<a id="_CPPv417if_encry_change_t"></a>

<a id="_CPPv317if_encry_change_t"></a> <a id="_CPPv217if_encry_change_t"></a> <a id="if_encry_change_t"></a> <a id="structif__encry__change__t"></a> struct if\_encry\_change\_t
:   encryption change event data struct defintion

<a id="_CPPv423if_change_lk_complete_t"></a>

<a id="_CPPv323if_change_lk_complete_t"></a> <a id="_CPPv223if_change_lk_complete_t"></a> <a id="if_change_lk_complete_t"></a> <a id="structif__change__lk__complete__t"></a> struct if\_change\_lk\_complete\_t
:   change link key complete event data struct definition

<a id="_CPPv423if_master_lk_complete_t"></a>

<a id="_CPPv323if_master_lk_complete_t"></a> <a id="_CPPv223if_master_lk_complete_t"></a> <a id="if_master_lk_complete_t"></a> <a id="structif__master__lk__complete__t"></a> struct if\_master\_lk\_complete\_t
:   select link key complete event data struct definition

<a id="_CPPv428if_remote_feature_complete_t"></a>

<a id="_CPPv328if_remote_feature_complete_t"></a> <a id="_CPPv228if_remote_feature_complete_t"></a> <a id="if_remote_feature_complete_t"></a> <a id="structif__remote__feature__complete__t"></a> struct if\_remote\_feature\_complete\_t
:   get remote feature complete event data struct definition

<a id="_CPPv428if_remote_version_complete_t"></a>

<a id="_CPPv328if_remote_version_complete_t"></a> <a id="_CPPv228if_remote_version_complete_t"></a> <a id="if_remote_version_complete_t"></a> <a id="structif__remote__version__complete__t"></a> struct if\_remote\_version\_complete\_t
:   get remote version compelete event data struct definition

<a id="_CPPv412if_hci_qos_t"></a>

<a id="_CPPv312if_hci_qos_t"></a> <a id="_CPPv212if_hci_qos_t"></a> <a id="if_hci_qos_t"></a> <a id="structif__hci__qos__t"></a> struct if\_hci\_qos\_t
:   QoS setup command data struct definition.

<a id="_CPPv423if_qos_setup_complete_t"></a>

<a id="_CPPv323if_qos_setup_complete_t"></a> <a id="_CPPv223if_qos_setup_complete_t"></a> <a id="if_qos_setup_complete_t"></a> <a id="structif__qos__setup__complete__t"></a> struct if\_qos\_setup\_complete\_t
:   QoS setup complete event data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N23if_qos_setup_complete_t5flagsE"></a>

    <a id="_CPPv3N23if_qos_setup_complete_t5flagsE"></a> <a id="_CPPv2N23if_qos_setup_complete_t5flagsE"></a> <a id="if_qos_setup_complete_t::flags__uint8_t"></a> <a id="structif__qos__setup__complete__t_1a500045424f822e2d6ddbb42b2d01db9d"></a> uint8\_t flags
    :   Reserved

<a id="_CPPv417if_cmd_complete_t"></a>

<a id="_CPPv317if_cmd_complete_t"></a> <a id="_CPPv217if_cmd_complete_t"></a> <a id="if_cmd_complete_t"></a> <a id="structif__cmd__complete__t"></a> struct if\_cmd\_complete\_t
:   command complete event data struct definition

<a id="_CPPv415if_cmd_status_t"></a>

<a id="_CPPv315if_cmd_status_t"></a> <a id="_CPPv215if_cmd_status_t"></a> <a id="if_cmd_status_t"></a> <a id="structif__cmd__status__t"></a> struct if\_cmd\_status\_t
:   command status event data struct definition

<a id="_CPPv413if_hw_error_t"></a>

<a id="_CPPv313if_hw_error_t"></a> <a id="_CPPv213if_hw_error_t"></a> <a id="if_hw_error_t"></a> <a id="structif__hw__error__t"></a> struct if\_hw\_error\_t
:   hardware error event data struct definition

<a id="_CPPv418if_flush_occured_t"></a>

<a id="_CPPv318if_flush_occured_t"></a> <a id="_CPPv218if_flush_occured_t"></a> <a id="if_flush_occured_t"></a> <a id="structif__flush__occured__t"></a> struct if\_flush\_occured\_t
:   flash occured event data struct definition

<a id="_CPPv416if_role_change_t"></a>

<a id="_CPPv316if_role_change_t"></a> <a id="_CPPv216if_role_change_t"></a> <a id="if_role_change_t"></a> <a id="structif__role__change__t"></a> struct if\_role\_change\_t
:   role changed event data struct definition

<a id="_CPPv420if_num_of_complete_t"></a>

<a id="_CPPv320if_num_of_complete_t"></a> <a id="_CPPv220if_num_of_complete_t"></a> <a id="if_num_of_complete_t"></a> <a id="structif__num__of__complete__t"></a> struct if\_num\_of\_complete\_t
:   set host number of completed packets command data struct definition

<a id="_CPPv416if_mode_change_t"></a>

<a id="_CPPv316if_mode_change_t"></a> <a id="_CPPv216if_mode_change_t"></a> <a id="if_mode_change_t"></a> <a id="structif__mode__change__t"></a> struct if\_mode\_change\_t
:   mode change event data struct definition

<a id="_CPPv414if_return_lk_t"></a>

<a id="_CPPv314if_return_lk_t"></a> <a id="_CPPv214if_return_lk_t"></a> <a id="if_return_lk_t"></a> <a id="structif__return__lk__t"></a> struct if\_return\_lk\_t
:   return link key event data struct definition

<a id="_CPPv417if_pin_code_req_t"></a>

<a id="_CPPv317if_pin_code_req_t"></a> <a id="_CPPv217if_pin_code_req_t"></a> <a id="if_pin_code_req_t"></a> <a id="structif__pin__code__req__t"></a> struct if\_pin\_code\_req\_t
:   PIN code request event data struct defintion.

<a id="_CPPv411if_lk_req_t"></a>

<a id="_CPPv311if_lk_req_t"></a> <a id="_CPPv211if_lk_req_t"></a> <a id="if_lk_req_t"></a> <a id="structif__lk__req__t"></a> struct if\_lk\_req\_t
:   link key request event data struct definition

<a id="_CPPv414if_lk_notify_t"></a>

<a id="_CPPv314if_lk_notify_t"></a> <a id="_CPPv214if_lk_notify_t"></a> <a id="if_lk_notify_t"></a> <a id="structif__lk__notify__t"></a> struct if\_lk\_notify\_t
:   link key notification event data struct definition

<a id="_CPPv425if_data_buffer_overflow_t"></a>

<a id="_CPPv325if_data_buffer_overflow_t"></a> <a id="_CPPv225if_data_buffer_overflow_t"></a> <a id="if_data_buffer_overflow_t"></a> <a id="structif__data__buffer__overflow__t"></a> struct if\_data\_buffer\_overflow\_t
:   data buffer overflow event data struct definition

<a id="_CPPv420if_max_slot_change_t"></a>

<a id="_CPPv320if_max_slot_change_t"></a> <a id="_CPPv220if_max_slot_change_t"></a> <a id="if_max_slot_change_t"></a> <a id="structif__max__slot__change__t"></a> struct if\_max\_slot\_change\_t
:   max slot change event data struct definition

<a id="_CPPv424if_clk_offset_complete_t"></a>

<a id="_CPPv324if_clk_offset_complete_t"></a> <a id="_CPPv224if_clk_offset_complete_t"></a> <a id="if_clk_offset_complete_t"></a> <a id="structif__clk__offset__complete__t"></a> struct if\_clk\_offset\_complete\_t
:   read clock offset complete event data struct definition

<a id="_CPPv420if_pac_type_change_t"></a>

<a id="_CPPv320if_pac_type_change_t"></a> <a id="_CPPv220if_pac_type_change_t"></a> <a id="if_pac_type_change_t"></a> <a id="structif__pac__type__change__t"></a> struct if\_pac\_type\_change\_t
:   connection packet type change event data struct definition

<a id="_CPPv418if_qos_violation_t"></a>

<a id="_CPPv318if_qos_violation_t"></a> <a id="_CPPv218if_qos_violation_t"></a> <a id="if_qos_violation_t"></a> <a id="structif__qos__violation__t"></a> struct if\_qos\_violation\_t
:   Qos violation event data struct definition.

<a id="_CPPv421if_pscan_rep_change_t"></a>

<a id="_CPPv321if_pscan_rep_change_t"></a> <a id="_CPPv221if_pscan_rep_change_t"></a> <a id="if_pscan_rep_change_t"></a> <a id="structif__pscan__rep__change__t"></a> struct if\_pscan\_rep\_change\_t
:   page scan repetition mode change event data struct definition

<a id="_CPPv423if_flow_spec_complete_t"></a>

<a id="_CPPv323if_flow_spec_complete_t"></a> <a id="_CPPv223if_flow_spec_complete_t"></a> <a id="if_flow_spec_complete_t"></a> <a id="structif__flow__spec__complete__t"></a> struct if\_flow\_spec\_complete\_t
:   flow specification complete event data struct definition

<a id="_CPPv423if_inq_info_with_rssi_t"></a>

<a id="_CPPv323if_inq_info_with_rssi_t"></a> <a id="_CPPv223if_inq_info_with_rssi_t"></a> <a id="if_inq_info_with_rssi_t"></a> <a id="structif__inq__info__with__rssi__t"></a> struct if\_inq\_info\_with\_rssi\_t
:   inquiry result with RSSI event data struct definition

<a id="_CPPv433if_inquiry_info_rssi_pscan_mode_t"></a>

<a id="_CPPv333if_inquiry_info_rssi_pscan_mode_t"></a> <a id="_CPPv233if_inquiry_info_rssi_pscan_mode_t"></a> <a id="if_inquiry_info_rssi_pscan_mode_t"></a> <a id="structif__inquiry__info__rssi__pscan__mode__t"></a> struct if\_inquiry\_info\_rssi\_pscan\_mode\_t

<a id="_CPPv433if_remote_ext_features_complete_t"></a>

<a id="_CPPv333if_remote_ext_features_complete_t"></a> <a id="_CPPv233if_remote_ext_features_complete_t"></a> <a id="if_remote_ext_features_complete_t"></a> <a id="structif__remote__ext__features__complete__t"></a> struct if\_remote\_ext\_features\_complete\_t
:   read remote extended features complete event data struct definition

<a id="_CPPv423if_sync_conn_complete_t"></a>

<a id="_CPPv323if_sync_conn_complete_t"></a> <a id="_CPPv223if_sync_conn_complete_t"></a> <a id="if_sync_conn_complete_t"></a> <a id="structif__sync__conn__complete__t"></a> struct if\_sync\_conn\_complete\_t
:   synchronous connection complete event data struct definition

<a id="_CPPv422if_sync_conn_changed_t"></a>

<a id="_CPPv322if_sync_conn_changed_t"></a> <a id="_CPPv222if_sync_conn_changed_t"></a> <a id="if_sync_conn_changed_t"></a> <a id="structif__sync__conn__changed__t"></a> struct if\_sync\_conn\_changed\_t
:   synchronous connection changed event data struct defintion

<a id="_CPPv420if_sniff_subrating_t"></a>

<a id="_CPPv320if_sniff_subrating_t"></a> <a id="_CPPv220if_sniff_subrating_t"></a> <a id="if_sniff_subrating_t"></a> <a id="structif__sniff__subrating__t"></a> struct if\_sniff\_subrating\_t
:   sniff subrating event data struct definition

<a id="_CPPv421if_ext_inquiry_info_t"></a>

<a id="_CPPv321if_ext_inquiry_info_t"></a> <a id="_CPPv221if_ext_inquiry_info_t"></a> <a id="if_ext_inquiry_info_t"></a> <a id="structif__ext__inquiry__info__t"></a> struct if\_ext\_inquiry\_info\_t
:   extended inquiry result event data struct definition

<a id="_CPPv423if_key_fresh_complete_t"></a>

<a id="_CPPv323if_key_fresh_complete_t"></a> <a id="_CPPv223if_key_fresh_complete_t"></a> <a id="if_key_fresh_complete_t"></a> <a id="structif__key__fresh__complete__t"></a> struct if\_key\_fresh\_complete\_t
:   encryption key refresh complete event data struct definition

<a id="_CPPv415if_io_cap_req_t"></a>

<a id="_CPPv315if_io_cap_req_t"></a> <a id="_CPPv215if_io_cap_req_t"></a> <a id="if_io_cap_req_t"></a> <a id="structif__io__cap__req__t"></a> struct if\_io\_cap\_req\_t
:   IO capability request event data struct definition.

<a id="_CPPv415if_io_cap_rsp_t"></a>

<a id="_CPPv315if_io_cap_rsp_t"></a> <a id="_CPPv215if_io_cap_rsp_t"></a> <a id="if_io_cap_rsp_t"></a> <a id="structif__io__cap__rsp__t"></a> struct if\_io\_cap\_rsp\_t
:   IO capability response event data struct definition.

<a id="_CPPv421if_user_confirm_req_t"></a>

<a id="_CPPv321if_user_confirm_req_t"></a> <a id="_CPPv221if_user_confirm_req_t"></a> <a id="if_user_confirm_req_t"></a> <a id="structif__user__confirm__req__t"></a> struct if\_user\_confirm\_req\_t
:   user confirmation request event data struct definition

<a id="_CPPv421if_user_passkey_req_t"></a>

<a id="_CPPv321if_user_passkey_req_t"></a> <a id="_CPPv221if_user_passkey_req_t"></a> <a id="if_user_passkey_req_t"></a> <a id="structif__user__passkey__req__t"></a> struct if\_user\_passkey\_req\_t
:   user passkey request event data struct definition

<a id="_CPPv428if_simple_pairing_complete_t"></a>

<a id="_CPPv328if_simple_pairing_complete_t"></a> <a id="_CPPv228if_simple_pairing_complete_t"></a> <a id="if_simple_pairing_complete_t"></a> <a id="structif__simple__pairing__complete__t"></a> struct if\_simple\_pairing\_complete\_t
:   simple pairing complete event data struct definition

<a id="_CPPv437if_link_supervision_timeout_changed_t"></a>

<a id="_CPPv337if_link_supervision_timeout_changed_t"></a> <a id="_CPPv237if_link_supervision_timeout_changed_t"></a> <a id="if_link_supervision_timeout_changed_t"></a> <a id="structif__link__supervision__timeout__changed__t"></a> struct if\_link\_supervision\_timeout\_changed\_t
:   ink supervision timeout changed event data struct definition

<a id="_CPPv424if_user_passkey_notify_t"></a>

<a id="_CPPv324if_user_passkey_notify_t"></a> <a id="_CPPv224if_user_passkey_notify_t"></a> <a id="if_user_passkey_notify_t"></a> <a id="structif__user__passkey__notify__t"></a> struct if\_user\_passkey\_notify\_t
:   user passkey notification event data struct definition

<a id="_CPPv432if_remote_host_features_notify_t"></a>

<a id="_CPPv332if_remote_host_features_notify_t"></a> <a id="_CPPv232if_remote_host_features_notify_t"></a> <a id="if_remote_host_features_notify_t"></a> <a id="structif__remote__host__features__notify__t"></a> struct if\_remote\_host\_features\_notify\_t
:   remote host supported features notification event data struct definition

<a id="_CPPv49if_rssi_t"></a>

<a id="_CPPv39if_rssi_t"></a> <a id="_CPPv29if_rssi_t"></a> <a id="if_rssi_t"></a> <a id="structif__rssi__t"></a> struct if\_rssi\_t
:   read RSSI command data struct definition

<a id="_CPPv48if_per_t"></a>

<a id="_CPPv38if_per_t"></a> <a id="_CPPv28if_per_t"></a> <a id="if_per_t"></a> <a id="structif__per__t"></a> struct if\_per\_t

<a id="_CPPv416if_switch_role_t"></a>

<a id="_CPPv316if_switch_role_t"></a> <a id="_CPPv216if_switch_role_t"></a> <a id="if_switch_role_t"></a> <a id="structif__switch__role__t"></a> struct if\_switch\_role\_t
:   role switch command data struct definition

<a id="_CPPv414if_disc_conn_t"></a>

<a id="_CPPv314if_disc_conn_t"></a> <a id="_CPPv214if_disc_conn_t"></a> <a id="if_disc_conn_t"></a> <a id="structif__disc__conn__t"></a> struct if\_disc\_conn\_t
:   disconnect command data struct definition

<a id="_CPPv416if_cancel_conn_t"></a>

<a id="_CPPv316if_cancel_conn_t"></a> <a id="_CPPv216if_cancel_conn_t"></a> <a id="if_cancel_conn_t"></a> <a id="structif__cancel__conn__t"></a> struct if\_cancel\_conn\_t
:   Create connection cancel command data struct definition.

<a id="_CPPv417if_write_policy_t"></a>

<a id="_CPPv317if_write_policy_t"></a> <a id="_CPPv217if_write_policy_t"></a> <a id="if_write_policy_t"></a> <a id="structif__write__policy__t"></a> struct if\_write\_policy\_t
:   write link policy settings command data struct definition

<a id="_CPPv412if_inquiry_t"></a>

<a id="_CPPv312if_inquiry_t"></a> <a id="_CPPv212if_inquiry_t"></a> <a id="if_inquiry_t"></a> <a id="structif__inquiry__t"></a> struct if\_inquiry\_t
:   inquiry command data struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N12if_inquiry_t6lengthE"></a>

    <a id="_CPPv3N12if_inquiry_t6lengthE"></a> <a id="_CPPv2N12if_inquiry_t6lengthE"></a> <a id="if_inquiry_t::length__uint8_t"></a> <a id="structif__inquiry__t_1a3599728fa704a910b6f6e6c1b7216cad"></a> uint8\_t length
    :   max amount of time (1.28s units)

<a id="_CPPv415if_wr_iac_lap_t"></a>

<a id="_CPPv315if_wr_iac_lap_t"></a> <a id="_CPPv215if_wr_iac_lap_t"></a> <a id="if_wr_iac_lap_t"></a> <a id="structif__wr__iac__lap__t"></a> struct if\_wr\_iac\_lap\_t
:   write current IAC LAP command data struct definition

<a id="_CPPv415if_inq_result_t"></a>

<a id="_CPPv315if_inq_result_t"></a> <a id="_CPPv215if_inq_result_t"></a> <a id="if_inq_result_t"></a> <a id="structif__inq__result__t"></a> struct if\_inq\_result\_t
:   inquiry result event data struct definition

<a id="_CPPv422if_user_event_ctrl_cmd"></a>

<a id="_CPPv322if_user_event_ctrl_cmd"></a> <a id="_CPPv222if_user_event_ctrl_cmd"></a> <a id="if_user_event_ctrl_cmd"></a> <a id="structif__user__event__ctrl__cmd"></a> struct if\_user\_event\_ctrl\_cmd
:   user event control data struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N22if_user_event_ctrl_cmd6enableE"></a>

    <a id="_CPPv3N22if_user_event_ctrl_cmd6enableE"></a> <a id="_CPPv2N22if_user_event_ctrl_cmd6enableE"></a> <a id="if_user_event_ctrl_cmd::enable__uint8_t"></a> <a id="structif__user__event__ctrl__cmd_1a30023991e4bac8680da9b3c00ad98a04"></a> uint8\_t enable
    :   true or false

    <a id="_CPPv4N22if_user_event_ctrl_cmd4modeE"></a>

    <a id="_CPPv3N22if_user_event_ctrl_cmd4modeE"></a> <a id="_CPPv2N22if_user_event_ctrl_cmd4modeE"></a> <a id="if_user_event_ctrl_cmd::mode__uint8_t"></a> <a id="structif__user__event__ctrl__cmd_1add283ceae2bce08e94fc3235196ad3fa"></a> uint8\_t mode
    :   mode value @btif\_user\_event\_mode\_t

    <a id="_CPPv4N22if_user_event_ctrl_cmd8dur_timeE"></a>

    <a id="_CPPv3N22if_user_event_ctrl_cmd8dur_timeE"></a> <a id="_CPPv2N22if_user_event_ctrl_cmd8dur_timeE"></a> <a id="if_user_event_ctrl_cmd::dur_time__uint32_t"></a> <a id="structif__user__event__ctrl__cmd_1a70a2434fab6da71d2558d80d33027c02"></a> uint32\_t dur\_time
    :   time duration, unit ms

    <a id="_CPPv4N22if_user_event_ctrl_cmd8intervalE"></a>

    <a id="_CPPv3N22if_user_event_ctrl_cmd8intervalE"></a> <a id="_CPPv2N22if_user_event_ctrl_cmd8intervalE"></a> <a id="if_user_event_ctrl_cmd::interval__uint32_t"></a> <a id="structif__user__event__ctrl__cmd_1a85d5092f464c1e5e2edef54b74ebdfd5"></a> uint32\_t interval
    :   user event interval, unit ms

    <a id="_CPPv4N22if_user_event_ctrl_cmd9le_handleE"></a>

    <a id="_CPPv3N22if_user_event_ctrl_cmd9le_handleE"></a> <a id="_CPPv2N22if_user_event_ctrl_cmd9le_handleE"></a> <a id="if_user_event_ctrl_cmd::le_handle__uint16_t"></a> <a id="structif__user__event__ctrl__cmd_1a2e8838a7ced6e1e1d90c86aab28b0de1"></a> uint16\_t le\_handle
    :   LE connection handle

    <a id="_CPPv4N22if_user_event_ctrl_cmd7usr_cbkE"></a>

    <a id="_CPPv3N22if_user_event_ctrl_cmd7usr_cbkE"></a> <a id="_CPPv2N22if_user_event_ctrl_cmd7usr_cbkE"></a> <a id="structif__user__event__ctrl__cmd_1a4311a7340917172f09f776535647c158"></a> void (\*usr\_cbk)(void)
    :   user callback function \- if bt controller service user event, then call this funtion

<a id="_CPPv425tws_snoop_connected_evt_t"></a>

<a id="_CPPv325tws_snoop_connected_evt_t"></a> <a id="_CPPv225tws_snoop_connected_evt_t"></a> <a id="tws_snoop_connected_evt_t"></a> <a id="structtws__snoop__connected__evt__t"></a> struct tws\_snoop\_connected\_evt\_t
:   TWS snoop connect event data struct definition.

<a id="_CPPv428tws_snoop_disconnected_evt_t"></a>

<a id="_CPPv328tws_snoop_disconnected_evt_t"></a> <a id="_CPPv228tws_snoop_disconnected_evt_t"></a> <a id="tws_snoop_disconnected_evt_t"></a> <a id="structtws__snoop__disconnected__evt__t"></a> struct tws\_snoop\_disconnected\_evt\_t
:   TWS snoop disconnect event data struct.

<a id="_CPPv416tws_switch_evt_t"></a>

<a id="_CPPv316tws_switch_evt_t"></a> <a id="_CPPv216tws_switch_evt_t"></a> <a id="tws_switch_evt_t"></a> <a id="structtws__switch__evt__t"></a> struct tws\_switch\_evt\_t
:   TWS switch event data struct.

<a id="_CPPv419tws_link_info_evt_t"></a>

<a id="_CPPv319tws_link_info_evt_t"></a> <a id="_CPPv219tws_link_info_evt_t"></a> <a id="tws_link_info_evt_t"></a> <a id="structtws__link__info__evt__t"></a> struct tws\_link\_info\_evt\_t
:   TWS private link information event data struct.

<a id="_CPPv425tws_bt_le_link_info_evt_t"></a>

<a id="_CPPv325tws_bt_le_link_info_evt_t"></a> <a id="_CPPv225tws_bt_le_link_info_evt_t"></a> <a id="tws_bt_le_link_info_evt_t"></a> <a id="structtws__bt__le__link__info__evt__t"></a> struct tws\_bt\_le\_link\_info\_evt\_t

<a id="_CPPv414if_tws_event_t"></a>

<a id="_CPPv314if_tws_event_t"></a> <a id="_CPPv214if_tws_event_t"></a> <a id="if_tws_event_t"></a> <a id="structif__tws__event__t"></a> struct if\_tws\_event\_t
:   TWS private event data struct.

<a id="_CPPv419freq_calib_reslut_t"></a>

<a id="_CPPv319freq_calib_reslut_t"></a> <a id="_CPPv219freq_calib_reslut_t"></a> <a id="freq_calib_reslut_t"></a> <a id="structfreq__calib__reslut__t"></a> struct freq\_calib\_reslut\_t

<a id="_CPPv416if_create_conn_t"></a>

<a id="_CPPv316if_create_conn_t"></a> <a id="_CPPv216if_create_conn_t"></a> <a id="if_create_conn_t"></a> <a id="structif__create__conn__t"></a> struct if\_create\_conn\_t
:   create connection data struct

<a id="_CPPv410tws_init_t"></a>

<a id="_CPPv310tws_init_t"></a> <a id="_CPPv210tws_init_t"></a> <a id="tws_init_t"></a> <a id="structtws__init__t"></a> struct tws\_init\_t
:   TWS private link data struct.

<a id="_CPPv413start_snoop_t"></a>

<a id="_CPPv313start_snoop_t"></a> <a id="_CPPv213start_snoop_t"></a> <a id="start_snoop_t"></a> <a id="structstart__snoop__t"></a> struct start\_snoop\_t
:   TWS start snoop data struct.

<a id="_CPPv412stop_snoop_t"></a>

<a id="_CPPv312stop_snoop_t"></a> <a id="_CPPv212stop_snoop_t"></a> <a id="stop_snoop_t"></a> <a id="structstop__snoop__t"></a> struct stop\_snoop\_t
:   TWS stop snoop data struct.

<a id="_CPPv412tws_switch_t"></a>

<a id="_CPPv312tws_switch_t"></a> <a id="_CPPv212tws_switch_t"></a> <a id="tws_switch_t"></a> <a id="structtws__switch__t"></a> struct tws\_switch\_t
:   TWS switch command data struct.

<a id="_CPPv413tws_sch_cmd_t"></a>

<a id="_CPPv313tws_sch_cmd_t"></a> <a id="_CPPv213tws_sch_cmd_t"></a> <a id="tws_sch_cmd_t"></a> <a id="structtws__sch__cmd__t"></a> struct tws\_sch\_cmd\_t
:   TWS schedule command data struct.

<a id="_CPPv422set_bt_compatibility_t"></a>

<a id="_CPPv322set_bt_compatibility_t"></a> <a id="_CPPv222set_bt_compatibility_t"></a> <a id="set_bt_compatibility_t"></a> <a id="structset__bt__compatibility__t"></a> struct set\_bt\_compatibility\_t
:   set BT compatibility command data struct

<a id="_CPPv422set_le_compatibility_t"></a>

<a id="_CPPv322set_le_compatibility_t"></a> <a id="_CPPv222set_le_compatibility_t"></a> <a id="set_le_compatibility_t"></a> <a id="structset__le__compatibility__t"></a> struct set\_le\_compatibility\_t
:   set BLE compatibility command data struct

<a id="_CPPv416if_accept_sync_t"></a>

<a id="_CPPv316if_accept_sync_t"></a> <a id="_CPPv216if_accept_sync_t"></a> <a id="if_accept_sync_t"></a> <a id="structif__accept__sync__t"></a> struct if\_accept\_sync\_t
:   accept sync parameter data struct

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N16if_accept_sync_t4addrE"></a>

    <a id="_CPPv3N16if_accept_sync_t4addrE"></a> <a id="_CPPv2N16if_accept_sync_t4addrE"></a> <a id="if_accept_sync_t::addr__btif_bd_addr_t"></a> <a id="structif__accept__sync__t_1acf727f2624cce71ef9d1e2a0a80c9014"></a> [btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr
    :   remote BT MAC address

    <a id="_CPPv4N16if_accept_sync_t11transmit_bwE"></a>

    <a id="_CPPv3N16if_accept_sync_t11transmit_bwE"></a> <a id="_CPPv2N16if_accept_sync_t11transmit_bwE"></a> <a id="if_accept_sync_t::transmit_bw__uint32_t"></a> <a id="structif__accept__sync__t_1afa3118cbe4050e215e02d232f9614a1a"></a> uint32\_t transmit\_bw
    :   transmit bandwith

    <a id="_CPPv4N16if_accept_sync_t10receive_bwE"></a>

    <a id="_CPPv3N16if_accept_sync_t10receive_bwE"></a> <a id="_CPPv2N16if_accept_sync_t10receive_bwE"></a> <a id="if_accept_sync_t::receive_bw__uint32_t"></a> <a id="structif__accept__sync__t_1a6a01df78adcff2ce17e67bac74f7d478"></a> uint32\_t receive\_bw
    :   receive bandwith

    <a id="_CPPv4N16if_accept_sync_t11max_latencyE"></a>

    <a id="_CPPv3N16if_accept_sync_t11max_latencyE"></a> <a id="_CPPv2N16if_accept_sync_t11max_latencyE"></a> <a id="if_accept_sync_t::max_latency__uint16_t"></a> <a id="structif__accept__sync__t_1a9b1a6185fcbe374af4d928758ec6a423"></a> uint16\_t max\_latency
    :   max latency

    <a id="_CPPv4N16if_accept_sync_t13voice_settingE"></a>

    <a id="_CPPv3N16if_accept_sync_t13voice_settingE"></a> <a id="_CPPv2N16if_accept_sync_t13voice_settingE"></a> <a id="if_accept_sync_t::voice_setting__uint16_t"></a> <a id="structif__accept__sync__t_1a66f92fab5d3a6a837b04af392c242ba7"></a> uint16\_t voice\_setting
    :   voice setting

    <a id="_CPPv4N16if_accept_sync_t17retransmit_effortE"></a>

    <a id="_CPPv3N16if_accept_sync_t17retransmit_effortE"></a> <a id="_CPPv2N16if_accept_sync_t17retransmit_effortE"></a> <a id="if_accept_sync_t::retransmit_effort__uint8_t"></a> <a id="structif__accept__sync__t_1a23b5964db6f0da5e2904d764ef51db5c"></a> uint8\_t retransmit\_effort
    :   retransmit effoer

    <a id="_CPPv4N16if_accept_sync_t11packet_typeE"></a>

    <a id="_CPPv3N16if_accept_sync_t11packet_typeE"></a> <a id="_CPPv2N16if_accept_sync_t11packet_typeE"></a> <a id="if_accept_sync_t::packet_type__uint16_t"></a> <a id="structif__accept__sync__t_1a7749d2dac8ad8619c4a0b8b306b72122"></a> uint16\_t packet\_type
    :   packet type of SCO

<a id="_CPPv428if_vs_set_link_profile_cmd_t"></a>

<a id="_CPPv328if_vs_set_link_profile_cmd_t"></a> <a id="_CPPv228if_vs_set_link_profile_cmd_t"></a> <a id="if_vs_set_link_profile_cmd_t"></a> <a id="structif__vs__set__link__profile__cmd__t"></a> struct if\_vs\_set\_link\_profile\_cmd\_t
:   Beken private HCI command for set profile state.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N28if_vs_set_link_profile_cmd_t6handleE"></a>

    <a id="_CPPv3N28if_vs_set_link_profile_cmd_t6handleE"></a> <a id="_CPPv2N28if_vs_set_link_profile_cmd_t6handleE"></a> <a id="if_vs_set_link_profile_cmd_t::handle__uint16_t"></a> <a id="structif__vs__set__link__profile__cmd__t_1a4948d891879378fa54322e5846ced5bd"></a> uint16\_t handle
    :   connection handle

    <a id="_CPPv4N28if_vs_set_link_profile_cmd_t12profile_typeE"></a>

    <a id="_CPPv3N28if_vs_set_link_profile_cmd_t12profile_typeE"></a> <a id="_CPPv2N28if_vs_set_link_profile_cmd_t12profile_typeE"></a> <a id="if_vs_set_link_profile_cmd_t::profile_type__btif_hci_profile_type_t"></a> <a id="structif__vs__set__link__profile__cmd__t_1ac214f5a44ad9bc50b853b4e54786754a"></a> [btif\_hci\_profile\_type\_t](#_CPPv423btif_hci_profile_type_t "btif_hci_profile_type_t") profile\_type
    :   profile index @btif\_hci\_profile\_type\_t

    <a id="_CPPv4N28if_vs_set_link_profile_cmd_t6enableE"></a>

    <a id="_CPPv3N28if_vs_set_link_profile_cmd_t6enableE"></a> <a id="_CPPv2N28if_vs_set_link_profile_cmd_t6enableE"></a> <a id="if_vs_set_link_profile_cmd_t::enable__uint8_t"></a> <a id="structif__vs__set__link__profile__cmd__t_1aad2d344d8b2658dc363b8320f83dcba1"></a> uint8\_t enable
    :   value for enable \| disable

<a id="_CPPv420if_vs_sleep_ctrl_cmd"></a>

<a id="_CPPv320if_vs_sleep_ctrl_cmd"></a> <a id="_CPPv220if_vs_sleep_ctrl_cmd"></a> <a id="if_vs_sleep_ctrl_cmd"></a> <a id="structif__vs__sleep__ctrl__cmd"></a> struct if\_vs\_sleep\_ctrl\_cmd
:   Beken private HCI command for sleep control.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20if_vs_sleep_ctrl_cmd4modeE"></a>

    <a id="_CPPv3N20if_vs_sleep_ctrl_cmd4modeE"></a> <a id="_CPPv2N20if_vs_sleep_ctrl_cmd4modeE"></a> <a id="if_vs_sleep_ctrl_cmd::mode__uint8_t"></a> <a id="structif__vs__sleep__ctrl__cmd_1a4ede460dd486c33642f877cbc0fad269"></a> uint8\_t mode
    :   mode @if\_sleep\_ctrl\_type

<a id="_CPPv418if_link_key_ctrl_t"></a>

<a id="_CPPv318if_link_key_ctrl_t"></a> <a id="_CPPv218if_link_key_ctrl_t"></a> <a id="if_link_key_ctrl_t"></a> <a id="structif__link__key__ctrl__t"></a> struct if\_link\_key\_ctrl\_t
:   link key control callback function struct

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18if_link_key_ctrl_t7get_keyE"></a>

    <a id="_CPPv3N18if_link_key_ctrl_t7get_keyE"></a> <a id="_CPPv2N18if_link_key_ctrl_t7get_keyE"></a> <a id="if_link_key_ctrl_t::get_key__hci_if_get_lk_pfn"></a> <a id="structif__link__key__ctrl__t_1a16d9f54e50aa2aef6d8ed699cdb7b66f"></a> [hci\_if\_get\_lk\_pfn](#_CPPv417hci_if_get_lk_pfn "hci_if_get_lk_pfn") get\_key
    :   callback function for get link key

    <a id="_CPPv4N18if_link_key_ctrl_t7add_keyE"></a>

    <a id="_CPPv3N18if_link_key_ctrl_t7add_keyE"></a> <a id="_CPPv2N18if_link_key_ctrl_t7add_keyE"></a> <a id="if_link_key_ctrl_t::add_key__hci_if_add_lk_pfn"></a> <a id="structif__link__key__ctrl__t_1a9638c4bff9ee106d901b37a8a1b27d81"></a> [hci\_if\_add\_lk\_pfn](#_CPPv417hci_if_add_lk_pfn "hci_if_add_lk_pfn") add\_key
    :   callback function for add link key

    <a id="_CPPv4N18if_link_key_ctrl_t7del_keyE"></a>

    <a id="_CPPv3N18if_link_key_ctrl_t7del_keyE"></a> <a id="_CPPv2N18if_link_key_ctrl_t7del_keyE"></a> <a id="if_link_key_ctrl_t::del_key__hci_if_delete_lk_pfn"></a> <a id="structif__link__key__ctrl__t_1a45b656f667c8bcedd9972d5eaabc504e"></a> [hci\_if\_delete\_lk\_pfn](#_CPPv420hci_if_delete_lk_pfn "hci_if_delete_lk_pfn") del\_key
    :   callback function for delete link key

    <a id="_CPPv4N18if_link_key_ctrl_t19get_last_two_recordE"></a>

    <a id="_CPPv3N18if_link_key_ctrl_t19get_last_two_recordE"></a> <a id="_CPPv2N18if_link_key_ctrl_t19get_last_two_recordE"></a> <a id="if_link_key_ctrl_t::get_last_two_record__hci_if_get_last_two_record_pfn"></a> <a id="structif__link__key__ctrl__t_1a728085a0fd60303a5b42746e8985d944"></a> [hci\_if\_get\_last\_two\_record\_pfn](#_CPPv430hci_if_get_last_two_record_pfn "hci_if_get_last_two_record_pfn") get\_last\_two\_record
    :   callback function for get last two devices

    <a id="_CPPv4N18if_link_key_ctrl_t16get_dev_info_ptrE"></a>

    <a id="_CPPv3N18if_link_key_ctrl_t16get_dev_info_ptrE"></a> <a id="_CPPv2N18if_link_key_ctrl_t16get_dev_info_ptrE"></a> <a id="if_link_key_ctrl_t::get_dev_info_ptr__hci_if_get_dev_info_ptr_pfn"></a> <a id="structif__link__key__ctrl__t_1a08fecd025e66a5dd11620f4658b76175"></a> [hci\_if\_get\_dev\_info\_ptr\_pfn](#_CPPv427hci_if_get_dev_info_ptr_pfn "hci_if_get_dev_info_ptr_pfn") get\_dev\_info\_ptr
    :   callback function fro get specific device infotmation

<a id="_CPPv421if_le_link_key_ctrl_t"></a>

<a id="_CPPv321if_le_link_key_ctrl_t"></a> <a id="_CPPv221if_le_link_key_ctrl_t"></a> <a id="if_le_link_key_ctrl_t"></a> <a id="structif__le__link__key__ctrl__t"></a> struct if\_le\_link\_key\_ctrl\_t
:   LE link key control callback function struct.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N21if_le_link_key_ctrl_t7get_keyE"></a>

    <a id="_CPPv3N21if_le_link_key_ctrl_t7get_keyE"></a> <a id="_CPPv2N21if_le_link_key_ctrl_t7get_keyE"></a> <a id="if_le_link_key_ctrl_t::get_key__hci_if_get_le_lk"></a> <a id="structif__le__link__key__ctrl__t_1ac3eb11827daa8ba43ecead867490f426"></a> [hci\_if\_get\_le\_lk](#_CPPv416hci_if_get_le_lk "hci_if_get_le_lk") get\_key
    :   callback function for get link key

    <a id="_CPPv4N21if_le_link_key_ctrl_t7add_keyE"></a>

    <a id="_CPPv3N21if_le_link_key_ctrl_t7add_keyE"></a> <a id="_CPPv2N21if_le_link_key_ctrl_t7add_keyE"></a> <a id="if_le_link_key_ctrl_t::add_key__hci_if_add_le_lk"></a> <a id="structif__le__link__key__ctrl__t_1a0e6f0d441ad6038ff5ce70aa5f7e2e58"></a> [hci\_if\_add\_le\_lk](#_CPPv416hci_if_add_le_lk "hci_if_add_le_lk") add\_key
    :   callback function for add link key

    <a id="_CPPv4N21if_le_link_key_ctrl_t7del_keyE"></a>

    <a id="_CPPv3N21if_le_link_key_ctrl_t7del_keyE"></a> <a id="_CPPv2N21if_le_link_key_ctrl_t7del_keyE"></a> <a id="if_le_link_key_ctrl_t::del_key__hci_if_delete_le_lk"></a> <a id="structif__le__link__key__ctrl__t_1a50026127a664b7a7a559c30167d5cf17"></a> [hci\_if\_delete\_le\_lk](#_CPPv419hci_if_delete_le_lk "hci_if_delete_le_lk") del\_key
    :   callback function for delete link key

<a id="macros"></a>

### Macros

<a id="c.HCI_SYNC_L2CAP_PENDING_CHAN_MAX_CNT"></a>

<a id="hci__if_8h_1af9ec23ba6036d75f2da6267fd4bc60e1"></a> HCI\_SYNC\_L2CAP\_PENDING\_CHAN\_MAX\_CNT

<a id="c.HCIIF_DEFAULT_TWS_INTERVAL"></a>

<a id="hci__if_8h_1a385610b31c24b9b617400a1a8fc6c229"></a> HCIIF\_DEFAULT\_TWS\_INTERVAL

<a id="c.HCIIF_DEFAULT_TWS_DURATION"></a>

<a id="hci__if_8h_1a1a1b90ce9a4deb5aed00910e2d99429c"></a> HCIIF\_DEFAULT\_TWS\_DURATION

<a id="c.HCIIF_SPEECHING_TWS_DURATION"></a>

<a id="hci__if_8h_1a5e6bd9fabd5c4cfda2b3fb0844bbbcaa"></a> HCIIF\_SPEECHING\_TWS\_DURATION

<a id="c.HCIIF_PROFILE_BUSY_TWS_INTERVAL"></a>

<a id="hci__if_8h_1afd170faf8c1a80f466f2068d3fd69e2c"></a> HCIIF\_PROFILE\_BUSY\_TWS\_INTERVAL

<a id="c.HCIIF_PROFILE_BUSY_TWS_DURATION"></a>

<a id="hci__if_8h_1a74ece71bd2ec3f48b52fc7776cda8ea5"></a> HCIIF\_PROFILE\_BUSY\_TWS\_DURATION

<a id="c.IF_PSCAN_EN"></a>

<a id="hci__if_8h_1a4fc437c6caca6956348a70e72cf2f141"></a> IF\_PSCAN\_EN

<a id="c.IF_ISCAN_EN"></a>

<a id="hci__if_8h_1af6cc640f0114d69c0e6d5920a57a8291"></a> IF\_ISCAN\_EN

<a id="c.IF_BOTH_SCAN_EN"></a>

<a id="hci__if_8h_1a84ba360b246c696ebd68d37101479aeb"></a> IF\_BOTH\_SCAN\_EN

<a id="c.IF_NO_SCAN_EN"></a>

<a id="hci__if_8h_1a910dfa71e6136d06cf45effd991dce7a"></a> IF\_NO\_SCAN\_EN

<a id="c.IF_LINK_KEY_LEN"></a>

<a id="hci__if_8h_1a6e2ded25e473c0d9076e4f8c04778b31"></a> IF\_LINK\_KEY\_LEN

<a id="c.LINK_INFO_MAX_LEN"></a>

<a id="hci__if_8h_1afcd6fb07a5f18468a8ea5020cf19f63b"></a> LINK\_INFO\_MAX\_LEN

<a id="c.LINK_INFO_MAX_TYPES"></a>

<a id="hci__if_8h_1a62c649d8d37c81def4e141fbdeb03aa2"></a> LINK\_INFO\_MAX\_TYPES

<a id="c.BTIF_HCI_INQ_CMP"></a>

<a id="hci__if_8h_1a475d963f8b1de14006a2c4c6b1a0f214"></a> BTIF\_HCI\_INQ\_CMP

<a id="c.BTIF_HCI_INQ_RESULT"></a>

<a id="hci__if_8h_1a16858a9417d5ace8c27ce11d94cb12fb"></a> BTIF\_HCI\_INQ\_RESULT

<a id="c.BTIF_CONN_COMPLETE"></a>

<a id="hci__if_8h_1a809375739daf4e93aa5d0ecb3b39e1b5"></a> BTIF\_CONN\_COMPLETE

<a id="c.BTIF_CONN_REQUEST"></a>

<a id="hci__if_8h_1a38236b140679338039e8d216d800b97c"></a> BTIF\_CONN\_REQUEST

<a id="c.BTIF_DISCONNECT_COMP"></a>

<a id="hci__if_8h_1a0805cc5760073830082af14a829d42c1"></a> BTIF\_DISCONNECT\_COMP

<a id="c.BTIF_AUTH_COMP"></a>

<a id="hci__if_8h_1af78333729b6410a91dd7bb685ae58101"></a> BTIF\_AUTH\_COMP

<a id="c.BTIF_ENCRYPT_CHG"></a>

<a id="hci__if_8h_1a9b11ff7d05261541427504657708d5b2"></a> BTIF\_ENCRYPT\_CHG

<a id="c.BTIF_ENCRYPT_CHG_V2"></a>

<a id="hci__if_8h_1a70ea97e4e05a3b5275d18da28f43ff80"></a> BTIF\_ENCRYPT\_CHG\_V2

<a id="c.BTIF_CMD_COMP"></a>

<a id="hci__if_8h_1a4e82abf50b3bc23a3c1c9183c337ada8"></a> BTIF\_CMD\_COMP

<a id="c.BTIF_CMD_STATUS"></a>

<a id="hci__if_8h_1a2a7b6a8d82aaf51b2de33af1093ac775"></a> BTIF\_CMD\_STATUS

<a id="c.BTIF_ROLE_CHG"></a>

<a id="hci__if_8h_1a14e5f157f224d602bf171b676d812f8d"></a> BTIF\_ROLE\_CHG

<a id="c.BTIF_MODE_CHG"></a>

<a id="hci__if_8h_1a24515ee0792f61382427a6d302202ccf"></a> BTIF\_MODE\_CHG

<a id="c.BTIF_KEY_REQUEST"></a>

<a id="hci__if_8h_1a8f6d71e68cbb686d36a04af69445466f"></a> BTIF\_KEY\_REQUEST

<a id="c.BTIF_KEY_NOTIFY"></a>

<a id="hci__if_8h_1acf6d286d4bc058c6e5e79d8c5c4bedc3"></a> BTIF\_KEY\_NOTIFY

<a id="c.BTIF_PSCAN_REP_CHANGE"></a>

<a id="hci__if_8h_1aa26150027cb693f3188d6678214225ff"></a> BTIF\_PSCAN\_REP\_CHANGE

<a id="c.BTIF_HCI_INQ_RESULT_EIR"></a>

<a id="hci__if_8h_1a59254a8f9abc0067e166f6e5146cbf5b"></a> BTIF\_HCI\_INQ\_RESULT\_EIR

<a id="c.BTIF_LE_EVENT"></a>

<a id="hci__if_8h_1ac653067645babeedabf1599d19be7904"></a> BTIF\_LE\_EVENT

<a id="c.BTIF_VENDOR_EVENT"></a>

<a id="hci__if_8h_1aaca4707005e913735707ca6bfdc36782"></a> BTIF\_VENDOR\_EVENT

<a id="c.BTIF_CONN_RELEASED"></a>

<a id="hci__if_8h_1a7f3ce18f3f1a66749fe9e55713b13e7f"></a> BTIF\_CONN\_RELEASED

<a id="c.BTIF_W4_OUT_CONNECT"></a>

<a id="hci__if_8h_1a4268387c7199e6177180686911622327"></a> BTIF\_W4\_OUT\_CONNECT

<a id="c.BTIF_W4_IN_CONNECT"></a>

<a id="hci__if_8h_1af08050329a25ba757a252838bd27fa05"></a> BTIF\_W4\_IN\_CONNECT

<a id="c.BTIF_CONN_CONNECTED"></a>

<a id="hci__if_8h_1a3c483f5779fb3ee72dba0adc3fb0c174"></a> BTIF\_CONN\_CONNECTED

<a id="c.BTIF_W4_RELEASE"></a>

<a id="hci__if_8h_1a396c714cb7fb44ecbb1249cada8c47ee"></a> BTIF\_W4\_RELEASE

<a id="c.BTIF_INVALID_STATE"></a>

<a id="hci__if_8h_1aa2d926817283758bbec02116fc8cd047"></a> BTIF\_INVALID\_STATE

<a id="c.IF_POLICY_ROLE_SWITCH"></a>

<a id="hci__if_8h_1ab2ec11178e77528f0072d5008defc36f"></a> IF\_POLICY\_ROLE\_SWITCH

<a id="c.IF_POLICY_HOLD_MODE"></a>

<a id="hci__if_8h_1ac61bb441f8ceeb2e90323a0e4a6f73c5"></a> IF\_POLICY\_HOLD\_MODE

<a id="c.IF_POLICY_SNIFF_MODE"></a>

<a id="hci__if_8h_1a465b6c4ac53f74f4cc16c17ba441150f"></a> IF\_POLICY\_SNIFF\_MODE

<a id="c.IF_ACTIVE"></a>

<a id="hci__if_8h_1a0c4695e17aaa65f9b0ca6de343b3ddc3"></a> IF\_ACTIVE

<a id="c.IF_HOLD"></a>

<a id="hci__if_8h_1a9efdf8504b9c743816fc34813e4fb156"></a> IF\_HOLD

<a id="c.IF_SNIFF"></a>

<a id="hci__if_8h_1a0061d61dbdac16ca565269fd500af16a"></a> IF\_SNIFF

<a id="c.IF_ERROR_MODE"></a>

<a id="hci__if_8h_1a21b36330d5dce27ac4d3817902f6298f"></a> IF\_ERROR\_MODE

<a id="c.IF_LINK_OUTGOING"></a>

<a id="hci__if_8h_1a1f9cbca35c18fbb55f7efd9a1074342e"></a> IF\_LINK\_OUTGOING

<a id="c.IF_LINK_INCOMING"></a>

<a id="hci__if_8h_1a955263bf7f518e749025344ee97945fa"></a> IF\_LINK\_INCOMING

<a id="c.IF_SCO_LINK"></a>

<a id="hci__if_8h_1ab32dd0d9db2b647727cdaa567626ec9e"></a> IF\_SCO\_LINK

<a id="c.IF_ACL_LINK"></a>

<a id="hci__if_8h_1aab28b5dd6324bc695865b7381323ac66"></a> IF\_ACL\_LINK

<a id="c.IF_ESCO_LINK"></a>

<a id="hci__if_8h_1ad2999629da52cd4b11655c51a0b7d560"></a> IF\_ESCO\_LINK

<a id="c.TWS_EVENT_SNOOP_CONNECTED"></a>

<a id="hci__if_8h_1a3462b9b43a37886639a056eb54281b73"></a> TWS\_EVENT\_SNOOP\_CONNECTED

<a id="c.TWS_EVENT_SNOOP_DISCONNECT"></a>

<a id="hci__if_8h_1aa4a2593d9e3f3ccb718931ca11129118"></a> TWS\_EVENT\_SNOOP\_DISCONNECT

<a id="c.TWS_EVENT_SWITCH_COMPLETE"></a>

<a id="hci__if_8h_1a7bfae639695ca8f4a75ef853b9be80d0"></a> TWS\_EVENT\_SWITCH\_COMPLETE

<a id="c.BT_CALIB_CMP_EVT_SUBCODE"></a>

<a id="hci__if_8h_1a1e3f85bf2e98876a4a60c155118b1d00"></a> BT\_CALIB\_CMP\_EVT\_SUBCODE

<a id="c.SLEEP_MODE_NORMAL"></a>

<a id="hci__if_8h_1a223407bbea2eae2a8ede19ea245e1f64"></a> SLEEP\_MODE\_NORMAL

<a id="c.SLEEP_MODE_TIME_WAKEUP"></a>

<a id="hci__if_8h_1a80e9830c9e13495c8d12e93ccf9c6b5a"></a> SLEEP\_MODE\_TIME\_WAKEUP

<a id="c.SLEEP_MODE_WAKEUP"></a>

<a id="hci__if_8h_1a5a70973ffdcd68fcc28ae4064db9fae3"></a> SLEEP\_MODE\_WAKEUP

<a id="c.BTIF_HCI_INQUIRY"></a>

<a id="hci__if_8h_1ad736056c71b46681e7db698e07930d41"></a> BTIF\_HCI\_INQUIRY
:   LINK CONTROL CMD.

<a id="c.BTIF_HCI_CANCEL_INQURIY"></a>

<a id="hci__if_8h_1a40106de1be3bf9dfcd27487aa9dcf3bf"></a> BTIF\_HCI\_CANCEL\_INQURIY

<a id="c.BTIF_HCI_ENTER_PERIODIC_INQURIY"></a>

<a id="hci__if_8h_1af184f13e5ed2216899b3705064a8ebf3"></a> BTIF\_HCI\_ENTER\_PERIODIC\_INQURIY

<a id="c.BTIF_HCI_EXIT_PERIODIC_INQURIY"></a>

<a id="hci__if_8h_1aa51d22aacb973bdf27ea0e760a3207f8"></a> BTIF\_HCI\_EXIT\_PERIODIC\_INQURIY

<a id="c.BTIF_HCI_CREATE_CONNECTION"></a>

<a id="hci__if_8h_1af948040a55e6703233f4eb61572d15a0"></a> BTIF\_HCI\_CREATE\_CONNECTION

<a id="c.BTIF_HCI_DISC_CONNECTION"></a>

<a id="hci__if_8h_1ab00b62dde8f2c077d2541ca6e643db24"></a> BTIF\_HCI\_DISC\_CONNECTION

<a id="c.BTIF_HCI_CANCEL_CREATE_CONNECTION"></a>

<a id="hci__if_8h_1a185596bb330d6c679189645a0bb8dfb8"></a> BTIF\_HCI\_CANCEL\_CREATE\_CONNECTION

<a id="c.BTIF_HCI_ACCEPT_CONN_REQUEST"></a>

<a id="hci__if_8h_1a2a5812c6df31d0714ffe63c435869dcf"></a> BTIF\_HCI\_ACCEPT\_CONN\_REQUEST

<a id="c.BTIF_HCI_REJECT_CONN_REQUEST"></a>

<a id="hci__if_8h_1aced7514cb89936f816d8564e3c20363b"></a> BTIF\_HCI\_REJECT\_CONN\_REQUEST

<a id="c.BTIF_HCI_LK_REQ_REPLY"></a>

<a id="hci__if_8h_1abd34316a323341b1ffafe3c1328d1ac6"></a> BTIF\_HCI\_LK\_REQ\_REPLY

<a id="c.BTIF_HCI_LK_REQ_NEG_REPLY"></a>

<a id="hci__if_8h_1aa0604c185616d49065f9de2d1707fee2"></a> BTIF\_HCI\_LK\_REQ\_NEG\_REPLY

<a id="c.BTIF_HCI_PIN_CODE_REQ_REPLY"></a>

<a id="hci__if_8h_1a8c7c1c3ebaf490952a18f86a576192c5"></a> BTIF\_HCI\_PIN\_CODE\_REQ\_REPLY

<a id="c.BTIF_HCI_PIN_CODE_REQ_NEG_REPLY"></a>

<a id="hci__if_8h_1a84f420d3acb88f1d1e664c95f66e2263"></a> BTIF\_HCI\_PIN\_CODE\_REQ\_NEG\_REPLY

<a id="c.BTIF_HCI_CHANGE_PACKET_TYPE"></a>

<a id="hci__if_8h_1a1c37a227b46246ee7250ac99d697e83b"></a> BTIF\_HCI\_CHANGE\_PACKET\_TYPE

<a id="c.BTIF_HCI_AUTH_REQUEST"></a>

<a id="hci__if_8h_1a9fa0c32526423a262dd269f000a7e93e"></a> BTIF\_HCI\_AUTH\_REQUEST

<a id="c.BTIF_HCI_SET_CONN_ENCRY"></a>

<a id="hci__if_8h_1ab782ea41dca718c4321a8a2a261849ee"></a> BTIF\_HCI\_SET\_CONN\_ENCRY

<a id="c.BTIF_HCI_CHANGE_CONN_LK"></a>

<a id="hci__if_8h_1aa54c2d7a7f5c9096915045de78327b49"></a> BTIF\_HCI\_CHANGE\_CONN\_LK

<a id="c.BTIF_HCI_MASTER_LK"></a>

<a id="hci__if_8h_1a2466617979f2dbe7824cbc00a38b8841"></a> BTIF\_HCI\_MASTER\_LK

<a id="c.BTIF_HCI_REMOTE_NAME_REQ"></a>

<a id="hci__if_8h_1a8cd70210aeaf5280055294b0f0f6bf24"></a> BTIF\_HCI\_REMOTE\_NAME\_REQ

<a id="c.BTIF_HCI_REMOTE_NAME_CANCEL"></a>

<a id="hci__if_8h_1a83dcc8a0dbf026da77531af634be0a88"></a> BTIF\_HCI\_REMOTE\_NAME\_CANCEL

<a id="c.BTIF_HCI_REMOTE_FEATURE"></a>

<a id="hci__if_8h_1ac115f08d9ff8deddd9839cf4ae457865"></a> BTIF\_HCI\_REMOTE\_FEATURE

<a id="c.BTIF_HCI_REMOTE_EXT_FEATURE"></a>

<a id="hci__if_8h_1ac28754d1ea0ff51f493831f9faebb2df"></a> BTIF\_HCI\_REMOTE\_EXT\_FEATURE

<a id="c.BTIF_HCI_REMOTE_VERSION"></a>

<a id="hci__if_8h_1a04a0ce4e992b5c6fd0ed09575b7142b0"></a> BTIF\_HCI\_REMOTE\_VERSION

<a id="c.BTIF_HCI_CLK_OFFSET"></a>

<a id="hci__if_8h_1af89af02db3dcacbc81d39266c12318ea"></a> BTIF\_HCI\_CLK\_OFFSET

<a id="c.BTIF_HCI_READ_LMP_HANDLE"></a>

<a id="hci__if_8h_1af0c5dce2ed2d1be0db65d0b5ac1f0ad4"></a> BTIF\_HCI\_READ\_LMP\_HANDLE

<a id="c.BTIF_HCI_SETUP_SYNC"></a>

<a id="hci__if_8h_1a82a8d344533954afcc102c1e5b8bfe78"></a> BTIF\_HCI\_SETUP\_SYNC

<a id="c.BTIF_HCI_ACCEPT_SYNC_REQ"></a>

<a id="hci__if_8h_1aad8e9a62f0443642d673debe3b3938b5"></a> BTIF\_HCI\_ACCEPT\_SYNC\_REQ

<a id="c.BTIF_HCI_REJECT_SYNC_REQ"></a>

<a id="hci__if_8h_1a2d04ec5ca0abb48221ecff08dd953187"></a> BTIF\_HCI\_REJECT\_SYNC\_REQ

<a id="c.BTIF_HCI_IO_CAP_REPLY"></a>

<a id="hci__if_8h_1a64d70bc72d935ed6f933e1963288134f"></a> BTIF\_HCI\_IO\_CAP\_REPLY

<a id="c.BTIF_HCI_USER_CONFIRM_REPLY"></a>

<a id="hci__if_8h_1a16135e1d82a5d6c7f08308592fc67c4e"></a> BTIF\_HCI\_USER\_CONFIRM\_REPLY

<a id="c.BTIF_HCI_USER_CONFIRM_NEG_REPLY"></a>

<a id="hci__if_8h_1a34c1d5b658cbcee43f6bf697105ee9eb"></a> BTIF\_HCI\_USER\_CONFIRM\_NEG\_REPLY

<a id="c.BTIF_HCI_USER_PASSKEY_REPLY"></a>

<a id="hci__if_8h_1a56f5d37acd32d46f9fc6c90ac5c29697"></a> BTIF\_HCI\_USER\_PASSKEY\_REPLY

<a id="c.BTIF_HCI_USER_PASSKEY_NEG_REPLY"></a>

<a id="hci__if_8h_1a053defa8ff51ac4ae10fea80dbe255c6"></a> BTIF\_HCI\_USER\_PASSKEY\_NEG\_REPLY

<a id="c.BTIF_HCI_IO_CAP_NEG_REPLY"></a>

<a id="hci__if_8h_1a5afdb3111dc82dbeecbf571439bc0b5d"></a> BTIF\_HCI\_IO\_CAP\_NEG\_REPLY

<a id="c.BTIF_HCI_ENTER_SNIFF"></a>

<a id="hci__if_8h_1ae9a4453865a00e28878c935dbfb69b17"></a> BTIF\_HCI\_ENTER\_SNIFF
:   LINK POLICY CMD.

<a id="c.BTIF_HCI_EXIT_SNIFF"></a>

<a id="hci__if_8h_1ae003988b5c519d1f051140a92e8d7952"></a> BTIF\_HCI\_EXIT\_SNIFF

<a id="c.BTIF_HCI_ROLE_DISCOVERY"></a>

<a id="hci__if_8h_1afa22c2a195136beba7d7bf18881288ec"></a> BTIF\_HCI\_ROLE\_DISCOVERY

<a id="c.BTIF_HCI_SWITCH_ROLE"></a>

<a id="hci__if_8h_1ae6473ca53b7fa6d615fba27b2f9d385e"></a> BTIF\_HCI\_SWITCH\_ROLE

<a id="c.BTIF_HCI_READ_LINK_POLICY"></a>

<a id="hci__if_8h_1a9a2def89c0c9ab66669226d25c5a2743"></a> BTIF\_HCI\_READ\_LINK\_POLICY

<a id="c.BTIF_HCI_WRITE_LINK_POLICY"></a>

<a id="hci__if_8h_1a4cb4b2c7670d368ac0ee0356a11fe1b2"></a> BTIF\_HCI\_WRITE\_LINK\_POLICY

<a id="c.BTIF_HCI_READ_DEFAULT_LINK_POLICY"></a>

<a id="hci__if_8h_1a552c413106ef65c83cae88bff99ac86c"></a> BTIF\_HCI\_READ\_DEFAULT\_LINK\_POLICY

<a id="c.BTIF_HCI_WRITE_DEFAULT_LINK_POLICY"></a>

<a id="hci__if_8h_1aa2ded7965b192e7fec3e5cc776f67f0e"></a> BTIF\_HCI\_WRITE\_DEFAULT\_LINK\_POLICY

<a id="c.BTIF_HCI_EN_DUT_MODE_CMD"></a>

<a id="hci__if_8h_1a1754accb713b3bb886e5c9ad60e5c484"></a> BTIF\_HCI\_EN\_DUT\_MODE\_CMD

<a id="c.BTIF_HCI_SET_EVENT_MASK"></a>

<a id="hci__if_8h_1a06eea836ef189c391ba8e0b5d6482321"></a> BTIF\_HCI\_SET\_EVENT\_MASK
:   CONTROLLER \& BASEBAND CMD.

<a id="c.BTIF_HCI_RESET"></a>

<a id="hci__if_8h_1a30d3329380fd02c6c0b233f9cf63c7d7"></a> BTIF\_HCI\_RESET

<a id="c.BTIF_HCI_SET_FILTER"></a>

<a id="hci__if_8h_1ab6a20b42b57eeb850c3e4c5884a87a2f"></a> BTIF\_HCI\_SET\_FILTER

<a id="c.BTIF_HCI_WRITE_LOCAL_NAME"></a>

<a id="hci__if_8h_1a449ad2ea88e9ab554240458cac100edf"></a> BTIF\_HCI\_WRITE\_LOCAL\_NAME

<a id="c.BTIF_HCI_READ_CONN_ACCEPT_TO"></a>

<a id="hci__if_8h_1ad584171abe6426ffb1b05676bb6c0232"></a> BTIF\_HCI\_READ\_CONN\_ACCEPT\_TO

<a id="c.BTIF_HCI_WRITE_CONN_ACCEPT_TO"></a>

<a id="hci__if_8h_1a37cb2457a5f40b5893ec77b8393ed5d1"></a> BTIF\_HCI\_WRITE\_CONN\_ACCEPT\_TO

<a id="c.BTIF_HCI_WRITE_PAGE_TO"></a>

<a id="hci__if_8h_1ac3be0618d99fb86585dda15b66b29595"></a> BTIF\_HCI\_WRITE\_PAGE\_TO

<a id="c.BTIF_HCI_READ_SCAN_ENABLE"></a>

<a id="hci__if_8h_1a7009d89fb1baacf8cf938f1fb2c702b4"></a> BTIF\_HCI\_READ\_SCAN\_ENABLE

<a id="c.BTIF_HCI_WRITE_SCAN_ENABLE"></a>

<a id="hci__if_8h_1a24709be2e5144510b08a0ad856ec09da"></a> BTIF\_HCI\_WRITE\_SCAN\_ENABLE

<a id="c.BTIF_HCI_WRITE_PSCAN_ACT"></a>

<a id="hci__if_8h_1a0298b51bfb2d7a02f400d6c9c010deec"></a> BTIF\_HCI\_WRITE\_PSCAN\_ACT

<a id="c.BTIF_HCI_WRITE_ISCAN_ACT"></a>

<a id="hci__if_8h_1aa6f2947de02b21290017bb194d060af8"></a> BTIF\_HCI\_WRITE\_ISCAN\_ACT

<a id="c.BTIF_HCI_WRITE_COD"></a>

<a id="hci__if_8h_1a395dba1e3abfb9457cd986ec5ca2cb10"></a> BTIF\_HCI\_WRITE\_COD

<a id="c.BTIF_HCI_WRITE_VOICE_SETTING"></a>

<a id="hci__if_8h_1ab67dac46b0ed8ea945c4ff83986a4ee5"></a> BTIF\_HCI\_WRITE\_VOICE\_SETTING

<a id="c.BTIF_HCI_SET_BTC_TO_BTH_FC"></a>

<a id="hci__if_8h_1a677e40ad9524fee3dd50f1cbca032c8d"></a> BTIF\_HCI\_SET\_BTC\_TO\_BTH\_FC

<a id="c.BTIF_HCI_HOST_BUFFER_SIZE"></a>

<a id="hci__if_8h_1a79d1854dff8e770c650bf87694a0539e"></a> BTIF\_HCI\_HOST\_BUFFER\_SIZE

<a id="c.BTIF_HCI_HOST_NUM_OF_COMPLETE"></a>

<a id="hci__if_8h_1a49ddc6fc575db4eb59ffb6b6e2682765"></a> BTIF\_HCI\_HOST\_NUM\_OF\_COMPLETE

<a id="c.BTIF_HCI_WRITE_LINK_STO"></a>

<a id="hci__if_8h_1a1af6a433ae7c03f5d913da13b8f367b9"></a> BTIF\_HCI\_WRITE\_LINK\_STO

<a id="c.BTIF_HCI_WRITE_IAC_LAP"></a>

<a id="hci__if_8h_1aa36fc4950467f294c9505ac8e97e9dff"></a> BTIF\_HCI\_WRITE\_IAC\_LAP

<a id="c.BTIF_HCI_SET_AFH_HOST_CHAN_CLASS"></a>

<a id="hci__if_8h_1aef4cc68581df53d088949f0b284e1dc6"></a> BTIF\_HCI\_SET\_AFH\_HOST\_CHAN\_CLASS

<a id="c.BTIF_HCI_WRITE_ISCAN_TYPE"></a>

<a id="hci__if_8h_1a5710950df8d04abb2c5c5c178f99d2ac"></a> BTIF\_HCI\_WRITE\_ISCAN\_TYPE

<a id="c.BTIF_HCI_WRITE_INQ_MODE"></a>

<a id="hci__if_8h_1a222962943361beb70a41e2144db6224b"></a> BTIF\_HCI\_WRITE\_INQ\_MODE

<a id="c.BTIF_HCI_WRITE_PSCAN_TYPE"></a>

<a id="hci__if_8h_1a625c4e5ba1222b33b934ec4dd30b02de"></a> BTIF\_HCI\_WRITE\_PSCAN\_TYPE

<a id="c.BTIF_HCI_WRITE_AFH_CH_ASSESS_MODE"></a>

<a id="hci__if_8h_1accceceae2e71b21e4e15c4309bc4bcb7"></a> BTIF\_HCI\_WRITE\_AFH\_CH\_ASSESS\_MODE

<a id="c.BTIF_HCI_WRITE_EXTENDED_INQ_RSP"></a>

<a id="hci__if_8h_1a09875c5873690a1cd6bc11d239eef483"></a> BTIF\_HCI\_WRITE\_EXTENDED\_INQ\_RSP

<a id="c.BTIF_HCI_WRITE_SIMPLE_PAIRING_MODE"></a>

<a id="hci__if_8h_1aaf43677b155725620b9f4711a44b8006"></a> BTIF\_HCI\_WRITE\_SIMPLE\_PAIRING\_MODE

<a id="c.BTIF_HCI_SET_EVENT_MASK_PAGE_2"></a>

<a id="hci__if_8h_1aff86cd8133fab358dcf4b4cc9e366c3c"></a> BTIF\_HCI\_SET\_EVENT\_MASK\_PAGE\_2

<a id="c.BTIF_HCI_WRITE_FLOW_CONTROL_MODE"></a>

<a id="hci__if_8h_1ae0bb68b9e920f5986e13de1e34dce52d"></a> BTIF\_HCI\_WRITE\_FLOW\_CONTROL\_MODE

<a id="c.BTIF_HCI_WRITE_LE_HOST_SUPPORT"></a>

<a id="hci__if_8h_1aee622e4e9e50760905d308b70e03ab72"></a> BTIF\_HCI\_WRITE\_LE\_HOST\_SUPPORT

<a id="c.BTIF_HCI_WRITE_SC_HOST_SUPPORTED"></a>

<a id="hci__if_8h_1a0b2ef6845097ffde3339621d7340c805"></a> BTIF\_HCI\_WRITE\_SC\_HOST\_SUPPORTED

<a id="c.BTIF_HCI_READ_LOCAL_VER_INFO"></a>

<a id="hci__if_8h_1a2f7b803e5ac52ef1fc3faa54946a2ab8"></a> BTIF\_HCI\_READ\_LOCAL\_VER\_INFO
:   INFO CMD.

<a id="c.BTIF_HCI_READ_LOCAL_SUPPORTED_COMMANDS"></a>

<a id="hci__if_8h_1af03d0c8d49908d5be164e96d344eb2f0"></a> BTIF\_HCI\_READ\_LOCAL\_SUPPORTED\_COMMANDS

<a id="c.BTIF_HCI_READ_LOCAL_SUPPORTED_FEATURES"></a>

<a id="hci__if_8h_1addebcc600349a871d662eb0ade0dacff"></a> BTIF\_HCI\_READ\_LOCAL\_SUPPORTED\_FEATURES

<a id="c.BTIF_HCI_READ_LOCAL_EXT_FEATURES"></a>

<a id="hci__if_8h_1ae3c077720fb82f5810e4ddc703a6c51c"></a> BTIF\_HCI\_READ\_LOCAL\_EXT\_FEATURES

<a id="c.BTIF_HCI_READ_BUFFER_SIZE"></a>

<a id="hci__if_8h_1a69333fb70893ff06e808eeff5e65d0ba"></a> BTIF\_HCI\_READ\_BUFFER\_SIZE

<a id="c.BTIF_HCI_READ_LOCAL_ADDR"></a>

<a id="hci__if_8h_1a5623d2fcf9c52cf63e35a19db3b38dbd"></a> BTIF\_HCI\_READ\_LOCAL\_ADDR

<a id="c.BTIF_HCI_LE_SET_EVT_MASK_CMD"></a>

<a id="hci__if_8h_1ae0105f36652aa156b5dfc2cf4a6d1117"></a> BTIF\_HCI\_LE\_SET\_EVT\_MASK\_CMD
:   BLE CMD.

<a id="c.BTIF_HCI_LE_RD_BUF_SIZE_CMD"></a>

<a id="hci__if_8h_1a3f07a2f493b0152f8822e52fe8b697cd"></a> BTIF\_HCI\_LE\_RD\_BUF\_SIZE\_CMD

<a id="c.BTIF_HCI_LE_RD_LOCAL_SUPP_FEATS_CMD"></a>

<a id="hci__if_8h_1a157bb50dea22d787ef2d2eaf1cb255f2"></a> BTIF\_HCI\_LE\_RD\_LOCAL\_SUPP\_FEATS\_CMD

<a id="c.BTIF_HCI_LE_SET_RAND_ADDR_CMD"></a>

<a id="hci__if_8h_1afc383f9bfaeb79bc2c2b27b97ed76203"></a> BTIF\_HCI\_LE\_SET\_RAND\_ADDR\_CMD

<a id="c.BTIF_HCI_LE_SET_ADV_PARAM_CMD"></a>

<a id="hci__if_8h_1a3080636838d6a0808ff10fdbc8b47835"></a> BTIF\_HCI\_LE\_SET\_ADV\_PARAM\_CMD

<a id="c.BTIF_HCI_LE_RD_ADV_CHNL_TX_PW_CMD"></a>

<a id="hci__if_8h_1a11f8205676befd44656188dfca7cb0e9"></a> BTIF\_HCI\_LE\_RD\_ADV\_CHNL\_TX\_PW\_CMD

<a id="c.BTIF_HCI_LE_SET_ADV_DATA_CMD"></a>

<a id="hci__if_8h_1a320eab40a8a1e3033ccc6b44b2e13bce"></a> BTIF\_HCI\_LE\_SET\_ADV\_DATA\_CMD

<a id="c.BTIF_HCI_LE_SET_SCAN_RSP_DATA_CMD"></a>

<a id="hci__if_8h_1a716c7312a6b1206c384e83270c80c827"></a> BTIF\_HCI\_LE\_SET\_SCAN\_RSP\_DATA\_CMD

<a id="c.BTIF_HCI_LE_SET_ADV_EN_CMD"></a>

<a id="hci__if_8h_1ac24e7bf874b0e78815fe394a4aa128cf"></a> BTIF\_HCI\_LE\_SET\_ADV\_EN\_CMD

<a id="c.BTIF_HCI_LE_SET_SCAN_PARAM_CMD"></a>

<a id="hci__if_8h_1a0f9b63f7da45fdaed4766a2557d86f17"></a> BTIF\_HCI\_LE\_SET\_SCAN\_PARAM\_CMD

<a id="c.BTIF_HCI_LE_SET_SCAN_EN_CMD"></a>

<a id="hci__if_8h_1a943b8fae5dfbae591615317eb8d052ba"></a> BTIF\_HCI\_LE\_SET\_SCAN\_EN\_CMD

<a id="c.BTIF_HCI_LE_CREATE_CON_CMD"></a>

<a id="hci__if_8h_1aa04e7cb29ec6bcf66979300d531eafce"></a> BTIF\_HCI\_LE\_CREATE\_CON\_CMD

<a id="c.BTIF_HCI_LE_CREATE_CON_CANCEL_CMD"></a>

<a id="hci__if_8h_1ae6e8995794ecc2d8c9feaa132b887bb9"></a> BTIF\_HCI\_LE\_CREATE\_CON\_CANCEL\_CMD

<a id="c.BTIF_HCI_LE_RD_FAL_SIZE_CMD"></a>

<a id="hci__if_8h_1a32da62ea37ccf05a9fcdd34d40346fb4"></a> BTIF\_HCI\_LE\_RD\_FAL\_SIZE\_CMD

<a id="c.BTIF_HCI_LE_CLEAR_FAL_CMD"></a>

<a id="hci__if_8h_1a0cf0524e219c5854f701ac1ed66e307f"></a> BTIF\_HCI\_LE\_CLEAR\_FAL\_CMD

<a id="c.BTIF_HCI_LE_ADD_DEV_TO_FAL_CMD"></a>

<a id="hci__if_8h_1ada95a9459707fd7a9c01221b3d5bf2ea"></a> BTIF\_HCI\_LE\_ADD\_DEV\_TO\_FAL\_CMD

<a id="c.BTIF_HCI_LE_RMV_DEV_FROM_FAL_CMD"></a>

<a id="hci__if_8h_1a819673967b71e855fe1a5bea792e4aba"></a> BTIF\_HCI\_LE\_RMV\_DEV\_FROM\_FAL\_CMD

<a id="c.BTIF_HCI_LE_CON_UPDATE_CMD"></a>

<a id="hci__if_8h_1a5f8f1ac0e0976ac59f26339e4dd99912"></a> BTIF\_HCI\_LE\_CON\_UPDATE\_CMD

<a id="c.BTIF_HCI_LE_SET_HOST_CH_CLASS_CMD"></a>

<a id="hci__if_8h_1aae45ed1c179c26ecf0038b13a4deaa5d"></a> BTIF\_HCI\_LE\_SET\_HOST\_CH\_CLASS\_CMD

<a id="c.BTIF_HCI_LE_RD_CHNL_MAP_CMD"></a>

<a id="hci__if_8h_1ac887c0db5ea3dab7d25c6c52515af83e"></a> BTIF\_HCI\_LE\_RD\_CHNL\_MAP\_CMD

<a id="c.BTIF_HCI_LE_RD_REM_FEATS_CMD"></a>

<a id="hci__if_8h_1af1d2740f24f4a91a9bfebf0ef4a59a48"></a> BTIF\_HCI\_LE\_RD\_REM\_FEATS\_CMD

<a id="c.BTIF_HCI_LE_ENC_CMD"></a>

<a id="hci__if_8h_1a0f9325cd7be2f440e7c67fb433b15e78"></a> BTIF\_HCI\_LE\_ENC\_CMD

<a id="c.BTIF_HCI_LE_RAND_CMD"></a>

<a id="hci__if_8h_1a825f14dfb6407c8772a440db7ae9d8e7"></a> BTIF\_HCI\_LE\_RAND\_CMD

<a id="c.BTIF_HCI_LE_EN_ENC_CMD"></a>

<a id="hci__if_8h_1a403b3e71349fd61c2245e44e661e90d4"></a> BTIF\_HCI\_LE\_EN\_ENC\_CMD

<a id="c.BTIF_HCI_LE_LTK_REQ_REPLY_CMD"></a>

<a id="hci__if_8h_1a8ee2282ce31dc2ba3d11fb2d24fb5af3"></a> BTIF\_HCI\_LE\_LTK\_REQ\_REPLY\_CMD

<a id="c.BTIF_HCI_LE_LTK_REQ_NEG_REPLY_CMD"></a>

<a id="hci__if_8h_1ade4dadec9c49d759fe737a448eff4f98"></a> BTIF\_HCI\_LE\_LTK\_REQ\_NEG\_REPLY\_CMD

<a id="c.BTIF_HCI_LE_RD_SUPP_STATES_CMD"></a>

<a id="hci__if_8h_1a4f722d5c4e64243ee1f217674a99232a"></a> BTIF\_HCI\_LE\_RD\_SUPP\_STATES\_CMD

<a id="c.BTIF_HCI_LE_RX_TEST_V1_CMD"></a>

<a id="hci__if_8h_1a91ae9ce675a16f85e7becd76cc2a0baa"></a> BTIF\_HCI\_LE\_RX\_TEST\_V1\_CMD

<a id="c.BTIF_HCI_LE_TX_TEST_V1_CMD"></a>

<a id="hci__if_8h_1aff5663df82180861700fcf66a61a1b40"></a> BTIF\_HCI\_LE\_TX\_TEST\_V1\_CMD

<a id="c.BTIF_HCI_LE_TEST_END_CMD"></a>

<a id="hci__if_8h_1a6a37922ed0ce317b98a848910dd9b971"></a> BTIF\_HCI\_LE\_TEST\_END\_CMD

<a id="c.BTIF_HCI_LE_REM_CON_PARAM_REQ_REPLY_CMD"></a>

<a id="hci__if_8h_1ab7d0e5ae804927db14bdd49101f02d9e"></a> BTIF\_HCI\_LE\_REM\_CON\_PARAM\_REQ\_REPLY\_CMD

<a id="c.BTIF_HCI_LE_REM_CON_PARAM_REQ_NEG_REPLY_CMD"></a>

<a id="hci__if_8h_1a2290df7f9f9ab3ef57182032bec3bbbf"></a> BTIF\_HCI\_LE\_REM\_CON\_PARAM\_REQ\_NEG\_REPLY\_CMD

<a id="c.BTIF_HCI_LE_SET_DATA_LEN_CMD"></a>

<a id="hci__if_8h_1aeb186a5fe2e38cc9d051e3a172f4e5b9"></a> BTIF\_HCI\_LE\_SET\_DATA\_LEN\_CMD

<a id="c.BTIF_HCI_LE_RD_SUGGTED_DFT_DATA_LEN_CMD"></a>

<a id="hci__if_8h_1a07b47e1caa2ffa04e39d1836f432658f"></a> BTIF\_HCI\_LE\_RD\_SUGGTED\_DFT\_DATA\_LEN\_CMD

<a id="c.BTIF_HCI_LE_WR_SUGGTED_DFT_DATA_LEN_CMD"></a>

<a id="hci__if_8h_1a57d6d1bd6325e62ed0197305d653bbd7"></a> BTIF\_HCI\_LE\_WR\_SUGGTED\_DFT\_DATA\_LEN\_CMD

<a id="c.BTIF_HCI_LE_RD_LOC_P256_PUB_KEY_CMD"></a>

<a id="hci__if_8h_1ab94fdff0a80a7fe7404578c9c8ba52cd"></a> BTIF\_HCI\_LE\_RD\_LOC\_P256\_PUB\_KEY\_CMD

<a id="c.BTIF_HCI_LE_GEN_DHKEY_V1_CMD"></a>

<a id="hci__if_8h_1aed3a140edf3da149b29c21ae272c0af9"></a> BTIF\_HCI\_LE\_GEN\_DHKEY\_V1\_CMD

<a id="c.BTIF_HCI_LE_ADD_DEV_TO_RSLV_LIST_CMD"></a>

<a id="hci__if_8h_1ad47067bca168b45cec333e865a746b6b"></a> BTIF\_HCI\_LE\_ADD\_DEV\_TO\_RSLV\_LIST\_CMD

<a id="c.BTIF_HCI_LE_RMV_DEV_FROM_RSLV_LIST_CMD"></a>

<a id="hci__if_8h_1a2d5276255b8a6755f6784da90cb3cced"></a> BTIF\_HCI\_LE\_RMV\_DEV\_FROM\_RSLV\_LIST\_CMD

<a id="c.BTIF_HCI_LE_CLEAR_RSLV_LIST_CMD"></a>

<a id="hci__if_8h_1adea57d328e1bb1285f92ef8e354c43ff"></a> BTIF\_HCI\_LE\_CLEAR\_RSLV\_LIST\_CMD

<a id="c.BTIF_HCI_LE_RD_RSLV_LIST_SIZE_CMD"></a>

<a id="hci__if_8h_1aa2055e2cf41292fd3bb083240cd60ae6"></a> BTIF\_HCI\_LE\_RD\_RSLV\_LIST\_SIZE\_CMD

<a id="c.BTIF_HCI_LE_RD_PEER_RSLV_ADDR_CMD"></a>

<a id="hci__if_8h_1a4b8361154733d9bf7847109fbe1cd19a"></a> BTIF\_HCI\_LE\_RD\_PEER\_RSLV\_ADDR\_CMD

<a id="c.BTIF_HCI_LE_RD_LOC_RSLV_ADDR_CMD"></a>

<a id="hci__if_8h_1ac96249122912078f9183ef4cd02582fc"></a> BTIF\_HCI\_LE\_RD\_LOC\_RSLV\_ADDR\_CMD

<a id="c.BTIF_HCI_LE_SET_ADDR_RESOL_EN_CMD"></a>

<a id="hci__if_8h_1aed325560f77611f7442cb0504485d20d"></a> BTIF\_HCI\_LE\_SET\_ADDR\_RESOL\_EN\_CMD

<a id="c.BTIF_HCI_LE_SET_RSLV_PRIV_ADDR_TO_CMD"></a>

<a id="hci__if_8h_1ae85916749572a52ac4aa196aa6bee286"></a> BTIF\_HCI\_LE\_SET\_RSLV\_PRIV\_ADDR\_TO\_CMD

<a id="c.BTIF_HCI_LE_RD_MAX_DATA_LEN_CMD"></a>

<a id="hci__if_8h_1aca9e070e8790b6abd7c826f6901dded1"></a> BTIF\_HCI\_LE\_RD\_MAX\_DATA\_LEN\_CMD

<a id="c.BTIF_HCI_LE_RD_PHY_CMD"></a>

<a id="hci__if_8h_1a008adc05b5f508c7346dddd68f4f314a"></a> BTIF\_HCI\_LE\_RD\_PHY\_CMD

<a id="c.BTIF_HCI_LE_SET_DFT_PHY_CMD"></a>

<a id="hci__if_8h_1a2d15ef8007ae2118fc96476f66a4a600"></a> BTIF\_HCI\_LE\_SET\_DFT\_PHY\_CMD

<a id="c.BTIF_HCI_LE_SET_PHY_CMD"></a>

<a id="hci__if_8h_1a96aa5cec264c045b53494376f9c73935"></a> BTIF\_HCI\_LE\_SET\_PHY\_CMD

<a id="c.BTIF_HCI_LE_RX_TEST_V2_CMD"></a>

<a id="hci__if_8h_1a91d9d737c3950e4e3a0202d7ed99fa4a"></a> BTIF\_HCI\_LE\_RX\_TEST\_V2\_CMD

<a id="c.BTIF_HCI_LE_TX_TEST_V2_CMD"></a>

<a id="hci__if_8h_1ad9c162b4b2d15e6b6fb7f24e751359b4"></a> BTIF\_HCI\_LE\_TX\_TEST\_V2\_CMD

<a id="c.BTIF_HCI_LE_SET_ADV_SET_RAND_ADDR_CMD"></a>

<a id="hci__if_8h_1a0be72e97b4034c3f7b97771bf2943d40"></a> BTIF\_HCI\_LE\_SET\_ADV\_SET\_RAND\_ADDR\_CMD

<a id="c.BTIF_HCI_LE_SET_EXT_ADV_PARAM_CMD"></a>

<a id="hci__if_8h_1acbf0ca36dfef5c626409f10421f3c428"></a> BTIF\_HCI\_LE\_SET\_EXT\_ADV\_PARAM\_CMD

<a id="c.BTIF_HCI_LE_SET_EXT_ADV_DATA_CMD"></a>

<a id="hci__if_8h_1ab85b947076bcca3e53d3f72e6e1d5ad7"></a> BTIF\_HCI\_LE\_SET\_EXT\_ADV\_DATA\_CMD

<a id="c.BTIF_HCI_LE_SET_EXT_SCAN_RSP_DATA_CMD"></a>

<a id="hci__if_8h_1aa404c7af668ce65ba027a07d0e9ae13b"></a> BTIF\_HCI\_LE\_SET\_EXT\_SCAN\_RSP\_DATA\_CMD

<a id="c.BTIF_HCI_LE_SET_EXT_ADV_EN_CMD"></a>

<a id="hci__if_8h_1aa5b3d15d7462d2c9994698d5d44daab7"></a> BTIF\_HCI\_LE\_SET\_EXT\_ADV\_EN\_CMD

<a id="c.BTIF_HCI_LE_RD_MAX_ADV_DATA_LEN_CMD"></a>

<a id="hci__if_8h_1a9b6706a1e970281fe60372bae16abb68"></a> BTIF\_HCI\_LE\_RD\_MAX\_ADV\_DATA\_LEN\_CMD

<a id="c.BTIF_HCI_LE_RD_NB_SUPP_ADV_SETS_CMD"></a>

<a id="hci__if_8h_1a365c452924fdde2da659236f21a4d202"></a> BTIF\_HCI\_LE\_RD\_NB\_SUPP\_ADV\_SETS\_CMD

<a id="c.BTIF_HCI_LE_RMV_ADV_SET_CMD"></a>

<a id="hci__if_8h_1a4cab8fc629874dfbb7dcb88c01cb967c"></a> BTIF\_HCI\_LE\_RMV\_ADV\_SET\_CMD

<a id="c.BTIF_HCI_LE_CLEAR_ADV_SETS_CMD"></a>

<a id="hci__if_8h_1a4eb18379410ff8528a2d21de8913b16d"></a> BTIF\_HCI\_LE\_CLEAR\_ADV\_SETS\_CMD

<a id="c.BTIF_HCI_LE_SET_PER_ADV_PARAM_CMD"></a>

<a id="hci__if_8h_1a16c999208f7e16ec1908121514eb3feb"></a> BTIF\_HCI\_LE\_SET\_PER\_ADV\_PARAM\_CMD

<a id="c.BTIF_HCI_LE_SET_PER_ADV_DATA_CMD"></a>

<a id="hci__if_8h_1ad74350835b712d9e70f0269493fa99fd"></a> BTIF\_HCI\_LE\_SET\_PER\_ADV\_DATA\_CMD

<a id="c.BTIF_HCI_LE_SET_PER_ADV_EN_CMD"></a>

<a id="hci__if_8h_1a59fe88afe78c36479ca17dcd212fbdc6"></a> BTIF\_HCI\_LE\_SET\_PER\_ADV\_EN\_CMD

<a id="c.BTIF_HCI_LE_SET_EXT_SCAN_PARAM_CMD"></a>

<a id="hci__if_8h_1ab1324c1c05dba03a1ac5af7103223e3c"></a> BTIF\_HCI\_LE\_SET\_EXT\_SCAN\_PARAM\_CMD

<a id="c.BTIF_HCI_LE_SET_EXT_SCAN_EN_CMD"></a>

<a id="hci__if_8h_1a8f683219d01c6ba73c5a1e12fcca9f00"></a> BTIF\_HCI\_LE\_SET\_EXT\_SCAN\_EN\_CMD

<a id="c.BTIF_HCI_LE_EXT_CREATE_CON_CMD"></a>

<a id="hci__if_8h_1a5ffc1d7b4421b57ad4ff0cbff7f50e15"></a> BTIF\_HCI\_LE\_EXT\_CREATE\_CON\_CMD

<a id="c.BTIF_HCI_LE_PER_ADV_CREATE_SYNC_CMD"></a>

<a id="hci__if_8h_1ac0e044ffca762067c8569c967aec57a1"></a> BTIF\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CMD

<a id="c.BTIF_HCI_LE_PER_ADV_CREATE_SYNC_CANCEL_CMD"></a>

<a id="hci__if_8h_1af621b88693b30108450bd0f49ac78199"></a> BTIF\_HCI\_LE\_PER\_ADV\_CREATE\_SYNC\_CANCEL\_CMD

<a id="c.BTIF_HCI_LE_PER_ADV_TERM_SYNC_CMD"></a>

<a id="hci__if_8h_1a3333d6c0a1e544e5bfb2c5aa005c89e3"></a> BTIF\_HCI\_LE\_PER\_ADV\_TERM\_SYNC\_CMD

<a id="c.BTIF_HCI_LE_ADD_DEV_TO_PER_ADV_LIST_CMD"></a>

<a id="hci__if_8h_1a6beffe5b21a68b9716ff982da4ede3fe"></a> BTIF\_HCI\_LE\_ADD\_DEV\_TO\_PER\_ADV\_LIST\_CMD

<a id="c.BTIF_HCI_LE_RMV_DEV_FROM_PER_ADV_LIST_CMD"></a>

<a id="hci__if_8h_1aa6b8d4900fa720f0a5cf46ab87256d05"></a> BTIF\_HCI\_LE\_RMV\_DEV\_FROM\_PER\_ADV\_LIST\_CMD

<a id="c.BTIF_HCI_LE_CLEAR_PER_ADV_LIST_CMD"></a>

<a id="hci__if_8h_1a5476e50742d19f444c6c3f85e44c0b8e"></a> BTIF\_HCI\_LE\_CLEAR\_PER\_ADV\_LIST\_CMD

<a id="c.BTIF_HCI_LE_RD_PER_ADV_LIST_SIZE_CMD"></a>

<a id="hci__if_8h_1a956fe1940cb7bd4c40e4508b8ae93822"></a> BTIF\_HCI\_LE\_RD\_PER\_ADV\_LIST\_SIZE\_CMD

<a id="c.BTIF_HCI_LE_RD_TX_PWR_CMD"></a>

<a id="hci__if_8h_1aeb8b2bc28f2c096a6147c8e37ad3862a"></a> BTIF\_HCI\_LE\_RD\_TX\_PWR\_CMD

<a id="c.BTIF_HCI_LE_RD_RF_PATH_COMP_CMD"></a>

<a id="hci__if_8h_1a48d21b53316739c94fce559703081b13"></a> BTIF\_HCI\_LE\_RD\_RF\_PATH\_COMP\_CMD

<a id="c.BTIF_HCI_LE_WR_RF_PATH_COMP_CMD"></a>

<a id="hci__if_8h_1aa45f8679275ef9705b41eb04d2e1ec44"></a> BTIF\_HCI\_LE\_WR\_RF\_PATH\_COMP\_CMD

<a id="c.BTIF_HCI_LE_SET_PRIV_MODE_CMD"></a>

<a id="hci__if_8h_1a6c5d554eca9b4bfd06c952d995572a21"></a> BTIF\_HCI\_LE\_SET\_PRIV\_MODE\_CMD

<a id="c.BTIF_HCI_LE_RX_TEST_V3_CMD"></a>

<a id="hci__if_8h_1ae8c14d4d23967399b2ce8757a0ae8ca3"></a> BTIF\_HCI\_LE\_RX\_TEST\_V3\_CMD

<a id="c.BTIF_HCI_LE_TX_TEST_V3_CMD"></a>

<a id="hci__if_8h_1a3f19b2987d348f86447c77405f0d8be7"></a> BTIF\_HCI\_LE\_TX\_TEST\_V3\_CMD

<a id="c.BTIF_HCI_LE_SET_CONLESS_CTE_TX_PARAM_CMD"></a>

<a id="hci__if_8h_1a44736a1ec3a86218a574768d7da23e0b"></a> BTIF\_HCI\_LE\_SET\_CONLESS\_CTE\_TX\_PARAM\_CMD

<a id="c.BTIF_HCI_LE_SET_CONLESS_CTE_TX_EN_CMD"></a>

<a id="hci__if_8h_1a6825b9e3d12d60c30e24a4543e179bbc"></a> BTIF\_HCI\_LE\_SET\_CONLESS\_CTE\_TX\_EN\_CMD

<a id="c.BTIF_HCI_LE_SET_CONLESS_IQ_SAMPL_EN_CMD"></a>

<a id="hci__if_8h_1a37a81e9a0fb7cee5211d71de898617e0"></a> BTIF\_HCI\_LE\_SET\_CONLESS\_IQ\_SAMPL\_EN\_CMD

<a id="c.BTIF_HCI_LE_SET_CON_CTE_RX_PARAM_CMD"></a>

<a id="hci__if_8h_1ad03047762c4270e0cd3c4d0f10faff45"></a> BTIF\_HCI\_LE\_SET\_CON\_CTE\_RX\_PARAM\_CMD

<a id="c.BTIF_HCI_LE_SET_CON_CTE_TX_PARAM_CMD"></a>

<a id="hci__if_8h_1af0fc8a95298b6c0edec1395066a8cd4e"></a> BTIF\_HCI\_LE\_SET\_CON\_CTE\_TX\_PARAM\_CMD

<a id="c.BTIF_HCI_LE_CON_CTE_REQ_EN_CMD"></a>

<a id="hci__if_8h_1ae25e783715aebe85255bdd1fe55d691a"></a> BTIF\_HCI\_LE\_CON\_CTE\_REQ\_EN\_CMD

<a id="c.BTIF_HCI_LE_CON_CTE_RSP_EN_CMD"></a>

<a id="hci__if_8h_1a711c4d69316ff6cdd328945b997f1264"></a> BTIF\_HCI\_LE\_CON\_CTE\_RSP\_EN\_CMD

<a id="c.BTIF_HCI_LE_RD_ANTENNA_INF_CMD"></a>

<a id="hci__if_8h_1a0328b36ed9c883fc8d93ee8c9732d752"></a> BTIF\_HCI\_LE\_RD\_ANTENNA\_INF\_CMD

<a id="c.BTIF_HCI_LE_SET_PER_ADV_REC_EN_CMD"></a>

<a id="hci__if_8h_1ac76233ae41baf4bdba059c04c2019ea2"></a> BTIF\_HCI\_LE\_SET\_PER\_ADV\_REC\_EN\_CMD

<a id="c.BTIF_HCI_LE_PER_ADV_SYNC_TRANSF_CMD"></a>

<a id="hci__if_8h_1a1f381a5fe78b141ade939fe66d020e63"></a> BTIF\_HCI\_LE\_PER\_ADV\_SYNC\_TRANSF\_CMD

<a id="c.BTIF_HCI_LE_PER_ADV_SET_INFO_TRANSF_CMD"></a>

<a id="hci__if_8h_1ae765c8d9826acf999d354c99aa0c6e56"></a> BTIF\_HCI\_LE\_PER\_ADV\_SET\_INFO\_TRANSF\_CMD

<a id="c.BTIF_HCI_LE_SET_PER_ADV_SYNC_TRANSF_PARAM_CMD"></a>

<a id="hci__if_8h_1a25d5356c453397eb8a2fb42b6cb29e3d"></a> BTIF\_HCI\_LE\_SET\_PER\_ADV\_SYNC\_TRANSF\_PARAM\_CMD

<a id="c.BTIF_HCI_LE_SET_DFT_PER_ADV_SYNC_TRANSF_PARAM_CMD"></a>

<a id="hci__if_8h_1ad9d1ca1eb41bb3e491a843783566f89e"></a> BTIF\_HCI\_LE\_SET\_DFT\_PER\_ADV\_SYNC\_TRANSF\_PARAM\_CMD

<a id="c.BTIF_HCI_LE_GEN_DHKEY_V2_CMD"></a>

<a id="hci__if_8h_1aef9f4b38fa55fb6d9f72246b5f855bd7"></a> BTIF\_HCI\_LE\_GEN\_DHKEY\_V2\_CMD

<a id="c.BTIF_HCI_LE_MOD_SLEEP_CLK_ACC_CMD"></a>

<a id="hci__if_8h_1a1a6f5d74794743b711fa8f8b820a389b"></a> BTIF\_HCI\_LE\_MOD\_SLEEP\_CLK\_ACC\_CMD

<a id="c.BTIF_HCI_LE_RD_BUF_SIZE_V2_CMD"></a>

<a id="hci__if_8h_1a02d651ff1d30e9ba1cc059177d6dcc6b"></a> BTIF\_HCI\_LE\_RD\_BUF\_SIZE\_V2\_CMD

<a id="c.BTIF_HCI_LE_RD_ISO_TX_SYNC_CMD"></a>

<a id="hci__if_8h_1afa645e9951980f90b4198c695d34bc3d"></a> BTIF\_HCI\_LE\_RD\_ISO\_TX\_SYNC\_CMD

<a id="c.BTIF_HCI_LE_SET_CIG_PARAMS_CMD"></a>

<a id="hci__if_8h_1adccf187833e0d45326e8603ccaebd9d4"></a> BTIF\_HCI\_LE\_SET\_CIG\_PARAMS\_CMD

<a id="c.BTIF_HCI_LE_SET_CIG_PARAMS_TEST_CMD"></a>

<a id="hci__if_8h_1aa266ad8c03c9ff8e66bec8172a0ab6a9"></a> BTIF\_HCI\_LE\_SET\_CIG\_PARAMS\_TEST\_CMD

<a id="c.BTIF_HCI_LE_CREATE_CIS_CMD"></a>

<a id="hci__if_8h_1a04ece06384483823b01ffccbb00f6006"></a> BTIF\_HCI\_LE\_CREATE\_CIS\_CMD

<a id="c.BTIF_HCI_LE_REMOVE_CIG_CMD"></a>

<a id="hci__if_8h_1a2edc7bdd420e8f39550692e2556730fb"></a> BTIF\_HCI\_LE\_REMOVE\_CIG\_CMD

<a id="c.BTIF_HCI_LE_ACCEPT_CIS_REQ_CMD"></a>

<a id="hci__if_8h_1a7b7c61038cfe768f56fd0fa0ba881dec"></a> BTIF\_HCI\_LE\_ACCEPT\_CIS\_REQ\_CMD

<a id="c.BTIF_HCI_LE_REJECT_CIS_REQ_CMD"></a>

<a id="hci__if_8h_1a56b9d50d3fee1aaa1786ac0de24e893a"></a> BTIF\_HCI\_LE\_REJECT\_CIS\_REQ\_CMD

<a id="c.BTIF_HCI_LE_CREATE_BIG_CMD"></a>

<a id="hci__if_8h_1a60ee4777d92e4e5e1271ac93746967a6"></a> BTIF\_HCI\_LE\_CREATE\_BIG\_CMD

<a id="c.BTIF_HCI_LE_CREATE_BIG_TEST_CMD"></a>

<a id="hci__if_8h_1a170188a2151addec58a977cb05f26ece"></a> BTIF\_HCI\_LE\_CREATE\_BIG\_TEST\_CMD

<a id="c.BTIF_HCI_LE_TERMINATE_BIG_CMD"></a>

<a id="hci__if_8h_1aa3e42327e020ae5bf112d11485a96d19"></a> BTIF\_HCI\_LE\_TERMINATE\_BIG\_CMD

<a id="c.BTIF_HCI_LE_BIG_CREATE_SYNC_CMD"></a>

<a id="hci__if_8h_1a341d0e9d9f680d4eb9dbc7b8bed851b4"></a> BTIF\_HCI\_LE\_BIG\_CREATE\_SYNC\_CMD

<a id="c.BTIF_HCI_LE_BIG_TERMINATE_SYNC_CMD"></a>

<a id="hci__if_8h_1a9c7e7ee6338c0b96eebc07bf3f2755d1"></a> BTIF\_HCI\_LE\_BIG\_TERMINATE\_SYNC\_CMD

<a id="c.BTIF_HCI_LE_REQ_PEER_SCA_CMD"></a>

<a id="hci__if_8h_1a33f01194d5bbe1023451f11d8a01f162"></a> BTIF\_HCI\_LE\_REQ\_PEER\_SCA\_CMD

<a id="c.BTIF_HCI_LE_SETUP_ISO_DATA_PATH_CMD"></a>

<a id="hci__if_8h_1a5b750306fc73fb775c176d16c543c5f4"></a> BTIF\_HCI\_LE\_SETUP\_ISO\_DATA\_PATH\_CMD

<a id="c.BTIF_HCI_LE_REMOVE_ISO_DATA_PATH_CMD"></a>

<a id="hci__if_8h_1a101b666bd9e87a303256fcf39b1c84f1"></a> BTIF\_HCI\_LE\_REMOVE\_ISO\_DATA\_PATH\_CMD

<a id="c.BTIF_HCI_LE_ISO_TX_TEST_CMD"></a>

<a id="hci__if_8h_1a4aa42f11a227f56b7ac78086bf9ad207"></a> BTIF\_HCI\_LE\_ISO\_TX\_TEST\_CMD

<a id="c.BTIF_HCI_LE_ISO_RX_TEST_CMD"></a>

<a id="hci__if_8h_1a3a972bb371202620fd10299eec7488bc"></a> BTIF\_HCI\_LE\_ISO\_RX\_TEST\_CMD

<a id="c.BTIF_HCI_LE_ISO_READ_TEST_COUNTERS_CMD"></a>

<a id="hci__if_8h_1afe8cc8bac54f124978eb08a7c4fa91bf"></a> BTIF\_HCI\_LE\_ISO\_READ\_TEST\_COUNTERS\_CMD

<a id="c.BTIF_HCI_LE_ISO_TEST_END_CMD"></a>

<a id="hci__if_8h_1ab92bf582a8b02937947e1e7e15bf2918"></a> BTIF\_HCI\_LE\_ISO\_TEST\_END\_CMD

<a id="c.BTIF_HCI_LE_SET_HOST_FEATURE_CMD"></a>

<a id="hci__if_8h_1a9f5bf0bbb5a515a7275c5ee114e96f7a"></a> BTIF\_HCI\_LE\_SET\_HOST\_FEATURE\_CMD

<a id="c.BTIF_HCI_LE_RD_ISO_LINK_QUALITY_CMD"></a>

<a id="hci__if_8h_1a62a57bf92ebcaeea0858b6a451d00d28"></a> BTIF\_HCI\_LE\_RD\_ISO\_LINK\_QUALITY\_CMD

<a id="c.BTIF_HCI_LE_ENH_RD_TX_PWR_LVL_CMD"></a>

<a id="hci__if_8h_1a6f5f9aa510a1c60f8f598cccdf803dae"></a> BTIF\_HCI\_LE\_ENH\_RD\_TX\_PWR\_LVL\_CMD

<a id="c.BTIF_HCI_LE_RD_REMOTE_TX_PWR_LVL_CMD"></a>

<a id="hci__if_8h_1a97806fb3a5c028ec1c202c54e9454742"></a> BTIF\_HCI\_LE\_RD\_REMOTE\_TX\_PWR\_LVL\_CMD

<a id="c.BTIF_HCI_LE_SET_PATH_LOSS_REP_PARAM_CMD"></a>

<a id="hci__if_8h_1a5788244b59819dcecadc0129c3de44f4"></a> BTIF\_HCI\_LE\_SET\_PATH\_LOSS\_REP\_PARAM\_CMD

<a id="c.BTIF_HCI_LE_SET_PATH_LOSS_REP_EN_CMD"></a>

<a id="hci__if_8h_1a5fa038a8d1a0e240213dc9b748652690"></a> BTIF\_HCI\_LE\_SET\_PATH\_LOSS\_REP\_EN\_CMD

<a id="c.BTIF_HCI_LE_SET_TX_POWER_REP_EN_CMD"></a>

<a id="hci__if_8h_1ab66087bb56df55e925b327813862c518"></a> BTIF\_HCI\_LE\_SET\_TX\_POWER\_REP\_EN\_CMD

<a id="c.BTIF_HCI_LE_TX_TEST_V4_CMD"></a>

<a id="hci__if_8h_1a362634b96a23c698bfc9b9fd3fa41c86"></a> BTIF\_HCI\_LE\_TX\_TEST\_V4\_CMD

<a id="c.BTIF_HCI_VS_SET_BD_ADDR_CMD_OPCODE"></a>

<a id="hci__if_8h_1a8315d639fba1466d1e1ba1ef2b803533"></a> BTIF\_HCI\_VS\_SET\_BD\_ADDR\_CMD\_OPCODE
:   BEKEN private HCI command defintion.

<a id="c.HCI_VS_SET_PREF_SLAVE_EVT_DUR_CMD_OPCODE"></a>

<a id="hci__if_8h_1ac0713897c05c9369a76f6997dd36b31b"></a> HCI\_VS\_SET\_PREF\_SLAVE\_EVT\_DUR\_CMD\_OPCODE

<a id="c.BTIF_HCI_VS_SET_LE_BD_ADDR_CMD_OPCODE"></a>

<a id="hci__if_8h_1a55973b21490dd82b7c7d30e605d2a1d4"></a> BTIF\_HCI\_VS\_SET\_LE\_BD\_ADDR\_CMD\_OPCODE

<a id="c.BTIF_HCI_VS_CONFIG_BT_FEATURE_CMD_OPCODE"></a>

<a id="hci__if_8h_1a4d971c8c24f99cd25be92d8c808b5efa"></a> BTIF\_HCI\_VS\_CONFIG\_BT\_FEATURE\_CMD\_OPCODE

<a id="c.BTIF_HCI_SET_VENDOR_FEATURE_CMD_OPCODE"></a>

<a id="hci__if_8h_1add48619000e62b647d512e7c9a1edd80"></a> BTIF\_HCI\_SET\_VENDOR\_FEATURE\_CMD\_OPCODE

<a id="c.BTIF_HCI_SET_SPI_WR_RF_REGIST_CMD_OPCODE"></a>

<a id="hci__if_8h_1ace8620b856693d4db6346bf76d595bf8"></a> BTIF\_HCI\_SET\_SPI\_WR\_RF\_REGIST\_CMD\_OPCODE

<a id="c.BTIF_HCI_VS_SET_SYNC_CONN_EN_CMD_OPCODE"></a>

<a id="hci__if_8h_1a041ac1bb81f46af81e4a9c83dd7740b2"></a> BTIF\_HCI\_VS\_SET\_SYNC\_CONN\_EN\_CMD\_OPCODE

<a id="c.BTIF_HCI_START_SNOOP_CMD"></a>

<a id="hci__if_8h_1af1f9d27a0eef429557303c6748b7b231"></a> BTIF\_HCI\_START\_SNOOP\_CMD

<a id="c.BTIF_HCI_TWS_INIT_CMD"></a>

<a id="hci__if_8h_1ac56264596d75dcb796a39a3391e2f61f"></a> BTIF\_HCI\_TWS\_INIT\_CMD

<a id="c.BTIF_HCI_TWS_STOP_SNOOP_CMD"></a>

<a id="hci__if_8h_1aba1308c4b54fcfb21df18f1af9f99322"></a> BTIF\_HCI\_TWS\_STOP\_SNOOP\_CMD

<a id="c.BTIF_HCI_TWS_SWITCH_CMD"></a>

<a id="hci__if_8h_1a86db5f3fe4b95a516f16170d786fb9c8"></a> BTIF\_HCI\_TWS\_SWITCH\_CMD

<a id="c.BTIF_HCI_TWS_SCH_CMD"></a>

<a id="hci__if_8h_1a01b736809ca7c1bc1acd4d6ef56ec561"></a> BTIF\_HCI\_TWS\_SCH\_CMD

<a id="c.BTIF_HCI_TWS_AUDIO_SYNC_CMD"></a>

<a id="hci__if_8h_1a46323d51150f6c656e286bd9cad7d68d"></a> BTIF\_HCI\_TWS\_AUDIO\_SYNC\_CMD

<a id="c.BTIF_HCI_VS_SET_LINK_PROFILE_CMD_OPCODE"></a>

<a id="hci__if_8h_1aa8587d5a3b87a0bab5611e8f00bbea6b"></a> BTIF\_HCI\_VS\_SET\_LINK\_PROFILE\_CMD\_OPCODE

<a id="c.BTIF_HCI_VS_USER_SLEEP_CTRL_CMD_OPCODE"></a>

<a id="hci__if_8h_1a36d9a133afc2885b7550950979640019"></a> BTIF\_HCI\_VS\_USER\_SLEEP\_CTRL\_CMD\_OPCODE

<a id="c.BTIF_HCI_VS_USER_EVENT_CTRL_CMD_OPCODE"></a>

<a id="hci__if_8h_1ad3579f181ac2a6da78987ff681324c98"></a> BTIF\_HCI\_VS\_USER\_EVENT\_CTRL\_CMD\_OPCODE

<a id="c.BTIF_HCI_VS_SET_CTUNE_CMD_OPCODE"></a>

<a id="hci__if_8h_1a36862656d841575dd8c44b977a7a31cc"></a> BTIF\_HCI\_VS\_SET\_CTUNE\_CMD\_OPCODE

<a id="c.BTIF_HCI_VS_SET_TX_PWR_LVL_CMD_OPCODE"></a>

<a id="hci__if_8h_1a155c1888acb34c4096e1275594386bc6"></a> BTIF\_HCI\_VS\_SET\_TX\_PWR\_LVL\_CMD\_OPCODE

<a id="c.BTIF_HCI_PROFILE_TYPE_A2DP_SNK"></a>

<a id="hci__if_8h_1a990b3e491c0df87446f802e6d66d42b5"></a> BTIF\_HCI\_PROFILE\_TYPE\_A2DP\_SNK

<a id="c.BTIF_HCI_PROFILE_TYPE_A2DP_SRC"></a>

<a id="hci__if_8h_1a542f3925c00951ea51f8697484a9965a"></a> BTIF\_HCI\_PROFILE\_TYPE\_A2DP\_SRC

<a id="c.BTIF_HCI_PROFILE_TYPE_A2DP_OOP_SNK"></a>

<a id="hci__if_8h_1ac673da3f1b71143ccd70f75699004c01"></a> BTIF\_HCI\_PROFILE\_TYPE\_A2DP\_OOP\_SNK

<a id="c.BTIF_HCI_PROFILE_TYPE_A2DP_OOP_SRC"></a>

<a id="hci__if_8h_1a1a0073f388bd51467b13c17fa4b6ab29"></a> BTIF\_HCI\_PROFILE\_TYPE\_A2DP\_OOP\_SRC

<a id="c.STANDARD_INQUIRY"></a>

<a id="hci__if_8h_1a526e282b1e04c6156ae1b08d1c61f42d"></a> STANDARD\_INQUIRY
:   inquiry mode definition

<a id="c.RSSI_INQUIRY"></a>

<a id="hci__if_8h_1a0f7aa043695d56938855aaeca2711f3f"></a> RSSI\_INQUIRY

<a id="c.EXTENDED_INQUIRY"></a>

<a id="hci__if_8h_1a1d7f521d12fc0ce535668a498e1e968e"></a> EXTENDED\_INQUIRY

<a id="c.BTIF_HCI_USER_EVENT_MODE_POD"></a>

<a id="hci__if_8h_1af28bd0f17b524b59e5a83f008d478e08"></a> BTIF\_HCI\_USER\_EVENT\_MODE\_POD

<a id="c.BTIF_HCI_USER_EVENT_MODE_TWS"></a>

<a id="hci__if_8h_1aaeb2c2d26dfc60aad00c1b2e2826fd0a"></a> BTIF\_HCI\_USER\_EVENT\_MODE\_TWS

<a id="c.BTIF_USER_EVENT_MODE_LE"></a>

<a id="hci__if_8h_1a6bbf1e3eabbfe54841ef6bde6f186e4b"></a> BTIF\_USER\_EVENT\_MODE\_LE

<a id="c.BTIF_USER_TEMPRATURE_CHANGED"></a>

<a id="hci__if_8h_1a829707f784e166035a47539b7ff470d5"></a> BTIF\_USER\_TEMPRATURE\_CHANGED

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv412if_scan_en_t"></a>

<a id="_CPPv312if_scan_en_t"></a> <a id="_CPPv212if_scan_en_t"></a> <a id="if_scan_en_t"></a> <a id="hci__if_8h_1a0b663699388ebe21b2617cec258ee42d"></a> typedef uint8\_t if\_scan\_en\_t

<a id="_CPPv417btif_conn_state_t"></a>

<a id="_CPPv317btif_conn_state_t"></a> <a id="_CPPv217btif_conn_state_t"></a> <a id="btif_conn_state_t"></a> <a id="hci__if_8h_1aa7588da25f6155bd223007ec6a306b74"></a> typedef uint8\_t btif\_conn\_state\_t

<a id="_CPPv421if_link_policy_type_t"></a>

<a id="_CPPv321if_link_policy_type_t"></a> <a id="_CPPv221if_link_policy_type_t"></a> <a id="if_link_policy_type_t"></a> <a id="hci__if_8h_1a95df7b27987666ef86647c3e0b2096f8"></a> typedef uint16\_t if\_link\_policy\_type\_t

<a id="_CPPv414if_link_mode_t"></a>

<a id="_CPPv314if_link_mode_t"></a> <a id="_CPPv214if_link_mode_t"></a> <a id="if_link_mode_t"></a> <a id="hci__if_8h_1a78196e25a1d87febe77333a89aa2e269"></a> typedef uint8\_t if\_link\_mode\_t

<a id="_CPPv413if_link_dir_t"></a>

<a id="_CPPv313if_link_dir_t"></a> <a id="_CPPv213if_link_dir_t"></a> <a id="if_link_dir_t"></a> <a id="hci__if_8h_1ad8c7658a3bd53dc6eb12c1ac6f233887"></a> typedef uint8\_t if\_link\_dir\_t

<a id="_CPPv412if_link_type"></a>

<a id="_CPPv312if_link_type"></a> <a id="_CPPv212if_link_type"></a> <a id="if_link_type"></a> <a id="hci__if_8h_1ae68a81c78a3e71baafb3bd29ceca5944"></a> typedef uint8\_t if\_link\_type

<a id="_CPPv418if_sleep_ctrl_type"></a>

<a id="_CPPv318if_sleep_ctrl_type"></a> <a id="_CPPv218if_sleep_ctrl_type"></a> <a id="if_sleep_ctrl_type"></a> <a id="hci__if_8h_1a0c4067cdd6b0a843e745a15a3b01e069"></a> typedef uint8\_t if\_sleep\_ctrl\_type

<a id="_CPPv419hci_if_cmd_opcode_t"></a>

<a id="_CPPv319hci_if_cmd_opcode_t"></a> <a id="_CPPv219hci_if_cmd_opcode_t"></a> <a id="hci_if_cmd_opcode_t"></a> <a id="hci__if_8h_1a49e7f04857b32ab4bd04f162eefec266"></a> typedef uint16\_t hci\_if\_cmd\_opcode\_t

<a id="_CPPv423btif_hci_profile_type_t"></a>

<a id="_CPPv323btif_hci_profile_type_t"></a> <a id="_CPPv223btif_hci_profile_type_t"></a> <a id="btif_hci_profile_type_t"></a> <a id="hci__if_8h_1a0d71a7e99d356d95e38abd81f8a22d3a"></a> typedef uint16\_t btif\_hci\_profile\_type\_t
:   profile tyep definition

<a id="_CPPv422btif_user_event_mode_t"></a>

<a id="_CPPv322btif_user_event_mode_t"></a> <a id="_CPPv222btif_user_event_mode_t"></a> <a id="btif_user_event_mode_t"></a> <a id="hci__if_8h_1a0376bd86ca19699e78b0dd4dff974f95"></a> typedef uint8\_t btif\_user\_event\_mode\_t
:   user event mode definition

<a id="_CPPv437hci_if_sync_profile_or_TSS_done_cb_fp"></a>

<a id="_CPPv337hci_if_sync_profile_or_TSS_done_cb_fp"></a> <a id="_CPPv237hci_if_sync_profile_or_TSS_done_cb_fp"></a> <a id="hci_if_sync_profile_or_TSS_done_cb_fp"></a> <a id="hci__if_8h_1a56acf802b239deb8921e5632ade8bad0"></a> typedef void (\*hci\_if\_sync\_profile\_or\_TSS\_done\_cb\_fp)(uint16\_t handle)

<a id="_CPPv417hci_if_get_lk_pfn"></a>

<a id="_CPPv317hci_if_get_lk_pfn"></a> <a id="_CPPv217hci_if_get_lk_pfn"></a> <a id="hci_if_get_lk_pfn"></a> <a id="hci__if_8h_1a1f8e99d3aaf3e8acb517a42c7714e250"></a> typedef [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") (\*hci\_if\_get\_lk\_pfn)([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, [btif\_lk\_t](btif_type.md#_CPPv49btif_lk_t "btif_lk_t") \*p\_lk)

<a id="_CPPv417hci_if_add_lk_pfn"></a>

<a id="_CPPv317hci_if_add_lk_pfn"></a> <a id="_CPPv217hci_if_add_lk_pfn"></a> <a id="hci_if_add_lk_pfn"></a> <a id="hci__if_8h_1a16b2df26c3c8f0dad4f4372bddbb9d01"></a> typedef [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") (\*hci\_if\_add\_lk\_pfn)([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, [btif\_lk\_t](btif_type.md#_CPPv49btif_lk_t "btif_lk_t") \*p\_lk, [if\_link\_key\_type\_t](btif_type.md#_CPPv418if_link_key_type_t "if_link_key_type_t") lk\_type)

<a id="_CPPv420hci_if_delete_lk_pfn"></a>

<a id="_CPPv320hci_if_delete_lk_pfn"></a> <a id="_CPPv220hci_if_delete_lk_pfn"></a> <a id="hci_if_delete_lk_pfn"></a> <a id="hci__if_8h_1af093e46b2c94affc42cec5b797c46d7b"></a> typedef [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") (\*hci\_if\_delete\_lk\_pfn)([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)

<a id="_CPPv430hci_if_get_last_two_record_pfn"></a>

<a id="_CPPv330hci_if_get_last_two_record_pfn"></a> <a id="_CPPv230hci_if_get_last_two_record_pfn"></a> <a id="hci_if_get_last_two_record_pfn"></a> <a id="hci__if_8h_1a63c46d925483944ce3483b2da499205e"></a> typedef uint8\_t (\*hci\_if\_get\_last\_two\_record\_pfn)([btif\_bt\_dev\_info\_t](btif_type.md#_CPPv418btif_bt_dev_info_t "btif_bt_dev_info_t") \*p\_dev\_info1, [btif\_bt\_dev\_info\_t](btif_type.md#_CPPv418btif_bt_dev_info_t "btif_bt_dev_info_t") \*p\_dev\_info2)

<a id="_CPPv427hci_if_get_dev_info_ptr_pfn"></a>

<a id="_CPPv327hci_if_get_dev_info_ptr_pfn"></a> <a id="_CPPv227hci_if_get_dev_info_ptr_pfn"></a> <a id="hci_if_get_dev_info_ptr_pfn"></a> <a id="hci__if_8h_1a4fd184a275c2fece5d387ece08203772"></a> typedef [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") (\*hci\_if\_get\_dev\_info\_ptr\_pfn)([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_bd\_addr, [btif\_bt\_dev\_info\_t](btif_type.md#_CPPv418btif_bt_dev_info_t "btif_bt_dev_info_t") \*\*p\_dev\_info)

<a id="_CPPv416hci_if_get_le_lk"></a>

<a id="_CPPv316hci_if_get_le_lk"></a> <a id="_CPPv216hci_if_get_le_lk"></a> <a id="hci_if_get_le_lk"></a> <a id="hci__if_8h_1af8b22d90cdb5e92e429735b015ebbba2"></a> typedef [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") (\*hci\_if\_get\_le\_lk)([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, [btif\_le\_lk\_t](btif_type.md#_CPPv412btif_le_lk_t "btif_le_lk_t") \*\*p\_lk)

<a id="_CPPv416hci_if_add_le_lk"></a>

<a id="_CPPv316hci_if_add_le_lk"></a> <a id="_CPPv216hci_if_add_le_lk"></a> <a id="hci_if_add_le_lk"></a> <a id="hci__if_8h_1a2f38af0462de8b131261287e2d84f58a"></a> typedef [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") (\*hci\_if\_add\_le\_lk)([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr, [btif\_le\_lk\_t](btif_type.md#_CPPv412btif_le_lk_t "btif_le_lk_t") \*p\_lk)

<a id="_CPPv419hci_if_delete_le_lk"></a>

<a id="_CPPv319hci_if_delete_le_lk"></a> <a id="_CPPv219hci_if_delete_le_lk"></a> <a id="hci_if_delete_le_lk"></a> <a id="hci__if_8h_1ad358d1745ce487b2951fa2ed1854d11f"></a> typedef [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") (\*hci\_if\_delete\_le\_lk)([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv420hci_if_le_meta_event"></a>

<a id="_CPPv320hci_if_le_meta_event"></a> <a id="_CPPv220hci_if_le_meta_event"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351"></a> enum hci\_if\_le\_meta\_event
:   *Values:*

    <a id="_CPPv4N20hci_if_le_meta_event32BTIF_LE_META_CON_CMP_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event32BTIF_LE_META_CON_CMP_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event32BTIF_LE_META_CON_CMP_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a23155f47174d7da826422305f36a54c4"></a> enumerator BTIF\_LE\_META\_CON\_CMP\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event35BTIF_LE_META_ADV_REPORT_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event35BTIF_LE_META_ADV_REPORT_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event35BTIF_LE_META_ADV_REPORT_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351af1b6c7a2b99bd53da54d197571860dd0"></a> enumerator BTIF\_LE\_META\_ADV\_REPORT\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event39BTIF_LE_META_CON_UPDATE_CMP_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event39BTIF_LE_META_CON_UPDATE_CMP_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event39BTIF_LE_META_CON_UPDATE_CMP_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a685d23b182ead022908e8566993db209"></a> enumerator BTIF\_LE\_META\_CON\_UPDATE\_CMP\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event41BTIF_LE_META_RD_REM_FEATS_CMP_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event41BTIF_LE_META_RD_REM_FEATS_CMP_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event41BTIF_LE_META_RD_REM_FEATS_CMP_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a53435ff78561d96103cceab0515aa1fd"></a> enumerator BTIF\_LE\_META\_RD\_REM\_FEATS\_CMP\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event36BTIF_LE_META_LTK_REQUEST_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event36BTIF_LE_META_LTK_REQUEST_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event36BTIF_LE_META_LTK_REQUEST_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a45171041edb2d03f85ddc4b94a2d3fe4"></a> enumerator BTIF\_LE\_META\_LTK\_REQUEST\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event42BTIF_LE_META_REM_CON_PARAM_REQ_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event42BTIF_LE_META_REM_CON_PARAM_REQ_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event42BTIF_LE_META_REM_CON_PARAM_REQ_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a59769e4179eb6f6eb29c39654c8a67a9"></a> enumerator BTIF\_LE\_META\_REM\_CON\_PARAM\_REQ\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event37BTIF_LE_META_DATA_LEN_CHG_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event37BTIF_LE_META_DATA_LEN_CHG_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event37BTIF_LE_META_DATA_LEN_CHG_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351af93eb9bcb9fbc67217264cca0dfe8a9e"></a> enumerator BTIF\_LE\_META\_DATA\_LEN\_CHG\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event48BTIF_LE_META_RD_LOC_P256_PUB_KEY_CMP_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event48BTIF_LE_META_RD_LOC_P256_PUB_KEY_CMP_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event48BTIF_LE_META_RD_LOC_P256_PUB_KEY_CMP_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a3fc2ec375bbf991b9e130b444cd428f6"></a> enumerator BTIF\_LE\_META\_RD\_LOC\_P256\_PUB\_KEY\_CMP\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event38BTIF_LE_META_GEN_DHKEY_CMP_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event38BTIF_LE_META_GEN_DHKEY_CMP_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event38BTIF_LE_META_GEN_DHKEY_CMP_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351ab007287ac53ea1da2325840fad827f14"></a> enumerator BTIF\_LE\_META\_GEN\_DHKEY\_CMP\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event36BTIF_LE_META_ENH_CON_CMP_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event36BTIF_LE_META_ENH_CON_CMP_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event36BTIF_LE_META_ENH_CON_CMP_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351aee1a33e01558e84dd14eb2ee71808ed4"></a> enumerator BTIF\_LE\_META\_ENH\_CON\_CMP\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event36BTIF_LE_META_DIR_ADV_REP_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event36BTIF_LE_META_DIR_ADV_REP_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event36BTIF_LE_META_DIR_ADV_REP_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a4989e44d473f185059fd87f31511ffb3"></a> enumerator BTIF\_LE\_META\_DIR\_ADV\_REP\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event36BTIF_LE_META_PHY_UPD_CMP_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event36BTIF_LE_META_PHY_UPD_CMP_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event36BTIF_LE_META_PHY_UPD_CMP_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a568406ba3d24d540bd72dee5821def0e"></a> enumerator BTIF\_LE\_META\_PHY\_UPD\_CMP\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event39BTIF_LE_META_EXT_ADV_REPORT_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event39BTIF_LE_META_EXT_ADV_REPORT_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event39BTIF_LE_META_EXT_ADV_REPORT_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351add3797686c9eae469236083bba61a53c"></a> enumerator BTIF\_LE\_META\_EXT\_ADV\_REPORT\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event41BTIF_LE_META_PER_ADV_SYNC_EST_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event41BTIF_LE_META_PER_ADV_SYNC_EST_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event41BTIF_LE_META_PER_ADV_SYNC_EST_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a6bb3c8a42057c97c1936f43517b4880b"></a> enumerator BTIF\_LE\_META\_PER\_ADV\_SYNC\_EST\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event39BTIF_LE_META_PER_ADV_REPORT_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event39BTIF_LE_META_PER_ADV_REPORT_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event39BTIF_LE_META_PER_ADV_REPORT_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351aaa2f67a33fb5941e913174415db925c5"></a> enumerator BTIF\_LE\_META\_PER\_ADV\_REPORT\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event42BTIF_LE_META_PER_ADV_SYNC_LOST_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event42BTIF_LE_META_PER_ADV_SYNC_LOST_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event42BTIF_LE_META_PER_ADV_SYNC_LOST_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351ad846aef2e03fc5946ed3268e5351bf3f"></a> enumerator BTIF\_LE\_META\_PER\_ADV\_SYNC\_LOST\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event37BTIF_LE_META_SCAN_TIMEOUT_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event37BTIF_LE_META_SCAN_TIMEOUT_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event37BTIF_LE_META_SCAN_TIMEOUT_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351aa01f92f9544beb73d8c8557a1e88f972"></a> enumerator BTIF\_LE\_META\_SCAN\_TIMEOUT\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event43BTIF_LE_META_ADV_SET_TERMINATED_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event43BTIF_LE_META_ADV_SET_TERMINATED_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event43BTIF_LE_META_ADV_SET_TERMINATED_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a22434c0ff0d9bb1f0ebbc5a786612004"></a> enumerator BTIF\_LE\_META\_ADV\_SET\_TERMINATED\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event38BTIF_LE_META_SCAN_REQ_RCVD_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event38BTIF_LE_META_SCAN_REQ_RCVD_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event38BTIF_LE_META_SCAN_REQ_RCVD_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a11bfd41537ff00b0ce0cdf3b9ce5b872"></a> enumerator BTIF\_LE\_META\_SCAN\_REQ\_RCVD\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event36BTIF_LE_META_CH_SEL_ALGO_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event36BTIF_LE_META_CH_SEL_ALGO_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event36BTIF_LE_META_CH_SEL_ALGO_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a85156da78b60891169cbd6a7efebb34b"></a> enumerator BTIF\_LE\_META\_CH\_SEL\_ALGO\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event42BTIF_LE_META_CONLESS_IQ_REPORT_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event42BTIF_LE_META_CONLESS_IQ_REPORT_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event42BTIF_LE_META_CONLESS_IQ_REPORT_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a9b09f1db93f358da0efe999d3b115300"></a> enumerator BTIF\_LE\_META\_CONLESS\_IQ\_REPORT\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event38BTIF_LE_META_CON_IQ_REPORT_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event38BTIF_LE_META_CON_IQ_REPORT_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event38BTIF_LE_META_CON_IQ_REPORT_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a3a274205de2b0d2682299cd2ece9164c"></a> enumerator BTIF\_LE\_META\_CON\_IQ\_REPORT\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event39BTIF_LE_META_CTE_REQ_FAILED_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event39BTIF_LE_META_CTE_REQ_FAILED_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event39BTIF_LE_META_CTE_REQ_FAILED_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a59b33a8b4fdbd1b7bce2b18edce58d9f"></a> enumerator BTIF\_LE\_META\_CTE\_REQ\_FAILED\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event48BTIF_LE_META_PER_ADV_SYNC_TRANSF_REC_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event48BTIF_LE_META_PER_ADV_SYNC_TRANSF_REC_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event48BTIF_LE_META_PER_ADV_SYNC_TRANSF_REC_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a65516c290f19c624d482f49b790523b5"></a> enumerator BTIF\_LE\_META\_PER\_ADV\_SYNC\_TRANSF\_REC\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event40BTIF_LE_META_CIS_ESTABLISHED_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event40BTIF_LE_META_CIS_ESTABLISHED_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event40BTIF_LE_META_CIS_ESTABLISHED_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a9336aa2383440c0ae4d1e079b576716e"></a> enumerator BTIF\_LE\_META\_CIS\_ESTABLISHED\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event36BTIF_LE_META_CIS_REQUEST_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event36BTIF_LE_META_CIS_REQUEST_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event36BTIF_LE_META_CIS_REQUEST_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a6f97a04c51118dc314672e7b9f2df6cb"></a> enumerator BTIF\_LE\_META\_CIS\_REQUEST\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event39BTIF_LE_META_CREATE_BIG_CMP_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event39BTIF_LE_META_CREATE_BIG_CMP_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event39BTIF_LE_META_CREATE_BIG_CMP_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351aea0b73a4107c7e2accc0cc90e8e9de5a"></a> enumerator BTIF\_LE\_META\_CREATE\_BIG\_CMP\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event42BTIF_LE_META_TERMINATE_BIG_CMP_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event42BTIF_LE_META_TERMINATE_BIG_CMP_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event42BTIF_LE_META_TERMINATE_BIG_CMP_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a735ba8d79779439474c439368d5bd915"></a> enumerator BTIF\_LE\_META\_TERMINATE\_BIG\_CMP\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event45BTIF_LE_META_BIG_SYNC_ESTABLISHED_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event45BTIF_LE_META_BIG_SYNC_ESTABLISHED_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event45BTIF_LE_META_BIG_SYNC_ESTABLISHED_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351accd6678e337daefb8f7a077ba1fe0ed4"></a> enumerator BTIF\_LE\_META\_BIG\_SYNC\_ESTABLISHED\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event38BTIF_LE_META_BIG_SYNC_LOST_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event38BTIF_LE_META_BIG_SYNC_LOST_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event38BTIF_LE_META_BIG_SYNC_LOST_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a6daf2b987b3adedbdb7c2b01d494a4f8"></a> enumerator BTIF\_LE\_META\_BIG\_SYNC\_LOST\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event41BTIF_LE_META_REQ_PEER_SCA_CMP_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event41BTIF_LE_META_REQ_PEER_SCA_CMP_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event41BTIF_LE_META_REQ_PEER_SCA_CMP_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a91d92c7073b31245b17844668d97d4b0"></a> enumerator BTIF\_LE\_META\_REQ\_PEER\_SCA\_CMP\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event44BTIF_LE_META_PATH_LOSS_THRESHOLD_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event44BTIF_LE_META_PATH_LOSS_THRESHOLD_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event44BTIF_LE_META_PATH_LOSS_THRESHOLD_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a053d4e44c19a8e642cbc563d146afb75"></a> enumerator BTIF\_LE\_META\_PATH\_LOSS\_THRESHOLD\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event43BTIF_LE_META_TX_POWER_REPORTING_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event43BTIF_LE_META_TX_POWER_REPORTING_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event43BTIF_LE_META_TX_POWER_REPORTING_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a7b9a8af04fcde392adc85cdae2289ce1"></a> enumerator BTIF\_LE\_META\_TX\_POWER\_REPORTING\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event44BTIF_LE_META_BIG_INFO_ADV_REPORT_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event44BTIF_LE_META_BIG_INFO_ADV_REPORT_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event44BTIF_LE_META_BIG_INFO_ADV_REPORT_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a58c37172f76dffa1f0d9b4f231d04f26"></a> enumerator BTIF\_LE\_META\_BIG\_INFO\_ADV\_REPORT\_EVT\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event44BTIF_LE_META_PER_ADV_SYNC_EST_EVT_V2_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event44BTIF_LE_META_PER_ADV_SYNC_EST_EVT_V2_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event44BTIF_LE_META_PER_ADV_SYNC_EST_EVT_V2_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351a2d03056a0e37a62116d0d3bd4b922e38"></a> enumerator BTIF\_LE\_META\_PER\_ADV\_SYNC\_EST\_EVT\_V2\_SUBCODE

    <a id="_CPPv4N20hci_if_le_meta_event39BTIF_LE_META_ENH_CON_CMP_V2_EVT_SUBCODEE"></a>

    <a id="_CPPv3N20hci_if_le_meta_event39BTIF_LE_META_ENH_CON_CMP_V2_EVT_SUBCODEE"></a> <a id="_CPPv2N20hci_if_le_meta_event39BTIF_LE_META_ENH_CON_CMP_V2_EVT_SUBCODEE"></a> <a id="hci__if_8h_1a11ef50f4aa382fd8cbbef1ed71e6c351aec43de824adacf1d0989c63cf18305de"></a> enumerator BTIF\_LE\_META\_ENH\_CON\_CMP\_V2\_EVT\_SUBCODE
