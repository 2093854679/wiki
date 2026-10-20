---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/bt_audio_proxy/bt_audio_a2dp_ctrl.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bluetooth-audio-a2dp-control-functions"></a>

# Bluetooth Audio A2DP Control Functions

<a id="bt-audio-a2dp-api-brief"></a>

## BT\_AUDIO\_A2DP API Brief

| Application | Brief |
| --- | --- |
| [`bt_audio_a2dp_ctrl_init()`](#_CPPv423bt_audio_a2dp_ctrl_initb "bt_audio_a2dp_ctrl_init") | Initialize A2DP audio control |
| [`bt_audio_a2dp_ctrl_get_recent_pac_seq()`](#_CPPv437bt_audio_a2dp_ctrl_get_recent_pac_seqv "bt_audio_a2dp_ctrl_get_recent_pac_seq") | Get the reconnect packet sequence number |
| [`bt_audio_a2dp_ctrl_get_start_pac_seq()`](#_CPPv436bt_audio_a2dp_ctrl_get_start_pac_seqv "bt_audio_a2dp_ctrl_get_start_pac_seq") | Get the start packet sequence number |
| [`bt_audio_a2dp_ctrl_set_start_pac_seq()`](#_CPPv436bt_audio_a2dp_ctrl_set_start_pac_seq8uint32_t "bt_audio_a2dp_ctrl_set_start_pac_seq") | Set the start packet sequence number |

<a id="bt-audio-a2dp-api-reference"></a>

## BT\_AUDIO\_A2DP API Reference

<a id="header-file"></a>

### Header File

- [bt\_audio\_proxy/inc/bt\_audio\_a2dp\_ctrl.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/bt_audio_proxy/inc/bt_audio_a2dp_ctrl.h)

<a id="functions"></a>

### Functions

<a id="_CPPv423bt_audio_a2dp_ctrl_initb"></a>

<a id="_CPPv323bt_audio_a2dp_ctrl_initb"></a> <a id="_CPPv223bt_audio_a2dp_ctrl_initb"></a> <a id="bt_audio_a2dp_ctrl_init__b"></a> <a id="bt__audio__a2dp__ctrl_8h_1a4a5f2f79f6690af3f833690548b835fd"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_a2dp\_ctrl\_init(bool aac\_enable)
:   Initialize A2DP audio control.

    Initialize the audio codec and register the callback to handle a2dp audio.

    参数:
    :   **aac\_enable** – **\[in\]** AAC codec enable status. true is enabled, false is disabled.

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result of type btif\_ret\_t

<a id="_CPPv437bt_audio_a2dp_ctrl_get_recent_pac_seqv"></a>

<a id="_CPPv337bt_audio_a2dp_ctrl_get_recent_pac_seqv"></a> <a id="_CPPv237bt_audio_a2dp_ctrl_get_recent_pac_seqv"></a> <a id="bt_audio_a2dp_ctrl_get_recent_pac_seq__void"></a> <a id="bt__audio__a2dp__ctrl_8h_1ad0eb669bf55631b19b02ce5038e9e3aa"></a> uint32\_t bt\_audio\_a2dp\_ctrl\_get\_recent\_pac\_seq(void)
:   Get the reconnect packet sequence number.

    Get the reconnect packet sequence number in a2dp information.

    返回:
    :   packet sequence number

<a id="_CPPv436bt_audio_a2dp_ctrl_get_start_pac_seqv"></a>

<a id="_CPPv336bt_audio_a2dp_ctrl_get_start_pac_seqv"></a> <a id="_CPPv236bt_audio_a2dp_ctrl_get_start_pac_seqv"></a> <a id="bt_audio_a2dp_ctrl_get_start_pac_seq__void"></a> <a id="bt__audio__a2dp__ctrl_8h_1a056670a356218c2ac8cd1300e7c86960"></a> int32\_t bt\_audio\_a2dp\_ctrl\_get\_start\_pac\_seq(void)
:   Get the start packet sequence number.

    Get the start packet sequence number in a2dp information.

    返回:
    :   packet sequence number

<a id="_CPPv436bt_audio_a2dp_ctrl_set_start_pac_seq8uint32_t"></a>

<a id="_CPPv336bt_audio_a2dp_ctrl_set_start_pac_seq8uint32_t"></a> <a id="_CPPv236bt_audio_a2dp_ctrl_set_start_pac_seq8uint32_t"></a> <a id="bt_audio_a2dp_ctrl_set_start_pac_seq__uint32_t"></a> <a id="bt__audio__a2dp__ctrl_8h_1adfc9089cffaf9681dd4bdcc42c49e46f"></a> void bt\_audio\_a2dp\_ctrl\_set\_start\_pac\_seq(uint32\_t start\_seq)
:   Set the start packet sequence number.

    Set the start packet sequence number in the a2dp information to \[start\_seq\].

    参数:
    :   **start\_seq** – **\[in\]** packet sequence number

    返回:
    :   N/A **BT\_AUDIO\_A2DP\_CTRL\_H** EOF

<a id="structures"></a>

### Structures

<a id="_CPPv427bt_audio_if_media_pkt_hdr_t"></a>

<a id="_CPPv327bt_audio_if_media_pkt_hdr_t"></a> <a id="_CPPv227bt_audio_if_media_pkt_hdr_t"></a> <a id="bt_audio_if_media_pkt_hdr_t"></a> <a id="structbt__audio__if__media__pkt__hdr__t"></a> struct bt\_audio\_if\_media\_pkt\_hdr\_t
:   Media packet header structure definition.

<a id="_CPPv427bt_audio_if_sbc_codec_hdr_t"></a>

<a id="_CPPv327bt_audio_if_sbc_codec_hdr_t"></a> <a id="_CPPv227bt_audio_if_sbc_codec_hdr_t"></a> <a id="bt_audio_if_sbc_codec_hdr_t"></a> <a id="structbt__audio__if__sbc__codec__hdr__t"></a> struct bt\_audio\_if\_sbc\_codec\_hdr\_t
:   SBC codec header structure definition.

<a id="macros"></a>

### Macros

<a id="c.BTIF_A2DP_MAX_CSRC_NUM"></a>

<a id="bt__audio__a2dp__ctrl_8h_1a15db209467c549fae73d1706236590c7"></a> BTIF\_A2DP\_MAX\_CSRC\_NUM

<a id="c.BTIF_A2DP_MEDIA_HDR_LEN"></a>

<a id="bt__audio__a2dp__ctrl_8h_1a307bdc2affd5b3b2820e19dedd37bb8e"></a> BTIF\_A2DP\_MEDIA\_HDR\_LEN

<a id="c.BTIF_A2DP_SBC_HDR_LEN"></a>

<a id="bt__audio__a2dp__ctrl_8h_1a260632ef48d398d2bbb9c2de0e8dc7bd"></a> BTIF\_A2DP\_SBC\_HDR\_LEN
