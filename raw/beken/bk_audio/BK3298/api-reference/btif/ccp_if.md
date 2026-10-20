---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/btif/ccp_if.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="ccp-interface-functions"></a>

# CCP Interface Functions

<a id="ccp-if-api-brief"></a>

## CCP\_IF API Brief

| Application | Brief |
| --- | --- |
| [`ccp_if_register_event_callback()`](#_CPPv430ccp_if_register_event_callbackP19btif_ccp_register_t "ccp_if_register_event_callback") | Register CCP event callback |
| [`ccp_if_init()`](#_CPPv411ccp_if_initv "ccp_if_init") | Initialize Call Control Profile |
| [`ccp_if_send_cp_opcode()`](#_CPPv421ccp_if_send_cp_opcode8uint16_t18ccp_if_cp_opcode_t7uint8_tP7uint8_t7uint8_t "ccp_if_send_cp_opcode") | Send CCP control point opcode |

<a id="ccp-if-api-reference"></a>

## CCP\_IF API Reference

<a id="header-file"></a>

### Header File

- [btif/inc/ccp\_if.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/btif/inc/ccp_if.h)

<a id="functions"></a>

### Functions

<a id="_CPPv430ccp_if_register_event_callbackP19btif_ccp_register_t"></a>

<a id="_CPPv330ccp_if_register_event_callbackP19btif_ccp_register_t"></a> <a id="_CPPv230ccp_if_register_event_callbackP19btif_ccp_register_t"></a> <a id="ccp_if_register_event_callback__btif_ccp_register_tP"></a> <a id="ccp__if_8h_1af256c0cb1f0bfec4a3513ec90df9eaf6"></a> void ccp\_if\_register\_event\_callback([btif\_ccp\_register\_t](#_CPPv419btif_ccp_register_t "btif_ccp_register_t") \*p\_callback)
:   Register CCP event callback.

    Register callback \[p\_callback\] to the CCP events callback list.

    参数:
    :   **p\_callback** – **\[in\]** pointer to a CCP event callback of type [btif\_ccp\_register\_t](#structbtif__ccp__register__t).

    返回:
    :   N/A

<a id="_CPPv411ccp_if_initv"></a>

<a id="_CPPv311ccp_if_initv"></a> <a id="_CPPv211ccp_if_initv"></a> <a id="ccp_if_init__void"></a> <a id="ccp__if_8h_1a56ad9a091b1f5b3aee11b89888cc337e"></a> void ccp\_if\_init(void)
:   Initialize Call Control Profile.

    Install the CCP event callback handler to the BLE host to enable CCP client functionality.

    返回:
    :   N/A

<a id="_CPPv421ccp_if_send_cp_opcode8uint16_t18ccp_if_cp_opcode_t7uint8_tP7uint8_t7uint8_t"></a>

<a id="_CPPv321ccp_if_send_cp_opcode8uint16_t18ccp_if_cp_opcode_t7uint8_tP7uint8_t7uint8_t"></a> <a id="_CPPv221ccp_if_send_cp_opcode8uint16_t18ccp_if_cp_opcode_t7uint8_tP7uint8_t7uint8_t"></a> <a id="ccp_if_send_cp_opcode__uint16_t.ccp_if_cp_opcode_t.uint8_t.uint8_tP.uint8_t"></a> <a id="ccp__if_8h_1a13646c5b4af93d485b4baebc3ed347c8"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") ccp\_if\_send\_cp\_opcode(uint16\_t handle, [ccp\_if\_cp\_opcode\_t](btif_type.md#_CPPv418ccp_if_cp_opcode_t "ccp_if_cp_opcode_t") opcode, uint8\_t idx, uint8\_t \*p\_uri, uint8\_t uri\_len)
:   Send CCP control point opcode.

    Write the opcode \[opcode\] to the call control point of the mobile phone with connection handle \[handle\].

    参数:
    :   - **handle** – **\[in\]** CCP connection handle
        - **opcode** – **\[in\]** call control point opcode of type ccp\_if\_cp\_opcode\_t
        - **idx** – **\[in\]** call index of the incoming call.
        - **p\_uri** – **\[in\]** pointer to a Uniform Resource Identifier(URI)
        - **uri\_len** – **\[in\]** length of a Uniform Resource Identifier(URI)

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail BK\_TBS\_CLIENT **CCP\_IF\_H** EOF

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv419btif_ccp_register_t"></a>

<a id="_CPPv319btif_ccp_register_t"></a> <a id="_CPPv219btif_ccp_register_t"></a> <a id="btif_ccp_register_t"></a> <a id="structbtif__ccp__register__t"></a> struct btif\_ccp\_register\_t
:   CCP register event callback structure definition.

<a id="_CPPv420ccp_if_general_evt_t"></a>

<a id="_CPPv320ccp_if_general_evt_t"></a> <a id="_CPPv220ccp_if_general_evt_t"></a> <a id="ccp_if_general_evt_t"></a> <a id="structccp__if__general__evt__t"></a> struct ccp\_if\_general\_evt\_t
:   CCP general event structure definition.

<a id="_CPPv430ccp_if_general_short_val_evt_t"></a>

<a id="_CPPv330ccp_if_general_short_val_evt_t"></a> <a id="_CPPv230ccp_if_general_short_val_evt_t"></a> <a id="ccp_if_general_short_val_evt_t"></a> <a id="structccp__if__general__short__val__evt__t"></a> struct ccp\_if\_general\_short\_val\_evt\_t
:   CCP general event by short value structure definition.

<a id="_CPPv429ccp_if_general_long_val_evt_t"></a>

<a id="_CPPv329ccp_if_general_long_val_evt_t"></a> <a id="_CPPv229ccp_if_general_long_val_evt_t"></a> <a id="ccp_if_general_long_val_evt_t"></a> <a id="structccp__if__general__long__val__evt__t"></a> struct ccp\_if\_general\_long\_val\_evt\_t
:   CCP general event by long value structure definition.

<a id="_CPPv425ccp_if_general_call_evt_t"></a>

<a id="_CPPv325ccp_if_general_call_evt_t"></a> <a id="_CPPv225ccp_if_general_call_evt_t"></a> <a id="ccp_if_general_call_evt_t"></a> <a id="structccp__if__general__call__evt__t"></a> struct ccp\_if\_general\_call\_evt\_t
:   CCP general call event structure definition.

<a id="macros"></a>

### Macros

<a id="c.CCP_IF_CB_EVENT_CONNECTED"></a>

<a id="ccp__if_8h_1a3301bd88903d312e88568ac96cbb41a5"></a> CCP\_IF\_CB\_EVENT\_CONNECTED

<a id="c.CCP_IF_CB_EVENT_DISCONNECTED"></a>

<a id="ccp__if_8h_1abdd8ed1843a5a6df9f9a0e73cadfb9d1"></a> CCP\_IF\_CB\_EVENT\_DISCONNECTED

<a id="c.CCP_IF_CB_EVENT_DISCOVER_DONE"></a>

<a id="ccp__if_8h_1a2e90af535f67ec291a9349a53929324e"></a> CCP\_IF\_CB\_EVENT\_DISCOVER\_DONE

<a id="c.CCP_IF_CB_EVENT_TECHNO"></a>

<a id="ccp__if_8h_1a31aefb46e891b6dde92d027df5923abc"></a> CCP\_IF\_CB\_EVENT\_TECHNO

<a id="c.CCP_IF_CB_EVENT_SIGN_STRENGTH"></a>

<a id="ccp__if_8h_1a90d1709de43895186be36841b6b3c804"></a> CCP\_IF\_CB\_EVENT\_SIGN\_STRENGTH

<a id="c.CCP_IF_CB_EVENT_SIGN_STRENGTH_INTV"></a>

<a id="ccp__if_8h_1aca3244398d4a49e5f6477e70de0cdece"></a> CCP\_IF\_CB\_EVENT\_SIGN\_STRENGTH\_INTV

<a id="c.CCP_IF_CB_EVENT_CALL_TERM"></a>

<a id="ccp__if_8h_1a3e5e356fa00db80a61f6ae790171064a"></a> CCP\_IF\_CB\_EVENT\_CALL\_TERM

<a id="c.CCP_IF_CB_EVENT_PROV_NAME"></a>

<a id="ccp__if_8h_1aa47e5a2597bbe09874463f1d320dd8fd"></a> CCP\_IF\_CB\_EVENT\_PROV\_NAME

<a id="c.CCP_IF_CB_EVENT_UCI"></a>

<a id="ccp__if_8h_1a71b6e63c7eb0282c0b5060eae1d26716"></a> CCP\_IF\_CB\_EVENT\_UCI

<a id="c.CCP_IF_CB_EVENT_INCOMING_CALL"></a>

<a id="ccp__if_8h_1a6c4e839ec35d6b52221b3c87222c16cf"></a> CCP\_IF\_CB\_EVENT\_INCOMING\_CALL

<a id="c.CCP_IF_CB_EVENT_FREE_ALL_CALL_INFO"></a>

<a id="ccp__if_8h_1af5ab7343bfc85319dca7390ca6e27321"></a> CCP\_IF\_CB\_EVENT\_FREE\_ALL\_CALL\_INFO

<a id="c.CCP_IF_CB_EVENT_CALL_STATE"></a>

<a id="ccp__if_8h_1a9a4f77ce1fdf899d1704598949e727c0"></a> CCP\_IF\_CB\_EVENT\_CALL\_STATE

<a id="c.CCP_IF_CB_EVENT_CURR_CALL_LIST"></a>

<a id="ccp__if_8h_1a891851ae3b1d071b0fe0969fe45eb371"></a> CCP\_IF\_CB\_EVENT\_CURR\_CALL\_LIST

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv417ccp_if_cb_event_t"></a>

<a id="_CPPv317ccp_if_cb_event_t"></a> <a id="_CPPv217ccp_if_cb_event_t"></a> <a id="ccp_if_cb_event_t"></a> <a id="ccp__if_8h_1a78021bf56b6c7f6afc34d92736f2e0df"></a> typedef uint8\_t ccp\_if\_cb\_event\_t
:   Call Control Profile(CCP) callback event type definition.
