---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/btif/hfp_if.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="hfp-interface-functions"></a>

# HFP Interface Functions

<a id="hfp-if-api-brief"></a>

## HFP\_IF API Brief

| Application | Brief |
| --- | --- |
| [`hfp_if_register_event_callback()`](#_CPPv430hfp_if_register_event_callbackP19btif_hfp_register_t "hfp_if_register_event_callback") | used to register HFP event callback function |
| [`hfp_if_hf_in_bandring_is_active()`](#_CPPv431hfp_if_hf_in_bandring_is_active8uint16_t "hfp_if_hf_in_bandring_is_active") | check if bandring is ongoing |
| [`hfp_if_hf_CLCC_get_current_calls_list()`](#_CPPv437hfp_if_hf_CLCC_get_current_calls_list8uint16_t "hfp_if_hf_CLCC_get_current_calls_list") | Get current call list |
| [`hfp_if_hf_BLDN_last_dailed_number()`](#_CPPv433hfp_if_hf_BLDN_last_dailed_number8uint16_t "hfp_if_hf_BLDN_last_dailed_number") | trigger last dailed |
| [`hfp_if_hf_ATD_dial_number()`](#_CPPv425hfp_if_hf_ATD_dial_number8uint16_tPc "hfp_if_hf_ATD_dial_number") | Trigger dial by call number |
| [`hfp_if_hf_CHUP_terminal_call()`](#_CPPv428hfp_if_hf_CHUP_terminal_call8uint16_t "hfp_if_hf_CHUP_terminal_call") | Terminal call |
| [`hfp_if_hf_ATA_answer_call()`](#_CPPv425hfp_if_hf_ATA_answer_call8uint16_t "hfp_if_hf_ATA_answer_call") | Answer call |
| [`hfp_if_hf_IPHONEACCEV_bat_level()`](#_CPPv431hfp_if_hf_IPHONEACCEV_bat_level8uint16_t7uint8_t "hfp_if_hf_IPHONEACCEV_bat_level") | Report battery level |
| [`hfp_if_hf_report_spk_gain()`](#_CPPv425hfp_if_hf_report_spk_gain8uint16_t7uint8_t "hfp_if_hf_report_spk_gain") | Report speaker gain |
| [`hfp_if_hf_report_mic_gain()`](#_CPPv425hfp_if_hf_report_mic_gain8uint16_t7uint8_t "hfp_if_hf_report_mic_gain") | Report microphone gain |
| [`hfp_if_hf_voice_recog()`](#_CPPv421hfp_if_hf_voice_recog8uint16_t7uint8_t "hfp_if_hf_voice_recog") | Enable or Disable Voice Recognition Activation |
| [`hfp_if_hf_setup_audio_connection()`](#_CPPv432hfp_if_hf_setup_audio_connection8uint16_t "hfp_if_hf_setup_audio_connection") | Setup Audio connection |
| [`hfp_if_hf_disc_audio_connection()`](#_CPPv431hfp_if_hf_disc_audio_connection8uint16_t "hfp_if_hf_disc_audio_connection") | Disconnect audio connection. |
| [`hfp_if_get_sync_len()`](#_CPPv419hfp_if_get_sync_lenP14btif_bd_addr_t "hfp_if_get_sync_len") | return the hfp connection sync buffer needed size |
| [`hfp_if_conn_sync()`](#_CPPv416hfp_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t "hfp_if_conn_sync") | TWS master used to sync host stack to TWS slave |
| [`hfp_if_conn_restore()`](#_CPPv419hfp_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t "hfp_if_conn_restore") | TWS slave used to rebuild its own host stack |
| [`hfp_if_connect()`](#_CPPv414hfp_if_connectP14btif_bd_addr_t "hfp_if_connect") | reconnect HFP profile API |
| [`hfp_if_disconnect()`](#_CPPv417hfp_if_disconnect8uint16_t "hfp_if_disconnect") | disconnect HFP profile API |
| [`hfp_if_init()`](#_CPPv411hfp_if_initv "hfp_if_init") | HFP stack initialise function |
| [`hfp_if_conn_restore_specific()`](#_CPPv428hfp_if_conn_restore_specificP14btif_bd_addr_t8uint16_t "hfp_if_conn_restore_specific") | restore HFP specific variable |
| [`hfp_if_get_codec_type()`](#_CPPv421hfp_if_get_codec_typev "hfp_if_get_codec_type") | get voice using codec type |
| [`hfp_if_register_ag_handler()`](#_CPPv426hfp_if_register_ag_handler8uint16_t25hfp_if_ag_result_callbackPKc "hfp_if_register_ag_handler") | register ag cmd handler |
| [`hfp_if_hf_voice_recog_with_cb()`](#_CPPv429hfp_if_hf_voice_recog_with_cb8uint16_t7uint8_t24hfp_if_response_callback "hfp_if_hf_voice_recog_with_cb") | send vr with callback |

<a id="hfp-if-api-reference"></a>

## HFP\_IF API Reference

<a id="header-file"></a>

### Header File

- [btif/inc/hfp\_if.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/btif/inc/hfp_if.h)

<a id="functions"></a>

### Functions

<a id="_CPPv430hfp_if_register_event_callbackP19btif_hfp_register_t"></a>

<a id="_CPPv330hfp_if_register_event_callbackP19btif_hfp_register_t"></a> <a id="_CPPv230hfp_if_register_event_callbackP19btif_hfp_register_t"></a> <a id="hfp_if_register_event_callback__btif_hfp_register_tP"></a> <a id="hfp__if_8h_1a3ecfa92d39aa23cd87e7795a61d29330"></a> void hfp\_if\_register\_event\_callback([btif\_hfp\_register\_t](#_CPPv419btif_hfp_register_t "btif_hfp_register_t") \*p\_callback)
:   hfp\_if\_register\_event\_callback brief description

    used to register HFP event callback function

    参数:
    :   **p\_callback** – **\[in\]** HFP event callback struct

    返回:
    :   N/A

<a id="_CPPv431hfp_if_hf_in_bandring_is_active8uint16_t"></a>

<a id="_CPPv331hfp_if_hf_in_bandring_is_active8uint16_t"></a> <a id="_CPPv231hfp_if_hf_in_bandring_is_active8uint16_t"></a> <a id="hfp_if_hf_in_bandring_is_active__uint16_t"></a> <a id="hfp__if_8h_1aa3a25c330d0be1195e3ac50742ea6f41"></a> bool hfp\_if\_hf\_in\_bandring\_is\_active(uint16\_t handle)
:   hfp\_if\_hf\_in\_bandring\_is\_active brief description

    check if bandring is ongoing

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **true** – active
        - **fail** – no active

    返回:
    :   result

<a id="_CPPv437hfp_if_hf_CLCC_get_current_calls_list8uint16_t"></a>

<a id="_CPPv337hfp_if_hf_CLCC_get_current_calls_list8uint16_t"></a> <a id="_CPPv237hfp_if_hf_CLCC_get_current_calls_list8uint16_t"></a> <a id="hfp_if_hf_CLCC_get_current_calls_list__uint16_t"></a> <a id="hfp__if_8h_1a682662ffb8253d1e2d94bc20cf483017"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hfp\_if\_hf\_CLCC\_get\_current\_calls\_list(uint16\_t handle)
:   hfp\_if\_hf\_CLCC\_get\_current\_calls\_list brief description

    Get current call list

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv433hfp_if_hf_BLDN_last_dailed_number8uint16_t"></a>

<a id="_CPPv333hfp_if_hf_BLDN_last_dailed_number8uint16_t"></a> <a id="_CPPv233hfp_if_hf_BLDN_last_dailed_number8uint16_t"></a> <a id="hfp_if_hf_BLDN_last_dailed_number__uint16_t"></a> <a id="hfp__if_8h_1a20dc7e7c1cd7a06860722e5bed9f2e2a"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hfp\_if\_hf\_BLDN\_last\_dailed\_number(uint16\_t handle)
:   hfp\_if\_hf\_BLDN\_last\_dailed\_number brief description

    trigger last dailed

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425hfp_if_hf_ATD_dial_number8uint16_tPc"></a>

<a id="_CPPv325hfp_if_hf_ATD_dial_number8uint16_tPc"></a> <a id="_CPPv225hfp_if_hf_ATD_dial_number8uint16_tPc"></a> <a id="hfp_if_hf_ATD_dial_number__uint16_t.cP"></a> <a id="hfp__if_8h_1a60d7032c7f3b076532d51c6f558f05e3"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hfp\_if\_hf\_ATD\_dial\_number(uint16\_t handle, char \*p\_number)
:   hfp\_if\_hf\_ATD\_dial\_number brief description

    Trigger dial by call number

    参数:
    :   - **handle** – **\[in\]** connnection handle
        - **p\_number** – **\[in\]** phone number

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv428hfp_if_hf_CHUP_terminal_call8uint16_t"></a>

<a id="_CPPv328hfp_if_hf_CHUP_terminal_call8uint16_t"></a> <a id="_CPPv228hfp_if_hf_CHUP_terminal_call8uint16_t"></a> <a id="hfp_if_hf_CHUP_terminal_call__uint16_t"></a> <a id="hfp__if_8h_1a32c0dcf4a4ff206773ff577420742229"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hfp\_if\_hf\_CHUP\_terminal\_call(uint16\_t handle)
:   hfp\_if\_hf\_CHUP\_terminal\_call brief description

    Terminal call

    参数:
    :   **handle** – **\[in\]** conneciton handle

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425hfp_if_hf_ATA_answer_call8uint16_t"></a>

<a id="_CPPv325hfp_if_hf_ATA_answer_call8uint16_t"></a> <a id="_CPPv225hfp_if_hf_ATA_answer_call8uint16_t"></a> <a id="hfp_if_hf_ATA_answer_call__uint16_t"></a> <a id="hfp__if_8h_1afefa5887796cc035760d8c02f11193aa"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hfp\_if\_hf\_ATA\_answer\_call(uint16\_t handle)
:   hfp\_if\_hf\_ATA\_answer\_call brief description

    Answer call

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv431hfp_if_hf_IPHONEACCEV_bat_level8uint16_t7uint8_t"></a>

<a id="_CPPv331hfp_if_hf_IPHONEACCEV_bat_level8uint16_t7uint8_t"></a> <a id="_CPPv231hfp_if_hf_IPHONEACCEV_bat_level8uint16_t7uint8_t"></a> <a id="hfp_if_hf_IPHONEACCEV_bat_level__uint16_t.uint8_t"></a> <a id="hfp__if_8h_1afe6cd6d11fea091164a1cf94ae197924"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hfp\_if\_hf\_IPHONEACCEV\_bat\_level(uint16\_t handle, uint8\_t level)
:   hfp\_if\_hf\_IPHONEACCEV\_bat\_level brief description

    Report battery level

    参数:
    :   - **handle** – **\[in\]** connection handle
        - **level** – **\[in\]** battery level

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425hfp_if_hf_report_spk_gain8uint16_t7uint8_t"></a>

<a id="_CPPv325hfp_if_hf_report_spk_gain8uint16_t7uint8_t"></a> <a id="_CPPv225hfp_if_hf_report_spk_gain8uint16_t7uint8_t"></a> <a id="hfp_if_hf_report_spk_gain__uint16_t.uint8_t"></a> <a id="hfp__if_8h_1ada8141cd91da03b9b31306a75fd17936"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hfp\_if\_hf\_report\_spk\_gain(uint16\_t handle, uint8\_t spk\_gain)
:   hfp\_if\_hf\_report\_spk\_gain brief description

    Report speaker gain

    参数:
    :   - **handle** – **\[in\]** conneciont handle
        - **spk\_gain** – **\[in\]** VGS value

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425hfp_if_hf_report_mic_gain8uint16_t7uint8_t"></a>

<a id="_CPPv325hfp_if_hf_report_mic_gain8uint16_t7uint8_t"></a> <a id="_CPPv225hfp_if_hf_report_mic_gain8uint16_t7uint8_t"></a> <a id="hfp_if_hf_report_mic_gain__uint16_t.uint8_t"></a> <a id="hfp__if_8h_1aeca6c08fe0c583464ccb3c56d500315d"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hfp\_if\_hf\_report\_mic\_gain(uint16\_t handle, uint8\_t mic\_gain)
:   hfp\_if\_hf\_report\_mic\_gain brief description

    Report microphone gain

    参数:
    :   - **handle** – **\[in\]** connection handle
        - **mic\_gain** – **\[in\]** VGM value

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421hfp_if_hf_voice_recog8uint16_t7uint8_t"></a>

<a id="_CPPv321hfp_if_hf_voice_recog8uint16_t7uint8_t"></a> <a id="_CPPv221hfp_if_hf_voice_recog8uint16_t7uint8_t"></a> <a id="hfp_if_hf_voice_recog__uint16_t.uint8_t"></a> <a id="hfp__if_8h_1af110e75a872894c1ff90015630c9ddcc"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hfp\_if\_hf\_voice\_recog(uint16\_t handle, uint8\_t enable)
:   hfp\_if\_hf\_voice\_recog brief description

    Enable or Disable Voice Recognition Activation

    参数:
    :   - **handle** – **\[in\]** coonection handle
        - **enable** – **\[in\]** BVRA value

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv432hfp_if_hf_setup_audio_connection8uint16_t"></a>

<a id="_CPPv332hfp_if_hf_setup_audio_connection8uint16_t"></a> <a id="_CPPv232hfp_if_hf_setup_audio_connection8uint16_t"></a> <a id="hfp_if_hf_setup_audio_connection__uint16_t"></a> <a id="hfp__if_8h_1a94e967a871ad413aa8e177ce7cd17b25"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hfp\_if\_hf\_setup\_audio\_connection(uint16\_t handle)
:   hfp\_if\_hf\_setup\_audio\_connection brief description

    Setup Audio connection

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv431hfp_if_hf_disc_audio_connection8uint16_t"></a>

<a id="_CPPv331hfp_if_hf_disc_audio_connection8uint16_t"></a> <a id="_CPPv231hfp_if_hf_disc_audio_connection8uint16_t"></a> <a id="hfp_if_hf_disc_audio_connection__uint16_t"></a> <a id="hfp__if_8h_1a26de66cfc0c126fe9a4717c4a39e40ec"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hfp\_if\_hf\_disc\_audio\_connection(uint16\_t handle)
:   hfp\_if\_hf\_disc\_audio\_connection brief description

    Disconnect audio connection.

    参数:
    :   **handle** – **\[in\]** connecction handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419hfp_if_get_sync_lenP14btif_bd_addr_t"></a>

<a id="_CPPv319hfp_if_get_sync_lenP14btif_bd_addr_t"></a> <a id="_CPPv219hfp_if_get_sync_lenP14btif_bd_addr_t"></a> <a id="hfp_if_get_sync_len__btif_bd_addr_tP"></a> <a id="hfp__if_8h_1af31ebb73adc41e0e4a03f79bb639c199"></a> uint16\_t hfp\_if\_get\_sync\_len([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   hfp\_if\_get\_sync\_len brief description

    return the hfp connection sync buffer needed size

    参数:
    :   **p\_addr** – **\[in\]** remote BT MAC address

    返回:
    :   data length

<a id="_CPPv416hfp_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t"></a>

<a id="_CPPv316hfp_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t"></a> <a id="_CPPv216hfp_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t"></a> <a id="hfp_if_conn_sync__btif_bd_addr_tP.uint8_tP.uint16_t.uint16_tP"></a> <a id="hfp__if_8h_1a48047bc88c9232071d20921b9fef6583"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hfp\_if\_conn\_sync([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, uint8\_t \*p\_buff, uint16\_t buff\_len, uint16\_t \*p\_length)
:   hfp\_if\_conn\_sync brief description

    TWS master used to sync host stack to TWS slave

    参数:
    :   - **addr** – **\[in\]** remote BT MAC addresss
        - **p\_buff** – **\[out\]** buffer used to sync profile data
        - **buff\_len** – **\[in\]** p\_buff allocated length
        - **p\_length** – **\[out\]** sync profile data length will be sent

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419hfp_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t"></a>

<a id="_CPPv319hfp_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t"></a> <a id="_CPPv219hfp_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t"></a> <a id="hfp_if_conn_restore__btif_bd_addr_tP.uint8_tP.uint16_t"></a> <a id="hfp__if_8h_1af4e629a3546776b008b484dd1ca66cf4"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hfp\_if\_conn\_restore([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, uint8\_t \*p\_buff, uint16\_t length)
:   hfp\_if\_conn\_restore brief description

    TWS slave used to rebuild its own host stack

    参数:
    :   - **p\_addr** – **\[in\]** remote BT MAC address
        - **p\_buff** – **\[in\]** sync profile data
        - **length** – **\[in\]** p\_buff data length

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv414hfp_if_connectP14btif_bd_addr_t"></a>

<a id="_CPPv314hfp_if_connectP14btif_bd_addr_t"></a> <a id="_CPPv214hfp_if_connectP14btif_bd_addr_t"></a> <a id="hfp_if_connect__btif_bd_addr_tP"></a> <a id="hfp__if_8h_1a18c381db77486a9a594c0751c4456ceb"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hfp\_if\_connect([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   hfp\_if\_connect brief description

    reconnect HFP profile API

    参数:
    :   **addr** – **\[in\]** remote BT MAC address

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv417hfp_if_disconnect8uint16_t"></a>

<a id="_CPPv317hfp_if_disconnect8uint16_t"></a> <a id="_CPPv217hfp_if_disconnect8uint16_t"></a> <a id="hfp_if_disconnect__uint16_t"></a> <a id="hfp__if_8h_1aaede0e1e14bee4ec615af1bbf579f9a3"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hfp\_if\_disconnect(uint16\_t handle)
:   hfp\_if\_disconnect brief description

    disconnect HFP profile API

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv411hfp_if_initv"></a>

<a id="_CPPv311hfp_if_initv"></a> <a id="_CPPv211hfp_if_initv"></a> <a id="hfp_if_init__void"></a> <a id="hfp__if_8h_1ac72a463c8fc6aa2e9a3ee24ce7f3a9b4"></a> void hfp\_if\_init(void)
:   hfp\_if\_init brief description

    HFP stack initialise function

    返回:
    :   N/A

<a id="_CPPv428hfp_if_conn_restore_specificP14btif_bd_addr_t8uint16_t"></a>

<a id="_CPPv328hfp_if_conn_restore_specificP14btif_bd_addr_t8uint16_t"></a> <a id="_CPPv228hfp_if_conn_restore_specificP14btif_bd_addr_t8uint16_t"></a> <a id="hfp_if_conn_restore_specific__btif_bd_addr_tP.uint16_t"></a> <a id="hfp__if_8h_1a2c0db1d7a46c4c0f0576182047266647"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hfp\_if\_conn\_restore\_specific([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, uint16\_t acl\_handle)
:   hfp\_if\_conn\_restore\_specific brief description

    restore HFP specific variable

    参数:
    :   - **addr** – **\[in\]** remote BT MAC address
        - **acl\_handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421hfp_if_get_codec_typev"></a>

<a id="_CPPv321hfp_if_get_codec_typev"></a> <a id="_CPPv221hfp_if_get_codec_typev"></a> <a id="hfp_if_get_codec_type__void"></a> <a id="hfp__if_8h_1a913fc28d73387feac7485b3cce969b00"></a> uint8\_t hfp\_if\_get\_codec\_type(void)
:   hfp\_if\_get\_codec\_type brief description

    get voice using codec type

    返回:
    :   codec type @btif\_sco\_codec\_t

<a id="_CPPv426hfp_if_register_ag_handler8uint16_t25hfp_if_ag_result_callbackPKc"></a>

<a id="_CPPv326hfp_if_register_ag_handler8uint16_t25hfp_if_ag_result_callbackPKc"></a> <a id="_CPPv226hfp_if_register_ag_handler8uint16_t25hfp_if_ag_result_callbackPKc"></a> <a id="hfp_if_register_ag_handler__uint16_t.hfp_if_ag_result_callback.cCP"></a> <a id="hfp__if_8h_1a4ac08c2c6326135dcb2b512aa01bed2d"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hfp\_if\_register\_ag\_handler(uint16\_t handle, [hfp\_if\_ag\_result\_callback](#_CPPv425hfp_if_ag_result_callback "hfp_if_ag_result_callback") callback, const char \*prefix)
:   hfp\_if\_register\_ag\_handler brief description

    register ag cmd handler

    返回:
    :   result

<a id="_CPPv429hfp_if_hf_voice_recog_with_cb8uint16_t7uint8_t24hfp_if_response_callback"></a>

<a id="_CPPv329hfp_if_hf_voice_recog_with_cb8uint16_t7uint8_t24hfp_if_response_callback"></a> <a id="_CPPv229hfp_if_hf_voice_recog_with_cb8uint16_t7uint8_t24hfp_if_response_callback"></a> <a id="hfp_if_hf_voice_recog_with_cb__uint16_t.uint8_t.hfp_if_response_callback"></a> <a id="hfp__if_8h_1abddfa6258e4e71b7fcf71500a7e7d85c"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") hfp\_if\_hf\_voice\_recog\_with\_cb(uint16\_t handle, uint8\_t enable, [hfp\_if\_response\_callback](#_CPPv424hfp_if_response_callback "hfp_if_response_callback") callback)
:   hfp\_if\_hf\_voice\_recog\_with\_cb brief description

    send vr with callback

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv411if_hfp_cb_t"></a>

<a id="_CPPv311if_hfp_cb_t"></a> <a id="_CPPv211if_hfp_cb_t"></a> <a id="if_hfp_cb_t"></a> <a id="structif__hfp__cb__t"></a> struct if\_hfp\_cb\_t
:   HFP event header struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N11if_hfp_cb_t5eventE"></a>

    <a id="_CPPv3N11if_hfp_cb_t5eventE"></a> <a id="_CPPv2N11if_hfp_cb_t5eventE"></a> <a id="if_hfp_cb_t::event__btif_hfp_event_t"></a> <a id="structif__hfp__cb__t_1a0463af989464f0948c121e7e9ccba871"></a> [btif\_hfp\_event\_t](#_CPPv416btif_hfp_event_t "btif_hfp_event_t") event
    :   event index

    <a id="_CPPv4N11if_hfp_cb_t6handleE"></a>

    <a id="_CPPv3N11if_hfp_cb_t6handleE"></a> <a id="_CPPv2N11if_hfp_cb_t6handleE"></a> <a id="if_hfp_cb_t::handle__uint16_t"></a> <a id="structif__hfp__cb__t_1aa07de0228dc10c24964ad38c910664a1"></a> uint16\_t handle
    :   connection handle

<a id="_CPPv420if_slc_connect_evt_t"></a>

<a id="_CPPv320if_slc_connect_evt_t"></a> <a id="_CPPv220if_slc_connect_evt_t"></a> <a id="if_slc_connect_evt_t"></a> <a id="structif__slc__connect__evt__t"></a> struct if\_slc\_connect\_evt\_t
:   HF profile connected struct defintion.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20if_slc_connect_evt_t3hdrE"></a>

    <a id="_CPPv3N20if_slc_connect_evt_t3hdrE"></a> <a id="_CPPv2N20if_slc_connect_evt_t3hdrE"></a> <a id="if_slc_connect_evt_t::hdr__if_hfp_cb_t"></a> <a id="structif__slc__connect__evt__t_1a2b4b520309f7e75141cf74218ab80866"></a> [if\_hfp\_cb\_t](#_CPPv411if_hfp_cb_t "if_hfp_cb_t") hdr
    :   HFP event haeader

    <a id="_CPPv4N20if_slc_connect_evt_t6statusE"></a>

    <a id="_CPPv3N20if_slc_connect_evt_t6statusE"></a> <a id="_CPPv2N20if_slc_connect_evt_t6statusE"></a> <a id="if_slc_connect_evt_t::status__uint8_t"></a> <a id="structif__slc__connect__evt__t_1aa05c0cbd49fefaf352848033d009aa3b"></a> uint8\_t status
    :   removte BT MAC address

<a id="_CPPv417if_slc_disc_evt_t"></a>

<a id="_CPPv317if_slc_disc_evt_t"></a> <a id="_CPPv217if_slc_disc_evt_t"></a> <a id="if_slc_disc_evt_t"></a> <a id="structif__slc__disc__evt__t"></a> struct if\_slc\_disc\_evt\_t
:   HF profile disconn struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17if_slc_disc_evt_t3hdrE"></a>

    <a id="_CPPv3N17if_slc_disc_evt_t3hdrE"></a> <a id="_CPPv2N17if_slc_disc_evt_t3hdrE"></a> <a id="if_slc_disc_evt_t::hdr__if_hfp_cb_t"></a> <a id="structif__slc__disc__evt__t_1ac9aee4e7fd57190deaa2e13d9054066e"></a> [if\_hfp\_cb\_t](#_CPPv411if_hfp_cb_t "if_hfp_cb_t") hdr
    :   HFP event haeader

<a id="_CPPv423if_ag_ind_changed_evt_t"></a>

<a id="_CPPv323if_ag_ind_changed_evt_t"></a> <a id="_CPPv223if_ag_ind_changed_evt_t"></a> <a id="if_ag_ind_changed_evt_t"></a> <a id="structif__ag__ind__changed__evt__t"></a> struct if\_ag\_ind\_changed\_evt\_t
:   HFP \+CIEV struct defintion.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N23if_ag_ind_changed_evt_t3hdrE"></a>

    <a id="_CPPv3N23if_ag_ind_changed_evt_t3hdrE"></a> <a id="_CPPv2N23if_ag_ind_changed_evt_t3hdrE"></a> <a id="if_ag_ind_changed_evt_t::hdr__if_hfp_cb_t"></a> <a id="structif__ag__ind__changed__evt__t_1a5e866a8f6bc02876a62971b093ba2a2f"></a> [if\_hfp\_cb\_t](#_CPPv411if_hfp_cb_t "if_hfp_cb_t") hdr
    :   HFP event haeader

    <a id="_CPPv4N23if_ag_ind_changed_evt_t5valueE"></a>

    <a id="_CPPv3N23if_ag_ind_changed_evt_t5valueE"></a> <a id="_CPPv2N23if_ag_ind_changed_evt_t5valueE"></a> <a id="if_ag_ind_changed_evt_t::value__uint8_t"></a> <a id="structif__ag__ind__changed__evt__t_1aa487bb8591b789e84386bc610c392c52"></a> uint8\_t value
    :   value for CIEV index

    <a id="_CPPv4N23if_ag_ind_changed_evt_t3minE"></a>

    <a id="_CPPv3N23if_ag_ind_changed_evt_t3minE"></a> <a id="_CPPv2N23if_ag_ind_changed_evt_t3minE"></a> <a id="if_ag_ind_changed_evt_t::min__uint8_t"></a> <a id="structif__ag__ind__changed__evt__t_1aa72c049e8420266a1e8b4b712a5452c3"></a> uint8\_t min
    :   min value for CIVE index

    <a id="_CPPv4N23if_ag_ind_changed_evt_t3maxE"></a>

    <a id="_CPPv3N23if_ag_ind_changed_evt_t3maxE"></a> <a id="_CPPv2N23if_ag_ind_changed_evt_t3maxE"></a> <a id="if_ag_ind_changed_evt_t::max__uint8_t"></a> <a id="structif__ag__ind__changed__evt__t_1a30ae336b75b2d88443346cde8474f71e"></a> uint8\_t max
    :   max value for CIVE index

    <a id="_CPPv4N23if_ag_ind_changed_evt_t7ind_idxE"></a>

    <a id="_CPPv3N23if_ag_ind_changed_evt_t7ind_idxE"></a> <a id="_CPPv2N23if_ag_ind_changed_evt_t7ind_idxE"></a> <a id="if_ag_ind_changed_evt_t::ind_idx__btif_hf_ind_t"></a> <a id="structif__ag__ind__changed__evt__t_1af5de792817bfa4abb8c5e8f95354b60e"></a> [btif\_hf\_ind\_t](btif_type.md#_CPPv413btif_hf_ind_t "btif_hf_ind_t") ind\_idx
    :   CIEV index @btif\_hf\_ind\_t

<a id="_CPPv424if_inband_ring_chg_evt_t"></a>

<a id="_CPPv324if_inband_ring_chg_evt_t"></a> <a id="_CPPv224if_inband_ring_chg_evt_t"></a> <a id="if_inband_ring_chg_evt_t"></a> <a id="structif__inband__ring__chg__evt__t"></a> struct if\_inband\_ring\_chg\_evt\_t
:   HFP in-band ring change struct defintion.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N24if_inband_ring_chg_evt_t3hdrE"></a>

    <a id="_CPPv3N24if_inband_ring_chg_evt_t3hdrE"></a> <a id="_CPPv2N24if_inband_ring_chg_evt_t3hdrE"></a> <a id="if_inband_ring_chg_evt_t::hdr__if_hfp_cb_t"></a> <a id="structif__inband__ring__chg__evt__t_1a1ae409d575c6fba192d7dacd5b0bf471"></a> [if\_hfp\_cb\_t](#_CPPv411if_hfp_cb_t "if_hfp_cb_t") hdr
    :   HFP event haeader

    <a id="_CPPv4N24if_inband_ring_chg_evt_t21inband_ring_supportedE"></a>

    <a id="_CPPv3N24if_inband_ring_chg_evt_t21inband_ring_supportedE"></a> <a id="_CPPv2N24if_inband_ring_chg_evt_t21inband_ring_supportedE"></a> <a id="if_inband_ring_chg_evt_t::inband_ring_supported__b"></a> <a id="structif__inband__ring__chg__evt__t_1ab9e5e9c8da211a6aca861e8a8e43ecb4"></a> bool inband\_ring\_supported
    :   boolean value for in-band ring active or not

<a id="_CPPv419if_spk_volume_evt_t"></a>

<a id="_CPPv319if_spk_volume_evt_t"></a> <a id="_CPPv219if_spk_volume_evt_t"></a> <a id="if_spk_volume_evt_t"></a> <a id="structif__spk__volume__evt__t"></a> struct if\_spk\_volume\_evt\_t
:   HFP speak volume change struct defintion.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19if_spk_volume_evt_t3hdrE"></a>

    <a id="_CPPv3N19if_spk_volume_evt_t3hdrE"></a> <a id="_CPPv2N19if_spk_volume_evt_t3hdrE"></a> <a id="if_spk_volume_evt_t::hdr__if_hfp_cb_t"></a> <a id="structif__spk__volume__evt__t_1a991c5b283b81627f454c1fb11b6f01da"></a> [if\_hfp\_cb\_t](#_CPPv411if_hfp_cb_t "if_hfp_cb_t") hdr
    :   HFP event haeader

    <a id="_CPPv4N19if_spk_volume_evt_t10spk_volumeE"></a>

    <a id="_CPPv3N19if_spk_volume_evt_t10spk_volumeE"></a> <a id="_CPPv2N19if_spk_volume_evt_t10spk_volumeE"></a> <a id="if_spk_volume_evt_t::spk_volume__uint8_t"></a> <a id="structif__spk__volume__evt__t_1a77df4eec623fce1ab7d3c5f48f31e99b"></a> uint8\_t spk\_volume
    :   speaker value

<a id="_CPPv420if_sco_connect_evt_t"></a>

<a id="_CPPv320if_sco_connect_evt_t"></a> <a id="_CPPv220if_sco_connect_evt_t"></a> <a id="if_sco_connect_evt_t"></a> <a id="structif__sco__connect__evt__t"></a> struct if\_sco\_connect\_evt\_t
:   HFP SCO connected struct defintion.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20if_sco_connect_evt_t3hdrE"></a>

    <a id="_CPPv3N20if_sco_connect_evt_t3hdrE"></a> <a id="_CPPv2N20if_sco_connect_evt_t3hdrE"></a> <a id="if_sco_connect_evt_t::hdr__if_hfp_cb_t"></a> <a id="structif__sco__connect__evt__t_1ae88dbd0b6feb0a85fe3bcae12b0a8b6f"></a> [if\_hfp\_cb\_t](#_CPPv411if_hfp_cb_t "if_hfp_cb_t") hdr
    :   HFP event haeader

    <a id="_CPPv4N20if_sco_connect_evt_t4addrE"></a>

    <a id="_CPPv3N20if_sco_connect_evt_t4addrE"></a> <a id="_CPPv2N20if_sco_connect_evt_t4addrE"></a> <a id="if_sco_connect_evt_t::addr__btif_bd_addr_t"></a> <a id="structif__sco__connect__evt__t_1a102bef10f38f0bb7943e3d873cdbb98d"></a> [btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr
    :   remote BT address

    <a id="_CPPv4N20if_sco_connect_evt_t10codec_typeE"></a>

    <a id="_CPPv3N20if_sco_connect_evt_t10codec_typeE"></a> <a id="_CPPv2N20if_sco_connect_evt_t10codec_typeE"></a> <a id="if_sco_connect_evt_t::codec_type__btif_sco_codec_t"></a> <a id="structif__sco__connect__evt__t_1a196014d36bc75fdf908e68ad6a3a6698"></a> [btif\_sco\_codec\_t](btif_type.md#_CPPv416btif_sco_codec_t "btif_sco_codec_t") codec\_type
    :   SCO codec type

    <a id="_CPPv4N20if_sco_connect_evt_t6statusE"></a>

    <a id="_CPPv3N20if_sco_connect_evt_t6statusE"></a> <a id="_CPPv2N20if_sco_connect_evt_t6statusE"></a> <a id="if_sco_connect_evt_t::status__uint8_t"></a> <a id="structif__sco__connect__evt__t_1a239566ac8b5782755fa47ba566f0d3cf"></a> uint8\_t status
    :   status @btif\_ret\_t

    <a id="_CPPv4N20if_sco_connect_evt_t10rx_pkt_lenE"></a>

    <a id="_CPPv3N20if_sco_connect_evt_t10rx_pkt_lenE"></a> <a id="_CPPv2N20if_sco_connect_evt_t10rx_pkt_lenE"></a> <a id="if_sco_connect_evt_t::rx_pkt_len__uint16_t"></a> <a id="structif__sco__connect__evt__t_1af184e26f403525348a890af34f88c825"></a> uint16\_t rx\_pkt\_len
    :   RX packet length

    <a id="_CPPv4N20if_sco_connect_evt_t10tx_pkt_lenE"></a>

    <a id="_CPPv3N20if_sco_connect_evt_t10tx_pkt_lenE"></a> <a id="_CPPv2N20if_sco_connect_evt_t10tx_pkt_lenE"></a> <a id="if_sco_connect_evt_t::tx_pkt_len__uint16_t"></a> <a id="structif__sco__connect__evt__t_1a0aa6795f38c635a55deb0d9ecaaec6ff"></a> uint16\_t tx\_pkt\_len
    :   TX packet length

    <a id="_CPPv4N20if_sco_connect_evt_t11sync_handleE"></a>

    <a id="_CPPv3N20if_sco_connect_evt_t11sync_handleE"></a> <a id="_CPPv2N20if_sco_connect_evt_t11sync_handleE"></a> <a id="if_sco_connect_evt_t::sync_handle__uint16_t"></a> <a id="structif__sco__connect__evt__t_1a3579e838bbe7e88abb92c6c4d643aac6"></a> uint16\_t sync\_handle
    :   SCO connection handle

<a id="_CPPv419if_mic_volume_evt_t"></a>

<a id="_CPPv319if_mic_volume_evt_t"></a> <a id="_CPPv219if_mic_volume_evt_t"></a> <a id="if_mic_volume_evt_t"></a> <a id="structif__mic__volume__evt__t"></a> struct if\_mic\_volume\_evt\_t
:   HFP MIC volume change struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19if_mic_volume_evt_t3hdrE"></a>

    <a id="_CPPv3N19if_mic_volume_evt_t3hdrE"></a> <a id="_CPPv2N19if_mic_volume_evt_t3hdrE"></a> <a id="if_mic_volume_evt_t::hdr__if_hfp_cb_t"></a> <a id="structif__mic__volume__evt__t_1ad75b0e567b4f5c0b116858284bd1d7de"></a> [if\_hfp\_cb\_t](#_CPPv411if_hfp_cb_t "if_hfp_cb_t") hdr
    :   HFP event haeader

    <a id="_CPPv4N19if_mic_volume_evt_t10mic_volumeE"></a>

    <a id="_CPPv3N19if_mic_volume_evt_t10mic_volumeE"></a> <a id="_CPPv2N19if_mic_volume_evt_t10mic_volumeE"></a> <a id="if_mic_volume_evt_t::mic_volume__uint8_t"></a> <a id="structif__mic__volume__evt__t_1a888683cee0219b69d0ea4a847e5d7059"></a> uint8\_t mic\_volume
    :   MIC value

<a id="_CPPv417if_sco_disc_evt_t"></a>

<a id="_CPPv317if_sco_disc_evt_t"></a> <a id="_CPPv217if_sco_disc_evt_t"></a> <a id="if_sco_disc_evt_t"></a> <a id="structif__sco__disc__evt__t"></a> struct if\_sco\_disc\_evt\_t
:   HFP SCO disconnect struct defintion.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17if_sco_disc_evt_t3hdrE"></a>

    <a id="_CPPv3N17if_sco_disc_evt_t3hdrE"></a> <a id="_CPPv2N17if_sco_disc_evt_t3hdrE"></a> <a id="if_sco_disc_evt_t::hdr__if_hfp_cb_t"></a> <a id="structif__sco__disc__evt__t_1a672c9a844144e68718521fba4c7e1813"></a> [if\_hfp\_cb\_t](#_CPPv411if_hfp_cb_t "if_hfp_cb_t") hdr
    :   HFP event haeader

<a id="_CPPv413if_ring_evt_t"></a>

<a id="_CPPv313if_ring_evt_t"></a> <a id="_CPPv213if_ring_evt_t"></a> <a id="if_ring_evt_t"></a> <a id="structif__ring__evt__t"></a> struct if\_ring\_evt\_t
:   HFP ring struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N13if_ring_evt_t3hdrE"></a>

    <a id="_CPPv3N13if_ring_evt_t3hdrE"></a> <a id="_CPPv2N13if_ring_evt_t3hdrE"></a> <a id="if_ring_evt_t::hdr__if_hfp_cb_t"></a> <a id="structif__ring__evt__t_1a735da83862efc9c4604585ad1f78aed5"></a> [if\_hfp\_cb\_t](#_CPPv411if_hfp_cb_t "if_hfp_cb_t") hdr
    :   HFP event haeader

<a id="_CPPv419if_start_ring_evt_t"></a>

<a id="_CPPv319if_start_ring_evt_t"></a> <a id="_CPPv219if_start_ring_evt_t"></a> <a id="if_start_ring_evt_t"></a> <a id="structif__start__ring__evt__t"></a> struct if\_start\_ring\_evt\_t
:   HFP start ring struct defintion.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19if_start_ring_evt_t3hdrE"></a>

    <a id="_CPPv3N19if_start_ring_evt_t3hdrE"></a> <a id="_CPPv2N19if_start_ring_evt_t3hdrE"></a> <a id="if_start_ring_evt_t::hdr__if_hfp_cb_t"></a> <a id="structif__start__ring__evt__t_1a596ab8709357528dd1c3c331899ffca4"></a> [if\_hfp\_cb\_t](#_CPPv411if_hfp_cb_t "if_hfp_cb_t") hdr
    :   HFP event haeader

<a id="_CPPv418if_stop_ring_evt_t"></a>

<a id="_CPPv318if_stop_ring_evt_t"></a> <a id="_CPPv218if_stop_ring_evt_t"></a> <a id="if_stop_ring_evt_t"></a> <a id="structif__stop__ring__evt__t"></a> struct if\_stop\_ring\_evt\_t
:   HFP stop ring struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18if_stop_ring_evt_t3hdrE"></a>

    <a id="_CPPv3N18if_stop_ring_evt_t3hdrE"></a> <a id="_CPPv2N18if_stop_ring_evt_t3hdrE"></a> <a id="if_stop_ring_evt_t::hdr__if_hfp_cb_t"></a> <a id="structif__stop__ring__evt__t_1a6870b84f684a682b63840090e57f4778"></a> [if\_hfp\_cb\_t](#_CPPv411if_hfp_cb_t "if_hfp_cb_t") hdr
    :   HFP event haeader

<a id="_CPPv420if_call_answer_evt_t"></a>

<a id="_CPPv320if_call_answer_evt_t"></a> <a id="_CPPv220if_call_answer_evt_t"></a> <a id="if_call_answer_evt_t"></a> <a id="structif__call__answer__evt__t"></a> struct if\_call\_answer\_evt\_t
:   HFP call answer struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20if_call_answer_evt_t3hdrE"></a>

    <a id="_CPPv3N20if_call_answer_evt_t3hdrE"></a> <a id="_CPPv2N20if_call_answer_evt_t3hdrE"></a> <a id="if_call_answer_evt_t::hdr__if_hfp_cb_t"></a> <a id="structif__call__answer__evt__t_1a951b0d7244b246d8ad28fc394c593454"></a> [if\_hfp\_cb\_t](#_CPPv411if_hfp_cb_t "if_hfp_cb_t") hdr
    :   HFP event haeader

<a id="_CPPv423if_call_terminate_evt_t"></a>

<a id="_CPPv323if_call_terminate_evt_t"></a> <a id="_CPPv223if_call_terminate_evt_t"></a> <a id="if_call_terminate_evt_t"></a> <a id="structif__call__terminate__evt__t"></a> struct if\_call\_terminate\_evt\_t
:   HFP call terminate struct definction.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N23if_call_terminate_evt_t3hdrE"></a>

    <a id="_CPPv3N23if_call_terminate_evt_t3hdrE"></a> <a id="_CPPv2N23if_call_terminate_evt_t3hdrE"></a> <a id="if_call_terminate_evt_t::hdr__if_hfp_cb_t"></a> <a id="structif__call__terminate__evt__t_1a4ad3576fedd8cf8ccaa7fa41d14483cc"></a> [if\_hfp\_cb\_t](#_CPPv411if_hfp_cb_t "if_hfp_cb_t") hdr
    :   HFP event haeader

<a id="_CPPv421if_sco_conn_req_evt_t"></a>

<a id="_CPPv321if_sco_conn_req_evt_t"></a> <a id="_CPPv221if_sco_conn_req_evt_t"></a> <a id="if_sco_conn_req_evt_t"></a> <a id="structif__sco__conn__req__evt__t"></a> struct if\_sco\_conn\_req\_evt\_t
:   HFP SCO connection request struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N21if_sco_conn_req_evt_t3hdrE"></a>

    <a id="_CPPv3N21if_sco_conn_req_evt_t3hdrE"></a> <a id="_CPPv2N21if_sco_conn_req_evt_t3hdrE"></a> <a id="if_sco_conn_req_evt_t::hdr__if_hfp_cb_t"></a> <a id="structif__sco__conn__req__evt__t_1adb3a19678468083e37a0a9c96a35b54e"></a> [if\_hfp\_cb\_t](#_CPPv411if_hfp_cb_t "if_hfp_cb_t") hdr
    :   HFP event haeader

    <a id="_CPPv4N21if_sco_conn_req_evt_t5validE"></a>

    <a id="_CPPv3N21if_sco_conn_req_evt_t5validE"></a> <a id="_CPPv2N21if_sco_conn_req_evt_t5validE"></a> <a id="if_sco_conn_req_evt_t::valid__b"></a> <a id="structif__sco__conn__req__evt__t_1a6a7fc96f91bb10e0962f3dc645397119"></a> bool valid
    :   static @btif\_ret\_t

    <a id="_CPPv4N21if_sco_conn_req_evt_t11accept_syncE"></a>

    <a id="_CPPv3N21if_sco_conn_req_evt_t11accept_syncE"></a> <a id="_CPPv2N21if_sco_conn_req_evt_t11accept_syncE"></a> <a id="if_sco_conn_req_evt_t::accept_sync__if_accept_sync_t"></a> <a id="structif__sco__conn__req__evt__t_1ad57dbdd207b739363544741280b3ae90"></a> [if\_accept\_sync\_t](hci_if.md#_CPPv416if_accept_sync_t "if_accept_sync_t") accept\_sync
    :   SCO setting relevant parameter

<a id="_CPPv419btif_hfp_register_t"></a>

<a id="_CPPv319btif_hfp_register_t"></a> <a id="_CPPv219btif_hfp_register_t"></a> <a id="btif_hfp_register_t"></a> <a id="structbtif__hfp__register__t"></a> struct btif\_hfp\_register\_t
:   HFP event callback struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19btif_hfp_register_t9dlst_nodeE"></a>

    <a id="_CPPv3N19btif_hfp_register_t9dlst_nodeE"></a> <a id="_CPPv2N19btif_hfp_register_t9dlst_nodeE"></a> <a id="btif_hfp_register_t::dlst_node__dl_list_t"></a> <a id="structbtif__hfp__register__t_1a9ffa17da7de27ca174836da928158235"></a> dl\_list\_t dlst\_node
    :   node for application handler will be linked to orthers

    <a id="_CPPv4N19btif_hfp_register_t8callbackE"></a>

    <a id="_CPPv3N19btif_hfp_register_t8callbackE"></a> <a id="_CPPv2N19btif_hfp_register_t8callbackE"></a> <a id="btif_hfp_register_t::callback__btif_hfp_event_callback"></a> <a id="structbtif__hfp__register__t_1ab8df9e0ce91abe4ffc86a76bdb72f52c"></a> [btif\_hfp\_event\_callback](btif_type.md#_CPPv423btif_hfp_event_callback "btif_hfp_event_callback") callback
    :   function pointer for callback function

<a id="_CPPv417hfp_if_response_t"></a>

<a id="_CPPv317hfp_if_response_t"></a> <a id="_CPPv217hfp_if_response_t"></a> <a id="hfp_if_response_t"></a> <a id="structhfp__if__response__t"></a> struct hfp\_if\_response\_t

<a id="macros"></a>

### Macros

<a id="c.BTIF_HFP_SLC_ESTABLISHED"></a>

<a id="hfp__if_8h_1aa2f67b948e684b40866dc068966cdcff"></a> BTIF\_HFP\_SLC\_ESTABLISHED
:   callback struct see@if\_slc\_connect\_evt\_t

<a id="c.BTIF_HFP_SLC_RELEASED"></a>

<a id="hfp__if_8h_1ae5178ea5d92a681ed0459124d65b604f"></a> BTIF\_HFP\_SLC\_RELEASED
:   callback struct see@if\_slc\_disc\_evt\_t

<a id="c.BTIF_HFP_AUDIO_CONNECTION_ESTABLISHED"></a>

<a id="hfp__if_8h_1ac2b4acfb79a769a468f411b07d46d584"></a> BTIF\_HFP\_AUDIO\_CONNECTION\_ESTABLISHED
:   callback struct see@if\_sco\_connect\_evt\_t

<a id="c.BTIF_HFP_AUDIO_CONNECTION_RELEASED"></a>

<a id="hfp__if_8h_1a94b8133fa74caae5e7877e7590221bc0"></a> BTIF\_HFP\_AUDIO\_CONNECTION\_RELEASED
:   callback struct see@if\_sco\_disc\_evt\_t

<a id="c.BTIF_HFP_AG_INDICATOR_STATUS_CHANGED"></a>

<a id="hfp__if_8h_1a73e3dac097fd313e47c0aed182b4131a"></a> BTIF\_HFP\_AG\_INDICATOR\_STATUS\_CHANGED
:   callback struct see@if\_ag\_ind\_changed\_evt\_t

<a id="c.BTIF_HFP_RING"></a>

<a id="hfp__if_8h_1a2954134823a4d9357145a8ddccfd4be9"></a> BTIF\_HFP\_RING
:   callback struct see@if\_ring\_evt\_t

<a id="c.BTIF_HFP_SPEAKER_VOLUME"></a>

<a id="hfp__if_8h_1af317a606aa47200e29e7ea7f7b887d29"></a> BTIF\_HFP\_SPEAKER\_VOLUME
:   callback struct see@if\_spk\_volume\_evt\_t

<a id="c.BTIF_HFP_MICROPHONE_VOLUME"></a>

<a id="hfp__if_8h_1a83c9b3b8732713e3abb666e1a25f234e"></a> BTIF\_HFP\_MICROPHONE\_VOLUME
:   callback struct see@if\_mic\_volume\_evt\_t

<a id="c.BTIF_HFP_ENHANCED_CALL_STATUS"></a>

<a id="hfp__if_8h_1a2fabe87a00413a8fb4bbc3a9330ef2fb"></a> BTIF\_HFP\_ENHANCED\_CALL\_STATUS
:   callback struct see@NUILL

<a id="c.BTIF_HFP_INBAND_RING_TONE_CHANGED"></a>

<a id="hfp__if_8h_1a31e460dde2e629d1ce34a87d26e0a6ea"></a> BTIF\_HFP\_INBAND\_RING\_TONE\_CHANGED
:   callback struct see@if\_inband\_ring\_chg\_evt\_t

<a id="c.BTIF_HFP_START_RINGING"></a>

<a id="hfp__if_8h_1ae9936c9066ceae80b356dfbe97a9d5b3"></a> BTIF\_HFP\_START\_RINGING
:   callback struct see@if\_start\_ring\_evt\_t

<a id="c.BTIF_HFP_STOP_RINGING"></a>

<a id="hfp__if_8h_1af396ed56b78ab852eb1e80b060a32933"></a> BTIF\_HFP\_STOP\_RINGING
:   callback struct see@if\_stop\_ring\_evt\_t

<a id="c.BTIF_HFP_CALL_ANSWER"></a>

<a id="hfp__if_8h_1afbb3a2ba060069cf8740af3246d56407"></a> BTIF\_HFP\_CALL\_ANSWER
:   callback struct see@if\_call\_answer\_evt\_t

<a id="c.BTFI_HFP_CALL_TERMINATED"></a>

<a id="hfp__if_8h_1a157910eea6e157caa91fe87a1de3ab26"></a> BTFI\_HFP\_CALL\_TERMINATED
:   callback struct see@if\_call\_terminate\_evt\_t

<a id="c.BTIF_HFP_SCO_CONN_REQ"></a>

<a id="hfp__if_8h_1ac87620307a85fd280aff626d9d57e10b"></a> BTIF\_HFP\_SCO\_CONN\_REQ
:   callback struct see@if\_sco\_conn\_req\_evt\_t

<a id="c.STATUS_IF_OK"></a>

<a id="hfp__if_8h_1a8b77d0442bd3519c48f3cb90e5edd731"></a> STATUS\_IF\_OK

<a id="c.STATUS_IF_CONNECT"></a>

<a id="hfp__if_8h_1a3128178107f9214be32f0c1e139ff07b"></a> STATUS\_IF\_CONNECT

<a id="c.STATUS_IF_RING"></a>

<a id="hfp__if_8h_1afd5bf797a34ce710f695e4d28d35643b"></a> STATUS\_IF\_RING

<a id="c.STATUS_IF_NO_CARRIER"></a>

<a id="hfp__if_8h_1ad110592dc1c313eb0b5c461f4b51a960"></a> STATUS\_IF\_NO\_CARRIER

<a id="c.STATUS_IF_ERROR"></a>

<a id="hfp__if_8h_1a37dde2a2ad0aafc6bfce8975f1534cd3"></a> STATUS\_IF\_ERROR

<a id="c.STATUS_IF_NO_DIALTONE"></a>

<a id="hfp__if_8h_1a7addf01689643e67228024cd8bc29e69"></a> STATUS\_IF\_NO\_DIALTONE

<a id="c.STATUS_IF_BUSY"></a>

<a id="hfp__if_8h_1a5a941f95b369e7029b359b5569e3b6d6"></a> STATUS\_IF\_BUSY

<a id="c.STATUS_IF_NO_ANSWER"></a>

<a id="hfp__if_8h_1adb5c77d03f83c48a733ad8c20db0cbee"></a> STATUS\_IF\_NO\_ANSWER

<a id="c.STATUS_IF_DELAYED"></a>

<a id="hfp__if_8h_1aa4673c6842ed732429cc3cec82729c8e"></a> STATUS\_IF\_DELAYED

<a id="c.STATUS_IF_BLACKLISTED"></a>

<a id="hfp__if_8h_1a15870cd274b8ec41f941931437ef3e29"></a> STATUS\_IF\_BLACKLISTED

<a id="c.STATUS_IF_CME_ERROR"></a>

<a id="hfp__if_8h_1abff20c7098cd2f5b1441b2880fd4edcd"></a> STATUS\_IF\_CME\_ERROR

<a id="c.IF_AG_FAILURE"></a>

<a id="hfp__if_8h_1a2a0eeb82c666c1a46a775d3411b3a551"></a> IF\_AG\_FAILURE

<a id="c.IF_NO_CONNECTION_TO_PHONE"></a>

<a id="hfp__if_8h_1a69811f099a0b0a625ee3918a2327648b"></a> IF\_NO\_CONNECTION\_TO\_PHONE

<a id="c.IF_OPERATION_NOT_ALLOWED"></a>

<a id="hfp__if_8h_1abf0edcc6f96cad9bbe354f299b15c0e3"></a> IF\_OPERATION\_NOT\_ALLOWED

<a id="c.IF_OPERATION_NOT_SUPPORTED"></a>

<a id="hfp__if_8h_1a3c90872e912bd7c3c99d18b8f57d52e5"></a> IF\_OPERATION\_NOT\_SUPPORTED

<a id="c.IF_PH_SIM_PIN_REQUIRED"></a>

<a id="hfp__if_8h_1a7461a1107206c0a40bd5ae057be79bd5"></a> IF\_PH\_SIM\_PIN\_REQUIRED

<a id="c.IF_SIM_NOT_INSERTED"></a>

<a id="hfp__if_8h_1a7aadd6b308e36a689754fd5f44d404f8"></a> IF\_SIM\_NOT\_INSERTED

<a id="c.IF_SIM_PIN_REQUIRED"></a>

<a id="hfp__if_8h_1a272254515aa76fef1ec660c74aff8066"></a> IF\_SIM\_PIN\_REQUIRED

<a id="c.IF_SIM_PUK_REQUIRED"></a>

<a id="hfp__if_8h_1a391371caa4e5fda677793cf7a8ae39d0"></a> IF\_SIM\_PUK\_REQUIRED

<a id="c.IF_SIM_FAILURE"></a>

<a id="hfp__if_8h_1ac34f765e066343d147368c55c149f334"></a> IF\_SIM\_FAILURE

<a id="c.IF_SIM_BUSY"></a>

<a id="hfp__if_8h_1afcc6153c2a46c511c5076cbd1e929056"></a> IF\_SIM\_BUSY

<a id="c.IF_INCORRECT_PASSWORD"></a>

<a id="hfp__if_8h_1a5c2f69ba1faf7aec865a5e7636cd8cb9"></a> IF\_INCORRECT\_PASSWORD

<a id="c.IF_SIM_PIN2_REQUIRED"></a>

<a id="hfp__if_8h_1a375599675507829e82062ea9926aff55"></a> IF\_SIM\_PIN2\_REQUIRED

<a id="c.IF_SIM_PUK2_REQUIRED"></a>

<a id="hfp__if_8h_1ac41a7128f6cf6f204940807e5eb39a8b"></a> IF\_SIM\_PUK2\_REQUIRED

<a id="c.IF_MEMORY_FULL"></a>

<a id="hfp__if_8h_1a6b221461d40bac4eb9ed8349def8837e"></a> IF\_MEMORY\_FULL

<a id="c.IF_INVALID_INDEX"></a>

<a id="hfp__if_8h_1adbd9cee67e3f714beb9c3ac7d801c0f1"></a> IF\_INVALID\_INDEX

<a id="c.IF_MEMORY_FAILURE"></a>

<a id="hfp__if_8h_1ac57e1e1f2024925a3ee6ac61afc80140"></a> IF\_MEMORY\_FAILURE

<a id="c.IF_TEXT_STRING_TOO_LONG"></a>

<a id="hfp__if_8h_1af0afed1d17118ba0f1b3af49465db644"></a> IF\_TEXT\_STRING\_TOO\_LONG

<a id="c.IF_INVALID_CHARS_IN_TEXT_STRING"></a>

<a id="hfp__if_8h_1a3fed00d06cad0217a1c57cb9c76e0213"></a> IF\_INVALID\_CHARS\_IN\_TEXT\_STRING

<a id="c.IF_DIAL_STRING_TO_LONG"></a>

<a id="hfp__if_8h_1a2f2cf5de78e31fff428f8b98dbdce405"></a> IF\_DIAL\_STRING\_TO\_LONG

<a id="c.IF_INVALID_CHARS_IN_DIAL_STRING"></a>

<a id="hfp__if_8h_1a0d50d9093feb13e8826dd25a429c2852"></a> IF\_INVALID\_CHARS\_IN\_DIAL\_STRING

<a id="c.IF_NO_NETWORK_SERVICE"></a>

<a id="hfp__if_8h_1a99250d05d5348084074911dc2bbd2214"></a> IF\_NO\_NETWORK\_SERVICE

<a id="c.IF_NETWORK_TIMEOUT"></a>

<a id="hfp__if_8h_1a3a515bb5e4342b7eb4efc3cc772c5d4f"></a> IF\_NETWORK\_TIMEOUT

<a id="c.IF_NETWORK_NOT_ALLOWED"></a>

<a id="hfp__if_8h_1a76116dd0aab7f1dd3ca0837f70487f4c"></a> IF\_NETWORK\_NOT\_ALLOWED

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv416btif_hfp_event_t"></a>

<a id="_CPPv316btif_hfp_event_t"></a> <a id="_CPPv216btif_hfp_event_t"></a> <a id="btif_hfp_event_t"></a> <a id="hfp__if_8h_1acccb709e1d83d7af3cc0f994a6397df0"></a> typedef uint8\_t btif\_hfp\_event\_t

<a id="_CPPv415hfp_if_status_t"></a>

<a id="_CPPv315hfp_if_status_t"></a> <a id="_CPPv215hfp_if_status_t"></a> <a id="hfp_if_status_t"></a> <a id="hfp__if_8h_1aaac7023f954f99d617e7e1ddd1aa0757"></a> typedef uint8\_t hfp\_if\_status\_t

<a id="_CPPv414hfp_if_error_t"></a>

<a id="_CPPv314hfp_if_error_t"></a> <a id="_CPPv214hfp_if_error_t"></a> <a id="hfp_if_error_t"></a> <a id="hfp__if_8h_1ab5d0e3305afa89e4c65cb29209e0bacf"></a> typedef uint8\_t hfp\_if\_error\_t

<a id="_CPPv424hfp_if_response_callback"></a>

<a id="_CPPv324hfp_if_response_callback"></a> <a id="_CPPv224hfp_if_response_callback"></a> <a id="hfp_if_response_callback"></a> <a id="hfp__if_8h_1affd9bd3bf691598ee9c10047a5c79fad"></a> typedef void (\*hfp\_if\_response\_callback)([hfp\_if\_status\_t](#_CPPv415hfp_if_status_t "hfp_if_status_t") result, [hfp\_if\_error\_t](#_CPPv414hfp_if_error_t "hfp_if_error_t") cme\_err, void \*p\_user\_data)

<a id="_CPPv425hfp_if_ag_result_callback"></a>

<a id="_CPPv325hfp_if_ag_result_callback"></a> <a id="_CPPv225hfp_if_ag_result_callback"></a> <a id="hfp_if_ag_result_callback"></a> <a id="hfp__if_8h_1a0e53f436c446256d1f7e4491eb849917"></a> typedef void (\*hfp\_if\_ag\_result\_callback)([hfp\_if\_response\_t](#_CPPv417hfp_if_response_t "hfp_if_response_t") \*p\_data, void \*p\_hf\_ctrl)
