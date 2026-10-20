---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/btif/avrcp_if.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="avrcp-interface-functions"></a>

# AVRCP Interface Functions

<a id="avrcp-if-api-brief"></a>

## AVRCP\_IF API Brief

| Application | Brief |
| --- | --- |
| [`avrcp_if_disconnect()`](#_CPPv419avrcp_if_disconnect8uint16_t "avrcp_if_disconnect") | AVRCP disconnect API |
| [`avrcp_if_connect()`](#_CPPv416avrcp_if_connectP14btif_bd_addr_t "avrcp_if_connect") | AVRCP connect API |
| [`avrcp_if_tg_set_dft_vol()`](#_CPPv423avrcp_if_tg_set_dft_vol8uint16_t7uint8_t "avrcp_if_tg_set_dft_vol") | AVRCP tg set default volume value, need volume value is AVRCP\_INVALID\_VOL first |
| [`avrcp_if_tg_vol_changed_ntf()`](#_CPPv427avrcp_if_tg_vol_changed_ntf8uint16_t7uint8_t "avrcp_if_tg_vol_changed_ntf") | AVRCP TG notify volume changed event |
| [`avrcp_if_ct_register_ntf()`](#_CPPv424avrcp_if_ct_register_ntf8uint16_t23btif_avrcp_ntf_evt_id_t "avrcp_if_ct_register_ntf") | AVRCP CT register event notify to TG |
| [`avrcp_if_ct_play()`](#_CPPv416avrcp_if_ct_play8uint16_t "avrcp_if_ct_play") | send AVCRP play command |
| [`avrcp_if_ct_pause()`](#_CPPv417avrcp_if_ct_pause8uint16_t "avrcp_if_ct_pause") | send AVCRP pause command |
| [`avrcp_if_ct_stop()`](#_CPPv416avrcp_if_ct_stop8uint16_t "avrcp_if_ct_stop") | send AVCRP stop command |
| [`avrcp_if_ct_forword()`](#_CPPv419avrcp_if_ct_forword8uint16_t "avrcp_if_ct_forword") | send AVCRP forward command |
| [`avrcp_if_ct_backword()`](#_CPPv420avrcp_if_ct_backword8uint16_t "avrcp_if_ct_backword") | send AVCRP backward command |
| [`avrcp_if_ct_fast_forword_start()`](#_CPPv430avrcp_if_ct_fast_forword_start8uint16_t "avrcp_if_ct_fast_forword_start") | send press command with opreation id fast forward |
| [`avrcp_if_ct_fast_forword_stop()`](#_CPPv429avrcp_if_ct_fast_forword_stop8uint16_t "avrcp_if_ct_fast_forword_stop") | send release command for fast forword stop |
| [`avrcp_if_ct_rewind_start()`](#_CPPv424avrcp_if_ct_rewind_start8uint16_t "avrcp_if_ct_rewind_start") | send press command with opreation id rewind |
| [`avrcp_if_ct_rewind_stop()`](#_CPPv423avrcp_if_ct_rewind_stop8uint16_t "avrcp_if_ct_rewind_stop") | send release command for rewind stop |
| [`avrcp_if_ct_get_play_status()`](#_CPPv427avrcp_if_ct_get_play_status8uint16_t "avrcp_if_ct_get_play_status") | send get play status command |
| [`avrcp_if_ct_get_support_evt()`](#_CPPv427avrcp_if_ct_get_support_evt8uint16_t "avrcp_if_ct_get_support_evt") | send the command which get capability id event |
| [`avrcp_if_ct_set_absolute_volume()`](#_CPPv431avrcp_if_ct_set_absolute_volume8uint16_t7uint8_t "avrcp_if_ct_set_absolute_volume") | set AVRCP absolute volume |
| [`avrcp_if_ct_cmd_exchange_ongoing()`](#_CPPv432avrcp_if_ct_cmd_exchange_ongoing8uint16_t "avrcp_if_ct_cmd_exchange_ongoing") | check AVRCP is processing command or not |
| [`avrcp_if_register_event_callback()`](#_CPPv432avrcp_if_register_event_callbackP21btif_avrcp_register_t "avrcp_if_register_event_callback") | AVCRP register event callback API |
| [`avrcp_if_init()`](#_CPPv413avrcp_if_initv "avrcp_if_init") | Initial AVRCP |
| [`avrcp_if_get_sync_len()`](#_CPPv421avrcp_if_get_sync_lenP14btif_bd_addr_t "avrcp_if_get_sync_len") | return the profile sync used max buffer size |
| [`avrcp_if_conn_sync()`](#_CPPv418avrcp_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t "avrcp_if_conn_sync") | TWS master used to send sync profile data |
| [`avrcp_if_conn_restore()`](#_CPPv421avrcp_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t "avrcp_if_conn_restore") | TWS slave used to rebuild its host stack |
| [`avrcp_if_conn_restore_specific()`](#_CPPv430avrcp_if_conn_restore_specificP14btif_bd_addr_t8uint16_t "avrcp_if_conn_restore_specific") | TWS slave update AVRCP connection handle and recover relevant settings |

<a id="avrcp-if-api-reference"></a>

## AVRCP\_IF API Reference

<a id="header-file"></a>

### Header File

- [btif/inc/avrcp\_if.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/btif/inc/avrcp_if.h)

<a id="functions"></a>

### Functions

<a id="_CPPv419avrcp_if_disconnect8uint16_t"></a>

<a id="_CPPv319avrcp_if_disconnect8uint16_t"></a> <a id="_CPPv219avrcp_if_disconnect8uint16_t"></a> <a id="avrcp_if_disconnect__uint16_t"></a> <a id="avrcp__if_8h_1a59b6191fc6d388699918118a2d9579b0"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_disconnect(uint16\_t handle)
:   avrcp\_if\_disconnect brief description

    AVRCP disconnect API

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416avrcp_if_connectP14btif_bd_addr_t"></a>

<a id="_CPPv316avrcp_if_connectP14btif_bd_addr_t"></a> <a id="_CPPv216avrcp_if_connectP14btif_bd_addr_t"></a> <a id="avrcp_if_connect__btif_bd_addr_tP"></a> <a id="avrcp__if_8h_1a0fb0e96bbd847e66f1b06729b8001b5e"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_connect([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   avrcp\_if\_connect brief description

    AVRCP connect API

    参数:
    :   **p\_addr** – **\[in\]** remote BT MAC address

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv423avrcp_if_tg_set_dft_vol8uint16_t7uint8_t"></a>

<a id="_CPPv323avrcp_if_tg_set_dft_vol8uint16_t7uint8_t"></a> <a id="_CPPv223avrcp_if_tg_set_dft_vol8uint16_t7uint8_t"></a> <a id="avrcp_if_tg_set_dft_vol__uint16_t.uint8_t"></a> <a id="avrcp__if_8h_1a6aa4085be5ec6efdffbf823bfa59e728"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_tg\_set\_dft\_vol(uint16\_t handle, uint8\_t vol)
:   avrcp\_if\_tg\_set\_dft\_vol brief description

    AVRCP tg set default volume value, need volume value is AVRCP\_INVALID\_VOL first

    参数:
    :   - **handle** – **\[in\]** connection handle
        - **vol** – **\[in\]** volume value

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427avrcp_if_tg_vol_changed_ntf8uint16_t7uint8_t"></a>

<a id="_CPPv327avrcp_if_tg_vol_changed_ntf8uint16_t7uint8_t"></a> <a id="_CPPv227avrcp_if_tg_vol_changed_ntf8uint16_t7uint8_t"></a> <a id="avrcp_if_tg_vol_changed_ntf__uint16_t.uint8_t"></a> <a id="avrcp__if_8h_1acfa28e833193cdcc1b04c4f88852891e"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_tg\_vol\_changed\_ntf(uint16\_t handle, uint8\_t vol)
:   avrcp\_if\_tg\_vol\_changed\_ntf brief description

    AVRCP TG notify volume changed event

    参数:
    :   - **handle** – **\[in\]** connection handle
        - **vol** – **\[in\]** volume changed value

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424avrcp_if_ct_register_ntf8uint16_t23btif_avrcp_ntf_evt_id_t"></a>

<a id="_CPPv324avrcp_if_ct_register_ntf8uint16_t23btif_avrcp_ntf_evt_id_t"></a> <a id="_CPPv224avrcp_if_ct_register_ntf8uint16_t23btif_avrcp_ntf_evt_id_t"></a> <a id="avrcp_if_ct_register_ntf__uint16_t.btif_avrcp_ntf_evt_id_t"></a> <a id="avrcp__if_8h_1a5f471a41d4f13bd523f794993709303b"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_ct\_register\_ntf(uint16\_t handle, [btif\_avrcp\_ntf\_evt\_id\_t](btif_type.md#_CPPv423btif_avrcp_ntf_evt_id_t "btif_avrcp_ntf_evt_id_t") evt\_id)
:   avrcp\_if\_ct\_register\_ntf brief description

    AVRCP CT register event notify to TG

    参数:
    :   - **handle** – **\[in\]** connection handle
        - **evt\_id** – **\[in\]** AVRCP event ID

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416avrcp_if_ct_play8uint16_t"></a>

<a id="_CPPv316avrcp_if_ct_play8uint16_t"></a> <a id="_CPPv216avrcp_if_ct_play8uint16_t"></a> <a id="avrcp_if_ct_play__uint16_t"></a> <a id="avrcp__if_8h_1ad11f1279f17c60b5f0a4eb714de31987"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_ct\_play(uint16\_t handle)
:   avrcp\_if\_ct\_play brief description

    send AVCRP play command

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv417avrcp_if_ct_pause8uint16_t"></a>

<a id="_CPPv317avrcp_if_ct_pause8uint16_t"></a> <a id="_CPPv217avrcp_if_ct_pause8uint16_t"></a> <a id="avrcp_if_ct_pause__uint16_t"></a> <a id="avrcp__if_8h_1a9721e8623cdec6f040ebcd324808c610"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_ct\_pause(uint16\_t handle)
:   avrcp\_if\_ct\_pause brief description

    send AVCRP pause command

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416avrcp_if_ct_stop8uint16_t"></a>

<a id="_CPPv316avrcp_if_ct_stop8uint16_t"></a> <a id="_CPPv216avrcp_if_ct_stop8uint16_t"></a> <a id="avrcp_if_ct_stop__uint16_t"></a> <a id="avrcp__if_8h_1a653933957f638ab8747b1f2f481ca8a7"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_ct\_stop(uint16\_t handle)
:   avrcp\_if\_ct\_stop brief description

    send AVCRP stop command

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419avrcp_if_ct_forword8uint16_t"></a>

<a id="_CPPv319avrcp_if_ct_forword8uint16_t"></a> <a id="_CPPv219avrcp_if_ct_forword8uint16_t"></a> <a id="avrcp_if_ct_forword__uint16_t"></a> <a id="avrcp__if_8h_1af7ff8a1e41f535207ac3ddab1aab6598"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_ct\_forword(uint16\_t handle)
:   avrcp\_if\_ct\_forward brief description

    send AVCRP forward command

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420avrcp_if_ct_backword8uint16_t"></a>

<a id="_CPPv320avrcp_if_ct_backword8uint16_t"></a> <a id="_CPPv220avrcp_if_ct_backword8uint16_t"></a> <a id="avrcp_if_ct_backword__uint16_t"></a> <a id="avrcp__if_8h_1a82fc94e72caad4be743af39b40d57db1"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_ct\_backword(uint16\_t handle)
:   avrcp\_if\_ct\_backward brief description

    send AVCRP backward command

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv430avrcp_if_ct_fast_forword_start8uint16_t"></a>

<a id="_CPPv330avrcp_if_ct_fast_forword_start8uint16_t"></a> <a id="_CPPv230avrcp_if_ct_fast_forword_start8uint16_t"></a> <a id="avrcp_if_ct_fast_forword_start__uint16_t"></a> <a id="avrcp__if_8h_1ad2f96ae9c78621b8a3902c6e622b48c7"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_ct\_fast\_forword\_start(uint16\_t handle)
:   avrcp\_if\_ct\_fast\_forward\_start brief description

    send press command with opreation id fast forward

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv429avrcp_if_ct_fast_forword_stop8uint16_t"></a>

<a id="_CPPv329avrcp_if_ct_fast_forword_stop8uint16_t"></a> <a id="_CPPv229avrcp_if_ct_fast_forword_stop8uint16_t"></a> <a id="avrcp_if_ct_fast_forword_stop__uint16_t"></a> <a id="avrcp__if_8h_1aa27ddb32e90dce14d4b1077f9ade5cfa"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_ct\_fast\_forword\_stop(uint16\_t handle)
:   avrcp\_if\_ct\_fast\_forward\_stop brief description

    send release command for fast forword stop

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424avrcp_if_ct_rewind_start8uint16_t"></a>

<a id="_CPPv324avrcp_if_ct_rewind_start8uint16_t"></a> <a id="_CPPv224avrcp_if_ct_rewind_start8uint16_t"></a> <a id="avrcp_if_ct_rewind_start__uint16_t"></a> <a id="avrcp__if_8h_1ad5de5e992fb31fce89a9742ef169fbc9"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_ct\_rewind\_start(uint16\_t handle)
:   avrcp\_if\_ct\_rewind\_start brief description

    send press command with opreation id rewind

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv423avrcp_if_ct_rewind_stop8uint16_t"></a>

<a id="_CPPv323avrcp_if_ct_rewind_stop8uint16_t"></a> <a id="_CPPv223avrcp_if_ct_rewind_stop8uint16_t"></a> <a id="avrcp_if_ct_rewind_stop__uint16_t"></a> <a id="avrcp__if_8h_1a10e799a8638b2b1e4c73a01ffea6cde8"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_ct\_rewind\_stop(uint16\_t handle)
:   avrcp\_if\_ct\_rewind\_stop brief description

    send release command for rewind stop

    参数:
    :   **handle** – **\[in\]** connnection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427avrcp_if_ct_get_play_status8uint16_t"></a>

<a id="_CPPv327avrcp_if_ct_get_play_status8uint16_t"></a> <a id="_CPPv227avrcp_if_ct_get_play_status8uint16_t"></a> <a id="avrcp_if_ct_get_play_status__uint16_t"></a> <a id="avrcp__if_8h_1ad409e5f2c5d198805f9cd27f60ccccac"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_ct\_get\_play\_status(uint16\_t handle)
:   avrcp\_if\_ct\_get\_play\_status brief description

    send get play status command

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427avrcp_if_ct_get_support_evt8uint16_t"></a>

<a id="_CPPv327avrcp_if_ct_get_support_evt8uint16_t"></a> <a id="_CPPv227avrcp_if_ct_get_support_evt8uint16_t"></a> <a id="avrcp_if_ct_get_support_evt__uint16_t"></a> <a id="avrcp__if_8h_1adcb33bb8a90ffcc6fb5a6bb4ba6ff781"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_ct\_get\_support\_evt(uint16\_t handle)
:   avrcp\_if\_ct\_get\_support\_evt brief description

    send the command which get capability id event

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv431avrcp_if_ct_set_absolute_volume8uint16_t7uint8_t"></a>

<a id="_CPPv331avrcp_if_ct_set_absolute_volume8uint16_t7uint8_t"></a> <a id="_CPPv231avrcp_if_ct_set_absolute_volume8uint16_t7uint8_t"></a> <a id="avrcp_if_ct_set_absolute_volume__uint16_t.uint8_t"></a> <a id="avrcp__if_8h_1a8cb7f4e1bc82cd238ae0160227601f1b"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_ct\_set\_absolute\_volume(uint16\_t handle, uint8\_t vol)
:   avrcp\_if\_ct\_set\_absolute\_volume brief description

    set AVRCP absolute volume

    参数:
    :   - **handle** – **\[in\]** connection handle
        - **vol** – **\[in\]** volume value

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv432avrcp_if_ct_cmd_exchange_ongoing8uint16_t"></a>

<a id="_CPPv332avrcp_if_ct_cmd_exchange_ongoing8uint16_t"></a> <a id="_CPPv232avrcp_if_ct_cmd_exchange_ongoing8uint16_t"></a> <a id="avrcp_if_ct_cmd_exchange_ongoing__uint16_t"></a> <a id="avrcp__if_8h_1ab7127bf012fade3bd3d45220e0c34998"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_ct\_cmd\_exchange\_ongoing(uint16\_t handle)
:   avrcp\_if\_ct\_cmd\_exchange\_ongoing brief description

    check AVRCP is processing command or not

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **1** – on going
        - **0** – idle

    返回:
    :   result

<a id="_CPPv432avrcp_if_register_event_callbackP21btif_avrcp_register_t"></a>

<a id="_CPPv332avrcp_if_register_event_callbackP21btif_avrcp_register_t"></a> <a id="_CPPv232avrcp_if_register_event_callbackP21btif_avrcp_register_t"></a> <a id="avrcp_if_register_event_callback__btif_avrcp_register_tP"></a> <a id="avrcp__if_8h_1a2c55a870c9eb99766529d219ef0eaa82"></a> void avrcp\_if\_register\_event\_callback([btif\_avrcp\_register\_t](#_CPPv421btif_avrcp_register_t "btif_avrcp_register_t") \*p\_callback)
:   avrcp\_if\_register\_event\_callback brief description

    AVCRP register event callback API

    参数:
    :   **p\_callback** – **\[in\]** strcut of callback function

    返回:
    :   N/A

<a id="_CPPv413avrcp_if_initv"></a>

<a id="_CPPv313avrcp_if_initv"></a> <a id="_CPPv213avrcp_if_initv"></a> <a id="avrcp_if_init__void"></a> <a id="avrcp__if_8h_1a9c2da19aee08ea42c8a1c879dc6023e1"></a> void avrcp\_if\_init(void)
:   avrcp\_if\_init brief description

    返回:
    :   N/A

<a id="_CPPv421avrcp_if_get_sync_lenP14btif_bd_addr_t"></a>

<a id="_CPPv321avrcp_if_get_sync_lenP14btif_bd_addr_t"></a> <a id="_CPPv221avrcp_if_get_sync_lenP14btif_bd_addr_t"></a> <a id="avrcp_if_get_sync_len__btif_bd_addr_tP"></a> <a id="avrcp__if_8h_1ad4b22f044453489b09380d63aa267b9b"></a> uint16\_t avrcp\_if\_get\_sync\_len([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   avrcp\_if\_get\_sync\_len brief description

    return the profile sync used max buffer size

    参数:
    :   **p\_addr** – **\[in\]** remote BT MAC address

    返回:
    :   data length

<a id="_CPPv418avrcp_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t"></a>

<a id="_CPPv318avrcp_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t"></a> <a id="_CPPv218avrcp_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t"></a> <a id="avrcp_if_conn_sync__btif_bd_addr_tP.uint8_tP.uint16_t.uint16_tP"></a> <a id="avrcp__if_8h_1a00737d89d29fc3b855edf68aa8861457"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_conn\_sync([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, uint8\_t \*p\_buff, uint16\_t buff\_len, uint16\_t \*p\_length)
:   avrcp\_if\_conn\_sync brief description

    TWS master used to send sync profile data

    参数:
    :   - **p\_addr** – **\[in\]** remote BT MAC addresss
        - **p\_buff** – **\[out\]** buffer used to sync profile data
        - **buff\_len** – **\[in\]** p\_buff allocated length
        - **p\_length** – **\[out\]** sync profile data length will be sent

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421avrcp_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t"></a>

<a id="_CPPv321avrcp_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t"></a> <a id="_CPPv221avrcp_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t"></a> <a id="avrcp_if_conn_restore__btif_bd_addr_tP.uint8_tP.uint16_t"></a> <a id="avrcp__if_8h_1acd32a9323ca642a3c3045dcadaccc5f8"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_conn\_restore([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, uint8\_t \*p\_buff, uint16\_t length)
:   avrcp\_if\_conn\_restore brief description

    TWS slave used to rebuild its host stack

    参数:
    :   - **p\_addr** – **\[in\]** remote BT MAC address
        - **p\_buff** – **\[in\]** sync profile data
        - **length** – **\[in\]** p\_buff data length

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv430avrcp_if_conn_restore_specificP14btif_bd_addr_t8uint16_t"></a>

<a id="_CPPv330avrcp_if_conn_restore_specificP14btif_bd_addr_t8uint16_t"></a> <a id="_CPPv230avrcp_if_conn_restore_specificP14btif_bd_addr_t8uint16_t"></a> <a id="avrcp_if_conn_restore_specific__btif_bd_addr_tP.uint16_t"></a> <a id="avrcp__if_8h_1a6195f44c19b5b300269c70d9851f7f40"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") avrcp\_if\_conn\_restore\_specific([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, uint16\_t handle)
:   avrcp\_if\_conn\_restore\_specific brief description

    TWS slave update AVRCP connection handle and recover relevant settings

    参数:
    :   - **p\_addr** – **\[in\]** remote BT MAC address
        - **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv419btif_avrcp_cb_hdr_t"></a>

<a id="_CPPv319btif_avrcp_cb_hdr_t"></a> <a id="_CPPv219btif_avrcp_cb_hdr_t"></a> <a id="btif_avrcp_cb_hdr_t"></a> <a id="structbtif__avrcp__cb__hdr__t"></a> struct btif\_avrcp\_cb\_hdr\_t
:   AVRCP header data struct defintion.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19btif_avrcp_cb_hdr_t3evtE"></a>

    <a id="_CPPv3N19btif_avrcp_cb_hdr_t3evtE"></a> <a id="_CPPv2N19btif_avrcp_cb_hdr_t3evtE"></a> <a id="btif_avrcp_cb_hdr_t::evt__btif_avrcp_evt_code_t"></a> <a id="structbtif__avrcp__cb__hdr__t_1aa5f15c3cb1482d5f6cbc1d93dbf8a89f"></a> [btif\_avrcp\_evt\_code\_t](#_CPPv421btif_avrcp_evt_code_t "btif_avrcp_evt_code_t") evt
    :   AVRCP event index

    <a id="_CPPv4N19btif_avrcp_cb_hdr_t6handleE"></a>

    <a id="_CPPv3N19btif_avrcp_cb_hdr_t6handleE"></a> <a id="_CPPv2N19btif_avrcp_cb_hdr_t6handleE"></a> <a id="btif_avrcp_cb_hdr_t::handle__uint16_t"></a> <a id="structbtif__avrcp__cb__hdr__t_1a0f43347bc0819c0fd0d8fae90af20293"></a> uint16\_t handle
    :   connection handle

<a id="_CPPv420btif_avcrp_conn_cb_t"></a>

<a id="_CPPv320btif_avcrp_conn_cb_t"></a> <a id="_CPPv220btif_avcrp_conn_cb_t"></a> <a id="btif_avcrp_conn_cb_t"></a> <a id="structbtif__avcrp__conn__cb__t"></a> struct btif\_avcrp\_conn\_cb\_t
:   AVRCP connection data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20btif_avcrp_conn_cb_t3hdrE"></a>

    <a id="_CPPv3N20btif_avcrp_conn_cb_t3hdrE"></a> <a id="_CPPv2N20btif_avcrp_conn_cb_t3hdrE"></a> <a id="btif_avcrp_conn_cb_t::hdr__btif_avrcp_cb_hdr_t"></a> <a id="structbtif__avcrp__conn__cb__t_1a6dc472a8a3794469d1a8a161e66f31b0"></a> [btif\_avrcp\_cb\_hdr\_t](#_CPPv419btif_avrcp_cb_hdr_t "btif_avrcp_cb_hdr_t") hdr
    :   AVRCP header data struct

    <a id="_CPPv4N20btif_avcrp_conn_cb_t3cidE"></a>

    <a id="_CPPv3N20btif_avcrp_conn_cb_t3cidE"></a> <a id="_CPPv2N20btif_avcrp_conn_cb_t3cidE"></a> <a id="btif_avcrp_conn_cb_t::cid__uint16_t"></a> <a id="structbtif__avcrp__conn__cb__t_1a51339fb428e9f6ac02eedb2ac01c6134"></a> uint16\_t cid
    :   cid value

    <a id="_CPPv4N20btif_avcrp_conn_cb_t4addrE"></a>

    <a id="_CPPv3N20btif_avcrp_conn_cb_t4addrE"></a> <a id="_CPPv2N20btif_avcrp_conn_cb_t4addrE"></a> <a id="btif_avcrp_conn_cb_t::addr__btif_bd_addr_t"></a> <a id="structbtif__avcrp__conn__cb__t_1ad3ee11b6f40b52c7adb8bfb7412bf59a"></a> [btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr
    :   remote BT MAC address

    <a id="_CPPv4N20btif_avcrp_conn_cb_t6statusE"></a>

    <a id="_CPPv3N20btif_avcrp_conn_cb_t6statusE"></a> <a id="_CPPv2N20btif_avcrp_conn_cb_t6statusE"></a> <a id="btif_avcrp_conn_cb_t::status__btif_ret_t"></a> <a id="structbtif__avcrp__conn__cb__t_1a1544895dd4c477a3d292078ed8b2ae17"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") status
    :   status result @btif\_ret\_t

<a id="_CPPv419btif_avcrp_gen_cb_t"></a>

<a id="_CPPv319btif_avcrp_gen_cb_t"></a> <a id="_CPPv219btif_avcrp_gen_cb_t"></a> <a id="btif_avcrp_gen_cb_t"></a> <a id="structbtif__avcrp__gen__cb__t"></a> struct btif\_avcrp\_gen\_cb\_t
:   AVRCP general data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19btif_avcrp_gen_cb_t3hdrE"></a>

    <a id="_CPPv3N19btif_avcrp_gen_cb_t3hdrE"></a> <a id="_CPPv2N19btif_avcrp_gen_cb_t3hdrE"></a> <a id="btif_avcrp_gen_cb_t::hdr__btif_avrcp_cb_hdr_t"></a> <a id="structbtif__avcrp__gen__cb__t_1abf9342018f87aca4f516999d44bb00b0"></a> [btif\_avrcp\_cb\_hdr\_t](#_CPPv419btif_avrcp_cb_hdr_t "btif_avrcp_cb_hdr_t") hdr
    :   AVRCP header data struct

    <a id="_CPPv4N19btif_avcrp_gen_cb_t3lenE"></a>

    <a id="_CPPv3N19btif_avcrp_gen_cb_t3lenE"></a> <a id="_CPPv2N19btif_avcrp_gen_cb_t3lenE"></a> <a id="btif_avcrp_gen_cb_t::len__uint8_t"></a> <a id="structbtif__avcrp__gen__cb__t_1a3f511ace2955ebd457e0b8adbe4eb935"></a> uint8\_t len
    :   length of p\_data

    <a id="_CPPv4N19btif_avcrp_gen_cb_t6p_dataE"></a>

    <a id="_CPPv3N19btif_avcrp_gen_cb_t6p_dataE"></a> <a id="_CPPv2N19btif_avcrp_gen_cb_t6p_dataE"></a> <a id="btif_avcrp_gen_cb_t::p_data__uint8_tCP"></a> <a id="structbtif__avcrp__gen__cb__t_1a3b6c1a41d1b52dd8d2562bd761e6e924"></a> const uint8\_t \*p\_data
    :   data buffer pointer

<a id="_CPPv427btif_avrcp_play_status_cb_t"></a>

<a id="_CPPv327btif_avrcp_play_status_cb_t"></a> <a id="_CPPv227btif_avrcp_play_status_cb_t"></a> <a id="btif_avrcp_play_status_cb_t"></a> <a id="structbtif__avrcp__play__status__cb__t"></a> struct btif\_avrcp\_play\_status\_cb\_t
:   AVRCP play status data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N27btif_avrcp_play_status_cb_t3hdrE"></a>

    <a id="_CPPv3N27btif_avrcp_play_status_cb_t3hdrE"></a> <a id="_CPPv2N27btif_avrcp_play_status_cb_t3hdrE"></a> <a id="btif_avrcp_play_status_cb_t::hdr__btif_avrcp_cb_hdr_t"></a> <a id="structbtif__avrcp__play__status__cb__t_1a8b057ad84e475e1a0e9857229fde2b69"></a> [btif\_avrcp\_cb\_hdr\_t](#_CPPv419btif_avrcp_cb_hdr_t "btif_avrcp_cb_hdr_t") hdr
    :   AVRCP header data struct

    <a id="_CPPv4N27btif_avrcp_play_status_cb_t8song_lenE"></a>

    <a id="_CPPv3N27btif_avrcp_play_status_cb_t8song_lenE"></a> <a id="_CPPv2N27btif_avrcp_play_status_cb_t8song_lenE"></a> <a id="btif_avrcp_play_status_cb_t::song_len__uint32_t"></a> <a id="structbtif__avrcp__play__status__cb__t_1a349c753d9e84b2e6756d4806c584d299"></a> uint32\_t song\_len
    :   total length of playing song

    <a id="_CPPv4N27btif_avrcp_play_status_cb_t13song_positionE"></a>

    <a id="_CPPv3N27btif_avrcp_play_status_cb_t13song_positionE"></a> <a id="_CPPv2N27btif_avrcp_play_status_cb_t13song_positionE"></a> <a id="btif_avrcp_play_status_cb_t::song_position__uint32_t"></a> <a id="structbtif__avrcp__play__status__cb__t_1afdcae7ab09a04d7d6f17ab7abd035f54"></a> uint32\_t song\_position
    :   current position of playing song

    <a id="_CPPv4N27btif_avrcp_play_status_cb_t11play_statusE"></a>

    <a id="_CPPv3N27btif_avrcp_play_status_cb_t11play_statusE"></a> <a id="_CPPv2N27btif_avrcp_play_status_cb_t11play_statusE"></a> <a id="btif_avrcp_play_status_cb_t::play_status__uint8_t"></a> <a id="structbtif__avrcp__play__status__cb__t_1a8d7ffe5cf13e3dda6b772503b5123d95"></a> uint8\_t play\_status
    :   playing status @avrcp\_play\_sts\_t

<a id="_CPPv438btif_avrcp_playback_status_change_cb_t"></a>

<a id="_CPPv338btif_avrcp_playback_status_change_cb_t"></a> <a id="_CPPv238btif_avrcp_playback_status_change_cb_t"></a> <a id="btif_avrcp_playback_status_change_cb_t"></a> <a id="structbtif__avrcp__playback__status__change__cb__t"></a> struct btif\_avrcp\_playback\_status\_change\_cb\_t
:   AVRCP playback status data struct definitino.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N38btif_avrcp_playback_status_change_cb_t3hdrE"></a>

    <a id="_CPPv3N38btif_avrcp_playback_status_change_cb_t3hdrE"></a> <a id="_CPPv2N38btif_avrcp_playback_status_change_cb_t3hdrE"></a> <a id="btif_avrcp_playback_status_change_cb_t::hdr__btif_avrcp_cb_hdr_t"></a> <a id="structbtif__avrcp__playback__status__change__cb__t_1acc42ee195a316a07124fb39a0c04662a"></a> [btif\_avrcp\_cb\_hdr\_t](#_CPPv419btif_avrcp_cb_hdr_t "btif_avrcp_cb_hdr_t") hdr
    :   AVRCP header data struct

    <a id="_CPPv4N38btif_avrcp_playback_status_change_cb_t8cmd_typeE"></a>

    <a id="_CPPv3N38btif_avrcp_playback_status_change_cb_t8cmd_typeE"></a> <a id="_CPPv2N38btif_avrcp_playback_status_change_cb_t8cmd_typeE"></a> <a id="btif_avrcp_playback_status_change_cb_t::cmd_type__btif_avrcp_cmd_type_t"></a> <a id="structbtif__avrcp__playback__status__change__cb__t_1ab96cbc57867a65838ddcadf5d0bd157f"></a> [btif\_avrcp\_cmd\_type\_t](btif_type.md#_CPPv421btif_avrcp_cmd_type_t "btif_avrcp_cmd_type_t") cmd\_type
    :   command type

    <a id="_CPPv4N38btif_avrcp_playback_status_change_cb_t6statusE"></a>

    <a id="_CPPv3N38btif_avrcp_playback_status_change_cb_t6statusE"></a> <a id="_CPPv2N38btif_avrcp_playback_status_change_cb_t6statusE"></a> <a id="btif_avrcp_playback_status_change_cb_t::status__uint8_t"></a> <a id="structbtif__avrcp__playback__status__change__cb__t_1af989bb6c941bcad8c5db690ddf49727c"></a> uint8\_t status
    :   status value @btif\_avrcp\_play\_sts\_t

<a id="_CPPv426btif_avrcp_vol_change_cb_t"></a>

<a id="_CPPv326btif_avrcp_vol_change_cb_t"></a> <a id="_CPPv226btif_avrcp_vol_change_cb_t"></a> <a id="btif_avrcp_vol_change_cb_t"></a> <a id="structbtif__avrcp__vol__change__cb__t"></a> struct btif\_avrcp\_vol\_change\_cb\_t
:   AVRCP volume change data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N26btif_avrcp_vol_change_cb_t3hdrE"></a>

    <a id="_CPPv3N26btif_avrcp_vol_change_cb_t3hdrE"></a> <a id="_CPPv2N26btif_avrcp_vol_change_cb_t3hdrE"></a> <a id="btif_avrcp_vol_change_cb_t::hdr__btif_avrcp_cb_hdr_t"></a> <a id="structbtif__avrcp__vol__change__cb__t_1a467535fd816460280d836adc36291b2b"></a> [btif\_avrcp\_cb\_hdr\_t](#_CPPv419btif_avrcp_cb_hdr_t "btif_avrcp_cb_hdr_t") hdr
    :   AVRCP header data struct

    <a id="_CPPv4N26btif_avrcp_vol_change_cb_t3volE"></a>

    <a id="_CPPv3N26btif_avrcp_vol_change_cb_t3volE"></a> <a id="_CPPv2N26btif_avrcp_vol_change_cb_t3volE"></a> <a id="btif_avrcp_vol_change_cb_t::vol__uint8_t"></a> <a id="structbtif__avrcp__vol__change__cb__t_1ae70abc909b7cd3d5347b172e4f167c55"></a> uint8\_t vol
    :   volume value

<a id="_CPPv424btif_avrcp_cmd_oper_cb_t"></a>

<a id="_CPPv324btif_avrcp_cmd_oper_cb_t"></a> <a id="_CPPv224btif_avrcp_cmd_oper_cb_t"></a> <a id="btif_avrcp_cmd_oper_cb_t"></a> <a id="structbtif__avrcp__cmd__oper__cb__t"></a> struct btif\_avrcp\_cmd\_oper\_cb\_t
:   AVRCP command operation data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N24btif_avrcp_cmd_oper_cb_t3hdrE"></a>

    <a id="_CPPv3N24btif_avrcp_cmd_oper_cb_t3hdrE"></a> <a id="_CPPv2N24btif_avrcp_cmd_oper_cb_t3hdrE"></a> <a id="btif_avrcp_cmd_oper_cb_t::hdr__btif_avrcp_cb_hdr_t"></a> <a id="structbtif__avrcp__cmd__oper__cb__t_1a8b9bb604fd2d7974f7b97468b3655ddf"></a> [btif\_avrcp\_cb\_hdr\_t](#_CPPv419btif_avrcp_cb_hdr_t "btif_avrcp_cb_hdr_t") hdr
    :   AVRCP header data struct

    <a id="_CPPv4N24btif_avrcp_cmd_oper_cb_t7oper_idE"></a>

    <a id="_CPPv3N24btif_avrcp_cmd_oper_cb_t7oper_idE"></a> <a id="_CPPv2N24btif_avrcp_cmd_oper_cb_t7oper_idE"></a> <a id="btif_avrcp_cmd_oper_cb_t::oper_id__btif_avrcp_oper_id_t"></a> <a id="structbtif__avrcp__cmd__oper__cb__t_1aedd0861ca15193eb807be06581066374"></a> [btif\_avrcp\_oper\_id\_t](btif_type.md#_CPPv420btif_avrcp_oper_id_t "btif_avrcp_oper_id_t") oper\_id
    :   index of operation ID

<a id="_CPPv424btif_avrcp_supp_evt_cb_t"></a>

<a id="_CPPv324btif_avrcp_supp_evt_cb_t"></a> <a id="_CPPv224btif_avrcp_supp_evt_cb_t"></a> <a id="btif_avrcp_supp_evt_cb_t"></a> <a id="structbtif__avrcp__supp__evt__cb__t"></a> struct btif\_avrcp\_supp\_evt\_cb\_t
:   AVRCP supported event data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N24btif_avrcp_supp_evt_cb_t3hdrE"></a>

    <a id="_CPPv3N24btif_avrcp_supp_evt_cb_t3hdrE"></a> <a id="_CPPv2N24btif_avrcp_supp_evt_cb_t3hdrE"></a> <a id="btif_avrcp_supp_evt_cb_t::hdr__btif_avrcp_cb_hdr_t"></a> <a id="structbtif__avrcp__supp__evt__cb__t_1a959c6f65049480bd3e225ce93fc05eac"></a> [btif\_avrcp\_cb\_hdr\_t](#_CPPv419btif_avrcp_cb_hdr_t "btif_avrcp_cb_hdr_t") hdr
    :   AVRCP header data struct

    <a id="_CPPv4N24btif_avrcp_supp_evt_cb_t7evt_cntE"></a>

    <a id="_CPPv3N24btif_avrcp_supp_evt_cb_t7evt_cntE"></a> <a id="_CPPv2N24btif_avrcp_supp_evt_cb_t7evt_cntE"></a> <a id="btif_avrcp_supp_evt_cb_t::evt_cnt__uint8_t"></a> <a id="structbtif__avrcp__supp__evt__cb__t_1ab148773eb3d6a56d7c156b44546b84a2"></a> uint8\_t evt\_cnt
    :   event count

    <a id="_CPPv4N24btif_avrcp_supp_evt_cb_t5p_evtE"></a>

    <a id="_CPPv3N24btif_avrcp_supp_evt_cb_t5p_evtE"></a> <a id="_CPPv2N24btif_avrcp_supp_evt_cb_t5p_evtE"></a> <a id="btif_avrcp_supp_evt_cb_t::p_evt__uint8_tCP"></a> <a id="structbtif__avrcp__supp__evt__cb__t_1ae0b2d649b698dc0a5ed2506eed2054f4"></a> const uint8\_t \*p\_evt
    :   pointer to supported list

<a id="_CPPv430btif_avrcp_forward_rewind_cb_t"></a>

<a id="_CPPv330btif_avrcp_forward_rewind_cb_t"></a> <a id="_CPPv230btif_avrcp_forward_rewind_cb_t"></a> <a id="btif_avrcp_forward_rewind_cb_t"></a> <a id="structbtif__avrcp__forward__rewind__cb__t"></a> struct btif\_avrcp\_forward\_rewind\_cb\_t
:   AVRCP forward backward data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N30btif_avrcp_forward_rewind_cb_t3hdrE"></a>

    <a id="_CPPv3N30btif_avrcp_forward_rewind_cb_t3hdrE"></a> <a id="_CPPv2N30btif_avrcp_forward_rewind_cb_t3hdrE"></a> <a id="btif_avrcp_forward_rewind_cb_t::hdr__btif_avrcp_cb_hdr_t"></a> <a id="structbtif__avrcp__forward__rewind__cb__t_1a29a788af0708d73264b6b29124ab512b"></a> [btif\_avrcp\_cb\_hdr\_t](#_CPPv419btif_avrcp_cb_hdr_t "btif_avrcp_cb_hdr_t") hdr
    :   AVRCP header data struct

    <a id="_CPPv4N30btif_avrcp_forward_rewind_cb_t7cmd_stsE"></a>

    <a id="_CPPv3N30btif_avrcp_forward_rewind_cb_t7cmd_stsE"></a> <a id="_CPPv2N30btif_avrcp_forward_rewind_cb_t7cmd_stsE"></a> <a id="btif_avrcp_forward_rewind_cb_t::cmd_sts__btif_avrcp_cmd_sts_t"></a> <a id="structbtif__avrcp__forward__rewind__cb__t_1a3a45f074faca66b82aeef2d82d5cea99"></a> [btif\_avrcp\_cmd\_sts\_t](btif_type.md#_CPPv420btif_avrcp_cmd_sts_t "btif_avrcp_cmd_sts_t") cmd\_sts
    :   command status

    <a id="_CPPv4N30btif_avrcp_forward_rewind_cb_t7oper_idE"></a>

    <a id="_CPPv3N30btif_avrcp_forward_rewind_cb_t7oper_idE"></a> <a id="_CPPv2N30btif_avrcp_forward_rewind_cb_t7oper_idE"></a> <a id="btif_avrcp_forward_rewind_cb_t::oper_id__btif_avrcp_oper_id_t"></a> <a id="structbtif__avrcp__forward__rewind__cb__t_1a3b24daf77a2bd1b935757f21333b142d"></a> [btif\_avrcp\_oper\_id\_t](btif_type.md#_CPPv420btif_avrcp_oper_id_t "btif_avrcp_oper_id_t") oper\_id
    :   operation ID

<a id="_CPPv421btif_avrcp_register_t"></a>

<a id="_CPPv321btif_avrcp_register_t"></a> <a id="_CPPv221btif_avrcp_register_t"></a> <a id="btif_avrcp_register_t"></a> <a id="structbtif__avrcp__register__t"></a> struct btif\_avrcp\_register\_t
:   callback struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N21btif_avrcp_register_t9dlst_nodeE"></a>

    <a id="_CPPv3N21btif_avrcp_register_t9dlst_nodeE"></a> <a id="_CPPv2N21btif_avrcp_register_t9dlst_nodeE"></a> <a id="btif_avrcp_register_t::dlst_node__dl_list_t"></a> <a id="structbtif__avrcp__register__t_1ab598198351e0470f50f9c0f867d456ee"></a> dl\_list\_t dlst\_node
    :   node for application handler will be linked to orthers

    <a id="_CPPv4N21btif_avrcp_register_t8callbackE"></a>

    <a id="_CPPv3N21btif_avrcp_register_t8callbackE"></a> <a id="_CPPv2N21btif_avrcp_register_t8callbackE"></a> <a id="btif_avrcp_register_t::callback__btif_avrcp_event_callback"></a> <a id="structbtif__avrcp__register__t_1aaa0a91832f28cc5b97722d0c1a21f998"></a> [btif\_avrcp\_event\_callback](btif_type.md#_CPPv425btif_avrcp_event_callback "btif_avrcp_event_callback") callback
    :   function pointer for callback function

<a id="macros"></a>

### Macros

<a id="c.BTIF_AVRCP_EVT_CONN"></a>

<a id="avrcp__if_8h_1a90a26bc65aca62d926f9371ec2a746f6"></a> BTIF\_AVRCP\_EVT\_CONN
:   callback struct see @btif\_avcrp\_conn\_cb\_t

<a id="c.BTIF_AVRCP_EVT_DISC"></a>

<a id="avrcp__if_8h_1a2a6ef80aa5a653cd4cd47e18b788454f"></a> BTIF\_AVRCP\_EVT\_DISC
:   callback struct see @btif\_avcrp\_conn\_cb\_t

<a id="c.BTIF_AVRCP_EVT_BROWSING_CONN"></a>

<a id="avrcp__if_8h_1aed58c3e58751651b757b34e0d7141b59"></a> BTIF\_AVRCP\_EVT\_BROWSING\_CONN
:   callback struct see @btif\_avcrp\_conn\_cb\_t

<a id="c.BTIF_AVRCP_EVT_BROWSING_DISC"></a>

<a id="avrcp__if_8h_1a7e5127848f90155810733ba74be3fc56"></a> BTIF\_AVRCP\_EVT\_BROWSING\_DISC
:   callback struct see @btif\_avcrp\_conn\_cb\_t

<a id="c.BTIF_AVRCP_EVT_NTF_PLAYBACK_STATUS_CHANGED"></a>

<a id="avrcp__if_8h_1a6e4be9ff045d060203b7dc81ce71e186"></a> BTIF\_AVRCP\_EVT\_NTF\_PLAYBACK\_STATUS\_CHANGED
:   callback struct see @btif\_avrcp\_playback\_status\_change\_cb\_t

<a id="c.BTIF_AVRCP_EVT_PLAY_STATUS"></a>

<a id="avrcp__if_8h_1a08bde38ddbfb28d331a148f1e914b21f"></a> BTIF\_AVRCP\_EVT\_PLAY\_STATUS
:   callback struct see @btif\_avrcp\_play\_status\_cb\_t

<a id="c.BTIF_AVRCP_EVT_VOL_CHANGED"></a>

<a id="avrcp__if_8h_1ad35368168b2a95e6e9ff733835a751be"></a> BTIF\_AVRCP\_EVT\_VOL\_CHANGED
:   callback struct see @btif\_avrcp\_vol\_change\_cb\_t

<a id="c.BTIF_AVRCP_EVT_CMD_OPERATION"></a>

<a id="avrcp__if_8h_1ac8dc9a9a3b357f7a9dd543e8716cffa2"></a> BTIF\_AVRCP\_EVT\_CMD\_OPERATION
:   callback struct see @btif\_avrcp\_cmd\_oper\_cb\_t

<a id="c.BTIF_AVRCP_EVT_SUPPORT_EVT_IDS"></a>

<a id="avrcp__if_8h_1a753bcdb522a9345d8826dcb6ff6e5ac8"></a> BTIF\_AVRCP\_EVT\_SUPPORT\_EVT\_IDS
:   callback struct see @btif\_avrcp\_supp\_evt\_cb\_t

<a id="c.BTIF_AVRCP_EVT_SET_ADDRESSED_PLAYER"></a>

<a id="avrcp__if_8h_1a13bf08d1ad4f41682894017e9c1dd6d2"></a> BTIF\_AVRCP\_EVT\_SET\_ADDRESSED\_PLAYER
:   callback struct see @ NULL

<a id="c.BTIF_AVRCP_EVT_L2CAP_DATA"></a>

<a id="avrcp__if_8h_1ab610116b054d97497e0c3d7c9c19c5f3"></a> BTIF\_AVRCP\_EVT\_L2CAP\_DATA
:   callback struct see @btif\_avcrp\_gen\_cb\_t

<a id="c.BTIF_AVRCP_EVT_BROWSING_DATA"></a>

<a id="avrcp__if_8h_1a0809069c85a64c9610a2a49013a96fdf"></a> BTIF\_AVRCP\_EVT\_BROWSING\_DATA
:   callback struct see @btif\_avcrp\_gen\_cb\_t

<a id="c.BTIF_AVRCP_EVT_FORWARD_REWIND_CMD_STAT"></a>

<a id="avrcp__if_8h_1abda814635dd08267ac9cf00853a4059f"></a> BTIF\_AVRCP\_EVT\_FORWARD\_REWIND\_CMD\_STAT
:   callback struct see @btif\_avrcp\_forward\_rewind\_cb\_t

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv421btif_avrcp_evt_code_t"></a>

<a id="_CPPv321btif_avrcp_evt_code_t"></a> <a id="_CPPv221btif_avrcp_evt_code_t"></a> <a id="btif_avrcp_evt_code_t"></a> <a id="avrcp__if_8h_1a1f52368d965aace3cd69ae3c8f3596ac"></a> typedef uint8\_t btif\_avrcp\_evt\_code\_t
