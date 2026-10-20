---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/tws/tws_trpc.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="tws-trpc-functions"></a>

# TWS TRPC Functions

<a id="tws-trpc-api-brief"></a>

## TWS\_TRPC API Brief

| Application | Brief |
| --- | --- |
| [`tws_trpc_send()`](#_CPPv413tws_trpc_sendP8uint32_t "tws_trpc_send") | Send RPC message to TWS task |
| [`tws_trpc_exec()`](#_CPPv413tws_trpc_execP8uint32_t "tws_trpc_exec") | Implement RPC function in TWS task |

<a id="tws-trpc-api-reference"></a>

## TWS\_TRPC API Reference

<a id="header-file"></a>

### Header File

- [tws/tws\_ux/inc/tws\_trpc.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/tws/tws_ux/inc/tws_trpc.h)

<a id="functions"></a>

### Functions

<a id="_CPPv413tws_trpc_sendP8uint32_t"></a>

<a id="_CPPv313tws_trpc_sendP8uint32_t"></a> <a id="_CPPv213tws_trpc_sendP8uint32_t"></a> <a id="tws_trpc_send__uint32_tP"></a> <a id="tws__trpc_8h_1a54a004a764ba3a2825895c4d04a16ac9"></a> void tws\_trpc\_send(uint32\_t \*pu4\_blk)
:   Send RPC message to TWS task.

    Send the RPC message \[pu4\_blk\] to TWS task.

    参数:
    :   **pu4\_blk** – **\[in\]** pointer to RPC message

    返回:
    :   N/A

<a id="_CPPv413tws_trpc_execP8uint32_t"></a>

<a id="_CPPv313tws_trpc_execP8uint32_t"></a> <a id="_CPPv213tws_trpc_execP8uint32_t"></a> <a id="tws_trpc_exec__uint32_tP"></a> <a id="tws__trpc_8h_1a49b17386080ddcd4986fbe918d6a1598"></a> void tws\_trpc\_exec(uint32\_t \*pu4\_blk)
:   Implement RPC function in TWS task.

    Implement the function of RPC message \[pu4\_blk\] in the TWS task.

    参数:
    :   **pu4\_blk** – **\[in\]** pointer to RPC message

    返回:
    :   N/A **TWS\_TRPC\_H** EOF

<a id="macros"></a>

### Macros

<a id="c.TWS_TRPC_0ARG"></a>

<a id="tws__trpc_8h_1a400de3551e58ae56c1f1c2610fa8594f"></a> TWS\_TRPC\_0ARG(ret\_type, ret\_val, func)

<a id="c.TWS_TRPC_0ARG_RET_VOID"></a>

<a id="tws__trpc_8h_1aecf8600da7bd165995245564253040b3"></a> TWS\_TRPC\_0ARG\_RET\_VOID(func)

<a id="c.TWS_TRPC_1ARG"></a>

<a id="tws__trpc_8h_1a14607eb54bcc8cb8b88d12415c785f12"></a> TWS\_TRPC\_1ARG(ret\_type, ret\_val, func, a1)
:   tws task RPC with 0 argument.

    tws task RPC blocking call with 0 argument, blocking call, the function will not return until it is actually executed.

    参数:
    :   - **ret\_type** – **\[in\]** the return type of func(next argument)
        - **func** – **\[in\]** rpc function to be called

    返回:
    :   value depends on ret\_type, return nothing when ret\_type\=void

<a id="c.TWS_TRPC_1ARG_RET_VOID"></a>

<a id="tws__trpc_8h_1a2b685a59d2a73d17dbf970437796f415"></a> TWS\_TRPC\_1ARG\_RET\_VOID(func, a1)

<a id="c.TWS_TRPC_2ARG"></a>

<a id="tws__trpc_8h_1ab67308ef78536348dd843a0553b6dc38"></a> TWS\_TRPC\_2ARG(ret\_type, ret\_val, func, a1, a2)

<a id="c.TWS_TRPC_2ARG_RET_VOID"></a>

<a id="tws__trpc_8h_1ab9816a99fa21d729780ff78f88b1ab80"></a> TWS\_TRPC\_2ARG\_RET\_VOID(func, a1, a2)

<a id="c.TWS_TRPC_3ARG"></a>

<a id="tws__trpc_8h_1a7bb0aa082b57edf1198184ce3d452f69"></a> TWS\_TRPC\_3ARG(ret\_type, ret\_val, func, a1, a2, a3)

<a id="c.TWS_TRPC_3ARG_RET_VOID"></a>

<a id="tws__trpc_8h_1ad994a70a0da91ff09c60a79bbc9b33f1"></a> TWS\_TRPC\_3ARG\_RET\_VOID(func, a1, a2, a3)

<a id="c.TWS_TRPC_4ARG"></a>

<a id="tws__trpc_8h_1a51560ad65c1149590ca289956e4b7e2d"></a> TWS\_TRPC\_4ARG(ret\_type, ret\_val, func, a1, a2, a3, a4)

<a id="c.TWS_TRPC_5ARG"></a>

<a id="tws__trpc_8h_1a6f5f374a5bad717303522e66fb8c7a78"></a> TWS\_TRPC\_5ARG(ret\_type, ret\_val, func, a1, a2, a3, a4, a5)

<a id="c.TWS_TRPC_6ARG"></a>

<a id="tws__trpc_8h_1a55d59f0b1a5c2a28094d4a8fcf29a039"></a> TWS\_TRPC\_6ARG(ret\_type, ret\_val, func, a1, a2, a3, a4, a5, a6)

<a id="c.TWS_TRPC_ASYNC_0ARG_RET_VOID"></a>

<a id="tws__trpc_8h_1af86ffbbab11c440da300d244a48667c9"></a> TWS\_TRPC\_ASYNC\_0ARG\_RET\_VOID(func)
:   tws stack RPC RPC async with 0 arguments.

    tws stack RPC RPC non-blocking call with 0 arguments, non-blocking call, the result of the function execution can be obtained via res\_cb.

    参数:
    :   - **func** – **\[in\]** rpc function to be called

    返回:
    :   N/A

<a id="c.TWS_TRPC_ASYNC_1ARG_RET_VOID"></a>

<a id="tws__trpc_8h_1a964fa8ab0b787ef3d6649cf4b0391286"></a> TWS\_TRPC\_ASYNC\_1ARG\_RET\_VOID(func, a1)

<a id="c.TWS_TRPC_ASYNC_2ARG"></a>

<a id="tws__trpc_8h_1abc7ba3543c3af558401a5f13379671c7"></a> TWS\_TRPC\_ASYNC\_2ARG(func, a1, a2)

<a id="c.TWS_TRPC_ASYNC_3ARG_RET_VOID"></a>

<a id="tws__trpc_8h_1a26eed27b1305127985ca4cb73deccf88"></a> TWS\_TRPC\_ASYNC\_3ARG\_RET\_VOID(func, a1, a2, a3)

<a id="c.TWS_TRPC_ASYNC_4ARG_RET_VOID"></a>

<a id="tws__trpc_8h_1ac9bd44658b8cf8d85cf78fdc1fb4bf8d"></a> TWS\_TRPC\_ASYNC\_4ARG\_RET\_VOID(func, a1, a2, a3, a4)

<a id="c.TWS_TRPC_ASYNC_5ARG_RET_VOID"></a>

<a id="tws__trpc_8h_1a190902f02c3d2142887c326eb522e2cb"></a> TWS\_TRPC\_ASYNC\_5ARG\_RET\_VOID(func, a1, a2, a3, a4, a5)

<a id="c.TWS_TRPC_ASYNC_6ARG_RET_VOID"></a>

<a id="tws__trpc_8h_1a93ad4ed4360e0822f10dd5480ac26aa3"></a> TWS\_TRPC\_ASYNC\_6ARG\_RET\_VOID(func, a1, a2, a3, a4, a5, a6)
