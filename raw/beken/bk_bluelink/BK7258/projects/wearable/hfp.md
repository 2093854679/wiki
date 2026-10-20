---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_bluelink/bk7258/zh_CN/v2.0.1/projects/wearable/hfp.html
sdk_family: bk_bluelink
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="hfp"></a>

# HFP 使用说明

hfp\_hf\_demo.c 文件是HFP（Hands-Free Profile） HF端功能的实现示例，主要功能包括：

1.HF功能实现 ：

- 实现HFP HF端状态管理（空闲/连接/通话等状态）；
- HFP AT命令（音量控制、拨号、拒接等）处理；
- 支持SCO/eSCO 音频链路管理；

2.音频处理 ：

- 支持CVSD和mSBC两种语音编解码；
- 实现麦克风数据采集编码传输（ mic\_task ）；
- 实现SCO/eSCO数据解码扬声器播放（ speaker\_task ）；

音频处理流程：

<a id="id1"></a>
![gatt client demo work flow chart](../../../../_assets/8b3ae066ad256b688905-hfp-demo.png)


Figure 1\. audio stream processing flow

<a id="header-file"></a>

## Header File

- [hfp\_hf\_demo.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hfp_hf_demo.h)

<a id="functions"></a>

## Functions

<a id="_CPPv416hfp_hf_demo_init7uint8_t"></a>

<a id="_CPPv316hfp_hf_demo_init7uint8_t"></a> <a id="_CPPv216hfp_hf_demo_init7uint8_t"></a> <a id="hfp_hf_demo_init__uint8_t"></a> <a id="hfp__hf__demo_8h_1ac7be1459caac9ae4b731804fbbf6e572"></a> int hfp\_hf\_demo\_init(uint8\_t msbc\_supported)

<a id="_CPPv418hfp_hf_demo_deinitv"></a>

<a id="_CPPv318hfp_hf_demo_deinitv"></a> <a id="_CPPv218hfp_hf_demo_deinitv"></a> <a id="hfp_hf_demo_deinit__void"></a> <a id="hfp__hf__demo_8h_1abe5b8f3959a93266e574c34b45e9f9cb"></a> int hfp\_hf\_demo\_deinit(void)

<a id="_CPPv411hfp_demo_vr7uint8_t"></a>

<a id="_CPPv311hfp_demo_vr7uint8_t"></a> <a id="_CPPv211hfp_demo_vr7uint8_t"></a> <a id="hfp_demo_vr__uint8_t"></a> <a id="hfp__hf__demo_8h_1aa22fc09dd330a75230238670ceb1dd20"></a> void hfp\_demo\_vr(uint8\_t enable)

<a id="_CPPv413hfp_demo_dial7uint8_tP7uint8_t"></a>

<a id="_CPPv313hfp_demo_dial7uint8_tP7uint8_t"></a> <a id="_CPPv213hfp_demo_dial7uint8_tP7uint8_t"></a> <a id="hfp_demo_dial__uint8_t.uint8_tP"></a> <a id="hfp__hf__demo_8h_1a3ecce751bdde46d286a8e2ec756404ce"></a> void hfp\_demo\_dial(uint8\_t enable, uint8\_t \*num)

<a id="_CPPv415hfp_demo_answer7uint8_t"></a>

<a id="_CPPv315hfp_demo_answer7uint8_t"></a> <a id="_CPPv215hfp_demo_answer7uint8_t"></a> <a id="hfp_demo_answer__uint8_t"></a> <a id="hfp__hf__demo_8h_1ada554aa8e9667c7312b886aa714068fa"></a> void hfp\_demo\_answer(uint8\_t accept)

<a id="_CPPv417hfp_demo_cust_cmdP7uint8_t"></a>

<a id="_CPPv317hfp_demo_cust_cmdP7uint8_t"></a> <a id="_CPPv217hfp_demo_cust_cmdP7uint8_t"></a> <a id="hfp_demo_cust_cmd__uint8_tP"></a> <a id="hfp__hf__demo_8h_1a23e7712ec6b4ea1873284fd118101eda"></a> void hfp\_demo\_cust\_cmd(uint8\_t \*cmd)

<a id="_CPPv417hfp_demo_chld_cmd7uint8_t"></a>

<a id="_CPPv317hfp_demo_chld_cmd7uint8_t"></a> <a id="_CPPv217hfp_demo_chld_cmd7uint8_t"></a> <a id="hfp_demo_chld_cmd__uint8_t"></a> <a id="hfp__hf__demo_8h_1ad654a5434ea0ee58ad2efbd57d62a2ba"></a> int32\_t hfp\_demo\_chld\_cmd(uint8\_t op)

<a id="_CPPv417hfp_demo_btrh_cmd7uint8_t"></a>

<a id="_CPPv317hfp_demo_btrh_cmd7uint8_t"></a> <a id="_CPPv217hfp_demo_btrh_cmd7uint8_t"></a> <a id="hfp_demo_btrh_cmd__uint8_t"></a> <a id="hfp__hf__demo_8h_1aae7e7332dee78f03c1bb622647f7e117"></a> int32\_t hfp\_demo\_btrh\_cmd(uint8\_t op)
