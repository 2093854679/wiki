---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/tws/tws_fsm_ctrl.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="tws-fsm-control-functions"></a>

# TWS FSM Control Functions

<a id="tws-fsm-ctrl-api-brief"></a>

## TWS\_FSM\_CTRL API Brief

| Application | Brief |
| --- | --- |
| [`tws_fsm_task_handle()`](#_CPPv419tws_fsm_task_handlePv8uint16_t "tws_fsm_task_handle") | handle TWS FAM task |
| [`tws_event_ext_isr_handle()`](#_CPPv424tws_event_ext_isr_handle13ext_operate_t "tws_event_ext_isr_handle") | handle TWS external operation events |
| [`tws_event_send_share_info()`](#_CPPv425tws_event_send_share_info15tws_info_type_t13ext_operate_t "tws_event_send_share_info") | send TWS shared information |
| [`tws_event_share_info_handle()`](#_CPPv427tws_event_share_info_handlePK7uint8_t8uint16_t "tws_event_share_info_handle") | handle TWS shared information |
| [`tws_update_saved_mobile_info()`](#_CPPv428tws_update_saved_mobile_infov "tws_update_saved_mobile_info") | update saved mobile information |
| [`tws_fsm_set_phone_connect_active()`](#_CPPv432tws_fsm_set_phone_connect_activeP14btif_bd_addr_t "tws_fsm_set_phone_connect_active") | activate phone connection event |
| [`tws_send_FSM_gen_msg()`](#_CPPv420tws_send_FSM_gen_msg13fsm_gen_msg_t "tws_send_FSM_gen_msg") | send FSM generate message |
| [`tws_fsm_ctrl_get_evt_env()`](#_CPPv424tws_fsm_ctrl_get_evt_envv "tws_fsm_ctrl_get_evt_env") | get TWS environment parameters |
| [`tws_fsm_get_pending_operate()`](#_CPPv427tws_fsm_get_pending_operatev "tws_fsm_get_pending_operate") | get FSM pending external operations |
| [`tws_get_mobile_info()`](#_CPPv419tws_get_mobile_infoPP11addr_info_t "tws_get_mobile_info") | get mobile information |
| [`tws_fsm_set_mobile_info_merged_active()`](#_CPPv437tws_fsm_set_mobile_info_merged_activev "tws_fsm_set_mobile_info_merged_active") | activate mobile information merged event |
| [`tws_fsm_ctrl_reconnect_tws()`](#_CPPv426tws_fsm_ctrl_reconnect_twsv "tws_fsm_ctrl_reconnect_tws") | reconnect tws |
| [`tws_fsm_ctrl_clear_operate()`](#_CPPv426tws_fsm_ctrl_clear_operate13ext_operate_t "tws_fsm_ctrl_clear_operate") | clear external operation |
| [`tws_fsm_set_link_loss_active()`](#_CPPv428tws_fsm_set_link_loss_activev "tws_fsm_set_link_loss_active") | activate tws link loss event |
| [`tws_fsm_del_local_env_addr()`](#_CPPv426tws_fsm_del_local_env_addrP14btif_bd_addr_t "tws_fsm_del_local_env_addr") | delete local address |
| [`tws_fsm_ctrl_get_tws_bat_level()`](#_CPPv430tws_fsm_ctrl_get_tws_bat_levelv "tws_fsm_ctrl_get_tws_bat_level") | get battery level |
| [`tws_fsm_master_req_connect_handle()`](#_CPPv433tws_fsm_master_req_connect_handlePK7uint8_t8uint16_t "tws_fsm_master_req_connect_handle") | right request left to run connect fsm |
| [`tws_fsm_ctrl_set_operate()`](#_CPPv424tws_fsm_ctrl_set_operate13ext_operate_t "tws_fsm_ctrl_set_operate") | enable tws operate |

<a id="tws-fsm-ctrl-api-reference"></a>

## TWS\_FSM\_CTRL API Reference

<a id="header-file"></a>

### Header File

- [tws/tws\_ux/inc/tws\_fsm\_ctrl.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/tws/tws_ux/inc/tws_fsm_ctrl.h)

<a id="functions"></a>

### Functions

<a id="_CPPv419tws_fsm_task_handlePv8uint16_t"></a>

<a id="_CPPv319tws_fsm_task_handlePv8uint16_t"></a> <a id="_CPPv219tws_fsm_task_handlePv8uint16_t"></a> <a id="tws_fsm_task_handle__voidP.uint16_t"></a> <a id="tws__fsm__ctrl_8h_1a3783f97a3731495fc30380bab5ee48e3"></a> void tws\_fsm\_task\_handle(void \*p\_data, uint16\_t length)
:   handle TWS FAM task

    run in tws task to generate one new FSM

    参数:
    :   - **p\_data** – **\[in\]** pointer to FSM generate message data
        - **length** – **\[in\]** length of FSM generate message data

    返回:
    :   N/A

<a id="_CPPv424tws_event_ext_isr_handle13ext_operate_t"></a>

<a id="_CPPv324tws_event_ext_isr_handle13ext_operate_t"></a> <a id="_CPPv224tws_event_ext_isr_handle13ext_operate_t"></a> <a id="tws_event_ext_isr_handle__ext_operate_t"></a> <a id="tws__fsm__ctrl_8h_1aecc91aaf9febefce96619acdeb963d46"></a> void tws\_event\_ext\_isr\_handle([ext\_operate\_t](#_CPPv413ext_operate_t "ext_operate_t") ext\_operate)
:   handle TWS external operation events

    external ISR handler

    参数:
    :   **ext\_operate** – **\[in\]** external operation of type ext\_operate\_t

    返回:
    :   N/A

<a id="_CPPv425tws_event_send_share_info15tws_info_type_t13ext_operate_t"></a>

<a id="_CPPv325tws_event_send_share_info15tws_info_type_t13ext_operate_t"></a> <a id="_CPPv225tws_event_send_share_info15tws_info_type_t13ext_operate_t"></a> <a id="tws_event_send_share_info__tws_info_type_t.ext_operate_t"></a> <a id="tws__fsm__ctrl_8h_1a266d4abc6601f0f6035d04a6f5173130"></a> void tws\_event\_send\_share\_info([tws\_info\_type\_t](#_CPPv415tws_info_type_t "tws_info_type_t") info\_type, [ext\_operate\_t](#_CPPv413ext_operate_t "ext_operate_t") ext\_operate)
:   send TWS shared information

    notify local earbuds info to peer

    参数:
    :   - **info\_type** – **\[in\]** information type of type tws\_info\_type\_t
        - **ext\_operate** – **\[in\]** external operation of type ext\_operate\_t

    返回:
    :   N/A

<a id="_CPPv427tws_event_share_info_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv327tws_event_share_info_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv227tws_event_share_info_handlePK7uint8_t8uint16_t"></a> <a id="tws_event_share_info_handle__uint8_tCP.uint16_t"></a> <a id="tws__fsm__ctrl_8h_1a9a54f4c72b41447c0a9da62bfd536744"></a> void tws\_event\_share\_info\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   handle TWS shared information

    peer earbus info handler

    参数:
    :   - **p\_data** – **\[in\]** pointer to TWS information data
        - **length** – **\[in\]** length of TWS information data

    返回:
    :   N/A

<a id="_CPPv428tws_update_saved_mobile_infov"></a>

<a id="_CPPv328tws_update_saved_mobile_infov"></a> <a id="_CPPv228tws_update_saved_mobile_infov"></a> <a id="tws_update_saved_mobile_info__void"></a> <a id="tws__fsm__ctrl_8h_1a1fc9cb08e74d4a141e5f2ab939a65156"></a> void tws\_update\_saved\_mobile\_info(void)
:   update saved mobile information

    update saved mobile info when link connect

    返回:
    :   N/A

<a id="_CPPv432tws_fsm_set_phone_connect_activeP14btif_bd_addr_t"></a>

<a id="_CPPv332tws_fsm_set_phone_connect_activeP14btif_bd_addr_t"></a> <a id="_CPPv232tws_fsm_set_phone_connect_activeP14btif_bd_addr_t"></a> <a id="tws_fsm_set_phone_connect_active__btif_bd_addr_tP"></a> <a id="tws__fsm__ctrl_8h_1ab2329bc554444bbb5e06eeedfb34223d"></a> [btif\_ret\_t](../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") tws\_fsm\_set\_phone\_connect\_active([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   activate phone connection event

    activates the connection to the phone with the address p\_addr.

    参数:
    :   **p\_addr** – **\[in\]** pointer to a phone address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t) to be connected.

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420tws_send_FSM_gen_msg13fsm_gen_msg_t"></a>

<a id="_CPPv320tws_send_FSM_gen_msg13fsm_gen_msg_t"></a> <a id="_CPPv220tws_send_FSM_gen_msg13fsm_gen_msg_t"></a> <a id="tws_send_FSM_gen_msg__fsm_gen_msg_t"></a> <a id="tws__fsm__ctrl_8h_1a2cc50ef4327ef90a2b52725a6e722d60"></a> void tws\_send\_FSM\_gen\_msg([fsm\_gen\_msg\_t](#_CPPv413fsm_gen_msg_t "fsm_gen_msg_t") fsm\_gen\_msg)
:   send FSM generate message

    trigger tws thread to generate a new mainfsm is exist

    参数:
    :   **fsm\_gen\_msg** – **\[in\]** FSM generate message

    返回:
    :   N/A

<a id="_CPPv424tws_fsm_ctrl_get_evt_envv"></a>

<a id="_CPPv324tws_fsm_ctrl_get_evt_envv"></a> <a id="_CPPv224tws_fsm_ctrl_get_evt_envv"></a> <a id="tws_fsm_ctrl_get_evt_env__void"></a> <a id="tws__fsm__ctrl_8h_1a1e2a3501dd47f598a2e1af863e1043b7"></a> [tws\_evt\_env\_t](#_CPPv413tws_evt_env_t "tws_evt_env_t") \*tws\_fsm\_ctrl\_get\_evt\_env(void)
:   get TWS environment parameters

    get TWS environment parameters

    返回:
    :   The pointer of [tws\_evt\_env\_t](#structtws__evt__env__t)

<a id="_CPPv427tws_fsm_get_pending_operatev"></a>

<a id="_CPPv327tws_fsm_get_pending_operatev"></a> <a id="_CPPv227tws_fsm_get_pending_operatev"></a> <a id="tws_fsm_get_pending_operate__void"></a> <a id="tws__fsm__ctrl_8h_1af629ece671bcf626c10b2f214c02e52b"></a> [ext\_operate\_t](#_CPPv413ext_operate_t "ext_operate_t") tws\_fsm\_get\_pending\_operate(void)
:   get FSM pending external operations

    get FSM pending external operations

    返回:
    :   external operation of type ext\_operate\_t

<a id="_CPPv419tws_get_mobile_infoPP11addr_info_t"></a>

<a id="_CPPv319tws_get_mobile_infoPP11addr_info_t"></a> <a id="_CPPv219tws_get_mobile_infoPP11addr_info_t"></a> <a id="tws_get_mobile_info__addr_info_tPP"></a> <a id="tws__fsm__ctrl_8h_1a0e0a79aae816490f117345e99dd654a8"></a> uint8\_t tws\_get\_mobile\_info([addr\_info\_t](#_CPPv411addr_info_t "addr_info_t") \*\*p\_mobile\_info)
:   get mobile information

    provides p\_mobile\_info type pointer for get the mobile information pointer.

    参数:
    :   **p\_mobile\_info** – **\[in\]** pointer to a [addr\_info\_t](#structaddr__info__t) type pointer.

    返回:
    :   mobile number

<a id="_CPPv437tws_fsm_set_mobile_info_merged_activev"></a>

<a id="_CPPv337tws_fsm_set_mobile_info_merged_activev"></a> <a id="_CPPv237tws_fsm_set_mobile_info_merged_activev"></a> <a id="tws_fsm_set_mobile_info_merged_active__void"></a> <a id="tws__fsm__ctrl_8h_1a9ee6c95c786f56fdf75251b52f6fabee"></a> void tws\_fsm\_set\_mobile\_info\_merged\_active(void)
:   activate mobile information merged event

    trigger mobile info merged event when tws connected

    返回:
    :   N/A

<a id="_CPPv426tws_fsm_ctrl_reconnect_twsv"></a>

<a id="_CPPv326tws_fsm_ctrl_reconnect_twsv"></a> <a id="_CPPv226tws_fsm_ctrl_reconnect_twsv"></a> <a id="tws_fsm_ctrl_reconnect_tws__void"></a> <a id="tws__fsm__ctrl_8h_1a3376aecbe09ff1e6e3440502b8d053d3"></a> void tws\_fsm\_ctrl\_reconnect\_tws(void)
:   reconnect tws

    trigger fsm ctrl module to start reconnect tws

    返回:
    :   N/A

<a id="_CPPv426tws_fsm_ctrl_clear_operate13ext_operate_t"></a>

<a id="_CPPv326tws_fsm_ctrl_clear_operate13ext_operate_t"></a> <a id="_CPPv226tws_fsm_ctrl_clear_operate13ext_operate_t"></a> <a id="tws_fsm_ctrl_clear_operate__ext_operate_t"></a> <a id="tws__fsm__ctrl_8h_1a6e339c45c72ec5a87a1e2a4c4e636523"></a> void tws\_fsm\_ctrl\_clear\_operate([ext\_operate\_t](#_CPPv413ext_operate_t "ext_operate_t") operate)
:   clear external operation

    clear operate

    参数:
    :   **operate** – **\[in\]** external operation of type ext\_operate\_t

    返回:
    :   N/A

<a id="_CPPv428tws_fsm_set_link_loss_activev"></a>

<a id="_CPPv328tws_fsm_set_link_loss_activev"></a> <a id="_CPPv228tws_fsm_set_link_loss_activev"></a> <a id="tws_fsm_set_link_loss_active__void"></a> <a id="tws__fsm__ctrl_8h_1a6f9d2bdbc11acfe47120582af4332a2d"></a> void tws\_fsm\_set\_link\_loss\_active(void)
:   activate tws link loss event

    activate tws link loss event

    返回:
    :   N/A

<a id="_CPPv426tws_fsm_del_local_env_addrP14btif_bd_addr_t"></a>

<a id="_CPPv326tws_fsm_del_local_env_addrP14btif_bd_addr_t"></a> <a id="_CPPv226tws_fsm_del_local_env_addrP14btif_bd_addr_t"></a> <a id="tws_fsm_del_local_env_addr__btif_bd_addr_tP"></a> <a id="tws__fsm__ctrl_8h_1a5da039ca22b722010d91fa5cd7068aa8"></a> void tws\_fsm\_del\_local\_env\_addr([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   delete local address

    delete the local address in the environment parameters

    参数:
    :   **p\_addr** – **\[in\]** pointer to an address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t).

    返回:
    :   N/A

<a id="_CPPv430tws_fsm_ctrl_get_tws_bat_levelv"></a>

<a id="_CPPv330tws_fsm_ctrl_get_tws_bat_levelv"></a> <a id="_CPPv230tws_fsm_ctrl_get_tws_bat_levelv"></a> <a id="tws_fsm_ctrl_get_tws_bat_level__void"></a> <a id="tws__fsm__ctrl_8h_1a9340d1919120ea8d2bd1611785852455"></a> uint8\_t tws\_fsm\_ctrl\_get\_tws\_bat\_level(void)
:   get battery level

    get the battery level in the environment parameters

    返回:
    :   battery level

<a id="_CPPv433tws_fsm_master_req_connect_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv333tws_fsm_master_req_connect_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv233tws_fsm_master_req_connect_handlePK7uint8_t8uint16_t"></a> <a id="tws_fsm_master_req_connect_handle__uint8_tCP.uint16_t"></a> <a id="tws__fsm__ctrl_8h_1ad3b33d14702355dfa106a112fb4f4b41"></a> void tws\_fsm\_master\_req\_connect\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   right request left to run connect fsm

    right request left to run connect fsm, due to phone cancel pairing

    返回:
    :   NA

<a id="_CPPv424tws_fsm_ctrl_set_operate13ext_operate_t"></a>

<a id="_CPPv324tws_fsm_ctrl_set_operate13ext_operate_t"></a> <a id="_CPPv224tws_fsm_ctrl_set_operate13ext_operate_t"></a> <a id="tws_fsm_ctrl_set_operate__ext_operate_t"></a> <a id="tws__fsm__ctrl_8h_1afd6ce38308029164f31d114438de9120"></a> void tws\_fsm\_ctrl\_set\_operate([ext\_operate\_t](#_CPPv413ext_operate_t "ext_operate_t") operate)
:   enable tws operate

    enable tws operate bitmap

    返回:
    :   NA **TWS\_EVENT\_CTRL\_H** EOF

<a id="structures"></a>

### Structures

<a id="_CPPv411addr_info_t"></a>

<a id="_CPPv311addr_info_t"></a> <a id="_CPPv211addr_info_t"></a> <a id="addr_info_t"></a> <a id="structaddr__info__t"></a> struct addr\_info\_t
:   Address information structure definition.

<a id="_CPPv413tws_evt_env_t"></a>

<a id="_CPPv313tws_evt_env_t"></a> <a id="_CPPv213tws_evt_env_t"></a> <a id="tws_evt_env_t"></a> <a id="structtws__evt__env__t"></a> struct tws\_evt\_env\_t
:   TWS event environment parameters structure definition.

<a id="_CPPv410tws_info_t"></a>

<a id="_CPPv310tws_info_t"></a> <a id="_CPPv210tws_info_t"></a> <a id="tws_info_t"></a> <a id="structtws__info__t"></a> struct tws\_info\_t
:   TWS information structure definition.

<a id="_CPPv421tws_master_req_conn_t"></a>

<a id="_CPPv321tws_master_req_conn_t"></a> <a id="_CPPv221tws_master_req_conn_t"></a> <a id="tws_master_req_conn_t"></a> <a id="structtws__master__req__conn__t"></a> struct tws\_master\_req\_conn\_t
:   TWS master request connect structure definition.

<a id="_CPPv413fsm_gen_msg_t"></a>

<a id="_CPPv313fsm_gen_msg_t"></a> <a id="_CPPv213fsm_gen_msg_t"></a> <a id="fsm_gen_msg_t"></a> <a id="structfsm__gen__msg__t"></a> struct fsm\_gen\_msg\_t
:   FSM generation event message structure definition.

<a id="macros"></a>

### Macros

<a id="c.OPERATE_IDLE"></a>

<a id="tws__fsm__ctrl_8h_1ae856a3aafcf5cd5ee679dfdd5d9e6829"></a> OPERATE\_IDLE
:   0x01

<a id="c.OPERATE_OPEN_BOX"></a>

<a id="tws__fsm__ctrl_8h_1afe81ed361d30e82589865feb3172d807"></a> OPERATE\_OPEN\_BOX
:   0x02

<a id="c.OPERATE_FETCH_OUT"></a>

<a id="tws__fsm__ctrl_8h_1a921e07115df6afb4dd105b2f404baec4"></a> OPERATE\_FETCH\_OUT
:   0x04

<a id="c.OPERATE_WEAR_UP"></a>

<a id="tws__fsm__ctrl_8h_1aad43cd3bd9bc3e7d8d4c6f9983b98593"></a> OPERATE\_WEAR\_UP
:   0x08

<a id="c.OPERATE_WEAR_DOWN"></a>

<a id="tws__fsm__ctrl_8h_1a644f94d90da55200f90284078d07988c"></a> OPERATE\_WEAR\_DOWN
:   0x10

<a id="c.OPERATE_PUT_IN"></a>

<a id="tws__fsm__ctrl_8h_1abcb65ef62dd8c80e315260dc8b9d4ba1"></a> OPERATE\_PUT\_IN
:   0x20

<a id="c.OPERATE_CLOSE_BOX"></a>

<a id="tws__fsm__ctrl_8h_1a46ef315986dd3f633726948eeb2b7fd1"></a> OPERATE\_CLOSE\_BOX
:   0x40

<a id="c.OPERATE_LINK_LOSS"></a>

<a id="tws__fsm__ctrl_8h_1ade26e7db83f06d31b542cc27dd85dbfd"></a> OPERATE\_LINK\_LOSS
:   0x80

<a id="c.OPERATE_ENTER_PAIRING"></a>

<a id="tws__fsm__ctrl_8h_1ac9e7ead21d3936eeb5d7606b9493777d"></a> OPERATE\_ENTER\_PAIRING
:   0x100

<a id="c.OPERATE_PHONE_CONNECT"></a>

<a id="tws__fsm__ctrl_8h_1afa706e8cc05ff2b4a563ab3f148dd096"></a> OPERATE\_PHONE\_CONNECT
:   0x200

<a id="c.OPERATE_TWS_CONNECT"></a>

<a id="tws__fsm__ctrl_8h_1a7e9b5c376e5f4b5130c07ab9d0441d63"></a> OPERATE\_TWS\_CONNECT
:   0x400

<a id="c.OPERATE_MOBILE_INFO_MERGED"></a>

<a id="tws__fsm__ctrl_8h_1a85eb95ea0d1e56c4dd8fcbed7227a157"></a> OPERATE\_MOBILE\_INFO\_MERGED
:   0x800

<a id="c.OPERATE_MASTER_REQ_CONNECT"></a>

<a id="tws__fsm__ctrl_8h_1a481ae89b0630bf1bf1c77e00f047e3bd"></a> OPERATE\_MASTER\_REQ\_CONNECT
:   0x1000

<a id="c.OPERATE_TWS_SYNC_BITMAP"></a>

<a id="tws__fsm__ctrl_8h_1a844326f66ae1aef1f6be0346e192ec89"></a> OPERATE\_TWS\_SYNC\_BITMAP

<a id="c.OPERATE_PEER_OPEN_BOX"></a>

<a id="tws__fsm__ctrl_8h_1acac2a3acb97968dd3da2d35e25ff8f12"></a> OPERATE\_PEER\_OPEN\_BOX
:   0x10000

<a id="c.OPERATE_PEER_FETCH_OUT"></a>

<a id="tws__fsm__ctrl_8h_1a1ff0a3de2062a73135c3ea50e1050874"></a> OPERATE\_PEER\_FETCH\_OUT
:   0x20000

<a id="c.OPERATE_PEER_WEAR_UP"></a>

<a id="tws__fsm__ctrl_8h_1a8507578b53a98eefbb913f4d98d3867d"></a> OPERATE\_PEER\_WEAR\_UP
:   0x40000

<a id="c.OPERATE_PEER_WEAR_DOWN"></a>

<a id="tws__fsm__ctrl_8h_1af49ce32756b0ad990670a9b84b616b61"></a> OPERATE\_PEER\_WEAR\_DOWN
:   0x80000

<a id="c.OPERATE_PEER_PUT_IN"></a>

<a id="tws__fsm__ctrl_8h_1ad0d5a1c2a0090380b16bf51bff745595"></a> OPERATE\_PEER\_PUT\_IN
:   0x100000

<a id="c.OPERATE_PEER_CLOSE_BOX"></a>

<a id="tws__fsm__ctrl_8h_1aad558b8efbe8d216c085d5700b324aa3"></a> OPERATE\_PEER\_CLOSE\_BOX
:   0x200000

<a id="c.OPERATE_PEER_BITMAP"></a>

<a id="tws__fsm__ctrl_8h_1ad66851ac86c2559036a81fb4943b8a0a"></a> OPERATE\_PEER\_BITMAP

<a id="c.IS_CONNECT_EXT_ISR"></a>

<a id="tws__fsm__ctrl_8h_1a829f1691c0f3909553bbabf7a66bb28e"></a> IS\_CONNECT\_EXT\_ISR(isr)
:   Macro for check if isr includes operations that requires a TWS connection.

<a id="c.IS_CLOSE_BOX_OPERATE"></a>

<a id="tws__fsm__ctrl_8h_1a3d461b03067038ea4dce8929977d95b0"></a> IS\_CLOSE\_BOX\_OPERATE(opt)
:   Macro for check if opt includes the close box operations.

<a id="c.CLEAR_CLOSE_BOX_OPERATE"></a>

<a id="tws__fsm__ctrl_8h_1a6f371e17c232f66006d2135d5f4c290e"></a> CLEAR\_CLOSE\_BOX\_OPERATE(opt)
:   Macro for clear the close box operation from opt.

<a id="c.CLEAR_PUT_IN_OPERATE"></a>

<a id="tws__fsm__ctrl_8h_1a237574965fb2975331aec8a12a97fe4a"></a> CLEAR\_PUT\_IN\_OPERATE(opt)
:   Macro for clear the put in operation from opt.

<a id="c.CLEAR_WEAR_DOWN_OPERATE"></a>

<a id="tws__fsm__ctrl_8h_1ae365b8f091e0876f47beb35005e7435a"></a> CLEAR\_WEAR\_DOWN\_OPERATE(opt)
:   Macro for clear the wear down operation from opt.

<a id="c.CLEAR_OPEN_BOX_OPERATE"></a>

<a id="tws__fsm__ctrl_8h_1ab0f7bfffcddd633282e990ccd44a9a1e"></a> CLEAR\_OPEN\_BOX\_OPERATE(opt)
:   Macro for clear the open box operation from opt.

<a id="c.CLEAR_FETCH_OUT_OPERATE"></a>

<a id="tws__fsm__ctrl_8h_1a2fcf4500d8be20658e62513aed57f76e"></a> CLEAR\_FETCH\_OUT\_OPERATE(opt)
:   Macro for clear the fetch out operation from opt.

<a id="c.CLEAR_WEAR_UP_OPERATE"></a>

<a id="tws__fsm__ctrl_8h_1a0f9a71dc35f207137b156c6e0f9fb414"></a> CLEAR\_WEAR\_UP\_OPERATE(opt)
:   Macro for clear the wear up operation from opt.

<a id="c.STATE_UNKNOWN"></a>

<a id="tws__fsm__ctrl_8h_1a3a671c5b5d9122f1158555575bc0feb1"></a> STATE\_UNKNOWN

<a id="c.STATE_IN_BOX_CLOSED"></a>

<a id="tws__fsm__ctrl_8h_1a5daeb056602b9ef5c6dc5af8515e203c"></a> STATE\_IN\_BOX\_CLOSED

<a id="c.STATE_IN_BOX_OPEN"></a>

<a id="tws__fsm__ctrl_8h_1a77cef3374a65ebb11cc43cacba677e00"></a> STATE\_IN\_BOX\_OPEN

<a id="c.STATE_OUT_OF_BOX"></a>

<a id="tws__fsm__ctrl_8h_1ad5bfe6e34186f91de83f2b45ef98b190"></a> STATE\_OUT\_OF\_BOX

<a id="c.STATE_OUTBOX_WEARED"></a>

<a id="tws__fsm__ctrl_8h_1a4fdeae69412c001c65b53323e979d176"></a> STATE\_OUTBOX\_WEARED

<a id="c.TWS_INFO_TYPE_UNKNOWN"></a>

<a id="tws__fsm__ctrl_8h_1a569620c7bcfbc3f086970d6ab8d69cec"></a> TWS\_INFO\_TYPE\_UNKNOWN

<a id="c.TWS_INFO_TYPE_OPERATE"></a>

<a id="tws__fsm__ctrl_8h_1a27a18bdc18623e462775ba73b9e4394b"></a> TWS\_INFO\_TYPE\_OPERATE

<a id="c.TWS_INFO_TYPE_BAT_INFO"></a>

<a id="tws__fsm__ctrl_8h_1a51c27e75edf4c8f922cb85d8e3f611bb"></a> TWS\_INFO\_TYPE\_BAT\_INFO

<a id="c.TWS_INFO_TYPE_PD_TIMER"></a>

<a id="tws__fsm__ctrl_8h_1a844019090b0c0e3b9303b900cce7e0e3"></a> TWS\_INFO\_TYPE\_PD\_TIMER

<a id="c.TWS_INFO_TYPE_PD"></a>

<a id="tws__fsm__ctrl_8h_1a0944a807ced0e59ceb8c4f59eddf8a0f"></a> TWS\_INFO\_TYPE\_PD

<a id="c.TWS_INFO_TYPE_ENTER_PAIR"></a>

<a id="tws__fsm__ctrl_8h_1a30d08ac4040feb09d2cc6f09dd47fa93"></a> TWS\_INFO\_TYPE\_ENTER\_PAIR

<a id="c.TWS_MOBILE_INFO_NO_CONNECT"></a>

<a id="tws__fsm__ctrl_8h_1a5346532ad0d2f0f935ccf2331e526a86"></a> TWS\_MOBILE\_INFO\_NO\_CONNECT

<a id="c.TWS_MOBILE_INFO_CONNECTED"></a>

<a id="tws__fsm__ctrl_8h_1a8c686f2bc613bdb9c6a53f4c040e9e44"></a> TWS\_MOBILE\_INFO\_CONNECTED

<a id="c.TWS_MOBILE_INFO_CONNECT_ONGOING"></a>

<a id="tws__fsm__ctrl_8h_1abdb261fc9f8791f1293dd55bf55318b2"></a> TWS\_MOBILE\_INFO\_CONNECT\_ONGOING

<a id="c.EXT_ISR_EVENT"></a>

<a id="tws__fsm__ctrl_8h_1a6abef97f2de51ae9b1f37473694f825e"></a> EXT\_ISR\_EVENT

<a id="c.PEER_INFO_EVENT"></a>

<a id="tws__fsm__ctrl_8h_1a948f6eaf88efde726bff80fbf2b85d2a"></a> PEER\_INFO\_EVENT

<a id="c.USER_LOGIC_EVENT"></a>

<a id="tws__fsm__ctrl_8h_1ae0cc0344b874de717a96fec007a4fbe6"></a> USER\_LOGIC\_EVENT

<a id="c.EXTCUTE_PENDING_EVENT"></a>

<a id="tws__fsm__ctrl_8h_1a7568e7321a942c80ec2d1e21ddf76606"></a> EXTCUTE\_PENDING\_EVENT

<a id="c.LINK_LOSS_EVENT"></a>

<a id="tws__fsm__ctrl_8h_1a987f8e7236c9011c1bdbd69164b53840"></a> LINK\_LOSS\_EVENT

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv413ext_operate_t"></a>

<a id="_CPPv313ext_operate_t"></a> <a id="_CPPv213ext_operate_t"></a> <a id="ext_operate_t"></a> <a id="tws__fsm__ctrl_8h_1a842541f8e64ba82fac8e28449d14ea79"></a> typedef uint32\_t ext\_operate\_t
:   External operation definition.

<a id="_CPPv415earbuds_state_t"></a>

<a id="_CPPv315earbuds_state_t"></a> <a id="_CPPv215earbuds_state_t"></a> <a id="earbuds_state_t"></a> <a id="tws__fsm__ctrl_8h_1a958169b258661ca5a6d3bf19391323e4"></a> typedef uint32\_t earbuds\_state\_t
:   Earbuds status definition.

<a id="_CPPv415tws_info_type_t"></a>

<a id="_CPPv315tws_info_type_t"></a> <a id="_CPPv215tws_info_type_t"></a> <a id="tws_info_type_t"></a> <a id="tws__fsm__ctrl_8h_1a436ef007fed0f698b7780f01bbbba2b9"></a> typedef uint8\_t tws\_info\_type\_t

<a id="_CPPv414fsm_gen_type_t"></a>

<a id="_CPPv314fsm_gen_type_t"></a> <a id="_CPPv214fsm_gen_type_t"></a> <a id="fsm_gen_type_t"></a> <a id="tws__fsm__ctrl_8h_1adb189cd439d536c18918c97c9e97513b"></a> typedef uint8\_t fsm\_gen\_type\_t
:   FSM generation event type definition.
