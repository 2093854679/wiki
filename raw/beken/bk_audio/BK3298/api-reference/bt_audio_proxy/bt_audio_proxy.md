---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/bt_audio_proxy/bt_audio_proxy.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bluetooth-audio-proxy-functions"></a>

# Bluetooth Audio PROXY Functions

<a id="bt-audio-proxy-api-brief"></a>

## BT\_AUDIO\_PROXY API Brief

| Application | Brief |
| --- | --- |
| [`bt_audio_proxy_alloc_ctx()`](#_CPPv424bt_audio_proxy_alloc_ctx8uint16_t14btif_bd_addr_t "bt_audio_proxy_alloc_ctx") | Allocate audio proxy context |
| [`bt_audio_proxy_free_ctx()`](#_CPPv423bt_audio_proxy_free_ctxP20bt_audio_proxy_ctx_t "bt_audio_proxy_free_ctx") | Free audio proxy context |
| [`bt_audio_proxy_find_ctx_by_handle()`](#_CPPv433bt_audio_proxy_find_ctx_by_handle8uint16_t "bt_audio_proxy_find_ctx_by_handle") | Find audio proxy context by handle |
| [`bt_audio_proxy_find_ctx_by_addr()`](#_CPPv431bt_audio_proxy_find_ctx_by_addrP14btif_bd_addr_t "bt_audio_proxy_find_ctx_by_addr") | Find audio proxy context by address |
| [`bt_audio_proxy_find_ctx_on_race_status()`](#_CPPv438bt_audio_proxy_find_ctx_on_race_statusv "bt_audio_proxy_find_ctx_on_race_status") | Fine audio proxy context of race status |
| [`bt_audio_proxy_a2dp_race_is_onging()`](#_CPPv434bt_audio_proxy_a2dp_race_is_onging8uint16_t "bt_audio_proxy_a2dp_race_is_onging") | Check that the A2DP race is ongoing |
| [`bt_audio_proxy_media_profile_discon_handle()`](#_CPPv442bt_audio_proxy_media_profile_discon_handleP20bt_audio_proxy_ctx_t "bt_audio_proxy_media_profile_discon_handle") | Media profile disconnection handler for disconnection event |
| [`bt_audio_proxy_media_profile_conn_handle()`](#_CPPv440bt_audio_proxy_media_profile_conn_handleP20bt_audio_proxy_ctx_t "bt_audio_proxy_media_profile_conn_handle") | Media profile connection handler for connection event |
| [`bt_audio_proxy_execute_hfp_stream_start()`](#_CPPv439bt_audio_proxy_execute_hfp_stream_startP20bt_audio_proxy_ctx_t "bt_audio_proxy_execute_hfp_stream_start") | start hfp stream after audio connection is established |
| [`bt_audio_proxy_execute_hfp_stream_stop()`](#_CPPv438bt_audio_proxy_execute_hfp_stream_stopP20bt_audio_proxy_ctx_t "bt_audio_proxy_execute_hfp_stream_stop") | stop hfp stream after audio connection is released |
| [`bt_audio_proxy_execute_a2dp_stream_start()`](#_CPPv440bt_audio_proxy_execute_a2dp_stream_startP20bt_audio_proxy_ctx_t "bt_audio_proxy_execute_a2dp_stream_start") | start a2dp stream after audio connection is established |
| [`bt_audio_proxy_execute_a2dp_stream_stop()`](#_CPPv439bt_audio_proxy_execute_a2dp_stream_stopP20bt_audio_proxy_ctx_t "bt_audio_proxy_execute_a2dp_stream_stop") | stop a2dp stream after audio connection is released |
| [`bt_audio_proxy_sync_profile_TSS_is_ongoing()`](#_CPPv442bt_audio_proxy_sync_profile_TSS_is_ongoingP20bt_audio_proxy_ctx_t "bt_audio_proxy_sync_profile_TSS_is_ongoing") | Check that the tws switch or sync profile is ongoing |
| [`bt_audio_proxy_update_race_status()`](#_CPPv433bt_audio_proxy_update_race_statusP20bt_audio_proxy_ctx_t20bt_audio_race_status "bt_audio_proxy_update_race_status") | Update and process race status |
| [`bt_audio_proxy_any_call_is_exist()`](#_CPPv432bt_audio_proxy_any_call_is_existv "bt_audio_proxy_any_call_is_exist") | Check that any call is existed |
| [`bt_audio_proxy_update_hfcall_active()`](#_CPPv435bt_audio_proxy_update_hfcall_activeP20bt_audio_proxy_ctx_t "bt_audio_proxy_update_hfcall_active") | Update and process hfcall active status |
| [`bt_audio_proxy_tx_profile_cmd()`](#_CPPv429bt_audio_proxy_tx_profile_cmdP20bt_audio_proxy_ctx_t23bt_audio_proxy_cmd_id_tPK7uint8_t8uint16_t "bt_audio_proxy_tx_profile_cmd") | Send profile command to paired earbud |
| [`bt_audio_proxy_tx_conn_cmd()`](#_CPPv426bt_audio_proxy_tx_conn_cmd14btif_bd_addr_t23bt_audio_proxy_cmd_id_t "bt_audio_proxy_tx_conn_cmd") | Send profile connection or disconnection command to paired earbud |
| [`bt_audio_proxy_vol_set()`](#_CPPv422bt_audio_proxy_vol_set19audio_stream_type_t8uint16_t7uint8_t "bt_audio_proxy_vol_set") | Set audio volume level |
| [`bt_audio_proxy_vol_up()`](#_CPPv421bt_audio_proxy_vol_up7uint8_t "bt_audio_proxy_vol_up") | Turn up the audio volume |
| [`bt_audio_proxy_vol_down()`](#_CPPv423bt_audio_proxy_vol_down7uint8_t "bt_audio_proxy_vol_down") | Turn down the audio volume |
| [`bt_audio_proxy_get_dft_vol()`](#_CPPv426bt_audio_proxy_get_dft_volP20bt_audio_proxy_ctx_t19audio_stream_type_t "bt_audio_proxy_get_dft_vol") | Get default audio volume |
| [`bt_audio_proxy_set_mute()`](#_CPPv423bt_audio_proxy_set_mute19audio_stream_type_tb "bt_audio_proxy_set_mute") | Set DSP mute mode |
| [`bt_audio_proxy_get_mute()`](#_CPPv423bt_audio_proxy_get_mute19audio_stream_type_tPb "bt_audio_proxy_get_mute") | Get DSP Mute mode |
| [`bt_audio_proxy_avrcp_play_pause()`](#_CPPv431bt_audio_proxy_avrcp_play_pausev "bt_audio_proxy_avrcp_play_pause") | Toggle play or pause audio by profile command |
| [`bt_audio_proxy_avrcp_next()`](#_CPPv425bt_audio_proxy_avrcp_nextv "bt_audio_proxy_avrcp_next") | play next music by profile command |
| [`bt_audio_proxy_avrcp_previous()`](#_CPPv429bt_audio_proxy_avrcp_previousv "bt_audio_proxy_avrcp_previous") | play previous music by profile command |
| [`bt_audio_proxy_avrcp_fast_forward_start()`](#_CPPv439bt_audio_proxy_avrcp_fast_forward_startv "bt_audio_proxy_avrcp_fast_forward_start") | Start fast forward music by profile command |
| [`bt_audio_proxy_avrcp_fast_forward_stop()`](#_CPPv438bt_audio_proxy_avrcp_fast_forward_stopv "bt_audio_proxy_avrcp_fast_forward_stop") | Stop fast forward music by profile command |
| [`bt_audio_proxy_avtive_dev_set_delay_rpt()`](#_CPPv439bt_audio_proxy_avtive_dev_set_delay_rpt8uint16_t "bt_audio_proxy_avtive_dev_set_delay_rpt") | send a2dp delay report command |
| [`bt_audio_proxy_avrcp_rewind_start()`](#_CPPv433bt_audio_proxy_avrcp_rewind_startv "bt_audio_proxy_avrcp_rewind_start") | Start rewind music by profile command |
| [`bt_audio_proxy_avrcp_rewind_stop()`](#_CPPv432bt_audio_proxy_avrcp_rewind_stopv "bt_audio_proxy_avrcp_rewind_stop") | Stop rewind music by profile command |
| [`bt_audio_proxy_redial_last_number()`](#_CPPv433bt_audio_proxy_redial_last_number8uint16_t "bt_audio_proxy_redial_last_number") | redial last number by profile command |
| [`bt_audio_proxy_dial_number()`](#_CPPv426bt_audio_proxy_dial_number8uint16_tP7uint8_t7uint8_t "bt_audio_proxy_dial_number") | dial number by profile command |
| [`bt_audio_proxy_call_terminal()`](#_CPPv428bt_audio_proxy_call_terminal8uint16_t "bt_audio_proxy_call_terminal") | terminate call by profile command |
| [`bt_audio_proxy_call_accept()`](#_CPPv426bt_audio_proxy_call_accept8uint16_t "bt_audio_proxy_call_accept") | accept call by profile command |
| [`bt_audio_proxy_call_reject()`](#_CPPv426bt_audio_proxy_call_reject8uint16_t "bt_audio_proxy_call_reject") | reject call by profile command |
| [`bt_audio_proxy_hf_bat_report()`](#_CPPv428bt_audio_proxy_hf_bat_report8uint16_t7uint8_t "bt_audio_proxy_hf_bat_report") | Send the HFP battery level by profile command |
| [`bt_audio_proxy_hf_vr_enable()`](#_CPPv427bt_audio_proxy_hf_vr_enable8uint16_t7uint8_t "bt_audio_proxy_hf_vr_enable") | Enable/disable voice recognition by profile command |
| [`bt_audio_proxy_hf_setup_audio_conn()`](#_CPPv434bt_audio_proxy_hf_setup_audio_conn8uint16_t "bt_audio_proxy_hf_setup_audio_conn") | Setup HFP audio connection by profile command |
| [`bt_audio_proxy_hf_disc_audio_conn()`](#_CPPv433bt_audio_proxy_hf_disc_audio_conn8uint16_t "bt_audio_proxy_hf_disc_audio_conn") | Disconnect HFP audio connection by profile command |
| [`bt_audio_proxy_connect_a2dp()`](#_CPPv427bt_audio_proxy_connect_a2dpP14btif_bd_addr_t "bt_audio_proxy_connect_a2dp") | Connect A2DP by profile command |
| [`bt_audio_proxy_disconnect_a2dp()`](#_CPPv430bt_audio_proxy_disconnect_a2dp8uint16_t "bt_audio_proxy_disconnect_a2dp") | Disconnect A2DP by profile command |
| [`bt_audio_proxy_connect_avrcp()`](#_CPPv428bt_audio_proxy_connect_avrcpP14btif_bd_addr_t "bt_audio_proxy_connect_avrcp") | Connect AVRCP by profile command |
| [`bt_audio_proxy_disconnect_avrcp()`](#_CPPv431bt_audio_proxy_disconnect_avrcp8uint16_t "bt_audio_proxy_disconnect_avrcp") | Disconnect AVRCP by profile command |
| [`bt_audio_proxy_connect_hfp()`](#_CPPv426bt_audio_proxy_connect_hfpP14btif_bd_addr_t "bt_audio_proxy_connect_hfp") | Connect HFP by profile command |
| [`bt_audio_proxy_disconnect_hfp()`](#_CPPv429bt_audio_proxy_disconnect_hfp8uint16_t "bt_audio_proxy_disconnect_hfp") | Disconnect HFP by profile command |
| [`bt_audio_proxy_get_avrcp_play_status()`](#_CPPv436bt_audio_proxy_get_avrcp_play_status8uint16_tP21btif_avrcp_play_sts_t "bt_audio_proxy_get_avrcp_play_status") | Get the AVRCP play status of proxy context |
| [`bt_audio_proxy_init()`](#_CPPv419bt_audio_proxy_initb "bt_audio_proxy_init") | Initialize aduio proxy |
| [`bt_audio_proxy_get_a2dp_active_handle()`](#_CPPv437bt_audio_proxy_get_a2dp_active_handlev "bt_audio_proxy_get_a2dp_active_handle") | Get A2DP active connection handle |
| [`bt_audio_proxy_get_hfp_active_handle()`](#_CPPv436bt_audio_proxy_get_hfp_active_handlev "bt_audio_proxy_get_hfp_active_handle") | Get HFP active connection handle |
| [`bt_audio_is_a2dp_streaming()`](#_CPPv426bt_audio_is_a2dp_streamingv "bt_audio_is_a2dp_streaming") | Check that a2dp is streaming |
| [`bt_audio_is_sco_on()`](#_CPPv418bt_audio_is_sco_onv "bt_audio_is_sco_on") | Check that SCO is turn on |
| [`bt_audio_proxy_get_ctx()`](#_CPPv422bt_audio_proxy_get_ctx8uint16_t "bt_audio_proxy_get_ctx") | Get audio proxy context |
| [`bt_audio_proxy_get_hf_avtive_codec_type()`](#_CPPv439bt_audio_proxy_get_hf_avtive_codec_typev "bt_audio_proxy_get_hf_avtive_codec_type") | Get the active HFP codec type |
| [`bt_audio_avrcp_ct_cmd_state_ntf()`](#_CPPv431bt_audio_avrcp_ct_cmd_state_ntf20btif_avrcp_cmd_sts_t20btif_avrcp_oper_id_t "bt_audio_avrcp_ct_cmd_state_ntf") | Notification AVRCP command state |
| [`bt_audio_proxy_get_last_hf_call_setup()`](#_CPPv437bt_audio_proxy_get_last_hf_call_setupv "bt_audio_proxy_get_last_hf_call_setup") | Get HFP call setup status |
| [`bt_audio_proxy_sco_exist()`](#_CPPv424bt_audio_proxy_sco_exist8uint16_t "bt_audio_proxy_sco_exist") | Check that SCO exists |

<a id="bt-audio-proxy-api-reference"></a>

## BT\_AUDIO\_PROXY API Reference

<a id="header-file"></a>

### Header File

- [bt\_audio\_proxy/inc/bt\_audio\_proxy.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/bt_audio_proxy/inc/bt_audio_proxy.h)

<a id="functions"></a>

### Functions

<a id="_CPPv424bt_audio_proxy_alloc_ctx8uint16_t14btif_bd_addr_t"></a>

<a id="_CPPv324bt_audio_proxy_alloc_ctx8uint16_t14btif_bd_addr_t"></a> <a id="_CPPv224bt_audio_proxy_alloc_ctx8uint16_t14btif_bd_addr_t"></a> <a id="bt_audio_proxy_alloc_ctx__uint16_t.btif_bd_addr_t"></a> <a id="bt__audio__proxy_8h_1adabb356663476f9037cbac0ca4a0e5a3"></a> [bt\_audio\_proxy\_ctx\_t](#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*bt\_audio\_proxy\_alloc\_ctx(uint16\_t handle, [btif\_bd\_addr\_t](../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr)
:   Allocate audio proxy context.

    Alloc audio proxy context

    参数:
    :   - **handle** – **\[in\]** connection handle
        - **addr** – **\[in\]** connection address of type [btif\_bd\_addr\_t](../btif/btif_type.md#structbtif__bd__addr__t)

    返回值:
    :   **NULL** – Alloc failed

    返回:
    :   Pointer of the audio proxy context

<a id="_CPPv423bt_audio_proxy_free_ctxP20bt_audio_proxy_ctx_t"></a>

<a id="_CPPv323bt_audio_proxy_free_ctxP20bt_audio_proxy_ctx_t"></a> <a id="_CPPv223bt_audio_proxy_free_ctxP20bt_audio_proxy_ctx_t"></a> <a id="bt_audio_proxy_free_ctx__bt_audio_proxy_ctx_tP"></a> <a id="bt__audio__proxy_8h_1a9327e5966bf04dfe111e2979c285f031"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_free\_ctx([bt\_audio\_proxy\_ctx\_t](#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*p\_audio\_proxy\_ctx)
:   Free audio proxy context.

    Free audio proxy context

    参数:
    :   **p\_audio\_proxy\_ctx** – **\[in\]** pointer to an audio proxy context of type [bt\_audio\_proxy\_ctx\_t](#structbt__audio__proxy__ctx__t)

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv433bt_audio_proxy_find_ctx_by_handle8uint16_t"></a>

<a id="_CPPv333bt_audio_proxy_find_ctx_by_handle8uint16_t"></a> <a id="_CPPv233bt_audio_proxy_find_ctx_by_handle8uint16_t"></a> <a id="bt_audio_proxy_find_ctx_by_handle__uint16_t"></a> <a id="bt__audio__proxy_8h_1a01442abb4a42001ea9e35e5c06f65f7b"></a> [bt\_audio\_proxy\_ctx\_t](#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*bt\_audio\_proxy\_find\_ctx\_by\_handle(uint16\_t handle)
:   Find audio proxy context by handle.

    Find audio proxy context by acl handle

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   **NULL** – find failed

    返回:
    :   Pointer of the audio proxy context

<a id="_CPPv431bt_audio_proxy_find_ctx_by_addrP14btif_bd_addr_t"></a>

<a id="_CPPv331bt_audio_proxy_find_ctx_by_addrP14btif_bd_addr_t"></a> <a id="_CPPv231bt_audio_proxy_find_ctx_by_addrP14btif_bd_addr_t"></a> <a id="bt_audio_proxy_find_ctx_by_addr__btif_bd_addr_tP"></a> <a id="bt__audio__proxy_8h_1a715ce711dcdec443980c6f86e87600b9"></a> [bt\_audio\_proxy\_ctx\_t](#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*bt\_audio\_proxy\_find\_ctx\_by\_addr([btif\_bd\_addr\_t](../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   Find audio proxy context by address.

    Find audio proxy context by remote device address

    参数:
    :   **p\_addr** – **\[in\]** pointer to a remote device address of type [btif\_bd\_addr\_t](../btif/btif_type.md#structbtif__bd__addr__t)

    返回值:
    :   **NULL** – Find failed

    返回:
    :   Pointer of the audio proxy context

<a id="_CPPv438bt_audio_proxy_find_ctx_on_race_statusv"></a>

<a id="_CPPv338bt_audio_proxy_find_ctx_on_race_statusv"></a> <a id="_CPPv238bt_audio_proxy_find_ctx_on_race_statusv"></a> <a id="bt_audio_proxy_find_ctx_on_race_status__void"></a> <a id="bt__audio__proxy_8h_1a077ae68e001bc1cae91107f92b323c4e"></a> [bt\_audio\_proxy\_ctx\_t](#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*bt\_audio\_proxy\_find\_ctx\_on\_race\_status(void)
:   Fine audio proxy context of race status.

    Find audio proxy context which on the race status

    返回值:
    :   **NULL** – Find failed

    返回:
    :   Pointer of the audio proxy context

<a id="_CPPv434bt_audio_proxy_a2dp_race_is_onging8uint16_t"></a>

<a id="_CPPv334bt_audio_proxy_a2dp_race_is_onging8uint16_t"></a> <a id="_CPPv234bt_audio_proxy_a2dp_race_is_onging8uint16_t"></a> <a id="bt_audio_proxy_a2dp_race_is_onging__uint16_t"></a> <a id="bt__audio__proxy_8h_1a787da76d36dabc558290b6cea3f839ed"></a> bool bt\_audio\_proxy\_a2dp\_race\_is\_onging(uint16\_t handle)
:   Check that the A2DP race is ongoing.

    Check that the race state of the proxy context with handle \[handle\] is ongoing.

    参数:
    :   **handle** – **\[in\]** connection handle

    返回:
    :   true: a2dp race ongoing

<a id="_CPPv442bt_audio_proxy_media_profile_discon_handleP20bt_audio_proxy_ctx_t"></a>

<a id="_CPPv342bt_audio_proxy_media_profile_discon_handleP20bt_audio_proxy_ctx_t"></a> <a id="_CPPv242bt_audio_proxy_media_profile_discon_handleP20bt_audio_proxy_ctx_t"></a> <a id="bt_audio_proxy_media_profile_discon_handle__bt_audio_proxy_ctx_tP"></a> <a id="bt__audio__proxy_8h_1a099d2eb05f8089784d995b470b751409"></a> void bt\_audio\_proxy\_media\_profile\_discon\_handle([bt\_audio\_proxy\_ctx\_t](#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*p\_proxy\_ctx)
:   Media profile disconnection handler for disconnection event.

    avrcp or a2dp disconnected handler

    参数:
    :   **p\_proxy\_ctx** – **\[in\]** pointer to a proxy context of type [bt\_audio\_proxy\_ctx\_t](#structbt__audio__proxy__ctx__t)

    返回:
    :   N/A

<a id="_CPPv440bt_audio_proxy_media_profile_conn_handleP20bt_audio_proxy_ctx_t"></a>

<a id="_CPPv340bt_audio_proxy_media_profile_conn_handleP20bt_audio_proxy_ctx_t"></a> <a id="_CPPv240bt_audio_proxy_media_profile_conn_handleP20bt_audio_proxy_ctx_t"></a> <a id="bt_audio_proxy_media_profile_conn_handle__bt_audio_proxy_ctx_tP"></a> <a id="bt__audio__proxy_8h_1a31e8c1af97339e1ca3c9d1b6670cb368"></a> void bt\_audio\_proxy\_media\_profile\_conn\_handle([bt\_audio\_proxy\_ctx\_t](#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*p\_proxy\_ctx)
:   Media profile connection handler for connection event.

    avrcp or a2dp connected handler

    参数:
    :   **p\_proxy\_ctx** – **\[in\]** pointer to a proxy context of type [bt\_audio\_proxy\_ctx\_t](#structbt__audio__proxy__ctx__t)

    返回:
    :   N/A

<a id="_CPPv439bt_audio_proxy_execute_hfp_stream_startP20bt_audio_proxy_ctx_t"></a>

<a id="_CPPv339bt_audio_proxy_execute_hfp_stream_startP20bt_audio_proxy_ctx_t"></a> <a id="_CPPv239bt_audio_proxy_execute_hfp_stream_startP20bt_audio_proxy_ctx_t"></a> <a id="bt_audio_proxy_execute_hfp_stream_start__bt_audio_proxy_ctx_tP"></a> <a id="bt__audio__proxy_8h_1adaadef4f5305e8805905e02754856d24"></a> void bt\_audio\_proxy\_execute\_hfp\_stream\_start([bt\_audio\_proxy\_ctx\_t](#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*p\_proxy\_ctx)
:   start hfp stream after audio connection is established

    hfp stream start handler

    参数:
    :   **p\_proxy\_ctx** – **\[in\]** pointer to a proxy context of type [bt\_audio\_proxy\_ctx\_t](#structbt__audio__proxy__ctx__t)

    返回:
    :   N/A

<a id="_CPPv438bt_audio_proxy_execute_hfp_stream_stopP20bt_audio_proxy_ctx_t"></a>

<a id="_CPPv338bt_audio_proxy_execute_hfp_stream_stopP20bt_audio_proxy_ctx_t"></a> <a id="_CPPv238bt_audio_proxy_execute_hfp_stream_stopP20bt_audio_proxy_ctx_t"></a> <a id="bt_audio_proxy_execute_hfp_stream_stop__bt_audio_proxy_ctx_tP"></a> <a id="bt__audio__proxy_8h_1aa5da91faa28b25340877fe702dbae9de"></a> void bt\_audio\_proxy\_execute\_hfp\_stream\_stop([bt\_audio\_proxy\_ctx\_t](#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*p\_proxy\_ctx)
:   stop hfp stream after audio connection is released

    hfp stream stop handler

    参数:
    :   **p\_proxy\_ctx** – **\[in\]** pointer to a proxy context of type [bt\_audio\_proxy\_ctx\_t](#structbt__audio__proxy__ctx__t)

    返回:
    :   N/A

<a id="_CPPv440bt_audio_proxy_execute_a2dp_stream_startP20bt_audio_proxy_ctx_t"></a>

<a id="_CPPv340bt_audio_proxy_execute_a2dp_stream_startP20bt_audio_proxy_ctx_t"></a> <a id="_CPPv240bt_audio_proxy_execute_a2dp_stream_startP20bt_audio_proxy_ctx_t"></a> <a id="bt_audio_proxy_execute_a2dp_stream_start__bt_audio_proxy_ctx_tP"></a> <a id="bt__audio__proxy_8h_1a3272c4b116d3584f9c1abd98972fb321"></a> void bt\_audio\_proxy\_execute\_a2dp\_stream\_start([bt\_audio\_proxy\_ctx\_t](#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*p\_proxy\_ctx)
:   start a2dp stream after audio connection is established

    a2dp stream start handler

    参数:
    :   **p\_proxy\_ctx** – **\[in\]** pointer to a proxy context of type [bt\_audio\_proxy\_ctx\_t](#structbt__audio__proxy__ctx__t)

    返回:
    :   N/A

<a id="_CPPv439bt_audio_proxy_execute_a2dp_stream_stopP20bt_audio_proxy_ctx_t"></a>

<a id="_CPPv339bt_audio_proxy_execute_a2dp_stream_stopP20bt_audio_proxy_ctx_t"></a> <a id="_CPPv239bt_audio_proxy_execute_a2dp_stream_stopP20bt_audio_proxy_ctx_t"></a> <a id="bt_audio_proxy_execute_a2dp_stream_stop__bt_audio_proxy_ctx_tP"></a> <a id="bt__audio__proxy_8h_1a09de1701fb9d612056fc318db54b928d"></a> void bt\_audio\_proxy\_execute\_a2dp\_stream\_stop([bt\_audio\_proxy\_ctx\_t](#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*p\_proxy\_ctx)
:   stop a2dp stream after audio connection is released

    a2dp stream stop handler

    参数:
    :   **p\_proxy\_ctx** – **\[in\]** pointer to a proxy context of type [bt\_audio\_proxy\_ctx\_t](#structbt__audio__proxy__ctx__t)

    返回:
    :   N/A

<a id="_CPPv442bt_audio_proxy_sync_profile_TSS_is_ongoingP20bt_audio_proxy_ctx_t"></a>

<a id="_CPPv342bt_audio_proxy_sync_profile_TSS_is_ongoingP20bt_audio_proxy_ctx_t"></a> <a id="_CPPv242bt_audio_proxy_sync_profile_TSS_is_ongoingP20bt_audio_proxy_ctx_t"></a> <a id="bt_audio_proxy_sync_profile_TSS_is_ongoing__bt_audio_proxy_ctx_tP"></a> <a id="bt__audio__proxy_8h_1aea276f6882a8a7a3797f42697498ab38"></a> bool bt\_audio\_proxy\_sync\_profile\_TSS\_is\_ongoing([bt\_audio\_proxy\_ctx\_t](#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*p\_proxy\_ctx)
:   Check that the tws switch or sync profile is ongoing.

    The device execute procedure of the tws switch or sync profile

    参数:
    :   **p\_proxy\_ctx** – **\[in\]** pointer to a proxy context of type [bt\_audio\_proxy\_ctx\_t](#structbt__audio__proxy__ctx__t)

    返回值:
    :   - **true** – ongoing
        - **false** – inactive

    返回:
    :   result

<a id="_CPPv433bt_audio_proxy_update_race_statusP20bt_audio_proxy_ctx_t20bt_audio_race_status"></a>

<a id="_CPPv333bt_audio_proxy_update_race_statusP20bt_audio_proxy_ctx_t20bt_audio_race_status"></a> <a id="_CPPv233bt_audio_proxy_update_race_statusP20bt_audio_proxy_ctx_t20bt_audio_race_status"></a> <a id="bt_audio_proxy_update_race_status__bt_audio_proxy_ctx_tP.bt_audio_race_status"></a> <a id="bt__audio__proxy_8h_1a182c4df4437b868f79b5f61ab6decf60"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_update\_race\_status([bt\_audio\_proxy\_ctx\_t](#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*p\_proxy\_ctx, [bt\_audio\_race\_status](#_CPPv420bt_audio_race_status "bt_audio_race_status") status)
:   Update and process race status.

    Update device race status

    参数:
    :   - **p\_proxy\_ctx** – **\[in\]** pointer to a proxy context of type [bt\_audio\_proxy\_ctx\_t](#structbt__audio__proxy__ctx__t)
        - **status** – **\[in\]** race status of type bt\_audio\_race\_status

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv432bt_audio_proxy_any_call_is_existv"></a>

<a id="_CPPv332bt_audio_proxy_any_call_is_existv"></a> <a id="_CPPv232bt_audio_proxy_any_call_is_existv"></a> <a id="bt_audio_proxy_any_call_is_exist__void"></a> <a id="bt__audio__proxy_8h_1a9632760510da4f6a1acb6cf783370469"></a> bool bt\_audio\_proxy\_any\_call\_is\_exist(void)
:   Check that any call is existed.

    Any call is exist

    返回值:
    :   - **true** – existed
        - **false** – not existed

    返回:
    :   results

<a id="_CPPv435bt_audio_proxy_update_hfcall_activeP20bt_audio_proxy_ctx_t"></a>

<a id="_CPPv335bt_audio_proxy_update_hfcall_activeP20bt_audio_proxy_ctx_t"></a> <a id="_CPPv235bt_audio_proxy_update_hfcall_activeP20bt_audio_proxy_ctx_t"></a> <a id="bt_audio_proxy_update_hfcall_active__bt_audio_proxy_ctx_tP"></a> <a id="bt__audio__proxy_8h_1a8e34fb2adc3cbe6f9bba1a09121e65cd"></a> void bt\_audio\_proxy\_update\_hfcall\_active([bt\_audio\_proxy\_ctx\_t](#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*p\_proxy\_ctx)
:   Update and process hfcall active status.

    Update hfcall active

    参数:
    :   **p\_proxy\_ctx** – **\[in\]** pointer to a proxy context of type [bt\_audio\_proxy\_ctx\_t](#structbt__audio__proxy__ctx__t)

    返回:
    :   N/A

<a id="_CPPv429bt_audio_proxy_tx_profile_cmdP20bt_audio_proxy_ctx_t23bt_audio_proxy_cmd_id_tPK7uint8_t8uint16_t"></a>

<a id="_CPPv329bt_audio_proxy_tx_profile_cmdP20bt_audio_proxy_ctx_t23bt_audio_proxy_cmd_id_tPK7uint8_t8uint16_t"></a> <a id="_CPPv229bt_audio_proxy_tx_profile_cmdP20bt_audio_proxy_ctx_t23bt_audio_proxy_cmd_id_tPK7uint8_t8uint16_t"></a> <a id="bt_audio_proxy_tx_profile_cmd__bt_audio_proxy_ctx_tP.bt_audio_proxy_cmd_id_t.uint8_tCP.uint16_t"></a> <a id="bt__audio__proxy_8h_1aee890d2eed106fee88ba05ae7a17f9d8"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_tx\_profile\_cmd([bt\_audio\_proxy\_ctx\_t](#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*p\_proxy\_ctx, [bt\_audio\_proxy\_cmd\_id\_t](#_CPPv423bt_audio_proxy_cmd_id_t "bt_audio_proxy_cmd_id_t") cmd, const uint8\_t \*p\_data, uint16\_t len)
:   Send profile command to paired earbud.

    Send profile(HFP.AVRCP A2dp) command

    参数:
    :   - **p\_proxy\_ctx** – **\[in\]** pointer to a proxy context of type [bt\_audio\_proxy\_ctx\_t](#structbt__audio__proxy__ctx__t)
        - **cmd** – **\[in\]** profile command of type bt\_audio\_proxy\_cmd\_id\_t
        - **p\_data** – **\[in\]** pointer to profile command information
        - **len** – **\[in\]** length of profile command information

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426bt_audio_proxy_tx_conn_cmd14btif_bd_addr_t23bt_audio_proxy_cmd_id_t"></a>

<a id="_CPPv326bt_audio_proxy_tx_conn_cmd14btif_bd_addr_t23bt_audio_proxy_cmd_id_t"></a> <a id="_CPPv226bt_audio_proxy_tx_conn_cmd14btif_bd_addr_t23bt_audio_proxy_cmd_id_t"></a> <a id="bt_audio_proxy_tx_conn_cmd__btif_bd_addr_t.bt_audio_proxy_cmd_id_t"></a> <a id="bt__audio__proxy_8h_1a593baed47e870810486dceb0893e7299"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_tx\_conn\_cmd([btif\_bd\_addr\_t](../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr, [bt\_audio\_proxy\_cmd\_id\_t](#_CPPv423bt_audio_proxy_cmd_id_t "bt_audio_proxy_cmd_id_t") cmd)
:   Send profile connection or disconnection command to paired earbud.

    Send profile connection or disconnection command

    参数:
    :   - **addr** – **\[in\]** pointer to address of type [btif\_bd\_addr\_t](../btif/btif_type.md#structbtif__bd__addr__t)
        - **cmd** – **\[in\]** profile command of type bt\_audio\_proxy\_cmd\_id\_t

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422bt_audio_proxy_vol_set19audio_stream_type_t8uint16_t7uint8_t"></a>

<a id="_CPPv322bt_audio_proxy_vol_set19audio_stream_type_t8uint16_t7uint8_t"></a> <a id="_CPPv222bt_audio_proxy_vol_set19audio_stream_type_t8uint16_t7uint8_t"></a> <a id="bt_audio_proxy_vol_set__audio_stream_type_t.uint16_t.uint8_t"></a> <a id="bt__audio__proxy_8h_1ab23d9e02ba45976a5121a8dad567e826"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_vol\_set([audio\_stream\_type\_t](#_CPPv419audio_stream_type_t "audio_stream_type_t") type, uint16\_t handle, uint8\_t vol\_level)
:   Set audio volume level.

    Set volume

    参数:
    :   - **type** – **\[in\]** stream type of type audio\_stream\_type\_t
        - **handle** – **\[in\]** connection handle
        - **vol\_level** – **\[in\]** audio volume level, range 0 to 15

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421bt_audio_proxy_vol_up7uint8_t"></a>

<a id="_CPPv321bt_audio_proxy_vol_up7uint8_t"></a> <a id="_CPPv221bt_audio_proxy_vol_up7uint8_t"></a> <a id="bt_audio_proxy_vol_up__uint8_t"></a> <a id="bt__audio__proxy_8h_1ab8e8dd1323bcf9d4a354375275249dd3"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_vol\_up(uint8\_t step\_size)
:   Turn up the audio volume.

    set (a2dp or hfp) volume up according to the current context(a2dp or hfp)

    参数:
    :   **step\_size** – **\[in\]** : The step of volume level up

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv423bt_audio_proxy_vol_down7uint8_t"></a>

<a id="_CPPv323bt_audio_proxy_vol_down7uint8_t"></a> <a id="_CPPv223bt_audio_proxy_vol_down7uint8_t"></a> <a id="bt_audio_proxy_vol_down__uint8_t"></a> <a id="bt__audio__proxy_8h_1a5f06485933a08fb0a1a69c7f91b1f17b"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_vol\_down(uint8\_t step\_size)
:   Turn down the audio volume.

    set (a2dp or hfp)volume down according to the current context(a2dp or hfp)

    参数:
    :   **step\_size** – **\[in\]** : The step of the volume level down

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426bt_audio_proxy_get_dft_volP20bt_audio_proxy_ctx_t19audio_stream_type_t"></a>

<a id="_CPPv326bt_audio_proxy_get_dft_volP20bt_audio_proxy_ctx_t19audio_stream_type_t"></a> <a id="_CPPv226bt_audio_proxy_get_dft_volP20bt_audio_proxy_ctx_t19audio_stream_type_t"></a> <a id="bt_audio_proxy_get_dft_vol__bt_audio_proxy_ctx_tP.audio_stream_type_t"></a> <a id="bt__audio__proxy_8h_1a5d8f7ec9740c172c03b4ecb9a9814229"></a> uint8\_t bt\_audio\_proxy\_get\_dft\_vol([bt\_audio\_proxy\_ctx\_t](#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*p\_proxy\_ctx, [audio\_stream\_type\_t](#_CPPv419audio_stream_type_t "audio_stream_type_t") stream\_type)
:   Get default audio volume.

    Get the default audio volume for stream type \[stream\_type\] in the proxy context \[p\_proxy\_ctx\].

    参数:
    :   - **p\_proxy\_ctx** – **\[in\]** pointer to a proxy context of type [bt\_audio\_proxy\_ctx\_t](#structbt__audio__proxy__ctx__t)
        - **stream\_type** – **\[in\]** stream type of type audio\_stream\_type\_t

    返回:
    :   audio volume, range 0 to 15\.

<a id="_CPPv423bt_audio_proxy_set_mute19audio_stream_type_tb"></a>

<a id="_CPPv323bt_audio_proxy_set_mute19audio_stream_type_tb"></a> <a id="_CPPv223bt_audio_proxy_set_mute19audio_stream_type_tb"></a> <a id="bt_audio_proxy_set_mute__audio_stream_type_t.b"></a> <a id="bt__audio__proxy_8h_1ae4b4e2c34100a12c5a767876bb5e0a12"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_set\_mute([audio\_stream\_type\_t](#_CPPv419audio_stream_type_t "audio_stream_type_t") type, bool mute\_state)
:   Set DSP mute mode.

    Set DSP mute mode

    参数:
    :   - **type** – **\[in\]** stream type of type audio\_stream\_type\_t
        - **mute\_state** – **\[in\]** mute state. true: MUTE, false:UNMUTE

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv423bt_audio_proxy_get_mute19audio_stream_type_tPb"></a>

<a id="_CPPv323bt_audio_proxy_get_mute19audio_stream_type_tPb"></a> <a id="_CPPv223bt_audio_proxy_get_mute19audio_stream_type_tPb"></a> <a id="bt_audio_proxy_get_mute__audio_stream_type_t.bP"></a> <a id="bt__audio__proxy_8h_1af6ac45f4c5d6b46f3d5b8bf08c9a0aab"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_get\_mute([audio\_stream\_type\_t](#_CPPv419audio_stream_type_t "audio_stream_type_t") type, bool \*p\_mute\_state)
:   Get DSP Mute mode.

    Get DSP Mute mode

    参数:
    :   - **type** – **\[in\]** stream type of type audio\_stream\_type\_t
        - **p\_mute\_state** – **\[in\]** pointer to mute state. true: MUTE, false:UNMUTE

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv431bt_audio_proxy_avrcp_play_pausev"></a>

<a id="_CPPv331bt_audio_proxy_avrcp_play_pausev"></a> <a id="_CPPv231bt_audio_proxy_avrcp_play_pausev"></a> <a id="bt_audio_proxy_avrcp_play_pause__void"></a> <a id="bt__audio__proxy_8h_1abcd1ac2612ef8bad4cf202b8a9f26681"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_avrcp\_play\_pause(void)
:   Toggle play or pause audio by profile command.

    Play or pause music

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425bt_audio_proxy_avrcp_nextv"></a>

<a id="_CPPv325bt_audio_proxy_avrcp_nextv"></a> <a id="_CPPv225bt_audio_proxy_avrcp_nextv"></a> <a id="bt_audio_proxy_avrcp_next__void"></a> <a id="bt__audio__proxy_8h_1a4ffc996bfec1af38146e64d567c988ec"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_avrcp\_next(void)
:   play next music by profile command.

    send avrcp next command

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv429bt_audio_proxy_avrcp_previousv"></a>

<a id="_CPPv329bt_audio_proxy_avrcp_previousv"></a> <a id="_CPPv229bt_audio_proxy_avrcp_previousv"></a> <a id="bt_audio_proxy_avrcp_previous__void"></a> <a id="bt__audio__proxy_8h_1a54b9dd59f81e27fd1dec089f25fb5bac"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_avrcp\_previous(void)
:   play previous music by profile command.

    Send avrcp privious command

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv439bt_audio_proxy_avrcp_fast_forward_startv"></a>

<a id="_CPPv339bt_audio_proxy_avrcp_fast_forward_startv"></a> <a id="_CPPv239bt_audio_proxy_avrcp_fast_forward_startv"></a> <a id="bt_audio_proxy_avrcp_fast_forward_start__void"></a> <a id="bt__audio__proxy_8h_1a348a1e82dac00d69e9769f6039decc9f"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_avrcp\_fast\_forward\_start(void)
:   Start fast forward music by profile command.

    Send fast forward start command

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv438bt_audio_proxy_avrcp_fast_forward_stopv"></a>

<a id="_CPPv338bt_audio_proxy_avrcp_fast_forward_stopv"></a> <a id="_CPPv238bt_audio_proxy_avrcp_fast_forward_stopv"></a> <a id="bt_audio_proxy_avrcp_fast_forward_stop__void"></a> <a id="bt__audio__proxy_8h_1a151957c27cb4f68015d8478d78cf5a88"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_avrcp\_fast\_forward\_stop(void)
:   Stop fast forward music by profile command.

    Send fast forward stop command

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv439bt_audio_proxy_avtive_dev_set_delay_rpt8uint16_t"></a>

<a id="_CPPv339bt_audio_proxy_avtive_dev_set_delay_rpt8uint16_t"></a> <a id="_CPPv239bt_audio_proxy_avtive_dev_set_delay_rpt8uint16_t"></a> <a id="bt_audio_proxy_avtive_dev_set_delay_rpt__uint16_t"></a> <a id="bt__audio__proxy_8h_1aeb7e885198df07106064c95e2df7db17"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_avtive\_dev\_set\_delay\_rpt(uint16\_t delay\_rpt\_100us)
:   send a2dp delay report command.

    Send a2dp delay report command

    参数:
    :   **delay\_rpt\_100us** – **\[in\]** delay report value(uint:100us)

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv433bt_audio_proxy_avrcp_rewind_startv"></a>

<a id="_CPPv333bt_audio_proxy_avrcp_rewind_startv"></a> <a id="_CPPv233bt_audio_proxy_avrcp_rewind_startv"></a> <a id="bt_audio_proxy_avrcp_rewind_start__void"></a> <a id="bt__audio__proxy_8h_1a1720008ad43b5328eb5c5aaec1badbce"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_avrcp\_rewind\_start(void)
:   Start rewind music by profile command.

    Send rewind start command

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv432bt_audio_proxy_avrcp_rewind_stopv"></a>

<a id="_CPPv332bt_audio_proxy_avrcp_rewind_stopv"></a> <a id="_CPPv232bt_audio_proxy_avrcp_rewind_stopv"></a> <a id="bt_audio_proxy_avrcp_rewind_stop__void"></a> <a id="bt__audio__proxy_8h_1a1f5c33b15a0b3aeef2a0f39c392035c3"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_avrcp\_rewind\_stop(void)
:   Stop rewind music by profile command.

    Send rewind stop command

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv433bt_audio_proxy_redial_last_number8uint16_t"></a>

<a id="_CPPv333bt_audio_proxy_redial_last_number8uint16_t"></a> <a id="_CPPv233bt_audio_proxy_redial_last_number8uint16_t"></a> <a id="bt_audio_proxy_redial_last_number__uint16_t"></a> <a id="bt__audio__proxy_8h_1a8c1e89f7a6e8a5d60f08ed3497376d46"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_redial\_last\_number(uint16\_t handle)
:   redial last number by profile command.

    send hfp redial last bumber command

    参数:
    :   **handle** – **\[in\]** hfp connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426bt_audio_proxy_dial_number8uint16_tP7uint8_t7uint8_t"></a>

<a id="_CPPv326bt_audio_proxy_dial_number8uint16_tP7uint8_t7uint8_t"></a> <a id="_CPPv226bt_audio_proxy_dial_number8uint16_tP7uint8_t7uint8_t"></a> <a id="bt_audio_proxy_dial_number__uint16_t.uint8_tP.uint8_t"></a> <a id="bt__audio__proxy_8h_1ab5d3ba13ba2b761ece33a2f1754e5c14"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_dial\_number(uint16\_t handle, uint8\_t \*p\_data, uint8\_t len)
:   dial number by profile command.

    send HFP dial number command

    参数:
    :   - **handle** – **\[in\]** hfp connection handle
        - **p\_data** – **\[in\]** pointer to phone number string of type ASCII
        - **len** – **\[in\]** length of phone number string

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv428bt_audio_proxy_call_terminal8uint16_t"></a>

<a id="_CPPv328bt_audio_proxy_call_terminal8uint16_t"></a> <a id="_CPPv228bt_audio_proxy_call_terminal8uint16_t"></a> <a id="bt_audio_proxy_call_terminal__uint16_t"></a> <a id="bt__audio__proxy_8h_1acb5e99c486336dfcba71ebfa6c3c1ea5"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_call\_terminal(uint16\_t handle)
:   terminate call by profile command.

    Send call terminal command

    参数:
    :   **handle** – **\[in\]** hfp connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426bt_audio_proxy_call_accept8uint16_t"></a>

<a id="_CPPv326bt_audio_proxy_call_accept8uint16_t"></a> <a id="_CPPv226bt_audio_proxy_call_accept8uint16_t"></a> <a id="bt_audio_proxy_call_accept__uint16_t"></a> <a id="bt__audio__proxy_8h_1a6739c55a0047d753c618c200dff5a070"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_call\_accept(uint16\_t handle)
:   accept call by profile command.

    Send call accept command

    参数:
    :   **handle** – **\[in\]** hfp connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426bt_audio_proxy_call_reject8uint16_t"></a>

<a id="_CPPv326bt_audio_proxy_call_reject8uint16_t"></a> <a id="_CPPv226bt_audio_proxy_call_reject8uint16_t"></a> <a id="bt_audio_proxy_call_reject__uint16_t"></a> <a id="bt__audio__proxy_8h_1a4ef8cf7b3caef684a2a68f59dc6b6c7c"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_call\_reject(uint16\_t handle)
:   reject call by profile command.

    Send call reject command

    参数:
    :   **handle** – **\[in\]** hfp connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv428bt_audio_proxy_hf_bat_report8uint16_t7uint8_t"></a>

<a id="_CPPv328bt_audio_proxy_hf_bat_report8uint16_t7uint8_t"></a> <a id="_CPPv228bt_audio_proxy_hf_bat_report8uint16_t7uint8_t"></a> <a id="bt_audio_proxy_hf_bat_report__uint16_t.uint8_t"></a> <a id="bt__audio__proxy_8h_1a406e16b0088abf93c6f6234e08677d52"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_hf\_bat\_report(uint16\_t handle, uint8\_t bat\_level)
:   Send the HFP battery level by profile command.

    Send Battery level accrod hfp

    参数:
    :   - **handle** – **\[in\]** hfp connection handle
        - **bat\_level** – **\[in\]** battery level

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427bt_audio_proxy_hf_vr_enable8uint16_t7uint8_t"></a>

<a id="_CPPv327bt_audio_proxy_hf_vr_enable8uint16_t7uint8_t"></a> <a id="_CPPv227bt_audio_proxy_hf_vr_enable8uint16_t7uint8_t"></a> <a id="bt_audio_proxy_hf_vr_enable__uint16_t.uint8_t"></a> <a id="bt__audio__proxy_8h_1a322614bb396ae71d2894ff2920159d37"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_hf\_vr\_enable(uint16\_t handle, uint8\_t enable)
:   Enable/disable voice recognition by profile command.

    Enable or Disable Voice Recognition Activation

    参数:
    :   - **handle** – **\[in\]** hfp connection handle
        - **enable** – **\[in\]** enable state. 0 is disable, 1 is enable.

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv434bt_audio_proxy_hf_setup_audio_conn8uint16_t"></a>

<a id="_CPPv334bt_audio_proxy_hf_setup_audio_conn8uint16_t"></a> <a id="_CPPv234bt_audio_proxy_hf_setup_audio_conn8uint16_t"></a> <a id="bt_audio_proxy_hf_setup_audio_conn__uint16_t"></a> <a id="bt__audio__proxy_8h_1ac4aec64bc1a6f7a2200f283728ebdff5"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_hf\_setup\_audio\_conn(uint16\_t handle)
:   Setup HFP audio connection by profile command.

    Setup Audio connection

    参数:
    :   **handle** – **\[in\]** hfp connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv433bt_audio_proxy_hf_disc_audio_conn8uint16_t"></a>

<a id="_CPPv333bt_audio_proxy_hf_disc_audio_conn8uint16_t"></a> <a id="_CPPv233bt_audio_proxy_hf_disc_audio_conn8uint16_t"></a> <a id="bt_audio_proxy_hf_disc_audio_conn__uint16_t"></a> <a id="bt__audio__proxy_8h_1afc064d66e8c30f8c5edda14ac3bbee3f"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_hf\_disc\_audio\_conn(uint16\_t handle)
:   Disconnect HFP audio connection by profile command.

    Disconnect Audio connection

    参数:
    :   **handle** – **\[in\]** hfp connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427bt_audio_proxy_connect_a2dpP14btif_bd_addr_t"></a>

<a id="_CPPv327bt_audio_proxy_connect_a2dpP14btif_bd_addr_t"></a> <a id="_CPPv227bt_audio_proxy_connect_a2dpP14btif_bd_addr_t"></a> <a id="bt_audio_proxy_connect_a2dp__btif_bd_addr_tP"></a> <a id="bt__audio__proxy_8h_1ac217b913a22744adb0acbda594dbd926"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_connect\_a2dp([btif\_bd\_addr\_t](../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   Connect A2DP by profile command.

    Connect A2dp API

    参数:
    :   **p\_addr** – **\[in\]** pointer to mobile phone address of type [btif\_bd\_addr\_t](../btif/btif_type.md#structbtif__bd__addr__t).

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv430bt_audio_proxy_disconnect_a2dp8uint16_t"></a>

<a id="_CPPv330bt_audio_proxy_disconnect_a2dp8uint16_t"></a> <a id="_CPPv230bt_audio_proxy_disconnect_a2dp8uint16_t"></a> <a id="bt_audio_proxy_disconnect_a2dp__uint16_t"></a> <a id="bt__audio__proxy_8h_1a7527363e36b5db25b8caf2966dd8a3ae"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_disconnect\_a2dp(uint16\_t handle)
:   Disconnect A2DP by profile command.

    Disconnect A2DP API

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv428bt_audio_proxy_connect_avrcpP14btif_bd_addr_t"></a>

<a id="_CPPv328bt_audio_proxy_connect_avrcpP14btif_bd_addr_t"></a> <a id="_CPPv228bt_audio_proxy_connect_avrcpP14btif_bd_addr_t"></a> <a id="bt_audio_proxy_connect_avrcp__btif_bd_addr_tP"></a> <a id="bt__audio__proxy_8h_1af4b61f609b6215bdf40829c199dc0ec3"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_connect\_avrcp([btif\_bd\_addr\_t](../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   Connect AVRCP by profile command.

    Connect AVRCP API

    参数:
    :   **p\_addr** – **\[in\]** pointer to mobile phone address of type [btif\_bd\_addr\_t](../btif/btif_type.md#structbtif__bd__addr__t).

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv431bt_audio_proxy_disconnect_avrcp8uint16_t"></a>

<a id="_CPPv331bt_audio_proxy_disconnect_avrcp8uint16_t"></a> <a id="_CPPv231bt_audio_proxy_disconnect_avrcp8uint16_t"></a> <a id="bt_audio_proxy_disconnect_avrcp__uint16_t"></a> <a id="bt__audio__proxy_8h_1a08f70d65e279f767368a86af675ec0ab"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_disconnect\_avrcp(uint16\_t handle)
:   Disconnect AVRCP by profile command.

    Disconnect AVRCP API

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426bt_audio_proxy_connect_hfpP14btif_bd_addr_t"></a>

<a id="_CPPv326bt_audio_proxy_connect_hfpP14btif_bd_addr_t"></a> <a id="_CPPv226bt_audio_proxy_connect_hfpP14btif_bd_addr_t"></a> <a id="bt_audio_proxy_connect_hfp__btif_bd_addr_tP"></a> <a id="bt__audio__proxy_8h_1ab0265bf12a8322de152511ed2f23fd19"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_connect\_hfp([btif\_bd\_addr\_t](../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   Connect HFP by profile command.

    Connect HFP API

    参数:
    :   **p\_addr** – **\[in\]** pointer to mobile phone address of type [btif\_bd\_addr\_t](../btif/btif_type.md#structbtif__bd__addr__t).

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv429bt_audio_proxy_disconnect_hfp8uint16_t"></a>

<a id="_CPPv329bt_audio_proxy_disconnect_hfp8uint16_t"></a> <a id="_CPPv229bt_audio_proxy_disconnect_hfp8uint16_t"></a> <a id="bt_audio_proxy_disconnect_hfp__uint16_t"></a> <a id="bt__audio__proxy_8h_1a31209f9dc95e6e2584fc67212315a3d9"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_disconnect\_hfp(uint16\_t handle)
:   Disconnect HFP by profile command.

    Disconnect HFP API

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv436bt_audio_proxy_get_avrcp_play_status8uint16_tP21btif_avrcp_play_sts_t"></a>

<a id="_CPPv336bt_audio_proxy_get_avrcp_play_status8uint16_tP21btif_avrcp_play_sts_t"></a> <a id="_CPPv236bt_audio_proxy_get_avrcp_play_status8uint16_tP21btif_avrcp_play_sts_t"></a> <a id="bt_audio_proxy_get_avrcp_play_status__uint16_t.btif_avrcp_play_sts_tP"></a> <a id="bt__audio__proxy_8h_1af3385fef5c14f0ba94758fa5b9f9c048"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_get\_avrcp\_play\_status(uint16\_t handle, [btif\_avrcp\_play\_sts\_t](../btif/btif_type.md#_CPPv421btif_avrcp_play_sts_t "btif_avrcp_play_sts_t") \*p\_play\_status)
:   Get the AVRCP play status of proxy context.

    Get AVRCP Play status API

    参数:
    :   - **handle** – **\[in\]** connection handle
        - **p\_play\_status** – **\[in\]** pointer to play status of type btif\_avrcp\_play\_sts\_t

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419bt_audio_proxy_initb"></a>

<a id="_CPPv319bt_audio_proxy_initb"></a> <a id="_CPPv219bt_audio_proxy_initb"></a> <a id="bt_audio_proxy_init__b"></a> <a id="bt__audio__proxy_8h_1a172806309fe9bedf1e0abba61f52ff0b"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_proxy\_init(bool aac\_enable)
:   Initialize aduio proxy.

    bt aduio proxy initial

    参数:
    :   **aac\_enable** – **\[in\]** AAC enable status. true is enable, false is disable.

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv437bt_audio_proxy_get_a2dp_active_handlev"></a>

<a id="_CPPv337bt_audio_proxy_get_a2dp_active_handlev"></a> <a id="_CPPv237bt_audio_proxy_get_a2dp_active_handlev"></a> <a id="bt_audio_proxy_get_a2dp_active_handle__void"></a> <a id="bt__audio__proxy_8h_1a52b849c9a50a8ed8d5858b4d9377ec36"></a> uint16\_t bt\_audio\_proxy\_get\_a2dp\_active\_handle(void)
:   Get A2DP active connection handle.

    Get the connection handle from the current a2dp proxy context.

    返回:
    :   active connection handle

<a id="_CPPv436bt_audio_proxy_get_hfp_active_handlev"></a>

<a id="_CPPv336bt_audio_proxy_get_hfp_active_handlev"></a> <a id="_CPPv236bt_audio_proxy_get_hfp_active_handlev"></a> <a id="bt_audio_proxy_get_hfp_active_handle__void"></a> <a id="bt__audio__proxy_8h_1a756f6450711a6b665e5baf6fc4a72449"></a> uint16\_t bt\_audio\_proxy\_get\_hfp\_active\_handle(void)
:   Get HFP active connection handle.

    Get the connection handle from the last hfp proxy context.

    返回:
    :   active connection handle

<a id="_CPPv426bt_audio_is_a2dp_streamingv"></a>

<a id="_CPPv326bt_audio_is_a2dp_streamingv"></a> <a id="_CPPv226bt_audio_is_a2dp_streamingv"></a> <a id="bt_audio_is_a2dp_streaming__void"></a> <a id="bt__audio__proxy_8h_1a599496188f369bd1526cbbc2b0c2c0ad"></a> bool bt\_audio\_is\_a2dp\_streaming(void)
:   Check that a2dp is streaming.

    Check that the state of current a2dp proxy context is streaming.

    返回值:
    :   - **true** – streaming
        - **false** – no streaming

    返回:
    :   result

<a id="_CPPv418bt_audio_is_sco_onv"></a>

<a id="_CPPv318bt_audio_is_sco_onv"></a> <a id="_CPPv218bt_audio_is_sco_onv"></a> <a id="bt_audio_is_sco_on__void"></a> <a id="bt__audio__proxy_8h_1ac7f0f38118a08c71ebcbcef6f5f3087a"></a> bool bt\_audio\_is\_sco\_on(void)
:   Check that SCO is turn on.

    Check that the SCO state of last hfp context is turn on.

    返回值:
    :   - **true** – no
        - **false** – off

    返回:
    :   result

<a id="_CPPv422bt_audio_proxy_get_ctx8uint16_t"></a>

<a id="_CPPv322bt_audio_proxy_get_ctx8uint16_t"></a> <a id="_CPPv222bt_audio_proxy_get_ctx8uint16_t"></a> <a id="bt_audio_proxy_get_ctx__uint16_t"></a> <a id="bt__audio__proxy_8h_1a66a9229fe48f20705552ca35f6c1c341"></a> [bt\_audio\_proxy\_ctx\_t](#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*bt\_audio\_proxy\_get\_ctx(uint16\_t handle)
:   Get audio proxy context.

    Get the audio proxy context with connection handle \[handle\].

    参数:
    :   **handle** – **\[in\]** connection handle

    返回:
    :   pointer to connection handle of type [bt\_audio\_proxy\_ctx\_t](#structbt__audio__proxy__ctx__t).

<a id="_CPPv439bt_audio_proxy_get_hf_avtive_codec_typev"></a>

<a id="_CPPv339bt_audio_proxy_get_hf_avtive_codec_typev"></a> <a id="_CPPv239bt_audio_proxy_get_hf_avtive_codec_typev"></a> <a id="bt_audio_proxy_get_hf_avtive_codec_type__void"></a> <a id="bt__audio__proxy_8h_1afc165ec8d385377a7838b724aaa47c64"></a> uint8\_t bt\_audio\_proxy\_get\_hf\_avtive\_codec\_type(void)
:   Get the active HFP codec type.

    Get HF active codec type

    返回:
    :   SCO codec type

<a id="_CPPv431bt_audio_avrcp_ct_cmd_state_ntf20btif_avrcp_cmd_sts_t20btif_avrcp_oper_id_t"></a>

<a id="_CPPv331bt_audio_avrcp_ct_cmd_state_ntf20btif_avrcp_cmd_sts_t20btif_avrcp_oper_id_t"></a> <a id="_CPPv231bt_audio_avrcp_ct_cmd_state_ntf20btif_avrcp_cmd_sts_t20btif_avrcp_oper_id_t"></a> <a id="bt_audio_avrcp_ct_cmd_state_ntf__btif_avrcp_cmd_sts_t.btif_avrcp_oper_id_t"></a> <a id="bt__audio__proxy_8h_1a0bd9af9d4b89e022c1dbc73fe006ff9a"></a> void bt\_audio\_avrcp\_ct\_cmd\_state\_ntf([btif\_avrcp\_cmd\_sts\_t](../btif/btif_type.md#_CPPv420btif_avrcp_cmd_sts_t "btif_avrcp_cmd_sts_t") cmd\_state, [btif\_avrcp\_oper\_id\_t](../btif/btif_type.md#_CPPv420btif_avrcp_oper_id_t "btif_avrcp_oper_id_t") op\_code)
:   Notification AVRCP command state.

    Notification AVRCP command state

    参数:
    :   - **cmd\_state** – **\[in\]** command state of type btif\_avrcp\_cmd\_sts\_t
        - **op\_code** – **\[in\]** opcode of type btif\_avrcp\_oper\_id\_t

    返回:
    :   N/A

<a id="_CPPv437bt_audio_proxy_get_last_hf_call_setupv"></a>

<a id="_CPPv337bt_audio_proxy_get_last_hf_call_setupv"></a> <a id="_CPPv237bt_audio_proxy_get_last_hf_call_setupv"></a> <a id="bt_audio_proxy_get_last_hf_call_setup__void"></a> <a id="bt__audio__proxy_8h_1a30d6ee4590e6571c9713e1065bf6f389"></a> [btif\_hfp\_callsetup\_t](../btif/btif_type.md#_CPPv420btif_hfp_callsetup_t "btif_hfp_callsetup_t") bt\_audio\_proxy\_get\_last\_hf\_call\_setup(void)
:   Get HFP call setup status.

    Get the HFP call setup status from the last HFP proxy context.

    返回:
    :   HFP call setup type of type btif\_hfp\_callsetup\_t

<a id="_CPPv424bt_audio_proxy_sco_exist8uint16_t"></a>

<a id="_CPPv324bt_audio_proxy_sco_exist8uint16_t"></a> <a id="_CPPv224bt_audio_proxy_sco_exist8uint16_t"></a> <a id="bt_audio_proxy_sco_exist__uint16_t"></a> <a id="bt__audio__proxy_8h_1ad0ca60f4cc20181f1fee237834ad3975"></a> bool bt\_audio\_proxy\_sco\_exist(uint16\_t handle)
:   Check that SCO exists.

    Check that the SCO of hfp context with the connection handle \[handle\] exists.

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **true** – exist
        - **false** – not exist **BT\_AUDIO\_PROXY\_H** EOF

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv417_proxy_sync_cmd_t"></a>

<a id="_CPPv317_proxy_sync_cmd_t"></a> <a id="_CPPv217_proxy_sync_cmd_t"></a> <a id="_proxy_sync_cmd_t"></a> <a id="struct__proxy__sync__cmd__t"></a> struct \_proxy\_sync\_cmd\_t
:   proxy sync command structure definition.

<a id="_CPPv427bt_audio_tws_exe_cmd_info_t"></a>

<a id="_CPPv327bt_audio_tws_exe_cmd_info_t"></a> <a id="_CPPv227bt_audio_tws_exe_cmd_info_t"></a> <a id="bt_audio_tws_exe_cmd_info_t"></a> <a id="structbt__audio__tws__exe__cmd__info__t"></a> struct bt\_audio\_tws\_exe\_cmd\_info\_t
:   TWS execute command information structure definition.

<a id="_CPPv419bt_audio_hfp_ctrl_t"></a>

<a id="_CPPv319bt_audio_hfp_ctrl_t"></a> <a id="_CPPv219bt_audio_hfp_ctrl_t"></a> <a id="bt_audio_hfp_ctrl_t"></a> <a id="structbt__audio__hfp__ctrl__t"></a> struct bt\_audio\_hfp\_ctrl\_t
:   HFP control structure definition.

<a id="_CPPv421bt_audio_avrcp_ctrl_t"></a>

<a id="_CPPv321bt_audio_avrcp_ctrl_t"></a> <a id="_CPPv221bt_audio_avrcp_ctrl_t"></a> <a id="bt_audio_avrcp_ctrl_t"></a> <a id="structbt__audio__avrcp__ctrl__t"></a> struct bt\_audio\_avrcp\_ctrl\_t
:   AVRCP control structure definition.

<a id="_CPPv426bt_audio_a2dp_codec_info_t"></a>

<a id="_CPPv326bt_audio_a2dp_codec_info_t"></a> <a id="_CPPv226bt_audio_a2dp_codec_info_t"></a> <a id="bt_audio_a2dp_codec_info_t"></a> <a id="structbt__audio__a2dp__codec__info__t"></a> struct bt\_audio\_a2dp\_codec\_info\_t
:   A2DP codec information structure definition.

<a id="_CPPv420bt_audio_a2dp_ctrl_t"></a>

<a id="_CPPv320bt_audio_a2dp_ctrl_t"></a> <a id="_CPPv220bt_audio_a2dp_ctrl_t"></a> <a id="bt_audio_a2dp_ctrl_t"></a> <a id="structbt__audio__a2dp__ctrl__t"></a> struct bt\_audio\_a2dp\_ctrl\_t
:   A2DP control structure definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20bt_audio_a2dp_ctrl_t9cp_statusE"></a>

    <a id="_CPPv3N20bt_audio_a2dp_ctrl_t9cp_statusE"></a> <a id="_CPPv2N20bt_audio_a2dp_ctrl_t9cp_statusE"></a> <a id="bt_audio_a2dp_ctrl_t::cp_status__btif_a2dp_cp_status_t"></a> <a id="structbt__audio__a2dp__ctrl__t_1ae1a51bb417cb3b1a3a837ecb38b69686"></a> [btif\_a2dp\_cp\_status\_t](../btif/btif_type.md#_CPPv421btif_a2dp_cp_status_t "btif_a2dp_cp_status_t") cp\_status
    :   context protection

<a id="_CPPv420bt_audio_proxy_ctx_t"></a>

<a id="_CPPv320bt_audio_proxy_ctx_t"></a> <a id="_CPPv220bt_audio_proxy_ctx_t"></a> <a id="bt_audio_proxy_ctx_t"></a> <a id="structbt__audio__proxy__ctx__t"></a> struct bt\_audio\_proxy\_ctx\_t
:   Audio proxy context structure definition.

<a id="macros"></a>

### Macros

<a id="c.BT_AUDIO_PROXY_LINKS_MAX"></a>

<a id="bt__audio__proxy_8h_1aaeadec384e2e3563cacc4872f64e2111"></a> BT\_AUDIO\_PROXY\_LINKS\_MAX
:   Maximum number of links for audio proxy

<a id="c.BT_AUDIO_ASSERT"></a>

<a id="bt__audio__proxy_8h_1ac42f07d56ff3a933fd716aa61621d724"></a> BT\_AUDIO\_ASSERT

<a id="c.BT_AUDIO_LOG_ERR"></a>

<a id="bt__audio__proxy_8h_1a6a7b7d5da504826a658fced8ad4d3519"></a> BT\_AUDIO\_LOG\_ERR

<a id="c.BT_AUDIO_LOG_INF"></a>

<a id="bt__audio__proxy_8h_1ada2b46f984a79593c9e58ae3ac9f0fb8"></a> BT\_AUDIO\_LOG\_INF

<a id="c.BT_AUDIO_LOG_DBG"></a>

<a id="bt__audio__proxy_8h_1a8031d9cc730c7ed1fa623f3749c405ef"></a> BT\_AUDIO\_LOG\_DBG

<a id="c.BT_AUDIO_DUMP"></a>

<a id="bt__audio__proxy_8h_1a75e68a390b5f2f8f58bb698c48ba12b2"></a> BT\_AUDIO\_DUMP

<a id="c.BT_AUDIO_HFP_CONN_BIT"></a>

<a id="bt__audio__proxy_8h_1a367c85e9354ee459258e8b710f5584cb"></a> BT\_AUDIO\_HFP\_CONN\_BIT

<a id="c.BT_AUDIO_A2DP_CONN_BIT"></a>

<a id="bt__audio__proxy_8h_1abb414cc2295cbec61094d62384a981b9"></a> BT\_AUDIO\_A2DP\_CONN\_BIT

<a id="c.BT_AUDIO_AVRCP_CONN_BIT"></a>

<a id="bt__audio__proxy_8h_1a483d802fb13a58ebe3c914244ab0cd28"></a> BT\_AUDIO\_AVRCP\_CONN\_BIT

<a id="c.BT_AUDIO_RACE_IDLE"></a>

<a id="bt__audio__proxy_8h_1aaa11868fccbf0755a3b18508eed89881"></a> BT\_AUDIO\_RACE\_IDLE

<a id="c.BT_AUDIO_RACE_PREPARE_DISCON"></a>

<a id="bt__audio__proxy_8h_1a5ced6b118dccf9a6399d279d96f8745d"></a> BT\_AUDIO\_RACE\_PREPARE\_DISCON

<a id="c.BT_AUDIO_RACE_DISCON_ONGOING"></a>

<a id="bt__audio__proxy_8h_1a56261097a680991fac4acfb64eaa82a0"></a> BT\_AUDIO\_RACE\_DISCON\_ONGOING

<a id="c.BT_AUDIO_RACE_DISCON_DONE"></a>

<a id="bt__audio__proxy_8h_1acf7ec9f9a0fc3d411afd37e011408ccd"></a> BT\_AUDIO\_RACE\_DISCON\_DONE

<a id="c.BT_AUDIO_RACE_RECONN_ONGOING"></a>

<a id="bt__audio__proxy_8h_1a43d415c568ac44506c6a7aeea7ef3379"></a> BT\_AUDIO\_RACE\_RECONN\_ONGOING

<a id="c.BT_AUDIO_RACE_TRY_PAUSE"></a>

<a id="bt__audio__proxy_8h_1af21a77adf567ecc86d5db4b77d1ee296"></a> BT\_AUDIO\_RACE\_TRY\_PAUSE

<a id="c.BT_AUDIO_PROXY_CAN_PLAY_MUSIC"></a>

<a id="bt__audio__proxy_8h_1aa335414115e8db61db1d75eaa6747041"></a> BT\_AUDIO\_PROXY\_CAN\_PLAY\_MUSIC(profile\_conn)
:   Macro for check if the profile connection bit can play music.

<a id="c.BT_AUDIO_PROXY_A2DP_IS_CONNECTED"></a>

<a id="bt__audio__proxy_8h_1a125cf1fcf31f3350bf0e25004e47b27a"></a> BT\_AUDIO\_PROXY\_A2DP\_IS\_CONNECTED(profile\_conn)
:   Macro for check if the profile connection bit is connected to A2DP.

<a id="c.BT_AUDIO_PROXY_AVRCP_IS_CONNECTED"></a>

<a id="bt__audio__proxy_8h_1a1414dd7273cc709a19d96b58bf31381d"></a> BT\_AUDIO\_PROXY\_AVRCP\_IS\_CONNECTED(profile\_conn)
:   Macro for check if the profile connection bit is connected to AVRCP.

<a id="c.BT_AUDIO_PROXY_HFP_IS_CONNECTED"></a>

<a id="bt__audio__proxy_8h_1ab5d2df328ac22bff2b7970a7f7c357c1"></a> BT\_AUDIO\_PROXY\_HFP\_IS\_CONNECTED(profile\_conn)
:   Macro for check if the profile connection bit is connected to HSP.

<a id="c.BT_AUDIO_PROXY_AVRCP_CMD_MIN"></a>

<a id="bt__audio__proxy_8h_1a9ff30669180bbfb3ce7cb07eb7ef54d0"></a> BT\_AUDIO\_PROXY\_AVRCP\_CMD\_MIN

<a id="c.BT_AUDIO_PROXY_AVRCP_PLAY"></a>

<a id="bt__audio__proxy_8h_1a964d952cdac664d5ee5a90f60ebe77e6"></a> BT\_AUDIO\_PROXY\_AVRCP\_PLAY

<a id="c.BT_AUDIO_PROXY_AVRCP_PAUSE"></a>

<a id="bt__audio__proxy_8h_1adfe57841b935919dfa3fa18590a10d0d"></a> BT\_AUDIO\_PROXY\_AVRCP\_PAUSE

<a id="c.BT_AUDIO_PROXY_AVRCP_PREVIOUS"></a>

<a id="bt__audio__proxy_8h_1a5fb6e6177f0e0fc9ae6e9b7b1100372a"></a> BT\_AUDIO\_PROXY\_AVRCP\_PREVIOUS

<a id="c.BT_AUDIO_PROXY_AVRCP_NEXT"></a>

<a id="bt__audio__proxy_8h_1a1619aba57641f4112c9f5f06c8cdb576"></a> BT\_AUDIO\_PROXY\_AVRCP\_NEXT

<a id="c.BT_AUDIO_PROXY_AVRCP_FAST_FORWORD_START"></a>

<a id="bt__audio__proxy_8h_1af286a7525cc432d7c7bd150f3419a045"></a> BT\_AUDIO\_PROXY\_AVRCP\_FAST\_FORWORD\_START

<a id="c.BT_AUDIO_PROXY_AVRCP_FAST_FORWORD_STOP"></a>

<a id="bt__audio__proxy_8h_1a06cca4e838dea2be16bb08fa9d10f8d6"></a> BT\_AUDIO\_PROXY\_AVRCP\_FAST\_FORWORD\_STOP

<a id="c.BT_AUDIO_PROXY_AVRCP_REWIND_START"></a>

<a id="bt__audio__proxy_8h_1afd44fabb8d315c3c3c500c2a8688cc33"></a> BT\_AUDIO\_PROXY\_AVRCP\_REWIND\_START

<a id="c.BT_AUDIO_PROXY_AVRCP_REWIND_STOP"></a>

<a id="bt__audio__proxy_8h_1abfb47de2c3d1d9083a63d70167923ad2"></a> BT\_AUDIO\_PROXY\_AVRCP\_REWIND\_STOP

<a id="c.BT_AUDIO_PROXY_AVRCP_CMD_MAX"></a>

<a id="bt__audio__proxy_8h_1ae99dcd0e462903f28c8cdf2e0681dd73"></a> BT\_AUDIO\_PROXY\_AVRCP\_CMD\_MAX

<a id="c.BT_AUDIO_PROXY_HFP_CMD_MIN"></a>

<a id="bt__audio__proxy_8h_1a6678d78e65425c34844ae79443768826"></a> BT\_AUDIO\_PROXY\_HFP\_CMD\_MIN

<a id="c.BT_AUDIO_PROXY_HFP_GET_CLCC"></a>

<a id="bt__audio__proxy_8h_1aff10dac19cf7b02de65deb807b958022"></a> BT\_AUDIO\_PROXY\_HFP\_GET\_CLCC

<a id="c.BT_AUDIO_PROXY_HFP_REDIAL_LAST_NUMBER"></a>

<a id="bt__audio__proxy_8h_1a27ae25113d91a3dd7f59d49978c021ca"></a> BT\_AUDIO\_PROXY\_HFP\_REDIAL\_LAST\_NUMBER

<a id="c.BT_AUDIO_PROXY_HFP_DIAL_NUMBER"></a>

<a id="bt__audio__proxy_8h_1a079591b7026157363c098d04e95bff90"></a> BT\_AUDIO\_PROXY\_HFP\_DIAL\_NUMBER

<a id="c.BT_AUDIO_PROXY_HFP_TERMINATE_CALL"></a>

<a id="bt__audio__proxy_8h_1ab699c7fbb73b23392e21ad0c3439dc74"></a> BT\_AUDIO\_PROXY\_HFP\_TERMINATE\_CALL

<a id="c.BT_AUDIO_PROXY_HFP_ACCEPT_CALL"></a>

<a id="bt__audio__proxy_8h_1a2ed79ed4faa823dd68869fa40020524d"></a> BT\_AUDIO\_PROXY\_HFP\_ACCEPT\_CALL

<a id="c.BT_AUDIO_PROXY_HFP_REJECT_CALL"></a>

<a id="bt__audio__proxy_8h_1a3cd3aea17617d6a009aaf6462560486c"></a> BT\_AUDIO\_PROXY\_HFP\_REJECT\_CALL

<a id="c.BT_AUDIO_PROXY_HFP_BAT_RPT"></a>

<a id="bt__audio__proxy_8h_1a2c76b2ffffc198849a505ab67f2de0a3"></a> BT\_AUDIO\_PROXY\_HFP\_BAT\_RPT

<a id="c.BT_AUDIO_PROXY_HFP_VR_ENABLE"></a>

<a id="bt__audio__proxy_8h_1a77f2001adf5ac9da21bb2f835b82c7f0"></a> BT\_AUDIO\_PROXY\_HFP\_VR\_ENABLE

<a id="c.BT_AUDIO_PROXY_HFP_SETUP_AUDIO_CONN"></a>

<a id="bt__audio__proxy_8h_1a7315ff22b9bf34976bda82a7530373c0"></a> BT\_AUDIO\_PROXY\_HFP\_SETUP\_AUDIO\_CONN

<a id="c.BT_AUDIO_PROXY_HFP_DISC_AUDIO_CONN"></a>

<a id="bt__audio__proxy_8h_1a4971246f0c5435a70c16c6003d7a4ae3"></a> BT\_AUDIO\_PROXY\_HFP\_DISC\_AUDIO\_CONN

<a id="c.BT_AUDIO_PROXY_HFP_CMD_MAX"></a>

<a id="bt__audio__proxy_8h_1ae2c2753b0e1857ef9053100a8760ace2"></a> BT\_AUDIO\_PROXY\_HFP\_CMD\_MAX

<a id="c.BT_AUDIO_PROXY_VOL_CMD_MIN"></a>

<a id="bt__audio__proxy_8h_1aa546b39b6f8acff675a659c637787b26"></a> BT\_AUDIO\_PROXY\_VOL\_CMD\_MIN

<a id="c.BT_AUDIO_PROXY_SET_ABS_VOL"></a>

<a id="bt__audio__proxy_8h_1a939a51bb683f961ef6ed34795199d983"></a> BT\_AUDIO\_PROXY\_SET\_ABS\_VOL

<a id="c.BT_AUDIO_PROXY_SET_SPK_VOL"></a>

<a id="bt__audio__proxy_8h_1a9c8bddeb32321d69114c3abe65730bb8"></a> BT\_AUDIO\_PROXY\_SET\_SPK\_VOL

<a id="c.BT_AUDIO_PROXY_SET_MIC_VOL"></a>

<a id="bt__audio__proxy_8h_1a02011e94688594c2e2391fc947ab2dfe"></a> BT\_AUDIO\_PROXY\_SET\_MIC\_VOL

<a id="c.BT_AUDIO_PROXY_VOL_CMD_MAX"></a>

<a id="bt__audio__proxy_8h_1a418b1621fce958a89db579f2cd5a018f"></a> BT\_AUDIO\_PROXY\_VOL\_CMD\_MAX

<a id="c.BT_AUDIO_PROXY_CONN_CMD_MIN"></a>

<a id="bt__audio__proxy_8h_1a09881420152a569b98665d359bedf210"></a> BT\_AUDIO\_PROXY\_CONN\_CMD\_MIN

<a id="c.BT_AUDIO_PROXY_CONN_A2DP"></a>

<a id="bt__audio__proxy_8h_1ab32fff9eae9da8a7a0aa9657d36a988a"></a> BT\_AUDIO\_PROXY\_CONN\_A2DP

<a id="c.BT_AUDIO_PROXY_CONN_AVRCP"></a>

<a id="bt__audio__proxy_8h_1a73819ce0f631502fcb1d02df6c5afcd0"></a> BT\_AUDIO\_PROXY\_CONN\_AVRCP

<a id="c.BT_AUDIO_PROXY_CONN_HFP"></a>

<a id="bt__audio__proxy_8h_1a70a809ff27360343ef20f011e2aedc20"></a> BT\_AUDIO\_PROXY\_CONN\_HFP

<a id="c.BT_AUDIO_PROXY_RACE_RECONN_A2DP"></a>

<a id="bt__audio__proxy_8h_1ad891064546d1ec908f43a0b803af76d3"></a> BT\_AUDIO\_PROXY\_RACE\_RECONN\_A2DP

<a id="c.BT_AUDIO_PROXY_RACE_RECONN_AVRCP"></a>

<a id="bt__audio__proxy_8h_1afadd9d8efe3e8e18e743fd26b2bbe5db"></a> BT\_AUDIO\_PROXY\_RACE\_RECONN\_AVRCP

<a id="c.BT_AUDIO_PROXY_DISCON_A2DP"></a>

<a id="bt__audio__proxy_8h_1ae07e0185f7b2dae55407e181c7ba95bd"></a> BT\_AUDIO\_PROXY\_DISCON\_A2DP

<a id="c.BT_AUDIO_PROXY_DISCON_AVRCP"></a>

<a id="bt__audio__proxy_8h_1a7f008bd72e6c792805f7de2a36c1b616"></a> BT\_AUDIO\_PROXY\_DISCON\_AVRCP

<a id="c.BT_AUDIO_PROXY_DISCON_HFP"></a>

<a id="bt__audio__proxy_8h_1ac4ecce1b529df1c0a9bd44f3ec6c431d"></a> BT\_AUDIO\_PROXY\_DISCON\_HFP

<a id="c.BT_AUDIO_PROXY_RACE_DISCON_A2DP"></a>

<a id="bt__audio__proxy_8h_1a1e56bfcc568f56f4571963468645f101"></a> BT\_AUDIO\_PROXY\_RACE\_DISCON\_A2DP

<a id="c.BT_AUDIO_PROXY_RACE_DISCON_AVRCP"></a>

<a id="bt__audio__proxy_8h_1ab605b29775377271287beddb4c9a17cc"></a> BT\_AUDIO\_PROXY\_RACE\_DISCON\_AVRCP

<a id="c.BT_AUDIO_PROXY_CONN_CMD_MAX"></a>

<a id="bt__audio__proxy_8h_1a93c5bd6f0229147f49b3805c80eb42ae"></a> BT\_AUDIO\_PROXY\_CONN\_CMD\_MAX

<a id="c.BT_AUDIO_PENDING_CMD_PARAM_LEN_MAX"></a>

<a id="bt__audio__proxy_8h_1a76cd0d43e8d67e7ad3b853c176d399d0"></a> BT\_AUDIO\_PENDING\_CMD\_PARAM\_LEN\_MAX

<a id="c.BT_AUDIO_AVRCP_W4_IDLE"></a>

<a id="bt__audio__proxy_8h_1af86ca61293ecf1112849966667cd6145"></a> BT\_AUDIO\_AVRCP\_W4\_IDLE

<a id="c.BT_AUDIO_AVRCP_W4_PLAY"></a>

<a id="bt__audio__proxy_8h_1a6d376e7f864ca6884def9d5a6a8de67f"></a> BT\_AUDIO\_AVRCP\_W4\_PLAY

<a id="c.BT_AUDIO_AVRCP_W4_PAUSE"></a>

<a id="bt__audio__proxy_8h_1ad65e64120cde7fe3b5b14f217ea0d140"></a> BT\_AUDIO\_AVRCP\_W4\_PAUSE

<a id="c.MEDIA_IS_PLAYING"></a>

<a id="bt__audio__proxy_8h_1ac62ec34de9ca51b9dd7d6d7bd8c3966c"></a> MEDIA\_IS\_PLAYING(play\_status)
:   Macro for check if the play status is playing.

<a id="c.MEDIA_IS_STOPED"></a>

<a id="bt__audio__proxy_8h_1a50c54be7e9813a44bccf8fd8a2162f05"></a> MEDIA\_IS\_STOPED(play\_status)
:   Macro for check if the play status is stopped.

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv427bt_audio_profile_conn_bit_t"></a>

<a id="_CPPv327bt_audio_profile_conn_bit_t"></a> <a id="_CPPv227bt_audio_profile_conn_bit_t"></a> <a id="bt_audio_profile_conn_bit_t"></a> <a id="bt__audio__proxy_8h_1aa5980af801295e74ec24fbd7f60fa41a"></a> typedef uint32\_t bt\_audio\_profile\_conn\_bit\_t
:   audio profile connection bit definition.

<a id="_CPPv420bt_audio_race_status"></a>

<a id="_CPPv320bt_audio_race_status"></a> <a id="_CPPv220bt_audio_race_status"></a> <a id="bt_audio_race_status"></a> <a id="bt__audio__proxy_8h_1ac9ab736b614d6b49c05df9287eb226f9"></a> typedef uint8\_t bt\_audio\_race\_status
:   audio race status definition.

<a id="_CPPv423bt_audio_proxy_cmd_id_t"></a>

<a id="_CPPv323bt_audio_proxy_cmd_id_t"></a> <a id="_CPPv223bt_audio_proxy_cmd_id_t"></a> <a id="bt_audio_proxy_cmd_id_t"></a> <a id="bt__audio__proxy_8h_1a97e7c7da6c37495624e44e87dcd9c361"></a> typedef uint8\_t bt\_audio\_proxy\_cmd\_id\_t
:   Audio proxy command id definition.

<a id="_CPPv424bt_audio_avrcp_w4_status"></a>

<a id="_CPPv324bt_audio_avrcp_w4_status"></a> <a id="_CPPv224bt_audio_avrcp_w4_status"></a> <a id="bt_audio_avrcp_w4_status"></a> <a id="bt__audio__proxy_8h_1add8fd9910dd9ffb4e7584fa475608fce"></a> typedef uint8\_t bt\_audio\_avrcp\_w4\_status
:   AVRCP wait state definition.

<a id="_CPPv433_sync_cmd_status_change_handle_fp"></a>

<a id="_CPPv333_sync_cmd_status_change_handle_fp"></a> <a id="_CPPv233_sync_cmd_status_change_handle_fp"></a> <a id="_sync_cmd_status_change_handle_fp"></a> <a id="bt__audio__proxy_8h_1a997ad57ad945ae36caaa146a1f5ccb12"></a> typedef void (\*\_sync\_cmd\_status\_change\_handle\_fp)(uint16\_t handle, bool sync\_cmd\_onging)
:   sync command status change handle function pointer definition.

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv419audio_stream_type_t"></a>

<a id="_CPPv319audio_stream_type_t"></a> <a id="_CPPv219audio_stream_type_t"></a> <a id="bt__audio__proxy_8h_1a617edfb76567ff93543b9ee637a07d5c"></a> enum audio\_stream\_type\_t
:   Audio stream type enumeration definition.

    *Values:*

    <a id="_CPPv4N19audio_stream_type_t22AUDIO_STREAM_TYPE_A2DPE"></a>

    <a id="_CPPv3N19audio_stream_type_t22AUDIO_STREAM_TYPE_A2DPE"></a> <a id="_CPPv2N19audio_stream_type_t22AUDIO_STREAM_TYPE_A2DPE"></a> <a id="bt__audio__proxy_8h_1a617edfb76567ff93543b9ee637a07d5ca3a973583af7ce952f9e8e9e19177e990"></a> enumerator AUDIO\_STREAM\_TYPE\_A2DP

    <a id="_CPPv4N19audio_stream_type_t21AUDIO_STREAM_TYPE_HFPE"></a>

    <a id="_CPPv3N19audio_stream_type_t21AUDIO_STREAM_TYPE_HFPE"></a> <a id="_CPPv2N19audio_stream_type_t21AUDIO_STREAM_TYPE_HFPE"></a> <a id="bt__audio__proxy_8h_1a617edfb76567ff93543b9ee637a07d5ca6a7a56d8daae07ec477340d19649a5e6"></a> enumerator AUDIO\_STREAM\_TYPE\_HFP

    <a id="_CPPv4N19audio_stream_type_t29AUDIO_STREAM_TYPE_LOCAL_MEDIAE"></a>

    <a id="_CPPv3N19audio_stream_type_t29AUDIO_STREAM_TYPE_LOCAL_MEDIAE"></a> <a id="_CPPv2N19audio_stream_type_t29AUDIO_STREAM_TYPE_LOCAL_MEDIAE"></a> <a id="bt__audio__proxy_8h_1a617edfb76567ff93543b9ee637a07d5caf808c8afa2a806572d1b3d53127915c2"></a> enumerator AUDIO\_STREAM\_TYPE\_LOCAL\_MEDIA

    <a id="_CPPv4N19audio_stream_type_t26AUDIO_STREAM_TYPE_MIC_GAINE"></a>

    <a id="_CPPv3N19audio_stream_type_t26AUDIO_STREAM_TYPE_MIC_GAINE"></a> <a id="_CPPv2N19audio_stream_type_t26AUDIO_STREAM_TYPE_MIC_GAINE"></a> <a id="bt__audio__proxy_8h_1a617edfb76567ff93543b9ee637a07d5ca077f23fa37803278f9fb0246ee23fd75"></a> enumerator AUDIO\_STREAM\_TYPE\_MIC\_GAIN
