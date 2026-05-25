# Timer[](#timer "永久链接至标题")

[[English]](../../../../en/v1.5/api-reference/peripheral/bk_timer.html "../../../../en/v1.5/api-reference/peripheral/bk_timer.html")


## Timer API Status[](#timer-api-status "永久链接至标题")

| API | BK7235A | BK7235B | BK7235 |
| --- | --- | --- | --- |
| [`bk_timer_driver_init()`](#_CPPv420bk_timer_driver_initv "bk_timer_driver_init") | Y | Y | Y |
| [`bk_timer_driver_deinit()`](#_CPPv422bk_timer_driver_deinitv "bk_timer_driver_deinit") | Y | Y | Y |
| [`bk_timer_start()`](#_CPPv414bk_timer_start10timer_id_t8uint32_t11timer_isr_t "bk_timer_start") | Y | Y | Y |
| [`bk_timer_stop()`](#_CPPv413bk_timer_stop10timer_id_t "bk_timer_stop") | Y | Y | Y |
| [`bk_timer_get_cnt()`](#_CPPv416bk_timer_get_cnt10timer_id_t "bk_timer_get_cnt") | Y | Y | Y |
| [`bk_timer_enable()`](#_CPPv415bk_timer_enable10timer_id_t "bk_timer_enable") | Y | Y | Y |
| [`bk_timer_disable()`](#_CPPv416bk_timer_disable10timer_id_t "bk_timer_disable") | Y | Y | Y |
| [`bk_timer_get_period()`](#_CPPv419bk_timer_get_period10timer_id_t "bk_timer_get_period") | Y | Y | Y |


## Timer API Reference[](#timer-api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [timer.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/timer.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/timer.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_timer_driver_init(void)[](#_CPPv420bk_timer_driver_initv "永久链接至目标")
:   Init the timer driver.

    This API init the resoure common to all timer channels:


    - Init timer driver control memory

    This API should be called before any other timer APIs.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_timer_driver_deinit(void)[](#_CPPv422bk_timer_driver_deinitv "永久链接至目标")
:   Deinit the timer driver.

    This API free all resource related to timer and power down all timer channels.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_timer_start([timer_id_t](#_CPPv410timer_id_t "timer_id_t") timer_id, uint32_t time_ms, [timer_isr_t](#_CPPv411timer_isr_t "timer_isr_t") callback)[](#_CPPv414bk_timer_start10timer_id_t8uint32_t11timer_isr_t "永久链接至目标")
:   Start the timer.


    **Attention**
    :   1. timer2 has been used for time cali

        2. timer3 has been used for clock, but bk7271 use timer1

        3. bk7271 has used timer0(10ms)

    参数
    :   - **timer_id** – the timer ID to be started

        - **time_ms** – time delay value of the timer

        - **callback** – the timer call back function

    返回
    :   - BK_OK: succeed

        - BK_ERR_TIMER_NOT_INIT: timer driver not init

        - BK_ERR_TIMER_ID: timer id is invalid

        - BK_ERR_TIMER_IS_RUNNING: timer id is running

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_timer_start_without_callback([timer_id_t](#_CPPv410timer_id_t "timer_id_t") timer_id, uint32_t time_ms)[](#_CPPv431bk_timer_start_without_callback10timer_id_t8uint32_t "永久链接至目标")
:   Start the timer without set callback.

    参数
    :   - **timer_id** – the timer ID to be started

        - **timer_ms** – time delay value of the timer

    返回
    :   - BK_OK: succeed

        - others: others errors

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_timer_stop([timer_id_t](#_CPPv410timer_id_t "timer_id_t") timer_id)[](#_CPPv413bk_timer_stop10timer_id_t "永久链接至目标")
:   Stop the timer.

    参数
    :   **timer_id** – the timer ID to be stoped

    返回
    :   - BK_OK: succeed

        - others: other errors.

uint32_t bk_timer_get_cnt([timer_id_t](#_CPPv410timer_id_t "timer_id_t") timer_id)[](#_CPPv416bk_timer_get_cnt10timer_id_t "永久链接至目标")
:   Get the current counter value.


    **Attention**
    :   1. The caller need to make sure the parameter timer_id is correct!

    参数
    :   **timer_id** – the timer id

    返回
    :   counter value

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_timer_enable([timer_id_t](#_CPPv410timer_id_t "timer_id_t") timer_id)[](#_CPPv415bk_timer_enable10timer_id_t "永久链接至目标")
:   Enable the timer.

    参数
    :   **timer_id** – the timer ID

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_timer_disable([timer_id_t](#_CPPv410timer_id_t "timer_id_t") timer_id)[](#_CPPv416bk_timer_disable10timer_id_t "永久链接至目标")
:   Disable the timer.

    参数
    :   **timer_id** – the timer ID

    返回
    :   - BK_OK: succeed

        - others: other errors.

uint32_t bk_timer_get_period([timer_id_t](#_CPPv410timer_id_t "timer_id_t") timer_id)[](#_CPPv419bk_timer_get_period10timer_id_t "永久链接至目标")
:   Get the counter value set by [bk_timer_start()](#group__bk__api__timer_1gafd8412ab7d4698fde8a944c39551c749 "#group__bk__api__timer_1gafd8412ab7d4698fde8a944c39551c749")

    参数
    :   **timer_id** – the timer id

    返回
    :   counter value set by [bk_timer_start()](#group__bk__api__timer_1gafd8412ab7d4698fde8a944c39551c749 "#group__bk__api__timer_1gafd8412ab7d4698fde8a944c39551c749")

uint32_t bk_timer_get_enable_status(void)[](#_CPPv426bk_timer_get_enable_statusv "永久链接至目标")
:   Get the timer enable status.

    参数
    :   **timer_id** – the timer id

    返回
    :   timer enable status

bool bk_timer_is_interrupt_triggered([timer_id_t](#_CPPv410timer_id_t "timer_id_t") timer_id)[](#_CPPv431bk_timer_is_interrupt_triggered10timer_id_t "永久链接至目标")
:   Get whether the timer interrupt triggered.

    参数
    :   **timer_id** – the timer id

    返回
    :   the timer interrupt status

uint64_t bk_timer_get_time([timer_id_t](#_CPPv410timer_id_t "timer_id_t") timer_id, uint32_t div, uint32_t last_count, [timer_value_unit_t](#_CPPv418timer_value_unit_t "timer_value_unit_t") unit_type)[](#_CPPv417bk_timer_get_time10timer_id_t8uint32_t8uint32_t18timer_value_unit_t "永久链接至目标")
:   Get the timer count value in ms or us.

    参数
    :   - **timer_id** – the timer id

        - **div** – the divider of clock frequency

        - **last_count** – last count of the timer

        - **timer_value_unit_t** – the time unit, ms or us

    返回
    :   the timer value in micro seconds

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_timer_delay_with_callback([timer_id_t](#_CPPv410timer_id_t "timer_id_t") timer_id, uint64_t time_us, [timer_isr_t](#_CPPv411timer_isr_t "timer_isr_t") callback)[](#_CPPv428bk_timer_delay_with_callback10timer_id_t8uint64_t11timer_isr_t "永久链接至目标")
:   This function set the delay based on the current running counter, which is different from bk_timer_start.

    参数
    :   - **timer_id** – the timer id

        - **time_us** – time delay value of the timer by us

        - **callback** – the timer delay call back function

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_timer_cancel([timer_id_t](#_CPPv410timer_id_t "timer_id_t") timer_id)[](#_CPPv415bk_timer_cancel10timer_id_t "永久链接至目标")
:   Cancel the timer delay task, reset timer and set ISR to NULL, it will not disable the timer, which is different from bk_timer_stop.

    参数
    :   **timer_id** – the timer id

    返回
    :   - BK_OK: succeed

        - others: other errors.


## Timer API Typedefs[](#timer-api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [timer_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/timer_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/timer_types.h")


### Macros[](#macros "永久链接至标题")

BK_ERR_TIMER_ID[](#c.BK_ERR_TIMER_ID "永久链接至目标")
:   timer id is invalid

BK_ERR_TIMER_NOT_INIT[](#c.BK_ERR_TIMER_NOT_INIT "永久链接至目标")
:   timer driver not init

BK_ERR_TIMER_IS_RUNNING[](#c.BK_ERR_TIMER_IS_RUNNING "永久链接至目标")
:   timer id is running

BK_ERR_TIMER_ID_ON_DEFCONFIG[](#c.BK_ERR_TIMER_ID_ON_DEFCONFIG "永久链接至目标")
:   timer id is error


### Type Definitions[](#type-definitions "永久链接至标题")

typedef void (*timer_isr_t)([timer_id_t](#_CPPv410timer_id_t "timer_id_t") timer_id)[](#_CPPv411timer_isr_t "永久链接至目标")
:   Timer interrupt service routine.


### Header File[](#id2 "永久链接至标题")


- [hal/hal_timer_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hal/hal_timer_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hal/hal_timer_types.h")


### Macros[](#id3 "永久链接至标题")

TIMER_CLOCK_FREQ_26M[](#c.TIMER_CLOCK_FREQ_26M "永久链接至目标")

TIMER_CLOCK_FREQ_32K[](#c.TIMER_CLOCK_FREQ_32K "永久链接至目标")


### Type Definitions[](#id4 "永久链接至标题")

typedef uint8_t timer_unit_t[](#_CPPv412timer_unit_t "永久链接至目标")
:   Timer uint id


### Enumerations[](#enumerations "永久链接至标题")

enum timer_src_clk_t[](#_CPPv415timer_src_clk_t "永久链接至目标")
:   *Values:*

    enumerator TIMER_SCLK_CLK32[](#_CPPv4N15timer_src_clk_t16TIMER_SCLK_CLK32E "永久链接至目标")
    :   TIMER source clock dco

    enumerator TIMER_SCLK_XTAL[](#_CPPv4N15timer_src_clk_t15TIMER_SCLK_XTALE "永久链接至目标")
    :   TIMER source clock xtal 26M

enum sys_sel_timer_t[](#_CPPv415sys_sel_timer_t "永久链接至目标")
:   *Values:*

    enumerator SYS_SEL_TIMER0[](#_CPPv4N15sys_sel_timer_t14SYS_SEL_TIMER0E "永久链接至目标")

    enumerator SYS_SEL_TIMER1[](#_CPPv4N15sys_sel_timer_t14SYS_SEL_TIMER1E "永久链接至目标")

enum timer_id_t[](#_CPPv410timer_id_t "永久链接至目标")
:   *Values:*

    enumerator TIMER_ID0[](#_CPPv4N10timer_id_t9TIMER_ID0E "永久链接至目标")
    :   TIMER id 0

    enumerator TIMER_ID1[](#_CPPv4N10timer_id_t9TIMER_ID1E "永久链接至目标")
    :   TIMER id 1

    enumerator TIMER_ID2[](#_CPPv4N10timer_id_t9TIMER_ID2E "永久链接至目标")
    :   TIMER id 2

    enumerator TIMER_ID3[](#_CPPv4N10timer_id_t9TIMER_ID3E "永久链接至目标")
    :   TIMER id 3

    enumerator TIMER_ID4[](#_CPPv4N10timer_id_t9TIMER_ID4E "永久链接至目标")
    :   TIMER id 4

    enumerator TIMER_ID5[](#_CPPv4N10timer_id_t9TIMER_ID5E "永久链接至目标")
    :   TIMER id 5

    enumerator TIMER_ID_MAX[](#_CPPv4N10timer_id_t12TIMER_ID_MAXE "永久链接至目标")
    :   TIMER id max

enum timer_value_unit_t[](#_CPPv418timer_value_unit_t "永久链接至目标")
:   *Values:*

    enumerator TIMER_UNIT_MS[](#_CPPv4N18timer_value_unit_t13TIMER_UNIT_MSE "永久链接至目标")
    :   TIMER unit type is ms

    enumerator TIMER_UNIT_US[](#_CPPv4N18timer_value_unit_t13TIMER_UNIT_USE "永久链接至目标")
    :   TIMER unit type is us
