---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/bt_audio_proxy/bt_audio_dsp_ctrl.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bluetooth-audio-dsp-control-functions"></a>

# Bluetooth Audio DSP Control Functions

<a id="bt-audio-dsp-api-brief"></a>

## BT\_AUDIO\_DSP API Brief

| Application | Brief |
| --- | --- |
| [`bt_audio_dsp_set_vol()`](#_CPPv420bt_audio_dsp_set_volP20bt_audio_proxy_ctx_t19audio_stream_type_t7uint8_t "bt_audio_dsp_set_vol") | Set DSP audio volume |
| [`bt_audio_dsp_set_mute()`](#_CPPv421bt_audio_dsp_set_mute19audio_stream_type_tb "bt_audio_dsp_set_mute") | Set DSP audio mute status |
| [`bt_audio_dsp_get_mute()`](#_CPPv421bt_audio_dsp_get_mute19audio_stream_type_tPb "bt_audio_dsp_get_mute") | Get DSP audio mute status |
| [`bt_audio_dsp_a2dp_stream_start()`](#_CPPv430bt_audio_dsp_a2dp_stream_startP20bt_audio_proxy_ctx_t "bt_audio_dsp_a2dp_stream_start") | Start a2dp stream decoding |
| [`bt_audio_dsp_rx_a2dp_stream_data()`](#_CPPv432bt_audio_dsp_rx_a2dp_stream_dataPK7uint8_t8uint16_t8uint32_t8uint32_t7uint8_t "bt_audio_dsp_rx_a2dp_stream_data") | Receive a2dp stream data |
| [`bt_audio_dsp_stop_a2dp_stream()`](#_CPPv429bt_audio_dsp_stop_a2dp_stream8uint16_tb "bt_audio_dsp_stop_a2dp_stream") | Stop a2dp stream decoding |
| [`bt_audio_dsp_start_hfp_stream()`](#_CPPv429bt_audio_dsp_start_hfp_stream8uint16_t16btif_sco_codec_t8uint16_t8uint16_t7uint8_t "bt_audio_dsp_start_hfp_stream") | Start sco stream decoding |
| [`bt_audio_dsp_stop_hfp_stream()`](#_CPPv428bt_audio_dsp_stop_hfp_streamv "bt_audio_dsp_stop_hfp_stream") | Stop sco stream decoding |
| [`bt_audio_dsp_start_ring()`](#_CPPv423bt_audio_dsp_start_ringv "bt_audio_dsp_start_ring") | Start call ringing |
| [`bt_audio_dsp_stop_ring()`](#_CPPv422bt_audio_dsp_stop_ringv "bt_audio_dsp_stop_ring") | Stop call ringing |
| [`bt_audio_dsp_ctrl_register_audio_callback()`](#_CPPv441bt_audio_dsp_ctrl_register_audio_callbackPK17bt_audio_dsp_cb_t "bt_audio_dsp_ctrl_register_audio_callback") | Register DSP audio callback |

<a id="bt-audio-dsp-api-reference"></a>

## BT\_AUDIO\_DSP API Reference

<a id="header-file"></a>

### Header File

- [bt\_audio\_proxy/inc/bt\_audio\_dsp\_ctrl.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/bt_audio_proxy/inc/bt_audio_dsp_ctrl.h)

<a id="functions"></a>

### Functions

<a id="_CPPv420bt_audio_dsp_set_volP20bt_audio_proxy_ctx_t19audio_stream_type_t7uint8_t"></a>

<a id="_CPPv320bt_audio_dsp_set_volP20bt_audio_proxy_ctx_t19audio_stream_type_t7uint8_t"></a> <a id="_CPPv220bt_audio_dsp_set_volP20bt_audio_proxy_ctx_t19audio_stream_type_t7uint8_t"></a> <a id="bt_audio_dsp_set_vol__bt_audio_proxy_ctx_tP.audio_stream_type_t.uint8_t"></a> <a id="bt__audio__dsp__ctrl_8h_1a8a3e9673771035793eb33b84a0daa2d7"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_dsp\_set\_vol([bt\_audio\_proxy\_ctx\_t](bt_audio_proxy.md#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*p\_audio\_proxy, [audio\_stream\_type\_t](bt_audio_proxy.md#_CPPv419audio_stream_type_t "audio_stream_type_t") stream\_type, uint8\_t vol)
:   Set DSP audio volume.

    Set the audio volume \[vol\] to the audio volume of mobile phone stream type \[stream\_type\] if the mobile phone specified by the proxy context \[p\_audio\_proxy\] is playing.

    参数:
    :   - **p\_audio\_proxy** – **\[in\]** pointer to an audio proxy context of type [bt\_audio\_proxy\_ctx\_t](bt_audio_proxy.md#structbt__audio__proxy__ctx__t)
        - **stream\_type** – **\[in\]** stream type of type audio\_stream\_type\_t
        - **vol** – **\[in\]** audio volume value

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421bt_audio_dsp_set_mute19audio_stream_type_tb"></a>

<a id="_CPPv321bt_audio_dsp_set_mute19audio_stream_type_tb"></a> <a id="_CPPv221bt_audio_dsp_set_mute19audio_stream_type_tb"></a> <a id="bt_audio_dsp_set_mute__audio_stream_type_t.b"></a> <a id="bt__audio__dsp__ctrl_8h_1a57187b21d0105d40ec2f6dcf7ccdc703"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_dsp\_set\_mute([audio\_stream\_type\_t](bt_audio_proxy.md#_CPPv419audio_stream_type_t "audio_stream_type_t") type, bool mute)
:   Set DSP audio mute status.

    Set the mute status \[mute\] to the mute status of mobile phone stream type \[type\].

    参数:
    :   - **type** – **\[in\]** stream type of type audio\_stream\_type\_t
        - **mute** – **\[in\]** mute status

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421bt_audio_dsp_get_mute19audio_stream_type_tPb"></a>

<a id="_CPPv321bt_audio_dsp_get_mute19audio_stream_type_tPb"></a> <a id="_CPPv221bt_audio_dsp_get_mute19audio_stream_type_tPb"></a> <a id="bt_audio_dsp_get_mute__audio_stream_type_t.bP"></a> <a id="bt__audio__dsp__ctrl_8h_1a5e57c20d821fa89a53f045903955d7f3"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_dsp\_get\_mute([audio\_stream\_type\_t](bt_audio_proxy.md#_CPPv419audio_stream_type_t "audio_stream_type_t") type, bool \*mute)
:   Get DSP audio mute status.

    Get the mute status of mobile phone stream type \[type\].

    参数:
    :   - **type** – **\[in\]** stream type of type audio\_stream\_type\_t
        - **mute** – **\[in\]** pointer to a mute status for getting the data

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv430bt_audio_dsp_a2dp_stream_startP20bt_audio_proxy_ctx_t"></a>

<a id="_CPPv330bt_audio_dsp_a2dp_stream_startP20bt_audio_proxy_ctx_t"></a> <a id="_CPPv230bt_audio_dsp_a2dp_stream_startP20bt_audio_proxy_ctx_t"></a> <a id="bt_audio_dsp_a2dp_stream_start__bt_audio_proxy_ctx_tP"></a> <a id="bt__audio__dsp__ctrl_8h_1a20b4d74cf25051d6ec01352707b0521e"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_dsp\_a2dp\_stream\_start([bt\_audio\_proxy\_ctx\_t](bt_audio_proxy.md#_CPPv420bt_audio_proxy_ctx_t "bt_audio_proxy_ctx_t") \*p\_audio\_proxy)
:   Start a2dp stream decoding.

    Start decoding the mobile phone a2dp stream specified by the proxy context \[p\_audio\_proxy\]

    参数:
    :   **p\_audio\_proxy** – **\[in\]** pointer to an audio proxy context of type [bt\_audio\_proxy\_ctx\_t](bt_audio_proxy.md#structbt__audio__proxy__ctx__t)

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv432bt_audio_dsp_rx_a2dp_stream_dataPK7uint8_t8uint16_t8uint32_t8uint32_t7uint8_t"></a>

<a id="_CPPv332bt_audio_dsp_rx_a2dp_stream_dataPK7uint8_t8uint16_t8uint32_t8uint32_t7uint8_t"></a> <a id="_CPPv232bt_audio_dsp_rx_a2dp_stream_dataPK7uint8_t8uint16_t8uint32_t8uint32_t7uint8_t"></a> <a id="bt_audio_dsp_rx_a2dp_stream_data__uint8_tCP.uint16_t.uint32_t.uint32_t.uint8_t"></a> <a id="bt__audio__dsp__ctrl_8h_1a7812220bd9a1f2014e9a14149889de9c"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_dsp\_rx\_a2dp\_stream\_data(const uint8\_t \*p\_data, uint16\_t len, uint32\_t pac\_seq, uint32\_t frame\_seq, uint8\_t cp\_len)
:   Receive a2dp stream data.

    Receive and process a2dp media stream data

    参数:
    :   - **p\_data** – **\[in\]** pointer to a2dp media stream data
        - **len** – **\[in\]** length of a2dp media stream data
        - **pac\_seq** – **\[in\]** packet sequence number
        - **frame\_seq** – **\[in\]** frame sequence number
        - **cp\_len** – **\[in\]** content protection header length

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv429bt_audio_dsp_stop_a2dp_stream8uint16_tb"></a>

<a id="_CPPv329bt_audio_dsp_stop_a2dp_stream8uint16_tb"></a> <a id="_CPPv229bt_audio_dsp_stop_a2dp_stream8uint16_tb"></a> <a id="bt_audio_dsp_stop_a2dp_stream__uint16_t.b"></a> <a id="bt__audio__dsp__ctrl_8h_1a302ec71ba23245c4758742590780f9b1"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_dsp\_stop\_a2dp\_stream(uint16\_t handle, bool at\_once)
:   Stop a2dp stream decoding.

    Stop decoding the a2dp stream of the mobile phone with connection handle \[handle\]

    参数:
    :   - **handle** – **\[in\]** connection handle
        - **at\_once** – **\[in\]** at once

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv429bt_audio_dsp_start_hfp_stream8uint16_t16btif_sco_codec_t8uint16_t8uint16_t7uint8_t"></a>

<a id="_CPPv329bt_audio_dsp_start_hfp_stream8uint16_t16btif_sco_codec_t8uint16_t8uint16_t7uint8_t"></a> <a id="_CPPv229bt_audio_dsp_start_hfp_stream8uint16_t16btif_sco_codec_t8uint16_t8uint16_t7uint8_t"></a> <a id="bt_audio_dsp_start_hfp_stream__uint16_t.btif_sco_codec_t.uint16_t.uint16_t.uint8_t"></a> <a id="bt__audio__dsp__ctrl_8h_1aa1ec6cf88024baded21d527aa59a8d9b"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_dsp\_start\_hfp\_stream(uint16\_t acl\_handle, [btif\_sco\_codec\_t](../btif/btif_type.md#_CPPv416btif_sco_codec_t "btif_sco_codec_t") codec, uint16\_t rx\_pkt\_len, uint16\_t tx\_pkt\_len, uint8\_t vol)
:   Start sco stream decoding.

    Start decoding the sco stream of the mobile phone with connection handle \[acl\_handle\]

    参数:
    :   - **acl\_handle** – **\[in\]** acl handle
        - **codec** – **\[in\]** sco codec type of type btif\_sco\_codec\_t
        - **rx\_pkt\_len** – **\[in\]** rx packet length
        - **tx\_pkt\_len** – **\[in\]** tx packet length
        - **vol** – **\[in\]** voice volume

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv428bt_audio_dsp_stop_hfp_streamv"></a>

<a id="_CPPv328bt_audio_dsp_stop_hfp_streamv"></a> <a id="_CPPv228bt_audio_dsp_stop_hfp_streamv"></a> <a id="bt_audio_dsp_stop_hfp_stream__void"></a> <a id="bt__audio__dsp__ctrl_8h_1a477500f1f727055baae8ed68c3ebc0ec"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_dsp\_stop\_hfp\_stream(void)
:   Stop sco stream decoding.

    Stop decoding the sco stream.

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv423bt_audio_dsp_start_ringv"></a>

<a id="_CPPv323bt_audio_dsp_start_ringv"></a> <a id="_CPPv223bt_audio_dsp_start_ringv"></a> <a id="bt_audio_dsp_start_ring__void"></a> <a id="bt__audio__dsp__ctrl_8h_1a518369cc2d1872624e86844b4b285792"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_dsp\_start\_ring(void)
:   Start call ringing.

    Handle HFP ring event.

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422bt_audio_dsp_stop_ringv"></a>

<a id="_CPPv322bt_audio_dsp_stop_ringv"></a> <a id="_CPPv222bt_audio_dsp_stop_ringv"></a> <a id="bt_audio_dsp_stop_ring__void"></a> <a id="bt__audio__dsp__ctrl_8h_1af92d10a99e471ef80aef84bd9c464aa2"></a> [btif\_ret\_t](../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") bt\_audio\_dsp\_stop\_ring(void)
:   Stop call ringing.

    Stop call ringing on HSP release event.

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv441bt_audio_dsp_ctrl_register_audio_callbackPK17bt_audio_dsp_cb_t"></a>

<a id="_CPPv341bt_audio_dsp_ctrl_register_audio_callbackPK17bt_audio_dsp_cb_t"></a> <a id="_CPPv241bt_audio_dsp_ctrl_register_audio_callbackPK17bt_audio_dsp_cb_t"></a> <a id="bt_audio_dsp_ctrl_register_audio_callback__bt_audio_dsp_cb_tCP"></a> <a id="bt__audio__dsp__ctrl_8h_1a509cb76a1445ea95a355a7df5bc9f13c"></a> void bt\_audio\_dsp\_ctrl\_register\_audio\_callback(const [bt\_audio\_dsp\_cb\_t](#_CPPv417bt_audio_dsp_cb_t "bt_audio_dsp_cb_t") \*p\_audio\_cb)
:   Register DSP audio callback.

    Register the audio callback \[p\_audio\_cb\] into the DSP control callback

    参数:
    :   **p\_audio\_cb** – **\[in\]** pointer to audio callback function of type [bt\_audio\_dsp\_cb\_t](#structbt__audio__dsp__cb__t)

    返回:
    :   N/A **BT\_AUDIO\_DSP\_CTRL\_H** EOF

<a id="structures"></a>

### Structures

<a id="_CPPv417bt_audio_dsp_cb_t"></a>

<a id="_CPPv317bt_audio_dsp_cb_t"></a> <a id="_CPPv217bt_audio_dsp_cb_t"></a> <a id="bt_audio_dsp_cb_t"></a> <a id="structbt__audio__dsp__cb__t"></a> struct bt\_audio\_dsp\_cb\_t
:   DSP callback structure definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17bt_audio_dsp_cb_t15a2dp_codec_initE"></a>

    <a id="_CPPv3N17bt_audio_dsp_cb_t15a2dp_codec_initE"></a> <a id="_CPPv2N17bt_audio_dsp_cb_t15a2dp_codec_initE"></a> <a id="bt_audio_dsp_cb_t::a2dp_codec_init__bt_audio_dsp_a2dp_stream_codec_init"></a> <a id="structbt__audio__dsp__cb__t_1adb9210387d566ccd8115f7cd787bba8d"></a> [bt\_audio\_dsp\_a2dp\_stream\_codec\_init](#_CPPv435bt_audio_dsp_a2dp_stream_codec_init "bt_audio_dsp_a2dp_stream_codec_init") a2dp\_codec\_init
    :   \< a2dp \- high layer callback

    <a id="_CPPv4N17bt_audio_dsp_cb_t19a2dp_rx_stream_dataE"></a>

    <a id="_CPPv3N17bt_audio_dsp_cb_t19a2dp_rx_stream_dataE"></a> <a id="_CPPv2N17bt_audio_dsp_cb_t19a2dp_rx_stream_dataE"></a> <a id="bt_audio_dsp_cb_t::a2dp_rx_stream_data__bt_audio_dsp_a2dp_rx_stream_data"></a> <a id="structbt__audio__dsp__cb__t_1add0264b3076d5f0b945b16b60d733793"></a> [bt\_audio\_dsp\_a2dp\_rx\_stream\_data](#_CPPv432bt_audio_dsp_a2dp_rx_stream_data "bt_audio_dsp_a2dp_rx_stream_data") a2dp\_rx\_stream\_data
    :   sco \- high layer callback

    <a id="_CPPv4N17bt_audio_dsp_cb_t16sco_codec_deinitE"></a>

    <a id="_CPPv3N17bt_audio_dsp_cb_t16sco_codec_deinitE"></a> <a id="_CPPv2N17bt_audio_dsp_cb_t16sco_codec_deinitE"></a> <a id="bt_audio_dsp_cb_t::sco_codec_deinit__bt_audio_dsp_sco_codec_deinit"></a> <a id="structbt__audio__dsp__cb__t_1a6ee0d10ed4f96e1527cb958ea5357393"></a> [bt\_audio\_dsp\_sco\_codec\_deinit](#_CPPv429bt_audio_dsp_sco_codec_deinit "bt_audio_dsp_sco_codec_deinit") sco\_codec\_deinit
    :   high layer set valume callback

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv437bt_audio_dsp_a2dp_stream_codec_deinit"></a>

<a id="_CPPv337bt_audio_dsp_a2dp_stream_codec_deinit"></a> <a id="_CPPv237bt_audio_dsp_a2dp_stream_codec_deinit"></a> <a id="bt_audio_dsp_a2dp_stream_codec_deinit"></a> <a id="bt__audio__dsp__ctrl_8h_1ac4fa6b31df8e1aaab49db6835a838ced"></a> typedef void (\*bt\_audio\_dsp\_a2dp\_stream\_codec\_deinit)(void)
:   A2DP stream codec deinitialize function pointer definition.

<a id="_CPPv423bt_audio_dsp_set_volume"></a>

<a id="_CPPv323bt_audio_dsp_set_volume"></a> <a id="_CPPv223bt_audio_dsp_set_volume"></a> <a id="bt_audio_dsp_set_volume"></a> <a id="bt__audio__dsp__ctrl_8h_1a52c191e9b24c013ef521abfcd7ad8001"></a> typedef void (\*bt\_audio\_dsp\_set\_volume)(uint8\_t id, uint32\_t volume)
:   set volume function pointer definition.

<a id="_CPPv435bt_audio_dsp_a2dp_stream_codec_init"></a>

<a id="_CPPv335bt_audio_dsp_a2dp_stream_codec_init"></a> <a id="_CPPv235bt_audio_dsp_a2dp_stream_codec_init"></a> <a id="bt_audio_dsp_a2dp_stream_codec_init"></a> <a id="bt__audio__dsp__ctrl_8h_1a349f607fe921409b5eec1419c17218f9"></a> typedef void (\*bt\_audio\_dsp\_a2dp\_stream\_codec\_init)(uint32\_t codec\_type, uint32\_t sample\_rate, uint32\_t channels, uint16\_t frame\_cnt\_per\_pkt, uint8\_t vol)
:   A2DP stream codec initialize function pointer definition.

<a id="_CPPv432bt_audio_dsp_a2dp_rx_stream_data"></a>

<a id="_CPPv332bt_audio_dsp_a2dp_rx_stream_data"></a> <a id="_CPPv232bt_audio_dsp_a2dp_rx_stream_data"></a> <a id="bt_audio_dsp_a2dp_rx_stream_data"></a> <a id="bt__audio__dsp__ctrl_8h_1a2e502ce8d8742d6e282c28749cdd7128"></a> typedef void (\*bt\_audio\_dsp\_a2dp\_rx\_stream\_data)(const uint8\_t \*p\_data, uint16\_t len, uint32\_t pac\_seq, uint32\_t frame\_seq, uint8\_t cp\_len)
:   Handle A2DP rx stream data function pointer definition.

<a id="_CPPv429bt_audio_dsp_sco_codec_deinit"></a>

<a id="_CPPv329bt_audio_dsp_sco_codec_deinit"></a> <a id="_CPPv229bt_audio_dsp_sco_codec_deinit"></a> <a id="bt_audio_dsp_sco_codec_deinit"></a> <a id="bt__audio__dsp__ctrl_8h_1aae7f88bbad9f2107f4006fb2f9518346"></a> typedef void (\*bt\_audio\_dsp\_sco\_codec\_deinit)(void)
:   SCO codec deinitialize function pointer definition.

<a id="_CPPv427bt_audio_dsp_sco_codec_init"></a>

<a id="_CPPv327bt_audio_dsp_sco_codec_init"></a> <a id="_CPPv227bt_audio_dsp_sco_codec_init"></a> <a id="bt_audio_dsp_sco_codec_init"></a> <a id="bt__audio__dsp__ctrl_8h_1abf50228bace42f53ad699fffdd022fd1"></a> typedef void (\*bt\_audio\_dsp\_sco\_codec\_init)(uint32\_t codec\_type, uint8\_t vol)
:   SCO codec initialize function pointer definition.
