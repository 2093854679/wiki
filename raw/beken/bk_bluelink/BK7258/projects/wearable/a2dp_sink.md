---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_bluelink/bk7258/zh_CN/v2.0.1/projects/wearable/a2dp_sink.html
sdk_family: bk_bluelink
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="a2dp-sink"></a>

# a2dp\_sink 使用说明

a2dp\_sink\_demo.c 是一个蓝牙A2DP Sink功能的实现示例，主要功能包括：

1. A2DP SINK 支持，蓝牙音频接收与解码（支持SBC和AAC格式）；
2. AVRCP CT/TG 支持，音频播放控制（播放/暂停/音量调节/快进/快退等）；
3. GAP链路管理；
4. 音频播放；

A2DP 音频处理流程：

<a id="id1"></a>
![gatt client demo work flow chart](../../../../_assets/bffdfb5e5c40580610a7-a2dp-demo.png)


Figure 1\. a2dp stream processing flow

<a id="header-file"></a>

## Header File

- [a2dp\_sink\_demo.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/a2dp_sink_demo.h)

<a id="functions"></a>

## Functions

<a id="_CPPv419a2dp_sink_demo_init7uint8_t"></a>

<a id="_CPPv319a2dp_sink_demo_init7uint8_t"></a> <a id="_CPPv219a2dp_sink_demo_init7uint8_t"></a> <a id="a2dp_sink_demo_init__uint8_t"></a> <a id="a2dp__sink__demo_8h_1aa880defacc8b51135fd1b565b1c80a7e"></a> int a2dp\_sink\_demo\_init(uint8\_t aac\_supported)

<a id="_CPPv421a2dp_sink_demo_deinitv"></a>

<a id="_CPPv321a2dp_sink_demo_deinitv"></a> <a id="_CPPv221a2dp_sink_demo_deinitv"></a> <a id="a2dp_sink_demo_deinit__void"></a> <a id="a2dp__sink__demo_8h_1a9cabec6f8c04e67b9bf93ed13653f06b"></a> int a2dp\_sink\_demo\_deinit(void)

<a id="_CPPv427bk_bt_app_avrcp_ct_get_attr8uint32_t"></a>

<a id="_CPPv327bk_bt_app_avrcp_ct_get_attr8uint32_t"></a> <a id="_CPPv227bk_bt_app_avrcp_ct_get_attr8uint32_t"></a> <a id="bk_bt_app_avrcp_ct_get_attr__uint32_t"></a> <a id="a2dp__sink__demo_8h_1a4e1892cca2bcc3a78730eaf96d7320bb"></a> int32\_t bk\_bt\_app\_avrcp\_ct\_get\_attr(uint32\_t attr)

<a id="_CPPv422a2dp_sink_demo_set_mix7uint8_t"></a>

<a id="_CPPv322a2dp_sink_demo_set_mix7uint8_t"></a> <a id="_CPPv222a2dp_sink_demo_set_mix7uint8_t"></a> <a id="a2dp_sink_demo_set_mix__uint8_t"></a> <a id="a2dp__sink__demo_8h_1a475e84bbaffda3b2c16ced090a306b6b"></a> void a2dp\_sink\_demo\_set\_mix(uint8\_t enable)

<a id="_CPPv431bk_bt_app_a2dp_audio_spk_enable7uint8_t"></a>

<a id="_CPPv331bk_bt_app_a2dp_audio_spk_enable7uint8_t"></a> <a id="_CPPv231bk_bt_app_a2dp_audio_spk_enable7uint8_t"></a> <a id="bk_bt_app_a2dp_audio_spk_enable__uint8_t"></a> <a id="a2dp__sink__demo_8h_1a1397cc51b4241e2f47435c0ab0681a91"></a> void bk\_bt\_app\_a2dp\_audio\_spk\_enable(uint8\_t enable)

<a id="_CPPv431bk_bt_a2dp_sink_demo_debug_infov"></a>

<a id="_CPPv331bk_bt_a2dp_sink_demo_debug_infov"></a> <a id="_CPPv231bk_bt_a2dp_sink_demo_debug_infov"></a> <a id="bk_bt_a2dp_sink_demo_debug_info__void"></a> <a id="a2dp__sink__demo_8h_1a1fd884438986cfd41701eb6628f0fd0a"></a> void bk\_bt\_a2dp\_sink\_demo\_debug\_info(void)
