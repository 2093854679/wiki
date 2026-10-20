---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/btif/l2cap_if.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="l2cap-interface-functions"></a>

# L2CAP Interface Functions

<a id="l2cap-if-api-brief"></a>

## L2CAP\_IF API Brief

| Application | Brief |
| --- | --- |
| [`l2cap_if_tws_channel_init()`](#_CPPv425l2cap_if_tws_channel_initP15tws_l2cap_env_t "l2cap_if_tws_channel_init") | TWS private channel init function |
| [`l2cap_if_tws_cmd_send()`](#_CPPv421l2cap_if_tws_cmd_sendPv8uint16_t8uint16_t "l2cap_if_tws_cmd_send") | TWS private cmd send API |
| [`l2cap_if_tws_create_connection()`](#_CPPv430l2cap_if_tws_create_connection14btif_bd_addr_t "l2cap_if_tws_create_connection") | TWS private connection link connect API |
| [`l2cap_if_pending_chan_run()`](#_CPPv425l2cap_if_pending_chan_run8uint16_t "l2cap_if_pending_chan_run") | l2cap pending channel restore run API |
| [`l2cap_if_get_base_cid()`](#_CPPv421l2cap_if_get_base_cid14btif_bd_addr_tP8uint16_t "l2cap_if_get_base_cid") | Get L2CAP base CID by address |

<a id="l2cap-if-api-reference"></a>

## L2CAP\_IF API Reference

<a id="header-file"></a>

### Header File

- [btif/inc/l2cap\_if.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/btif/inc/l2cap_if.h)

<a id="functions"></a>

### Functions

<a id="_CPPv425l2cap_if_tws_channel_initP15tws_l2cap_env_t"></a>

<a id="_CPPv325l2cap_if_tws_channel_initP15tws_l2cap_env_t"></a> <a id="_CPPv225l2cap_if_tws_channel_initP15tws_l2cap_env_t"></a> <a id="l2cap_if_tws_channel_init__tws_l2cap_env_tP"></a> <a id="l2cap__if_8h_1a6c208242657ad74535fcef25dae6a71d"></a> void l2cap\_if\_tws\_channel\_init([tws\_l2cap\_env\_t](#_CPPv415tws_l2cap_env_t "tws_l2cap_env_t") \*p\_tws\_l2cap\_init)
:   l2cap\_if\_tws\_channel\_init brief description

    TWS private channel init function

    参数:
    :   **p\_tws\_l2cap\_init** – **\[in\]**

    返回:
    :   N/A

<a id="_CPPv421l2cap_if_tws_cmd_sendPv8uint16_t8uint16_t"></a>

<a id="_CPPv321l2cap_if_tws_cmd_sendPv8uint16_t8uint16_t"></a> <a id="_CPPv221l2cap_if_tws_cmd_sendPv8uint16_t8uint16_t"></a> <a id="l2cap_if_tws_cmd_send__voidP.uint16_t.uint16_t"></a> <a id="l2cap__if_8h_1ab95c2557efdc833738ad5e6b336cce9c"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") l2cap\_if\_tws\_cmd\_send(void \*p\_data, uint16\_t length, uint16\_t cmd\_seq)
:   l2cap\_if\_tws\_cmd\_send brief description

    TWS private cmd send API

    参数:
    :   - **p\_data** – **\[in\]** data buffer will be sent
        - **length** – **\[in\]** p\_data length
        - **cmd\_seq** – **\[in\]** commnad sequenece

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv430l2cap_if_tws_create_connection14btif_bd_addr_t"></a>

<a id="_CPPv330l2cap_if_tws_create_connection14btif_bd_addr_t"></a> <a id="_CPPv230l2cap_if_tws_create_connection14btif_bd_addr_t"></a> <a id="l2cap_if_tws_create_connection__btif_bd_addr_t"></a> <a id="l2cap__if_8h_1a4082b08fde9c15498513b4837b5026df"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") l2cap\_if\_tws\_create\_connection([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr)
:   l2cap\_if\_tws\_create\_connection brief description

    TWS private connection link connect API

    参数:
    :   **addr** – **\[in\]** remote BT MAC address

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425l2cap_if_pending_chan_run8uint16_t"></a>

<a id="_CPPv325l2cap_if_pending_chan_run8uint16_t"></a> <a id="_CPPv225l2cap_if_pending_chan_run8uint16_t"></a> <a id="l2cap_if_pending_chan_run__uint16_t"></a> <a id="l2cap__if_8h_1a39aa5c8755bd73a46276bf1551394178"></a> void l2cap\_if\_pending\_chan\_run(uint16\_t handle)
:   l2cap\_if\_pending\_chan\_run brief description

    l2cap pending channel restore run API

    参数:
    :   **handle** – **\[in\]** acl\_handle

    返回:
    :   N/A

<a id="_CPPv421l2cap_if_get_base_cid14btif_bd_addr_tP8uint16_t"></a>

<a id="_CPPv321l2cap_if_get_base_cid14btif_bd_addr_tP8uint16_t"></a> <a id="_CPPv221l2cap_if_get_base_cid14btif_bd_addr_tP8uint16_t"></a> <a id="l2cap_if_get_base_cid__btif_bd_addr_t.uint16_tP"></a> <a id="l2cap__if_8h_1a1b140e19e3d91ba91ef4aed7cb17ea53"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") l2cap\_if\_get\_base\_cid([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr, uint16\_t \*p\_base\_cid)
:   l2cap\_if\_get\_base\_cid brief description

    Get L2CAP base CID by address

    参数:
    :   - **addr** – **\[in\]** remote BT MAC address
        - **p\_base\_cid** – **\[out\]** base CID value

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv415tws_l2cap_env_t"></a>

<a id="_CPPv315tws_l2cap_env_t"></a> <a id="_CPPv215tws_l2cap_env_t"></a> <a id="tws_l2cap_env_t"></a> <a id="structtws__l2cap__env__t"></a> struct tws\_l2cap\_env\_t
:   TWS private channel L2CAP environment struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N15tws_l2cap_env_t13data_callbackE"></a>

    <a id="_CPPv3N15tws_l2cap_env_t13data_callbackE"></a> <a id="_CPPv2N15tws_l2cap_env_t13data_callbackE"></a> <a id="tws_l2cap_env_t::data_callback__l2cap_tws_data_handle"></a> <a id="structtws__l2cap__env__t_1aede3a4c3aba510e140e0097d079480d7"></a> [l2cap\_tws\_data\_handle](#_CPPv421l2cap_tws_data_handle "l2cap_tws_data_handle") data\_callback
    :   TWS private channel data callback struct

    <a id="_CPPv4N15tws_l2cap_env_t14event_callbackE"></a>

    <a id="_CPPv3N15tws_l2cap_env_t14event_callbackE"></a> <a id="_CPPv2N15tws_l2cap_env_t14event_callbackE"></a> <a id="tws_l2cap_env_t::event_callback__l2cap_tws_event_handle"></a> <a id="structtws__l2cap__env__t_1ab8c07949a4103a1a5a3cac421a09592b"></a> [l2cap\_tws\_event\_handle](#_CPPv422l2cap_tws_event_handle "l2cap_tws_event_handle") event\_callback
    :   TWS private channel event callback struct

    <a id="_CPPv4N15tws_l2cap_env_t4addrE"></a>

    <a id="_CPPv3N15tws_l2cap_env_t4addrE"></a> <a id="_CPPv2N15tws_l2cap_env_t4addrE"></a> <a id="tws_l2cap_env_t::addr__btif_bd_addr_t"></a> <a id="structtws__l2cap__env__t_1a6e9c7e07109978378ee0079eef39f1e3"></a> [btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr
    :   remote BT MAC address

    <a id="_CPPv4N15tws_l2cap_env_t6handleE"></a>

    <a id="_CPPv3N15tws_l2cap_env_t6handleE"></a> <a id="_CPPv2N15tws_l2cap_env_t6handleE"></a> <a id="tws_l2cap_env_t::handle__uint16_t"></a> <a id="structtws__l2cap__env__t_1a680e3b08266a3e278b2668877fc759a9"></a> uint16\_t handle
    :   connection handle

    <a id="_CPPv4N15tws_l2cap_env_t5stateE"></a>

    <a id="_CPPv3N15tws_l2cap_env_t5stateE"></a> <a id="_CPPv2N15tws_l2cap_env_t5stateE"></a> <a id="tws_l2cap_env_t::state__tws_l2cap_state_t"></a> <a id="structtws__l2cap__env__t_1af34ce9ed64225bffc00eb69993145462"></a> [tws\_l2cap\_state\_t](#_CPPv417tws_l2cap_state_t "tws_l2cap_state_t") state
    :   TWS private channel connection state

<a id="_CPPv419l2cap_if_cb_param_t"></a>

<a id="_CPPv319l2cap_if_cb_param_t"></a> <a id="_CPPv219l2cap_if_cb_param_t"></a> <a id="l2cap_if_cb_param_t"></a> <a id="structl2cap__if__cb__param__t"></a> struct l2cap\_if\_cb\_param\_t
:   TWS private channel L2CAP callback interface data struct definition.

<a id="macros"></a>

### Macros

<a id="c.BTIF_L2CAP_CONN_REQ"></a>

<a id="l2cap__if_8h_1a604c6976df5c046f46662c117ceb72b6"></a> BTIF\_L2CAP\_CONN\_REQ

<a id="c.BTIF_L2CACP_LOCAL_OPEN"></a>

<a id="l2cap__if_8h_1abbf9326138035d3bee0700cc22b1de2e"></a> BTIF\_L2CACP\_LOCAL\_OPEN

<a id="c.BTIF_L2CAP_REMOTE_OPEN"></a>

<a id="l2cap__if_8h_1a14b97f04520b405876dd584f100d7f17"></a> BTIF\_L2CAP\_REMOTE\_OPEN

<a id="c.BTIF_L2CAP_TX_DONE"></a>

<a id="l2cap__if_8h_1ae4e9426eec1a4c96a6ff5896d6bbb2bd"></a> BTIF\_L2CAP\_TX\_DONE

<a id="c.BTIF_L2CAP_CLOSED"></a>

<a id="l2cap__if_8h_1adf1231fb67cc6a1f82cdb6448eb6fc5d"></a> BTIF\_L2CAP\_CLOSED

<a id="c.L2CAP_TWS_CID"></a>

<a id="l2cap__if_8h_1ab7305a647c152b25ccaa6cb345456fba"></a> L2CAP\_TWS\_CID

<a id="c.L2CAP_TWS_CONNECTED"></a>

<a id="l2cap__if_8h_1abe668e52638cbdb905f3187235757cc4"></a> L2CAP\_TWS\_CONNECTED

<a id="c.L2CAP_TWS_DISCONNECTED"></a>

<a id="l2cap__if_8h_1a15e71f80fd95f3caabe4ab65ae9c6d5a"></a> L2CAP\_TWS\_DISCONNECTED

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv421l2cap_tws_data_handle"></a>

<a id="_CPPv321l2cap_tws_data_handle"></a> <a id="_CPPv221l2cap_tws_data_handle"></a> <a id="l2cap_tws_data_handle"></a> <a id="l2cap__if_8h_1aadf08e722d4fde302afd22b464abe56a"></a> typedef void (\*l2cap\_tws\_data\_handle)(uint8\_t \*p\_data, uint16\_t length)

<a id="_CPPv422l2cap_tws_event_handle"></a>

<a id="_CPPv322l2cap_tws_event_handle"></a> <a id="_CPPv222l2cap_tws_event_handle"></a> <a id="l2cap_tws_event_handle"></a> <a id="l2cap__if_8h_1a640ff598f6253f285c3b565cf76040be"></a> typedef void (\*l2cap\_tws\_event\_handle)(uint8\_t event)

<a id="_CPPv417tws_l2cap_state_t"></a>

<a id="_CPPv317tws_l2cap_state_t"></a> <a id="_CPPv217tws_l2cap_state_t"></a> <a id="tws_l2cap_state_t"></a> <a id="l2cap__if_8h_1a3aad76049f73563a4d9dcd0d0d37c1af"></a> typedef uint8\_t tws\_l2cap\_state\_t
:   TWS private channel L2CAP state definition.
