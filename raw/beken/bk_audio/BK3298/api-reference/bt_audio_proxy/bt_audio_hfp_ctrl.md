---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/bt_audio_proxy/bt_audio_hfp_ctrl.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bluetooth-audio-hfp-control-functions"></a>

# Bluetooth Audio HFP Control Functions

<a id="bt-audio-hfp-api-brief"></a>

## BT\_AUDIO\_HFP API Brief

| Application | Brief |
| --- | --- |
| [`bt_audio_hfp_ctrl_set_spk_vol()`](#_CPPv429bt_audio_hfp_ctrl_set_spk_volPv7uint8_t "bt_audio_hfp_ctrl_set_spk_vol") | Set speak volume |
| [`bt_audio_hfp_ctrl_set_mic_vol()`](#_CPPv429bt_audio_hfp_ctrl_set_mic_volPv7uint8_t "bt_audio_hfp_ctrl_set_mic_vol") | Set microphone volume |
| [`bt_audio_hfp_ctrl_init()`](#_CPPv422bt_audio_hfp_ctrl_initv "bt_audio_hfp_ctrl_init") | Initialize HFP control |

<a id="bt-audio-hfp-api-reference"></a>

## BT\_AUDIO\_HFP API Reference

<a id="header-file"></a>

### Header File

- [bt\_audio\_proxy/inc/bt\_audio\_hfp\_ctrl.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/bt_audio_proxy/inc/bt_audio_hfp_ctrl.h)

<a id="functions"></a>

### Functions

<a id="_CPPv429bt_audio_hfp_ctrl_set_spk_volPv7uint8_t"></a>

<a id="_CPPv329bt_audio_hfp_ctrl_set_spk_volPv7uint8_t"></a> <a id="_CPPv229bt_audio_hfp_ctrl_set_spk_volPv7uint8_t"></a> <a id="bt_audio_hfp_ctrl_set_spk_vol__voidP.uint8_t"></a> <a id="bt__audio__hfp__ctrl_8h_1a378446b691bf5360e6ca9354b874c281"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_hfp\_ctrl\_set\_spk\_vol(void \*p\_ctx, uint8\_t value)
:   Set speak volume.

    Set speak volume value to \[value\]

    参数:
    :   - **p\_ctx** – **\[in\]** pointer to an audio proxy context
        - **value** – **\[in\]** speak volume value

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv429bt_audio_hfp_ctrl_set_mic_volPv7uint8_t"></a>

<a id="_CPPv329bt_audio_hfp_ctrl_set_mic_volPv7uint8_t"></a> <a id="_CPPv229bt_audio_hfp_ctrl_set_mic_volPv7uint8_t"></a> <a id="bt_audio_hfp_ctrl_set_mic_vol__voidP.uint8_t"></a> <a id="bt__audio__hfp__ctrl_8h_1a0e7cb7bef9f84014bc1921bdaad79c80"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_hfp\_ctrl\_set\_mic\_vol(void \*p\_ctx, uint8\_t value)
:   Set microphone volume.

    Set microphone volume value to \[value\]

    参数:
    :   - **p\_ctx** – **\[in\]** pointer to an audio proxy context
        - **value** – **\[in\]** microphone volume value

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422bt_audio_hfp_ctrl_initv"></a>

<a id="_CPPv322bt_audio_hfp_ctrl_initv"></a> <a id="_CPPv222bt_audio_hfp_ctrl_initv"></a> <a id="bt_audio_hfp_ctrl_init__void"></a> <a id="bt__audio__hfp__ctrl_8h_1a20ea808c982d29356b82f1c2bff33fad"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_hfp\_ctrl\_init(void)
:   Initialize HFP control.

    Register callback for HFP event handler

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail **BT\_AUDIO\_HFP\_CTRL\_H** EOF

    返回:
    :   result
