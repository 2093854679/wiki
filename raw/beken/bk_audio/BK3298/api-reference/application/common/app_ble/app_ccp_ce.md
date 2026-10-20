---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_ble/app_ccp_ce.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="call-control-client-application-handle-functions"></a>

# Call Control Client Application Handle Functions

<a id="app-ccp-ce-api-brief"></a>

## APP\_CCP\_CE API Brief

| Application | Brief |
| --- | --- |
| [`app_ccp_ce_init()`](#_CPPv415app_ccp_ce_initv "app_ccp_ce_init") | Initialize BLE Call Control Profile (CCP) |
| [`app_ccp_is_ccp_active()`](#_CPPv421app_ccp_is_ccp_activev "app_ccp_is_ccp_active") | BLE Call Control Profile (CCP) is active |
| [`app_ccp_get_tbs_call_state()`](#_CPPv426app_ccp_get_tbs_call_statev "app_ccp_get_tbs_call_state") | Get the call state of the Telephone Bearer Service (TBS) |
| [`app_ccp_btn_type_reg()`](#_CPPv420app_ccp_btn_type_reg23_ccp_ce_set_btn_type_cb "app_ccp_btn_type_reg") | Register Handle BLE Call Control button type callback function |
| [`app_ccp_call_control()`](#_CPPv420app_ccp_call_control7uint8_tP7uint8_t7uint8_t "app_ccp_call_control") | Perform BLE Call control operation |

<a id="app-ccp-ce-api-reference"></a>

## APP\_CCP\_CE API Reference

<a id="header-file"></a>

### Header File

- [common/app\_ble/app\_ccp\_ce.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_ble/app_ccp_ce.h)

<a id="functions"></a>

### Functions

<a id="_CPPv415app_ccp_ce_initv"></a>

<a id="_CPPv315app_ccp_ce_initv"></a> <a id="_CPPv215app_ccp_ce_initv"></a> <a id="app_ccp_ce_init__void"></a> <a id="app__ccp__ce_8h_1a8f8bff9203b639e1b6390a2c19082061"></a> void app\_ccp\_ce\_init(void)
:   Initialize BLE Call Control Profile (CCP).

    Initialize and mount the BLE Call Control Profile (CCP).

    返回:
    :   N/A

<a id="_CPPv421app_ccp_is_ccp_activev"></a>

<a id="_CPPv321app_ccp_is_ccp_activev"></a> <a id="_CPPv221app_ccp_is_ccp_activev"></a> <a id="app_ccp_is_ccp_active__void"></a> <a id="app__ccp__ce_8h_1a682296cf1e53c4003309712aef570c18"></a> uint8\_t app\_ccp\_is\_ccp\_active(void)
:   BLE Call Control Profile (CCP) is active.

    Verify if the BLE call control profile is active.

    返回值:
    :   - **true** – active
        - **false** – inactive

    返回:
    :   active status

<a id="_CPPv426app_ccp_get_tbs_call_statev"></a>

<a id="_CPPv326app_ccp_get_tbs_call_statev"></a> <a id="_CPPv226app_ccp_get_tbs_call_statev"></a> <a id="app_ccp_get_tbs_call_state__void"></a> <a id="app__ccp__ce_8h_1ab1d051c67a6488b72cc7384c8c71d605"></a> uint8\_t app\_ccp\_get\_tbs\_call\_state(void)
:   Get the call state of the Telephone Bearer Service (TBS).

    Obtain the current call status of the mobile phone.

    返回值:
    :   - **0x00** – Incoming
        - **0x01** – Dialing
        - **0x02** – Alerting
        - **0x03** – Active
        - **0x04** – Locally Held
        - **0x05** – Remotely Held
        - **0x06** – Locally and Remotely Held
        - **0xFF** – Invalid state

    返回:
    :   call state

<a id="_CPPv420app_ccp_btn_type_reg23_ccp_ce_set_btn_type_cb"></a>

<a id="_CPPv320app_ccp_btn_type_reg23_ccp_ce_set_btn_type_cb"></a> <a id="_CPPv220app_ccp_btn_type_reg23_ccp_ce_set_btn_type_cb"></a> <a id="app_ccp_btn_type_reg___ccp_ce_set_btn_type_cb"></a> <a id="app__ccp__ce_8h_1aa582614ae1d124a61135b4e794299ac2"></a> void app\_ccp\_btn\_type\_reg([\_ccp\_ce\_set\_btn\_type\_cb](#_CPPv423_ccp_ce_set_btn_type_cb "_ccp_ce_set_btn_type_cb") p\_cb)
:   Register Handle BLE Call Control button type callback function.

    Register a function to handle button events initiated by Call Control.

    参数:
    :   **p\_cb** – **\[in\]** The callback function pointer used to process BLE Call Control button types.

    返回:
    :   N/A

<a id="_CPPv420app_ccp_call_control7uint8_tP7uint8_t7uint8_t"></a>

<a id="_CPPv320app_ccp_call_control7uint8_tP7uint8_t7uint8_t"></a> <a id="_CPPv220app_ccp_call_control7uint8_tP7uint8_t7uint8_t"></a> <a id="app_ccp_call_control__uint8_t.uint8_tP.uint8_t"></a> <a id="app__ccp__ce_8h_1a23dfc0f4b65b6797edd136b4c4cee083"></a> [btif\_ret\_t](../../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") app\_ccp\_call\_control(uint8\_t opcode, uint8\_t \*p\_uri, uint8\_t uri\_len)
:   Perform BLE Call control operation.

    Manage mobile phone call behavior.

    参数:
    :   - **opcode** – **\[in\]** telephone bearer opcode 0 Accept 1 Terminate 2 Hold 3 Retrieve 4 Originate 5 Join
        - **p\_uri** – **\[in\]** URI data pointer
        - **uri\_len** – **\[in\]** URI data length

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv415app_call_info_t"></a>

<a id="_CPPv315app_call_info_t"></a> <a id="_CPPv215app_call_info_t"></a> <a id="app_call_info_t"></a> <a id="structapp__call__info__t"></a> struct app\_call\_info\_t
:   BLE Call information struct definition.

<a id="macros"></a>

### Macros

<a id="c.URI_MAX_LEN"></a>

<a id="app__ccp__ce_8h_1aa4932299f4968f1e73c4f53c715ad1f9"></a> URI\_MAX\_LEN

<a id="c.BUTTON_TYPE_LE_AUDIO_NO_CALL_ACT"></a>

<a id="app__ccp__ce_8h_1a112655ce5ca6dcec957f3294b2771e63"></a> BUTTON\_TYPE\_LE\_AUDIO\_NO\_CALL\_ACT
:   BLE Call Control button type definition.

<a id="c.BUTTON_TYPE_LE_AUDIO_CALL_ACT"></a>

<a id="app__ccp__ce_8h_1ae32e759d114d8c96eff38af6da387547"></a> BUTTON\_TYPE\_LE\_AUDIO\_CALL\_ACT

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv423_ccp_ce_set_btn_type_cb"></a>

<a id="_CPPv323_ccp_ce_set_btn_type_cb"></a> <a id="_CPPv223_ccp_ce_set_btn_type_cb"></a> <a id="_ccp_ce_set_btn_type_cb"></a> <a id="app__ccp__ce_8h_1a4dfa4bb09ad57aba517fe0e730cc9312"></a> typedef void (\*\_ccp\_ce\_set\_btn\_type\_cb)(uint64\_t type)
:   Process the BLE Call Control button type callback function pointer definition.
