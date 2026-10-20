---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/bt_audio_proxy/bt_audio_avrcp_ctrl.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bluetooth-audio-avrcp-control-functions"></a>

# Bluetooth Audio AVRCP Control Functions

<a id="bt-audio-avrcp-api-brief"></a>

## BT\_AUDIO\_AVRCP API Brief

| Application | Brief |
| --- | --- |
| [`bt_audio_avrcp_ctrl_play_pause()`](#_CPPv430bt_audio_avrcp_ctrl_play_pausev "bt_audio_avrcp_ctrl_play_pause") | AVRCP control audio play/pause |
| [`bt_audio_avrcp_ctrl_tx_cmd()`](#_CPPv426bt_audio_avrcp_ctrl_tx_cmd23bt_audio_proxy_cmd_id_t "bt_audio_avrcp_ctrl_tx_cmd") | Send AVRCP control command |
| [`bt_audio_avrcp_ctrl_set_vol()`](#_CPPv427bt_audio_avrcp_ctrl_set_volP20bt_audio_proxy_ctx_t7uint8_t "bt_audio_avrcp_ctrl_set_vol") | Set volume via AVRCP |
| [`bt_audio_avrcp_ctrl_init()`](#_CPPv424bt_audio_avrcp_ctrl_initv "bt_audio_avrcp_ctrl_init") | Initialize AVRCP audio control |
| [`bt_audio_force_stop_dither_timer()`](#_CPPv432bt_audio_force_stop_dither_timerv "bt_audio_force_stop_dither_timer") | Force stop dither timer |

<a id="bt-audio-avrcp-api-reference"></a>

## BT\_AUDIO\_AVRCP API Reference

<a id="header-file"></a>

### Header File

- [bt\_audio\_proxy/inc/bt\_audio\_avrcp\_ctrl.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/bt_audio_proxy/inc/bt_audio_avrcp_ctrl.h)

<a id="functions"></a>

### Functions

<a id="_CPPv430bt_audio_avrcp_ctrl_play_pausev"></a>

<a id="_CPPv330bt_audio_avrcp_ctrl_play_pausev"></a> <a id="_CPPv230bt_audio_avrcp_ctrl_play_pausev"></a> <a id="bt_audio_avrcp_ctrl_play_pause__void"></a> <a id="bt__audio__avrcp__ctrl_8h_1a64cc6d60c3ba16224db985eb77ade362"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_avrcp\_ctrl\_play\_pause(void)
:   AVRCP control audio play/pause.

    Toggle active mobile phone to play or pause audio via AVRCP.

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426bt_audio_avrcp_ctrl_tx_cmd23bt_audio_proxy_cmd_id_t"></a>

<a id="_CPPv326bt_audio_avrcp_ctrl_tx_cmd23bt_audio_proxy_cmd_id_t"></a> <a id="_CPPv226bt_audio_avrcp_ctrl_tx_cmd23bt_audio_proxy_cmd_id_t"></a> <a id="bt_audio_avrcp_ctrl_tx_cmd__bt_audio_proxy_cmd_id_t"></a> <a id="bt__audio__avrcp__ctrl_8h_1a5daed5cd75cdd76121a308797f69f05c"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_avrcp\_ctrl\_tx\_cmd([bt\_audio\_proxy\_cmd\_id\_t](bt_audio_proxy.md#_CPPv423bt_audio_proxy_cmd_id_t "bt_audio_proxy_cmd_id_t") cmd)
:   Send AVRCP control command.

    Send AVRCP control command to active mobile phone.

    参数:
    :   **cmd** – **\[in\]** AVRCP control command of type bt\_audio\_proxy\_cmd\_id\_t.

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427bt_audio_avrcp_ctrl_set_volP20bt_audio_proxy_ctx_t7uint8_t"></a>

<a id="_CPPv327bt_audio_avrcp_ctrl_set_volP20bt_audio_proxy_ctx_t7uint8_t"></a> <a id="_CPPv227bt_audio_avrcp_ctrl_set_volP20bt_audio_proxy_ctx_t7uint8_t"></a> <a id="bt_audio_avrcp_ctrl_set_vol__bt_audio_proxy_ctx_tP.uint8_t"></a> <a id="bt__audio__avrcp__ctrl_8h_1a1b67609193e95765e17f0bd24c8aeffc"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_avrcp\_ctrl\_set\_vol([bt\_audio\_proxy\_ctx\_t](bt_audio_proxy.md#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*p\_proxy\_ctx, uint8\_t value)
:   Set volume via AVRCP.

    Set the local audio volume \[value\] to the mobile phone audio volume specified by the proxy context \[p\_proxy\_ctx\] via AVRCP.

    参数:
    :   - **p\_proxy\_ctx** – **\[in\]** pointer to an audio proxy context of type [bt\_audio\_proxy\_ctx\_t](bt_audio_proxy.md#structbt__audio__proxy__ctx__t).
        - **value** – **\[in\]** local audio volume value, range 0 to 15\.

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424bt_audio_avrcp_ctrl_initv"></a>

<a id="_CPPv324bt_audio_avrcp_ctrl_initv"></a> <a id="_CPPv224bt_audio_avrcp_ctrl_initv"></a> <a id="bt_audio_avrcp_ctrl_init__void"></a> <a id="bt__audio__avrcp__ctrl_8h_1ab5031e3c4d99e94b90643851d2b233a0"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_avrcp\_ctrl\_init(void)
:   Initialize AVRCP audio control.

    Register the callback to handle AVRCP event.

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result of type btif\_ret\_t

<a id="_CPPv432bt_audio_force_stop_dither_timerv"></a>

<a id="_CPPv332bt_audio_force_stop_dither_timerv"></a> <a id="_CPPv232bt_audio_force_stop_dither_timerv"></a> <a id="bt_audio_force_stop_dither_timer__void"></a> <a id="bt__audio__avrcp__ctrl_8h_1ad14db02da2b25cb4004e3a5e8c8d4209"></a> void bt\_audio\_force\_stop\_dither\_timer(void)
:   Force stop dither timer.

    Forces the dither timer to stop when the AVRCP receives a fast-forward or rewind event.

    返回:
    :   N/A **BT\_AUDIO\_AVRCP\_CTRL\_H** EOF
