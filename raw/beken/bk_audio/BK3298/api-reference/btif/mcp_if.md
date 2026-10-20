---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/btif/mcp_if.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="mcp-interface-functions"></a>

# MCP Interface Functions

<a id="mcp-if-api-brief"></a>

## MCP\_IF API Brief

| Application | Brief |
| --- | --- |
| [`mcp_if_register_event_callback()`](#_CPPv430mcp_if_register_event_callbackP19btif_mcp_register_t "mcp_if_register_event_callback") | register event callback function |
| [`mcp_if_init()`](#_CPPv411mcp_if_initv "mcp_if_init") | Media Control Profile interface initialize |
| [`mcp_if_send_cp_opcode()`](#_CPPv421mcp_if_send_cp_opcode8uint16_t18mcp_if_cp_opcode_t "mcp_if_send_cp_opcode") | send Media Control Point opcode |

<a id="mcp-if-api-reference"></a>

## MCP\_IF API Reference

<a id="header-file"></a>

### Header File

- [btif/inc/mcp\_if.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/btif/inc/mcp_if.h)

<a id="functions"></a>

### Functions

<a id="_CPPv430mcp_if_register_event_callbackP19btif_mcp_register_t"></a>

<a id="_CPPv330mcp_if_register_event_callbackP19btif_mcp_register_t"></a> <a id="_CPPv230mcp_if_register_event_callbackP19btif_mcp_register_t"></a> <a id="mcp_if_register_event_callback__btif_mcp_register_tP"></a> <a id="mcp__if_8h_1a764653ca6aa6e853284e0ba98bf0fb78"></a> void mcp\_if\_register\_event\_callback([btif\_mcp\_register\_t](#_CPPv419btif_mcp_register_t "btif_mcp_register_t") \*p\_callback)
:   mcp\_if\_register\_event\_callback brief description

    register event callback function

    参数:
    :   **p\_callback** – **\[in\]** function pointer [btif\_mcp\_register\_t](#structbtif__mcp__register__t)

    返回值:
    :   **N/A** –

<a id="_CPPv411mcp_if_initv"></a>

<a id="_CPPv311mcp_if_initv"></a> <a id="_CPPv211mcp_if_initv"></a> <a id="mcp_if_init__void"></a> <a id="mcp__if_8h_1a315f0e38865fc10ca036c13e47abbbb7"></a> void mcp\_if\_init(void)
:   Media Control Profile interface initialize.

    返回值:
    :   **N/A** –

<a id="_CPPv421mcp_if_send_cp_opcode8uint16_t18mcp_if_cp_opcode_t"></a>

<a id="_CPPv321mcp_if_send_cp_opcode8uint16_t18mcp_if_cp_opcode_t"></a> <a id="_CPPv221mcp_if_send_cp_opcode8uint16_t18mcp_if_cp_opcode_t"></a> <a id="mcp_if_send_cp_opcode__uint16_t.mcp_if_cp_opcode_t"></a> <a id="mcp__if_8h_1ae390bfefbb7d2e67880375969260f06b"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") mcp\_if\_send\_cp\_opcode(uint16\_t handle, [mcp\_if\_cp\_opcode\_t](btif_type.md#_CPPv418mcp_if_cp_opcode_t "mcp_if_cp_opcode_t") opcode)
:   Media Control Profile interface initialize.

    参数:
    :   - **handle** – **\[in\]** gatt attribute handle
        - **opcode** – **\[in\]** media play operate code example(play music,PREVIOUS\_SEGMENT…)@mcp\_if\_cp\_opcode\_t

    返回值:
    :   **status** –

<a id="structures"></a>

### Structures

<a id="_CPPv419btif_mcp_register_t"></a>

<a id="_CPPv319btif_mcp_register_t"></a> <a id="_CPPv219btif_mcp_register_t"></a> <a id="btif_mcp_register_t"></a> <a id="structbtif__mcp__register__t"></a> struct btif\_mcp\_register\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19btif_mcp_register_t9dlst_nodeE"></a>

    <a id="_CPPv3N19btif_mcp_register_t9dlst_nodeE"></a> <a id="_CPPv2N19btif_mcp_register_t9dlst_nodeE"></a> <a id="btif_mcp_register_t::dlst_node__dl_list_t"></a> <a id="structbtif__mcp__register__t_1a1a6acfd32d0382af8facfe2f28d6f0e3"></a> dl\_list\_t dlst\_node
    :   Hang to \_mcp\_if\_event\_list link list

    <a id="_CPPv4N19btif_mcp_register_t8callbackE"></a>

    <a id="_CPPv3N19btif_mcp_register_t8callbackE"></a> <a id="_CPPv2N19btif_mcp_register_t8callbackE"></a> <a id="btif_mcp_register_t::callback__btif_mcp_event_callback"></a> <a id="structbtif__mcp__register__t_1ac45039351cfe98672da66f9553f7a9fe"></a> [btif\_mcp\_event\_callback](btif_type.md#_CPPv423btif_mcp_event_callback "btif_mcp_event_callback") callback
    :   Option callback called on media event received

<a id="_CPPv420mcp_if_general_evt_t"></a>

<a id="_CPPv320mcp_if_general_evt_t"></a> <a id="_CPPv220mcp_if_general_evt_t"></a> <a id="mcp_if_general_evt_t"></a> <a id="structmcp__if__general__evt__t"></a> struct mcp\_if\_general\_evt\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20mcp_if_general_evt_t5eventE"></a>

    <a id="_CPPv3N20mcp_if_general_evt_t5eventE"></a> <a id="_CPPv2N20mcp_if_general_evt_t5eventE"></a> <a id="mcp_if_general_evt_t::event__mcp_if_cb_event_t"></a> <a id="structmcp__if__general__evt__t_1a2217596cf709b9df09eed5c03aa04de7"></a> [mcp\_if\_cb\_event\_t](#_CPPv417mcp_if_cb_event_t "mcp_if_cb_event_t") event
    :   media interface callback event code,@mcp\_if\_cb\_event\_t

    <a id="_CPPv4N20mcp_if_general_evt_t6statusE"></a>

    <a id="_CPPv3N20mcp_if_general_evt_t6statusE"></a> <a id="_CPPv2N20mcp_if_general_evt_t6statusE"></a> <a id="mcp_if_general_evt_t::status__uint8_t"></a> <a id="structmcp__if__general__evt__t_1ac6279aacfd0cd72fd629726ad2572f4c"></a> uint8\_t status
    :   media interface callback status

<a id="_CPPv424mcp_if_media_state_evt_t"></a>

<a id="_CPPv324mcp_if_media_state_evt_t"></a> <a id="_CPPv224mcp_if_media_state_evt_t"></a> <a id="mcp_if_media_state_evt_t"></a> <a id="structmcp__if__media__state__evt__t"></a> struct mcp\_if\_media\_state\_evt\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N24mcp_if_media_state_evt_t5eventE"></a>

    <a id="_CPPv3N24mcp_if_media_state_evt_t5eventE"></a> <a id="_CPPv2N24mcp_if_media_state_evt_t5eventE"></a> <a id="mcp_if_media_state_evt_t::event__mcp_if_cb_event_t"></a> <a id="structmcp__if__media__state__evt__t_1abd5dbeee3c20c28de7698ddb9dc68308"></a> [mcp\_if\_cb\_event\_t](#_CPPv417mcp_if_cb_event_t "mcp_if_cb_event_t") event
    :   media interface callback event code,@mcp\_if\_cb\_event\_t

    <a id="_CPPv4N24mcp_if_media_state_evt_t6statusE"></a>

    <a id="_CPPv3N24mcp_if_media_state_evt_t6statusE"></a> <a id="_CPPv2N24mcp_if_media_state_evt_t6statusE"></a> <a id="mcp_if_media_state_evt_t::status__uint8_t"></a> <a id="structmcp__if__media__state__evt__t_1a8effc93e56b7d0eeebafad97a39abb93"></a> uint8\_t status
    :   media interface callback status

    <a id="_CPPv4N24mcp_if_media_state_evt_t5stateE"></a>

    <a id="_CPPv3N24mcp_if_media_state_evt_t5stateE"></a> <a id="_CPPv2N24mcp_if_media_state_evt_t5stateE"></a> <a id="mcp_if_media_state_evt_t::state__uint8_t"></a> <a id="structmcp__if__media__state__evt__t_1a9ece5dbc7da7727e9f0adcf6d34a27c6"></a> uint8\_t state
    :   media interface callback MEDIA state ,when event code is EVENT\_MEDIA\_STATE

<a id="_CPPv418mcp_if_speed_evt_t"></a>

<a id="_CPPv318mcp_if_speed_evt_t"></a> <a id="_CPPv218mcp_if_speed_evt_t"></a> <a id="mcp_if_speed_evt_t"></a> <a id="structmcp__if__speed__evt__t"></a> struct mcp\_if\_speed\_evt\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18mcp_if_speed_evt_t5eventE"></a>

    <a id="_CPPv3N18mcp_if_speed_evt_t5eventE"></a> <a id="_CPPv2N18mcp_if_speed_evt_t5eventE"></a> <a id="mcp_if_speed_evt_t::event__mcp_if_cb_event_t"></a> <a id="structmcp__if__speed__evt__t_1a82aeed464de38f3c0602106cb3899a30"></a> [mcp\_if\_cb\_event\_t](#_CPPv417mcp_if_cb_event_t "mcp_if_cb_event_t") event
    :   media interface callback event code for MCP\_CB\_EVENT\_PLAY\_SPEED,MCP\_CB\_EVENT\_SEEK\_SPEED only

    <a id="_CPPv4N18mcp_if_speed_evt_t6statusE"></a>

    <a id="_CPPv3N18mcp_if_speed_evt_t6statusE"></a> <a id="_CPPv2N18mcp_if_speed_evt_t6statusE"></a> <a id="mcp_if_speed_evt_t::status__uint8_t"></a> <a id="structmcp__if__speed__evt__t_1af0f5cd12edf7a1d44bbfd8c849a11f55"></a> uint8\_t status
    :   media interface callback status

    <a id="_CPPv4N18mcp_if_speed_evt_t5speedE"></a>

    <a id="_CPPv3N18mcp_if_speed_evt_t5speedE"></a> <a id="_CPPv2N18mcp_if_speed_evt_t5speedE"></a> <a id="mcp_if_speed_evt_t::speed__uint8_t"></a> <a id="structmcp__if__speed__evt__t_1a9321163f2a155886757f95e329b6ec41"></a> uint8\_t speed
    :   MCP\_CB\_EVENT\_PLAY\_SPEED,MCP\_CB\_EVENT\_SEEK\_SPEED speed value

<a id="_CPPv423mcp_if_play_order_evt_t"></a>

<a id="_CPPv323mcp_if_play_order_evt_t"></a> <a id="_CPPv223mcp_if_play_order_evt_t"></a> <a id="mcp_if_play_order_evt_t"></a> <a id="structmcp__if__play__order__evt__t"></a> struct mcp\_if\_play\_order\_evt\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N23mcp_if_play_order_evt_t5eventE"></a>

    <a id="_CPPv3N23mcp_if_play_order_evt_t5eventE"></a> <a id="_CPPv2N23mcp_if_play_order_evt_t5eventE"></a> <a id="mcp_if_play_order_evt_t::event__mcp_if_cb_event_t"></a> <a id="structmcp__if__play__order__evt__t_1a3d074e950a3b533054743c1c52735304"></a> [mcp\_if\_cb\_event\_t](#_CPPv417mcp_if_cb_event_t "mcp_if_cb_event_t") event
    :   media interface callback event code for MCP\_CB\_EVENT\_PLAY\_ORDER only

    <a id="_CPPv4N23mcp_if_play_order_evt_t6statusE"></a>

    <a id="_CPPv3N23mcp_if_play_order_evt_t6statusE"></a> <a id="_CPPv2N23mcp_if_play_order_evt_t6statusE"></a> <a id="mcp_if_play_order_evt_t::status__uint8_t"></a> <a id="structmcp__if__play__order__evt__t_1a292574e8fa253cd59a3048aeeca3290c"></a> uint8\_t status
    :   media interface callback status

    <a id="_CPPv4N23mcp_if_play_order_evt_t5orderE"></a>

    <a id="_CPPv3N23mcp_if_play_order_evt_t5orderE"></a> <a id="_CPPv2N23mcp_if_play_order_evt_t5orderE"></a> <a id="mcp_if_play_order_evt_t::order__uint8_t"></a> <a id="structmcp__if__play__order__evt__t_1ababac1b4d6b225d1ac7804efc8218a76"></a> uint8\_t order
    :   media interface callback play order

<a id="_CPPv428mcp_if_play_supp_order_evt_t"></a>

<a id="_CPPv328mcp_if_play_supp_order_evt_t"></a> <a id="_CPPv228mcp_if_play_supp_order_evt_t"></a> <a id="mcp_if_play_supp_order_evt_t"></a> <a id="structmcp__if__play__supp__order__evt__t"></a> struct mcp\_if\_play\_supp\_order\_evt\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N28mcp_if_play_supp_order_evt_t5eventE"></a>

    <a id="_CPPv3N28mcp_if_play_supp_order_evt_t5eventE"></a> <a id="_CPPv2N28mcp_if_play_supp_order_evt_t5eventE"></a> <a id="mcp_if_play_supp_order_evt_t::event__mcp_if_cb_event_t"></a> <a id="structmcp__if__play__supp__order__evt__t_1a6d4a67f9b893ae4c473238cc93e0bb5b"></a> [mcp\_if\_cb\_event\_t](#_CPPv417mcp_if_cb_event_t "mcp_if_cb_event_t") event
    :   media interface callback event code for MCP\_CB\_EVENT\_PLAY\_SUPP\_ORDER only

    <a id="_CPPv4N28mcp_if_play_supp_order_evt_t6statusE"></a>

    <a id="_CPPv3N28mcp_if_play_supp_order_evt_t6statusE"></a> <a id="_CPPv2N28mcp_if_play_supp_order_evt_t6statusE"></a> <a id="mcp_if_play_supp_order_evt_t::status__uint8_t"></a> <a id="structmcp__if__play__supp__order__evt__t_1a5343d8082f9e52bdef1032a29c395df4"></a> uint8\_t status
    :   media interface callback status

    <a id="_CPPv4N28mcp_if_play_supp_order_evt_t10supp_orderE"></a>

    <a id="_CPPv3N28mcp_if_play_supp_order_evt_t10supp_orderE"></a> <a id="_CPPv2N28mcp_if_play_supp_order_evt_t10supp_orderE"></a> <a id="mcp_if_play_supp_order_evt_t::supp_order__uint16_t"></a> <a id="structmcp__if__play__supp__order__evt__t_1a69d8bfc7054ee064679af1bd6d6824ef"></a> uint16\_t supp\_order
    :   media interface callback support play order

<a id="macros"></a>

### Macros

<a id="c.MCP_IF_CB_EVENT_CONNECTED"></a>

<a id="mcp__if_8h_1affcac05d314939ccd605823db474dc6b"></a> MCP\_IF\_CB\_EVENT\_CONNECTED

<a id="c.MCP_IF_CB_EVENT_DISCONNECTED"></a>

<a id="mcp__if_8h_1afc6e4521d2f6477b2ff2aac292c2cb60"></a> MCP\_IF\_CB\_EVENT\_DISCONNECTED

<a id="c.MCP_IF_CB_EVENT_DISCOVER_DONE"></a>

<a id="mcp__if_8h_1ab22078fb566c428861602c9bc38238da"></a> MCP\_IF\_CB\_EVENT\_DISCOVER\_DONE

<a id="c.MCP_IF_CB_EVENT_PLAY_SPEED"></a>

<a id="mcp__if_8h_1af5627f1f2d50b44a9f0140d65d32ec7a"></a> MCP\_IF\_CB\_EVENT\_PLAY\_SPEED

<a id="c.MCP_IF_CB_EVENT_SEEK_SPEED"></a>

<a id="mcp__if_8h_1a3e97cb1d4fa6bef4640472691f832b18"></a> MCP\_IF\_CB\_EVENT\_SEEK\_SPEED

<a id="c.MCP_IF_CB_EVENT_PLAY_ORDER"></a>

<a id="mcp__if_8h_1a4cc67c315270aec6cb986f0688aa1837"></a> MCP\_IF\_CB\_EVENT\_PLAY\_ORDER

<a id="c.MCP_IF_CB_EVENT_PLAY_SUPP_ORDER"></a>

<a id="mcp__if_8h_1ad4575739a1736c0c5079110f73de2219"></a> MCP\_IF\_CB\_EVENT\_PLAY\_SUPP\_ORDER

<a id="c.MCP_IF_CB_EVENT_MEDIA_STATE"></a>

<a id="mcp__if_8h_1a51cba683e63e8420f2fb99a21a1a5d0c"></a> MCP\_IF\_CB\_EVENT\_MEDIA\_STATE

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv417mcp_if_cb_event_t"></a>

<a id="_CPPv317mcp_if_cb_event_t"></a> <a id="_CPPv217mcp_if_cb_event_t"></a> <a id="mcp_if_cb_event_t"></a> <a id="mcp__if_8h_1a4903b6fd7406b2f9d3b01cebef07ace3"></a> typedef uint8\_t mcp\_if\_cb\_event\_t
