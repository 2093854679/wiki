---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/tws/tws_task.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="tws-task-functions"></a>

# TWS Task Functions

<a id="tws-task-api-brief"></a>

## TWS\_TASK API Brief

| Application | Brief |
| --- | --- |
| [`tws_task_send_msg()`](#_CPPv417tws_task_send_msgPv14tws_msg_type_t8uint32_t "tws_task_send_msg") | Send message to TWS task |
| [`tws_task_get_handle()`](#_CPPv419tws_task_get_handlev "tws_task_get_handle") | Get TWS task handle |
| [`tws_init()`](#_CPPv48tws_initP13tws_ux_info_t "tws_init") | Initialize TWS task |

<a id="tws-task-api-reference"></a>

## TWS\_TASK API Reference

<a id="header-file"></a>

### Header File

- [tws/tws\_ux/inc/tws\_task.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/tws/tws_ux/inc/tws_task.h)

<a id="functions"></a>

### Functions

<a id="_CPPv417tws_task_send_msgPv14tws_msg_type_t8uint32_t"></a>

<a id="_CPPv317tws_task_send_msgPv14tws_msg_type_t8uint32_t"></a> <a id="_CPPv217tws_task_send_msgPv14tws_msg_type_t8uint32_t"></a> <a id="tws_task_send_msg__voidP.tws_msg_type_t.uint32_t"></a> <a id="tws__task_8h_1a6872313892a5e0df3db2eef708d445c5"></a> int32\_t tws\_task\_send\_msg(void \*p\_buff, [tws\_msg\_type\_t](#_CPPv414tws_msg_type_t "tws_msg_type_t") msg\_type, uint32\_t msg\_len)
:   Send message to TWS task.

    Send the message data \[p\_buff\] to the TWS task by osi\_msgq\_send().

    参数:
    :   - **p\_buff** – **\[in\]** pointer to message data
        - **msg\_type** – **\[in\]** message type of type tws\_msg\_type\_t
        - **msg\_len** – **\[in\]** message length

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419tws_task_get_handlev"></a>

<a id="_CPPv319tws_task_get_handlev"></a> <a id="_CPPv219tws_task_get_handlev"></a> <a id="tws_task_get_handle__void"></a> <a id="tws__task_8h_1a493c8ca77c277ee00e4064a60f41f1f7"></a> uint32\_t tws\_task\_get\_handle(void)
:   Get TWS task handle.

    Get the TWS task thread handle returned by osi\_thread\_create().

    返回值:
    :   - **0** – fail
        - **other** – success

    返回:
    :   thread handle

<a id="_CPPv48tws_initP13tws_ux_info_t"></a>

<a id="_CPPv38tws_initP13tws_ux_info_t"></a> <a id="_CPPv28tws_initP13tws_ux_info_t"></a> <a id="tws_init__tws_ux_info_tP"></a> <a id="tws__task_8h_1a922fc72e036752f8b93838949e60cc59"></a> void tws\_init([tws\_ux\_info\_t](../../btif/btif_type.md#_CPPv413tws_ux_info_t "tws_ux_info_t") \*p\_tws\_ux\_info)
:   Initialize TWS task.

    Create a TWS task and set the task parameters to \[p\_tws\_ux\_info\].

    参数:
    :   **p\_tws\_ux\_info** – **\[in\]** pointer to TWS information of type [tws\_ux\_info\_t](../../btif/btif_type.md#structtws__ux__info__t).

    返回:
    :   N/A **TWS\_THREAD\_H** EOF

<a id="structures"></a>

### Structures

<a id="_CPPv49tws_msg_t"></a>

<a id="_CPPv39tws_msg_t"></a> <a id="_CPPv29tws_msg_t"></a> <a id="tws_msg_t"></a> <a id="structtws__msg__t"></a> struct tws\_msg\_t
:   TWS message structure definition.

<a id="_CPPv413tws_msg_tbl_t"></a>

<a id="_CPPv313tws_msg_tbl_t"></a> <a id="_CPPv213tws_msg_tbl_t"></a> <a id="tws_msg_tbl_t"></a> <a id="structtws__msg__tbl__t"></a> struct tws\_msg\_tbl\_t
:   TWS message table structure definition.

<a id="macros"></a>

### Macros

<a id="c.TWS_MSG_START"></a>

<a id="tws__task_8h_1a1628a3ed677ce3317c6415c82420217f"></a> TWS\_MSG\_START

<a id="c.TX_TWS_DATA_MSG"></a>

<a id="tws__task_8h_1aa96f111b8e452f645b1d9a45f767ce2b"></a> TX\_TWS\_DATA\_MSG

<a id="c.RX_TWS_DATA_MSG"></a>

<a id="tws__task_8h_1a9442fcfd0cf14ae824c9d00bdee08517"></a> RX\_TWS\_DATA\_MSG

<a id="c.TWS_FSM_GEN_MSG"></a>

<a id="tws__task_8h_1ac9eaf443cc4a340585795b00bba01c96"></a> TWS\_FSM\_GEN\_MSG

<a id="c.TWS_RPC_MSG"></a>

<a id="tws__task_8h_1ae1912f506136c749035348a6f0848590"></a> TWS\_RPC\_MSG

<a id="c.TWS_TX_PENDING_MSG"></a>

<a id="tws__task_8h_1a31755ffa71184075a96e84ff5385ebbd"></a> TWS\_TX\_PENDING\_MSG

<a id="c.TWS_TEST_MSG"></a>

<a id="tws__task_8h_1acb13acd9957c9238e4492c2834f92430"></a> TWS\_TEST\_MSG

<a id="c.TWS_RX_HOST_EVT"></a>

<a id="tws__task_8h_1a449d477791eedb93e499dbd6f5ec8182"></a> TWS\_RX\_HOST\_EVT

<a id="c.TWS_MSG_END"></a>

<a id="tws__task_8h_1a3d1444fbb6b1194b0f056aa57df2548a"></a> TWS\_MSG\_END

<a id="c.IS_VALID_TWS_MSG"></a>

<a id="tws__task_8h_1a216110b17f8205a65d460ec293732683"></a> IS\_VALID\_TWS\_MSG(msg)
:   Check that the TWS message is valid macro.

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv414tws_msg_type_t"></a>

<a id="_CPPv314tws_msg_type_t"></a> <a id="_CPPv214tws_msg_type_t"></a> <a id="tws_msg_type_t"></a> <a id="tws__task_8h_1acb0f2ffed343acc07fbd1b1bd13c7d36"></a> typedef uint32\_t tws\_msg\_type\_t
:   TWS message type definition.

<a id="_CPPv420tws_task_msg_handler"></a>

<a id="_CPPv320tws_task_msg_handler"></a> <a id="_CPPv220tws_task_msg_handler"></a> <a id="tws_task_msg_handler"></a> <a id="tws__task_8h_1a9042043b507be15c10de4c9849f0b22f"></a> typedef void (\*tws\_task\_msg\_handler)([tws\_msg\_t](#_CPPv49tws_msg_t "tws_msg_t") \*p\_msg)
:   Handle TWS task message function pointer definition.
