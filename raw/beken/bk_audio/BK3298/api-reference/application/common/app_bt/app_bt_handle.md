---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_bt/app_bt_handle.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bt-application-handle-functions"></a>

# BT Application Handle Functions

<a id="app-bt-handle-api-brief"></a>

## APP\_BT\_HANDLE API Brief

| Application | Brief |
| --- | --- |
| [`app_bt_handle_init()`](#_CPPv418app_bt_handle_initv "app_bt_handle_init") | application for bt handle initialize |
| [`app_bt_playpause()`](#_CPPv416app_bt_playpausev "app_bt_playpause") | application for media control , button action can call this function to trigger bluetooth media action, play or pause song |
| [`app_bt_next_track()`](#_CPPv417app_bt_next_trackv "app_bt_next_track") | application for media control , button action can call this function to trigger bluetooth media action, change to next song |
| [`app_bt_prev_track()`](#_CPPv417app_bt_prev_trackv "app_bt_prev_track") | application for media control , button action can call this function to trigger bluetooth media action, change to previous song |
| [`app_bt_rewind()`](#_CPPv413app_bt_rewindv "app_bt_rewind") | application for media control , button action can call this function to trigger bluetooth media action |
| [`app_bt_forward()`](#_CPPv414app_bt_forwardv "app_bt_forward") | application for media control , button action can call this function to trigger bluetooth media action, faster backward song |
| [`app_bt_volume_up()`](#_CPPv416app_bt_volume_upv "app_bt_volume_up") | application for media control , button action can call this function to trigger bluetooth media action,faster forward song |
| [`app_bt_volume_down()`](#_CPPv418app_bt_volume_downv "app_bt_volume_down") | application for media control , button action can call this function to trigger bluetooth media action, increase headset volume |
| [`app_bt_mute()`](#_CPPv411app_bt_mutev "app_bt_mute") | application for media control , button action can call this function to trigger bluetooth media action, decrease headset volume |
| [`app_bt_enter_paring()`](#_CPPv419app_bt_enter_paringv "app_bt_enter_paring") | no used |
| [`app_bt_powerdown()`](#_CPPv416app_bt_powerdown8uint32_t8uint32_t "app_bt_powerdown") | application for powerdown bt headset |
| [`app_bt_shutdown()`](#_CPPv415app_bt_shutdownv "app_bt_shutdown") | application for powerdown bt headset |
| [`app_bt_call_hfack()`](#_CPPv417app_bt_call_hfackv "app_bt_call_hfack") | application for handfree function can pick the incoming call or reject call |
| [`app_bt_call_reject()`](#_CPPv418app_bt_call_rejectv "app_bt_call_reject") | application for hand-free function reject call |
| [`app_bt_call_redial()`](#_CPPv418app_bt_call_redialv "app_bt_call_redial") | application for hand-free function last number re-dial |
| [`app_bt_mic_gain_up()`](#_CPPv418app_bt_mic_gain_upv "app_bt_mic_gain_up") | no effect,microphone gain can not control |
| [`app_bt_mic_gain_down()`](#_CPPv420app_bt_mic_gain_downv "app_bt_mic_gain_down") | no effect,microphone gain can not control |
| [`app_bt_mic_mute()`](#_CPPv415app_bt_mic_mutev "app_bt_mic_mute") | application for hand-free can mute Microphone |
| [`app_bt_voice_dial_set()`](#_CPPv421app_bt_voice_dial_setv "app_bt_voice_dial_set") | application for hand-free can trigger voice dial function |
| [`app_bt_call_transfer_toggle()`](#_CPPv427app_bt_call_transfer_togglev "app_bt_call_transfer_toggle") | application for hand-free can swap phone call to phone or headset |
| [`app_bt_conn_discon()`](#_CPPv418app_bt_conn_disconv "app_bt_conn_discon") | no effect,not implement |
| [`app_bt_restore_factory_setting()`](#_CPPv430app_bt_restore_factory_settingv "app_bt_restore_factory_setting") | application for reset all application environment variable and disconnect all bt link |
| [`app_bt_enter_dut()`](#_CPPv416app_bt_enter_dutv "app_bt_enter_dut") | application for enter bluetooth device under test mode(DUT) |
| [`app_bt_exit_dut()`](#_CPPv415app_bt_exit_dutv "app_bt_exit_dut") | application for exit bluetooth device under test mode(DUT) |
| [`app_bt_hint_lang_change()`](#_CPPv423app_bt_hint_lang_changev "app_bt_hint_lang_change") | no effect |
| [`app_bt_get_mic_mute_state()`](#_CPPv425app_bt_get_mic_mute_statev "app_bt_get_mic_mute_state") | application get microphone current mute state |
| [`app_get_dut_mode_active()`](#_CPPv423app_get_dut_mode_activev "app_get_dut_mode_active") | application get bluetooth DUT mode state |
| [`app_bt_auto_pd_timer_start_ext()`](#_CPPv430app_bt_auto_pd_timer_start_ext7uint8_t "app_bt_auto_pd_timer_start_ext") | application start pd timer |
| [`app_bt_connect()`](#_CPPv414app_bt_connectv "app_bt_connect") | reconnect to mobile phone api |

<a id="app-bt-handle-api-reference"></a>

## APP\_BT\_HANDLE API Reference

<a id="header-file"></a>

### Header File

- [common/app\_bt/app\_bt\_handle.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_bt/app_bt_handle.h)

<a id="functions"></a>

### Functions

<a id="_CPPv418app_bt_handle_initv"></a>

<a id="_CPPv318app_bt_handle_initv"></a> <a id="_CPPv218app_bt_handle_initv"></a> <a id="app_bt_handle_init__void"></a> <a id="app__bt__handle_8h_1a293275b2d6af8eb3e23fdbf8b2a38324"></a> void app\_bt\_handle\_init(void)
:   application for bt handle initialize event callback register

    返回:
    :   N/A

<a id="_CPPv416app_bt_playpausev"></a>

<a id="_CPPv316app_bt_playpausev"></a> <a id="_CPPv216app_bt_playpausev"></a> <a id="app_bt_playpause__void"></a> <a id="app__bt__handle_8h_1aaff8a41c22512332026ebc03b2e36ab3"></a> void app\_bt\_playpause(void)
:   application for media control , button action can call this function to trigger bluetooth media action, play or pause song

    返回:
    :   N/A

<a id="_CPPv417app_bt_next_trackv"></a>

<a id="_CPPv317app_bt_next_trackv"></a> <a id="_CPPv217app_bt_next_trackv"></a> <a id="app_bt_next_track__void"></a> <a id="app__bt__handle_8h_1a3768709374773ab7b6af0d315ac997ae"></a> void app\_bt\_next\_track(void)
:   application for media control , button action can call this function to trigger bluetooth media action, change to next song

    返回:
    :   N/A

<a id="_CPPv417app_bt_prev_trackv"></a>

<a id="_CPPv317app_bt_prev_trackv"></a> <a id="_CPPv217app_bt_prev_trackv"></a> <a id="app_bt_prev_track__void"></a> <a id="app__bt__handle_8h_1a67b67549f66e7b273133af351c94761e"></a> void app\_bt\_prev\_track(void)
:   application for media control , button action can call this function to trigger bluetooth media action, change to previous song

    返回:
    :   N/A

<a id="_CPPv413app_bt_rewindv"></a>

<a id="_CPPv313app_bt_rewindv"></a> <a id="_CPPv213app_bt_rewindv"></a> <a id="app_bt_rewind__void"></a> <a id="app__bt__handle_8h_1ac09a51b001cd8b2e1a3e1d6f0f2db29b"></a> void app\_bt\_rewind(void)
:   application for media control , button action can call this function to trigger bluetooth media action

    返回:
    :   N/A

<a id="_CPPv414app_bt_forwardv"></a>

<a id="_CPPv314app_bt_forwardv"></a> <a id="_CPPv214app_bt_forwardv"></a> <a id="app_bt_forward__void"></a> <a id="app__bt__handle_8h_1ae5b57dbf62f73def4aac4455f8017609"></a> void app\_bt\_forward(void)
:   application for media control , button action can call this function to trigger bluetooth media action, faster backward song

    返回:
    :   N/A

<a id="_CPPv416app_bt_volume_upv"></a>

<a id="_CPPv316app_bt_volume_upv"></a> <a id="_CPPv216app_bt_volume_upv"></a> <a id="app_bt_volume_up__void"></a> <a id="app__bt__handle_8h_1a18f64c5a159877602d0dd2bb29e3d34e"></a> void app\_bt\_volume\_up(void)
:   application for media control , button action can call this function to trigger bluetooth media action,faster forward song

    返回:
    :   N/A

<a id="_CPPv418app_bt_volume_downv"></a>

<a id="_CPPv318app_bt_volume_downv"></a> <a id="_CPPv218app_bt_volume_downv"></a> <a id="app_bt_volume_down__void"></a> <a id="app__bt__handle_8h_1a8a2f56b0932e6827ef75dd2f6f054bc6"></a> void app\_bt\_volume\_down(void)
:   application for media control , button action can call this function to trigger bluetooth media action, increase headset volume

    返回:
    :   N/A

<a id="_CPPv411app_bt_mutev"></a>

<a id="_CPPv311app_bt_mutev"></a> <a id="_CPPv211app_bt_mutev"></a> <a id="app_bt_mute__void"></a> <a id="app__bt__handle_8h_1a522572dae22b7fe13b27f83ba50f8205"></a> void app\_bt\_mute(void)
:   application for media control , button action can call this function to trigger bluetooth media action, decrease headset volume

    返回:
    :   N/A

<a id="_CPPv419app_bt_enter_paringv"></a>

<a id="_CPPv319app_bt_enter_paringv"></a> <a id="_CPPv219app_bt_enter_paringv"></a> <a id="app_bt_enter_paring__void"></a> <a id="app__bt__handle_8h_1a698fd75ec185054147d1917c91aa816a"></a> void app\_bt\_enter\_paring(void)
:   no used

    返回:
    :   N/A

<a id="_CPPv416app_bt_powerdown8uint32_t8uint32_t"></a>

<a id="_CPPv316app_bt_powerdown8uint32_t8uint32_t"></a> <a id="_CPPv216app_bt_powerdown8uint32_t8uint32_t"></a> <a id="app_bt_powerdown__uint32_t.uint32_t"></a> <a id="app__bt__handle_8h_1aa10b96ac8b39ce56ce31abbcd0dcd64c"></a> void app\_bt\_powerdown(uint32\_t param, uint32\_t state\_tick)
:   application for powerdown bt headset

    返回:
    :   N/A

<a id="_CPPv415app_bt_shutdownv"></a>

<a id="_CPPv315app_bt_shutdownv"></a> <a id="_CPPv215app_bt_shutdownv"></a> <a id="app_bt_shutdown__void"></a> <a id="app__bt__handle_8h_1a107d6e655e414c5c4a9b0d49231d21c8"></a> void app\_bt\_shutdown(void)
:   application for powerdown bt headset

    返回:
    :   N/A

<a id="_CPPv417app_bt_call_hfackv"></a>

<a id="_CPPv317app_bt_call_hfackv"></a> <a id="_CPPv217app_bt_call_hfackv"></a> <a id="app_bt_call_hfack__void"></a> <a id="app__bt__handle_8h_1ab44042ad2de2196e9f48cbc1c3ae6269"></a> void app\_bt\_call\_hfack(void)
:   application for handfree function can pick the incoming call or reject call

    返回:
    :   N/A

<a id="_CPPv418app_bt_call_rejectv"></a>

<a id="_CPPv318app_bt_call_rejectv"></a> <a id="_CPPv218app_bt_call_rejectv"></a> <a id="app_bt_call_reject__void"></a> <a id="app__bt__handle_8h_1acc9326b7639065d381c43fa5d29284ce"></a> void app\_bt\_call\_reject(void)
:   application for hand-free function reject call

    返回:
    :   N/A

<a id="_CPPv418app_bt_call_redialv"></a>

<a id="_CPPv318app_bt_call_redialv"></a> <a id="_CPPv218app_bt_call_redialv"></a> <a id="app_bt_call_redial__void"></a> <a id="app__bt__handle_8h_1aa48d630f9308f442116e1c703a027c8f"></a> void app\_bt\_call\_redial(void)
:   application for hand-free function last number re-dial

    返回:
    :   N/A

<a id="_CPPv418app_bt_mic_gain_upv"></a>

<a id="_CPPv318app_bt_mic_gain_upv"></a> <a id="_CPPv218app_bt_mic_gain_upv"></a> <a id="app_bt_mic_gain_up__void"></a> <a id="app__bt__handle_8h_1a4f66092aa1a7c629e954fd1ffdf78451"></a> void app\_bt\_mic\_gain\_up(void)
:   no effect,microphone gain can not control

    返回:
    :   N/A

<a id="_CPPv420app_bt_mic_gain_downv"></a>

<a id="_CPPv320app_bt_mic_gain_downv"></a> <a id="_CPPv220app_bt_mic_gain_downv"></a> <a id="app_bt_mic_gain_down__void"></a> <a id="app__bt__handle_8h_1a72761c33881b8e80e89182e4fb9d4195"></a> void app\_bt\_mic\_gain\_down(void)
:   no effect,microphone gain can not control

    返回:
    :   N/A

<a id="_CPPv415app_bt_mic_mutev"></a>

<a id="_CPPv315app_bt_mic_mutev"></a> <a id="_CPPv215app_bt_mic_mutev"></a> <a id="app_bt_mic_mute__void"></a> <a id="app__bt__handle_8h_1ab2ccc8b721ee97482baf8d3a45aec188"></a> void app\_bt\_mic\_mute(void)
:   application for hand-free can mute Microphone

    返回:
    :   N/A

<a id="_CPPv421app_bt_voice_dial_setv"></a>

<a id="_CPPv321app_bt_voice_dial_setv"></a> <a id="_CPPv221app_bt_voice_dial_setv"></a> <a id="app_bt_voice_dial_set__void"></a> <a id="app__bt__handle_8h_1aaf9c6fa41eb03604f641c6313a7f31bf"></a> void app\_bt\_voice\_dial\_set(void)
:   application for hand-free can trigger voice dial function

    返回:
    :   N/A

<a id="_CPPv427app_bt_call_transfer_togglev"></a>

<a id="_CPPv327app_bt_call_transfer_togglev"></a> <a id="_CPPv227app_bt_call_transfer_togglev"></a> <a id="app_bt_call_transfer_toggle__void"></a> <a id="app__bt__handle_8h_1abcda01fab357ef948a254a37fa27f7ff"></a> void app\_bt\_call\_transfer\_toggle(void)
:   application for hand-free can swap phone call to phone or headset

    返回:
    :   N/A

<a id="_CPPv418app_bt_conn_disconv"></a>

<a id="_CPPv318app_bt_conn_disconv"></a> <a id="_CPPv218app_bt_conn_disconv"></a> <a id="app_bt_conn_discon__void"></a> <a id="app__bt__handle_8h_1a17288efc0f92c422407feb7278c43178"></a> void app\_bt\_conn\_discon(void)
:   no effect,not implement

    返回:
    :   N/A

<a id="_CPPv430app_bt_restore_factory_settingv"></a>

<a id="_CPPv330app_bt_restore_factory_settingv"></a> <a id="_CPPv230app_bt_restore_factory_settingv"></a> <a id="app_bt_restore_factory_setting__void"></a> <a id="app__bt__handle_8h_1a365c5270a079abb7f09a50fb9b978271"></a> void app\_bt\_restore\_factory\_setting(void)
:   application for reset all application environment variable and disconnect all bt link

    返回:
    :   N/A

<a id="_CPPv416app_bt_enter_dutv"></a>

<a id="_CPPv316app_bt_enter_dutv"></a> <a id="_CPPv216app_bt_enter_dutv"></a> <a id="app_bt_enter_dut__void"></a> <a id="app__bt__handle_8h_1a4accb28cea1b74603fc92cc9395a39e0"></a> void app\_bt\_enter\_dut(void)
:   application for enter bluetooth device under test mode(DUT)

    返回:
    :   N/A

<a id="_CPPv415app_bt_exit_dutv"></a>

<a id="_CPPv315app_bt_exit_dutv"></a> <a id="_CPPv215app_bt_exit_dutv"></a> <a id="app_bt_exit_dut__void"></a> <a id="app__bt__handle_8h_1afa45a7022b76181a2c8384b1703aa34f"></a> void app\_bt\_exit\_dut(void)
:   application for exit bluetooth device under test mode(DUT)

    返回:
    :   N/A

<a id="_CPPv423app_bt_hint_lang_changev"></a>

<a id="_CPPv323app_bt_hint_lang_changev"></a> <a id="_CPPv223app_bt_hint_lang_changev"></a> <a id="app_bt_hint_lang_change__void"></a> <a id="app__bt__handle_8h_1a80e458be79097dc72a6350bf7b748e8d"></a> void app\_bt\_hint\_lang\_change(void)
:   no effect

    返回:
    :   N/A

<a id="_CPPv425app_bt_get_mic_mute_statev"></a>

<a id="_CPPv325app_bt_get_mic_mute_statev"></a> <a id="_CPPv225app_bt_get_mic_mute_statev"></a> <a id="app_bt_get_mic_mute_state__void"></a> <a id="app__bt__handle_8h_1a25adbdd0c9d31733fced1f8df29acd52"></a> bool app\_bt\_get\_mic\_mute\_state(void)
:   application get microphone current mute state

    返回值:
    :   - **1** – mute
        - **0** – not mute

    返回:
    :   mute state

<a id="_CPPv423app_get_dut_mode_activev"></a>

<a id="_CPPv323app_get_dut_mode_activev"></a> <a id="_CPPv223app_get_dut_mode_activev"></a> <a id="app_get_dut_mode_active__void"></a> <a id="app__bt__handle_8h_1a0057d6fb208aff54d8c733a7d09bacb6"></a> bool app\_get\_dut\_mode\_active(void)
:   application get bluetooth DUT mode state

    返回值:
    :   - **true** – DUT is active
        - **false** – DUT is not active

    返回:
    :   result

    返回:
    :   DUT status

<a id="_CPPv430app_bt_auto_pd_timer_start_ext7uint8_t"></a>

<a id="_CPPv330app_bt_auto_pd_timer_start_ext7uint8_t"></a> <a id="_CPPv230app_bt_auto_pd_timer_start_ext7uint8_t"></a> <a id="app_bt_auto_pd_timer_start_ext__uint8_t"></a> <a id="app__bt__handle_8h_1a443511ef443e64995b2c2c537dc71670"></a> void app\_bt\_auto\_pd\_timer\_start\_ext(uint8\_t cond)
:   application start pd timer

    返回:
    :   N/A

<a id="_CPPv414app_bt_connectv"></a>

<a id="_CPPv314app_bt_connectv"></a> <a id="_CPPv214app_bt_connectv"></a> <a id="app_bt_connect__void"></a> <a id="app__bt__handle_8h_1aa4db23e630a22bf800e89ea634c8377f"></a> void app\_bt\_connect(void)
:   reconnect to mobile phone api

    返回:
    :   N/A

<a id="macros"></a>

### Macros

<a id="c.ENTER_SHUTDOWN"></a>

<a id="app__bt__handle_8h_1a792de0ef8d7c035f9fc90a8d7a3e45c6"></a> ENTER\_SHUTDOWN

<a id="c.ENTER_CHARGER_DEEP_SLEEP"></a>

<a id="app__bt__handle_8h_1a9c83f587f0c75cac56eeb146ffc8a2f2"></a> ENTER\_CHARGER\_DEEP\_SLEEP

<a id="c.ENTER_CHARGER_SHUTDOWN"></a>

<a id="app__bt__handle_8h_1a6ee696a857321cbb0aca05f9930b886b"></a> ENTER\_CHARGER\_SHUTDOWN

<a id="c.ENTER_CHARGER_REBOOT"></a>

<a id="app__bt__handle_8h_1a4e6a415817c9bd9e6265c2e6c1ff3404"></a> ENTER\_CHARGER\_REBOOT

<a id="c.ENTER_LOW_BAT_SHUTDOWN"></a>

<a id="app__bt__handle_8h_1ae08f2011f7d24acb13afdbebcec11da6"></a> ENTER\_LOW\_BAT\_SHUTDOWN

<a id="c.ENTER_BOX_LOW_BAT_SHUTDOWN"></a>

<a id="app__bt__handle_8h_1a990782854864b1b92bd83e72f6491caa"></a> ENTER\_BOX\_LOW\_BAT\_SHUTDOWN

<a id="c.LOCAL_PD_TIMER"></a>

<a id="app__bt__handle_8h_1a35003577db7eaff68f1d078488bed3d5"></a> LOCAL\_PD\_TIMER

<a id="c.PEER_PD_TIMER"></a>

<a id="app__bt__handle_8h_1a40cc65dba3601a2c332dc3c5fd627f91"></a> PEER\_PD\_TIMER
