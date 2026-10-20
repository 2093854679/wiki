---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_thread/app_task.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="task-application-functions"></a>

# Task Application Functions

<a id="app-task-api-brief"></a>

## APP\_TASK API Brief

| Application | Brief |
| --- | --- |
| [`app_task_init()`](#_CPPv413app_task_initv "app_task_init") | app task thread create |
| [`app_task_send_msg()`](#_CPPv417app_task_send_msg14app_msg_type_t8uint16_tPv8uint32_t8uint32_t "app_task_send_msg") | send message to app\_msg\_q |
| [`app_task_register_task_cb_handler()`](#_CPPv433app_task_register_task_cb_handlerP21app_task_cb_handler_t "app_task_register_task_cb_handler") | app task call back register |

<a id="app-task-api-reference"></a>

## APP\_TASK API Reference

<a id="header-file"></a>

### Header File

- [common/app\_thread/app\_task.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_thread/app_task.h)

<a id="functions"></a>

### Functions

<a id="_CPPv413app_task_initv"></a>

<a id="_CPPv313app_task_initv"></a> <a id="_CPPv213app_task_initv"></a> <a id="app_task_init__void"></a> <a id="app__task_8h_1a515a442c049b2e137fbfa1633cbb3719"></a> void app\_task\_init(void)
:   app\_task\_init brief description

    application task inititial

    返回:
    :   N/A

<a id="_CPPv417app_task_send_msg14app_msg_type_t8uint16_tPv8uint32_t8uint32_t"></a>

<a id="_CPPv317app_task_send_msg14app_msg_type_t8uint16_tPv8uint32_t8uint32_t"></a> <a id="_CPPv217app_task_send_msg14app_msg_type_t8uint16_tPv8uint32_t8uint32_t"></a> <a id="app_task_send_msg__app_msg_type_t.uint16_t.voidP.uint32_t.uint32_t"></a> <a id="app__task_8h_1a5c52121567fd1a111c7d65c6dad3d4a7"></a> int32\_t app\_task\_send\_msg([app\_msg\_type\_t](#_CPPv414app_msg_type_t "app_msg_type_t") msg\_type, uint16\_t sub\_type, void \*p\_hdl, uint32\_t arg1, uint32\_t arg2)
:   app\_task\_send\_msg brief description

    Send application message to app\_task

    参数:
    :   - **msg\_type** – **\[in\]** message type see@app\_msg\_type\_t
        - **sub\_type** – **\[in\]** Sub type that is defined in the application module
        - **p\_hdl** – **\[in\]** pointer to data buffer which pass to specific module
        - **arg1** – **\[in\]** argument\_1 which pass to specific module
        - **arg2** – **\[in\]** argument\_2 which pass to specific module

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv433app_task_register_task_cb_handlerP21app_task_cb_handler_t"></a>

<a id="_CPPv333app_task_register_task_cb_handlerP21app_task_cb_handler_t"></a> <a id="_CPPv233app_task_register_task_cb_handlerP21app_task_cb_handler_t"></a> <a id="app_task_register_task_cb_handler__app_task_cb_handler_tP"></a> <a id="app__task_8h_1aca88a6f74c87e63e2102baa894eed0d9"></a> int32\_t app\_task\_register\_task\_cb\_handler([app\_task\_cb\_handler\_t](#_CPPv421app_task_cb_handler_t "app_task_cb_handler_t") \*p\_cb\_handler)
:   app\_task\_register\_task\_cb\_handler brief description

    Register application module callback handler that process to the app task.

    参数:
    :   **p\_cb\_handler** – **\[in\]** dedicated module task handler

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv413app_msg_env_t"></a>

<a id="_CPPv313app_msg_env_t"></a> <a id="_CPPv213app_msg_env_t"></a> <a id="app_msg_env_t"></a> <a id="structapp__msg__env__t"></a> struct app\_msg\_env\_t
:   application task message struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N13app_msg_env_t8msg_typeE"></a>

    <a id="_CPPv3N13app_msg_env_t8msg_typeE"></a> <a id="_CPPv2N13app_msg_env_t8msg_typeE"></a> <a id="app_msg_env_t::msg_type__app_msg_type_t"></a> <a id="structapp__msg__env__t_1a34957ef8c9663df60b57ec987b9d9413"></a> [app\_msg\_type\_t](#_CPPv414app_msg_type_t "app_msg_type_t") msg\_type
    :   message index of modules @app\_msg\_type\_t

    <a id="_CPPv4N13app_msg_env_t8sub_typeE"></a>

    <a id="_CPPv3N13app_msg_env_t8sub_typeE"></a> <a id="_CPPv2N13app_msg_env_t8sub_typeE"></a> <a id="app_msg_env_t::sub_type__uint16_t"></a> <a id="structapp__msg__env__t_1a40ad13258e216eb55242dea981c5bd67"></a> uint16\_t sub\_type
    :   sub message event types

    <a id="_CPPv4N13app_msg_env_t5p_hdlE"></a>

    <a id="_CPPv3N13app_msg_env_t5p_hdlE"></a> <a id="_CPPv2N13app_msg_env_t5p_hdlE"></a> <a id="app_msg_env_t::p_hdl__voidP"></a> <a id="structapp__msg__env__t_1a92a4e2b0dabd676cc33de271c481f0cc"></a> void \*p\_hdl
    :   pointer to data buffer which pass to specific module

    <a id="_CPPv4N13app_msg_env_t4arg1E"></a>

    <a id="_CPPv3N13app_msg_env_t4arg1E"></a> <a id="_CPPv2N13app_msg_env_t4arg1E"></a> <a id="app_msg_env_t::arg1__uint32_t"></a> <a id="structapp__msg__env__t_1a500345699c10cd6a53f24e4f6089b1a1"></a> uint32\_t arg1
    :   argument\_1 which pass to specific module

    <a id="_CPPv4N13app_msg_env_t4arg2E"></a>

    <a id="_CPPv3N13app_msg_env_t4arg2E"></a> <a id="_CPPv2N13app_msg_env_t4arg2E"></a> <a id="app_msg_env_t::arg2__uint32_t"></a> <a id="structapp__msg__env__t_1a8d59762fc1f4154b5fe89666d6ecde48"></a> uint32\_t arg2
    :   argument\_2 which pass to specific module

<a id="_CPPv421app_task_cb_handler_t"></a>

<a id="_CPPv321app_task_cb_handler_t"></a> <a id="_CPPv221app_task_cb_handler_t"></a> <a id="app_task_cb_handler_t"></a> <a id="structapp__task__cb__handler__t"></a> struct app\_task\_cb\_handler\_t
:   module task handler struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N21app_task_cb_handler_t9dlst_nodeE"></a>

    <a id="_CPPv3N21app_task_cb_handler_t9dlst_nodeE"></a> <a id="_CPPv2N21app_task_cb_handler_t9dlst_nodeE"></a> <a id="app_task_cb_handler_t::dlst_node__dl_list_t"></a> <a id="structapp__task__cb__handler__t_1a53ae693539aeb6f69c75c3dd110cb845"></a> dl\_list\_t dlst\_node
    :   node for appliction handler will be linked with others

    <a id="_CPPv4N21app_task_cb_handler_t8msg_typeE"></a>

    <a id="_CPPv3N21app_task_cb_handler_t8msg_typeE"></a> <a id="_CPPv2N21app_task_cb_handler_t8msg_typeE"></a> <a id="app_task_cb_handler_t::msg_type__app_msg_type_t"></a> <a id="structapp__task__cb__handler__t_1a408240aa53eec42522ecbebf89f177eb"></a> [app\_msg\_type\_t](#_CPPv414app_msg_type_t "app_msg_type_t") msg\_type
    :   message index of modules @app\_msg\_type\_t

    <a id="_CPPv4N21app_task_cb_handler_t8callbackE"></a>

    <a id="_CPPv3N21app_task_cb_handler_t8callbackE"></a> <a id="_CPPv2N21app_task_cb_handler_t8callbackE"></a> <a id="app_task_cb_handler_t::callback__app_task_cb_handler_pfn"></a> <a id="structapp__task__cb__handler__t_1a7962d4fad44406afc4601f8f8fa6fba5"></a> [app\_task\_cb\_handler\_pfn](#_CPPv423app_task_cb_handler_pfn "app_task_cb_handler_pfn") callback
    :   function pointer for callback function

<a id="macros"></a>

### Macros

<a id="c.APP_MSG_BUTTON"></a>

<a id="app__task_8h_1aef82a0a68d426ae84d27e7cc00dcbbf1"></a> APP\_MSG\_BUTTON

<a id="c.APP_MSG_LED"></a>

<a id="app__task_8h_1aedea1976cc46cf9586523aa1218714d0"></a> APP\_MSG\_LED

<a id="c.APP_MSG_BT"></a>

<a id="app__task_8h_1a36d974e9c3e86aaaa72a74d1481da9b2"></a> APP\_MSG\_BT

<a id="c.APP_MSG_BLE"></a>

<a id="app__task_8h_1a54c022c60a1d41d9015d3cad6d717a65"></a> APP\_MSG\_BLE

<a id="c.APP_FLASH_WR_DONE_MSG"></a>

<a id="app__task_8h_1a72d6482fd9959297ff9c3a5a33d6418e"></a> APP\_FLASH\_WR\_DONE\_MSG

<a id="c.APP_MSG_DLP"></a>

<a id="app__task_8h_1a28f053a4bf95a0b21630c3cee4cfd495"></a> APP\_MSG\_DLP

<a id="c.APP_MSG_UART_LOG_RX"></a>

<a id="app__task_8h_1adb2e7e3f6c28bae08e5e1b41dcc45c76"></a> APP\_MSG\_UART\_LOG\_RX

<a id="c.APP_MSG_AURACAST_SRC"></a>

<a id="app__task_8h_1a06192eca66838c40d7610297cd5d3179"></a> APP\_MSG\_AURACAST\_SRC

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv414app_msg_type_t"></a>

<a id="_CPPv314app_msg_type_t"></a> <a id="_CPPv214app_msg_type_t"></a> <a id="app_msg_type_t"></a> <a id="app__task_8h_1a4655d38ba9c967311091f86c796dd3a7"></a> typedef uint8\_t app\_msg\_type\_t
:   application task message definition

<a id="_CPPv423app_task_cb_handler_pfn"></a>

<a id="_CPPv323app_task_cb_handler_pfn"></a> <a id="_CPPv223app_task_cb_handler_pfn"></a> <a id="app_task_cb_handler_pfn"></a> <a id="app__task_8h_1a6a3f64a9f4386d91bb3555b87cf48edb"></a> typedef void (\*app\_task\_cb\_handler\_pfn)(uint16\_t msg\_type, void \*p\_hdl, uint32\_t arg1, uint32\_t arg2)
