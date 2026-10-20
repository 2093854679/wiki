---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/tws/tws_sub_fsm.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="tws-sub-fsm-functions"></a>

# TWS Sub FSM Functions

<a id="tws-sub-fsm-api-brief"></a>

## TWS\_SUB\_FSM API Brief

| Application | Brief |
| --- | --- |
| [`subfsm_entry()`](#_CPPv412subfsm_entry14btif_bd_addr_t13subfsm_type_t "subfsm_entry") | subfsm entry |
| [`subfsm_tws_handshake_handle()`](#_CPPv427subfsm_tws_handshake_handlePK7uint8_t8uint16_t "subfsm_tws_handshake_handle") | handle tws handshake command |
| [`subfsm_tws_handshake_rsp_handle()`](#_CPPv431subfsm_tws_handshake_rsp_handlePK7uint8_t8uint16_t "subfsm_tws_handshake_rsp_handle") | handle tws handshake command response |
| [`subfsm_tws_handshake_rsp_TO_handle()`](#_CPPv434subfsm_tws_handshake_rsp_TO_handlePK7uint8_t8uint16_t "subfsm_tws_handshake_rsp_TO_handle") | handle tws handshake command response timeout |
| [`subfsm_disc_mobile_handle()`](#_CPPv425subfsm_disc_mobile_handlePK7uint8_t8uint16_t "subfsm_disc_mobile_handle") | handle disconnect mobile phone command |
| [`subfsm_recv_master_TSS_handle()`](#_CPPv429subfsm_recv_master_TSS_handlePK7uint8_t8uint16_t "subfsm_recv_master_TSS_handle") | handle receive master TSS command |
| [`subfsm_recv_master_TSS_rsp_handle()`](#_CPPv433subfsm_recv_master_TSS_rsp_handlePK7uint8_t8uint16_t "subfsm_recv_master_TSS_rsp_handle") | handle receive master TSS command response |
| [`subfsm_recv_master_TSS_rsp_TO_handle()`](#_CPPv436subfsm_recv_master_TSS_rsp_TO_handlePK7uint8_t8uint16_t "subfsm_recv_master_TSS_rsp_TO_handle") | handle receive master TSS command response timeout |
| [`subfsm_recv_slave_TSS_handle()`](#_CPPv428subfsm_recv_slave_TSS_handlePK7uint8_t8uint16_t "subfsm_recv_slave_TSS_handle") | handle receive slave TSS command |
| [`subfsm_recv_slave_TSS_rsp_handle()`](#_CPPv432subfsm_recv_slave_TSS_rsp_handlePK7uint8_t8uint16_t "subfsm_recv_slave_TSS_rsp_handle") | handle receive slave TSS command response |
| [`subfsm_recv_slave_TSS_rsp_TO_handle()`](#_CPPv435subfsm_recv_slave_TSS_rsp_TO_handlePK7uint8_t8uint16_t "subfsm_recv_slave_TSS_rsp_TO_handle") | handle receive slave TSS command response timeout |
| [`subfsm_recv_stop_snoop_handle()`](#_CPPv429subfsm_recv_stop_snoop_handlePK7uint8_t8uint16_t "subfsm_recv_stop_snoop_handle") | handle receive stop snoop command |
| [`subfsm_initialise()`](#_CPPv417subfsm_initialisev "subfsm_initialise") | initialize sub FSM |
| [`subfsm_register_mainfsm_callback()`](#_CPPv432subfsm_register_mainfsm_callback16sub_fsm_callback "subfsm_register_mainfsm_callback") | register main FSM callback |
| [`subfsm_is_enabled()`](#_CPPv417subfsm_is_enabled13subfsm_type_t "subfsm_is_enabled") | is some fsm type is running |

<a id="tws-sub-fsm-api-reference"></a>

## TWS\_SUB\_FSM API Reference

<a id="header-file"></a>

### Header File

- [tws/tws\_ux/inc/tws\_sub\_fsm.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/tws/tws_ux/inc/tws_sub_fsm.h)

<a id="functions"></a>

### Functions

<a id="_CPPv412subfsm_entry14btif_bd_addr_t13subfsm_type_t"></a>

<a id="_CPPv312subfsm_entry14btif_bd_addr_t13subfsm_type_t"></a> <a id="_CPPv212subfsm_entry14btif_bd_addr_t13subfsm_type_t"></a> <a id="subfsm_entry__btif_bd_addr_t.subfsm_type_t"></a> <a id="tws__sub__fsm_8h_1ad190cf03f8e88322631d10d1d2ee24b0"></a> [fsm\_result\_t](#_CPPv412fsm_result_t "fsm_result_t") subfsm\_entry([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr, [subfsm\_type\_t](#_CPPv413subfsm_type_t "subfsm_type_t") type)
:   subfsm entry

    subfsm entry function used by mainfsm

    参数:
    :   - **addr** – **\[in\]** address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)
        - **type** – **\[in\]** sub FSM type of type subfsm\_type\_t

    返回值:
    :   - **0** – success \[FSM\_NO\_ERROR\]
        - **other** – fail

    返回:
    :   result of type fsm\_result\_t

<a id="_CPPv427subfsm_tws_handshake_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv327subfsm_tws_handshake_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv227subfsm_tws_handshake_handlePK7uint8_t8uint16_t"></a> <a id="subfsm_tws_handshake_handle__uint8_tCP.uint16_t"></a> <a id="tws__sub__fsm_8h_1a96bcc30b74090d3944cfa30e8b056ad6"></a> void subfsm\_tws\_handshake\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   handle tws handshake command

    handshake cmd handler

    参数:
    :   - **p\_data** – **\[in\]** pointer to command data
        - **length** – **\[in\]** length of command data

    返回:
    :   N/A

<a id="_CPPv431subfsm_tws_handshake_rsp_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv331subfsm_tws_handshake_rsp_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv231subfsm_tws_handshake_rsp_handlePK7uint8_t8uint16_t"></a> <a id="subfsm_tws_handshake_rsp_handle__uint8_tCP.uint16_t"></a> <a id="tws__sub__fsm_8h_1a233147ddc1101351539e3e69e2028143"></a> void subfsm\_tws\_handshake\_rsp\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   handle tws handshake command response

    handshake cmd rsp handle

    参数:
    :   - **p\_data** – **\[in\]** pointer to command data
        - **length** – **\[in\]** length of command data

    返回:
    :   N/A

<a id="_CPPv434subfsm_tws_handshake_rsp_TO_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv334subfsm_tws_handshake_rsp_TO_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv234subfsm_tws_handshake_rsp_TO_handlePK7uint8_t8uint16_t"></a> <a id="subfsm_tws_handshake_rsp_TO_handle__uint8_tCP.uint16_t"></a> <a id="tws__sub__fsm_8h_1a94ff4f742aa56500edc3235ba098ff70"></a> void subfsm\_tws\_handshake\_rsp\_TO\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   handle tws handshake command response timeout

    handshake rsp timeout handle

    参数:
    :   - **p\_data** – **\[in\]** pointer to command data
        - **length** – **\[in\]** length of command data

    返回:
    :   N/A

<a id="_CPPv425subfsm_disc_mobile_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv325subfsm_disc_mobile_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv225subfsm_disc_mobile_handlePK7uint8_t8uint16_t"></a> <a id="subfsm_disc_mobile_handle__uint8_tCP.uint16_t"></a> <a id="tws__sub__fsm_8h_1a092b210471e0cfafbae77015a51a27db"></a> void subfsm\_disc\_mobile\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   handle disconnect mobile phone command

    disconnect mobile cmd handle

    参数:
    :   - **p\_data** – **\[in\]** pointer to command data
        - **length** – **\[in\]** length of command data

    返回:
    :   N/A

<a id="_CPPv429subfsm_recv_master_TSS_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv329subfsm_recv_master_TSS_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv229subfsm_recv_master_TSS_handlePK7uint8_t8uint16_t"></a> <a id="subfsm_recv_master_TSS_handle__uint8_tCP.uint16_t"></a> <a id="tws__sub__fsm_8h_1aec1e65df0e085822e44b96a2b95e4987"></a> void subfsm\_recv\_master\_TSS\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   handle receive master TSS command

    rece master TSS cmd handle

    参数:
    :   - **p\_data** – **\[in\]** pointer to command data
        - **length** – **\[in\]** length of command data

    返回:
    :   N/A

<a id="_CPPv433subfsm_recv_master_TSS_rsp_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv333subfsm_recv_master_TSS_rsp_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv233subfsm_recv_master_TSS_rsp_handlePK7uint8_t8uint16_t"></a> <a id="subfsm_recv_master_TSS_rsp_handle__uint8_tCP.uint16_t"></a> <a id="tws__sub__fsm_8h_1a2dc0ca97a1b89ed71e2f30b73997ce1b"></a> void subfsm\_recv\_master\_TSS\_rsp\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   handle receive master TSS command response

    recv master TSS cmd rsp handle

    参数:
    :   - **p\_data** – **\[in\]** pointer to command data
        - **length** – **\[in\]** length of command data

    返回:
    :   N/A

<a id="_CPPv436subfsm_recv_master_TSS_rsp_TO_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv336subfsm_recv_master_TSS_rsp_TO_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv236subfsm_recv_master_TSS_rsp_TO_handlePK7uint8_t8uint16_t"></a> <a id="subfsm_recv_master_TSS_rsp_TO_handle__uint8_tCP.uint16_t"></a> <a id="tws__sub__fsm_8h_1a4d6dad5218671a8231bbaa75f0bc5148"></a> void subfsm\_recv\_master\_TSS\_rsp\_TO\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   handle receive master TSS command response timeout

    recv master TSS rsp timeout handle

    参数:
    :   - **p\_data** – **\[in\]** pointer to command data
        - **length** – **\[in\]** length of command data

    返回:
    :   N/A

<a id="_CPPv428subfsm_recv_slave_TSS_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv328subfsm_recv_slave_TSS_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv228subfsm_recv_slave_TSS_handlePK7uint8_t8uint16_t"></a> <a id="subfsm_recv_slave_TSS_handle__uint8_tCP.uint16_t"></a> <a id="tws__sub__fsm_8h_1aed862d1614807b60ea24b7b06cd1b527"></a> void subfsm\_recv\_slave\_TSS\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   handle receive slave TSS command

    recv slave TSS cmd handle

    参数:
    :   - **p\_data** – **\[in\]** pointer to command data
        - **length** – **\[in\]** length of command data

    返回:
    :   N/A

<a id="_CPPv432subfsm_recv_slave_TSS_rsp_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv332subfsm_recv_slave_TSS_rsp_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv232subfsm_recv_slave_TSS_rsp_handlePK7uint8_t8uint16_t"></a> <a id="subfsm_recv_slave_TSS_rsp_handle__uint8_tCP.uint16_t"></a> <a id="tws__sub__fsm_8h_1a1d3da4b519bf250b1aa7ab18cc225f92"></a> void subfsm\_recv\_slave\_TSS\_rsp\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   handle receive slave TSS command response

    recv slave TSS rsp handle

    参数:
    :   - **p\_data** – **\[in\]** pointer to command data
        - **length** – **\[in\]** length of command data

    返回:
    :   N/A

<a id="_CPPv435subfsm_recv_slave_TSS_rsp_TO_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv335subfsm_recv_slave_TSS_rsp_TO_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv235subfsm_recv_slave_TSS_rsp_TO_handlePK7uint8_t8uint16_t"></a> <a id="subfsm_recv_slave_TSS_rsp_TO_handle__uint8_tCP.uint16_t"></a> <a id="tws__sub__fsm_8h_1adc573aa0a7e921336a1e0be004722798"></a> void subfsm\_recv\_slave\_TSS\_rsp\_TO\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   handle receive slave TSS command response timeout

    recv slave TSS rsp timeout handle

    参数:
    :   - **p\_data** – **\[in\]** pointer to command data
        - **length** – **\[in\]** length of command data

    返回:
    :   N/A

<a id="_CPPv429subfsm_recv_stop_snoop_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv329subfsm_recv_stop_snoop_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv229subfsm_recv_stop_snoop_handlePK7uint8_t8uint16_t"></a> <a id="subfsm_recv_stop_snoop_handle__uint8_tCP.uint16_t"></a> <a id="tws__sub__fsm_8h_1a70eefc41e444ae3f559a06547fb42645"></a> void subfsm\_recv\_stop\_snoop\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   handle receive stop snoop command

    recv stop snoop cmd handle

    参数:
    :   - **p\_data** – **\[in\]** pointer to command data
        - **length** – **\[in\]** length of command data

    返回:
    :   N/A

<a id="_CPPv417subfsm_initialisev"></a>

<a id="_CPPv317subfsm_initialisev"></a> <a id="_CPPv217subfsm_initialisev"></a> <a id="subfsm_initialise__void"></a> <a id="tws__sub__fsm_8h_1af293454139ba31a2a5a1857551b022a0"></a> void subfsm\_initialise(void)
:   initialize sub FSM

    subfsm initialise

    返回:
    :   N/A

<a id="_CPPv432subfsm_register_mainfsm_callback16sub_fsm_callback"></a>

<a id="_CPPv332subfsm_register_mainfsm_callback16sub_fsm_callback"></a> <a id="_CPPv232subfsm_register_mainfsm_callback16sub_fsm_callback"></a> <a id="subfsm_register_mainfsm_callback__sub_fsm_callback"></a> <a id="tws__sub__fsm_8h_1a75a89bd17a3f8542975eff09eee13ebd"></a> void subfsm\_register\_mainfsm\_callback([sub\_fsm\_callback](#_CPPv416sub_fsm_callback "sub_fsm_callback") callback)
:   register main FSM callback

    used for mainfsm to register callback function

    参数:
    :   **callback** – **\[in\]** callback of type sub\_fsm\_callback

    返回:
    :   N/A

<a id="_CPPv417subfsm_is_enabled13subfsm_type_t"></a>

<a id="_CPPv317subfsm_is_enabled13subfsm_type_t"></a> <a id="_CPPv217subfsm_is_enabled13subfsm_type_t"></a> <a id="subfsm_is_enabled__subfsm_type_t"></a> <a id="tws__sub__fsm_8h_1af13bf76ec2423a3710ca4223e6d7ee31"></a> bool subfsm\_is\_enabled([subfsm\_type\_t](#_CPPv413subfsm_type_t "subfsm_type_t") fsm\_type)
:   is some fsm type is running

    used to check if the corresponding fsm is running

    参数:
    :   **fsm\_type** – **\[in\]**

    返回:
    :   N/A **TWS\_SUB\_FSM\_H** EOF

<a id="structures"></a>

### Structures

<a id="_CPPv419share_mobile_info_t"></a>

<a id="_CPPv319share_mobile_info_t"></a> <a id="_CPPv219share_mobile_info_t"></a> <a id="share_mobile_info_t"></a> <a id="structshare__mobile__info__t"></a> struct share\_mobile\_info\_t
:   Share mobile phone information structure definition.

<a id="_CPPv413subfsm_info_t"></a>

<a id="_CPPv313subfsm_info_t"></a> <a id="_CPPv213subfsm_info_t"></a> <a id="subfsm_info_t"></a> <a id="structsubfsm__info__t"></a> struct subfsm\_info\_t
:   TWS sub FSM information structure definition.

<a id="_CPPv416handshake_info_t"></a>

<a id="_CPPv316handshake_info_t"></a> <a id="_CPPv216handshake_info_t"></a> <a id="handshake_info_t"></a> <a id="structhandshake__info__t"></a> struct handshake\_info\_t
:   TWS handshake information command structure definition.

<a id="_CPPv415handshake_rsp_t"></a>

<a id="_CPPv315handshake_rsp_t"></a> <a id="_CPPv215handshake_rsp_t"></a> <a id="handshake_rsp_t"></a> <a id="structhandshake__rsp__t"></a> struct handshake\_rsp\_t
:   TWS handshake response command structure definition.

<a id="_CPPv413disc_mobile_t"></a>

<a id="_CPPv313disc_mobile_t"></a> <a id="_CPPv213disc_mobile_t"></a> <a id="disc_mobile_t"></a> <a id="structdisc__mobile__t"></a> struct disc\_mobile\_t
:   Disconnect mobile phone command structure definition.

<a id="_CPPv414tws_switch_m_t"></a>

<a id="_CPPv314tws_switch_m_t"></a> <a id="_CPPv214tws_switch_m_t"></a> <a id="tws_switch_m_t"></a> <a id="structtws__switch__m__t"></a> struct tws\_switch\_m\_t
:   TWS Master switch command structure definition.

<a id="_CPPv414tws_switch_s_t"></a>

<a id="_CPPv314tws_switch_s_t"></a> <a id="_CPPv214tws_switch_s_t"></a> <a id="tws_switch_s_t"></a> <a id="structtws__switch__s__t"></a> struct tws\_switch\_s\_t
:   TWS Slave switch command structure definition.

<a id="_CPPv416tws_stop_snoop_t"></a>

<a id="_CPPv316tws_stop_snoop_t"></a> <a id="_CPPv216tws_stop_snoop_t"></a> <a id="tws_stop_snoop_t"></a> <a id="structtws__stop__snoop__t"></a> struct tws\_stop\_snoop\_t
:   Stop snoop command structure definition.

<a id="_CPPv417tws_start_snoop_t"></a>

<a id="_CPPv317tws_start_snoop_t"></a> <a id="_CPPv217tws_start_snoop_t"></a> <a id="tws_start_snoop_t"></a> <a id="structtws__start__snoop__t"></a> struct tws\_start\_snoop\_t
:   Start snoop command structure definition.

<a id="_CPPv421tws_start_snoop_rsp_t"></a>

<a id="_CPPv321tws_start_snoop_rsp_t"></a> <a id="_CPPv221tws_start_snoop_rsp_t"></a> <a id="tws_start_snoop_rsp_t"></a> <a id="structtws__start__snoop__rsp__t"></a> struct tws\_start\_snoop\_rsp\_t
:   Start snoop response command structure definition.

<a id="macros"></a>

### Macros

<a id="c.FSM_NO_ERROR"></a>

<a id="tws__sub__fsm_8h_1a01f8f78ff3287ea44ddff00bb164862f"></a> FSM\_NO\_ERROR

<a id="c.FSM_ERROR"></a>

<a id="tws__sub__fsm_8h_1ab7a7bb597dad79568aa18d2a4c3e0929"></a> FSM\_ERROR

<a id="c.FSM_CMD_RSP_TO"></a>

<a id="tws__sub__fsm_8h_1aae12525efb725e3fa831243f4369cf4a"></a> FSM\_CMD\_RSP\_TO

<a id="c.FSM_NO_CONN"></a>

<a id="tws__sub__fsm_8h_1a40c40680f60ea8bd470a3f119e427121"></a> FSM\_NO\_CONN

<a id="c.FSM_NO_SNOOP"></a>

<a id="tws__sub__fsm_8h_1a79b568c9666f530049a6cbeb8ef37b21"></a> FSM\_NO\_SNOOP

<a id="c.FSM_CONDITION_ERROR"></a>

<a id="tws__sub__fsm_8h_1aa55c695f64c4ceefa98aebd2d3dccb12"></a> FSM\_CONDITION\_ERROR

<a id="c.FSM_TWS_CONN_FAILED"></a>

<a id="tws__sub__fsm_8h_1a612e917209f12954b9c34cb0deb46d4b"></a> FSM\_TWS\_CONN\_FAILED

<a id="c.FSM_TWS_RETRY_TO"></a>

<a id="tws__sub__fsm_8h_1a901961fc3f865903d8c6177c906e25f7"></a> FSM\_TWS\_RETRY\_TO

<a id="c.IDLE_FSM"></a>

<a id="tws__sub__fsm_8h_1a5dc3f6fa837a4853829ed1f4d5f4c755"></a> IDLE\_FSM

<a id="c.CONNECT_MOBILE_FSM"></a>

<a id="tws__sub__fsm_8h_1a525608f5edae39adc53ed617919fc893"></a> CONNECT\_MOBILE\_FSM
:   0x01

<a id="c.CONNECT_TWS_FSM"></a>

<a id="tws__sub__fsm_8h_1aa5345605b1cd24e5eb45b7f5d35153df"></a> CONNECT\_TWS\_FSM
:   0x02

<a id="c.DISC_MOBILE_FSM"></a>

<a id="tws__sub__fsm_8h_1af5727ef12c9584954ff40a796da90b78"></a> DISC\_MOBILE\_FSM
:   0x04

<a id="c.DISC_TWS_FSM"></a>

<a id="tws__sub__fsm_8h_1a9a13d1681e8becc03c997a1f1c771cb5"></a> DISC\_TWS\_FSM
:   0x08

<a id="c.SYNC_PROFILE_FSM"></a>

<a id="tws__sub__fsm_8h_1a9b762ce4e14fde37398d0a5e0cbf343e"></a> SYNC\_PROFILE\_FSM
:   0x10

<a id="c.START_SNOOP_FSM"></a>

<a id="tws__sub__fsm_8h_1aee619a6225348b197bf80dd2a80bb9ee"></a> START\_SNOOP\_FSM
:   0x20

<a id="c.SUB_TWS_SWITCH_FSM"></a>

<a id="tws__sub__fsm_8h_1addea72eabbb265a0429bfcdff9609590"></a> SUB\_TWS\_SWITCH\_FSM
:   0x40

<a id="c.STOP_SNOOP_FSM"></a>

<a id="tws__sub__fsm_8h_1a3ea6d858484e576ad490394e08631cde"></a> STOP\_SNOOP\_FSM
:   0x80

<a id="c.MAX_SUB_FSM_NUM"></a>

<a id="tws__sub__fsm_8h_1a60ff172c939b2ae846da00ecf631a900"></a> MAX\_SUB\_FSM\_NUM

<a id="c.INVALID_SUB_FSM_IDX"></a>

<a id="tws__sub__fsm_8h_1a24db353500f3f542ed2d715041b0e321"></a> INVALID\_SUB\_FSM\_IDX

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv416sub_fsm_callback"></a>

<a id="_CPPv316sub_fsm_callback"></a> <a id="_CPPv216sub_fsm_callback"></a> <a id="sub_fsm_callback"></a> <a id="tws__sub__fsm_8h_1aa7eb5818189ee6c9d4c6b3fa72b60247"></a> typedef void (\*sub\_fsm\_callback)([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr, uint8\_t action, uint8\_t status, void \*p\_para)
:   TWS sub FSM callback function pointer definition.

<a id="_CPPv412fsm_result_t"></a>

<a id="_CPPv312fsm_result_t"></a> <a id="_CPPv212fsm_result_t"></a> <a id="fsm_result_t"></a> <a id="tws__sub__fsm_8h_1aa1988df180a16f55110463dfc7386559"></a> typedef uint8\_t fsm\_result\_t
:   TWS sub FSM result definition.

<a id="_CPPv413subfsm_type_t"></a>

<a id="_CPPv313subfsm_type_t"></a> <a id="_CPPv213subfsm_type_t"></a> <a id="subfsm_type_t"></a> <a id="tws__sub__fsm_8h_1a7bf4d5c85cd9d602b08dd60f257ab7e9"></a> typedef uint32\_t subfsm\_type\_t
:   TWS sub FSM type definition.

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv413btif_action_e"></a>

<a id="_CPPv313btif_action_e"></a> <a id="_CPPv213btif_action_e"></a> <a id="tws__sub__fsm_8h_1af74c388dcf54e425ac73896fed2d715f"></a> enum btif\_action\_e
:   TWS sub FSM action enumeration definition.

    *Values:*

    <a id="_CPPv4N13btif_action_e11IDLE_ACTIONE"></a>

    <a id="_CPPv3N13btif_action_e11IDLE_ACTIONE"></a> <a id="_CPPv2N13btif_action_e11IDLE_ACTIONE"></a> <a id="tws__sub__fsm_8h_1af74c388dcf54e425ac73896fed2d715fabb080b360babfd96f29da0a896146889"></a> enumerator IDLE\_ACTION
    :   0

    <a id="_CPPv4N13btif_action_e25TWS_LINK_CONNECTED_ACTIONE"></a>

    <a id="_CPPv3N13btif_action_e25TWS_LINK_CONNECTED_ACTIONE"></a> <a id="_CPPv2N13btif_action_e25TWS_LINK_CONNECTED_ACTIONE"></a> <a id="tws__sub__fsm_8h_1af74c388dcf54e425ac73896fed2d715fa85fe85037d553322225614c83523135d"></a> enumerator TWS\_LINK\_CONNECTED\_ACTION
    :   1

    <a id="_CPPv4N13btif_action_e28MOBILE_LINK_CONNECTED_ACTIONE"></a>

    <a id="_CPPv3N13btif_action_e28MOBILE_LINK_CONNECTED_ACTIONE"></a> <a id="_CPPv2N13btif_action_e28MOBILE_LINK_CONNECTED_ACTIONE"></a> <a id="tws__sub__fsm_8h_1af74c388dcf54e425ac73896fed2d715faabf152cb53a69c4dc08b8eec99972292"></a> enumerator MOBILE\_LINK\_CONNECTED\_ACTION
    :   2

    <a id="_CPPv4N13btif_action_e26TWS_LINK_DISCONNECT_ACTIONE"></a>

    <a id="_CPPv3N13btif_action_e26TWS_LINK_DISCONNECT_ACTIONE"></a> <a id="_CPPv2N13btif_action_e26TWS_LINK_DISCONNECT_ACTIONE"></a> <a id="tws__sub__fsm_8h_1af74c388dcf54e425ac73896fed2d715fa73953ea4817b831d8f29d488f8d54360"></a> enumerator TWS\_LINK\_DISCONNECT\_ACTION
    :   3

    <a id="_CPPv4N13btif_action_e29MOBILE_LINK_DISCONNECT_ACTIONE"></a>

    <a id="_CPPv3N13btif_action_e29MOBILE_LINK_DISCONNECT_ACTIONE"></a> <a id="_CPPv2N13btif_action_e29MOBILE_LINK_DISCONNECT_ACTIONE"></a> <a id="tws__sub__fsm_8h_1af74c388dcf54e425ac73896fed2d715faffb2da3c3dc95f72d2d331dc7d3d3635"></a> enumerator MOBILE\_LINK\_DISCONNECT\_ACTION
    :   4

    <a id="_CPPv4N13btif_action_e26MOBILE_ENTER_ACTIVE_ACTIONE"></a>

    <a id="_CPPv3N13btif_action_e26MOBILE_ENTER_ACTIVE_ACTIONE"></a> <a id="_CPPv2N13btif_action_e26MOBILE_ENTER_ACTIVE_ACTIONE"></a> <a id="tws__sub__fsm_8h_1af74c388dcf54e425ac73896fed2d715fae08eb81043222af4ee1b85fb2b882ffa"></a> enumerator MOBILE\_ENTER\_ACTIVE\_ACTION
    :   5

    <a id="_CPPv4N13btif_action_e22SNOOP_CONNECTED_ACTIONE"></a>

    <a id="_CPPv3N13btif_action_e22SNOOP_CONNECTED_ACTIONE"></a> <a id="_CPPv2N13btif_action_e22SNOOP_CONNECTED_ACTIONE"></a> <a id="tws__sub__fsm_8h_1af74c388dcf54e425ac73896fed2d715fa14dafece73040069f88c182949a3823e"></a> enumerator SNOOP\_CONNECTED\_ACTION
    :   6

    <a id="_CPPv4N13btif_action_e24PROFILE_SYNC_DONE_ACTIONE"></a>

    <a id="_CPPv3N13btif_action_e24PROFILE_SYNC_DONE_ACTIONE"></a> <a id="_CPPv2N13btif_action_e24PROFILE_SYNC_DONE_ACTIONE"></a> <a id="tws__sub__fsm_8h_1af74c388dcf54e425ac73896fed2d715fab0c59da94246dc2ed0c26557813ecacb"></a> enumerator PROFILE\_SYNC\_DONE\_ACTION
    :   7

    <a id="_CPPv4N13btif_action_e23SNOOP_DISCONNECT_ACTIONE"></a>

    <a id="_CPPv3N13btif_action_e23SNOOP_DISCONNECT_ACTIONE"></a> <a id="_CPPv2N13btif_action_e23SNOOP_DISCONNECT_ACTIONE"></a> <a id="tws__sub__fsm_8h_1af74c388dcf54e425ac73896fed2d715fa8c75bcb4a72497ef1e912fd62654b50e"></a> enumerator SNOOP\_DISCONNECT\_ACTION
    :   8

    <a id="_CPPv4N13btif_action_e22TWS_SWITCH_COMP_ACTIONE"></a>

    <a id="_CPPv3N13btif_action_e22TWS_SWITCH_COMP_ACTIONE"></a> <a id="_CPPv2N13btif_action_e22TWS_SWITCH_COMP_ACTIONE"></a> <a id="tws__sub__fsm_8h_1af74c388dcf54e425ac73896fed2d715fae3df5b2db1b3eb515a1038a8f7727cdb"></a> enumerator TWS\_SWITCH\_COMP\_ACTION
    :   9

    <a id="_CPPv4N13btif_action_e21HANDSHARK_COMP_ACTIONE"></a>

    <a id="_CPPv3N13btif_action_e21HANDSHARK_COMP_ACTIONE"></a> <a id="_CPPv2N13btif_action_e21HANDSHARK_COMP_ACTIONE"></a> <a id="tws__sub__fsm_8h_1af74c388dcf54e425ac73896fed2d715faa773af16a742e577541b7e5b9cd0065a"></a> enumerator HANDSHARK\_COMP\_ACTION
    :   10

    <a id="_CPPv4N13btif_action_e25TWS_SWITCH_ALLOWED_ACTIONE"></a>

    <a id="_CPPv3N13btif_action_e25TWS_SWITCH_ALLOWED_ACTIONE"></a> <a id="_CPPv2N13btif_action_e25TWS_SWITCH_ALLOWED_ACTIONE"></a> <a id="tws__sub__fsm_8h_1af74c388dcf54e425ac73896fed2d715fa71ce17cd3bc7e5af44b02760b5a22c37"></a> enumerator TWS\_SWITCH\_ALLOWED\_ACTION
    :   11

    <a id="_CPPv4N13btif_action_e21TWS_SWITCH_RSP_ACTIONE"></a>

    <a id="_CPPv3N13btif_action_e21TWS_SWITCH_RSP_ACTIONE"></a> <a id="_CPPv2N13btif_action_e21TWS_SWITCH_RSP_ACTIONE"></a> <a id="tws__sub__fsm_8h_1af74c388dcf54e425ac73896fed2d715fadbcf0a5ef50ef1f21df880a8b36cc429"></a> enumerator TWS\_SWITCH\_RSP\_ACTION
    :   12

<a id="_CPPv414subfsm_state_e"></a>

<a id="_CPPv314subfsm_state_e"></a> <a id="_CPPv214subfsm_state_e"></a> <a id="tws__sub__fsm_8h_1a03c09076b9d3a056d52d99d48e1926f3"></a> enum subfsm\_state\_e
:   TWS sub FSM state enumeration definition.

    *Values:*

    <a id="_CPPv4N14subfsm_state_e12SUB_FSM_IDLEE"></a>

    <a id="_CPPv3N14subfsm_state_e12SUB_FSM_IDLEE"></a> <a id="_CPPv2N14subfsm_state_e12SUB_FSM_IDLEE"></a> <a id="tws__sub__fsm_8h_1a03c09076b9d3a056d52d99d48e1926f3ac4a10f934f6b882f8e34b569c885e616"></a> enumerator SUB\_FSM\_IDLE
    :   0

    <a id="_CPPv4N14subfsm_state_e24SUB_FSM_W4_TWS_CONNECTEDE"></a>

    <a id="_CPPv3N14subfsm_state_e24SUB_FSM_W4_TWS_CONNECTEDE"></a> <a id="_CPPv2N14subfsm_state_e24SUB_FSM_W4_TWS_CONNECTEDE"></a> <a id="tws__sub__fsm_8h_1a03c09076b9d3a056d52d99d48e1926f3a14f6e227f6351786dc783389469be7b3"></a> enumerator SUB\_FSM\_W4\_TWS\_CONNECTED
    :   1

    <a id="_CPPv4N14subfsm_state_e27SUB_FSM_W4_MOBILE_CONNECTEDE"></a>

    <a id="_CPPv3N14subfsm_state_e27SUB_FSM_W4_MOBILE_CONNECTEDE"></a> <a id="_CPPv2N14subfsm_state_e27SUB_FSM_W4_MOBILE_CONNECTEDE"></a> <a id="tws__sub__fsm_8h_1a03c09076b9d3a056d52d99d48e1926f3af0c9c93a6654887d0d4614ecb3f63eb7"></a> enumerator SUB\_FSM\_W4\_MOBILE\_CONNECTED
    :   2

    <a id="_CPPv4N14subfsm_state_e27SUB_FSM_W4_TWS_DISCONNECTEDE"></a>

    <a id="_CPPv3N14subfsm_state_e27SUB_FSM_W4_TWS_DISCONNECTEDE"></a> <a id="_CPPv2N14subfsm_state_e27SUB_FSM_W4_TWS_DISCONNECTEDE"></a> <a id="tws__sub__fsm_8h_1a03c09076b9d3a056d52d99d48e1926f3a49de2a0df6a194b5883b675d3519e289"></a> enumerator SUB\_FSM\_W4\_TWS\_DISCONNECTED
    :   3

    <a id="_CPPv4N14subfsm_state_e30SUB_FSM_W4_MOBILE_DISCONNECTEDE"></a>

    <a id="_CPPv3N14subfsm_state_e30SUB_FSM_W4_MOBILE_DISCONNECTEDE"></a> <a id="_CPPv2N14subfsm_state_e30SUB_FSM_W4_MOBILE_DISCONNECTEDE"></a> <a id="tws__sub__fsm_8h_1a03c09076b9d3a056d52d99d48e1926f3a89f321449cd38ad39a057e4681f4d270"></a> enumerator SUB\_FSM\_W4\_MOBILE\_DISCONNECTED
    :   4

    <a id="_CPPv4N14subfsm_state_e23SUB_FSM_W4_ENTER_ACTIVEE"></a>

    <a id="_CPPv3N14subfsm_state_e23SUB_FSM_W4_ENTER_ACTIVEE"></a> <a id="_CPPv2N14subfsm_state_e23SUB_FSM_W4_ENTER_ACTIVEE"></a> <a id="tws__sub__fsm_8h_1a03c09076b9d3a056d52d99d48e1926f3a88a50dfa5841e5cc9dd87ed3e324e06f"></a> enumerator SUB\_FSM\_W4\_ENTER\_ACTIVE
    :   5

    <a id="_CPPv4N14subfsm_state_e26SUB_FSM_W4_SNOOP_CONNECTEDE"></a>

    <a id="_CPPv3N14subfsm_state_e26SUB_FSM_W4_SNOOP_CONNECTEDE"></a> <a id="_CPPv2N14subfsm_state_e26SUB_FSM_W4_SNOOP_CONNECTEDE"></a> <a id="tws__sub__fsm_8h_1a03c09076b9d3a056d52d99d48e1926f3ae7530497c83c45d7dcef08e0c4a6c937"></a> enumerator SUB\_FSM\_W4\_SNOOP\_CONNECTED
    :   6

    <a id="_CPPv4N14subfsm_state_e23SUB_FSM_W4_PROFILE_SYNCE"></a>

    <a id="_CPPv3N14subfsm_state_e23SUB_FSM_W4_PROFILE_SYNCE"></a> <a id="_CPPv2N14subfsm_state_e23SUB_FSM_W4_PROFILE_SYNCE"></a> <a id="tws__sub__fsm_8h_1a03c09076b9d3a056d52d99d48e1926f3ae92b3084ac43875c39a7f4df75932877"></a> enumerator SUB\_FSM\_W4\_PROFILE\_SYNC
    :   7

    <a id="_CPPv4N14subfsm_state_e29SUB_FSM_W4_SNOOP_DISCONNECTEDE"></a>

    <a id="_CPPv3N14subfsm_state_e29SUB_FSM_W4_SNOOP_DISCONNECTEDE"></a> <a id="_CPPv2N14subfsm_state_e29SUB_FSM_W4_SNOOP_DISCONNECTEDE"></a> <a id="tws__sub__fsm_8h_1a03c09076b9d3a056d52d99d48e1926f3af1fcd13c7d7e2b686d1535754e471919"></a> enumerator SUB\_FSM\_W4\_SNOOP\_DISCONNECTED
    :   8

    <a id="_CPPv4N14subfsm_state_e26SUB_FSM_W4_TWS_SWITCH_COMPE"></a>

    <a id="_CPPv3N14subfsm_state_e26SUB_FSM_W4_TWS_SWITCH_COMPE"></a> <a id="_CPPv2N14subfsm_state_e26SUB_FSM_W4_TWS_SWITCH_COMPE"></a> <a id="tws__sub__fsm_8h_1a03c09076b9d3a056d52d99d48e1926f3ab3e27ca1ea2190e16ca227c08371f55f"></a> enumerator SUB\_FSM\_W4\_TWS\_SWITCH\_COMP
    :   9

    <a id="_CPPv4N14subfsm_state_e25SUB_FSM_W4_HANDSHARK_COMPE"></a>

    <a id="_CPPv3N14subfsm_state_e25SUB_FSM_W4_HANDSHARK_COMPE"></a> <a id="_CPPv2N14subfsm_state_e25SUB_FSM_W4_HANDSHARK_COMPE"></a> <a id="tws__sub__fsm_8h_1a03c09076b9d3a056d52d99d48e1926f3aa1621ad7c239a9e2b9acf74f5f062f06"></a> enumerator SUB\_FSM\_W4\_HANDSHARK\_COMP
    :   10

    <a id="_CPPv4N14subfsm_state_e29SUB_FSM_W4_TWS_SWITCH_ALLOWEDE"></a>

    <a id="_CPPv3N14subfsm_state_e29SUB_FSM_W4_TWS_SWITCH_ALLOWEDE"></a> <a id="_CPPv2N14subfsm_state_e29SUB_FSM_W4_TWS_SWITCH_ALLOWEDE"></a> <a id="tws__sub__fsm_8h_1a03c09076b9d3a056d52d99d48e1926f3ae980ef59cace4e0ee396452d88ba8c6d"></a> enumerator SUB\_FSM\_W4\_TWS\_SWITCH\_ALLOWED
    :   11

    <a id="_CPPv4N14subfsm_state_e25SUB_FSM_W4_TWS_SWITCH_RSPE"></a>

    <a id="_CPPv3N14subfsm_state_e25SUB_FSM_W4_TWS_SWITCH_RSPE"></a> <a id="_CPPv2N14subfsm_state_e25SUB_FSM_W4_TWS_SWITCH_RSPE"></a> <a id="tws__sub__fsm_8h_1a03c09076b9d3a056d52d99d48e1926f3a29cae347b6cc9e6037aa618de0ed8ae6"></a> enumerator SUB\_FSM\_W4\_TWS\_SWITCH\_RSP
    :   12
