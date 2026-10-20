---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7239/zh_CN/v2.2.1/api-reference/pm/bk_pm.html
sdk_family: bk_idk
chip: BK7239
processor: ''
sdk_version: v2.2.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="pm-apis"></a>

# PM APIs

重要

The PM API v1.0 is the lastest stable PM APIs.

<a id="pm-interface"></a>

## PM Interface

The BK PM Driver supports following logical PM interfaces:

> - BK enter different sleep mode interface
> - BK clock control interface
> - BK power control interface

<a id="pm-api-categories"></a>

## PM API Categories

Most of PM APIs can be categoried as:

> - Common APIs
>   The common APIs are frequently-used.
> - Specific APIs.
>   The specific APIs are used in specific configuration.

Common PM APIs:
:   - [`bk_pm_sleep_mode_set()`](#_CPPv420bk_pm_sleep_mode_set15pm_sleep_mode_e "bk_pm_sleep_mode_set") \- set sleep mode
    - [`bk_pm_module_vote_sleep_ctrl()`](#_CPPv428bk_pm_module_vote_sleep_ctrl22pm_sleep_module_name_e8uint32_t8uint32_t "bk_pm_module_vote_sleep_ctrl") \- module vote sleep ctrl
    - [`bk_pm_module_vote_power_ctrl()`](#_CPPv428bk_pm_module_vote_power_ctrl22pm_power_module_name_e23pm_power_module_state_e "bk_pm_module_vote_power_ctrl") \- module vote power ctrl
    - [`bk_pm_wakeup_source_set()`](#_CPPv423bk_pm_wakeup_source_set18pm_wakeup_source_ePv "bk_pm_wakeup_source_set") \- set wakeup source

Specific APIs:
:   - [`bk_pm_mcu_pm_state_get()`](#_CPPv422bk_pm_mcu_pm_state_getv "bk_pm_mcu_pm_state_get") \- get the state of whether enter the sleep
    - [`bk_pm_mcu_pm_ctrl()`](#_CPPv417bk_pm_mcu_pm_ctrl8uint32_t "bk_pm_mcu_pm_ctrl") \- config whether enter the sleep
    - [`bk_pm_lpo_src_get()`](#_CPPv417bk_pm_lpo_src_getv "bk_pm_lpo_src_get") \- get the lpo source
    - [`bk_pm_lpo_src_set()`](#_CPPv417bk_pm_lpo_src_set12pm_lpo_src_e "bk_pm_lpo_src_set") \- set the lpo source
    - [`bk_pm_lp_vol_get()`](#_CPPv416bk_pm_lp_vol_getv "bk_pm_lp_vol_get") \- get the voltage when enter low voltage
    - [`bk_pm_lp_vol_set()`](#_CPPv416bk_pm_lp_vol_set8uint32_t "bk_pm_lp_vol_set") \- set the voltage when enter low voltage
    - [`bk_pm_light_sleep_unregister_cb()`](#_CPPv431bk_pm_light_sleep_unregister_cbbb "bk_pm_light_sleep_unregister_cb") \- unregister the light sleep callback
    - [`bk_pm_light_sleep_register_cb()`](#_CPPv429bk_pm_light_sleep_register_cbP12pm_cb_conf_tP12pm_cb_conf_t "bk_pm_light_sleep_register_cb") \- register the light sleep callback
    - [`bk_pm_clock_ctrl()`](#_CPPv416bk_pm_clock_ctrl12pm_dev_clk_e16pm_dev_clk_pwr_e "bk_pm_clock_ctrl") \- module vote power ctrl
    - [`bk_pm_wakeup_from_lowvol_consume_time_get()`](#_CPPv441bk_pm_wakeup_from_lowvol_consume_time_getv "bk_pm_wakeup_from_lowvol_consume_time_get") \- get the consume time wakeuping from low voltage
    - [`bk_pm_module_power_state_get()`](#_CPPv428bk_pm_module_power_state_get22pm_power_module_name_e "bk_pm_module_power_state_get") \- get the module power domain state
    - [`bk_pm_phy_cali_state_get()`](#_CPPv424bk_pm_phy_cali_state_getv "bk_pm_phy_cali_state_get") \- get the state whether phy have calibration
    - [`bk_pm_suppress_ticks_and_sleep()`](#_CPPv430bk_pm_suppress_ticks_and_sleep8uint32_t "bk_pm_suppress_ticks_and_sleep") \- enter sleep process(return int)
    - [`bk_pm_enter_sleep()`](#_CPPv417bk_pm_enter_sleepv "bk_pm_enter_sleep") \- enter sleep process(return void)

<a id="programing-principle"></a>

## Programing Principle

重要

Here is some general principle for pm API users:
:   - Enter deep sleep and low voltage ,it only need call the “Common PM APIs”,if you want to call the Specific APIs,please contact us in case of make issue.
    - Use BK\_ERR\_CHECK to check the return value of the pm API
    - If you are not sure how to use pm APIs, study the pm used guide example code first.
    - If you are not sure how to initialize some fields of config struct, use the default configuration macro to use the config first and then set application specific fields

<a id="user-development-model"></a>

## User Development Model

pm interface detail

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [pm.h](https://github.com/bekencorp/armino/blob/main/components/pm.h)

<a id="functions"></a>

### Functions

<a id="_CPPv414bk_pm_send_msgP16pm_ap_core_msg_t"></a>

<a id="_CPPv314bk_pm_send_msgP16pm_ap_core_msg_t"></a> <a id="_CPPv214bk_pm_send_msgP16pm_ap_core_msg_t"></a> <a id="bk_pm_send_msg__pm_ap_core_msg_tP"></a> <a id="pm_8h_1aad034e61fe324b2b1abf41ee93b8f359"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_send\_msg([pm\_ap\_core\_msg\_t](#_CPPv416pm_ap_core_msg_t "pm_ap_core_msg_t") \*msg)
:   send message to pm thread for enter deepsleep or low voltage

    **Attention**
    :   - This API is to send message to pm demo thread for enter deepsleep or low voltage.

    参数
    :   **-msg:message** – info

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv414pm_thread_mainv"></a>

<a id="_CPPv314pm_thread_mainv"></a> <a id="_CPPv214pm_thread_mainv"></a> <a id="pm_thread_main__void"></a> <a id="pm_8h_1a45e08f0d9597855a4e0574e3682175ee"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") pm\_thread\_main(void)
:   start pm thread

    **Attention**
    :   - This API is start pm thread.

    参数
    :   **-void** –

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv433bk_pm_pre_sleep_callback_register16sleep_callback_tPv7uint8_t"></a>

<a id="_CPPv333bk_pm_pre_sleep_callback_register16sleep_callback_tPv7uint8_t"></a> <a id="_CPPv233bk_pm_pre_sleep_callback_register16sleep_callback_tPv7uint8_t"></a> <a id="bk_pm_pre_sleep_callback_register__sleep_callback_t.voidP.uint8_t"></a> <a id="pm_8h_1a09e0512800285267d019818ef508b01c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_pre\_sleep\_callback\_register([sleep\_callback\_t](#_CPPv416sleep_callback_t "sleep_callback_t") callback, void \*arg, uint8\_t priority)
:   Register a pre-sleep callback with execution priority.

    This callback will be called BEFORE the system enters sleep mode. Callbacks are executed in priority order (0\=first, 255\=last).

    Typical use cases:

    - Save peripheral states
    - Power down devices
    - Flush buffers

    Memory cost: 16 bytes per registration (32-bit ARM, aligned) Time complexity: O(n) insertion, O(n) execution

    Example: void uart\_pre\_sleep(void \*arg) { // Save UART state and power down } bk\_pm\_pre\_sleep\_callback\_register(uart\_pre\_sleep, NULL, PM\_CALLBACK\_PRIORITY\_HIGH);

    Priority table example: Priority 0 (CRITICAL): Clock manager, PMU Priority 50 (HIGH): UART, SPI Priority 100 (NORMAL): GPIO, ADC Priority 150 (LOW): Sensors Priority 200 (LOWEST): Debug logging

    参数
    :   - **callback** – Function to call before sleep (must not be NULL)
        - **arg** – User argument passed to callback (can be NULL)
        - **priority** – Execution priority: 0 (highest) to 255 (lowest) Use predefined constants: PM\_CALLBACK\_PRIORITY\_\*

    返回
    :   0 Success -1 Invalid callback (NULL pointer) -2 Out of memory

<a id="_CPPv435bk_pm_pre_sleep_callback_unregister16sleep_callback_t"></a>

<a id="_CPPv335bk_pm_pre_sleep_callback_unregister16sleep_callback_t"></a> <a id="_CPPv235bk_pm_pre_sleep_callback_unregister16sleep_callback_t"></a> <a id="bk_pm_pre_sleep_callback_unregister__sleep_callback_t"></a> <a id="pm_8h_1a518b204dae9ae7e912f7a13105b94938"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_pre\_sleep\_callback\_unregister([sleep\_callback\_t](#_CPPv416sleep_callback_t "sleep_callback_t") callback)
:   Unregister a pre-sleep callback.

    Memory: Frees 12 bytes Time complexity: O(n) where n is number of registered callbacks

    Example: bk\_pm\_pre\_sleep\_callback\_unregister(uart\_pre\_sleep);

    参数
    :   **callback** – Function to remove

    返回
    :   0 Success -1 Invalid callback (NULL pointer) -2 Callback not found

<a id="_CPPv432bk_pm_pre_sleep_callback_executev"></a>

<a id="_CPPv332bk_pm_pre_sleep_callback_executev"></a> <a id="_CPPv232bk_pm_pre_sleep_callback_executev"></a> <a id="bk_pm_pre_sleep_callback_execute__void"></a> <a id="pm_8h_1a7715971258c3eb94bce7e82a5edd21f2"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_pre\_sleep\_callback\_execute(void)
:   Execute all pre-sleep callbacks.

    This function is called automatically by the PM system before entering sleep. Application modules should NOT call this directly.

    Execution order: LIFO (Last-In-First-Out)

    - The most recently registered callback executes first

    Time complexity: O(n)

<a id="_CPPv434bk_pm_post_sleep_callback_register16sleep_callback_tPv7uint8_t"></a>

<a id="_CPPv334bk_pm_post_sleep_callback_register16sleep_callback_tPv7uint8_t"></a> <a id="_CPPv234bk_pm_post_sleep_callback_register16sleep_callback_tPv7uint8_t"></a> <a id="bk_pm_post_sleep_callback_register__sleep_callback_t.voidP.uint8_t"></a> <a id="pm_8h_1aa20daeeaeea9019080174a822b0a16fe"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_post\_sleep\_callback\_register([sleep\_callback\_t](#_CPPv416sleep_callback_t "sleep_callback_t") callback, void \*arg, uint8\_t priority)
:   Register a post-sleep (wakeup) callback with execution priority.

    This callback will be called AFTER the system wakes up from sleep. Callbacks are executed in priority order (0\=first, 255\=last).

    Typical use cases:

    - Restore peripheral states
    - Power up devices
    - Reconfigure clocks

    Memory cost: 16 bytes per registration (32-bit ARM, aligned) Time complexity: O(n) insertion, O(n) execution

    Example: void uart\_post\_sleep(void \*arg) { // Restore UART state and power up } bk\_pm\_post\_sleep\_callback\_register(uart\_post\_sleep, NULL, PM\_CALLBACK\_PRIORITY\_HIGH);

    参数
    :   - **callback** – Function to call after wakeup (must not be NULL)
        - **arg** – User argument passed to callback (can be NULL)
        - **priority** – Execution priority: 0 (highest) to 255 (lowest) Use predefined constants: PM\_CALLBACK\_PRIORITY\_\*

    返回
    :   0 Success -1 Invalid callback (NULL pointer) -2 Out of memory

<a id="_CPPv436bk_pm_post_sleep_callback_unregister16sleep_callback_t"></a>

<a id="_CPPv336bk_pm_post_sleep_callback_unregister16sleep_callback_t"></a> <a id="_CPPv236bk_pm_post_sleep_callback_unregister16sleep_callback_t"></a> <a id="bk_pm_post_sleep_callback_unregister__sleep_callback_t"></a> <a id="pm_8h_1a996b213584a982ae9d0ae71a44cbf01a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_post\_sleep\_callback\_unregister([sleep\_callback\_t](#_CPPv416sleep_callback_t "sleep_callback_t") callback)
:   Unregister a post-sleep callback.

    Memory: Frees 12 bytes Time complexity: O(n)

    Example: bk\_pm\_post\_sleep\_callback\_unregister(uart\_post\_sleep);

    参数
    :   **callback** – Function to remove

    返回
    :   0 Success -1 Invalid callback (NULL pointer) -2 Callback not found

<a id="_CPPv433bk_pm_post_sleep_callback_executev"></a>

<a id="_CPPv333bk_pm_post_sleep_callback_executev"></a> <a id="_CPPv233bk_pm_post_sleep_callback_executev"></a> <a id="bk_pm_post_sleep_callback_execute__void"></a> <a id="pm_8h_1aeed77363defd4c23fb362c4ded50b7a1"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_post\_sleep\_callback\_execute(void)
:   Execute all post-sleep callbacks.

    This function is called automatically by the PM system after waking up. Application modules should NOT call this directly.

    Execution order: LIFO (Last-In-First-Out)

    Time complexity: O(n)

<a id="_CPPv429bk_pm_sleep_wakeup_reason_set8uint64_t"></a>

<a id="_CPPv329bk_pm_sleep_wakeup_reason_set8uint64_t"></a> <a id="_CPPv229bk_pm_sleep_wakeup_reason_set8uint64_t"></a> <a id="bk_pm_sleep_wakeup_reason_set__uint64_t"></a> <a id="pm_8h_1a6c936d50ae9cf36a00398f7f69196851"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_sleep\_wakeup\_reason\_set(uint64\_t wakeup\_irq)
:   set and save wakeup source of exiting sleep

    set and save wakeup source of exiting sleep

    **Attention**
    :   - This API is used to set and save wakeup source of exiting sleep

    参数
    :   **-wakeup\_irq:wakeup** – irq

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv431bk_pm_sleep_wakeup_reason_clearv"></a>

<a id="_CPPv331bk_pm_sleep_wakeup_reason_clearv"></a> <a id="_CPPv231bk_pm_sleep_wakeup_reason_clearv"></a> <a id="bk_pm_sleep_wakeup_reason_clear"></a> <a id="pm_8h_1accc0fbbcf15dcca3e3de434afc187ee9"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_sleep\_wakeup\_reason\_clear()
:   clear wakeup source of exiting sleep process

    clear wakeup source of exit sleep

    **Attention**
    :   - This API is used to clear wakeup source of exiting sleep process

    参数
    :   **-void** –

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv429bk_pm_sleep_wakeup_reason_getv"></a>

<a id="_CPPv329bk_pm_sleep_wakeup_reason_getv"></a> <a id="_CPPv229bk_pm_sleep_wakeup_reason_getv"></a> <a id="bk_pm_sleep_wakeup_reason_get"></a> <a id="pm_8h_1a94ca84cc6fdc496a3b25fef04fe14984"></a> [bk\_pm\_wakeup\_reason\_e](#_CPPv421bk_pm_wakeup_reason_e "bk_pm_wakeup_reason_e") bk\_pm\_sleep\_wakeup\_reason\_get()
:   get wakeup source of exiting sleep

    get wakeup source of exiting sleep

    **Attention**
    :   - This API is used to get wakeup source of exiting sleep

    参数
    :   **-void** –

    返回
    :   - wakeup source(refer to icu\_int\_src\_t in int\_types.h)

<a id="_CPPv437bk_pm_clear_deep_sleep_modules_config22pm_power_module_name_e"></a>

<a id="_CPPv337bk_pm_clear_deep_sleep_modules_config22pm_power_module_name_e"></a> <a id="_CPPv237bk_pm_clear_deep_sleep_modules_config22pm_power_module_name_e"></a> <a id="bk_pm_clear_deep_sleep_modules_config__pm_power_module_name_e"></a> <a id="pm_8h_1adbb78bb789efeeed74ba4828dede103e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_clear\_deep\_sleep\_modules\_config(pm\_power\_module\_name\_e module\_name)
:   clear deep sleep module config

    clear deep sleep module config

    **Attention**
    :   - This API is used to clear deep sleep module config
        - If entering DEEPSLEEP fails, do not call this interface either.
        - Instead, proactively investigate the reasons why entering DEEPSLEEP was unsuccessful.
        - Calling this interface indicates that you are not concerned with whether the relevant modules were closed before attempting to enter DEEPSLEEP.
        - If the relevant modules were prematurely closed before using this method,
        - it is highly likely that DEEPSLEEP will fail to wake up properly.
        - Therefore, this interface is a special case for forcibly entering DEEPSLEEP,
        - but it cannot guarantee that DEEPSLEEP will wake up normally

    参数
    :   **-module:module** – name

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv430bk_pm_get_video_vote_pwr_statev"></a>

<a id="_CPPv330bk_pm_get_video_vote_pwr_statev"></a> <a id="_CPPv230bk_pm_get_video_vote_pwr_statev"></a> <a id="bk_pm_get_video_vote_pwr_state"></a> <a id="pm_8h_1a2cda47c5545551c8faaac3a6f84bc05a"></a> uint32\_t bk\_pm\_get\_video\_vote\_pwr\_state()
:   get the video vote power state

    get the video vote power state

    **Attention**
    :   - This API is used to get the video vote power state

    参数
    :   **-void** –

    返回
    :   - the video vote power state(refer to the enum:power\_sub\_module\_name\_vidp\_e)

<a id="_CPPv430bk_pm_get_audio_vote_pwr_statev"></a>

<a id="_CPPv330bk_pm_get_audio_vote_pwr_statev"></a> <a id="_CPPv230bk_pm_get_audio_vote_pwr_statev"></a> <a id="bk_pm_get_audio_vote_pwr_state"></a> <a id="pm_8h_1ad686a2b7826af329ed340f08e97ec1a0"></a> uint32\_t bk\_pm\_get\_audio\_vote\_pwr\_state()
:   get the audio vote power state

    get the audio vote power state

    **Attention**
    :   - This API is used to get the audio vote power state

    参数
    :   **-void** –

    返回
    :   - the audio vote power state(refer to the enum:power\_sub\_module\_name\_audp\_e)

<a id="_CPPv429bk_pm_check_enter_lv_time_outv"></a>

<a id="_CPPv329bk_pm_check_enter_lv_time_outv"></a> <a id="_CPPv229bk_pm_check_enter_lv_time_outv"></a> <a id="bk_pm_check_enter_lv_time_out__void"></a> <a id="pm_8h_1a121edcdfe291af1fd25c7e3f72636d60"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_check\_enter\_lv\_time\_out(void)
:   check whether enter low voltage sleep mode time out

    check whether enter low voltage sleep mode time out

    **Attention**
    :   - This API is used to check whether enter low voltage sleep mode time out

    参数
    :   **-void** –

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv441bk_pm_enter_lv_time_out_register_callbackP24pm_enter_lv_timeout_cb_t"></a>

<a id="_CPPv341bk_pm_enter_lv_time_out_register_callbackP24pm_enter_lv_timeout_cb_t"></a> <a id="_CPPv241bk_pm_enter_lv_time_out_register_callbackP24pm_enter_lv_timeout_cb_t"></a> <a id="bk_pm_enter_lv_time_out_register_callback__pm_enter_lv_timeout_cb_tP"></a> <a id="pm_8h_1aeb869015abd2cdc657cd1376c27f3eba"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_enter\_lv\_time\_out\_register\_callback([pm\_enter\_lv\_timeout\_cb\_t](#_CPPv424pm_enter_lv_timeout_cb_t "pm_enter_lv_timeout_cb_t") \*lv\_timeout\_cb)
:   register enter low voltage sleep mode time out callback

    register enter low voltage sleep mode time out callback

    **Attention**
    :   - This API is used to register enter low voltage sleep mode time out callback

    参数
    :   **-lv\_timeout\_cb:enter** – low voltage sleep mode time out callback

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv433bk_pm_module_lv_sleep_state_clear11pm_dev_id_e"></a>

<a id="_CPPv333bk_pm_module_lv_sleep_state_clear11pm_dev_id_e"></a> <a id="_CPPv233bk_pm_module_lv_sleep_state_clear11pm_dev_id_e"></a> <a id="bk_pm_module_lv_sleep_state_clear__pm_dev_id_e"></a> <a id="pm_8h_1a8d8731986de7c9b1e0bf1e64b5fb799a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_module\_lv\_sleep\_state\_clear([pm\_dev\_id\_e](#_CPPv411pm_dev_id_e "pm_dev_id_e") module)
:   clear the lv sleep state

    clear the lv sleep state

    **Attention**
    :   - This API is used to clear the lv sleep state

    参数
    :   **-module:module** – name

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv431bk_pm_module_lv_sleep_state_setv"></a>

<a id="_CPPv331bk_pm_module_lv_sleep_state_setv"></a> <a id="_CPPv231bk_pm_module_lv_sleep_state_setv"></a> <a id="bk_pm_module_lv_sleep_state_set__void"></a> <a id="pm_8h_1ad240b51e73a61a9f271ebe23be6e3100"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_module\_lv\_sleep\_state\_set(void)
:   set the lv sleep state

    set the lv sleep state

    **Attention**
    :   - This API is used to set the lv sleep state

    参数
    :   **-void** –

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv431bk_pm_module_lv_sleep_state_get11pm_dev_id_e"></a>

<a id="_CPPv331bk_pm_module_lv_sleep_state_get11pm_dev_id_e"></a> <a id="_CPPv231bk_pm_module_lv_sleep_state_get11pm_dev_id_e"></a> <a id="bk_pm_module_lv_sleep_state_get__pm_dev_id_e"></a> <a id="pm_8h_1a4690e7ecafd0e8263a95631fe0688f7d"></a> uint64\_t bk\_pm\_module\_lv\_sleep\_state\_get([pm\_dev\_id\_e](#_CPPv411pm_dev_id_e "pm_dev_id_e") module)
:   get the lv sleep state

    get the lv sleep state

    **Attention**
    :   - This API is used to get the lv sleep state

    参数
    :   **-module:module** – name

    返回
    :   - module\_lv\_sleep\_state

<a id="_CPPv434bk_pm_deep_sleep_wakeup_source_getv"></a>

<a id="_CPPv334bk_pm_deep_sleep_wakeup_source_getv"></a> <a id="_CPPv234bk_pm_deep_sleep_wakeup_source_getv"></a> <a id="bk_pm_deep_sleep_wakeup_source_get__void"></a> <a id="pm_8h_1a429692ffe3752a6989215c1da44bcb12"></a> pm\_wakeup\_source\_e bk\_pm\_deep\_sleep\_wakeup\_source\_get(void)
:   get wakeup source from deepsleep

    get wakeup source from deepsleep

    **Attention**
    :   - This API is used to get wakeup source from deepsleep

    参数
    :   **-void** –

    返回
    :   - wakeup source(0x0:WAKEUP SOURCE OF GPIO;0x1:WAKEUP SOURCE OF RTC;0x2:WAKEUP SOURCE OF WIFI OR BT;0x4:WAKEUP SOURCE OF TOUCHED;0x5:NONE WAKEUP\_SOURCE)

<a id="_CPPv438bk_pm_exit_low_vol_wakeup_source_clearv"></a>

<a id="_CPPv338bk_pm_exit_low_vol_wakeup_source_clearv"></a> <a id="_CPPv238bk_pm_exit_low_vol_wakeup_source_clearv"></a> <a id="bk_pm_exit_low_vol_wakeup_source_clear__void"></a> <a id="pm_8h_1afaf548e8489e5a1b9e0821df0df16735"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_exit\_low\_vol\_wakeup\_source\_clear(void)
:   clear wakeup source of exiting low voltage process

    clear wakeup source of exit low voltage

    **Attention**
    :   - This API is used to clear wakeup source of exiting low voltage process

    参数
    :   **-void** –

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv436bk_pm_exit_low_vol_wakeup_source_setv"></a>

<a id="_CPPv336bk_pm_exit_low_vol_wakeup_source_setv"></a> <a id="_CPPv236bk_pm_exit_low_vol_wakeup_source_setv"></a> <a id="bk_pm_exit_low_vol_wakeup_source_set__void"></a> <a id="pm_8h_1a278855294e051958e5da4db9f5a801d2"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_exit\_low\_vol\_wakeup\_source\_set(void)
:   set and save wakeup source of exiting low voltage

    set and save wakeup source of exiting low voltage

    **Attention**
    :   - This API is used to set and save wakeup source of exiting low voltage

    参数
    :   **void** –

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv436bk_pm_exit_low_vol_wakeup_source_getv"></a>

<a id="_CPPv336bk_pm_exit_low_vol_wakeup_source_getv"></a> <a id="_CPPv236bk_pm_exit_low_vol_wakeup_source_getv"></a> <a id="bk_pm_exit_low_vol_wakeup_source_get__void"></a> <a id="pm_8h_1adfc55c7a601cfeee3e01ed7faef25d7d"></a> pm\_wakeup\_source\_e bk\_pm\_exit\_low\_vol\_wakeup\_source\_get(void)
:   get wakeup source of exiting low voltage

    get wakeup source of exiting low voltage

    **Attention**
    :   - This API is used to get wakeup source of exiting low voltage

    参数
    :   **-void** –

    返回
    :   - wakeup source(0x0:WAKEUP SOURCE OF GPIO;0x1:WAKEUP SOURCE OF RTC;0x2:WAKEUP SOURCE OF WIFI OR BT;0x4:WAKEUP SOURCE OF TOUCHED;0x5:NONE WAKEUP\_SOURCE)

<a id="_CPPv435bk_pm_mem_auto_power_down_state_getv"></a>

<a id="_CPPv335bk_pm_mem_auto_power_down_state_getv"></a> <a id="_CPPv235bk_pm_mem_auto_power_down_state_getv"></a> <a id="bk_pm_mem_auto_power_down_state_get__void"></a> <a id="pm_8h_1a77ff51e2bb1e5ee8b81dd6e51de6331b"></a> [pm\_mem\_auto\_ctrl\_e](#_CPPv418pm_mem_auto_ctrl_e "pm_mem_auto_ctrl_e") bk\_pm\_mem\_auto\_power\_down\_state\_get(void)
:   get memory auto power down flag

    get memory auto power down flag

    **Attention**
    :   - This API is used to get memory auto power down flag

    参数
    :   **-void** –

    返回
    :   - memory auto power down flag(PM\_MEM\_AUTO\_CTRL\_DISABLE:disable memory auto power down feature ;PM\_MEM\_AUTO\_CTRL\_ENABLE:enable memory auto power down feature)

<a id="_CPPv435bk_pm_mem_auto_power_down_state_set18pm_mem_auto_ctrl_e"></a>

<a id="_CPPv335bk_pm_mem_auto_power_down_state_set18pm_mem_auto_ctrl_e"></a> <a id="_CPPv235bk_pm_mem_auto_power_down_state_set18pm_mem_auto_ctrl_e"></a> <a id="bk_pm_mem_auto_power_down_state_set__pm_mem_auto_ctrl_e"></a> <a id="pm_8h_1ab73937ec22fd2ff3ebf215b37c656679"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_mem\_auto\_power\_down\_state\_set([pm\_mem\_auto\_ctrl\_e](#_CPPv418pm_mem_auto_ctrl_e "pm_mem_auto_ctrl_e") value)
:   memory auto power down flag set

    set memory auto power down flag

    **Attention**
    :   - This API is used to set memory auto power down flag

    参数
    :   **-PM\_MEM\_AUTO\_CTRL\_DISABLE:disable** – memory auto power down feature ;PM\_MEM\_AUTO\_CTRL\_ENABLE:enable memory auto power down feature

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv435bk_pm_cp1_auto_power_down_state_getv"></a>

<a id="_CPPv335bk_pm_cp1_auto_power_down_state_getv"></a> <a id="_CPPv235bk_pm_cp1_auto_power_down_state_getv"></a> <a id="bk_pm_cp1_auto_power_down_state_get__void"></a> <a id="pm_8h_1aae9361b268d540a69ccdf6e675154286"></a> uint32\_t bk\_pm\_cp1\_auto\_power\_down\_state\_get(void)
:   get cp1 auto power down flag

    get cp1 auto power down flag

    **Attention**
    :   - This API is used to get cp1 auto power down flag

    参数
    :   **-void** –

    返回
    :   - cp1 auto power down flag(0x0:close cp1 auto power down feature ;0x1:open cp1 auto power down feature)

<a id="_CPPv435bk_pm_cp1_auto_power_down_state_set8uint32_t"></a>

<a id="_CPPv335bk_pm_cp1_auto_power_down_state_set8uint32_t"></a> <a id="_CPPv235bk_pm_cp1_auto_power_down_state_set8uint32_t"></a> <a id="bk_pm_cp1_auto_power_down_state_set__uint32_t"></a> <a id="pm_8h_1a07ef89ec6b4ec9e8ae786f519a35932d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_cp1\_auto\_power\_down\_state\_set(uint32\_t value)
:   cp1 auto power down flag set

    set cp1 auto power down flag

    **Attention**
    :   - This API is used to set cp1 auto power down flag

    参数
    :   **-0x0:close** – cp1 auto power down feature ;0x1:open cp1 auto power down feature

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv423bk_pm_cp1_boot_flag_getv"></a>

<a id="_CPPv323bk_pm_cp1_boot_flag_getv"></a> <a id="_CPPv223bk_pm_cp1_boot_flag_getv"></a> <a id="bk_pm_cp1_boot_flag_get__void"></a> <a id="pm_8h_1a62800576c2c11d6fdd7507e17cf182e8"></a> uint32\_t bk\_pm\_cp1\_boot\_flag\_get(void)
:   get cpu1 boot flag

    get cpu1 boot flag(ready or not ready)

    **Attention**
    :   - This API is used to get cpu1 boot flag(ready or not ready)

    参数
    :   **-void** –

    返回
    :   - the flag of cpu1 boot flag (0x0:cpu1 not boot ready;0x1:cpu1 boot ready)

<a id="_CPPv422bk_pm_rosc_calibration19pm_rosc_cali_mode_e8uint32_t"></a>

<a id="_CPPv322bk_pm_rosc_calibration19pm_rosc_cali_mode_e8uint32_t"></a> <a id="_CPPv222bk_pm_rosc_calibration19pm_rosc_cali_mode_e8uint32_t"></a> <a id="bk_pm_rosc_calibration__pm_rosc_cali_mode_e.uint32_t"></a> <a id="pm_8h_1acc81286ff8048271d6fd2667f085bb2d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_rosc\_calibration([pm\_rosc\_cali\_mode\_e](#_CPPv419pm_rosc_cali_mode_e "pm_rosc_cali_mode_e") rosc\_cali\_mode, uint32\_t cali\_interval)
:   rosc calibration

    rosc calibration

    **Attention**
    :   - This API is used to calibrate rosc

    参数
    :   **-rosc\_cali\_mode:0x1:rosc** – calibrate manual; 0x0:rosc calibrate auto -cali\_interval: 0x0:0.25s;0x1:0.5s;0x2:0.75s;0x3:1.0s;0x4:1.25s;0x5:1.5s;0x6:1.75s;0x7:2s;

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv423bk_pm_external_ldo_ctrl8uint32_t"></a>

<a id="_CPPv323bk_pm_external_ldo_ctrl8uint32_t"></a> <a id="_CPPv223bk_pm_external_ldo_ctrl8uint32_t"></a> <a id="bk_pm_external_ldo_ctrl__uint32_t"></a> <a id="pm_8h_1a66002867ae298cbdf7dad0aa133c0cc3"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_external\_ldo\_ctrl(uint32\_t value)
:   using the gpio to control the external ldo

    control the external ldo

    **Attention**
    :   - This API is used to use the specific gpio(define in GPIO\_CTRL\_LDO\_OUTPUT\_HIGH\_MAP or GPIO\_CTRL\_LDO\_OUTPUT\_LOW\_MAP in gpio\_map.h) control the external ldo

    参数
    :   **-value:0x1:output** – high; 0x0:output low

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_pm_phy_cali_state_getv"></a>

<a id="_CPPv324bk_pm_phy_cali_state_getv"></a> <a id="_CPPv224bk_pm_phy_cali_state_getv"></a> <a id="bk_pm_phy_cali_state_get__void"></a> <a id="pm_8h_1aff3ee3c79f252cd6ec165eefffedbffd"></a> bool bk\_pm\_phy\_cali\_state\_get(void)
:   get the state of phy calibration

    get the state of phy calibration

    **Attention**
    :   - This API is used to get the state of phy calibration

    参数
    :   **-void** –

    返回
    :   - the state of phy calibration(True:have calibration;False:not calibration)

<a id="_CPPv425bk_pm_phy_reinit_flag_getv"></a>

<a id="_CPPv325bk_pm_phy_reinit_flag_getv"></a> <a id="_CPPv225bk_pm_phy_reinit_flag_getv"></a> <a id="bk_pm_phy_reinit_flag_get__void"></a> <a id="pm_8h_1ab8a5b9b1703297def8bf7e5112e3bbd5"></a> bool bk\_pm\_phy\_reinit\_flag\_get(void)
:   get the flag of phy reinit part1

    get the flag of phy reinit part1

    **Attention**
    :   - This API is used to get the flag of phy reinit part1

    参数
    :   **-void** –

    返回
    :   - the flag of phy reinit part1 (True:have part1;False:not do it)

<a id="_CPPv427bk_pm_phy_reinit_flag_clearv"></a>

<a id="_CPPv327bk_pm_phy_reinit_flag_clearv"></a> <a id="_CPPv227bk_pm_phy_reinit_flag_clearv"></a> <a id="bk_pm_phy_reinit_flag_clear__void"></a> <a id="pm_8h_1abe31cf7b809f5e5da43f4b01f1f6d5ce"></a> void bk\_pm\_phy\_reinit\_flag\_clear(void)
:   clear the flag of phy reinit part1

    clear the flag of phy reinit part1

    **Attention**
    :   - This API is used to clear the flag of phy reinit part1

    参数
    :   **-void** –

    返回
    :   -void

<a id="_CPPv422bk_pm_phy_pm_state_getv"></a>

<a id="_CPPv322bk_pm_phy_pm_state_getv"></a> <a id="_CPPv222bk_pm_phy_pm_state_getv"></a> <a id="bk_pm_phy_pm_state_get__void"></a> <a id="pm_8h_1a8ae778196327f9fbfe256ea9db30977f"></a> uint32\_t bk\_pm\_phy\_pm\_state\_get(void)
:   get the phy power feature state

    get the phy power feature state

    **Attention**
    :   - This API is used to get the phy power manage feature state(open or close)

    参数
    :   **-void** –

    返回
    :   - the state of the phy power manage (0x0:close the power manage of the corresponding module; 0x1:open the power manage of the corresponding module)
        - ( bit0: represents BT’s pm state;
        - bit1: represents WIFI’s pm state;
        - bit2: represents RF’s pm state)

<a id="_CPPv441bk_pm_wakeup_from_lowvol_consume_time_getv"></a>

<a id="_CPPv341bk_pm_wakeup_from_lowvol_consume_time_getv"></a> <a id="_CPPv241bk_pm_wakeup_from_lowvol_consume_time_getv"></a> <a id="bk_pm_wakeup_from_lowvol_consume_time_get__void"></a> <a id="pm_8h_1a2f91c9f463912a44aa1abcfce967aa22"></a> uint32\_t bk\_pm\_wakeup\_from\_lowvol\_consume\_time\_get(void)
:   get the consume time from lowvol wakeup

    the consume time from lowvol wakeup

    **Attention**
    :   - This API is used to get the consume time from lowvol wakeup

    参数
    :   **-void** –

    返回
    :   - the consume time of wakeup from lowvol

<a id="_CPPv423bk_pm_sleep_register_cb15pm_sleep_mode_e11pm_dev_id_eP12pm_cb_conf_tP12pm_cb_conf_t"></a>

<a id="_CPPv323bk_pm_sleep_register_cb15pm_sleep_mode_e11pm_dev_id_eP12pm_cb_conf_tP12pm_cb_conf_t"></a> <a id="_CPPv223bk_pm_sleep_register_cb15pm_sleep_mode_e11pm_dev_id_eP12pm_cb_conf_tP12pm_cb_conf_t"></a> <a id="bk_pm_sleep_register_cb__pm_sleep_mode_e.pm_dev_id_e.pm_cb_conf_tP.pm_cb_conf_tP"></a> <a id="pm_8h_1a4fc73a4741b7dbb69ac33506bc555ccb"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_sleep\_register\_cb([pm\_sleep\_mode\_e](#_CPPv415pm_sleep_mode_e "pm_sleep_mode_e") sleep\_mode, [pm\_dev\_id\_e](#_CPPv411pm_dev_id_e "pm_dev_id_e") dev\_id, [pm\_cb\_conf\_t](#_CPPv412pm_cb_conf_t "pm_cb_conf_t") \*enter\_config, [pm\_cb\_conf\_t](#_CPPv412pm_cb_conf_t "pm_cb_conf_t") \*exit\_config)
:   register sleep mode(low voltage and deepsleep) config

    register sleep config(include callback function and parameter)

    **Attention**
    :   - This API is used to register low voltage and deepsleep config

    参数
    :   **-sleep\_mode:low** – voltage or deepsleep mode -dev\_id:dev id -enter\_config:enter sleep config -exit\_config:exit sleep config

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv425bk_pm_sleep_unregister_cb15pm_sleep_mode_e11pm_dev_id_ebb"></a>

<a id="_CPPv325bk_pm_sleep_unregister_cb15pm_sleep_mode_e11pm_dev_id_ebb"></a> <a id="_CPPv225bk_pm_sleep_unregister_cb15pm_sleep_mode_e11pm_dev_id_ebb"></a> <a id="bk_pm_sleep_unregister_cb__pm_sleep_mode_e.pm_dev_id_e.b.b"></a> <a id="pm_8h_1a0bda874d497ace72fded556e76790f51"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_sleep\_unregister\_cb([pm\_sleep\_mode\_e](#_CPPv415pm_sleep_mode_e "pm_sleep_mode_e") sleep\_mode, [pm\_dev\_id\_e](#_CPPv411pm_dev_id_e "pm_dev_id_e") dev\_id, bool enter\_cb, bool exit\_cb)
:   unregister sleep mode(low voltage and deepsleep) config

    unregister sleep config(include callback function and parameter)

    **Attention**
    :   - This API is used to unregister low voltage and deepsleep config

    参数
    :   **-sleep\_mode:low** – voltage or deepsleep mode -dev\_id:dev id -enter\_cb:whether unregister the enter call back -exit\_cb:whether unregister the exit call back

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv429bk_pm_light_sleep_register_cbP12pm_cb_conf_tP12pm_cb_conf_t"></a>

<a id="_CPPv329bk_pm_light_sleep_register_cbP12pm_cb_conf_tP12pm_cb_conf_t"></a> <a id="_CPPv229bk_pm_light_sleep_register_cbP12pm_cb_conf_tP12pm_cb_conf_t"></a> <a id="bk_pm_light_sleep_register_cb__pm_cb_conf_tP.pm_cb_conf_tP"></a> <a id="pm_8h_1aec6a7c9b0e7632544ad90f73be5dbfc7"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_light\_sleep\_register\_cb([pm\_cb\_conf\_t](#_CPPv412pm_cb_conf_t "pm_cb_conf_t") \*enter\_config, [pm\_cb\_conf\_t](#_CPPv412pm_cb_conf_t "pm_cb_conf_t") \*exit\_config)
:   register light sleep config

    register light sleep config(include callback function and parameter)

    **Attention**
    :   - This API is used to register light sleep config

    参数
    :   **-enter\_config:enter** – light sleep config -exit\_config:exit light sleep config

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv431bk_pm_light_sleep_unregister_cbbb"></a>

<a id="_CPPv331bk_pm_light_sleep_unregister_cbbb"></a> <a id="_CPPv231bk_pm_light_sleep_unregister_cbbb"></a> <a id="bk_pm_light_sleep_unregister_cb__b.b"></a> <a id="pm_8h_1a5a44decf77873a87f254df72783932b4"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_light\_sleep\_unregister\_cb(bool enter\_cb, bool exit\_cb)
:   unregister light sleep callback

    unregister light sleep callback(enter light sleep callback and exit light sleep callback)

    **Attention**
    :   - This API is used to unregister light sleep callback

    参数
    :   **-enter\_cb:whether** – unregister the enter call back -exit\_cb:whether unregister the exit call back

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv428bk_pm_module_sleep_state_get22pm_sleep_module_name_e"></a>

<a id="_CPPv328bk_pm_module_sleep_state_get22pm_sleep_module_name_e"></a> <a id="_CPPv228bk_pm_module_sleep_state_get22pm_sleep_module_name_e"></a> <a id="bk_pm_module_sleep_state_get__pm_sleep_module_name_e"></a> <a id="pm_8h_1adcd277e002a4c7acc7600b01df756272"></a> int32\_t bk\_pm\_module\_sleep\_state\_get([pm\_sleep\_module\_name\_e](#_CPPv422pm_sleep_module_name_e "pm_sleep_module_name_e") module)
:   get sleep state of module

    get current sleep state of pm sleep module.

    **Attention**
    :   - This API is used to get the sleep state

    参数
    :   **\-** – module: module name

    返回
    :   - sleep state: 0x0:active;0x1:sleeped;

<a id="_CPPv428bk_pm_module_power_state_get22pm_power_module_name_e"></a>

<a id="_CPPv328bk_pm_module_power_state_get22pm_power_module_name_e"></a> <a id="_CPPv228bk_pm_module_power_state_get22pm_power_module_name_e"></a> <a id="bk_pm_module_power_state_get__pm_power_module_name_e"></a> <a id="pm_8h_1a6d4e534fc11e59f95ab8e6defd35f2eb"></a> int32\_t bk\_pm\_module\_power\_state\_get(pm\_power\_module\_name\_e module)
:   get power domain of module state

    get the power domain state

    **Attention**
    :   - This API is used to get the power domain state

    参数
    :   **-module:module** – name

    返回
    :   -the state of power domain state

<a id="_CPPv433bk_pm_module_current_cpu_freq_get11pm_dev_id_e"></a>

<a id="_CPPv333bk_pm_module_current_cpu_freq_get11pm_dev_id_e"></a> <a id="_CPPv233bk_pm_module_current_cpu_freq_get11pm_dev_id_e"></a> <a id="bk_pm_module_current_cpu_freq_get__pm_dev_id_e"></a> <a id="pm_8h_1a276f84f764380b4040e77c094788a7dc"></a> [pm\_cpu\_freq\_e](#_CPPv413pm_cpu_freq_e "pm_cpu_freq_e") bk\_pm\_module\_current\_cpu\_freq\_get([pm\_dev\_id\_e](#_CPPv411pm_dev_id_e "pm_dev_id_e") module)
:   get the cpu frequency of the module vote

    get the module voting cpu frequency

    **Attention**
    :   - This API is used to get the module voting cpu frequency

    参数
    :   **-module:module** – id

    返回
    :   - the cpu frequency of the module vote

<a id="_CPPv430bk_pm_current_max_cpu_freq_getv"></a>

<a id="_CPPv330bk_pm_current_max_cpu_freq_getv"></a> <a id="_CPPv230bk_pm_current_max_cpu_freq_getv"></a> <a id="bk_pm_current_max_cpu_freq_get__void"></a> <a id="pm_8h_1ad2b59fb1fa4ac2289d2193ae9ff46dcb"></a> [pm\_cpu\_freq\_e](#_CPPv413pm_cpu_freq_e "pm_cpu_freq_e") bk\_pm\_current\_max\_cpu\_freq\_get(void)
:   get the current max and used cpu frequency

    select the cpu frequency

    **Attention**
    :   - This API is used to get the current max and used cpu frequency

    参数
    :   **-void** –

    返回
    :   - get the current max and used cpu frequency

<a id="_CPPv426bk_pm_module_vote_cpu_freq11pm_dev_id_e13pm_cpu_freq_e"></a>

<a id="_CPPv326bk_pm_module_vote_cpu_freq11pm_dev_id_e13pm_cpu_freq_e"></a> <a id="_CPPv226bk_pm_module_vote_cpu_freq11pm_dev_id_e13pm_cpu_freq_e"></a> <a id="bk_pm_module_vote_cpu_freq__pm_dev_id_e.pm_cpu_freq_e"></a> <a id="pm_8h_1a24c58fe00c65203fd92e4ff315bdef13"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_module\_vote\_cpu\_freq([pm\_dev\_id\_e](#_CPPv411pm_dev_id_e "pm_dev_id_e") module, [pm\_cpu\_freq\_e](#_CPPv413pm_cpu_freq_e "pm_cpu_freq_e") cpu\_freq)
:   vote cpu frequency

    select the cpu frequency

    **Attention**
    :   - This API is used to vote ,then select the cpu frequency

    参数
    :   **-module:module** – id;cpu\_freq:cpu frequency(320M,240M,120M,26M)

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv416bk_pm_clock_ctrl12pm_dev_clk_e16pm_dev_clk_pwr_e"></a>

<a id="_CPPv316bk_pm_clock_ctrl12pm_dev_clk_e16pm_dev_clk_pwr_e"></a> <a id="_CPPv216bk_pm_clock_ctrl12pm_dev_clk_e16pm_dev_clk_pwr_e"></a> <a id="bk_pm_clock_ctrl__pm_dev_clk_e.pm_dev_clk_pwr_e"></a> <a id="pm_8h_1abb622cbb575b649242a287b5c9a1317e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_clock\_ctrl(pm\_dev\_clk\_e module, [pm\_dev\_clk\_pwr\_e](#_CPPv416pm_dev_clk_pwr_e "pm_dev_clk_pwr_e") clock\_state)
:   clock ctrl

    enable or disable dev clock

    **Attention**
    :   - This API is used to enable or disable dev clock

    参数
    :   **-module:device** – id;clock\_state:PM\_CLK\_CTRL\_PWR\_DOWN or PM\_CLK\_CTRL\_PWR\_DOWN

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv416bk_pm_lp_vol_set8uint32_t"></a>

<a id="_CPPv316bk_pm_lp_vol_set8uint32_t"></a> <a id="_CPPv216bk_pm_lp_vol_set8uint32_t"></a> <a id="bk_pm_lp_vol_set__uint32_t"></a> <a id="pm_8h_1a2f55724117180f40e9d8553be5f5693d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_lp\_vol\_set(uint32\_t lp\_vol)
:   lp voltage set

    set the lp voltage

    **Attention**
    :   - This API is used to set lp voltage when enter low voltage

    参数
    :   **-uint32\_t:0x0:0.6v;0x1:0.7v;0x2:0.8v;0x3:0.9v;0x4:1.0v;0x5:1.1v;0x6:1.2v;0x7:1.3v;** –

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv416bk_pm_lp_vol_getv"></a>

<a id="_CPPv316bk_pm_lp_vol_getv"></a> <a id="_CPPv216bk_pm_lp_vol_getv"></a> <a id="bk_pm_lp_vol_get__void"></a> <a id="pm_8h_1a22020f31b86fb729f952c5d97eb48bd1"></a> uint32\_t bk\_pm\_lp\_vol\_get(void)
:   lp voltage get

    get the lpo voltage

    **Attention**
    :   - This API is used to get lpo voltage value

    参数
    :   **-void** –

    返回
    :   - the lp voltage value

<a id="_CPPv419bk_pm_rf_tx_vol_set8uint32_t"></a>

<a id="_CPPv319bk_pm_rf_tx_vol_set8uint32_t"></a> <a id="_CPPv219bk_pm_rf_tx_vol_set8uint32_t"></a> <a id="bk_pm_rf_tx_vol_set__uint32_t"></a> <a id="pm_8h_1a2e1dc69cd965bfc0fee4c45814f1e1c1"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_rf\_tx\_vol\_set(uint32\_t tx\_vol)
:   rf tx voltage set

    set the tx voltage of RF

    **Attention**
    :   - This API is used to set tx voltage of RF

    参数
    :   **-uint32\_t:0x0:1.25v;0x1:1.3v;0x2:1.35v;0x3:1.4v;0x4:1.45v;0x5:1.5v;0x6:1.55v;0x7:1.6v;** –

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv419bk_pm_rf_tx_vol_getv"></a>

<a id="_CPPv319bk_pm_rf_tx_vol_getv"></a> <a id="_CPPv219bk_pm_rf_tx_vol_getv"></a> <a id="bk_pm_rf_tx_vol_get__void"></a> <a id="pm_8h_1a4f692f881e401eb21803cfe8c07d4e8f"></a> uint32\_t bk\_pm\_rf\_tx\_vol\_get(void)
:   rf tx voltage get

    get the tx voltage of RF

    **Attention**
    :   - This API is used to get tx voltage value of RF

    参数
    :   **-void** –

    返回
    :   - the tx voltage value

<a id="_CPPv419bk_pm_rf_rx_vol_set8uint32_t"></a>

<a id="_CPPv319bk_pm_rf_rx_vol_set8uint32_t"></a> <a id="_CPPv219bk_pm_rf_rx_vol_set8uint32_t"></a> <a id="bk_pm_rf_rx_vol_set__uint32_t"></a> <a id="pm_8h_1a359dd8e687b8a1850acd04888c0be71d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_rf\_rx\_vol\_set(uint32\_t rx\_vol)
:   rf rx voltage set

    set the rx voltage of RF

    **Attention**
    :   - This API is used to set rx voltage of RF

    参数
    :   **-uint32\_t:0x0:1.25v;0x1:1.3v;0x2:1.35v;0x3:1.4v;0x4:1.45v;0x5:1.5v;0x6:1.55v;0x7:1.6v;** –

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv419bk_pm_rf_rx_vol_getv"></a>

<a id="_CPPv319bk_pm_rf_rx_vol_getv"></a> <a id="_CPPv219bk_pm_rf_rx_vol_getv"></a> <a id="bk_pm_rf_rx_vol_get__void"></a> <a id="pm_8h_1a9c4dab5b0367423997335bab8cf1ca09"></a> uint32\_t bk\_pm\_rf\_rx\_vol\_get(void)
:   rf rx voltage get

    get the rx voltage of RF

    **Attention**
    :   - This API is used to get rx voltage value of RF

    参数
    :   **-void** –

    返回
    :   - the rx voltage value

<a id="_CPPv417bk_pm_lpo_src_set12pm_lpo_src_e"></a>

<a id="_CPPv317bk_pm_lpo_src_set12pm_lpo_src_e"></a> <a id="_CPPv217bk_pm_lpo_src_set12pm_lpo_src_e"></a> <a id="bk_pm_lpo_src_set__pm_lpo_src_e"></a> <a id="pm_8h_1add44fd1c88a749cd535ce3719c0913b7"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_lpo\_src\_set([pm\_lpo\_src\_e](#_CPPv412pm_lpo_src_e "pm_lpo_src_e") lpo\_src)
:   lpo source set

    set the lpo source

    **Attention**
    :   - This API is used to select 32k source when enter low voltage and deepsleep

    参数
    :   **-lpo\_src:0x0:32K** – from 26m;0x1:32K from 26m;0x2:32K from ROSC;0x3:32K from ROSC

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv417bk_pm_lpo_src_getv"></a>

<a id="_CPPv317bk_pm_lpo_src_getv"></a> <a id="_CPPv217bk_pm_lpo_src_getv"></a> <a id="bk_pm_lpo_src_get__void"></a> <a id="pm_8h_1ac2a31955c32098ba67d3162b91a4eff4"></a> [pm\_lpo\_src\_e](#_CPPv412pm_lpo_src_e "pm_lpo_src_e") bk\_pm\_lpo\_src\_get(void)
:   lpo source get

    get the lpo source

    **Attention**
    :   - This API is used to get 32k lpo source

    参数
    :   **void** –

    返回
    :   -lpo\_src:0x0:32K from 26m;0x1:32K from 26m;0x2:32K from ROSC;0x3:32K from ROSC

<a id="_CPPv417bk_pm_mcu_pm_ctrl8uint32_t"></a>

<a id="_CPPv317bk_pm_mcu_pm_ctrl8uint32_t"></a> <a id="_CPPv217bk_pm_mcu_pm_ctrl8uint32_t"></a> <a id="bk_pm_mcu_pm_ctrl__uint32_t"></a> <a id="pm_8h_1a3c2ac239b2d9853be2aba131ac3fad91"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_mcu\_pm\_ctrl(uint32\_t power\_state)
:   mcu pm ctrl

    enabel and disable the mcu power manage

    **Attention**
    :   - This API is used to enabel and disable the mcu power manage

    参数
    :   **-power\_state:0x0:enable** – the mcu power manage;0x1:disable the mcu power manage

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv422bk_pm_mcu_pm_state_getv"></a>

<a id="_CPPv322bk_pm_mcu_pm_state_getv"></a> <a id="_CPPv222bk_pm_mcu_pm_state_getv"></a> <a id="bk_pm_mcu_pm_state_get__void"></a> <a id="pm_8h_1a17dbcddb40ea21384c26f6d303789606"></a> uint32\_t bk\_pm\_mcu\_pm\_state\_get(void)
:   get the mcu power feature state

    get the mcu power feature state

    **Attention**
    :   -This API is used to get the mcu power manage feature state(open or close)

    参数
    :   **none** –

    返回
    :   -mcu power manage state(0x0:enable the mcu power manage;0x1:disable the mcu power manage)

<a id="_CPPv420bk_pm_sleep_mode_set15pm_sleep_mode_e"></a>

<a id="_CPPv320bk_pm_sleep_mode_set15pm_sleep_mode_e"></a> <a id="_CPPv220bk_pm_sleep_mode_set15pm_sleep_mode_e"></a> <a id="bk_pm_sleep_mode_set__pm_sleep_mode_e"></a> <a id="pm_8h_1a153ea5566c17e684b045d5f49aaf9e4e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_sleep\_mode\_set([pm\_sleep\_mode\_e](#_CPPv415pm_sleep_mode_e "pm_sleep_mode_e") sleep\_mode)
:   set sleep mode

    set sleep mode.

    **Attention**
    :   - This API set sleep mode

    参数
    :   **sleep** – mode:0x0:NORMAL\_SLEEP;0x1:LOW\_VOLTAGE;0x2:DEEP\_SLEEP;0x3:DEFAULT(if it meet low voltage,enter low voltage,otherwise enter normal sleep);

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv423bk_pm_wakeup_source_set18pm_wakeup_source_ePv"></a>

<a id="_CPPv323bk_pm_wakeup_source_set18pm_wakeup_source_ePv"></a> <a id="_CPPv223bk_pm_wakeup_source_set18pm_wakeup_source_ePv"></a> <a id="bk_pm_wakeup_source_set__pm_wakeup_source_e.voidP"></a> <a id="pm_8h_1a4d1aa403afc68bbcc84f109fd7ef9753"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_wakeup\_source\_set(pm\_wakeup\_source\_e wakeup\_source, void \*source\_param)
:   set wakeup source

    set wakeup source(eg.rtc,gpio)

    **Attention**
    :   - This API set wakeup source,wifi and bt themselves not need set wakup source when in volatage

    参数
    :   **-wakeup\_source:wake** – up source -source\_param: the wakeup source parameter

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv423bk_pm_wakeup_source_getv"></a>

<a id="_CPPv323bk_pm_wakeup_source_getv"></a> <a id="_CPPv223bk_pm_wakeup_source_getv"></a> <a id="bk_pm_wakeup_source_get__void"></a> <a id="pm_8h_1aa47d07141191862ec85f373831eba5ab"></a> pm\_wakeup\_source\_e bk\_pm\_wakeup\_source\_get(void)
:   get wakeup source

    get wakeup source

    **Attention**
    :   - This API is used to get wakeup source

    参数
    :   **-void** –

    返回
    :   - wakeup source(0x0:WAKEUP SOURCE OF GPIO;0x1:WAKEUP SOURCE OF RTC;0x2:WAKEUP SOURCE OF WIFI OR BT;0x4:WAKEUP SOURCE OF TOUCHED;0x5:NONE WAKEUP\_SOURCE)

<a id="_CPPv425bk_pm_wakeup_source_clear18pm_wakeup_source_e"></a>

<a id="_CPPv325bk_pm_wakeup_source_clear18pm_wakeup_source_e"></a> <a id="_CPPv225bk_pm_wakeup_source_clear18pm_wakeup_source_e"></a> <a id="bk_pm_wakeup_source_clear__pm_wakeup_source_e"></a> <a id="pm_8h_1a027ee1cd49644eda055a54a24f1f96a3"></a> void bk\_pm\_wakeup\_source\_clear(pm\_wakeup\_source\_e wakeup\_source)
:   clear wakeup source

    clear wakeup source

    **Attention**
    :   - This API is used to clear wakeup source

<a id="_CPPv428bk_pm_module_vote_sleep_ctrl22pm_sleep_module_name_e8uint32_t8uint32_t"></a>

<a id="_CPPv328bk_pm_module_vote_sleep_ctrl22pm_sleep_module_name_e8uint32_t8uint32_t"></a> <a id="_CPPv228bk_pm_module_vote_sleep_ctrl22pm_sleep_module_name_e8uint32_t8uint32_t"></a> <a id="bk_pm_module_vote_sleep_ctrl__pm_sleep_module_name_e.uint32_t.uint32_t"></a> <a id="pm_8h_1a0244dfa987566880fc5cf7a336414271"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_module\_vote\_sleep\_ctrl([pm\_sleep\_module\_name\_e](#_CPPv422pm_sleep_module_name_e "pm_sleep_module_name_e") module, uint32\_t sleep\_state, uint32\_t sleep\_time)
:   module vote sleep ctrl

    other module tell pm module, they have entered sleep.(eg.wifi or bt enter sleep,then call the function ,tell pm it have entered sleep)

    **Attention**
    :   - This API is used by wifi or bt… let pm module know them(wifi or bt…) enter sleep or exit sleep
        - if all the specific module enter sleep, the mcu will enter low voltage

    参数
    :   **-module:module** – name -sleep\_state:0x1:enter sleep;0x0:exit sleep -sleep\_time: sleep time

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv428bk_pm_module_vote_power_ctrl22pm_power_module_name_e23pm_power_module_state_e"></a>

<a id="_CPPv328bk_pm_module_vote_power_ctrl22pm_power_module_name_e23pm_power_module_state_e"></a> <a id="_CPPv228bk_pm_module_vote_power_ctrl22pm_power_module_name_e23pm_power_module_state_e"></a> <a id="bk_pm_module_vote_power_ctrl__pm_power_module_name_e.pm_power_module_state_e"></a> <a id="pm_8h_1a7c7e4c78d0394dddb5d18d9f94d46742"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pm\_module\_vote\_power\_ctrl(pm\_power\_module\_name\_e module, [pm\_power\_module\_state\_e](#_CPPv423pm_power_module_state_e "pm_power_module_state_e") power\_state)
:   pm module vote power ctrl

    ther module tell pm module, they can enter power on or power off

    **Attention**
    :   - This API is used for the module power on and power off.
        - if all the specific module power off, the mcu will enter deep sleep

    参数
    :   **-module:module** – name -power\_state:0x1:power off;0x0:power on

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv430bk_pm_suppress_ticks_and_sleep8uint32_t"></a>

<a id="_CPPv330bk_pm_suppress_ticks_and_sleep8uint32_t"></a> <a id="_CPPv230bk_pm_suppress_ticks_and_sleep8uint32_t"></a> <a id="bk_pm_suppress_ticks_and_sleep__uint32_t"></a> <a id="pm_8h_1aec3fd04baac3e24899a33f11f8895f0b"></a> uint64\_t bk\_pm\_suppress\_ticks\_and\_sleep(uint32\_t sleep\_ticks)
:   pm suppress ticks and sleep

    when the rtos enter idle task and sleep time \> 2\*(time per tick),it will call the function enter power manager

    **Attention**
    :   - This API is used for power manager.

    参数
    :   **-sleep\_ticks:sleep** – time using tick unit

    返回
    :   - uint64\_t: missed\_ticks missed\_ticks is the number of missed ticks during the sleep time

<a id="_CPPv417bk_pm_enter_sleepv"></a>

<a id="_CPPv317bk_pm_enter_sleepv"></a> <a id="_CPPv217bk_pm_enter_sleepv"></a> <a id="bk_pm_enter_sleep__void"></a> <a id="pm_8h_1ae12b00fad132502741aaa20b8321b91b"></a> void bk\_pm\_enter\_sleep(void)
:   enter sleep

    the function is for adapting harmony os

    **Attention**
    :   - This API is used for power manager.

    参数
    :   **\-** – void

    返回
    :   - void

<a id="_CPPv418pm_sleep_vote_initv"></a>

<a id="_CPPv318pm_sleep_vote_initv"></a> <a id="_CPPv218pm_sleep_vote_initv"></a> <a id="pm_sleep_vote_init__void"></a> <a id="pm_8h_1a8382dc2812160b204677b138a50e5b9c"></a> static inline [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") pm\_sleep\_vote\_init(void)
:   sleep vote init

    the function is for init the enter low voltage sleep vote

    **Attention**
    :   - This API is used for init the enter low voltage sleep vote

    参数
    :   **\-** – void

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424pm_clk_32k_source_switch12pm_lpo_src_e"></a>

<a id="_CPPv324pm_clk_32k_source_switch12pm_lpo_src_e"></a> <a id="_CPPv224pm_clk_32k_source_switch12pm_lpo_src_e"></a> <a id="pm_clk_32k_source_switch__pm_lpo_src_e"></a> <a id="pm_8h_1a6aee936bb9365b610146fc40bb4daf75"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") pm\_clk\_32k\_source\_switch([pm\_lpo\_src\_e](#_CPPv412pm_lpo_src_e "pm_lpo_src_e") lpo\_src)
:   32k source switch

    When the external 32k clock source is enabled, this api used to switch the 32k clock source

    参数
    :   **\-** – pm\_lpo\_src\_e taget 32k clock source

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424pm_extern32k_register_cbP21pm_cb_extern32k_cfg_t"></a>

<a id="_CPPv324pm_extern32k_register_cbP21pm_cb_extern32k_cfg_t"></a> <a id="_CPPv224pm_extern32k_register_cbP21pm_cb_extern32k_cfg_t"></a> <a id="pm_extern32k_register_cb__pm_cb_extern32k_cfg_tP"></a> <a id="pm_8h_1a47e05d560584e02006228eacc53efff9"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") pm\_extern32k\_register\_cb([pm\_cb\_extern32k\_cfg\_t](#_CPPv421pm_cb_extern32k_cfg_t "pm_cb_extern32k_cfg_t") \*cfg)
:   register callback function

    BT WIFI module registered callback function, used to switch synchronization when switching clock source

    参数
    :   **\-** – [pm\_cb\_extern32k\_cfg\_t](#structpm__cb__extern32k__cfg__t) Structure pointer

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv426pm_extern32k_unregister_cbP21pm_cb_extern32k_cfg_t"></a>

<a id="_CPPv326pm_extern32k_unregister_cbP21pm_cb_extern32k_cfg_t"></a> <a id="_CPPv226pm_extern32k_unregister_cbP21pm_cb_extern32k_cfg_t"></a> <a id="pm_extern32k_unregister_cb__pm_cb_extern32k_cfg_tP"></a> <a id="pm_8h_1a47959980a4d35f32d1c727a24808d351"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") pm\_extern32k\_unregister\_cb([pm\_cb\_extern32k\_cfg\_t](#_CPPv421pm_cb_extern32k_cfg_t "pm_cb_extern32k_cfg_t") \*cfg)
:   unregister callback function

    参数
    :   **\-** – [pm\_cb\_extern32k\_cfg\_t](#structpm__cb__extern32k__cfg__t) Structure pointer

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv418bk_pm_wifi_rtc_set8uint32_tPv"></a>

<a id="_CPPv318bk_pm_wifi_rtc_set8uint32_tPv"></a> <a id="_CPPv218bk_pm_wifi_rtc_set8uint32_tPv"></a> <a id="bk_pm_wifi_rtc_set__uint32_t.voidP"></a> <a id="pm_8h_1aca8b08ba9ca04e727e3916141d91b3e3"></a> void bk\_pm\_wifi\_rtc\_set(uint32\_t tick, void \*callback)
:   register rtc callback for wifi

    参数
    :   **-tick:tick** – cnt for lv -callback:callback when exit lv

    返回
    :   - void

<a id="_CPPv420bk_pm_wifi_rtc_clearv"></a>

<a id="_CPPv320bk_pm_wifi_rtc_clearv"></a> <a id="_CPPv220bk_pm_wifi_rtc_clearv"></a> <a id="bk_pm_wifi_rtc_clear__void"></a> <a id="pm_8h_1a3944d294d056086c8260b3bfe663dc1a"></a> void bk\_pm\_wifi\_rtc\_clear(void)
:   unregister rtc callback for wifi

    返回
    :   - void

<a id="_CPPv416pm_hardware_initv"></a>

<a id="_CPPv316pm_hardware_initv"></a> <a id="_CPPv216pm_hardware_initv"></a> <a id="pm_hardware_init"></a> <a id="pm_8h_1a5ea682405c1b67e71aa840a9a9639262"></a> void pm\_hardware\_init()
:   pm hardware init

    参数
    :   **void** –

    返回
    :   - void

<a id="structures"></a>

### Structures

<a id="_CPPv416pm_ap_core_msg_t"></a>

<a id="_CPPv316pm_ap_core_msg_t"></a> <a id="_CPPv216pm_ap_core_msg_t"></a> <a id="pm_ap_core_msg_t"></a> <a id="structpm__ap__core__msg__t"></a> struct pm\_ap\_core\_msg\_t

<a id="_CPPv419gpio_wakeup_param_t"></a>

<a id="_CPPv319gpio_wakeup_param_t"></a> <a id="_CPPv219gpio_wakeup_param_t"></a> <a id="gpio_wakeup_param_t"></a> <a id="structgpio__wakeup__param__t"></a> struct gpio\_wakeup\_param\_t

<a id="_CPPv418rtc_wakeup_param_t"></a>

<a id="_CPPv318rtc_wakeup_param_t"></a> <a id="_CPPv218rtc_wakeup_param_t"></a> <a id="rtc_wakeup_param_t"></a> <a id="structrtc__wakeup__param__t"></a> struct rtc\_wakeup\_param\_t

<a id="_CPPv421system_wakeup_param_t"></a>

<a id="_CPPv321system_wakeup_param_t"></a> <a id="_CPPv221system_wakeup_param_t"></a> <a id="system_wakeup_param_t"></a> <a id="structsystem__wakeup__param__t"></a> struct system\_wakeup\_param\_t

<a id="_CPPv422usbplug_wakeup_param_t"></a>

<a id="_CPPv322usbplug_wakeup_param_t"></a> <a id="_CPPv222usbplug_wakeup_param_t"></a> <a id="usbplug_wakeup_param_t"></a> <a id="structusbplug__wakeup__param__t"></a> struct usbplug\_wakeup\_param\_t

<a id="_CPPv420touch_wakeup_param_t"></a>

<a id="_CPPv320touch_wakeup_param_t"></a> <a id="_CPPv220touch_wakeup_param_t"></a> <a id="touch_wakeup_param_t"></a> <a id="structtouch__wakeup__param__t"></a> struct touch\_wakeup\_param\_t

<a id="_CPPv423pm_lv_timeout_cb_conf_t"></a>

<a id="_CPPv323pm_lv_timeout_cb_conf_t"></a> <a id="_CPPv223pm_lv_timeout_cb_conf_t"></a> <a id="pm_lv_timeout_cb_conf_t"></a> <a id="structpm__lv__timeout__cb__conf__t"></a> struct pm\_lv\_timeout\_cb\_conf\_t

<a id="_CPPv424pm_enter_lv_timeout_cb_t"></a>

<a id="_CPPv324pm_enter_lv_timeout_cb_t"></a> <a id="_CPPv224pm_enter_lv_timeout_cb_t"></a> <a id="pm_enter_lv_timeout_cb_t"></a> <a id="structpm__enter__lv__timeout__cb__t"></a> struct pm\_enter\_lv\_timeout\_cb\_t

<a id="_CPPv412pm_cb_conf_t"></a>

<a id="_CPPv312pm_cb_conf_t"></a> <a id="_CPPv212pm_cb_conf_t"></a> <a id="pm_cb_conf_t"></a> <a id="structpm__cb__conf__t"></a> struct pm\_cb\_conf\_t

<a id="_CPPv413pm_sleep_cb_t"></a>

<a id="_CPPv313pm_sleep_cb_t"></a> <a id="_CPPv213pm_sleep_cb_t"></a> <a id="pm_sleep_cb_t"></a> <a id="structpm__sleep__cb__t"></a> struct pm\_sleep\_cb\_t

<a id="_CPPv421pm_cb_extern32k_cfg_t"></a>

<a id="_CPPv321pm_cb_extern32k_cfg_t"></a> <a id="_CPPv221pm_cb_extern32k_cfg_t"></a> <a id="pm_cb_extern32k_cfg_t"></a> <a id="structpm__cb__extern32k__cfg__t"></a> struct pm\_cb\_extern32k\_cfg\_t

<a id="macros"></a>

### Macros

<a id="c.PM_CALLBACK_PRIORITY_CRITICAL"></a>

<a id="pm_8h_1a10e14e0e4cc35de79deb228a56b1f898"></a> PM\_CALLBACK\_PRIORITY\_CRITICAL
:   Critical hardware (clocks, PMU, power domains)

<a id="c.PM_CALLBACK_PRIORITY_HIGH"></a>

<a id="pm_8h_1a76813abcc5ec05e104cb5312d51134f7"></a> PM\_CALLBACK\_PRIORITY\_HIGH
:   Important peripherals (UART, SPI, I2C)

<a id="c.PM_CALLBACK_PRIORITY_NORMAL"></a>

<a id="pm_8h_1a70ed878bdcdfb8470f70265974510e8d"></a> PM\_CALLBACK\_PRIORITY\_NORMAL
:   Standard drivers (GPIO, ADC, PWM)

<a id="c.PM_CALLBACK_PRIORITY_LOW"></a>

<a id="pm_8h_1a4c787f1f2640c866d7f3b15f2ad66a67"></a> PM\_CALLBACK\_PRIORITY\_LOW
:   Non-critical modules (sensors, LEDs)

<a id="c.PM_CALLBACK_PRIORITY_LOWEST"></a>

<a id="pm_8h_1aadf7fcac013f35371d8a4260ed4d00e8"></a> PM\_CALLBACK\_PRIORITY\_LOWEST
:   Optional features (debug, logging, statistics)

<a id="c.PARAM_DATA_VALID"></a>

<a id="pm_8h_1a5ab8e0cca43587601d838f03ca7ed3ef"></a> PARAM\_DATA\_VALID

<a id="c.PM_APP_AUTO_VOTE_ENABLE"></a>

<a id="pm_8h_1ac4c3be7f71c8dce2982c6c1ba9d3d626"></a> PM\_APP\_AUTO\_VOTE\_ENABLE

<a id="c.PM_APP_AUTO_VOTE_DISENABLE"></a>

<a id="pm_8h_1af1d889f9875dcf0ec65cc3a27df95982"></a> PM\_APP\_AUTO\_VOTE\_DISENABLE

<a id="c.PM_CP1_AUTO_POWER_DOWN_ENABLE"></a>

<a id="pm_8h_1a988bd6d20dfa813cd540653393c360e4"></a> PM\_CP1\_AUTO\_POWER\_DOWN\_ENABLE

<a id="c.PM_CP1_AUTO_POWER_DOWN_DISENABLE"></a>

<a id="pm_8h_1ace6c57891d54f759af30d6403b62b436"></a> PM\_CP1\_AUTO\_POWER\_DOWN\_DISENABLE

<a id="c.pm_wakeup_source_e"></a>

<a id="pm_8h_1a0f4d6b60927be42f43537edbf72c3a25"></a> pm\_wakeup\_source\_e

<a id="c.PM_WAKEUP_SOURCE_INT_GPIO"></a>

<a id="pm_8h_1a44f7e5f95a7af6a0258cfd6052a23d9f"></a> PM\_WAKEUP\_SOURCE\_INT\_GPIO

<a id="c.PM_WAKEUP_SOURCE_INT_RTC"></a>

<a id="pm_8h_1a8867d581fc8b8693c49e2d612ba7108c"></a> PM\_WAKEUP\_SOURCE\_INT\_RTC

<a id="c.PM_WAKEUP_SOURCE_INT_TOUCHED"></a>

<a id="pm_8h_1ad94dd354a577b41d7b0ce69864e96cac"></a> PM\_WAKEUP\_SOURCE\_INT\_TOUCHED

<a id="c.PM_WAKEUP_SOURCE_INT_SYSTEM_WAKE"></a>

<a id="pm_8h_1a916cbb68395453d57fa1d789949b301e"></a> PM\_WAKEUP\_SOURCE\_INT\_SYSTEM\_WAKE

<a id="c.PM_WAKEUP_SOURCE_INT_WIFI"></a>

<a id="pm_8h_1a4a88f94efcd2451f3d304db9d41dea4c"></a> PM\_WAKEUP\_SOURCE\_INT\_WIFI

<a id="c.PM_WAKEUP_SOURCE_INT_BT"></a>

<a id="pm_8h_1ad018ba85368d2a67032b580b5de7ad12"></a> PM\_WAKEUP\_SOURCE\_INT\_BT

<a id="c.PM_WAKEUP_SOURCE_INT_USBPLUG"></a>

<a id="pm_8h_1a8d412e3169f921f83f891c5543b9361b"></a> PM\_WAKEUP\_SOURCE\_INT\_USBPLUG

<a id="c.PM_WAKEUP_SOURCE_INT_NONE"></a>

<a id="pm_8h_1a5b6c767ce60d2eb1552381762d9d3cd6"></a> PM\_WAKEUP\_SOURCE\_INT\_NONE

<a id="c.pm_power_module_name_e"></a>

<a id="pm_8h_1a622259d0f252b4322590f820ad8373e3"></a> pm\_power\_module\_name\_e

<a id="c.PM_POWER_MODULE_NAME_MEM1"></a>

<a id="pm_8h_1a19ea565f03e9e37aa92c2a1836f050e3"></a> PM\_POWER\_MODULE\_NAME\_MEM1

<a id="c.PM_POWER_MODULE_NAME_MEM2"></a>

<a id="pm_8h_1ae03f0d2504149b31e6b8ac3d50f8229a"></a> PM\_POWER\_MODULE\_NAME\_MEM2

<a id="c.PM_POWER_MODULE_NAME_MEM3"></a>

<a id="pm_8h_1afc757669e10d04b9d6be28a53b90f4a0"></a> PM\_POWER\_MODULE\_NAME\_MEM3

<a id="c.PM_POWER_MODULE_NAME_ENCP"></a>

<a id="pm_8h_1a9a810464454f31695e4cb8c98104b73a"></a> PM\_POWER\_MODULE\_NAME\_ENCP

<a id="c.PM_POWER_MODULE_NAME_BAKP"></a>

<a id="pm_8h_1ac8f4f2db5308ae8ed58ef967a169873b"></a> PM\_POWER\_MODULE\_NAME\_BAKP

<a id="c.PM_POWER_MODULE_NAME_AHBP"></a>

<a id="pm_8h_1abc0878f39042e2d0743ed0c9d3edeac8"></a> PM\_POWER\_MODULE\_NAME\_AHBP

<a id="c.PM_POWER_MODULE_NAME_AUDP"></a>

<a id="pm_8h_1ae29726eb30aaddfd76862957acdde662"></a> PM\_POWER\_MODULE\_NAME\_AUDP

<a id="c.PM_POWER_MODULE_NAME_VIDP"></a>

<a id="pm_8h_1a608652bb6b4701828d0872cfd1e6c5a7"></a> PM\_POWER\_MODULE\_NAME\_VIDP

<a id="c.PM_POWER_MODULE_NAME_BTSP"></a>

<a id="pm_8h_1a1ddd02ef7243b684f55b6490cf1bc7c3"></a> PM\_POWER\_MODULE\_NAME\_BTSP

<a id="c.PM_POWER_MODULE_NAME_WIFIP_MAC"></a>

<a id="pm_8h_1a68327aa5bfa799f7e0e319d44827f1a4"></a> PM\_POWER\_MODULE\_NAME\_WIFIP\_MAC

<a id="c.PM_POWER_MODULE_NAME_PHY"></a>

<a id="pm_8h_1ae4109c998353ef4b616c7dc32da48999"></a> PM\_POWER\_MODULE\_NAME\_PHY

<a id="c.PM_POWER_MODULE_NAME_MEM0"></a>

<a id="pm_8h_1ab760a712402a8d5d6ae96a612ab4d824"></a> PM\_POWER\_MODULE\_NAME\_MEM0

<a id="c.PM_POWER_MODULE_NAME_MEM4"></a>

<a id="pm_8h_1a21386afd414589140b7c4f081a4fc9a4"></a> PM\_POWER\_MODULE\_NAME\_MEM4

<a id="c.PM_POWER_MODULE_NAME_OFDM"></a>

<a id="pm_8h_1a56254ba808944e4fc218d511f6f9319b"></a> PM\_POWER\_MODULE\_NAME\_OFDM

<a id="c.PM_POWER_MODULE_NAME_THREAD"></a>

<a id="pm_8h_1a67a1367b1e3eb7e217ec24f4c5d8cd45"></a> PM\_POWER\_MODULE\_NAME\_THREAD

<a id="c.PM_POWER_MODULE_NAME_TCM0_PGEN"></a>

<a id="pm_8h_1a13375fb45082736a7daf16056aba0354"></a> PM\_POWER\_MODULE\_NAME\_TCM0\_PGEN

<a id="c.PM_POWER_MODULE_NAME_ROM_PGEN"></a>

<a id="pm_8h_1a4ee93da6ae3582dc313119e687deccd9"></a> PM\_POWER\_MODULE\_NAME\_ROM\_PGEN

<a id="c.PM_POWER_MODULE_NAME_TCM1_PGEN"></a>

<a id="pm_8h_1a77cafa2241895da954444c28f936e49e"></a> PM\_POWER\_MODULE\_NAME\_TCM1\_PGEN

<a id="c.PM_POWER_MODULE_NAME_CPU1"></a>

<a id="pm_8h_1a22ffe1f5469dfc6de00836c8518bdf2d"></a> PM\_POWER\_MODULE\_NAME\_CPU1

<a id="c.PM_POWER_MODULE_NAME_CPU2"></a>

<a id="pm_8h_1a48de9c3793911ff67b48b3e416097795"></a> PM\_POWER\_MODULE\_NAME\_CPU2

<a id="c.PM_POWER_MODULE_NAME_APP"></a>

<a id="pm_8h_1a84936ddfddee7de18da5b918931e7503"></a> PM\_POWER\_MODULE\_NAME\_APP

<a id="c.PM_POWER_MODULE_NAME_NONE"></a>

<a id="pm_8h_1ae6851181a422a97075179a871c3fbb86"></a> PM\_POWER\_MODULE\_NAME\_NONE

<a id="c.PM_POWER_SUB_MODULE_NAME_ENCP_OTP"></a>

<a id="pm_8h_1aba4a04b8f76daa82fa653b3cd39b9217"></a> PM\_POWER\_SUB\_MODULE\_NAME\_ENCP\_OTP

<a id="c.PM_POWER_SUB_MODULE_NAME_ENCP_TRUSTENGINE"></a>

<a id="pm_8h_1aaaa1764ed68eea8e794ebac3e015a7db"></a> PM\_POWER\_SUB\_MODULE\_NAME\_ENCP\_TRUSTENGINE

<a id="c.PM_POWER_SUB_MODULE_NAME_AUDP_FFT"></a>

<a id="pm_8h_1a787eb02ea509b0cbe08efb5a603d9c04"></a> PM\_POWER\_SUB\_MODULE\_NAME\_AUDP\_FFT

<a id="c.PM_POWER_SUB_MODULE_NAME_AUDP_SBC"></a>

<a id="pm_8h_1ab4733dad37c1df8419e7bef3b24f195e"></a> PM\_POWER\_SUB\_MODULE\_NAME\_AUDP\_SBC

<a id="c.PM_POWER_SUB_MODULE_NAME_AUDP_AUDIO"></a>

<a id="pm_8h_1aea6fc43c0d2078e3d2b2b510e44e4182"></a> PM\_POWER\_SUB\_MODULE\_NAME\_AUDP\_AUDIO

<a id="c.PM_POWER_SUB_MODULE_NAME_AUDP_I2S"></a>

<a id="pm_8h_1add97ac7e97f18809b55338c5055d3bf7"></a> PM\_POWER\_SUB\_MODULE\_NAME\_AUDP\_I2S

<a id="c.PM_POWER_SUB_MODULE_NAME_VIDP_DMA2D"></a>

<a id="pm_8h_1ab01c9cb1c45f2501ccfd3bbc5ec0d4c8"></a> PM\_POWER\_SUB\_MODULE\_NAME\_VIDP\_DMA2D

<a id="c.PM_POWER_SUB_MODULE_NAME_VIDP_YUVBUF"></a>

<a id="pm_8h_1ad5aa872d5a4360b3cc0ec3c0737e5b04"></a> PM\_POWER\_SUB\_MODULE\_NAME\_VIDP\_YUVBUF

<a id="c.PM_POWER_SUB_MODULE_NAME_VIDP_JPEG_EN"></a>

<a id="pm_8h_1aa7da249bcc6b9d153725295a7f746428"></a> PM\_POWER\_SUB\_MODULE\_NAME\_VIDP\_JPEG\_EN

<a id="c.PM_POWER_SUB_MODULE_NAME_VIDP_JPEG_DE"></a>

<a id="pm_8h_1a466f4cb54bfa4c0814c8985eef142de9"></a> PM\_POWER\_SUB\_MODULE\_NAME\_VIDP\_JPEG\_DE

<a id="c.PM_POWER_SUB_MODULE_NAME_VIDP_LCD"></a>

<a id="pm_8h_1a5bf62e03ae537a33f2d2c300f3b55b7d"></a> PM\_POWER\_SUB\_MODULE\_NAME\_VIDP\_LCD

<a id="c.PM_POWER_SUB_MODULE_NAME_VIDP_ROTT"></a>

<a id="pm_8h_1a7ecae6555949f23d8e69c8483f3bec57"></a> PM\_POWER\_SUB\_MODULE\_NAME\_VIDP\_ROTT

<a id="c.PM_POWER_SUB_MODULE_NAME_VIDP_SCAL0"></a>

<a id="pm_8h_1ae96dd9746f3243925c16d624a4281761"></a> PM\_POWER\_SUB\_MODULE\_NAME\_VIDP\_SCAL0

<a id="c.PM_POWER_SUB_MODULE_NAME_VIDP_SCAL1"></a>

<a id="pm_8h_1a2819d5ec3dd5c8ced437c90d2cf053bd"></a> PM\_POWER\_SUB\_MODULE\_NAME\_VIDP\_SCAL1

<a id="c.PM_POWER_SUB_MODULE_NAME_VIDP_H264"></a>

<a id="pm_8h_1aae39b86e6524911dfdc3b89254b395f1"></a> PM\_POWER\_SUB\_MODULE\_NAME\_VIDP\_H264

<a id="c.PM_POWER_SUB_MODULE_NAME_BTSP"></a>

<a id="pm_8h_1aa91506bfbcb52cf85f218d1c5728d4db"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BTSP

<a id="c.PM_POWER_SUB_MODULE_NAME_THREAD"></a>

<a id="pm_8h_1a931e168eea69e764022e23eef12cef2e"></a> PM\_POWER\_SUB\_MODULE\_NAME\_THREAD

<a id="c.PM_POWER_SUB_MODULE_NAME_PHY_BT"></a>

<a id="pm_8h_1a64ece40a79d482e577a1c2623c640e86"></a> PM\_POWER\_SUB\_MODULE\_NAME\_PHY\_BT

<a id="c.PM_POWER_SUB_MODULE_NAME_PHY_WIFI"></a>

<a id="pm_8h_1aebe0995985b32bc13b55db7513c142f7"></a> PM\_POWER\_SUB\_MODULE\_NAME\_PHY\_WIFI

<a id="c.PM_POWER_SUB_MODULE_NAME_PHY_RF"></a>

<a id="pm_8h_1a1f098ea804b9777bc618f40ce5563268"></a> PM\_POWER\_SUB\_MODULE\_NAME\_PHY\_RF

<a id="c.PM_POWER_SUB_MODULE_NAME_PHY_THREAD"></a>

<a id="pm_8h_1ae522ed61da643379786faa78dea79ec5"></a> PM\_POWER\_SUB\_MODULE\_NAME\_PHY\_THREAD

<a id="c.PM_POWER_SUB_MODULE_NAME_AHBP_CAN"></a>

<a id="pm_8h_1aebd409aecae955f6742ee47a50ee86f5"></a> PM\_POWER\_SUB\_MODULE\_NAME\_AHBP\_CAN

<a id="c.PM_POWER_SUB_MODULE_NAME_AHBP_QSPI"></a>

<a id="pm_8h_1a8b451d73f87ec775e4bf410eb447a960"></a> PM\_POWER\_SUB\_MODULE\_NAME\_AHBP\_QSPI

<a id="c.PM_POWER_SUB_MODULE_NAME_AHBP_USB"></a>

<a id="pm_8h_1adc4c56f4fe921e496ab74e07edd37cd1"></a> PM\_POWER\_SUB\_MODULE\_NAME\_AHBP\_USB

<a id="c.PM_POWER_SUB_MODULE_NAME_AHBP_PSRAM"></a>

<a id="pm_8h_1a4b80fb84a687db43d52baa86af87d680"></a> PM\_POWER\_SUB\_MODULE\_NAME\_AHBP\_PSRAM

<a id="c.PM_POWER_SUB_MODULE_NAME_AHBP_QSPI1"></a>

<a id="pm_8h_1ac0ea02088b1e05da7ae8d57c3918e975"></a> PM\_POWER\_SUB\_MODULE\_NAME\_AHBP\_QSPI1

<a id="c.PM_POWER_SUB_MODULE_NAME_AHBP_ENET"></a>

<a id="pm_8h_1ac19ebd9fc75e3b60328deaa81625a4ce"></a> PM\_POWER\_SUB\_MODULE\_NAME\_AHBP\_ENET

<a id="c.PM_POWER_SUB_MODULE_NAME_AHBP_SCR"></a>

<a id="pm_8h_1a3fadc13d5e969c3a05998a9bbf562f83"></a> PM\_POWER\_SUB\_MODULE\_NAME\_AHBP\_SCR

<a id="c.PM_POWER_SUB_MODULE_NAME_AHBP_LIN"></a>

<a id="pm_8h_1af3361827d317d9f421c082896f6f4972"></a> PM\_POWER\_SUB\_MODULE\_NAME\_AHBP\_LIN

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_TIMER1"></a>

<a id="pm_8h_1a2075b6535cdf1dadf16e30ad60244fd4"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_TIMER1

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_UART1"></a>

<a id="pm_8h_1a458409eda7acd98b92b7a2194ef86137"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_UART1

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_UART2"></a>

<a id="pm_8h_1a65186318635458578bb70daad2ec3461"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_UART2

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_SPI1"></a>

<a id="pm_8h_1a7332ac5b79d463a16f4154f983582ddf"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_SPI1

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_I2C0"></a>

<a id="pm_8h_1aa3bbb1f9c09bf715aa7cc015046d025b"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_I2C0

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_I2C1"></a>

<a id="pm_8h_1aa084743308c0b3002763222ee2cd9507"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_I2C1

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_SADC"></a>

<a id="pm_8h_1ac2bf42b36d2889f0794e035f35fd5687"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_SADC

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_PWM1"></a>

<a id="pm_8h_1a7b39ec3b42e23724c39d9a7d5a67244d"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_PWM1

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_PWM0"></a>

<a id="pm_8h_1ad291f82b4463d4d865ec0b229dbd76e8"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_PWM0

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_TRNG"></a>

<a id="pm_8h_1af5158916d71bd8e240da00e40682a831"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_TRNG

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_IRDA"></a>

<a id="pm_8h_1a8a13db1579b2b2b129223a28efbf56c7"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_IRDA

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_SDIO"></a>

<a id="pm_8h_1a1dcdc950e7bc2c7f07daf3b2aa409a2e"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_SDIO

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_COMSEG"></a>

<a id="pm_8h_1a4d85d8a9fd3e2f618a85ff597458e0af"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_COMSEG

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_DMA0"></a>

<a id="pm_8h_1aa26d043dd26004a821aeb4d785506d80"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_DMA0

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_DMA1"></a>

<a id="pm_8h_1a943edf54b3fe56a6207a05291ef73319"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_DMA1

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_LA"></a>

<a id="pm_8h_1a50a9385aa6e5f6365807b7f50df76070"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_LA

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_UART3"></a>

<a id="pm_8h_1ab9dbf99229d54e76151656e1d18145c6"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_UART3

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_I2S"></a>

<a id="pm_8h_1ad1c7cfe5eb2de78df8f2e6a15190113a"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_I2S

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_LEDC"></a>

<a id="pm_8h_1a8b84b1edc61fd34d3dd17b2983919e58"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_LEDC

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_QSPI1"></a>

<a id="pm_8h_1a6db789d2bbc14506a53b27b5156524cd"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_QSPI1

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_PSRAM"></a>

<a id="pm_8h_1af0a1f375b7b512c37e44941adaa36740"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_PSRAM

<a id="c.PM_POWER_SUB_MODULE_NAME_BAKP_PM"></a>

<a id="pm_8h_1a2b874d8f9bf93769c9077be0138cd715"></a> PM\_POWER\_SUB\_MODULE\_NAME\_BAKP\_PM

<a id="c.pm_dev_clk_e"></a>

<a id="pm_8h_1a0aefd84f992d65c96c0cee4a892b0d9d"></a> pm\_dev\_clk\_e

<a id="c.PM_CLK_ID_I2C1"></a>

<a id="pm_8h_1aa921b7c309fbb1e21c97d409f1fc65a3"></a> PM\_CLK\_ID\_I2C1

<a id="c.PM_CLK_ID_SPI_1"></a>

<a id="pm_8h_1a97c9f9c354dd5851d32d91c7358e65a3"></a> PM\_CLK\_ID\_SPI\_1

<a id="c.PM_CLK_ID_UART1"></a>

<a id="pm_8h_1ac4ab62e8905789c82222d54fddde7d16"></a> PM\_CLK\_ID\_UART1

<a id="c.PM_CLK_ID_PWM_1"></a>

<a id="pm_8h_1ae801198a7134b09255e23aa164c20337"></a> PM\_CLK\_ID\_PWM\_1

<a id="c.PM_CLK_ID_TIMER_1"></a>

<a id="pm_8h_1ac3b5e773833b087b6b85624b6a8fa5f9"></a> PM\_CLK\_ID\_TIMER\_1

<a id="c.PM_CLK_ID_SARADC"></a>

<a id="pm_8h_1a19e846c1c8ac53076a33685bc959105e"></a> PM\_CLK\_ID\_SARADC

<a id="c.PM_CLK_ID_IRDA"></a>

<a id="pm_8h_1a2b2cb157b243b103bc63c3f5ea0b93fa"></a> PM\_CLK\_ID\_IRDA

<a id="c.PM_CLK_ID_EFUSE"></a>

<a id="pm_8h_1a2c010259824c95fbcd61a9c3bd6a5b14"></a> PM\_CLK\_ID\_EFUSE

<a id="c.PM_CLK_ID_I2C2"></a>

<a id="pm_8h_1af713845a98f214fed95a3b1ba171c5d3"></a> PM\_CLK\_ID\_I2C2

<a id="c.PM_CLK_ID_SPI_2"></a>

<a id="pm_8h_1a913a87a23bdbf46f46ad6346fa69d300"></a> PM\_CLK\_ID\_SPI\_2

<a id="c.PM_CLK_ID_UART2"></a>

<a id="pm_8h_1ac0ee27f75925e800b44e769ba952808b"></a> PM\_CLK\_ID\_UART2

<a id="c.PM_CLK_ID_UART3"></a>

<a id="pm_8h_1a865c164e3b5c631cacb217d2122c5a49"></a> PM\_CLK\_ID\_UART3

<a id="c.PM_CLK_ID_PWM_2"></a>

<a id="pm_8h_1a32e5db603457daf54ce9bab73b02cd09"></a> PM\_CLK\_ID\_PWM\_2

<a id="c.PM_CLK_ID_TIMER_2"></a>

<a id="pm_8h_1ad9579fd679da6247fdfbb382fd806c72"></a> PM\_CLK\_ID\_TIMER\_2

<a id="c.PM_CLK_ID_TIMER_3"></a>

<a id="pm_8h_1a48e4e25534add667b8bbc12fb6ce9739"></a> PM\_CLK\_ID\_TIMER\_3

<a id="c.PM_CLK_ID_OTP"></a>

<a id="pm_8h_1afb778f5f51d453fae2cb05e7c00b373d"></a> PM\_CLK\_ID\_OTP

<a id="c.PM_CLK_ID_I2S_1"></a>

<a id="pm_8h_1af8c35e7a789dbd7065f80898d22503d6"></a> PM\_CLK\_ID\_I2S\_1

<a id="c.PM_CLK_ID_USB_1"></a>

<a id="pm_8h_1acd4dfb93005cb8627d3bb15bb58399d8"></a> PM\_CLK\_ID\_USB\_1

<a id="c.PM_CLK_ID_CAN"></a>

<a id="pm_8h_1afb3b9c651457631350814811fd53b1ad"></a> PM\_CLK\_ID\_CAN

<a id="c.PM_CLK_ID_PSRAM"></a>

<a id="pm_8h_1a6dbe80a7ede39887c6222d6677b13176"></a> PM\_CLK\_ID\_PSRAM

<a id="c.PM_CLK_ID_QSPI_1"></a>

<a id="pm_8h_1a895b35ced6f654c3fa897369558eb3a1"></a> PM\_CLK\_ID\_QSPI\_1

<a id="c.PM_CLK_ID_QSPI_2"></a>

<a id="pm_8h_1a766ecf7e767c9919ac55b1ff46506108"></a> PM\_CLK\_ID\_QSPI\_2

<a id="c.PM_CLK_ID_SDIO"></a>

<a id="pm_8h_1af52d6e66b5d6cd600a7a5d1a030cfff9"></a> PM\_CLK\_ID\_SDIO

<a id="c.PM_CLK_ID_AUXS"></a>

<a id="pm_8h_1a77cd4ccb0fe74c73d4b12e45c833fe6a"></a> PM\_CLK\_ID\_AUXS

<a id="c.PM_CLK_ID_BTDM"></a>

<a id="pm_8h_1abb4983aa2502a6d48621340c71bd5d02"></a> PM\_CLK\_ID\_BTDM

<a id="c.PM_CLK_ID_XVR"></a>

<a id="pm_8h_1a3b0c12f9b3901ccc0ff7bc62358bb2a8"></a> PM\_CLK\_ID\_XVR

<a id="c.PM_CLK_ID_MAC"></a>

<a id="pm_8h_1a648d177c8117006c0d12b9b45fabbb18"></a> PM\_CLK\_ID\_MAC

<a id="c.PM_CLK_ID_PHY"></a>

<a id="pm_8h_1a29249a09ddccd60db9eaf0582953c052"></a> PM\_CLK\_ID\_PHY

<a id="c.PM_CLK_ID_JPEG"></a>

<a id="pm_8h_1a1df4b6385892f8b0c4f75b5f1f7eea16"></a> PM\_CLK\_ID\_JPEG

<a id="c.PM_CLK_ID_DISP"></a>

<a id="pm_8h_1a3f90485ef96812cd991ec7d1a06f2e41"></a> PM\_CLK\_ID\_DISP

<a id="c.PM_CLK_ID_AUDIO"></a>

<a id="pm_8h_1a4f5418e4514ceb56e2b84fd2bfbbfab0"></a> PM\_CLK\_ID\_AUDIO

<a id="c.PM_CLK_ID_WDG_CPU"></a>

<a id="pm_8h_1aa3d3265a4388f05affe6b6365ae261e2"></a> PM\_CLK\_ID\_WDG\_CPU

<a id="c.PM_CLK_ID_UART4"></a>

<a id="pm_8h_1a853f97d02f5852068b6b520b102ccf57"></a> PM\_CLK\_ID\_UART4

<a id="c.PM_CLK_ID_GPIO"></a>

<a id="pm_8h_1aa015dbce7ad34447711010cac6fd423e"></a> PM\_CLK\_ID\_GPIO

<a id="c.PM_CLK_ID_LED"></a>

<a id="pm_8h_1a024bf997a2c9e22b4032cd2e92c2d571"></a> PM\_CLK\_ID\_LED

<a id="c.PM_CLK_ID_DPLLDIV"></a>

<a id="pm_8h_1ab36900df802f4d4aed74cfe6b242d012"></a> PM\_CLK\_ID\_DPLLDIV

<a id="c.PM_CLK_ID_THREAD"></a>

<a id="pm_8h_1ab00b85c3f0e2e29e3109e158c0f2788d"></a> PM\_CLK\_ID\_THREAD

<a id="c.PM_CLK_ID_RF"></a>

<a id="pm_8h_1a36c51c1f04f372c3134a90cff5644fbd"></a> PM\_CLK\_ID\_RF

<a id="c.PM_ENTER_NORMAL_SLEEP_MODULES_CONFIG"></a>

<a id="pm_8h_1a37b9af1766aaa15a01b34dbd0615015e"></a> PM\_ENTER\_NORMAL\_SLEEP\_MODULES\_CONFIG

<a id="c.PM_ENTER_LOW_VOL_MODULES_CONFIG"></a>

<a id="pm_8h_1aa353472a8841c49f36eb6acaf4422b8e"></a> PM\_ENTER\_LOW\_VOL\_MODULES\_CONFIG

<a id="c.PM_ENTER_DEEP_SLEEP_MODULES_CONFIG"></a>

<a id="pm_8h_1a827973d38b055254e8670855d4d377b5"></a> PM\_ENTER\_DEEP\_SLEEP\_MODULES\_CONFIG

<a id="c.PM_VOLTAGE_OF_LOW_VOL"></a>

<a id="pm_8h_1ad1d51df4688b7a67fc3df4ba53cd9d32"></a> PM\_VOLTAGE\_OF\_LOW\_VOL

<a id="c.PM_LPO_SOURCE"></a>

<a id="pm_8h_1a4bddbd8d2fb05cb202d350ae34fd3b8e"></a> PM\_LPO\_SOURCE

<a id="c.PM_APP_AUTO_VOTE_CTRL"></a>

<a id="pm_8h_1a5ffb706580ea15aa0dfac0ef25eb87b4"></a> PM\_APP\_AUTO\_VOTE\_CTRL

<a id="c.PM_CP1_AUTO_POWER_DOWN_CTRL"></a>

<a id="pm_8h_1a01cec514a54c5202c9ede6ed6605009d"></a> PM\_CP1\_AUTO\_POWER\_DOWN\_CTRL

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv416sleep_callback_t"></a>

<a id="_CPPv316sleep_callback_t"></a> <a id="_CPPv216sleep_callback_t"></a> <a id="sleep_callback_t"></a> <a id="pm_8h_1ad65351b48b6ec8be7fed5c71f1822838"></a> typedef void (\*sleep\_callback\_t)(void \*arg)
:   Sleep callback function type

    Note: Callback functions are called at specific points in sleep cycle:

    - Pre-sleep callback: Called before entering sleep mode
    - Post-sleep callback: Called after waking up from sleep

    Param arg
    :   User-defined argument passed during registration

<a id="_CPPv422pm_enter_lv_timeout_cb"></a>

<a id="_CPPv322pm_enter_lv_timeout_cb"></a> <a id="_CPPv222pm_enter_lv_timeout_cb"></a> <a id="pm_enter_lv_timeout_cb"></a> <a id="pm_8h_1ab6584a3c3b8187bc519ecde1bb31b78f"></a> typedef [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") (\*pm\_enter\_lv\_timeout\_cb)(void \*args)

<a id="_CPPv45pm_cb"></a>

<a id="_CPPv35pm_cb"></a> <a id="_CPPv25pm_cb"></a> <a id="pm_cb"></a> <a id="pm_8h_1a0fac550e92f2fe3271e8d3176029f7a7"></a> typedef int (\*pm\_cb)(uint64\_t sleep\_time, void \*args)

<a id="_CPPv412pm_cb_notify"></a>

<a id="_CPPv312pm_cb_notify"></a> <a id="_CPPv212pm_cb_notify"></a> <a id="pm_cb_notify"></a> <a id="pm_8h_1ab504b011a1186200779994c0f0a7f85d"></a> typedef int (\*pm\_cb\_notify)(void)

<a id="_CPPv415pm_cb_extern32k"></a>

<a id="_CPPv315pm_cb_extern32k"></a> <a id="_CPPv215pm_cb_extern32k"></a> <a id="pm_cb_extern32k"></a> <a id="pm_8h_1ad47546fd28aab29f482a187228ba6f09"></a> typedef int (\*pm\_cb\_extern32k)([pm\_sw\_step\_e](#_CPPv412pm_sw_step_e "pm_sw_step_e") sw\_step, [pm\_lpo\_src\_e](#_CPPv412pm_lpo_src_e "pm_lpo_src_e") lpo\_src, [pm\_cb\_notify](#_CPPv412pm_cb_notify "pm_cb_notify") cb)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv419pm_sleep_mode_msg_e"></a>

<a id="_CPPv319pm_sleep_mode_msg_e"></a> <a id="_CPPv219pm_sleep_mode_msg_e"></a> <a id="pm_8h_1a78d50449688a9b4602a6dc64fb09f1b8"></a> enum pm\_sleep\_mode\_msg\_e
:   *Values:*

    <a id="_CPPv4N19pm_sleep_mode_msg_e24PM_ENTER_LOW_VOLTAGE_MSGE"></a>

    <a id="_CPPv3N19pm_sleep_mode_msg_e24PM_ENTER_LOW_VOLTAGE_MSGE"></a> <a id="_CPPv2N19pm_sleep_mode_msg_e24PM_ENTER_LOW_VOLTAGE_MSGE"></a> <a id="pm_8h_1a78d50449688a9b4602a6dc64fb09f1b8ae6212322ced74ce8dc28bd185cbf1f50"></a> enumerator PM\_ENTER\_LOW\_VOLTAGE\_MSG

    <a id="_CPPv4N19pm_sleep_mode_msg_e23PM_ENTER_DEEP_SLEEP_MSGE"></a>

    <a id="_CPPv3N19pm_sleep_mode_msg_e23PM_ENTER_DEEP_SLEEP_MSGE"></a> <a id="_CPPv2N19pm_sleep_mode_msg_e23PM_ENTER_DEEP_SLEEP_MSGE"></a> <a id="pm_8h_1a78d50449688a9b4602a6dc64fb09f1b8a2246f4d902071240f38a5684b7271f24"></a> enumerator PM\_ENTER\_DEEP\_SLEEP\_MSG

    <a id="_CPPv4N19pm_sleep_mode_msg_e22PM_CALLBACK_HANDLE_MSGE"></a>

    <a id="_CPPv3N19pm_sleep_mode_msg_e22PM_CALLBACK_HANDLE_MSGE"></a> <a id="_CPPv2N19pm_sleep_mode_msg_e22PM_CALLBACK_HANDLE_MSGE"></a> <a id="pm_8h_1a78d50449688a9b4602a6dc64fb09f1b8a4b119b1d92ca199fe19e2aaf6455f59b"></a> enumerator PM\_CALLBACK\_HANDLE\_MSG

<a id="_CPPv418pm_cp1_auto_ctrl_e"></a>

<a id="_CPPv318pm_cp1_auto_ctrl_e"></a> <a id="_CPPv218pm_cp1_auto_ctrl_e"></a> <a id="pm_8h_1a7c018dab03ddc36d433844d0a4fae54c"></a> enum pm\_cp1\_auto\_ctrl\_e
:   *Values:*

    <a id="_CPPv4N18pm_cp1_auto_ctrl_e24PM_CP1_AUTO_CTRL_DISABLEE"></a>

    <a id="_CPPv3N18pm_cp1_auto_ctrl_e24PM_CP1_AUTO_CTRL_DISABLEE"></a> <a id="_CPPv2N18pm_cp1_auto_ctrl_e24PM_CP1_AUTO_CTRL_DISABLEE"></a> <a id="pm_8h_1a7c018dab03ddc36d433844d0a4fae54cab939075d4535ce2e71b22361141c6c48"></a> enumerator PM\_CP1\_AUTO\_CTRL\_DISABLE

    <a id="_CPPv4N18pm_cp1_auto_ctrl_e23PM_CP1_AUTO_CTRL_ENABLEE"></a>

    <a id="_CPPv3N18pm_cp1_auto_ctrl_e23PM_CP1_AUTO_CTRL_ENABLEE"></a> <a id="_CPPv2N18pm_cp1_auto_ctrl_e23PM_CP1_AUTO_CTRL_ENABLEE"></a> <a id="pm_8h_1a7c018dab03ddc36d433844d0a4fae54caaf2f11b612f557ed98980e318975c559"></a> enumerator PM\_CP1\_AUTO\_CTRL\_ENABLE

<a id="_CPPv418pm_mem_auto_ctrl_e"></a>

<a id="_CPPv318pm_mem_auto_ctrl_e"></a> <a id="_CPPv218pm_mem_auto_ctrl_e"></a> <a id="pm_8h_1a9ee6f7f57e8200df10b6b84a0b0207a4"></a> enum pm\_mem\_auto\_ctrl\_e
:   *Values:*

    <a id="_CPPv4N18pm_mem_auto_ctrl_e24PM_MEM_AUTO_CTRL_DISABLEE"></a>

    <a id="_CPPv3N18pm_mem_auto_ctrl_e24PM_MEM_AUTO_CTRL_DISABLEE"></a> <a id="_CPPv2N18pm_mem_auto_ctrl_e24PM_MEM_AUTO_CTRL_DISABLEE"></a> <a id="pm_8h_1a9ee6f7f57e8200df10b6b84a0b0207a4aa1ace8b83b8f49ff7ad999dafbe1231a"></a> enumerator PM\_MEM\_AUTO\_CTRL\_DISABLE

    <a id="_CPPv4N18pm_mem_auto_ctrl_e23PM_MEM_AUTO_CTRL_ENABLEE"></a>

    <a id="_CPPv3N18pm_mem_auto_ctrl_e23PM_MEM_AUTO_CTRL_ENABLEE"></a> <a id="_CPPv2N18pm_mem_auto_ctrl_e23PM_MEM_AUTO_CTRL_ENABLEE"></a> <a id="pm_8h_1a9ee6f7f57e8200df10b6b84a0b0207a4a457091da33200179bec5e5cdb0d1382c"></a> enumerator PM\_MEM\_AUTO\_CTRL\_ENABLE

<a id="_CPPv429gpio_trigger_interrupt_type_e"></a>

<a id="_CPPv329gpio_trigger_interrupt_type_e"></a> <a id="_CPPv229gpio_trigger_interrupt_type_e"></a> <a id="pm_8h_1ab727a464c0940f7faf413a291fca6d47"></a> enum gpio\_trigger\_interrupt\_type\_e
:   *Values:*

    <a id="_CPPv4N29gpio_trigger_interrupt_type_e39GPIO_TRIGGER_INTERRUPE_LEVEL_LOW_ACTIVEE"></a>

    <a id="_CPPv3N29gpio_trigger_interrupt_type_e39GPIO_TRIGGER_INTERRUPE_LEVEL_LOW_ACTIVEE"></a> <a id="_CPPv2N29gpio_trigger_interrupt_type_e39GPIO_TRIGGER_INTERRUPE_LEVEL_LOW_ACTIVEE"></a> <a id="pm_8h_1ab727a464c0940f7faf413a291fca6d47a01994d9af6198447230a3ffa333ff653"></a> enumerator GPIO\_TRIGGER\_INTERRUPE\_LEVEL\_LOW\_ACTIVE

    <a id="_CPPv4N29gpio_trigger_interrupt_type_e40GPIO_TRIGGER_INTERRUPE_LEVEL_HIGH_ACTIVEE"></a>

    <a id="_CPPv3N29gpio_trigger_interrupt_type_e40GPIO_TRIGGER_INTERRUPE_LEVEL_HIGH_ACTIVEE"></a> <a id="_CPPv2N29gpio_trigger_interrupt_type_e40GPIO_TRIGGER_INTERRUPE_LEVEL_HIGH_ACTIVEE"></a> <a id="pm_8h_1ab727a464c0940f7faf413a291fca6d47a1ec46b1e590e6f09ad1652674f4e31a6"></a> enumerator GPIO\_TRIGGER\_INTERRUPE\_LEVEL\_HIGH\_ACTIVE

    <a id="_CPPv4N29gpio_trigger_interrupt_type_e34GPIO_TRIGGER_INTERRUPE_EDGE_RISINGE"></a>

    <a id="_CPPv3N29gpio_trigger_interrupt_type_e34GPIO_TRIGGER_INTERRUPE_EDGE_RISINGE"></a> <a id="_CPPv2N29gpio_trigger_interrupt_type_e34GPIO_TRIGGER_INTERRUPE_EDGE_RISINGE"></a> <a id="pm_8h_1ab727a464c0940f7faf413a291fca6d47a6840731f6142cb865179e1805f401064"></a> enumerator GPIO\_TRIGGER\_INTERRUPE\_EDGE\_RISING

    <a id="_CPPv4N29gpio_trigger_interrupt_type_e35GPIO_TRIGGER_INTERRUPE_EDGE_FALLINGE"></a>

    <a id="_CPPv3N29gpio_trigger_interrupt_type_e35GPIO_TRIGGER_INTERRUPE_EDGE_FALLINGE"></a> <a id="_CPPv2N29gpio_trigger_interrupt_type_e35GPIO_TRIGGER_INTERRUPE_EDGE_FALLINGE"></a> <a id="pm_8h_1ab727a464c0940f7faf413a291fca6d47a931ac8ad0a84f7cf4c6c687767c301a2"></a> enumerator GPIO\_TRIGGER\_INTERRUPE\_EDGE\_FALLING

<a id="_CPPv421wifi_bt_wakeup_type_e"></a>

<a id="_CPPv321wifi_bt_wakeup_type_e"></a> <a id="_CPPv221wifi_bt_wakeup_type_e"></a> <a id="pm_8h_1ac8a195e4cdf552d54802b022992e84ba"></a> enum wifi\_bt\_wakeup\_type\_e
:   *Values:*

    <a id="_CPPv4N21wifi_bt_wakeup_type_e11WIFI_WAKEUPE"></a>

    <a id="_CPPv3N21wifi_bt_wakeup_type_e11WIFI_WAKEUPE"></a> <a id="_CPPv2N21wifi_bt_wakeup_type_e11WIFI_WAKEUPE"></a> <a id="pm_8h_1ac8a195e4cdf552d54802b022992e84baa66d79c947edaf951029c6ee82f259ff6"></a> enumerator WIFI\_WAKEUP

    <a id="_CPPv4N21wifi_bt_wakeup_type_e9BT_WAKEUPE"></a>

    <a id="_CPPv3N21wifi_bt_wakeup_type_e9BT_WAKEUPE"></a> <a id="_CPPv2N21wifi_bt_wakeup_type_e9BT_WAKEUPE"></a> <a id="pm_8h_1ac8a195e4cdf552d54802b022992e84baa867971d0d892507413bf056bec50d4f1"></a> enumerator BT\_WAKEUP

<a id="_CPPv415pm_sleep_mode_e"></a>

<a id="_CPPv315pm_sleep_mode_e"></a> <a id="_CPPv215pm_sleep_mode_e"></a> <a id="pm_8h_1a1e18f6a017fe6d7638c44fd98a11ba80"></a> enum pm\_sleep\_mode\_e
:   *Values:*

    <a id="_CPPv4N15pm_sleep_mode_e20PM_MODE_NORMAL_SLEEPE"></a>

    <a id="_CPPv3N15pm_sleep_mode_e20PM_MODE_NORMAL_SLEEPE"></a> <a id="_CPPv2N15pm_sleep_mode_e20PM_MODE_NORMAL_SLEEPE"></a> <a id="pm_8h_1a1e18f6a017fe6d7638c44fd98a11ba80a8073c9c175eae3a2196d70df0ef86a4d"></a> enumerator PM\_MODE\_NORMAL\_SLEEP

    <a id="_CPPv4N15pm_sleep_mode_e19PM_MODE_LOW_VOLTAGEE"></a>

    <a id="_CPPv3N15pm_sleep_mode_e19PM_MODE_LOW_VOLTAGEE"></a> <a id="_CPPv2N15pm_sleep_mode_e19PM_MODE_LOW_VOLTAGEE"></a> <a id="pm_8h_1a1e18f6a017fe6d7638c44fd98a11ba80a5237dda1f2094d9c4bfe78878b6f7068"></a> enumerator PM\_MODE\_LOW\_VOLTAGE

    <a id="_CPPv4N15pm_sleep_mode_e18PM_MODE_DEEP_SLEEPE"></a>

    <a id="_CPPv3N15pm_sleep_mode_e18PM_MODE_DEEP_SLEEPE"></a> <a id="_CPPv2N15pm_sleep_mode_e18PM_MODE_DEEP_SLEEPE"></a> <a id="pm_8h_1a1e18f6a017fe6d7638c44fd98a11ba80adf1726166321b3ed0283427423d90426"></a> enumerator PM\_MODE\_DEEP\_SLEEP

    <a id="_CPPv4N15pm_sleep_mode_e24PM_MODE_SUPER_DEEP_SLEEPE"></a>

    <a id="_CPPv3N15pm_sleep_mode_e24PM_MODE_SUPER_DEEP_SLEEPE"></a> <a id="_CPPv2N15pm_sleep_mode_e24PM_MODE_SUPER_DEEP_SLEEPE"></a> <a id="pm_8h_1a1e18f6a017fe6d7638c44fd98a11ba80a7a92b90c40829e7ef98d6a9e87d92e22"></a> enumerator PM\_MODE\_SUPER\_DEEP\_SLEEP

    <a id="_CPPv4N15pm_sleep_mode_e15PM_MODE_DEFAULTE"></a>

    <a id="_CPPv3N15pm_sleep_mode_e15PM_MODE_DEFAULTE"></a> <a id="_CPPv2N15pm_sleep_mode_e15PM_MODE_DEFAULTE"></a> <a id="pm_8h_1a1e18f6a017fe6d7638c44fd98a11ba80a31ff9eab80f03437597a4d68b3d10a66"></a> enumerator PM\_MODE\_DEFAULT

<a id="_CPPv422pm_normal_sleep_mode_e"></a>

<a id="_CPPv322pm_normal_sleep_mode_e"></a> <a id="_CPPv222pm_normal_sleep_mode_e"></a> <a id="pm_8h_1a9ac4f33dd102e6c7f5fc3a9c5f27e4de"></a> enum pm\_normal\_sleep\_mode\_e
:   *Values:*

    <a id="_CPPv4N22pm_normal_sleep_mode_e26PM_NORMAL_SLEEP_ULTRA_EXITE"></a>

    <a id="_CPPv3N22pm_normal_sleep_mode_e26PM_NORMAL_SLEEP_ULTRA_EXITE"></a> <a id="_CPPv2N22pm_normal_sleep_mode_e26PM_NORMAL_SLEEP_ULTRA_EXITE"></a> <a id="pm_8h_1a9ac4f33dd102e6c7f5fc3a9c5f27e4dea4628a078a7f60ac8318942f3c3e1321d"></a> enumerator PM\_NORMAL\_SLEEP\_ULTRA\_EXIT

    <a id="_CPPv4N22pm_normal_sleep_mode_e27PM_NORMAL_SLEEP_ULTRA_ENTERE"></a>

    <a id="_CPPv3N22pm_normal_sleep_mode_e27PM_NORMAL_SLEEP_ULTRA_ENTERE"></a> <a id="_CPPv2N22pm_normal_sleep_mode_e27PM_NORMAL_SLEEP_ULTRA_ENTERE"></a> <a id="pm_8h_1a9ac4f33dd102e6c7f5fc3a9c5f27e4dea0b02291acd2abd060fe225fbca36931c"></a> enumerator PM\_NORMAL\_SLEEP\_ULTRA\_ENTER

    <a id="_CPPv4N22pm_normal_sleep_mode_e22PM_NORMAL_SLEEP_MODE_1E"></a>

    <a id="_CPPv3N22pm_normal_sleep_mode_e22PM_NORMAL_SLEEP_MODE_1E"></a> <a id="_CPPv2N22pm_normal_sleep_mode_e22PM_NORMAL_SLEEP_MODE_1E"></a> <a id="pm_8h_1a9ac4f33dd102e6c7f5fc3a9c5f27e4dea006a81fbfb127942d30eaa0c75d36bde"></a> enumerator PM\_NORMAL\_SLEEP\_MODE\_1

    <a id="_CPPv4N22pm_normal_sleep_mode_e23PM_NORMAL_SLEEP_WORKINGE"></a>

    <a id="_CPPv3N22pm_normal_sleep_mode_e23PM_NORMAL_SLEEP_WORKINGE"></a> <a id="_CPPv2N22pm_normal_sleep_mode_e23PM_NORMAL_SLEEP_WORKINGE"></a> <a id="pm_8h_1a9ac4f33dd102e6c7f5fc3a9c5f27e4deaa92566012030f43fd0d0d4cd34b5d150"></a> enumerator PM\_NORMAL\_SLEEP\_WORKING

<a id="_CPPv422pm_sleep_module_name_e"></a>

<a id="_CPPv322pm_sleep_module_name_e"></a> <a id="_CPPv222pm_sleep_module_name_e"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8c"></a> enum pm\_sleep\_module\_name\_e
:   *Values:*

    <a id="_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_I2C1E"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_I2C1E"></a> <a id="_CPPv2N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_I2C1E"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8cab8871f48fa8ee2f6759afc33d824075c"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_I2C1

    <a id="_CPPv4N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_SPI_1E"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_SPI_1E"></a> <a id="_CPPv2N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_SPI_1E"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8ca34ba2b12246c3b1f3f5b7ae49bae2859"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_SPI\_1

    <a id="_CPPv4N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_UART1E"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_UART1E"></a> <a id="_CPPv2N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_UART1E"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8caf7c65baaf910370a91c00c08a9ecf5cb"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_UART1

    <a id="_CPPv4N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_PWM_1E"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_PWM_1E"></a> <a id="_CPPv2N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_PWM_1E"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8caf30319557580c456d91f76693cfe80b4"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_PWM\_1

    <a id="_CPPv4N22pm_sleep_module_name_e28PM_SLEEP_MODULE_NAME_TIMER_1E"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e28PM_SLEEP_MODULE_NAME_TIMER_1E"></a> <a id="_CPPv2N22pm_sleep_module_name_e28PM_SLEEP_MODULE_NAME_TIMER_1E"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8ca101d2b1a7f0e376255a945d8f8ae8553"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_TIMER\_1

    <a id="_CPPv4N22pm_sleep_module_name_e27PM_SLEEP_MODULE_NAME_SARADCE"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e27PM_SLEEP_MODULE_NAME_SARADCE"></a> <a id="_CPPv2N22pm_sleep_module_name_e27PM_SLEEP_MODULE_NAME_SARADCE"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8ca5d94e57796d60ca7ce4bf92aa5cd826e"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_SARADC

    <a id="_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_AUDPE"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_AUDPE"></a> <a id="_CPPv2N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_AUDPE"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8ca00e7f79272e62bad3514e4a86c355115"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_AUDP

    <a id="_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_VIDPE"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_VIDPE"></a> <a id="_CPPv2N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_VIDPE"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8ca149eb088c4c2c3b3c5e105c4410dac35"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_VIDP

    <a id="_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_BTSPE"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_BTSPE"></a> <a id="_CPPv2N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_BTSPE"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8ca503f681d60b9706eebe3acfdd1ba74a4"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_BTSP

    <a id="_CPPv4N22pm_sleep_module_name_e30PM_SLEEP_MODULE_NAME_WIFIP_MACE"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e30PM_SLEEP_MODULE_NAME_WIFIP_MACE"></a> <a id="_CPPv2N22pm_sleep_module_name_e30PM_SLEEP_MODULE_NAME_WIFIP_MACE"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8caeb6f88cb6257aabf4f2df4ffce4ab5d3"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_WIFIP\_MAC

    <a id="_CPPv4N22pm_sleep_module_name_e29PM_SLEEP_MODULE_NAME_WIFI_PHYE"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e29PM_SLEEP_MODULE_NAME_WIFI_PHYE"></a> <a id="_CPPv2N22pm_sleep_module_name_e29PM_SLEEP_MODULE_NAME_WIFI_PHYE"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8caedbcb73b854b4ba40f99835561cf79c0"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_WIFI\_PHY

    <a id="_CPPv4N22pm_sleep_module_name_e28PM_SLEEP_MODULE_NAME_TIMER_2E"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e28PM_SLEEP_MODULE_NAME_TIMER_2E"></a> <a id="_CPPv2N22pm_sleep_module_name_e28PM_SLEEP_MODULE_NAME_TIMER_2E"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8ca7d3d82529c09fa2edc74e8a3b5901a48"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_TIMER\_2

    <a id="_CPPv4N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_APPE"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_APPE"></a> <a id="_CPPv2N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_APPE"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8caf10eedff7c800a2cd3339031a2067ae1"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_APP

    <a id="_CPPv4N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_OTPE"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_OTPE"></a> <a id="_CPPv2N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_OTPE"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8ca0807ff83595334ba6acb2a40cc78faea"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_OTP

    <a id="_CPPv4N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_I2S_1E"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_I2S_1E"></a> <a id="_CPPv2N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_I2S_1E"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8caeb2493bf3a428326143c39d568cbb793"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_I2S\_1

    <a id="_CPPv4N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_USB_1E"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_USB_1E"></a> <a id="_CPPv2N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_USB_1E"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8ca8e43f88bda8a470161e826196016d038"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_USB\_1

    <a id="_CPPv4N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_CANE"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_CANE"></a> <a id="_CPPv2N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_CANE"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8ca08f2d87034ed75e35a7f5f0982899878"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_CAN

    <a id="_CPPv4N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_PSRAME"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_PSRAME"></a> <a id="_CPPv2N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_PSRAME"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8ca66c5a8687fdce6b2d04193e8ffbe819f"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_PSRAM

    <a id="_CPPv4N22pm_sleep_module_name_e27PM_SLEEP_MODULE_NAME_QSPI_1E"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e27PM_SLEEP_MODULE_NAME_QSPI_1E"></a> <a id="_CPPv2N22pm_sleep_module_name_e27PM_SLEEP_MODULE_NAME_QSPI_1E"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8ca05b2bd5d39544d3e21d216bf956d9969"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_QSPI\_1

    <a id="_CPPv4N22pm_sleep_module_name_e27PM_SLEEP_MODULE_NAME_QSPI_2E"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e27PM_SLEEP_MODULE_NAME_QSPI_2E"></a> <a id="_CPPv2N22pm_sleep_module_name_e27PM_SLEEP_MODULE_NAME_QSPI_2E"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8cae0aa96ec7280fac8004ba27054f41657"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_QSPI\_2

    <a id="_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_SDIOE"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_SDIOE"></a> <a id="_CPPv2N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_SDIOE"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8cadfe25fbbe533bf041dccbfe015b076b1"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_SDIO

    <a id="_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_AUXSE"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_AUXSE"></a> <a id="_CPPv2N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_AUXSE"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8ca25c57cea4f95ec9b2e4c0ed2c4195237"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_AUXS

    <a id="_CPPv4N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_LOGE"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_LOGE"></a> <a id="_CPPv2N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_LOGE"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8cab2a765d9e692eee348628df327642d74"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_LOG

    <a id="_CPPv4N22pm_sleep_module_name_e23PM_SLEEP_MODULE_NAME_ATE"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e23PM_SLEEP_MODULE_NAME_ATE"></a> <a id="_CPPv2N22pm_sleep_module_name_e23PM_SLEEP_MODULE_NAME_ATE"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8cad2d0d81d5aa79476b95a232d244f93bb"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_AT

    <a id="_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_I2C2E"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_I2C2E"></a> <a id="_CPPv2N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_I2C2E"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8ca60aa72d2c2e7d253c424d2f119c93013"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_I2C2

    <a id="_CPPv4N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_UART2E"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_UART2E"></a> <a id="_CPPv2N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_UART2E"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8ca1296d32b41b173ab9b25c2cfae98f52f"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_UART2

    <a id="_CPPv4N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_UART3E"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_UART3E"></a> <a id="_CPPv2N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_UART3E"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8cacc98cb35c818b1049cb68c618c103fa8"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_UART3

    <a id="_CPPv4N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_WDGE"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_WDGE"></a> <a id="_CPPv2N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_WDGE"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8caf54bc80a2891b6bece138466cea11d39"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_WDG

    <a id="_CPPv4N22pm_sleep_module_name_e28PM_SLEEP_MODULE_NAME_TIMER_3E"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e28PM_SLEEP_MODULE_NAME_TIMER_3E"></a> <a id="_CPPv2N22pm_sleep_module_name_e28PM_SLEEP_MODULE_NAME_TIMER_3E"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8ca059bce8a427ef27cc8318bb88b753afe"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_TIMER\_3

    <a id="_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_APP1E"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_APP1E"></a> <a id="_CPPv2N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_APP1E"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8cad3eda884f827bf723a59d827f75f87d3"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_APP1

    <a id="_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_CPU1E"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_CPU1E"></a> <a id="_CPPv2N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_CPU1E"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8cafa2ebb18e6503ff69d26823e239993b4"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_CPU1

    <a id="_CPPv4N22pm_sleep_module_name_e30PM_SLEEP_MODULE_NAME_ROSC_PROGE"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e30PM_SLEEP_MODULE_NAME_ROSC_PROGE"></a> <a id="_CPPv2N22pm_sleep_module_name_e30PM_SLEEP_MODULE_NAME_ROSC_PROGE"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8ca1536c01f8705edac152ae1271c3330c3"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_ROSC\_PROG

    <a id="_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_ROSCE"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_ROSCE"></a> <a id="_CPPv2N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_ROSCE"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8cac752f64e2d93adef20bf5a2d58fb7515"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_ROSC

    <a id="_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_ENCPE"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_ENCPE"></a> <a id="_CPPv2N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_ENCPE"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8ca7994ae2783a22dcc57afc37e4197d67d"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_ENCP

    <a id="_CPPv4N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_MAXE"></a>

    <a id="_CPPv3N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_MAXE"></a> <a id="_CPPv2N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_MAXE"></a> <a id="pm_8h_1aa865dd93ab7a4d386825fbc976024b8cac3d64902a934d724c3928864985f936e"></a> enumerator PM\_SLEEP\_MODULE\_NAME\_MAX

<a id="_CPPv423pm_power_module_state_e"></a>

<a id="_CPPv323pm_power_module_state_e"></a> <a id="_CPPv223pm_power_module_state_e"></a> <a id="pm_8h_1a1087f7aca4e59514203a4e26e94969a4"></a> enum pm\_power\_module\_state\_e
:   *Values:*

    <a id="_CPPv4N23pm_power_module_state_e24PM_POWER_MODULE_STATE_ONE"></a>

    <a id="_CPPv3N23pm_power_module_state_e24PM_POWER_MODULE_STATE_ONE"></a> <a id="_CPPv2N23pm_power_module_state_e24PM_POWER_MODULE_STATE_ONE"></a> <a id="pm_8h_1a1087f7aca4e59514203a4e26e94969a4a39749082223512447878b1e1c4803c5c"></a> enumerator PM\_POWER\_MODULE\_STATE\_ON

    <a id="_CPPv4N23pm_power_module_state_e25PM_POWER_MODULE_STATE_OFFE"></a>

    <a id="_CPPv3N23pm_power_module_state_e25PM_POWER_MODULE_STATE_OFFE"></a> <a id="_CPPv2N23pm_power_module_state_e25PM_POWER_MODULE_STATE_OFFE"></a> <a id="pm_8h_1a1087f7aca4e59514203a4e26e94969a4a824f36e6b8fd936337bb157426e19dcf"></a> enumerator PM\_POWER\_MODULE\_STATE\_OFF

    <a id="_CPPv4N23pm_power_module_state_e26PM_POWER_MODULE_STATE_NONEE"></a>

    <a id="_CPPv3N23pm_power_module_state_e26PM_POWER_MODULE_STATE_NONEE"></a> <a id="_CPPv2N23pm_power_module_state_e26PM_POWER_MODULE_STATE_NONEE"></a> <a id="pm_8h_1a1087f7aca4e59514203a4e26e94969a4a1d802a10f4cbeb04d2184cd813686510"></a> enumerator PM\_POWER\_MODULE\_STATE\_NONE

<a id="_CPPv416pm_module_name_e"></a>

<a id="_CPPv316pm_module_name_e"></a> <a id="_CPPv216pm_module_name_e"></a> <a id="pm_8h_1a42df214a2ebf985fa7a6b72d02c96517"></a> enum pm\_module\_name\_e
:   *Values:*

    <a id="_CPPv4N16pm_module_name_e19PM_MODULE_NAME_WIFIE"></a>

    <a id="_CPPv3N16pm_module_name_e19PM_MODULE_NAME_WIFIE"></a> <a id="_CPPv2N16pm_module_name_e19PM_MODULE_NAME_WIFIE"></a> <a id="pm_8h_1a42df214a2ebf985fa7a6b72d02c96517aaab190f4949f4a39895354587f553e69"></a> enumerator PM\_MODULE\_NAME\_WIFI

    <a id="_CPPv4N16pm_module_name_e17PM_MODULE_NAME_BTE"></a>

    <a id="_CPPv3N16pm_module_name_e17PM_MODULE_NAME_BTE"></a> <a id="_CPPv2N16pm_module_name_e17PM_MODULE_NAME_BTE"></a> <a id="pm_8h_1a42df214a2ebf985fa7a6b72d02c96517af66ef8e9d5ade22b8b6131ec9c540931"></a> enumerator PM\_MODULE\_NAME\_BT

    <a id="_CPPv4N16pm_module_name_e19PM_MODULE_NAME_NONEE"></a>

    <a id="_CPPv3N16pm_module_name_e19PM_MODULE_NAME_NONEE"></a> <a id="_CPPv2N16pm_module_name_e19PM_MODULE_NAME_NONEE"></a> <a id="pm_8h_1a42df214a2ebf985fa7a6b72d02c96517a488992a67ca700826222f63986c31533"></a> enumerator PM\_MODULE\_NAME\_NONE

<a id="_CPPv412pm_lpo_src_e"></a>

<a id="_CPPv312pm_lpo_src_e"></a> <a id="_CPPv212pm_lpo_src_e"></a> <a id="pm_8h_1ac637df4ac37d413c198d5c46cab7ee48"></a> enum pm\_lpo\_src\_e
:   *Values:*

    <a id="_CPPv4N12pm_lpo_src_e15PM_LPO_SRC_DIVDE"></a>

    <a id="_CPPv3N12pm_lpo_src_e15PM_LPO_SRC_DIVDE"></a> <a id="_CPPv2N12pm_lpo_src_e15PM_LPO_SRC_DIVDE"></a> <a id="pm_8h_1ac637df4ac37d413c198d5c46cab7ee48ad71607b6c90a4a1879c406073a995c3d"></a> enumerator PM\_LPO\_SRC\_DIVD

    <a id="_CPPv4N12pm_lpo_src_e15PM_LPO_SRC_X32KE"></a>

    <a id="_CPPv3N12pm_lpo_src_e15PM_LPO_SRC_X32KE"></a> <a id="_CPPv2N12pm_lpo_src_e15PM_LPO_SRC_X32KE"></a> <a id="pm_8h_1ac637df4ac37d413c198d5c46cab7ee48a666b09005f90cbe3f0ec4afc149099e1"></a> enumerator PM\_LPO\_SRC\_X32K

    <a id="_CPPv4N12pm_lpo_src_e15PM_LPO_SRC_ROSCE"></a>

    <a id="_CPPv3N12pm_lpo_src_e15PM_LPO_SRC_ROSCE"></a> <a id="_CPPv2N12pm_lpo_src_e15PM_LPO_SRC_ROSCE"></a> <a id="pm_8h_1ac637df4ac37d413c198d5c46cab7ee48a2f38527a55a1e4c32ca942fe876615cc"></a> enumerator PM\_LPO\_SRC\_ROSC

    <a id="_CPPv4N12pm_lpo_src_e18PM_LPO_SRC_DEFAULTE"></a>

    <a id="_CPPv3N12pm_lpo_src_e18PM_LPO_SRC_DEFAULTE"></a> <a id="_CPPv2N12pm_lpo_src_e18PM_LPO_SRC_DEFAULTE"></a> <a id="pm_8h_1ac637df4ac37d413c198d5c46cab7ee48a16214fbac2117b2d3d091d43b14c41dc"></a> enumerator PM\_LPO\_SRC\_DEFAULT

<a id="_CPPv416pm_dev_clk_pwr_e"></a>

<a id="_CPPv316pm_dev_clk_pwr_e"></a> <a id="_CPPv216pm_dev_clk_pwr_e"></a> <a id="pm_8h_1ac7d278ebb2c4231e0142c4915ee3ffed"></a> enum pm\_dev\_clk\_pwr\_e
:   *Values:*

    <a id="_CPPv4N16pm_dev_clk_pwr_e20PM_CLK_CTRL_PWR_DOWNE"></a>

    <a id="_CPPv3N16pm_dev_clk_pwr_e20PM_CLK_CTRL_PWR_DOWNE"></a> <a id="_CPPv2N16pm_dev_clk_pwr_e20PM_CLK_CTRL_PWR_DOWNE"></a> <a id="pm_8h_1ac7d278ebb2c4231e0142c4915ee3ffeda95a6d348aa8a9ebf0ad222e6b73dee59"></a> enumerator PM\_CLK\_CTRL\_PWR\_DOWN

    <a id="_CPPv4N16pm_dev_clk_pwr_e18PM_CLK_CTRL_PWR_UPE"></a>

    <a id="_CPPv3N16pm_dev_clk_pwr_e18PM_CLK_CTRL_PWR_UPE"></a> <a id="_CPPv2N16pm_dev_clk_pwr_e18PM_CLK_CTRL_PWR_UPE"></a> <a id="pm_8h_1ac7d278ebb2c4231e0142c4915ee3ffeda3334b34b13f5fbddae128b274b84365b"></a> enumerator PM\_CLK\_CTRL\_PWR\_UP

<a id="_CPPv411pm_dev_id_e"></a>

<a id="_CPPv311pm_dev_id_e"></a> <a id="_CPPv211pm_dev_id_e"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541"></a> enum pm\_dev\_id\_e
:   *Values:*

    <a id="_CPPv4N11pm_dev_id_e17PM_DEV_ID_TIMER_0E"></a>

    <a id="_CPPv3N11pm_dev_id_e17PM_DEV_ID_TIMER_0E"></a> <a id="_CPPv2N11pm_dev_id_e17PM_DEV_ID_TIMER_0E"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541aac80957faa0b5f79ace80a9de9a1bfc1"></a> enumerator PM\_DEV\_ID\_TIMER\_0

    <a id="_CPPv4N11pm_dev_id_e14PM_DEV_ID_I2C1E"></a>

    <a id="_CPPv3N11pm_dev_id_e14PM_DEV_ID_I2C1E"></a> <a id="_CPPv2N11pm_dev_id_e14PM_DEV_ID_I2C1E"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541ac675d8fb0c8307c6e0fdc10292b143ff"></a> enumerator PM\_DEV\_ID\_I2C1

    <a id="_CPPv4N11pm_dev_id_e15PM_DEV_ID_SPI_1E"></a>

    <a id="_CPPv3N11pm_dev_id_e15PM_DEV_ID_SPI_1E"></a> <a id="_CPPv2N11pm_dev_id_e15PM_DEV_ID_SPI_1E"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541aaa4ffb29804d81b3a3e2fbc652ddc140"></a> enumerator PM\_DEV\_ID\_SPI\_1

    <a id="_CPPv4N11pm_dev_id_e15PM_DEV_ID_UART1E"></a>

    <a id="_CPPv3N11pm_dev_id_e15PM_DEV_ID_UART1E"></a> <a id="_CPPv2N11pm_dev_id_e15PM_DEV_ID_UART1E"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541ae903eb3f336100261220ec51c2d76b14"></a> enumerator PM\_DEV\_ID\_UART1

    <a id="_CPPv4N11pm_dev_id_e17PM_DEV_ID_AIRPLAYE"></a>

    <a id="_CPPv3N11pm_dev_id_e17PM_DEV_ID_AIRPLAYE"></a> <a id="_CPPv2N11pm_dev_id_e17PM_DEV_ID_AIRPLAYE"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541ae18ab58854753952e386c47f74b47a8e"></a> enumerator PM\_DEV\_ID\_AIRPLAY

    <a id="_CPPv4N11pm_dev_id_e17PM_DEV_ID_TIMER_1E"></a>

    <a id="_CPPv3N11pm_dev_id_e17PM_DEV_ID_TIMER_1E"></a> <a id="_CPPv2N11pm_dev_id_e17PM_DEV_ID_TIMER_1E"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a98e4f7d01ab826b3d3f7818090fd5fb3"></a> enumerator PM\_DEV\_ID\_TIMER\_1

    <a id="_CPPv4N11pm_dev_id_e16PM_DEV_ID_SARADCE"></a>

    <a id="_CPPv3N11pm_dev_id_e16PM_DEV_ID_SARADCE"></a> <a id="_CPPv2N11pm_dev_id_e16PM_DEV_ID_SARADCE"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541abe66d411c8bcea29d63b05063ce4c367"></a> enumerator PM\_DEV\_ID\_SARADC

    <a id="_CPPv4N11pm_dev_id_e14PM_DEV_ID_IRDAE"></a>

    <a id="_CPPv3N11pm_dev_id_e14PM_DEV_ID_IRDAE"></a> <a id="_CPPv2N11pm_dev_id_e14PM_DEV_ID_IRDAE"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a200e558d27ff277583dc27c7bb3701c1"></a> enumerator PM\_DEV\_ID\_IRDA

    <a id="_CPPv4N11pm_dev_id_e15PM_DEV_ID_EFUSEE"></a>

    <a id="_CPPv3N11pm_dev_id_e15PM_DEV_ID_EFUSEE"></a> <a id="_CPPv2N11pm_dev_id_e15PM_DEV_ID_EFUSEE"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541ae0873ed5007ffdd1443764d578d8b02c"></a> enumerator PM\_DEV\_ID\_EFUSE

    <a id="_CPPv4N11pm_dev_id_e14PM_DEV_ID_I2C2E"></a>

    <a id="_CPPv3N11pm_dev_id_e14PM_DEV_ID_I2C2E"></a> <a id="_CPPv2N11pm_dev_id_e14PM_DEV_ID_I2C2E"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a2e0b5318b1503d1e6ff3241358028ebb"></a> enumerator PM\_DEV\_ID\_I2C2

    <a id="_CPPv4N11pm_dev_id_e15PM_DEV_ID_SPI_2E"></a>

    <a id="_CPPv3N11pm_dev_id_e15PM_DEV_ID_SPI_2E"></a> <a id="_CPPv2N11pm_dev_id_e15PM_DEV_ID_SPI_2E"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541ac9266da486969cc460e2e5ce1e19378b"></a> enumerator PM\_DEV\_ID\_SPI\_2

    <a id="_CPPv4N11pm_dev_id_e15PM_DEV_ID_UART2E"></a>

    <a id="_CPPv3N11pm_dev_id_e15PM_DEV_ID_UART2E"></a> <a id="_CPPv2N11pm_dev_id_e15PM_DEV_ID_UART2E"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a8e991d16431123280e4a552f8f0d6a40"></a> enumerator PM\_DEV\_ID\_UART2

    <a id="_CPPv4N11pm_dev_id_e15PM_DEV_ID_UART3E"></a>

    <a id="_CPPv3N11pm_dev_id_e15PM_DEV_ID_UART3E"></a> <a id="_CPPv2N11pm_dev_id_e15PM_DEV_ID_UART3E"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a46ab7d7652fa9a85f6f9df853c54362f"></a> enumerator PM\_DEV\_ID\_UART3

    <a id="_CPPv4N11pm_dev_id_e15PM_DEV_ID_PWM_2E"></a>

    <a id="_CPPv3N11pm_dev_id_e15PM_DEV_ID_PWM_2E"></a> <a id="_CPPv2N11pm_dev_id_e15PM_DEV_ID_PWM_2E"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a7fec1168779742af1ef954dab9fda541"></a> enumerator PM\_DEV\_ID\_PWM\_2

    <a id="_CPPv4N11pm_dev_id_e17PM_DEV_ID_TIMER_2E"></a>

    <a id="_CPPv3N11pm_dev_id_e17PM_DEV_ID_TIMER_2E"></a> <a id="_CPPv2N11pm_dev_id_e17PM_DEV_ID_TIMER_2E"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a53eb0582feff206817f62d1d4506e160"></a> enumerator PM\_DEV\_ID\_TIMER\_2

    <a id="_CPPv4N11pm_dev_id_e17PM_DEV_ID_TIMER_3E"></a>

    <a id="_CPPv3N11pm_dev_id_e17PM_DEV_ID_TIMER_3E"></a> <a id="_CPPv2N11pm_dev_id_e17PM_DEV_ID_TIMER_3E"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a9da105c021a2af87b7b0192ca2f20d03"></a> enumerator PM\_DEV\_ID\_TIMER\_3

    <a id="_CPPv4N11pm_dev_id_e15PM_DEV_ID_I2S_1E"></a>

    <a id="_CPPv3N11pm_dev_id_e15PM_DEV_ID_I2S_1E"></a> <a id="_CPPv2N11pm_dev_id_e15PM_DEV_ID_I2S_1E"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541ac84f5d401ac93a1f21a0bdd4964b453f"></a> enumerator PM\_DEV\_ID\_I2S\_1

    <a id="_CPPv4N11pm_dev_id_e15PM_DEV_ID_USB_1E"></a>

    <a id="_CPPv3N11pm_dev_id_e15PM_DEV_ID_USB_1E"></a> <a id="_CPPv2N11pm_dev_id_e15PM_DEV_ID_USB_1E"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a8cf9789925acddda727b1a401e79f63f"></a> enumerator PM\_DEV\_ID\_USB\_1

    <a id="_CPPv4N11pm_dev_id_e15PM_DEV_ID_PSRAME"></a>

    <a id="_CPPv3N11pm_dev_id_e15PM_DEV_ID_PSRAME"></a> <a id="_CPPv2N11pm_dev_id_e15PM_DEV_ID_PSRAME"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a77a88353df92a293d51ea9083a5a8418"></a> enumerator PM\_DEV\_ID\_PSRAM

    <a id="_CPPv4N11pm_dev_id_e16PM_DEV_ID_QSPI_1E"></a>

    <a id="_CPPv3N11pm_dev_id_e16PM_DEV_ID_QSPI_1E"></a> <a id="_CPPv2N11pm_dev_id_e16PM_DEV_ID_QSPI_1E"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a9633588a2ec468771a2dfc7e8d92f77f"></a> enumerator PM\_DEV\_ID\_QSPI\_1

    <a id="_CPPv4N11pm_dev_id_e16PM_DEV_ID_QSPI_2E"></a>

    <a id="_CPPv3N11pm_dev_id_e16PM_DEV_ID_QSPI_2E"></a> <a id="_CPPv2N11pm_dev_id_e16PM_DEV_ID_QSPI_2E"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a1e3dd693e715bf79c4e992f7fc6807c4"></a> enumerator PM\_DEV\_ID\_QSPI\_2

    <a id="_CPPv4N11pm_dev_id_e14PM_DEV_ID_SDIOE"></a>

    <a id="_CPPv3N11pm_dev_id_e14PM_DEV_ID_SDIOE"></a> <a id="_CPPv2N11pm_dev_id_e14PM_DEV_ID_SDIOE"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a1b09793ea1688130115d95a1c82a4528"></a> enumerator PM\_DEV\_ID\_SDIO

    <a id="_CPPv4N11pm_dev_id_e14PM_DEV_ID_AUXSE"></a>

    <a id="_CPPv3N11pm_dev_id_e14PM_DEV_ID_AUXSE"></a> <a id="_CPPv2N11pm_dev_id_e14PM_DEV_ID_AUXSE"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a5905a23982045dec815c86fcbc04f167"></a> enumerator PM\_DEV\_ID\_AUXS

    <a id="_CPPv4N11pm_dev_id_e14PM_DEV_ID_BTDME"></a>

    <a id="_CPPv3N11pm_dev_id_e14PM_DEV_ID_BTDME"></a> <a id="_CPPv2N11pm_dev_id_e14PM_DEV_ID_BTDME"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a4579f3991f6a6c7764ea9671ca4b6ece"></a> enumerator PM\_DEV\_ID\_BTDM

    <a id="_CPPv4N11pm_dev_id_e14PM_DEV_ID_WPASE"></a>

    <a id="_CPPv3N11pm_dev_id_e14PM_DEV_ID_WPASE"></a> <a id="_CPPv2N11pm_dev_id_e14PM_DEV_ID_WPASE"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541af3842312272d1dbc572a52a9ecc99bc6"></a> enumerator PM\_DEV\_ID\_WPAS

    <a id="_CPPv4N11pm_dev_id_e13PM_DEV_ID_PHYE"></a>

    <a id="_CPPv3N11pm_dev_id_e13PM_DEV_ID_PHYE"></a> <a id="_CPPv2N11pm_dev_id_e13PM_DEV_ID_PHYE"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a180bdc771ba3807a81e9979bd9d1145d"></a> enumerator PM\_DEV\_ID\_PHY

    <a id="_CPPv4N11pm_dev_id_e13PM_DEV_ID_RTCE"></a>

    <a id="_CPPv3N11pm_dev_id_e13PM_DEV_ID_RTCE"></a> <a id="_CPPv2N11pm_dev_id_e13PM_DEV_ID_RTCE"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a11211a7ede02c7c4fc95e9a41fdb1f32"></a> enumerator PM\_DEV\_ID\_RTC

    <a id="_CPPv4N11pm_dev_id_e14PM_DEV_ID_GPIOE"></a>

    <a id="_CPPv3N11pm_dev_id_e14PM_DEV_ID_GPIOE"></a> <a id="_CPPv2N11pm_dev_id_e14PM_DEV_ID_GPIOE"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541ac90ded0e855ad2857149d043e8f1ded7"></a> enumerator PM\_DEV\_ID\_GPIO

    <a id="_CPPv4N11pm_dev_id_e15PM_DEV_ID_PWM_1E"></a>

    <a id="_CPPv3N11pm_dev_id_e15PM_DEV_ID_PWM_1E"></a> <a id="_CPPv2N11pm_dev_id_e15PM_DEV_ID_PWM_1E"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a3ba61f6748613e3226b88e20e58cbcd9"></a> enumerator PM\_DEV\_ID\_PWM\_1

    <a id="_CPPv4N11pm_dev_id_e22PM_DEV_ID_SECURE_WORLDE"></a>

    <a id="_CPPv3N11pm_dev_id_e22PM_DEV_ID_SECURE_WORLDE"></a> <a id="_CPPv2N11pm_dev_id_e22PM_DEV_ID_SECURE_WORLDE"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a6b25e2b7925ec25b3133151480a047b9"></a> enumerator PM\_DEV\_ID\_SECURE\_WORLD

    <a id="_CPPv4N11pm_dev_id_e15PM_DEV_ID_UART4E"></a>

    <a id="_CPPv3N11pm_dev_id_e15PM_DEV_ID_UART4E"></a> <a id="_CPPv2N11pm_dev_id_e15PM_DEV_ID_UART4E"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a82df781f37c380d544efb4e00dcf6e2f"></a> enumerator PM\_DEV\_ID\_UART4

    <a id="_CPPv4N11pm_dev_id_e14PM_DEV_ID_TRNGE"></a>

    <a id="_CPPv3N11pm_dev_id_e14PM_DEV_ID_TRNGE"></a> <a id="_CPPv2N11pm_dev_id_e14PM_DEV_ID_TRNGE"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a6e639061a5f08f4a941f7d40a00a3149"></a> enumerator PM\_DEV\_ID\_TRNG

    <a id="_CPPv4N11pm_dev_id_e22PM_DEV_ID_PHY_DPD_CALIE"></a>

    <a id="_CPPv3N11pm_dev_id_e22PM_DEV_ID_PHY_DPD_CALIE"></a> <a id="_CPPv2N11pm_dev_id_e22PM_DEV_ID_PHY_DPD_CALIE"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541ac23add61d3b02627ba5b706c56e6503f"></a> enumerator PM\_DEV\_ID\_PHY\_DPD\_CALI

    <a id="_CPPv4N11pm_dev_id_e13PM_DEV_ID_MACE"></a>

    <a id="_CPPv3N11pm_dev_id_e13PM_DEV_ID_MACE"></a> <a id="_CPPv2N11pm_dev_id_e13PM_DEV_ID_MACE"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a06ce4ab07d7c29f8cc66e984b2324611"></a> enumerator PM\_DEV\_ID\_MAC

    <a id="_CPPv4N11pm_dev_id_e17PM_DEV_ID_DEFAULTE"></a>

    <a id="_CPPv3N11pm_dev_id_e17PM_DEV_ID_DEFAULTE"></a> <a id="_CPPv2N11pm_dev_id_e17PM_DEV_ID_DEFAULTE"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541aba10581e9835ae209622e0744b29e633"></a> enumerator PM\_DEV\_ID\_DEFAULT

    <a id="_CPPv4N11pm_dev_id_e13PM_DEV_ID_MAXE"></a>

    <a id="_CPPv3N11pm_dev_id_e13PM_DEV_ID_MAXE"></a> <a id="_CPPv2N11pm_dev_id_e13PM_DEV_ID_MAXE"></a> <a id="pm_8h_1a54e97824c9150c5632fb771f317a9541a0375b49d564eda46f5ca08cac2726309"></a> enumerator PM\_DEV\_ID\_MAX

<a id="_CPPv413pm_cpu_freq_e"></a>

<a id="_CPPv313pm_cpu_freq_e"></a> <a id="_CPPv213pm_cpu_freq_e"></a> <a id="pm_8h_1ae5eeebe678bcda0e81503ec569b2b386"></a> enum pm\_cpu\_freq\_e
:   *Values:*

    <a id="_CPPv4N13pm_cpu_freq_e15PM_CPU_FRQ_XTALE"></a>

    <a id="_CPPv3N13pm_cpu_freq_e15PM_CPU_FRQ_XTALE"></a> <a id="_CPPv2N13pm_cpu_freq_e15PM_CPU_FRQ_XTALE"></a> <a id="pm_8h_1ae5eeebe678bcda0e81503ec569b2b386accef45b01117f5cde9b1cdd18a0173d8"></a> enumerator PM\_CPU\_FRQ\_XTAL

    <a id="_CPPv4N13pm_cpu_freq_e14PM_CPU_FRQ_60ME"></a>

    <a id="_CPPv3N13pm_cpu_freq_e14PM_CPU_FRQ_60ME"></a> <a id="_CPPv2N13pm_cpu_freq_e14PM_CPU_FRQ_60ME"></a> <a id="pm_8h_1ae5eeebe678bcda0e81503ec569b2b386a1f60de573e5bef640fd986976fc7e370"></a> enumerator PM\_CPU\_FRQ\_60M

    <a id="_CPPv4N13pm_cpu_freq_e14PM_CPU_FRQ_80ME"></a>

    <a id="_CPPv3N13pm_cpu_freq_e14PM_CPU_FRQ_80ME"></a> <a id="_CPPv2N13pm_cpu_freq_e14PM_CPU_FRQ_80ME"></a> <a id="pm_8h_1ae5eeebe678bcda0e81503ec569b2b386a4b1014c264ffb610764671a788fb8bf7"></a> enumerator PM\_CPU\_FRQ\_80M

    <a id="_CPPv4N13pm_cpu_freq_e15PM_CPU_FRQ_120ME"></a>

    <a id="_CPPv3N13pm_cpu_freq_e15PM_CPU_FRQ_120ME"></a> <a id="_CPPv2N13pm_cpu_freq_e15PM_CPU_FRQ_120ME"></a> <a id="pm_8h_1ae5eeebe678bcda0e81503ec569b2b386a3da160e5b74f06a93cc451c11e28a3a7"></a> enumerator PM\_CPU\_FRQ\_120M

    <a id="_CPPv4N13pm_cpu_freq_e15PM_CPU_FRQ_160ME"></a>

    <a id="_CPPv3N13pm_cpu_freq_e15PM_CPU_FRQ_160ME"></a> <a id="_CPPv2N13pm_cpu_freq_e15PM_CPU_FRQ_160ME"></a> <a id="pm_8h_1ae5eeebe678bcda0e81503ec569b2b386a18a37ee7687200c8ed3fde74c418ace4"></a> enumerator PM\_CPU\_FRQ\_160M

    <a id="_CPPv4N13pm_cpu_freq_e15PM_CPU_FRQ_240ME"></a>

    <a id="_CPPv3N13pm_cpu_freq_e15PM_CPU_FRQ_240ME"></a> <a id="_CPPv2N13pm_cpu_freq_e15PM_CPU_FRQ_240ME"></a> <a id="pm_8h_1ae5eeebe678bcda0e81503ec569b2b386a1baa40ec15a3eb2e36e5cbf1e2f85a2d"></a> enumerator PM\_CPU\_FRQ\_240M

    <a id="_CPPv4N13pm_cpu_freq_e15PM_CPU_FRQ_320ME"></a>

    <a id="_CPPv3N13pm_cpu_freq_e15PM_CPU_FRQ_320ME"></a> <a id="_CPPv2N13pm_cpu_freq_e15PM_CPU_FRQ_320ME"></a> <a id="pm_8h_1ae5eeebe678bcda0e81503ec569b2b386a52ac263df4e5bf4966d30b2aed070b5a"></a> enumerator PM\_CPU\_FRQ\_320M

    <a id="_CPPv4N13pm_cpu_freq_e15PM_CPU_FRQ_480ME"></a>

    <a id="_CPPv3N13pm_cpu_freq_e15PM_CPU_FRQ_480ME"></a> <a id="_CPPv2N13pm_cpu_freq_e15PM_CPU_FRQ_480ME"></a> <a id="pm_8h_1ae5eeebe678bcda0e81503ec569b2b386ae6803aadaee5017d1209f2bd71f63be8"></a> enumerator PM\_CPU\_FRQ\_480M

    <a id="_CPPv4N13pm_cpu_freq_e18PM_CPU_FRQ_HIGHESTE"></a>

    <a id="_CPPv3N13pm_cpu_freq_e18PM_CPU_FRQ_HIGHESTE"></a> <a id="_CPPv2N13pm_cpu_freq_e18PM_CPU_FRQ_HIGHESTE"></a> <a id="pm_8h_1ae5eeebe678bcda0e81503ec569b2b386a8b37a47956ed5d9ccf57b7fded508e34"></a> enumerator PM\_CPU\_FRQ\_HIGHEST

    <a id="_CPPv4N13pm_cpu_freq_e18PM_CPU_FRQ_DEFAULTE"></a>

    <a id="_CPPv3N13pm_cpu_freq_e18PM_CPU_FRQ_DEFAULTE"></a> <a id="_CPPv2N13pm_cpu_freq_e18PM_CPU_FRQ_DEFAULTE"></a> <a id="pm_8h_1ae5eeebe678bcda0e81503ec569b2b386a2e45c2d527cdccd0aa24a4c676e7857c"></a> enumerator PM\_CPU\_FRQ\_DEFAULT

<a id="_CPPv419pm_rosc_cali_mode_e"></a>

<a id="_CPPv319pm_rosc_cali_mode_e"></a> <a id="_CPPv219pm_rosc_cali_mode_e"></a> <a id="pm_8h_1ab03c1e8155833bd1e3257169d8d88fad"></a> enum pm\_rosc\_cali\_mode\_e
:   *Values:*

    <a id="_CPPv4N19pm_rosc_cali_mode_e17PM_ROSC_CALI_AUTOE"></a>

    <a id="_CPPv3N19pm_rosc_cali_mode_e17PM_ROSC_CALI_AUTOE"></a> <a id="_CPPv2N19pm_rosc_cali_mode_e17PM_ROSC_CALI_AUTOE"></a> <a id="pm_8h_1ab03c1e8155833bd1e3257169d8d88fada89728df96dff5406f7e3157fbdd8b1ac"></a> enumerator PM\_ROSC\_CALI\_AUTO

    <a id="_CPPv4N19pm_rosc_cali_mode_e19PM_ROSC_CALI_MANUALE"></a>

    <a id="_CPPv3N19pm_rosc_cali_mode_e19PM_ROSC_CALI_MANUALE"></a> <a id="_CPPv2N19pm_rosc_cali_mode_e19PM_ROSC_CALI_MANUALE"></a> <a id="pm_8h_1ab03c1e8155833bd1e3257169d8d88fada1f1e5cfb153503b64d18d9774042742a"></a> enumerator PM\_ROSC\_CALI\_MANUAL

    <a id="_CPPv4N19pm_rosc_cali_mode_e17PM_ROSC_CALI_STOPE"></a>

    <a id="_CPPv3N19pm_rosc_cali_mode_e17PM_ROSC_CALI_STOPE"></a> <a id="_CPPv2N19pm_rosc_cali_mode_e17PM_ROSC_CALI_STOPE"></a> <a id="pm_8h_1ab03c1e8155833bd1e3257169d8d88fada0d718e6c83a5b892753ffc261505b738"></a> enumerator PM\_ROSC\_CALI\_STOP

<a id="_CPPv428pm_enter_lv_timeout_module_e"></a>

<a id="_CPPv328pm_enter_lv_timeout_module_e"></a> <a id="_CPPv228pm_enter_lv_timeout_module_e"></a> <a id="pm_8h_1a7f0d89651cd1ce4a704256c46a847633"></a> enum pm\_enter\_lv\_timeout\_module\_e
:   *Values:*

    <a id="_CPPv4N28pm_enter_lv_timeout_module_e31PM_ENTER_LV_TIME_OUT_MODULE_APPE"></a>

    <a id="_CPPv3N28pm_enter_lv_timeout_module_e31PM_ENTER_LV_TIME_OUT_MODULE_APPE"></a> <a id="_CPPv2N28pm_enter_lv_timeout_module_e31PM_ENTER_LV_TIME_OUT_MODULE_APPE"></a> <a id="pm_8h_1a7f0d89651cd1ce4a704256c46a847633a5edfb25feed941c7da959cb224991ff4"></a> enumerator PM\_ENTER\_LV\_TIME\_OUT\_MODULE\_APP

    <a id="_CPPv4N28pm_enter_lv_timeout_module_e31PM_ENTER_LV_TIME_OUT_MODULE_MAXE"></a>

    <a id="_CPPv3N28pm_enter_lv_timeout_module_e31PM_ENTER_LV_TIME_OUT_MODULE_MAXE"></a> <a id="_CPPv2N28pm_enter_lv_timeout_module_e31PM_ENTER_LV_TIME_OUT_MODULE_MAXE"></a> <a id="pm_8h_1a7f0d89651cd1ce4a704256c46a847633aae60709408e4e251b8c5f9f691c7d24f"></a> enumerator PM\_ENTER\_LV\_TIME\_OUT\_MODULE\_MAX

<a id="_CPPv416pm_cb_priority_e"></a>

<a id="_CPPv316pm_cb_priority_e"></a> <a id="_CPPv216pm_cb_priority_e"></a> <a id="pm_8h_1abeaabf50380c244ebea8ff7827a072e9"></a> enum pm\_cb\_priority\_e
:   *Values:*

    <a id="_CPPv4N16pm_cb_priority_e16PM_CB_PRIORITY_0E"></a>

    <a id="_CPPv3N16pm_cb_priority_e16PM_CB_PRIORITY_0E"></a> <a id="_CPPv2N16pm_cb_priority_e16PM_CB_PRIORITY_0E"></a> <a id="pm_8h_1abeaabf50380c244ebea8ff7827a072e9a1c7fdf651720a7e71cff4d29eea6d31a"></a> enumerator PM\_CB\_PRIORITY\_0

    <a id="_CPPv4N16pm_cb_priority_e16PM_CB_PRIORITY_1E"></a>

    <a id="_CPPv3N16pm_cb_priority_e16PM_CB_PRIORITY_1E"></a> <a id="_CPPv2N16pm_cb_priority_e16PM_CB_PRIORITY_1E"></a> <a id="pm_8h_1abeaabf50380c244ebea8ff7827a072e9a216a4784d9a8fb56a2be8a15dff9812a"></a> enumerator PM\_CB\_PRIORITY\_1

    <a id="_CPPv4N16pm_cb_priority_e16PM_CB_PRIORITY_2E"></a>

    <a id="_CPPv3N16pm_cb_priority_e16PM_CB_PRIORITY_2E"></a> <a id="_CPPv2N16pm_cb_priority_e16PM_CB_PRIORITY_2E"></a> <a id="pm_8h_1abeaabf50380c244ebea8ff7827a072e9a04c65c01ea4bae7601fb5921dfd7f79a"></a> enumerator PM\_CB\_PRIORITY\_2

    <a id="_CPPv4N16pm_cb_priority_e16PM_CB_PRIORITY_3E"></a>

    <a id="_CPPv3N16pm_cb_priority_e16PM_CB_PRIORITY_3E"></a> <a id="_CPPv2N16pm_cb_priority_e16PM_CB_PRIORITY_3E"></a> <a id="pm_8h_1abeaabf50380c244ebea8ff7827a072e9a50c5f83e8ad5198fdf5c8c7b819dcdf1"></a> enumerator PM\_CB\_PRIORITY\_3

    <a id="_CPPv4N16pm_cb_priority_e18PM_CB_PRIORITY_MAXE"></a>

    <a id="_CPPv3N16pm_cb_priority_e18PM_CB_PRIORITY_MAXE"></a> <a id="_CPPv2N16pm_cb_priority_e18PM_CB_PRIORITY_MAXE"></a> <a id="pm_8h_1abeaabf50380c244ebea8ff7827a072e9a05799c85295f40810b0adeee49363329"></a> enumerator PM\_CB\_PRIORITY\_MAX

<a id="_CPPv414pm_cb_module_e"></a>

<a id="_CPPv314pm_cb_module_e"></a> <a id="_CPPv214pm_cb_module_e"></a> <a id="pm_8h_1a1aaf38ec5512672c88a57750c203e719"></a> enum pm\_cb\_module\_e
:   *Values:*

    <a id="_CPPv4N14pm_cb_module_e16PM_32K_MODULE_BTE"></a>

    <a id="_CPPv3N14pm_cb_module_e16PM_32K_MODULE_BTE"></a> <a id="_CPPv2N14pm_cb_module_e16PM_32K_MODULE_BTE"></a> <a id="pm_8h_1a1aaf38ec5512672c88a57750c203e719a5fe4c2f08c35286d3e382e10db9f7c6c"></a> enumerator PM\_32K\_MODULE\_BT

    <a id="_CPPv4N14pm_cb_module_e18PM_32K_MODULE_WIFIE"></a>

    <a id="_CPPv3N14pm_cb_module_e18PM_32K_MODULE_WIFIE"></a> <a id="_CPPv2N14pm_cb_module_e18PM_32K_MODULE_WIFIE"></a> <a id="pm_8h_1a1aaf38ec5512672c88a57750c203e719a1e9b8e5580460103d5d0a503e3501545"></a> enumerator PM\_32K\_MODULE\_WIFI

    <a id="_CPPv4N14pm_cb_module_e17PM_32K_MODULE_MAXE"></a>

    <a id="_CPPv3N14pm_cb_module_e17PM_32K_MODULE_MAXE"></a> <a id="_CPPv2N14pm_cb_module_e17PM_32K_MODULE_MAXE"></a> <a id="pm_8h_1a1aaf38ec5512672c88a57750c203e719a34352e9fe8747d8860c03c2b78ff30de"></a> enumerator PM\_32K\_MODULE\_MAX

<a id="_CPPv412pm_sw_step_e"></a>

<a id="_CPPv312pm_sw_step_e"></a> <a id="_CPPv212pm_sw_step_e"></a> <a id="pm_8h_1ade532cdd1ac720b41100cba1437f12ab"></a> enum pm\_sw\_step\_e
:   *Values:*

    <a id="_CPPv4N12pm_sw_step_e17PM_32K_STEP_BEGINE"></a>

    <a id="_CPPv3N12pm_sw_step_e17PM_32K_STEP_BEGINE"></a> <a id="_CPPv2N12pm_sw_step_e17PM_32K_STEP_BEGINE"></a> <a id="pm_8h_1ade532cdd1ac720b41100cba1437f12aba5092b45a97b21881e36379b6ad88c608"></a> enumerator PM\_32K\_STEP\_BEGIN

    <a id="_CPPv4N12pm_sw_step_e18PM_32K_STEP_FINISHE"></a>

    <a id="_CPPv3N12pm_sw_step_e18PM_32K_STEP_FINISHE"></a> <a id="_CPPv2N12pm_sw_step_e18PM_32K_STEP_FINISHE"></a> <a id="pm_8h_1ade532cdd1ac720b41100cba1437f12aba975081f08de43034d006f9e42e43816d"></a> enumerator PM\_32K\_STEP\_FINISH

<a id="_CPPv420pm_low_vol_voltage_e"></a>

<a id="_CPPv320pm_low_vol_voltage_e"></a> <a id="_CPPv220pm_low_vol_voltage_e"></a> <a id="pm_8h_1a6a4f9c770ed7b8dfea14acfa0c68edb1"></a> enum pm\_low\_vol\_voltage\_e
:   *Values:*

    <a id="_CPPv4N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_0_6E"></a>

    <a id="_CPPv3N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_0_6E"></a> <a id="_CPPv2N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_0_6E"></a> <a id="pm_8h_1a6a4f9c770ed7b8dfea14acfa0c68edb1a54ee2f3123422b02e26bc66cbf2dc3a5"></a> enumerator PM\_LOW\_VOL\_VOLTAGE\_0\_6

    <a id="_CPPv4N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_0_7E"></a>

    <a id="_CPPv3N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_0_7E"></a> <a id="_CPPv2N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_0_7E"></a> <a id="pm_8h_1a6a4f9c770ed7b8dfea14acfa0c68edb1a562a8f8c85f3fef90f279b3f33b32909"></a> enumerator PM\_LOW\_VOL\_VOLTAGE\_0\_7

    <a id="_CPPv4N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_0_8E"></a>

    <a id="_CPPv3N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_0_8E"></a> <a id="_CPPv2N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_0_8E"></a> <a id="pm_8h_1a6a4f9c770ed7b8dfea14acfa0c68edb1a48c0a6d2ea5f2d766b0bec9dedecd8a8"></a> enumerator PM\_LOW\_VOL\_VOLTAGE\_0\_8

    <a id="_CPPv4N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_0_9E"></a>

    <a id="_CPPv3N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_0_9E"></a> <a id="_CPPv2N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_0_9E"></a> <a id="pm_8h_1a6a4f9c770ed7b8dfea14acfa0c68edb1a6861560f7409730d59591a8dc34a449f"></a> enumerator PM\_LOW\_VOL\_VOLTAGE\_0\_9

    <a id="_CPPv4N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_1_0E"></a>

    <a id="_CPPv3N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_1_0E"></a> <a id="_CPPv2N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_1_0E"></a> <a id="pm_8h_1a6a4f9c770ed7b8dfea14acfa0c68edb1a8f35ecd664d6de9d79c265fe5ab4c6df"></a> enumerator PM\_LOW\_VOL\_VOLTAGE\_1\_0

    <a id="_CPPv4N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_1_1E"></a>

    <a id="_CPPv3N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_1_1E"></a> <a id="_CPPv2N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_1_1E"></a> <a id="pm_8h_1a6a4f9c770ed7b8dfea14acfa0c68edb1abb902e8170b8b4d7b3fc50159617a93c"></a> enumerator PM\_LOW\_VOL\_VOLTAGE\_1\_1

    <a id="_CPPv4N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_1_2E"></a>

    <a id="_CPPv3N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_1_2E"></a> <a id="_CPPv2N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_1_2E"></a> <a id="pm_8h_1a6a4f9c770ed7b8dfea14acfa0c68edb1a8d237c6f46545cd64756c852d38fc97f"></a> enumerator PM\_LOW\_VOL\_VOLTAGE\_1\_2

    <a id="_CPPv4N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_1_3E"></a>

    <a id="_CPPv3N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_1_3E"></a> <a id="_CPPv2N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_1_3E"></a> <a id="pm_8h_1a6a4f9c770ed7b8dfea14acfa0c68edb1a7b4fdcc2e72e6fba99ebf5b63894de00"></a> enumerator PM\_LOW\_VOL\_VOLTAGE\_1\_3

<a id="_CPPv421bk_pm_wakeup_reason_e"></a>

<a id="_CPPv321bk_pm_wakeup_reason_e"></a> <a id="_CPPv221bk_pm_wakeup_reason_e"></a> <a id="pm_8h_1a0182483f4d9b82c3e4590da635da11f8"></a> enum bk\_pm\_wakeup\_reason\_e
:   *Values:*

    <a id="_CPPv4N21bk_pm_wakeup_reason_e20BK_PM_WAKEUP_UNKNOWNE"></a>

    <a id="_CPPv3N21bk_pm_wakeup_reason_e20BK_PM_WAKEUP_UNKNOWNE"></a> <a id="_CPPv2N21bk_pm_wakeup_reason_e20BK_PM_WAKEUP_UNKNOWNE"></a> <a id="pm_8h_1a0182483f4d9b82c3e4590da635da11f8aff34a2839fbce7aa02cd29259c616e5f"></a> enumerator BK\_PM\_WAKEUP\_UNKNOWN

    <a id="_CPPv4N21bk_pm_wakeup_reason_e16BK_PM_WAKEUP_BLEE"></a>

    <a id="_CPPv3N21bk_pm_wakeup_reason_e16BK_PM_WAKEUP_BLEE"></a> <a id="_CPPv2N21bk_pm_wakeup_reason_e16BK_PM_WAKEUP_BLEE"></a> <a id="pm_8h_1a0182483f4d9b82c3e4590da635da11f8a43395b472f769fa4522282015772d121"></a> enumerator BK\_PM\_WAKEUP\_BLE

    <a id="_CPPv4N21bk_pm_wakeup_reason_e17BK_PM_WAKEUP_WIFIE"></a>

    <a id="_CPPv3N21bk_pm_wakeup_reason_e17BK_PM_WAKEUP_WIFIE"></a> <a id="_CPPv2N21bk_pm_wakeup_reason_e17BK_PM_WAKEUP_WIFIE"></a> <a id="pm_8h_1a0182483f4d9b82c3e4590da635da11f8a225dbed858592a26ae18df1d89ed825d"></a> enumerator BK\_PM\_WAKEUP\_WIFI

    <a id="_CPPv4N21bk_pm_wakeup_reason_e25BK_PM_WAKEUP_UART_CONSOLEE"></a>

    <a id="_CPPv3N21bk_pm_wakeup_reason_e25BK_PM_WAKEUP_UART_CONSOLEE"></a> <a id="_CPPv2N21bk_pm_wakeup_reason_e25BK_PM_WAKEUP_UART_CONSOLEE"></a> <a id="pm_8h_1a0182483f4d9b82c3e4590da635da11f8a66e9a42ccfc8040e2447c2a4c2476a53"></a> enumerator BK\_PM\_WAKEUP\_UART\_CONSOLE

    <a id="_CPPv4N21bk_pm_wakeup_reason_e23BK_PM_WAKEUP_UART_TTYS2E"></a>

    <a id="_CPPv3N21bk_pm_wakeup_reason_e23BK_PM_WAKEUP_UART_TTYS2E"></a> <a id="_CPPv2N21bk_pm_wakeup_reason_e23BK_PM_WAKEUP_UART_TTYS2E"></a> <a id="pm_8h_1a0182483f4d9b82c3e4590da635da11f8afdde22ac35bb7d481235ecfb185ed21a"></a> enumerator BK\_PM\_WAKEUP\_UART\_TTYS2

    <a id="_CPPv4N21bk_pm_wakeup_reason_e17BK_PM_WAKEUP_GPIOE"></a>

    <a id="_CPPv3N21bk_pm_wakeup_reason_e17BK_PM_WAKEUP_GPIOE"></a> <a id="_CPPv2N21bk_pm_wakeup_reason_e17BK_PM_WAKEUP_GPIOE"></a> <a id="pm_8h_1a0182483f4d9b82c3e4590da635da11f8a1bdf4c36b66b6e1903ab694968f527ad"></a> enumerator BK\_PM\_WAKEUP\_GPIO

    <a id="_CPPv4N21bk_pm_wakeup_reason_e21BK_PM_WAKEUP_HW_TIMERE"></a>

    <a id="_CPPv3N21bk_pm_wakeup_reason_e21BK_PM_WAKEUP_HW_TIMERE"></a> <a id="_CPPv2N21bk_pm_wakeup_reason_e21BK_PM_WAKEUP_HW_TIMERE"></a> <a id="pm_8h_1a0182483f4d9b82c3e4590da635da11f8a655aa7084b09f3f69e13cd11f86cd5b4"></a> enumerator BK\_PM\_WAKEUP\_HW\_TIMER

    <a id="_CPPv4N21bk_pm_wakeup_reason_e22BK_PM_WAKEUP_SRC_COUNTE"></a>

    <a id="_CPPv3N21bk_pm_wakeup_reason_e22BK_PM_WAKEUP_SRC_COUNTE"></a> <a id="_CPPv2N21bk_pm_wakeup_reason_e22BK_PM_WAKEUP_SRC_COUNTE"></a> <a id="pm_8h_1a0182483f4d9b82c3e4590da635da11f8af8c9d6771f132e49629bd8a9e0a8f0bb"></a> enumerator BK\_PM\_WAKEUP\_SRC\_COUNT
