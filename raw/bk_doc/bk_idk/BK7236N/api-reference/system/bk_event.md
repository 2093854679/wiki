# 事件机制[](#id1 "永久链接至标题")

[[English]](../../../../en/v2.2.1/api-reference/system/bk_event.html "../../../../en/v2.2.1/api-reference/system/bk_event.html")


## Header File[](#header-file "永久链接至标题")


- [event.h](https://github.com/bekencorp/armino/blob/main/components/event.h "https://github.com/bekencorp/armino/blob/main/components/event.h")


## Functions[](#functions "永久链接至标题")

[bk_err_t](os.html#_CPPv48bk_err_t "bk_err_t") bk_event_register_cb([event_module_t](#_CPPv414event_module_t "event_module_t") event_module_id, int event_id, [event_cb_t](#_CPPv410event_cb_t "event_cb_t") event_cb, void *event_cb_arg)[](#_CPPv420bk_event_register_cb14event_module_ti10event_cb_tPv "永久链接至目标")
:   Register event callback.

    参数
    :   - **event_module_id** – the module ID of the event to register the callback for

        - **event_id** – the id of the event to register the callback for

        - **event_cb** – the callback which gets called when the event is dispatched

        - **event_cb_arg** – data, aside from event data, that is passed to the handler when it is called

    返回
    :   - BK_OK: succeed

        - BK_ERR_EVENT_NOT_INIT: the event module is not initialized

        - BK_ERR_EVENT_MOD_OR_ID: the event module ID or event ID is invalid

        - BK_ERR_EVENT_NO_MEM: out of memory

        - BK_ERR_EVENT_INIT_SEM: failed to init the internal event semaphore

        - BK_ERR_EVENT_POST_QUEUE: failed to post the event to event queue

        - BK_ERR_EVENT_CB_EXIST: the event callback already unregistered

        - Others: Fail

[bk_err_t](os.html#_CPPv48bk_err_t "bk_err_t") bk_event_unregister_cb([event_module_t](#_CPPv414event_module_t "event_module_t") event_module_id, int event_id, [event_cb_t](#_CPPv410event_cb_t "event_cb_t") event_cb)[](#_CPPv422bk_event_unregister_cb14event_module_ti10event_cb_t "永久链接至目标")
:   Unregister a callback.

    This function can be used to unregister a callback so that it no longer gets called during dispatch.

    参数
    :   - **event_module_id** – the ID of the module with which to unregister the callback

        - **event_id** – the ID of the event with which to unregister the callback

        - **event_cb** – the callback to be unregistered

    返回
    :   - BK_OK: Success

        - BK_ERR_EVENT_NOT_INIT: the event module is not initialized

        - BK_ERR_EVENT_MOD_OR_ID: the event module ID or event ID is invalid

        - BK_ERR_EVENT_NO_MEM: out of memory

        - BK_ERR_EVENT_INIT_SEM: failed to init the internal event semaphore

        - BK_ERR_EVENT_POST_QUEUE: failed to post the event to event queue

        - BK_ERR_EVENT_NO_CB: the event callback already unregistered

        - Others: Fail

[bk_err_t](os.html#_CPPv48bk_err_t "bk_err_t") bk_event_post([event_module_t](#_CPPv414event_module_t "event_module_t") event_module_id, int event_id, void *event_data, size_t event_data_size, uint32_t timeout)[](#_CPPv413bk_event_post14event_module_tiPv6size_t8uint32_t "永久链接至目标")
:   Posts an event to the event task.

    参数
    :   - **event_module_id** – The ID of the module that generates the event

        - **event_id** – the event id that identifies the event

        - **event_data** – the data, specific to the event occurence, that gets passed to the callback

        - **event_data_size** – the size of the event data

        - **timeout** – number of milliseconds to block on a full event queue

    返回
    :   - BK_OK: Success

        - BK_ERR_EVENT_NOT_INIT: the event module is not initialized

        - BK_ERR_EVENT_MOD_OR_ID: the event module ID or event ID is not invalid

        - BK_ERR_EVENT_NO_MEM: out of memory

        - BK_ERR_EVENT_INIT_SEM: failed to init the internal event semaphore

        - BK_ERR_EVENT_POST_QUEUE: failed to post the event to event queue

        - Others: Fail

[bk_err_t](os.html#_CPPv48bk_err_t "bk_err_t") bk_event_init(void)[](#_CPPv413bk_event_initv "永久链接至目标")
:   Init the event module.

    This API initializes the event queue and create the event task.

    This API should be called before any event API is called, generally it should be called before WiFi/BLE is initialized.

    返回
    :   - BK_OK: succeed

        - BK_ERR_EVENT_CREATE_QUEUE: failed to create event queue

        - BK_ERR_EVENT_CREATE_TASK: failed to create event task

        - Others: Fail

[bk_err_t](os.html#_CPPv48bk_err_t "bk_err_t") bk_event_deinit(void)[](#_CPPv415bk_event_deinitv "永久链接至目标")
:   Deinit the event module.

    This API destroy the event queue and delete the event task.

    返回
    :   - BK_OK: succeed

        - BK_ERR_NO_MEM: out of memory

        - Others: Fail

[bk_err_t](os.html#_CPPv48bk_err_t "bk_err_t") bk_event_dump(void)[](#_CPPv413bk_event_dumpv "永久链接至目标")
:   Dump all registered event callback.


    **Attention**
    :   This API is for debug only

    返回
    :   - BK_OK: succeed

        - BK_ERR_NO_MEM: out of memory

        - Others: Fail


## Macros[](#macros "永久链接至标题")

BK_ERR_EVENT_MOD[](#c.BK_ERR_EVENT_MOD "永久链接至目标")
:   Event module is not supported

BK_ERR_EVENT_ID[](#c.BK_ERR_EVENT_ID "永久链接至目标")
:   Event ID is not supported

BK_ERR_EVENT_MOD_OR_ID[](#c.BK_ERR_EVENT_MOD_OR_ID "永久链接至目标")
:   Event ID or Module is invalid

BK_ERR_EVENT_CB_EXIST[](#c.BK_ERR_EVENT_CB_EXIST "永久链接至目标")
:   Event cb already registered

BK_ERR_EVENT_NO_CB[](#c.BK_ERR_EVENT_NO_CB "永久链接至目标")
:   No event cb is registered

BK_ERR_EVENT_CREATE_QUEUE[](#c.BK_ERR_EVENT_CREATE_QUEUE "永久链接至目标")
:   Failed to create event message queue

BK_ERR_EVENT_CREATE_MUTEX[](#c.BK_ERR_EVENT_CREATE_MUTEX "永久链接至目标")
:   Failed to create event mutex

BK_ERR_EVENT_CREATE_TASK[](#c.BK_ERR_EVENT_CREATE_TASK "永久链接至目标")
:   Failed to create event task

BK_ERR_EVENT_NULL_MSG[](#c.BK_ERR_EVENT_NULL_MSG "永久链接至目标")
:   Event message is NULL

BK_ERR_EVENT_INIT_SEM[](#c.BK_ERR_EVENT_INIT_SEM "永久链接至目标")
:   Failed to init RTOS semaphore

BK_ERR_EVENT_NOT_INIT[](#c.BK_ERR_EVENT_NOT_INIT "永久链接至目标")
:   Event module not init

BK_ERR_EVENT_POST_QUEUE[](#c.BK_ERR_EVENT_POST_QUEUE "永久链接至目标")
:   Failed to post event request to event queue

BK_ERR_EVENT_UNKNOWN_MSG[](#c.BK_ERR_EVENT_UNKNOWN_MSG "永久链接至目标")
:   Not supported event message

EVENT_ID_ALL[](#c.EVENT_ID_ALL "永久链接至目标")
:   All events in a event module


## Type Definitions[](#type-definitions "永久链接至标题")

typedef [bk_err_t](os.html#_CPPv48bk_err_t "bk_err_t") (*event_cb_t)(void *arg, [event_module_t](#_CPPv414event_module_t "event_module_t") event_module, int event_id, void *event_data)[](#_CPPv410event_cb_t "永久链接至目标")
:   Event callback.

    The event callback get called when related event dispatched.

typedef [bk_err_t](os.html#_CPPv48bk_err_t "bk_err_t") (*event_callback_t)(void *arg, [event_module_t](#_CPPv414event_module_t "event_module_t") event_module, int event_id, void *event_data)[](#_CPPv416event_callback_t "永久链接至目标")


## Enumerations[](#enumerations "永久链接至标题")

enum event_module_t[](#_CPPv414event_module_t "永久链接至目标")
:   *Values:*

    enumerator EVENT_MOD_WIFI_INTERNAL[](#_CPPv4N14event_module_t23EVENT_MOD_WIFI_INTERNALE "永久链接至目标")
    :   WiFi internal event

    enumerator EVENT_MOD_WIFI[](#_CPPv4N14event_module_t14EVENT_MOD_WIFIE "永久链接至目标")
    :   WiFi public event

    enumerator EVENT_MOD_NETIF[](#_CPPv4N14event_module_t15EVENT_MOD_NETIFE "永久链接至目标")
    :   Netif event

    enumerator EVENT_MOD_COUNT[](#_CPPv4N14event_module_t15EVENT_MOD_COUNTE "永久链接至目标")
    :   Event module count
