---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/tws/tws_bt_if.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="tws-bluetooth-interface-functions"></a>

# TWS Bluetooth Interface Functions

<a id="tws-bt-if-api-brief"></a>

## TWS\_BT\_IF API Brief

| Application | Brief |
| --- | --- |
| [`tws_bt_if_hci_event_handler()`](#_CPPv427tws_bt_if_hci_event_handlerP7uint8_t8uint16_t "tws_bt_if_hci_event_handler") | TWS HCI event handler |
| [`tws_bt_if_hfp_event_handler()`](#_CPPv427tws_bt_if_hfp_event_handlerP7uint8_t8uint16_t "tws_bt_if_hfp_event_handler") | TWS HFP event handler |
| [`tws_bt_if_avrcp_event_handle()`](#_CPPv428tws_bt_if_avrcp_event_handlePKv8uint16_t "tws_bt_if_avrcp_event_handle") | TWS AVRCP event handler |
| [`tws_bt_if_a2dp_event_handle()`](#_CPPv427tws_bt_if_a2dp_event_handlePKv8uint16_t "tws_bt_if_a2dp_event_handle") | TWS A2DP event handler |
| [`tws_bt_if_register_subfsm_callback()`](#_CPPv434tws_bt_if_register_subfsm_callback26tws_bt_if_sub_fsm_callback "tws_bt_if_register_subfsm_callback") | Register TWS sub FSM callback function |
| [`tws_bt_if_connect_req_callback()`](#_CPPv430tws_bt_if_connect_req_callbackPv "tws_bt_if_connect_req_callback") | TWS connection request callback |
| [`tws_bt_if_spp_event_handle()`](#_CPPv426tws_bt_if_spp_event_handleP7uint8_t8uint16_t "tws_bt_if_spp_event_handle") | TWS SPP event handler |
| [`tws_bt_if_rx_host_evt()`](#_CPPv421tws_bt_if_rx_host_evtP7uint8_t8uint16_t "tws_bt_if_rx_host_evt") | TWS RX host event handler |
| [`tws_bt_if_trigger_fsm()`](#_CPPv421tws_bt_if_trigger_fsmv "tws_bt_if_trigger_fsm") | trigger tws ui re-run fsm |

<a id="tws-bt-if-api-reference"></a>

## TWS\_BT\_IF API Reference

<a id="header-file"></a>

### Header File

- [tws/tws\_ux/inc/tws\_bt\_if.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/tws/tws_ux/inc/tws_bt_if.h)

<a id="functions"></a>

### Functions

<a id="_CPPv427tws_bt_if_hci_event_handlerP7uint8_t8uint16_t"></a>

<a id="_CPPv327tws_bt_if_hci_event_handlerP7uint8_t8uint16_t"></a> <a id="_CPPv227tws_bt_if_hci_event_handlerP7uint8_t8uint16_t"></a> <a id="tws_bt_if_hci_event_handler__uint8_tP.uint16_t"></a> <a id="tws__bt__if_8h_1ad41d5b2dbb5f7cb466f90d30cd931fd7"></a> void tws\_bt\_if\_hci\_event\_handler(uint8\_t \*p\_data, uint16\_t length)
:   TWS HCI event handler.

    Handle TWS HCI events in the BT task.

    参数:
    :   - **p\_data** – **\[in\]** HCI event data pointer
        - **length** – **\[in\]** HCI event data length

    返回:
    :   N/A

<a id="_CPPv427tws_bt_if_hfp_event_handlerP7uint8_t8uint16_t"></a>

<a id="_CPPv327tws_bt_if_hfp_event_handlerP7uint8_t8uint16_t"></a> <a id="_CPPv227tws_bt_if_hfp_event_handlerP7uint8_t8uint16_t"></a> <a id="tws_bt_if_hfp_event_handler__uint8_tP.uint16_t"></a> <a id="tws__bt__if_8h_1a88eec74c6adf53efa7b5915af642d409"></a> void tws\_bt\_if\_hfp\_event\_handler(uint8\_t \*p\_data, uint16\_t size)
:   TWS HFP event handler.

    Handle TWS HFP events in the BT task.

    参数:
    :   - **p\_data** – **\[in\]** HFP event data pointer
        - **length** – **\[in\]** HFP event data length

    返回:
    :   N/A

<a id="_CPPv428tws_bt_if_avrcp_event_handlePKv8uint16_t"></a>

<a id="_CPPv328tws_bt_if_avrcp_event_handlePKv8uint16_t"></a> <a id="_CPPv228tws_bt_if_avrcp_event_handlePKv8uint16_t"></a> <a id="tws_bt_if_avrcp_event_handle__voidCP.uint16_t"></a> <a id="tws__bt__if_8h_1a56e8fa5680266cade05148ff3070980a"></a> void tws\_bt\_if\_avrcp\_event\_handle(const void \*p\_cb\_param, uint16\_t length)
:   TWS AVRCP event handler.

    Handle TWS AVRCP events in the BT task.

    参数:
    :   - **p\_cb\_param** – **\[in\]** AVRCP event parameter pointer
        - **length** – **\[in\]** AVRCP event parameter length

    返回:
    :   N/A

<a id="_CPPv427tws_bt_if_a2dp_event_handlePKv8uint16_t"></a>

<a id="_CPPv327tws_bt_if_a2dp_event_handlePKv8uint16_t"></a> <a id="_CPPv227tws_bt_if_a2dp_event_handlePKv8uint16_t"></a> <a id="tws_bt_if_a2dp_event_handle__voidCP.uint16_t"></a> <a id="tws__bt__if_8h_1aa02222daaaf16b94c82d57464702ad8f"></a> void tws\_bt\_if\_a2dp\_event\_handle(const void \*p\_cb\_param, uint16\_t length)
:   TWS A2DP event handler.

    Handle TWS A2DP events in the BT task.

    参数:
    :   - **p\_cb\_param** – **\[in\]** A2DP event parameter pointer
        - **length** – **\[in\]** A2DP event parameter length

    返回:
    :   N/A

<a id="_CPPv434tws_bt_if_register_subfsm_callback26tws_bt_if_sub_fsm_callback"></a>

<a id="_CPPv334tws_bt_if_register_subfsm_callback26tws_bt_if_sub_fsm_callback"></a> <a id="_CPPv234tws_bt_if_register_subfsm_callback26tws_bt_if_sub_fsm_callback"></a> <a id="tws_bt_if_register_subfsm_callback__tws_bt_if_sub_fsm_callback"></a> <a id="tws__bt__if_8h_1afe8183adff6d95160d7272b12861e54b"></a> void tws\_bt\_if\_register\_subfsm\_callback([tws\_bt\_if\_sub\_fsm\_callback](#_CPPv426tws_bt_if_sub_fsm_callback "tws_bt_if_sub_fsm_callback") callback)
:   Register TWS sub FSM callback function.

    Register the TWS sub FSM callback function running in the BT task.

    参数:
    :   **callback** – **\[in\]** TWS sub FSM callback function.

    返回:
    :   N/A

<a id="_CPPv430tws_bt_if_connect_req_callbackPv"></a>

<a id="_CPPv330tws_bt_if_connect_req_callbackPv"></a> <a id="_CPPv230tws_bt_if_connect_req_callbackPv"></a> <a id="tws_bt_if_connect_req_callback__voidP"></a> <a id="tws__bt__if_8h_1ae7459a517c3b5523ea50a3e5d1b1dca4"></a> uint8\_t tws\_bt\_if\_connect\_req\_callback(void \*p\_addr)
:   TWS connection request callback.

    TWS connection request callback running in the BT task.

    参数:
    :   **p\_addr** – **\[in\]** The address pointer of the connection requesting device.

    返回值:
    :   - **0** – success \[BTIF\_EXIT\_SUCCESS\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426tws_bt_if_spp_event_handleP7uint8_t8uint16_t"></a>

<a id="_CPPv326tws_bt_if_spp_event_handleP7uint8_t8uint16_t"></a> <a id="_CPPv226tws_bt_if_spp_event_handleP7uint8_t8uint16_t"></a> <a id="tws_bt_if_spp_event_handle__uint8_tP.uint16_t"></a> <a id="tws__bt__if_8h_1a0f1fc03b28e8d77658c1693e28a63ec0"></a> void tws\_bt\_if\_spp\_event\_handle(uint8\_t \*p\_data, uint16\_t size)
:   TWS SPP event handler.

    Handle TWS SPP events in the BT task.

    参数:
    :   - **p\_data** – **\[in\]** SPP event data pointer
        - **size** – **\[in\]** SPP event data size

    返回:
    :   N/A

<a id="_CPPv421tws_bt_if_rx_host_evtP7uint8_t8uint16_t"></a>

<a id="_CPPv321tws_bt_if_rx_host_evtP7uint8_t8uint16_t"></a> <a id="_CPPv221tws_bt_if_rx_host_evtP7uint8_t8uint16_t"></a> <a id="tws_bt_if_rx_host_evt__uint8_tP.uint16_t"></a> <a id="tws__bt__if_8h_1ac0fadece76de563fcb73cd327eb9d4c9"></a> void tws\_bt\_if\_rx\_host\_evt(uint8\_t \*p\_data, uint16\_t length)
:   TWS RX host event handler.

    Handle TWS RX host events in the TWS task.

    参数:
    :   - **p\_data** – **\[in\]** RX host event data pointer
        - **length** – **\[in\]** RX host event data length

    返回:
    :   N/A

<a id="_CPPv421tws_bt_if_trigger_fsmv"></a>

<a id="_CPPv321tws_bt_if_trigger_fsmv"></a> <a id="_CPPv221tws_bt_if_trigger_fsmv"></a> <a id="tws_bt_if_trigger_fsm__void"></a> <a id="tws__bt__if_8h_1a1c7bde6c1f54222b1e1226f6486e76c7"></a> void tws\_bt\_if\_trigger\_fsm(void)
:   trigger tws ui re-run fsm.

    send one re-run message to tws task.

    参数:
    :   **N/A** – **\[in\]**

    返回:
    :   N/A **TWS\_BT\_IF\_H** EOF

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv426tws_bt_if_sub_fsm_callback"></a>

<a id="_CPPv326tws_bt_if_sub_fsm_callback"></a> <a id="_CPPv226tws_bt_if_sub_fsm_callback"></a> <a id="tws_bt_if_sub_fsm_callback"></a> <a id="tws__bt__if_8h_1af6f6605a958571d9e99d2da24fe4ad94"></a> typedef void (\*tws\_bt\_if\_sub\_fsm\_callback)([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr, uint8\_t action, uint8\_t status, void \*p\_para)
:   Define the callback function pointer for the TWS sub finite state machine (FSM).
