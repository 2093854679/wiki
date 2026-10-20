---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/api-reference/peripheral/gpio.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="gpio-api"></a>

# GPIO API

GPIO (General Purpose Input/Output) 通用输入输出API接口。

<a id="header-file"></a>

## Header File

- [gpio.h](https://github.com/bekencorp/armino/blob/main/components/gpio.h)

<a id="functions"></a>

## Functions

<a id="_CPPv419bk_gpio_driver_initv"></a>

<a id="_CPPv319bk_gpio_driver_initv"></a> <a id="_CPPv219bk_gpio_driver_initv"></a> <a id="bk_gpio_driver_init__void"></a> <a id="group__bk__api__gpio_1gacae1346ccd48c98d892fe82d0473cfde"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_driver\_init(void)
:   Init the GPIO driver.

    This API init the resoure common to all GPIO channels:

    - Init GPIO driver control memory

    This API should be called before any other GPIO APIs.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_gpio_driver_deinitv"></a>

<a id="_CPPv321bk_gpio_driver_deinitv"></a> <a id="_CPPv221bk_gpio_driver_deinitv"></a> <a id="bk_gpio_driver_deinit__void"></a> <a id="group__bk__api__gpio_1ga1f1b3f85bc530c7bd4179fdcc3fb5868"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_driver\_deinit(void)
:   Deinit the GPIO driver.

    This API free all resource related to GPIO and power down all GPIO channels.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv417bk_gpio_set_value9gpio_id_t8uint32_t"></a>

<a id="_CPPv317bk_gpio_set_value9gpio_id_t8uint32_t"></a> <a id="_CPPv217bk_gpio_set_value9gpio_id_t8uint32_t"></a> <a id="bk_gpio_set_value__gpio_id_t.uint32_t"></a> <a id="group__bk__api__gpio_1gafca019ef63ca760b3764e97462c0585b"></a> void bk\_gpio\_set\_value(gpio\_id\_t id, uint32\_t v)
:   Direct set GPIO config value.

    @NOTES Please be care to use this API,unless you know the detail mean, because it will set the GPIO config value. Sometimes the special GPIO needs to re-used by one more owner, after the second owner re-used it, it should restore the config value. Before re-use a GPIO, the owner can call bk\_gpio\_get\_value and bakup it, after re-used finish, it call bk\_gpio\_set\_value to restore the prevous value.

<a id="_CPPv417bk_gpio_get_value9gpio_id_t"></a>

<a id="_CPPv317bk_gpio_get_value9gpio_id_t"></a> <a id="_CPPv217bk_gpio_get_value9gpio_id_t"></a> <a id="bk_gpio_get_value__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga21130dd4b1f24b16e8526226438f9b31"></a> uint32\_t bk\_gpio\_get\_value(gpio\_id\_t id)
:   get GPIO config value.

<a id="_CPPv421bk_gpio_enable_output9gpio_id_t"></a>

<a id="_CPPv321bk_gpio_enable_output9gpio_id_t"></a> <a id="_CPPv221bk_gpio_enable_output9gpio_id_t"></a> <a id="bk_gpio_enable_output__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga2973cb2479aaf6bbfe2efebd84d3985d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_enable\_output(gpio\_id\_t gpio\_id)
:   enable GPIO output mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - others: other errors.

<a id="_CPPv422bk_gpio_disable_output9gpio_id_t"></a>

<a id="_CPPv322bk_gpio_disable_output9gpio_id_t"></a> <a id="_CPPv222bk_gpio_disable_output9gpio_id_t"></a> <a id="bk_gpio_disable_output__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga2e177c4285dd8673b446bcd15db92126"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_disable\_output(gpio\_id\_t gpio\_id)
:   disable GPIO output mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - others: other errors.

<a id="_CPPv420bk_gpio_enable_input9gpio_id_t"></a>

<a id="_CPPv320bk_gpio_enable_input9gpio_id_t"></a> <a id="_CPPv220bk_gpio_enable_input9gpio_id_t"></a> <a id="bk_gpio_enable_input__gpio_id_t"></a> <a id="group__bk__api__gpio_1gaf9acdf13c743f920174bbb103f108ac7"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_enable\_input(gpio\_id\_t gpio\_id)
:   enable GPIO input mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - others: other errors.

<a id="_CPPv421bk_gpio_disable_input9gpio_id_t"></a>

<a id="_CPPv321bk_gpio_disable_input9gpio_id_t"></a> <a id="_CPPv221bk_gpio_disable_input9gpio_id_t"></a> <a id="bk_gpio_disable_input__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga200faf135f7d18061fc1c4057bd48b6f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_disable\_input(gpio\_id\_t gpio\_id)
:   disable GPIO input mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - others: other errors.

<a id="_CPPv419bk_gpio_enable_pull9gpio_id_t"></a>

<a id="_CPPv319bk_gpio_enable_pull9gpio_id_t"></a> <a id="_CPPv219bk_gpio_enable_pull9gpio_id_t"></a> <a id="bk_gpio_enable_pull__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga231a1940364f61c699d2d4fba643a743"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_enable\_pull(gpio\_id\_t gpio\_id)
:   enable GPIO pull mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - others: other errors.

<a id="_CPPv420bk_gpio_disable_pull9gpio_id_t"></a>

<a id="_CPPv320bk_gpio_disable_pull9gpio_id_t"></a> <a id="_CPPv220bk_gpio_disable_pull9gpio_id_t"></a> <a id="bk_gpio_disable_pull__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga044f2ca367852a0ae8f85f9440db08f8"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_disable\_pull(gpio\_id\_t gpio\_id)
:   disable gpio pull mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - others: other errors.

<a id="_CPPv415bk_gpio_pull_up9gpio_id_t"></a>

<a id="_CPPv315bk_gpio_pull_up9gpio_id_t"></a> <a id="_CPPv215bk_gpio_pull_up9gpio_id_t"></a> <a id="bk_gpio_pull_up__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga8d974991d0a7d561eda8bd14c9bfc3b5"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_pull\_up(gpio\_id\_t gpio\_id)
:   set GPIO as pull up mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - others: other errors.

<a id="_CPPv417bk_gpio_pull_down9gpio_id_t"></a>

<a id="_CPPv317bk_gpio_pull_down9gpio_id_t"></a> <a id="_CPPv217bk_gpio_pull_down9gpio_id_t"></a> <a id="bk_gpio_pull_down__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga206cf499bae8f2d5b7057f8d3f3f21fe"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_pull\_down(gpio\_id\_t gpio\_id)
:   set GPIO as pull down mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - others: other errors.

<a id="_CPPv418bk_gpio_set_config9gpio_id_tPK13gpio_config_t"></a>

<a id="_CPPv318bk_gpio_set_config9gpio_id_tPK13gpio_config_t"></a> <a id="_CPPv218bk_gpio_set_config9gpio_id_tPK13gpio_config_t"></a> <a id="bk_gpio_set_config__gpio_id_t.gpio_config_tCP"></a> <a id="group__bk__api__gpio_1gabc229ebbc3ae486f8538789a61491bc7"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_set\_config(gpio\_id\_t gpio\_id, const gpio\_config\_t \*config)
:   Config the GPIO mode.

    This API config GPIO’s mode

    - BK\_OK: succeed
    - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
    - BK\_ERR\_GPIO\_INVALID\_MODE: invalid GPIO’s io\_mode/pull\_mode
    - BK\_ERR\_GPIO\_INTERNAL\_USED:GPIO was map to another device
    - others: other errors.

<a id="_CPPv423bk_gpio_set_output_high9gpio_id_t"></a>

<a id="_CPPv323bk_gpio_set_output_high9gpio_id_t"></a> <a id="_CPPv223bk_gpio_set_output_high9gpio_id_t"></a> <a id="bk_gpio_set_output_high__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga6813699d36a76f6ed87e72c6f90a0592"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_set\_output\_high(gpio\_id\_t gpio\_id)
:   Set the GPIO output high,.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - BK\_ERR\_GPIO\_NOT\_OUTPUT\_MODE:GPIO not in output mode
        - others: other errors.

<a id="_CPPv422bk_gpio_set_output_low9gpio_id_t"></a>

<a id="_CPPv322bk_gpio_set_output_low9gpio_id_t"></a> <a id="_CPPv222bk_gpio_set_output_low9gpio_id_t"></a> <a id="bk_gpio_set_output_low__gpio_id_t"></a> <a id="group__bk__api__gpio_1gad53b1f39990fd6d6d051b75b0424dd9c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_set\_output\_low(gpio\_id\_t gpio\_id)
:   Set the GPIO output low,.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - BK\_ERR\_GPIO\_NOT\_OUTPUT\_MODE:GPIO not in output mode
        - others: other errors.

<a id="_CPPv417bk_gpio_get_input9gpio_id_t"></a>

<a id="_CPPv317bk_gpio_get_input9gpio_id_t"></a> <a id="_CPPv217bk_gpio_get_input9gpio_id_t"></a> <a id="bk_gpio_get_input__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga71b4f9272a2c8bc27d906f2de602bce2"></a> bool bk\_gpio\_get\_input(gpio\_id\_t gpio\_id)
:   Get the GPIO input value,.

    This API get GPIO’s input level: 0 :low\_level 1:high\_level.

    返回
    :   - input value
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - BK\_ERR\_GPIO\_NOT\_INPUT\_MODE : GPIO is not input mode
        - others: other errors.

<a id="_CPPv418bk_gpio_get_output9gpio_id_t"></a>

<a id="_CPPv318bk_gpio_get_output9gpio_id_t"></a> <a id="_CPPv218bk_gpio_get_output9gpio_id_t"></a> <a id="bk_gpio_get_output__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga7f0727891df79177a60026077b694db8"></a> bool bk\_gpio\_get\_output(gpio\_id\_t gpio\_id)
:   Get the GPIO output value,.

    This API get GPIO’s output level: 0 :low\_level 1:high\_level.

    返回
    :   - output value
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - BK\_ERR\_GPIO\_NOT\_INPUT\_MODE : GPIO is not input mode
        - others: other errors.

<a id="_CPPv420bk_gpio_set_capacity9gpio_id_t6uint32"></a>

<a id="_CPPv320bk_gpio_set_capacity9gpio_id_t6uint32"></a> <a id="_CPPv220bk_gpio_set_capacity9gpio_id_t6uint32"></a> <a id="bk_gpio_set_capacity__gpio_id_t.uint32"></a> <a id="group__bk__api__gpio_1ga2e422b1299cf61773beedbddcdc15c47"></a> bool bk\_gpio\_set\_capacity(gpio\_id\_t gpio\_id, uint32 capacity)
:   Set the GPIO driver capacity.

    This API Set GPIO’s output driver capacity which range is 0\~3.

    返回
    :   - input value
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - BK\_ERR\_GPIO\_NOT\_INPUT\_MODE : GPIO is not input mode
        - others: other errors.

<a id="_CPPv426bk_gpio_set_interrupt_type9gpio_id_t15gpio_int_type_t"></a>

<a id="_CPPv326bk_gpio_set_interrupt_type9gpio_id_t15gpio_int_type_t"></a> <a id="_CPPv226bk_gpio_set_interrupt_type9gpio_id_t15gpio_int_type_t"></a> <a id="bk_gpio_set_interrupt_type__gpio_id_t.gpio_int_type_t"></a> <a id="group__bk__api__gpio_1ga33259d746c51989bbeb0d98956570235"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_set\_interrupt\_type(gpio\_id\_t gpio\_id, gpio\_int\_type\_t type)
:   Config the GPIO intterrupt type mode when use gpio intterrupt mode,.

    This API config all GPIO channels’ intterrupt mode, the mode included in gpio\_int\_type\_t.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - BK\_ERR\_GPIO\_INVALID\_INT\_TYPE: invalid GPIO int type
        - others: other errors.

<a id="_CPPv424bk_gpio_enable_interrupt9gpio_id_t"></a>

<a id="_CPPv324bk_gpio_enable_interrupt9gpio_id_t"></a> <a id="_CPPv224bk_gpio_enable_interrupt9gpio_id_t"></a> <a id="bk_gpio_enable_interrupt__gpio_id_t"></a> <a id="group__bk__api__gpio_1gacd7ff15a6390a73472c435411da6c660"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_enable\_interrupt(gpio\_id\_t id)
:   Enable GPIO intterrupt.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - BK\_ERR\_GPIO\_NOT\_INPUT\_MODE : GPIO is not input mode
        - others: other errors.

<a id="_CPPv425bk_gpio_disable_interrupt9gpio_id_t"></a>

<a id="_CPPv325bk_gpio_disable_interrupt9gpio_id_t"></a> <a id="_CPPv225bk_gpio_disable_interrupt9gpio_id_t"></a> <a id="bk_gpio_disable_interrupt__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga48e0eaf44663f68f2f2cea47e6476f95"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_disable\_interrupt(gpio\_id\_t id)
:   Disable GPIO intterrupt.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - others: other errors.

<a id="_CPPv423bk_gpio_clear_interrupt9gpio_id_t"></a>

<a id="_CPPv323bk_gpio_clear_interrupt9gpio_id_t"></a> <a id="_CPPv223bk_gpio_clear_interrupt9gpio_id_t"></a> <a id="bk_gpio_clear_interrupt__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga9309e183217de3b2dfadd4b3d35290cd"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_clear\_interrupt(gpio\_id\_t gpio\_id)
:   Clear GPIO intterrupt.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid gpio channel
        - others: other errors.

<a id="_CPPv420bk_gpio_register_isr9gpio_id_t10gpio_isr_t"></a>

<a id="_CPPv320bk_gpio_register_isr9gpio_id_t10gpio_isr_t"></a> <a id="_CPPv220bk_gpio_register_isr9gpio_id_t10gpio_isr_t"></a> <a id="bk_gpio_register_isr__gpio_id_t.gpio_isr_t"></a> <a id="group__bk__api__gpio_1gadf2d7a2aaf11b9140e9ee78de984ed2e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_register\_isr(gpio\_id\_t id, gpio\_isr\_t isr)
:   Register the interrupt service routine for GPIO channel.

    This API regist gpio isr callback function.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid gpio channel
        - others: other errors.

<a id="_CPPv422bk_gpio_unregister_isr9gpio_id_t"></a>

<a id="_CPPv322bk_gpio_unregister_isr9gpio_id_t"></a> <a id="_CPPv222bk_gpio_unregister_isr9gpio_id_t"></a> <a id="bk_gpio_unregister_isr__gpio_id_t"></a> <a id="group__bk__api__gpio_1gac5d7e52d0c90e032dfa52089f6492f01"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_unregister\_isr(gpio\_id\_t id)
:   Unregister the interrupt service routine for GPIO channel.

    This API deregist gpio isr callback function.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid gpio channel
        - others: other errors.

<a id="_CPPv437bk_gpio_register_lowpower_keep_status9gpio_id_tPK13gpio_config_t"></a>

<a id="_CPPv337bk_gpio_register_lowpower_keep_status9gpio_id_tPK13gpio_config_t"></a> <a id="_CPPv237bk_gpio_register_lowpower_keep_status9gpio_id_tPK13gpio_config_t"></a> <a id="bk_gpio_register_lowpower_keep_status__gpio_id_t.gpio_config_tCP"></a> <a id="group__bk__api__gpio_1ga2bbceab99c3c881173f0f7a0a112d8a0"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_register\_lowpower\_keep\_status(gpio\_id\_t gpio\_id, const gpio\_config\_t \*config)
:   Register the GPIO channel to keep status.

    This API regist gpio to keep status when enter low power or deepsleep.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid gpio channel
        - CONFIG\_GPIO\_DYNAMIC\_KEEP\_STATUS\_MAX\_CNT: too many gpio is register to keep status default max value is: CONFIG\_GPIO\_DYNAMIC\_KEEP\_STATUS\_MAX\_CNT
        - others: other errors.

<a id="_CPPv439bk_gpio_unregister_lowpower_keep_status9gpio_id_t"></a>

<a id="_CPPv339bk_gpio_unregister_lowpower_keep_status9gpio_id_t"></a> <a id="_CPPv239bk_gpio_unregister_lowpower_keep_status9gpio_id_t"></a> <a id="bk_gpio_unregister_lowpower_keep_status__gpio_id_t"></a> <a id="group__bk__api__gpio_1gac4c3e706b78194b3294c7c0ba749b55e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_unregister\_lowpower\_keep\_status(gpio\_id\_t gpio\_id)
:   Unregister the GPIO channel from keep status.

    This API unregist gpio from keep status.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid gpio channel
        - others: other errors.

<a id="_CPPv416bk_gpio_reg_saveP8uint32_t"></a>

<a id="_CPPv316bk_gpio_reg_saveP8uint32_t"></a> <a id="_CPPv216bk_gpio_reg_saveP8uint32_t"></a> <a id="bk_gpio_reg_save__uint32_tP"></a> <a id="group__bk__api__gpio_1gab087a8620f896615b5080fc7f5186b4d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_reg\_save(uint32\_t \*gpio\_cfg)
:   Register save all gpio reg value.

    This API save all gpio reg value function.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv419bk_gpio_reg_restoreP8uint32_t"></a>

<a id="_CPPv319bk_gpio_reg_restoreP8uint32_t"></a> <a id="_CPPv219bk_gpio_reg_restoreP8uint32_t"></a> <a id="bk_gpio_reg_restore__uint32_tP"></a> <a id="group__bk__api__gpio_1gac0f85bcc46f1f17f82d56d60720723ad"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_reg\_restore(uint32\_t \*gpio\_cfg)
:   Register restore all gpio reg value.

    This API restore all gpio reg value function.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_gpio_wakeup_enable7int64_t8uint64_t8uint64_t"></a>

<a id="_CPPv321bk_gpio_wakeup_enable7int64_t8uint64_t8uint64_t"></a> <a id="_CPPv221bk_gpio_wakeup_enable7int64_t8uint64_t8uint64_t"></a> <a id="bk_gpio_wakeup_enable__int64_t.uint64_t.uint64_t"></a> <a id="group__bk__api__gpio_1ga54bf46c728d9157572b533e225daf14c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_wakeup\_enable(int64\_t index, uint64\_t type\_l, uint64\_t type\_h)
:   Register configue the gpio wakeup value.

    This API configue the gpio wakeup value function.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv430bk_gpio_wakeup_interrupt_clearv"></a>

<a id="_CPPv330bk_gpio_wakeup_interrupt_clearv"></a> <a id="_CPPv230bk_gpio_wakeup_interrupt_clearv"></a> <a id="bk_gpio_wakeup_interrupt_clear"></a> <a id="group__bk__api__gpio_1gab8fe4b39f956d0151701327998bf044a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_wakeup\_interrupt\_clear()
:   Register clear wake up interrupt.

    This API clear wake up interrupt function.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv425bk_gpio_ctrl_external_ldo22gpio_ctrl_ldo_module_e9gpio_id_t19gpio_output_state_e"></a>

<a id="_CPPv325bk_gpio_ctrl_external_ldo22gpio_ctrl_ldo_module_e9gpio_id_t19gpio_output_state_e"></a> <a id="_CPPv225bk_gpio_ctrl_external_ldo22gpio_ctrl_ldo_module_e9gpio_id_t19gpio_output_state_e"></a> <a id="bk_gpio_ctrl_external_ldo__gpio_ctrl_ldo_module_e.gpio_id_t.gpio_output_state_e"></a> <a id="group__bk__api__gpio_1ga3ba1f2491962ef391b68deae24787671"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_ctrl\_external\_ldo(gpio\_ctrl\_ldo\_module\_e module, gpio\_id\_t gpio\_id, gpio\_output\_state\_e value)
:   using the gpio to control the external ldo

    control the external ldo,multi modules power on use one gpio control

    **Attention**
    :   - This API is used to use the specific gpio(define in GPIO\_CTRL\_LDO\_MAP in gpio\_map.h) control the external ldo(multi modules power on use one gpio control)

    参数
    :   **-module:gpio** – ctrl ldo module name -gpio\_id:gpio id -value:gpio output state

    返回
    :   - BK\_OK: succeed
        - others: other errors.
