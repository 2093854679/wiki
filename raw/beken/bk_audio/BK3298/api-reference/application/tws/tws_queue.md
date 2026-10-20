---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/tws/tws_queue.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="tws-queue-functions"></a>

# TWS Queue Functions

<a id="tws-queue-api-brief"></a>

## TWS\_QUEUE API Brief

| Application | Brief |
| --- | --- |
| [`tws_fsm_q_pop()`](#_CPPv413tws_fsm_q_popP15tws_fsm_q_env_tP13subfsm_info_t "tws_fsm_q_pop") | Pop FSM from queue |
| [`tws_fsm_q_insert()`](#_CPPv416tws_fsm_q_insertP15tws_fsm_q_env_tP13subfsm_info_t "tws_fsm_q_insert") | Insert FSM into queue |
| [`tws_fsm_q_get_front()`](#_CPPv419tws_fsm_q_get_frontP15tws_fsm_q_env_tP13subfsm_info_t "tws_fsm_q_get_front") | Get the FSM in front of the queue |
| [`tws_fsm_q_is_empty()`](#_CPPv418tws_fsm_q_is_emptyP15tws_fsm_q_env_t "tws_fsm_q_is_empty") | Check that the queue is empty |
| [`tws_fsm_is_duplicate_fsm()`](#_CPPv424tws_fsm_is_duplicate_fsmP15tws_fsm_q_env_tP13subfsm_info_t "tws_fsm_is_duplicate_fsm") | Check queue for duplicate FSM |
| [`tws_fsm_get_q()`](#_CPPv413tws_fsm_get_q12fsm_q_type_t "tws_fsm_get_q") | Get FSM queue environment parameter |
| [`tws_fsm_q_init()`](#_CPPv414tws_fsm_q_initv "tws_fsm_q_init") | Initialize FSM queue |

<a id="tws-queue-api-reference"></a>

## TWS\_QUEUE API Reference

<a id="header-file"></a>

### Header File

- [tws/tws\_ux/inc/tws\_queue.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/tws/tws_ux/inc/tws_queue.h)

<a id="functions"></a>

### Functions

<a id="_CPPv413tws_fsm_q_popP15tws_fsm_q_env_tP13subfsm_info_t"></a>

<a id="_CPPv313tws_fsm_q_popP15tws_fsm_q_env_tP13subfsm_info_t"></a> <a id="_CPPv213tws_fsm_q_popP15tws_fsm_q_env_tP13subfsm_info_t"></a> <a id="tws_fsm_q_pop__tws_fsm_q_env_tP.subfsm_info_tP"></a> <a id="tws__queue_8h_1a0165e58b5814afc5808082e0075ba826"></a> [tws\_q\_sts\_t](#_CPPv411tws_q_sts_t "tws_q_sts_t") tws\_fsm\_q\_pop([tws\_fsm\_q\_env\_t](#_CPPv415tws_fsm_q_env_t "tws_fsm_q_env_t") \*p\_fsm\_q, [subfsm\_info\_t](tws_sub_fsm.md#_CPPv413subfsm_info_t "subfsm_info_t") \*p\_fsm)
:   Pop FSM from queue.

    Pop FSM from the queue \[p\_fsm\_q\] to the \[p\_fsm\].

    参数:
    :   - **p\_fsm\_q** – **\[in\]** pointer to FSM queue of type [tws\_fsm\_q\_env\_t](#structtws__fsm__q__env__t).
        - **p\_fsm** – **\[in\]** pointer to sub FSM of type [subfsm\_info\_t](tws_sub_fsm.md#structsubfsm__info__t).

    返回:
    :   queue status of type tws\_q\_sts\_t

<a id="_CPPv416tws_fsm_q_insertP15tws_fsm_q_env_tP13subfsm_info_t"></a>

<a id="_CPPv316tws_fsm_q_insertP15tws_fsm_q_env_tP13subfsm_info_t"></a> <a id="_CPPv216tws_fsm_q_insertP15tws_fsm_q_env_tP13subfsm_info_t"></a> <a id="tws_fsm_q_insert__tws_fsm_q_env_tP.subfsm_info_tP"></a> <a id="tws__queue_8h_1acf6e8909ba2c6a5fdbef6e2f23f6532c"></a> [tws\_q\_sts\_t](#_CPPv411tws_q_sts_t "tws_q_sts_t") tws\_fsm\_q\_insert([tws\_fsm\_q\_env\_t](#_CPPv415tws_fsm_q_env_t "tws_fsm_q_env_t") \*p\_fsm\_q, [subfsm\_info\_t](tws_sub_fsm.md#_CPPv413subfsm_info_t "subfsm_info_t") \*p\_fsm)
:   Insert FSM into queue.

    Insert the FSM \[p\_fsm\] into queue \[p\_fsm\_q\].

    参数:
    :   - **p\_fsm\_q** – **\[in\]** pointer to FSM queue of type [tws\_fsm\_q\_env\_t](#structtws__fsm__q__env__t).
        - **p\_fsm** – **\[in\]** pointer to sub FSM of type [subfsm\_info\_t](tws_sub_fsm.md#structsubfsm__info__t).

    返回:
    :   queue status of type tws\_q\_sts\_t

<a id="_CPPv419tws_fsm_q_get_frontP15tws_fsm_q_env_tP13subfsm_info_t"></a>

<a id="_CPPv319tws_fsm_q_get_frontP15tws_fsm_q_env_tP13subfsm_info_t"></a> <a id="_CPPv219tws_fsm_q_get_frontP15tws_fsm_q_env_tP13subfsm_info_t"></a> <a id="tws_fsm_q_get_front__tws_fsm_q_env_tP.subfsm_info_tP"></a> <a id="tws__queue_8h_1af8a2041b1a74378be47f25c9c4ebca62"></a> [tws\_q\_sts\_t](#_CPPv411tws_q_sts_t "tws_q_sts_t") tws\_fsm\_q\_get\_front([tws\_fsm\_q\_env\_t](#_CPPv415tws_fsm_q_env_t "tws_fsm_q_env_t") \*p\_fsm\_q, [subfsm\_info\_t](tws_sub_fsm.md#_CPPv413subfsm_info_t "subfsm_info_t") \*p\_fsm)
:   Get the FSM in front of the queue.

    Get the FSM in front of queue \[p\_fsm\_q\] to the \[p\_fsm\].

    参数:
    :   - **p\_fsm\_q** – **\[in\]** pointer to FSM queue of type [tws\_fsm\_q\_env\_t](#structtws__fsm__q__env__t).
        - **p\_fsm** – **\[in\]** pointer to sub FSM queue of type [subfsm\_info\_t](tws_sub_fsm.md#structsubfsm__info__t).

    返回:
    :   queue status of type tws\_q\_sts\_t

<a id="_CPPv418tws_fsm_q_is_emptyP15tws_fsm_q_env_t"></a>

<a id="_CPPv318tws_fsm_q_is_emptyP15tws_fsm_q_env_t"></a> <a id="_CPPv218tws_fsm_q_is_emptyP15tws_fsm_q_env_t"></a> <a id="tws_fsm_q_is_empty__tws_fsm_q_env_tP"></a> <a id="tws__queue_8h_1a94eff72907d88234c03ecb44a55c0c6b"></a> bool tws\_fsm\_q\_is\_empty([tws\_fsm\_q\_env\_t](#_CPPv415tws_fsm_q_env_t "tws_fsm_q_env_t") \*p\_fsm\_q)
:   Check that the queue is empty.

    Check that the queue \[p\_fsm\_q\] is empty.

    参数:
    :   **p\_fsm\_q** – **\[in\]** pointer to FSM queue of type [tws\_fsm\_q\_env\_t](#structtws__fsm__q__env__t).

    返回值:
    :   - **true** – empty
        - **false** – not empty

    返回:
    :   result

<a id="_CPPv424tws_fsm_is_duplicate_fsmP15tws_fsm_q_env_tP13subfsm_info_t"></a>

<a id="_CPPv324tws_fsm_is_duplicate_fsmP15tws_fsm_q_env_tP13subfsm_info_t"></a> <a id="_CPPv224tws_fsm_is_duplicate_fsmP15tws_fsm_q_env_tP13subfsm_info_t"></a> <a id="tws_fsm_is_duplicate_fsm__tws_fsm_q_env_tP.subfsm_info_tP"></a> <a id="tws__queue_8h_1a15827d2e1320370a2314819b62c4092a"></a> bool tws\_fsm\_is\_duplicate\_fsm([tws\_fsm\_q\_env\_t](#_CPPv415tws_fsm_q_env_t "tws_fsm_q_env_t") \*p\_fsm\_q, [subfsm\_info\_t](tws_sub_fsm.md#_CPPv413subfsm_info_t "subfsm_info_t") \*p\_fsm)
:   Check queue for duplicate FSM.

    Check queue \[p\_fsm\_q\] for duplicate FSM \[p\_fsm\].

    参数:
    :   - **p\_fsm\_q** – **\[in\]** pointer to FSM queue of type [tws\_fsm\_q\_env\_t](#structtws__fsm__q__env__t).
        - **p\_fsm** – **\[in\]** pointer to sub FSM of type [subfsm\_info\_t](tws_sub_fsm.md#structsubfsm__info__t).

    返回值:
    :   - **true** – is duplicate
        - **false** – not duplicate

    返回:
    :   result

<a id="_CPPv413tws_fsm_get_q12fsm_q_type_t"></a>

<a id="_CPPv313tws_fsm_get_q12fsm_q_type_t"></a> <a id="_CPPv213tws_fsm_get_q12fsm_q_type_t"></a> <a id="tws_fsm_get_q__fsm_q_type_t"></a> <a id="tws__queue_8h_1a81c1d7dd68e7436e39e101450f5b0ed0"></a> [tws\_fsm\_q\_env\_t](#_CPPv415tws_fsm_q_env_t "tws_fsm_q_env_t") \*tws\_fsm\_get\_q([fsm\_q\_type\_t](#_CPPv412fsm_q_type_t "fsm_q_type_t") fsm\_q\_type)
:   Get FSM queue environment parameter.

    Get FSM queue environment parameter with type \[fsm\_q\_type\].

    参数:
    :   **fsm\_q\_type** – **\[in\]** FSM queue type of type fsm\_q\_type\_t

    返回:
    :   pointer to an FSM queue environment parameter of type [tws\_fsm\_q\_env\_t](#structtws__fsm__q__env__t).

<a id="_CPPv414tws_fsm_q_initv"></a>

<a id="_CPPv314tws_fsm_q_initv"></a> <a id="_CPPv214tws_fsm_q_initv"></a> <a id="tws_fsm_q_init__void"></a> <a id="tws__queue_8h_1a1cb8798b237054b1c58640f311a0856b"></a> void tws\_fsm\_q\_init(void)
:   Initialize FSM queue.

    Clean up the FSM queue.

    返回:
    :   N/A **TWS\_QUEUE\_H** EOF

<a id="structures"></a>

### Structures

<a id="_CPPv415tws_fsm_q_env_t"></a>

<a id="_CPPv315tws_fsm_q_env_t"></a> <a id="_CPPv215tws_fsm_q_env_t"></a> <a id="tws_fsm_q_env_t"></a> <a id="structtws__fsm__q__env__t"></a> struct tws\_fsm\_q\_env\_t
:   FSM environment parameters structure definition.

<a id="_CPPv411tws_fsm_q_t"></a>

<a id="_CPPv311tws_fsm_q_t"></a> <a id="_CPPv211tws_fsm_q_t"></a> <a id="tws_fsm_q_t"></a> <a id="structtws__fsm__q__t"></a> struct tws\_fsm\_q\_t
:   FSM queue structure definition.

<a id="macros"></a>

### Macros

<a id="c.MAX_FSM_Q_NUM"></a>

<a id="tws__queue_8h_1a76007561bf3c726776e525f21d8105b4"></a> MAX\_FSM\_Q\_NUM
:   Maximum number of FSM queues

<a id="c.TWS_Q_OK"></a>

<a id="tws__queue_8h_1aa56a6f373bcc66a564ed9a0698d9bf0b"></a> TWS\_Q\_OK

<a id="c.TWS_Q_ERROR"></a>

<a id="tws__queue_8h_1a8d5f12f4d4d59294d74248e37e12bd48"></a> TWS\_Q\_ERROR

<a id="c.TWS_Q_EMPTY"></a>

<a id="tws__queue_8h_1a408e4d057854bfaf801453c5aeff797c"></a> TWS\_Q\_EMPTY

<a id="c.TWS_Q_FULL"></a>

<a id="tws__queue_8h_1abc97eee74f76c9b67b73b9d2ea51b22b"></a> TWS\_Q\_FULL

<a id="c.TWS_FSM_Q_HIGH"></a>

<a id="tws__queue_8h_1a9368ef852340f1e0cfd11d5b89b96fec"></a> TWS\_FSM\_Q\_HIGH

<a id="c.TWS_FSM_Q_NORMAL"></a>

<a id="tws__queue_8h_1a34a24b1bad488390a4f792789e004827"></a> TWS\_FSM\_Q\_NORMAL

<a id="c.TWS_FSM_Q_LOW"></a>

<a id="tws__queue_8h_1a3b8311fe328f1f11a3e7d28caa3565da"></a> TWS\_FSM\_Q\_LOW

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv411tws_q_sts_t"></a>

<a id="_CPPv311tws_q_sts_t"></a> <a id="_CPPv211tws_q_sts_t"></a> <a id="tws_q_sts_t"></a> <a id="tws__queue_8h_1afe521bb4abeb44bedffcc3d73c332e7e"></a> typedef uint8\_t tws\_q\_sts\_t
:   TWS queue status type definition.

<a id="_CPPv412fsm_q_type_t"></a>

<a id="_CPPv312fsm_q_type_t"></a> <a id="_CPPv212fsm_q_type_t"></a> <a id="fsm_q_type_t"></a> <a id="tws__queue_8h_1aff29cc144aea310f003a24735a9193d4"></a> typedef uint8\_t fsm\_q\_type\_t
:   FSM queue type definition.
