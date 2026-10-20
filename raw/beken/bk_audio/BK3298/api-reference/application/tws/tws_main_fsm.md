---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/tws/tws_main_fsm.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="tws-main-fsm-functions"></a>

# TWS Main FSM Functions

<a id="tws-main-fsm-api-brief"></a>

## TWS\_MAIN\_FSM API Brief

| Application | Brief |
| --- | --- |
| [`tws_mainfsm_entry()`](#_CPPv417tws_mainfsm_entry15maimfsm_input_t "tws_mainfsm_entry") | TWS Main FSM entry |
| [`tws_mainfsm_initialise()`](#_CPPv422tws_mainfsm_initialisev "tws_mainfsm_initialise") | Initialize TWS Main FSM |
| [`tws_mainfsm_get_active_by_type()`](#_CPPv430tws_mainfsm_get_active_by_type8uint32_t "tws_mainfsm_get_active_by_type") | Get the active status of the TWS Main FSM |
| [`tws_mainfsm_connnect_fsm_ongoing()`](#_CPPv432tws_mainfsm_connnect_fsm_ongoingP14btif_bd_addr_t "tws_mainfsm_connnect_fsm_ongoing") | Check that the TWS main FSM is connecting |

<a id="tws-main-fsm-api-reference"></a>

## TWS\_MAIN\_FSM API Reference

<a id="header-file"></a>

### Header File

- [tws/tws\_ux/inc/tws\_main\_fsm.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/tws/tws_ux/inc/tws_main_fsm.h)

<a id="functions"></a>

### Functions

<a id="_CPPv417tws_mainfsm_entry15maimfsm_input_t"></a>

<a id="_CPPv317tws_mainfsm_entry15maimfsm_input_t"></a> <a id="_CPPv217tws_mainfsm_entry15maimfsm_input_t"></a> <a id="tws_mainfsm_entry__maimfsm_input_t"></a> <a id="tws__main__fsm_8h_1afd38bac24ab916c0fb4561edf9713b9d"></a> void tws\_mainfsm\_entry([maimfsm\_input\_t](#_CPPv415maimfsm_input_t "maimfsm_input_t") mainfsm\_input)
:   TWS Main FSM entry.

    Handle the TWS Main finite state machine (FSM).

    参数:
    :   **mainfsm\_input** – **\[in\]** main FSM input of type [maimfsm\_input\_t](#structmaimfsm__input__t).

    返回:
    :   N/A

<a id="_CPPv422tws_mainfsm_initialisev"></a>

<a id="_CPPv322tws_mainfsm_initialisev"></a> <a id="_CPPv222tws_mainfsm_initialisev"></a> <a id="tws_mainfsm_initialise__void"></a> <a id="tws__main__fsm_8h_1a01cbb46ef0feb22325ebf689b57f473b"></a> void tws\_mainfsm\_initialise(void)
:   Initialize TWS Main FSM.

    Initialize the TWS Main finite state machine (FSM).

    返回:
    :   N/A

<a id="_CPPv430tws_mainfsm_get_active_by_type8uint32_t"></a>

<a id="_CPPv330tws_mainfsm_get_active_by_type8uint32_t"></a> <a id="_CPPv230tws_mainfsm_get_active_by_type8uint32_t"></a> <a id="tws_mainfsm_get_active_by_type__uint32_t"></a> <a id="tws__main__fsm_8h_1a6f0194f1358f9ee31c182bbc955785c2"></a> [mainfsm\_type\_t](#_CPPv414mainfsm_type_t "mainfsm_type_t") tws\_mainfsm\_get\_active\_by\_type(uint32\_t mainfsm\_type)
:   Get the active status of the TWS Main FSM.

    More details

    参数:
    :   **mainfsm\_type** – **\[in\]** find mainfsm type, if the mainfsm type is INVALID\_FSM, then return fsm type that the main fsm is currently running, without comparing the mainfsm\_type.

    返回:
    :   main FSM input of type [maimfsm\_input\_t](#structmaimfsm__input__t).

<a id="_CPPv432tws_mainfsm_connnect_fsm_ongoingP14btif_bd_addr_t"></a>

<a id="_CPPv332tws_mainfsm_connnect_fsm_ongoingP14btif_bd_addr_t"></a> <a id="_CPPv232tws_mainfsm_connnect_fsm_ongoingP14btif_bd_addr_t"></a> <a id="tws_mainfsm_connnect_fsm_ongoing__btif_bd_addr_tP"></a> <a id="tws__main__fsm_8h_1a2bca5bb7fead9fab18a3bd1bbd2d0e4f"></a> bool tws\_mainfsm\_connnect\_fsm\_ongoing([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_bd\_addr)
:   Check that the TWS main FSM is connecting.

    Check that the TWS main FSM is connecting to the mobile phone with address \[p\_bd\_addr\].

    参数:
    :   **p\_bd\_addr** – **\[in\]** pointer to an address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t).

    返回值:
    :   - **true** – on going
        - **false** – no action **TWS\_MAIN\_FSM\_H** EOF

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv413mobile_info_t"></a>

<a id="_CPPv313mobile_info_t"></a> <a id="_CPPv213mobile_info_t"></a> <a id="mobile_info_t"></a> <a id="structmobile__info__t"></a> struct mobile\_info\_t
:   mobile information structure definition.

<a id="_CPPv415maimfsm_input_t"></a>

<a id="_CPPv315maimfsm_input_t"></a> <a id="_CPPv215maimfsm_input_t"></a> <a id="maimfsm_input_t"></a> <a id="structmaimfsm__input__t"></a> struct maimfsm\_input\_t
:   Main FSM input structure definition.

<a id="macros"></a>

### Macros

<a id="c.MAINFSM_ENV_MAX"></a>

<a id="tws__main__fsm_8h_1a1ba40176b0fc3de76abe80a5e6d4f205"></a> MAINFSM\_ENV\_MAX

<a id="c.INVALID_MAIN_FSM_IDX"></a>

<a id="tws__main__fsm_8h_1a9897f89d1570199acded4717b9575323"></a> INVALID\_MAIN\_FSM\_IDX

<a id="c.INVALID_FSM"></a>

<a id="tws__main__fsm_8h_1aed30357ce34143279e28247c38fe6466"></a> INVALID\_FSM

<a id="c.CONNECT_FSM"></a>

<a id="tws__main__fsm_8h_1a6749826db2ba82230748cb63de5c69e7"></a> CONNECT\_FSM

<a id="c.TWS_SWITCH_FSM"></a>

<a id="tws__main__fsm_8h_1a729100eccdc78cb47fa454e2b6905839"></a> TWS\_SWITCH\_FSM

<a id="c.DISCONNECT_MOBILE_FSM"></a>

<a id="tws__main__fsm_8h_1a86922304bc6672e934b5220caa61f360"></a> DISCONNECT\_MOBILE\_FSM

<a id="c.ENTER_PAIRING_FSM"></a>

<a id="tws__main__fsm_8h_1a313eebfb8568924502eeef79dee28954"></a> ENTER\_PAIRING\_FSM

<a id="c.DISCONNECT_TWS_FSM"></a>

<a id="tws__main__fsm_8h_1abf0cc77e3aa51e60d4a91392b04699eb"></a> DISCONNECT\_TWS\_FSM

<a id="c.CONNECT_TWS_MAIN_FSM"></a>

<a id="tws__main__fsm_8h_1a452753a1672073bb4805113e383f016e"></a> CONNECT\_TWS\_MAIN\_FSM

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv414mainfsm_type_t"></a>

<a id="_CPPv314mainfsm_type_t"></a> <a id="_CPPv214mainfsm_type_t"></a> <a id="mainfsm_type_t"></a> <a id="tws__main__fsm_8h_1ae1b5b38d90db2f8e977fa7fc00eac6f5"></a> typedef uint32\_t mainfsm\_type\_t
:   Main FSM type definition.

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv413main_action_e"></a>

<a id="_CPPv313main_action_e"></a> <a id="_CPPv213main_action_e"></a> <a id="tws__main__fsm_8h_1a6886c6212cdde4cdb27e3b61128a8edd"></a> enum main\_action\_e
:   Main action enumeration definition.

    *Values:*

    <a id="_CPPv4N13main_action_e16MAIN_IDLE_ACTIONE"></a>

    <a id="_CPPv3N13main_action_e16MAIN_IDLE_ACTIONE"></a> <a id="_CPPv2N13main_action_e16MAIN_IDLE_ACTIONE"></a> <a id="tws__main__fsm_8h_1a6886c6212cdde4cdb27e3b61128a8eddab794d52f56194f190688977cc572af95"></a> enumerator MAIN\_IDLE\_ACTION

    <a id="_CPPv4N13main_action_e30MAIN_TWS_LINK_CONNECTED_ACTIONE"></a>

    <a id="_CPPv3N13main_action_e30MAIN_TWS_LINK_CONNECTED_ACTIONE"></a> <a id="_CPPv2N13main_action_e30MAIN_TWS_LINK_CONNECTED_ACTIONE"></a> <a id="tws__main__fsm_8h_1a6886c6212cdde4cdb27e3b61128a8eddad1d13f72b453ee492a3c8bf243d83df4"></a> enumerator MAIN\_TWS\_LINK\_CONNECTED\_ACTION

    <a id="_CPPv4N13main_action_e33MAIN_MOBILE_LINK_CONNECTED_ACTIONE"></a>

    <a id="_CPPv3N13main_action_e33MAIN_MOBILE_LINK_CONNECTED_ACTIONE"></a> <a id="_CPPv2N13main_action_e33MAIN_MOBILE_LINK_CONNECTED_ACTIONE"></a> <a id="tws__main__fsm_8h_1a6886c6212cdde4cdb27e3b61128a8edda369499ad3e1a7974ca14e0758941a9c0"></a> enumerator MAIN\_MOBILE\_LINK\_CONNECTED\_ACTION

    <a id="_CPPv4N13main_action_e31MAIN_TWS_LINK_DISCONNECT_ACTIONE"></a>

    <a id="_CPPv3N13main_action_e31MAIN_TWS_LINK_DISCONNECT_ACTIONE"></a> <a id="_CPPv2N13main_action_e31MAIN_TWS_LINK_DISCONNECT_ACTIONE"></a> <a id="tws__main__fsm_8h_1a6886c6212cdde4cdb27e3b61128a8eddaa7d23ab30168ad23f9e41091a4c8c551"></a> enumerator MAIN\_TWS\_LINK\_DISCONNECT\_ACTION

    <a id="_CPPv4N13main_action_e34MAIN_MOBILE_LINK_DISCONNECT_ACTIONE"></a>

    <a id="_CPPv3N13main_action_e34MAIN_MOBILE_LINK_DISCONNECT_ACTIONE"></a> <a id="_CPPv2N13main_action_e34MAIN_MOBILE_LINK_DISCONNECT_ACTIONE"></a> <a id="tws__main__fsm_8h_1a6886c6212cdde4cdb27e3b61128a8eddab8fa952278efd2a62793e8fa94fd3115"></a> enumerator MAIN\_MOBILE\_LINK\_DISCONNECT\_ACTION

    <a id="_CPPv4N13main_action_e31MAIN_MOBILE_ENTER_ACTIVE_ACTIONE"></a>

    <a id="_CPPv3N13main_action_e31MAIN_MOBILE_ENTER_ACTIVE_ACTIONE"></a> <a id="_CPPv2N13main_action_e31MAIN_MOBILE_ENTER_ACTIVE_ACTIONE"></a> <a id="tws__main__fsm_8h_1a6886c6212cdde4cdb27e3b61128a8eddaf99dc00bbdb296c6714c60c3694f5c71"></a> enumerator MAIN\_MOBILE\_ENTER\_ACTIVE\_ACTION

    <a id="_CPPv4N13main_action_e27MAIN_SNOOP_CONNECTED_ACTIONE"></a>

    <a id="_CPPv3N13main_action_e27MAIN_SNOOP_CONNECTED_ACTIONE"></a> <a id="_CPPv2N13main_action_e27MAIN_SNOOP_CONNECTED_ACTIONE"></a> <a id="tws__main__fsm_8h_1a6886c6212cdde4cdb27e3b61128a8eddaf7a30c48f0a10c86ee3d799828f7339f"></a> enumerator MAIN\_SNOOP\_CONNECTED\_ACTION

    <a id="_CPPv4N13main_action_e29MAIN_PROFILE_SYNC_DONE_ACTIONE"></a>

    <a id="_CPPv3N13main_action_e29MAIN_PROFILE_SYNC_DONE_ACTIONE"></a> <a id="_CPPv2N13main_action_e29MAIN_PROFILE_SYNC_DONE_ACTIONE"></a> <a id="tws__main__fsm_8h_1a6886c6212cdde4cdb27e3b61128a8edda89b7b07815e0fc4592430cb5dc7fcb4c"></a> enumerator MAIN\_PROFILE\_SYNC\_DONE\_ACTION

    <a id="_CPPv4N13main_action_e28MAIN_SNOOP_DISCONNECT_ACTIONE"></a>

    <a id="_CPPv3N13main_action_e28MAIN_SNOOP_DISCONNECT_ACTIONE"></a> <a id="_CPPv2N13main_action_e28MAIN_SNOOP_DISCONNECT_ACTIONE"></a> <a id="tws__main__fsm_8h_1a6886c6212cdde4cdb27e3b61128a8edda650418281b17ad5f8e3337ef3fe9c5f8"></a> enumerator MAIN\_SNOOP\_DISCONNECT\_ACTION

    <a id="_CPPv4N13main_action_e27MAIN_TWS_SWITCH_COMP_ACTIONE"></a>

    <a id="_CPPv3N13main_action_e27MAIN_TWS_SWITCH_COMP_ACTIONE"></a> <a id="_CPPv2N13main_action_e27MAIN_TWS_SWITCH_COMP_ACTIONE"></a> <a id="tws__main__fsm_8h_1a6886c6212cdde4cdb27e3b61128a8eddac670212d35165b6e33c0050e82ce3afe"></a> enumerator MAIN\_TWS\_SWITCH\_COMP\_ACTION

<a id="_CPPv415mainfsm_state_e"></a>

<a id="_CPPv315mainfsm_state_e"></a> <a id="_CPPv215mainfsm_state_e"></a> <a id="tws__main__fsm_8h_1a3876a020909e04663b9262f98e2df95f"></a> enum mainfsm\_state\_e
:   Main FSM state enumeration definition.

    *Values:*

    <a id="_CPPv4N15mainfsm_state_e13MAIN_FSM_IDLEE"></a>

    <a id="_CPPv3N15mainfsm_state_e13MAIN_FSM_IDLEE"></a> <a id="_CPPv2N15mainfsm_state_e13MAIN_FSM_IDLEE"></a> <a id="tws__main__fsm_8h_1a3876a020909e04663b9262f98e2df95fa9b4e0adc955c1af8fa9209026a788d4f"></a> enumerator MAIN\_FSM\_IDLE

    <a id="_CPPv4N15mainfsm_state_e25MAIN_FSM_W4_TWS_CONNECTEDE"></a>

    <a id="_CPPv3N15mainfsm_state_e25MAIN_FSM_W4_TWS_CONNECTEDE"></a> <a id="_CPPv2N15mainfsm_state_e25MAIN_FSM_W4_TWS_CONNECTEDE"></a> <a id="tws__main__fsm_8h_1a3876a020909e04663b9262f98e2df95fa270644dd831c64346b2b8e3609f2a978"></a> enumerator MAIN\_FSM\_W4\_TWS\_CONNECTED
    :   1

    <a id="_CPPv4N15mainfsm_state_e28MAIN_FSM_W4_MOBILE_CONNECTEDE"></a>

    <a id="_CPPv3N15mainfsm_state_e28MAIN_FSM_W4_MOBILE_CONNECTEDE"></a> <a id="_CPPv2N15mainfsm_state_e28MAIN_FSM_W4_MOBILE_CONNECTEDE"></a> <a id="tws__main__fsm_8h_1a3876a020909e04663b9262f98e2df95fa08ab1b1046735ddf860eedca160ad01d"></a> enumerator MAIN\_FSM\_W4\_MOBILE\_CONNECTED
    :   2

    <a id="_CPPv4N15mainfsm_state_e28MAIN_FSM_W4_TWS_DISCONNECTEDE"></a>

    <a id="_CPPv3N15mainfsm_state_e28MAIN_FSM_W4_TWS_DISCONNECTEDE"></a> <a id="_CPPv2N15mainfsm_state_e28MAIN_FSM_W4_TWS_DISCONNECTEDE"></a> <a id="tws__main__fsm_8h_1a3876a020909e04663b9262f98e2df95fad6e66b107b4b61938a772a358d891ed3"></a> enumerator MAIN\_FSM\_W4\_TWS\_DISCONNECTED
    :   3

    <a id="_CPPv4N15mainfsm_state_e31MAIN_FSM_W4_MOBILE_DISCONNECTEDE"></a>

    <a id="_CPPv3N15mainfsm_state_e31MAIN_FSM_W4_MOBILE_DISCONNECTEDE"></a> <a id="_CPPv2N15mainfsm_state_e31MAIN_FSM_W4_MOBILE_DISCONNECTEDE"></a> <a id="tws__main__fsm_8h_1a3876a020909e04663b9262f98e2df95fa93fefe835026ad21525ebaac0f88e7bf"></a> enumerator MAIN\_FSM\_W4\_MOBILE\_DISCONNECTED
    :   4

    <a id="_CPPv4N15mainfsm_state_e24MAIN_FSM_W4_ENTER_ACTIVEE"></a>

    <a id="_CPPv3N15mainfsm_state_e24MAIN_FSM_W4_ENTER_ACTIVEE"></a> <a id="_CPPv2N15mainfsm_state_e24MAIN_FSM_W4_ENTER_ACTIVEE"></a> <a id="tws__main__fsm_8h_1a3876a020909e04663b9262f98e2df95faa194550deb0b0a25d8e7f06381467195"></a> enumerator MAIN\_FSM\_W4\_ENTER\_ACTIVE
    :   5

    <a id="_CPPv4N15mainfsm_state_e27MAIN_FSM_W4_SNOOP_CONNECTEDE"></a>

    <a id="_CPPv3N15mainfsm_state_e27MAIN_FSM_W4_SNOOP_CONNECTEDE"></a> <a id="_CPPv2N15mainfsm_state_e27MAIN_FSM_W4_SNOOP_CONNECTEDE"></a> <a id="tws__main__fsm_8h_1a3876a020909e04663b9262f98e2df95fa2ae848a91f13f2b1d3e03dafe1b3f518"></a> enumerator MAIN\_FSM\_W4\_SNOOP\_CONNECTED
    :   6

    <a id="_CPPv4N15mainfsm_state_e29MAIN_FSM_W4_PROFILE_SYNC_DONEE"></a>

    <a id="_CPPv3N15mainfsm_state_e29MAIN_FSM_W4_PROFILE_SYNC_DONEE"></a> <a id="_CPPv2N15mainfsm_state_e29MAIN_FSM_W4_PROFILE_SYNC_DONEE"></a> <a id="tws__main__fsm_8h_1a3876a020909e04663b9262f98e2df95fa2abd4618d463a1dc28dfb96ce4c69979"></a> enumerator MAIN\_FSM\_W4\_PROFILE\_SYNC\_DONE
    :   7

    <a id="_CPPv4N15mainfsm_state_e30MAIN_FSM_W4_SNOOP_DISCONNECTEDE"></a>

    <a id="_CPPv3N15mainfsm_state_e30MAIN_FSM_W4_SNOOP_DISCONNECTEDE"></a> <a id="_CPPv2N15mainfsm_state_e30MAIN_FSM_W4_SNOOP_DISCONNECTEDE"></a> <a id="tws__main__fsm_8h_1a3876a020909e04663b9262f98e2df95fac43c10ac4c2b12318e88c4e870cc507b"></a> enumerator MAIN\_FSM\_W4\_SNOOP\_DISCONNECTED
    :   8

    <a id="_CPPv4N15mainfsm_state_e27MAIN_FSM_W4_TWS_SWITCH_COMPE"></a>

    <a id="_CPPv3N15mainfsm_state_e27MAIN_FSM_W4_TWS_SWITCH_COMPE"></a> <a id="_CPPv2N15mainfsm_state_e27MAIN_FSM_W4_TWS_SWITCH_COMPE"></a> <a id="tws__main__fsm_8h_1a3876a020909e04663b9262f98e2df95fa7f09a7a7116105687294ea36e954a629"></a> enumerator MAIN\_FSM\_W4\_TWS\_SWITCH\_COMP
    :   9
