# Mailbox[](#mailbox "永久链接至标题")


## Mailbox API Status[](#mailbox-api-status "永久链接至标题")

| API | BK7236N |
| --- | --- |
| [`bk_mailbox_init()`](#_CPPv415bk_mailbox_initv "bk_mailbox_init") | N |
| [`bk_mailbox_deinit()`](#_CPPv417bk_mailbox_deinitv "bk_mailbox_deinit") | N |
| [`bk_mailbox_set_param()`](#_CPPv420bk_mailbox_set_paramP14mailbox_data_t8uint32_t8uint32_t8uint32_t8uint32_t "bk_mailbox_set_param") | N |
| [`bk_mailbox_recv_callback_register()`](#_CPPv433bk_mailbox_recv_callback_register18mailbox_endpoint_t18mailbox_endpoint_t18mailbox_callback_t "bk_mailbox_recv_callback_register") | N |
| [`bk_mailbox_recv_callback_unregister()`](#_CPPv435bk_mailbox_recv_callback_unregister18mailbox_endpoint_t18mailbox_endpoint_t "bk_mailbox_recv_callback_unregister") | N |
| [`bk_mailbox_send()`](#_CPPv415bk_mailbox_sendP14mailbox_data_t18mailbox_endpoint_t18mailbox_endpoint_tPv "bk_mailbox_send") | N |


## Mailbox UNIT Number[](#mailbox-unit-number "永久链接至标题")

| Capability | BK7236N |
| --- | --- |
| UNIT Number | 2 |


## Mailbox API Reference[](#mailbox-api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [mailbox.h](https://github.com/bekencorp/armino/blob/main/components/mailbox.h "https://github.com/bekencorp/armino/blob/main/components/mailbox.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_mailbox_init(void)[](#_CPPv415bk_mailbox_initv "永久链接至目标")
:   Init the MAILBOX driver.

    This API init the resoure common to all MAILBOXs:


    - Init MAILBOX driver control register

    - Configure MAILBOX interrupt handling function

    This API should be called before any other MAILBOX APIs.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_mailbox_deinit(void)[](#_CPPv417bk_mailbox_deinitv "永久链接至目标")
:   Deinit the MAILBOX driver.

    This API free all resource related to MAILBOX.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_mailbox_set_param([mailbox_data_t](#_CPPv414mailbox_data_t "mailbox_data_t") *data, uint32_t p0, uint32_t p1, uint32_t p2, uint32_t p3)[](#_CPPv420bk_mailbox_set_paramP14mailbox_data_t8uint32_t8uint32_t8uint32_t8uint32_t "永久链接至目标")
:   Configure the MAILBOX cmd and data.

    This API is used to configure data. Write parameters to variables as required by the structure, [mailbox_data_t](#structmailbox__data__t "#structmailbox__data__t").

    example: [mailbox_data_t](#structmailbox__data__t "#structmailbox__data__t") send_data; uint32_t param0 = 123456; uint32_t param1 = 111; uint32_t param2 = 666; uint32_t param3 = 888; mailbox_set_param(&send_data, param0, param1, param2, param3);

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_mailbox_recv_callback_register([mailbox_endpoint_t](#_CPPv418mailbox_endpoint_t "mailbox_endpoint_t") src, [mailbox_endpoint_t](#_CPPv418mailbox_endpoint_t "mailbox_endpoint_t") dst, [mailbox_callback_t](#_CPPv418mailbox_callback_t "mailbox_callback_t") callback)[](#_CPPv433bk_mailbox_recv_callback_register18mailbox_endpoint_t18mailbox_endpoint_t18mailbox_callback_t "永久链接至目标")
:   Register the callback function for MAILBOX.


    **Attention**
    :   src : Associated with the CPU that needs to send data dst : Associated with the CPU of the current code execution system callback: After receiving the data, it is transmitted to the correspongding processing function. example: The current code runs in CPU0 and receives data from CPU1.

        ```
           src = MAILBOX_CPU1;
           dst = MAILBOX_CPU0;
           callback = receive_from_CPU_1;
        ```

    返回
    :   - BK_OK: succeed

        - BK_ERR_MAILBOX_SRC_DST: MAILBOX data transmission direction error

        - BK_ERR_MAILBOX_CALLBACK: Insufficient space or wrong format of registered function, etc

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_mailbox_recv_callback_unregister([mailbox_endpoint_t](#_CPPv418mailbox_endpoint_t "mailbox_endpoint_t") src, [mailbox_endpoint_t](#_CPPv418mailbox_endpoint_t "mailbox_endpoint_t") dst)[](#_CPPv435bk_mailbox_recv_callback_unregister18mailbox_endpoint_t18mailbox_endpoint_t "永久链接至目标")
:   Unregister the callback function for MAILBOX.


    **Attention**
    :   src : Associated with the CPU that needs to send data dst : Associated with the CPU of the current code execution system callback: After receiving the data, it is transmitted to the correspongding processing function. example: The current code runs in CPU0 and receives data from CPU1.

        ```
           src = MAILBOX_CPU1
           dst = MAILBOX_CPU0
        ```

    返回
    :   - BK_OK: succeed

        - BK_ERR_MAILBOX_SRC_DST: MAILBOX data transmission direction error.

        - BK_ERR_MAILBOX_CALLBACK: Callback function is not registered.

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_mailbox_send([mailbox_data_t](#_CPPv414mailbox_data_t "mailbox_data_t") *data, [mailbox_endpoint_t](#_CPPv418mailbox_endpoint_t "mailbox_endpoint_t") src, [mailbox_endpoint_t](#_CPPv418mailbox_endpoint_t "mailbox_endpoint_t") dst, void *arg)[](#_CPPv415bk_mailbox_sendP14mailbox_data_t18mailbox_endpoint_t18mailbox_endpoint_tPv "永久链接至目标")
:   Unregister the callback function for MAILBOX.

    example: The current code runs in CPU0 and send data to CPU1.

    ```
       src = MAILBOX_ENDPOINT_CPU0
       dst = MAILBOX_CPU1
       data : mbx ('by mailbox_set_param(&mbx, p0, p1, p2, p3)')
    ```


    **Attention**
    :   Before sending data, need to use the mailbox_set_param() to configure the data format.

    返回
    :   - BK_OK: succeed

        - BK_ERR_MAILBOX_SRC_DST: MAILBOX data transmission direction error.

        - BK_ERR_MAILBOX_BOX: No empty box store data.

        - BK_ERR_MAILBOX_TIMEOUT: Timeout waiting for the opposite end to fetch data.

        - others: other errors.


## Mailbox Typedefs[](#mailbox-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [mailbox_types.h](https://github.com/bekencorp/armino/blob/main/components/mailbox_types.h "https://github.com/bekencorp/armino/blob/main/components/mailbox_types.h")


### Structures[](#structures "永久链接至标题")

struct mailbox_data_t[](#_CPPv414mailbox_data_t "永久链接至目标")
:   A MAILBOX has multiple boxes, one box has four spaces to fill in data Define the meaning of each space by user.

    ```
         |_____________________________|      |_____________________________|
         |_____________________________|      |_____________________________|
         | Mailbox0                    |      | Mailbox1                    |
         |______________|______________|      |______________|______________|
         |     box0     |     box1     |      |     box0     |     box1     |
         | ____________ | ____________ |      | ____________ | ____________ |
         | | param0   | | | param0   | |      | | param0   | | | param0   | |
         | | param1   | | | param1   | |      | | param1   | | | param1   | |
         | | param2   | | | param2   | |      | | param2   | | | param2   | |
         | | param3   | | | param3   | |      | | param3   | | | param3   | |
         | |__________| | |__________| |      | |__________| | |__________| |
         | _____________|______________|      |______________|______________|
         |_____________________________|      |_____________________________|
    ```

    Public Members

    uint32_t param0[](#_CPPv4N14mailbox_data_t6param0E "永久链接至目标")
    :   MAILBOX Space 0

    uint32_t param1[](#_CPPv4N14mailbox_data_t6param1E "永久链接至目标")
    :   MAILBOX Space 1

    uint32_t param2[](#_CPPv4N14mailbox_data_t6param2E "永久链接至目标")
    :   MAILBOX Space 2

    uint32_t param3[](#_CPPv4N14mailbox_data_t6param3E "永久链接至目标")
    :   MAILBOX Space 3


### Macros[](#macros "永久链接至标题")

BK_ERR_MAILBOX_SRC_DST[](#c.BK_ERR_MAILBOX_SRC_DST "永久链接至目标")
:   MAILBOX source address error

BK_ERR_MAILBOX_ID[](#c.BK_ERR_MAILBOX_ID "永久链接至目标")
:   MAILBOX BOX number error

BK_ERR_MAILBOX_FLAG[](#c.BK_ERR_MAILBOX_FLAG "永久链接至目标")
:   MAILBOX flag error

BK_ERR_MAILBOX_CALLBACK[](#c.BK_ERR_MAILBOX_CALLBACK "永久链接至目标")
:   MAILBOX callback function error

BK_ERR_MAILBOX_TIMEOUT[](#c.BK_ERR_MAILBOX_TIMEOUT "永久链接至目标")
:   MAILBOX waite timeout

BK_ERR_MAILBOX_NOT_INIT[](#c.BK_ERR_MAILBOX_NOT_INIT "永久链接至目标")
:   MAILBOX isnt init

BK_ERR_MAILBOX_REPEAT_INIT[](#c.BK_ERR_MAILBOX_REPEAT_INIT "永久链接至目标")
:   MAILBOX repeat init


### Type Definitions[](#type-definitions "永久链接至标题")

typedef void (*mailbox_callback_t)([mailbox_data_t](#_CPPv414mailbox_data_t "mailbox_data_t") *data)[](#_CPPv418mailbox_callback_t "永久链接至目标")
:   MAILBOX interrupt service routine.


### Enumerations[](#enumerations "永久链接至标题")

enum mailbox_endpoint_t[](#_CPPv418mailbox_endpoint_t "永久链接至目标")
:   *Values:*

    enumerator MAILBOX_CPU0[](#_CPPv4N18mailbox_endpoint_t12MAILBOX_CPU0E "永久链接至目标")
    :   MAILBOX CPU0 endpoint

    enumerator MAILBOX_CPU1[](#_CPPv4N18mailbox_endpoint_t12MAILBOX_CPU1E "永久链接至目标")
    :   MAILBOX CPU1 endpoint

    enumerator MAILBOX_CPU2[](#_CPPv4N18mailbox_endpoint_t12MAILBOX_CPU2E "永久链接至目标")
    :   MAILBOX CPU2 endpoint

    enumerator MAILBOX_DSP[](#_CPPv4N18mailbox_endpoint_t11MAILBOX_DSPE "永久链接至目标")
    :   MAILBOX DSP endpoint

    enumerator MAILBOX_BT[](#_CPPv4N18mailbox_endpoint_t10MAILBOX_BTE "永久链接至目标")
    :   MAILBOX BT endpoint

    enumerator MAILBOX_ENDPOINT_INVALID[](#_CPPv4N18mailbox_endpoint_t24MAILBOX_ENDPOINT_INVALIDE "永久链接至目标")
    :   MAILBOX invalid endpoint


### Header File[](#id2 "永久链接至标题")


- [hal/hal_mailbox_types.h](https://github.com/bekencorp/armino/blob/main/components/hal/hal_mailbox_types.h "https://github.com/bekencorp/armino/blob/main/components/hal/hal_mailbox_types.h")


### Type Definitions[](#id3 "永久链接至标题")

typedef uint32_t mailbox_id_t[](#_CPPv412mailbox_id_t "永久链接至目标")

typedef uint32_t mailbox_ep_config_t[](#_CPPv419mailbox_ep_config_t "永久链接至目标")
