---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/tws/tws_private_cmd.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="tws-private-command-functions"></a>

# TWS Private Command Functions

<a id="tws-private-cmd-api-brief"></a>

## TWS\_PRIVATE\_CMD API Brief

| Application | Brief |
| --- | --- |
| [`tws_send_private_cmd()`](#_CPPv420tws_send_private_cmdPv8uint32_tb "tws_send_private_cmd") | send tws private command |
| [`tws_recv_tws_cmd_in_task()`](#_CPPv424tws_recv_tws_cmd_in_taskP13tws_rx_data_t "tws_recv_tws_cmd_in_task") | receive tws command |
| [`tws_send_tws_cmd_in_task()`](#_CPPv424tws_send_tws_cmd_in_taskP13tws_tx_data_t "tws_send_tws_cmd_in_task") | send tws command |
| [`tws_l2cap_rx_data_handle()`](#_CPPv424tws_l2cap_rx_data_handleP7uint8_t8uint16_t "tws_l2cap_rx_data_handle") | handle rx tws private data |
| [`tws_l2cap_rx_event_handle()`](#_CPPv425tws_l2cap_rx_event_handle7uint8_t "tws_l2cap_rx_event_handle") | handle rx tws private connection event |
| [`tws_private_cmd_init()`](#_CPPv420tws_private_cmd_initv "tws_private_cmd_init") | initialize tws private command |
| [`tws_carryout_pending_tx_cmd()`](#_CPPv427tws_carryout_pending_tx_cmdv "tws_carryout_pending_tx_cmd") | carry out pending tx command |

<a id="tws-private-cmd-api-reference"></a>

## TWS\_PRIVATE\_CMD API Reference

<a id="header-file"></a>

### Header File

- [tws/tws\_ux/inc/tws\_private\_cmd.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/tws/tws_ux/inc/tws_private_cmd.h)

<a id="functions"></a>

### Functions

<a id="_CPPv420tws_send_private_cmdPv8uint32_tb"></a>

<a id="_CPPv320tws_send_private_cmdPv8uint32_tb"></a> <a id="_CPPv220tws_send_private_cmdPv8uint32_tb"></a> <a id="tws_send_private_cmd__voidP.uint32_t.b"></a> <a id="tws__private__cmd_8h_1aca538f5eb9679c36cbbccc02c640b33e"></a> void tws\_send\_private\_cmd(void \*p\_data, uint32\_t length, bool need\_rsp)
:   send tws private command

    common interface for send tws command

    参数:
    :   - **p\_data** – **\[in\]** pointer to command data.
        - **length** – **\[in\]** length of command data.
        - **need\_rsp** – **\[in\]** need response. true is need response, false is no response.

    返回:
    :   N/A

<a id="_CPPv424tws_recv_tws_cmd_in_taskP13tws_rx_data_t"></a>

<a id="_CPPv324tws_recv_tws_cmd_in_taskP13tws_rx_data_t"></a> <a id="_CPPv224tws_recv_tws_cmd_in_taskP13tws_rx_data_t"></a> <a id="tws_recv_tws_cmd_in_task__tws_rx_data_tP"></a> <a id="tws__private__cmd_8h_1a550f06961aeb85e4629a7df343d8a94a"></a> void tws\_recv\_tws\_cmd\_in\_task([tws\_rx\_data\_t](#_CPPv413tws_rx_data_t "tws_rx_data_t") \*p\_msg)
:   receive tws command

    receive tws command handler in tws task

    参数:
    :   **p\_msg** – **\[in\]** pointer to message data.

    返回:
    :   N/A

<a id="_CPPv424tws_send_tws_cmd_in_taskP13tws_tx_data_t"></a>

<a id="_CPPv324tws_send_tws_cmd_in_taskP13tws_tx_data_t"></a> <a id="_CPPv224tws_send_tws_cmd_in_taskP13tws_tx_data_t"></a> <a id="tws_send_tws_cmd_in_task__tws_tx_data_tP"></a> <a id="tws__private__cmd_8h_1a637abe434b8b4df35a915032a94c682c"></a> void tws\_send\_tws\_cmd\_in\_task([tws\_tx\_data\_t](#_CPPv413tws_tx_data_t "tws_tx_data_t") \*p\_msg)
:   send tws command

    send tws command in tws task

    参数:
    :   **p\_msg** – **\[in\]** pointer to message data.

    返回:
    :   N/A

<a id="_CPPv424tws_l2cap_rx_data_handleP7uint8_t8uint16_t"></a>

<a id="_CPPv324tws_l2cap_rx_data_handleP7uint8_t8uint16_t"></a> <a id="_CPPv224tws_l2cap_rx_data_handleP7uint8_t8uint16_t"></a> <a id="tws_l2cap_rx_data_handle__uint8_tP.uint16_t"></a> <a id="tws__private__cmd_8h_1a1e6cd433ba6717b002e41235ac2adbf8"></a> void tws\_l2cap\_rx\_data\_handle(uint8\_t \*p\_data, uint16\_t length)
:   handle rx tws private data

    tws private data handler in bt task

    参数:
    :   - **p\_data** – **\[in\]** pointer to rx data.
        - **length** – **\[in\]** length of rx data.

    返回:
    :   N/A

<a id="_CPPv425tws_l2cap_rx_event_handle7uint8_t"></a>

<a id="_CPPv325tws_l2cap_rx_event_handle7uint8_t"></a> <a id="_CPPv225tws_l2cap_rx_event_handle7uint8_t"></a> <a id="tws_l2cap_rx_event_handle__uint8_t"></a> <a id="tws__private__cmd_8h_1ac76be2af7172825d68de47d03ac46c40"></a> void tws\_l2cap\_rx\_event\_handle(uint8\_t event)
:   handle rx tws private connection event

    tws private connection event callback function

    参数:
    :   **event** – **\[in\]** tws private connection event.

    返回:
    :   N/A

<a id="_CPPv420tws_private_cmd_initv"></a>

<a id="_CPPv320tws_private_cmd_initv"></a> <a id="_CPPv220tws_private_cmd_initv"></a> <a id="tws_private_cmd_init__void"></a> <a id="tws__private__cmd_8h_1a0851562a5f0533c5521de1d17333432d"></a> void tws\_private\_cmd\_init(void)
:   initialize tws private command

    tws private cmd init function

    返回:
    :   N/A

<a id="_CPPv427tws_carryout_pending_tx_cmdv"></a>

<a id="_CPPv327tws_carryout_pending_tx_cmdv"></a> <a id="_CPPv227tws_carryout_pending_tx_cmdv"></a> <a id="tws_carryout_pending_tx_cmd__void"></a> <a id="tws__private__cmd_8h_1a20249c4fb35ea3c59b811ee0dad4442e"></a> void tws\_carryout\_pending\_tx\_cmd(void)
:   carry out pending tx command

    carry out pending tx command

    返回:
    :   N/A **TWS\_PRIVATE\_CMD\_H** EOF

<a id="structures"></a>

### Structures

<a id="_CPPv46del_lk"></a>

<a id="_CPPv36del_lk"></a> <a id="_CPPv26del_lk"></a> <a id="del_lk"></a> <a id="structdel__lk"></a> struct del\_lk
:   Delete link key structure definition.

<a id="_CPPv49cmd_rsp_t"></a>

<a id="_CPPv39cmd_rsp_t"></a> <a id="_CPPv29cmd_rsp_t"></a> <a id="cmd_rsp_t"></a> <a id="structcmd__rsp__t"></a> struct cmd\_rsp\_t
:   Command response structure definition.

<a id="_CPPv420private_cmd_handle_t"></a>

<a id="_CPPv320private_cmd_handle_t"></a> <a id="_CPPv220private_cmd_handle_t"></a> <a id="private_cmd_handle_t"></a> <a id="structprivate__cmd__handle__t"></a> struct private\_cmd\_handle\_t
:   tws private command handle structure definition.

<a id="_CPPv48tws_tx_t"></a>

<a id="_CPPv38tws_tx_t"></a> <a id="_CPPv28tws_tx_t"></a> <a id="tws_tx_t"></a> <a id="structtws__tx__t"></a> struct tws\_tx\_t
:   tws tx structure definition.

<a id="_CPPv413tws_tx_data_t"></a>

<a id="_CPPv313tws_tx_data_t"></a> <a id="_CPPv213tws_tx_data_t"></a> <a id="tws_tx_data_t"></a> <a id="structtws__tx__data__t"></a> struct tws\_tx\_data\_t
:   tws tx data structure definition.

<a id="_CPPv413tws_rx_data_t"></a>

<a id="_CPPv313tws_rx_data_t"></a> <a id="_CPPv213tws_rx_data_t"></a> <a id="tws_rx_data_t"></a> <a id="structtws__rx__data__t"></a> struct tws\_rx\_data\_t
:   tws rx data structure definition.

<a id="macros"></a>

### Macros

<a id="c.NO_RSP_TIMEOUT"></a>

<a id="tws__private__cmd_8h_1a96c9867a9b99009c21ede11751bbd9d6"></a> NO\_RSP\_TIMEOUT

<a id="c.RSP_TIMEOUT"></a>

<a id="tws__private__cmd_8h_1aa8294dbcb1577ae5bf28db1b1dfb7374"></a> RSP\_TIMEOUT

<a id="c.RX_RSP_NULL"></a>

<a id="tws__private__cmd_8h_1a657254cdfa1533cf8c9b6f0b5dbb1078"></a> RX\_RSP\_NULL

<a id="c.RX_RSP_TO_NULL"></a>

<a id="tws__private__cmd_8h_1a8184d67dfb4c83020e15829e2ac9d3f4"></a> RX\_RSP\_TO\_NULL

<a id="c.RSP_CMD"></a>

<a id="tws__private__cmd_8h_1aecd132376665c5530d01b0014576f2c4"></a> RSP\_CMD

<a id="c.SHARE_INFO_CMD"></a>

<a id="tws__private__cmd_8h_1a782ecef8c6278b891245e141f42725cb"></a> SHARE\_INFO\_CMD

<a id="c.DEL_LINK_KEY"></a>

<a id="tws__private__cmd_8h_1ac28cfecb455f3fdd13ef824482d962a1"></a> DEL\_LINK\_KEY

<a id="c.TWS_HANDSHAKE_CMD"></a>

<a id="tws__private__cmd_8h_1abca14465f354a2e43007a9dd86051767"></a> TWS\_HANDSHAKE\_CMD

<a id="c.DISC_MOBILE_CMD"></a>

<a id="tws__private__cmd_8h_1a4a9df37da402cc2c2f130a65a57ba4dd"></a> DISC\_MOBILE\_CMD

<a id="c.MASTER_REQ_TSS"></a>

<a id="tws__private__cmd_8h_1a41c0ea7c08eabec673c6664363be5907"></a> MASTER\_REQ\_TSS

<a id="c.SLAVE_REQ_TSS"></a>

<a id="tws__private__cmd_8h_1acc4a6c697eefffd2aa3d27db5db3ebdc"></a> SLAVE\_REQ\_TSS

<a id="c.TWS_STOP_SNOOP"></a>

<a id="tws__private__cmd_8h_1a34ed01a35b1b89ac88452d883f072a98"></a> TWS\_STOP\_SNOOP

<a id="c.TWS_SYNC_PROFILE"></a>

<a id="tws__private__cmd_8h_1a58bc8e1ad888c6a9e9852de45559941a"></a> TWS\_SYNC\_PROFILE

<a id="c.TWS_SYNC_DONE"></a>

<a id="tws__private__cmd_8h_1a1f880e57bc5a514943416ca343e91b2c"></a> TWS\_SYNC\_DONE

<a id="c.TWS_SYNC_CMD_INFO"></a>

<a id="tws__private__cmd_8h_1aa11ed04403179d6c90e3fa1e798b64a5"></a> TWS\_SYNC\_CMD\_INFO

<a id="c.TWS_PLAYBACK_INFO"></a>

<a id="tws__private__cmd_8h_1ada80ba3543981faa6571fb8e981f08c8"></a> TWS\_PLAYBACK\_INFO

<a id="c.NOTIFY_SLAVE_OTA_RESULT"></a>

<a id="tws__private__cmd_8h_1a19f1289ac27b819d7ffdc99eb3d01973"></a> NOTIFY\_SLAVE\_OTA\_RESULT

<a id="c.TWS_ANC_CTRL"></a>

<a id="tws__private__cmd_8h_1a5e8cc885144849ae0f0ce30816a1f260"></a> TWS\_ANC\_CTRL

<a id="c.TWS_MASTER_REQ_CONNECT"></a>

<a id="tws__private__cmd_8h_1acfa6311ca7f73e6be086fdb5efebfc37"></a> TWS\_MASTER\_REQ\_CONNECT

<a id="c.TWS_CMD_DIRECT_SEND_START"></a>

<a id="tws__private__cmd_8h_1a641327046dea9bffe46cf67432e483c0"></a> TWS\_CMD\_DIRECT\_SEND\_START

<a id="c.TWS_SET_TRIGGER"></a>

<a id="tws__private__cmd_8h_1a538ead7f96767f1081db5336bf252bf4"></a> TWS\_SET\_TRIGGER

<a id="c.TWS_SET_RETRIGGER"></a>

<a id="tws__private__cmd_8h_1ae805a1601678c24612002236a8c17fc3"></a> TWS\_SET\_RETRIGGER

<a id="c.TWS_SET_A2DP_SCH"></a>

<a id="tws__private__cmd_8h_1a7bbfe511cdcf9b37dda9ce22c524d700"></a> TWS\_SET\_A2DP\_SCH

<a id="c.TWS_AUDIO_REJOIN"></a>

<a id="tws__private__cmd_8h_1a638d15334c4ee3ecc7010431fc66b468"></a> TWS\_AUDIO\_REJOIN

<a id="c.TWS_LOCAL_MEDIA_TRIGGER"></a>

<a id="tws__private__cmd_8h_1afa2eafcf0a7e6f23d487b5c233298c07"></a> TWS\_LOCAL\_MEDIA\_TRIGGER

<a id="c.TWS_AUDIO_JOIN_DIFF"></a>

<a id="tws__private__cmd_8h_1a18f5c80ef7f5ed558161f16c53379c1c"></a> TWS\_AUDIO\_JOIN\_DIFF

<a id="c.TWS_CMD_DIRECT_SEND_END"></a>

<a id="tws__private__cmd_8h_1a232a36aa663bacd8630a046134f3174e"></a> TWS\_CMD\_DIRECT\_SEND\_END

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv421private_cmd_rx_handle"></a>

<a id="_CPPv321private_cmd_rx_handle"></a> <a id="_CPPv221private_cmd_rx_handle"></a> <a id="private_cmd_rx_handle"></a> <a id="tws__private__cmd_8h_1a8ab7eb296396ac1b05186501e0fa0444"></a> typedef void (\*private\_cmd\_rx\_handle)(const uint8\_t \*p\_buff, uint16\_t length)
:   Handles rx tws private command function pointer definition.

<a id="_CPPv413private_cmd_t"></a>

<a id="_CPPv313private_cmd_t"></a> <a id="_CPPv213private_cmd_t"></a> <a id="private_cmd_t"></a> <a id="tws__private__cmd_8h_1ab6179dcb243d11cd7d7258e0741c0a80"></a> typedef uint16\_t private\_cmd\_t
:   tws private command type definition.
