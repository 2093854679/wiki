# PM APIs[](#pm-apis "永久链接至标题")


重要

The PM API v1.0 is the lastest stable PM APIs.


## PM Interface[](#pm-interface "永久链接至标题")

The BK PM Driver supports following logical PM interfaces:

> - BK enter different sleep mode interface
> - BK clock control interface
> - BK power control interface


## PM API Categories[](#pm-api-categories "永久链接至标题")

Most of PM APIs can be categoried as:

> - Common APIs
>   The common APIs are frequently-used.
> - Specific APIs.
>   The specific APIs are used in specific configuration.

Common PM APIs:
:   - [`bk_pm_sleep_mode_set()`](#_CPPv420bk_pm_sleep_mode_set15pm_sleep_mode_e "bk_pm_sleep_mode_set") - set sleep mode

    - [`bk_pm_module_vote_sleep_ctrl()`](#_CPPv428bk_pm_module_vote_sleep_ctrl22pm_sleep_module_name_e8uint32_t8uint32_t "bk_pm_module_vote_sleep_ctrl") - module vote sleep ctrl

    - [`bk_pm_module_vote_power_ctrl()`](#_CPPv428bk_pm_module_vote_power_ctrl22pm_power_module_name_e23pm_power_module_state_e "bk_pm_module_vote_power_ctrl") - module vote power ctrl

    - [`bk_pm_wakeup_source_set()`](#_CPPv423bk_pm_wakeup_source_set18pm_wakeup_source_ePv "bk_pm_wakeup_source_set") - set wakeup source

Specific APIs:
:   - [`bk_pm_mcu_pm_state_get()`](#_CPPv422bk_pm_mcu_pm_state_getv "bk_pm_mcu_pm_state_get") - get the state of whether enter the sleep

    - [`bk_pm_mcu_pm_ctrl()`](#_CPPv417bk_pm_mcu_pm_ctrl8uint32_t "bk_pm_mcu_pm_ctrl") - config whether enter the sleep

    - [`bk_pm_lpo_src_get()`](#_CPPv417bk_pm_lpo_src_getv "bk_pm_lpo_src_get") - get the lpo source

    - [`bk_pm_lpo_src_set()`](#_CPPv417bk_pm_lpo_src_set12pm_lpo_src_e "bk_pm_lpo_src_set") - set the lpo source

    - [`bk_pm_lp_vol_get()`](#_CPPv416bk_pm_lp_vol_getv "bk_pm_lp_vol_get") - get the voltage when enter low voltage

    - [`bk_pm_lp_vol_set()`](#_CPPv416bk_pm_lp_vol_set8uint32_t "bk_pm_lp_vol_set") - set the voltage when enter low voltage

    - [`bk_pm_light_sleep_unregister_cb()`](#_CPPv431bk_pm_light_sleep_unregister_cbbb "bk_pm_light_sleep_unregister_cb") - unregister the light sleep callback

    - [`bk_pm_light_sleep_register_cb()`](#_CPPv429bk_pm_light_sleep_register_cbP12pm_cb_conf_tP12pm_cb_conf_t "bk_pm_light_sleep_register_cb") - register the light sleep callback

    - [`bk_pm_clock_ctrl()`](#_CPPv416bk_pm_clock_ctrl12pm_dev_clk_e16pm_dev_clk_pwr_e "bk_pm_clock_ctrl") - module vote power ctrl

    - [`bk_pm_wakeup_from_lowvol_consume_time_get()`](#_CPPv441bk_pm_wakeup_from_lowvol_consume_time_getv "bk_pm_wakeup_from_lowvol_consume_time_get") - get the consume time wakeuping from low voltage

    - [`bk_pm_module_power_state_get()`](#_CPPv428bk_pm_module_power_state_get22pm_power_module_name_e "bk_pm_module_power_state_get") - get the module power domain state

    - [`bk_pm_phy_cali_state_get()`](#_CPPv424bk_pm_phy_cali_state_getv "bk_pm_phy_cali_state_get") - get the state whether phy have calibration

    - [`bk_pm_suppress_ticks_and_sleep()`](#_CPPv430bk_pm_suppress_ticks_and_sleep8uint32_t "bk_pm_suppress_ticks_and_sleep") - enter sleep process(return int)

    - [`bk_pm_enter_sleep()`](#_CPPv417bk_pm_enter_sleepv "bk_pm_enter_sleep") - enter sleep process(return void)


## Programing Principle[](#programing-principle "永久链接至标题")

重要

Here is some general principle for pm API users:
:   - Enter deep sleep and low voltage ,it only need call the “Common PM APIs”,if you want to call the Specific APIs,please contact us in case of make issue.

    - Use BK_ERR_CHECK to check the return value of the pm API

    - If you are not sure how to use pm APIs, study the pm used guide example code first.

    - If you are not sure how to initialize some fields of config struct, use the default configuration macro to use the config first and then set application specific fields


## User Development Model[](#user-development-model "永久链接至标题")

pm interface detail


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [pm.h](https://github.com/bekencorp/armino/blob/main/components/pm.h "https://github.com/bekencorp/armino/blob/main/components/pm.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_module_lv_sleep_state_clear([pm_dev_id_e](#_CPPv411pm_dev_id_e "pm_dev_id_e") module)[](#_CPPv433bk_pm_module_lv_sleep_state_clear11pm_dev_id_e "永久链接至目标")
:   clear the lv sleep state

    clear the lv sleep state


    **Attention**
    :   - This API is used to clear the lv sleep state

    参数
    :   **-module:module** – name

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_module_lv_sleep_state_set()[](#_CPPv431bk_pm_module_lv_sleep_state_setv "永久链接至目标")
:   set the lv sleep state

    set the lv sleep state


    **Attention**
    :   - This API is used to set the lv sleep state

    参数
    :   **-void** –

    返回
    :   - BK_OK: succeed

        - others: other errors.

uint64_t bk_pm_module_lv_sleep_state_get([pm_dev_id_e](#_CPPv411pm_dev_id_e "pm_dev_id_e") module)[](#_CPPv431bk_pm_module_lv_sleep_state_get11pm_dev_id_e "永久链接至目标")
:   get the lv sleep state

    get the lv sleep state


    **Attention**
    :   - This API is used to get the lv sleep state

    参数
    :   **-module:module** – name

    返回
    :   - module_lv_sleep_state

pm_wakeup_source_e bk_pm_deep_sleep_wakeup_source_get()[](#_CPPv434bk_pm_deep_sleep_wakeup_source_getv "永久链接至目标")
:   get wakeup source from deepsleep

    get wakeup source from deepsleep


    **Attention**
    :   - This API is used to get wakeup source from deepsleep

    参数
    :   **-void** –

    返回
    :   - wakeup source(0x0:WAKEUP SOURCE OF GPIO;0x1:WAKEUP SOURCE OF RTC;0x2:WAKEUP SOURCE OF WIFI OR BT;0x4:WAKEUP SOURCE OF TOUCHED;0x5:NONE WAKEUP_SOURCE)

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_exit_low_vol_wakeup_source_clear()[](#_CPPv438bk_pm_exit_low_vol_wakeup_source_clearv "永久链接至目标")
:   clear wakeup source of exiting low voltage process

    clear wakeup source of exit low voltage


    **Attention**
    :   - This API is used to clear wakeup source of exiting low voltage process

    参数
    :   **-void** –

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_exit_low_vol_wakeup_source_set()[](#_CPPv436bk_pm_exit_low_vol_wakeup_source_setv "永久链接至目标")
:   set and save wakeup source of exiting low voltage

    set and save wakeup source of exiting low voltage


    **Attention**
    :   - This API is used to set and save wakeup source of exiting low voltage

    参数
    :   **-0x0:close** – cp1 auto power down feature ;0x1:open cp1 auto power down feature

    返回
    :   - BK_OK: succeed

        - others: other errors.

pm_wakeup_source_e bk_pm_exit_low_vol_wakeup_source_get()[](#_CPPv436bk_pm_exit_low_vol_wakeup_source_getv "永久链接至目标")
:   get wakeup source of exiting low voltage

    get wakeup source of exiting low voltage


    **Attention**
    :   - This API is used to get wakeup source of exiting low voltage

    参数
    :   **-void** –

    返回
    :   - wakeup source(0x0:WAKEUP SOURCE OF GPIO;0x1:WAKEUP SOURCE OF RTC;0x2:WAKEUP SOURCE OF WIFI OR BT;0x4:WAKEUP SOURCE OF TOUCHED;0x5:NONE WAKEUP_SOURCE)

[pm_mem_auto_ctrl_e](#_CPPv418pm_mem_auto_ctrl_e "pm_mem_auto_ctrl_e") bk_pm_mem_auto_power_down_state_get()[](#_CPPv435bk_pm_mem_auto_power_down_state_getv "永久链接至目标")
:   get memory auto power down flag

    get memory auto power down flag


    **Attention**
    :   - This API is used to get memory auto power down flag

    参数
    :   **-void** –

    返回
    :   - memory auto power down flag(PM_MEM_AUTO_CTRL_DISABLE:disable memory auto power down feature ;PM_MEM_AUTO_CTRL_ENABLE:enable memory auto power down feature)

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_mem_auto_power_down_state_set([pm_mem_auto_ctrl_e](#_CPPv418pm_mem_auto_ctrl_e "pm_mem_auto_ctrl_e") value)[](#_CPPv435bk_pm_mem_auto_power_down_state_set18pm_mem_auto_ctrl_e "永久链接至目标")
:   memory auto power down flag set

    set memory auto power down flag


    **Attention**
    :   - This API is used to set memory auto power down flag

    参数
    :   **-PM_MEM_AUTO_CTRL_DISABLE:disable** – memory auto power down feature ;PM_MEM_AUTO_CTRL_ENABLE:enable memory auto power down feature

    返回
    :   - BK_OK: succeed

        - others: other errors.

uint32_t bk_pm_cp1_auto_power_down_state_get()[](#_CPPv435bk_pm_cp1_auto_power_down_state_getv "永久链接至目标")
:   get cp1 auto power down flag

    get cp1 auto power down flag


    **Attention**
    :   - This API is used to get cp1 auto power down flag

    参数
    :   **-void** –

    返回
    :   - cp1 auto power down flag(0x0:close cp1 auto power down feature ;0x1:open cp1 auto power down feature)

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_cp1_auto_power_down_state_set(uint32_t value)[](#_CPPv435bk_pm_cp1_auto_power_down_state_set8uint32_t "永久链接至目标")
:   cp1 auto power down flag set

    set cp1 auto power down flag


    **Attention**
    :   - This API is used to set cp1 auto power down flag

    参数
    :   **-0x0:close** – cp1 auto power down feature ;0x1:open cp1 auto power down feature

    返回
    :   - BK_OK: succeed

        - others: other errors.

uint32_t bk_pm_cp1_boot_flag_get()[](#_CPPv423bk_pm_cp1_boot_flag_getv "永久链接至目标")
:   get cpu1 boot flag

    get cpu1 boot flag(ready or not ready)


    **Attention**
    :   - This API is used to get cpu1 boot flag(ready or not ready)

    参数
    :   **-void** –

    返回
    :   - the flag of cpu1 boot flag (0x0:cpu1 not boot ready;0x1:cpu1 boot ready)

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_rosc_calibration([pm_rosc_cali_mode_e](#_CPPv419pm_rosc_cali_mode_e "pm_rosc_cali_mode_e") rosc_cali_mode, uint32_t cali_interval)[](#_CPPv422bk_pm_rosc_calibration19pm_rosc_cali_mode_e8uint32_t "永久链接至目标")
:   rosc calibration

    rosc calibration


    **Attention**
    :   - This API is used to calibrate rosc

    参数
    :   **-rosc_cali_mode:0x1:rosc** – calibrate manual; 0x0:rosc calibrate auto -cali_interval: 0x0:0.25s;0x1:0.5s;0x2:0.75s;0x3:1.0s;0x4:1.25s;0x5:1.5s;0x6:1.75s;0x7:2s;

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_external_ldo_ctrl(uint32_t value)[](#_CPPv423bk_pm_external_ldo_ctrl8uint32_t "永久链接至目标")
:   using the gpio to control the external ldo

    control the external ldo


    **Attention**
    :   - This API is used to use the specific gpio(define in GPIO_CTRL_LDO_OUTPUT_HIGH_MAP or GPIO_CTRL_LDO_OUTPUT_LOW_MAP in gpio_map.h) control the external ldo

    参数
    :   **-value:0x1:output** – high; 0x0:output low

    返回
    :   - BK_OK: succeed

        - others: other errors.

uint32_t bk_pm_phy_cali_state_get()[](#_CPPv424bk_pm_phy_cali_state_getv "永久链接至目标")
:   get the state of phy calibration

    get the state of phy calibration


    **Attention**
    :   - This API is used to get the state of phy calibration

    参数
    :   **-void** –

    返回
    :   - the state of phy calibration(0x1:have calibration;0x0:not calibration)

bool bk_pm_phy_reinit_flag_get()[](#_CPPv425bk_pm_phy_reinit_flag_getv "永久链接至目标")
:   get the flag of phy reinit part1

    get the flag of phy reinit part1


    **Attention**
    :   - This API is used to get the flag of phy reinit part1

    参数
    :   **-void** –

    返回
    :   - the flag of phy reinit part1 (True:have part1;false:not do it)

void bk_pm_phy_reinit_flag_clear()[](#_CPPv427bk_pm_phy_reinit_flag_clearv "永久链接至目标")
:   clear the flag of phy reinit part1

    clear the flag of phy reinit part1


    **Attention**
    :   - This API is used to clear the flag of phy reinit part1

    参数
    :   **-void** –

    返回
    :   -void

uint32_t bk_pm_wakeup_from_lowvol_consume_time_get()[](#_CPPv441bk_pm_wakeup_from_lowvol_consume_time_getv "永久链接至目标")
:   get the consume time from lowvol wakeup

    the consume time from lowvol wakeup


    **Attention**
    :   - This API is used to get the consume time from lowvol wakeup

    参数
    :   **-void** –

    返回
    :   - the consume time of wakeup from lowvol

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_sleep_register_cb([pm_sleep_mode_e](#_CPPv415pm_sleep_mode_e "pm_sleep_mode_e") sleep_mode, [pm_dev_id_e](#_CPPv411pm_dev_id_e "pm_dev_id_e") dev_id, [pm_cb_conf_t](#_CPPv412pm_cb_conf_t "pm_cb_conf_t") *enter_config, [pm_cb_conf_t](#_CPPv412pm_cb_conf_t "pm_cb_conf_t") *exit_config)[](#_CPPv423bk_pm_sleep_register_cb15pm_sleep_mode_e11pm_dev_id_eP12pm_cb_conf_tP12pm_cb_conf_t "永久链接至目标")
:   register sleep mode(low voltage and deepsleep) config

    register sleep config(include callback function and parameter)


    **Attention**
    :   - This API is used to register low voltage and deepsleep config

    参数
    :   **-sleep_mode:low** – voltage or deepsleep mode -dev_id:dev id -enter_config:enter sleep config -exit_config:exit sleep config

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_sleep_unregister_cb([pm_sleep_mode_e](#_CPPv415pm_sleep_mode_e "pm_sleep_mode_e") sleep_mode, [pm_dev_id_e](#_CPPv411pm_dev_id_e "pm_dev_id_e") dev_id, bool enter_cb, bool exit_cb)[](#_CPPv425bk_pm_sleep_unregister_cb15pm_sleep_mode_e11pm_dev_id_ebb "永久链接至目标")
:   unregister sleep mode(low voltage and deepsleep) config

    unregister sleep config(include callback function and parameter)


    **Attention**
    :   - This API is used to unregister low voltage and deepsleep config

    参数
    :   **-sleep_mode:low** – voltage or deepsleep mode -dev_id:dev id -enter_cb:whether unregister the enter call back -exit_cb:whether unregister the exit call back

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_light_sleep_register_cb([pm_cb_conf_t](#_CPPv412pm_cb_conf_t "pm_cb_conf_t") *enter_config, [pm_cb_conf_t](#_CPPv412pm_cb_conf_t "pm_cb_conf_t") *exit_config)[](#_CPPv429bk_pm_light_sleep_register_cbP12pm_cb_conf_tP12pm_cb_conf_t "永久链接至目标")
:   register light sleep config

    register light sleep config(include callback function and parameter)


    **Attention**
    :   - This API is used to register light sleep config

    参数
    :   **-enter_config:enter** – light sleep config -exit_config:exit light sleep config

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_light_sleep_unregister_cb(bool enter_cb, bool exit_cb)[](#_CPPv431bk_pm_light_sleep_unregister_cbbb "永久链接至目标")
:   unregister light sleep callback

    unregister light sleep callback(enter light sleep callback and exit light sleep callback)


    **Attention**
    :   - This API is used to unregister light sleep callback

    参数
    :   **-enter_cb:whether** – unregister the enter call back -exit_cb:whether unregister the exit call back

    返回
    :   - BK_OK: succeed

        - others: other errors.

int32_t bk_pm_module_sleep_state_get([pm_sleep_module_name_e](#_CPPv422pm_sleep_module_name_e "pm_sleep_module_name_e") module)[](#_CPPv428bk_pm_module_sleep_state_get22pm_sleep_module_name_e "永久链接至目标")
:   get sleep state of module

    get current sleep state of pm sleep module.


    **Attention**
    :   - This API is used to get the sleep state

    参数
    :   **-** – module: module name

    返回
    :   - sleep state: 0x0:active;0x1:sleeped;

int32_t bk_pm_module_power_state_get(pm_power_module_name_e module)[](#_CPPv428bk_pm_module_power_state_get22pm_power_module_name_e "永久链接至目标")
:   get power domain of module state

    get the power domain state


    **Attention**
    :   - This API is used to get the power domain state

    参数
    :   **-module:module** – name

    返回
    :   -the state of power domain state

[pm_cpu_freq_e](#_CPPv413pm_cpu_freq_e "pm_cpu_freq_e") bk_pm_module_current_cpu_freq_get([pm_dev_id_e](#_CPPv411pm_dev_id_e "pm_dev_id_e") module)[](#_CPPv433bk_pm_module_current_cpu_freq_get11pm_dev_id_e "永久链接至目标")
:   get the cpu frequency of the module vote

    get the module voting cpu frequency


    **Attention**
    :   - This API is used to get the module voting cpu frequency

    参数
    :   **-module:module** – id

    返回
    :   - the cpu frequency of the module vote

[pm_cpu_freq_e](#_CPPv413pm_cpu_freq_e "pm_cpu_freq_e") bk_pm_current_max_cpu_freq_get()[](#_CPPv430bk_pm_current_max_cpu_freq_getv "永久链接至目标")
:   get the current max and used cpu frequency

    select the cpu frequency


    **Attention**
    :   - This API is used to get the current max and used cpu frequency

    参数
    :   **-void** –

    返回
    :   - get the current max and used cpu frequency

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_module_vote_cpu_freq([pm_dev_id_e](#_CPPv411pm_dev_id_e "pm_dev_id_e") module, [pm_cpu_freq_e](#_CPPv413pm_cpu_freq_e "pm_cpu_freq_e") cpu_freq)[](#_CPPv426bk_pm_module_vote_cpu_freq11pm_dev_id_e13pm_cpu_freq_e "永久链接至目标")
:   vote cpu frequency

    select the cpu frequency


    **Attention**
    :   - This API is used to vote ,then select the cpu frequency

    参数
    :   **-module:module** – id;cpu_freq:cpu frequency(320M,240M,120M,26M)

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_clock_ctrl([pm_dev_clk_e](#_CPPv412pm_dev_clk_e "pm_dev_clk_e") module, [pm_dev_clk_pwr_e](#_CPPv416pm_dev_clk_pwr_e "pm_dev_clk_pwr_e") clock_state)[](#_CPPv416bk_pm_clock_ctrl12pm_dev_clk_e16pm_dev_clk_pwr_e "永久链接至目标")
:   clock ctrl

    enable or disable dev clock


    **Attention**
    :   - This API is used to enable or disable dev clock

    参数
    :   **-module:device** – id;clock_state:PM_CLK_CTRL_PWR_DOWN or PM_CLK_CTRL_PWR_DOWN

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_lp_vol_set(uint32_t lp_vol)[](#_CPPv416bk_pm_lp_vol_set8uint32_t "永久链接至目标")
:   lp voltage set

    set the lp voltage


    **Attention**
    :   - This API is used to set lp voltage when enter low voltage

    参数
    :   **-uint32_t:0x0:0.6v;0x1:0.7v;0x2:0.8v;0x3:0.9v;0x4:1.0v;0x5:1.1v;0x6:1.2v;0x7:1.3v;** –

    返回
    :   - BK_OK: succeed

        - others: other errors.

uint32_t bk_pm_lp_vol_get()[](#_CPPv416bk_pm_lp_vol_getv "永久链接至目标")
:   lp voltage get

    get the lpo voltage


    **Attention**
    :   - This API is used to get lpo voltage value

    参数
    :   **-void** –

    返回
    :   - the lp voltage value

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_rf_tx_vol_set(uint32_t tx_vol)[](#_CPPv419bk_pm_rf_tx_vol_set8uint32_t "永久链接至目标")
:   rf tx voltage set

    set the tx voltage of RF


    **Attention**
    :   - This API is used to set tx voltage of RF

    参数
    :   **-uint32_t:0x0:1.25v;0x1:1.3v;0x2:1.35v;0x3:1.4v;0x4:1.45v;0x5:1.5v;0x6:1.55v;0x7:1.6v;** –

    返回
    :   - BK_OK: succeed

        - others: other errors.

uint32_t bk_pm_rf_tx_vol_get()[](#_CPPv419bk_pm_rf_tx_vol_getv "永久链接至目标")
:   rf tx voltage get

    get the tx voltage of RF


    **Attention**
    :   - This API is used to get tx voltage value of RF

    参数
    :   **-void** –

    返回
    :   - the tx voltage value

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_rf_rx_vol_set(uint32_t rx_vol)[](#_CPPv419bk_pm_rf_rx_vol_set8uint32_t "永久链接至目标")
:   rf rx voltage set

    set the rx voltage of RF


    **Attention**
    :   - This API is used to set rx voltage of RF

    参数
    :   **-uint32_t:0x0:1.25v;0x1:1.3v;0x2:1.35v;0x3:1.4v;0x4:1.45v;0x5:1.5v;0x6:1.55v;0x7:1.6v;** –

    返回
    :   - BK_OK: succeed

        - others: other errors.

uint32_t bk_pm_rf_rx_vol_get()[](#_CPPv419bk_pm_rf_rx_vol_getv "永久链接至目标")
:   rf rx voltage get

    get the rx voltage of RF


    **Attention**
    :   - This API is used to get rx voltage value of RF

    参数
    :   **-void** –

    返回
    :   - the rx voltage value

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_lpo_src_set([pm_lpo_src_e](#_CPPv412pm_lpo_src_e "pm_lpo_src_e") lpo_src)[](#_CPPv417bk_pm_lpo_src_set12pm_lpo_src_e "永久链接至目标")
:   lpo source set

    set the lpo source


    **Attention**
    :   - This API is used to select 32k source when enter low voltage and deepsleep

    参数
    :   **-lpo_src:0x0:32K** – from 26m;0x1:32K from 26m;0x2:32K from ROSC;0x3:32K from ROSC

    返回
    :   - BK_OK: succeed

        - others: other errors.

[pm_lpo_src_e](#_CPPv412pm_lpo_src_e "pm_lpo_src_e") bk_pm_lpo_src_get()[](#_CPPv417bk_pm_lpo_src_getv "永久链接至目标")
:   lpo source get

    get the lpo source


    **Attention**
    :   - This API is used to get 32k lpo source

    参数
    :   **void** –

    返回
    :   -lpo_src:0x0:32K from 26m;0x1:32K from 26m;0x2:32K from ROSC;0x3:32K from ROSC

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_mcu_pm_ctrl(uint32_t power_state)[](#_CPPv417bk_pm_mcu_pm_ctrl8uint32_t "永久链接至目标")
:   mcu pm ctrl

    enabel and disable the mcu power manage


    **Attention**
    :   - This API is used to enabel and disable the mcu power manage

    参数
    :   **-power_state:0x0:enable** – the mcu power manage;0x1:disable the mcu power manage

    返回
    :   - BK_OK: succeed

        - others: other errors.

uint32_t bk_pm_mcu_pm_state_get()[](#_CPPv422bk_pm_mcu_pm_state_getv "永久链接至目标")
:   get the mcu power feature state

    get the mcu power feature state


    **Attention**
    :   -This API is used to get the mcu power manage feature state(open or close)

    参数
    :   **none** –

    返回
    :   -mcu power manage state(0x0:enable the mcu power manage;0x1:disable the mcu power manage)

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_sleep_mode_set([pm_sleep_mode_e](#_CPPv415pm_sleep_mode_e "pm_sleep_mode_e") sleep_mode)[](#_CPPv420bk_pm_sleep_mode_set15pm_sleep_mode_e "永久链接至目标")
:   set sleep mode

    set sleep mode.


    **Attention**
    :   - This API set sleep mode

    参数
    :   **sleep** – mode:0x0:NORMAL_SLEEP;0x1:LOW_VOLTAGE;0x2:DEEP_SLEEP;0x3:DEFAULT(if it meet low voltage,enter low voltage,otherwise enter normal sleep);

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_wakeup_source_set(pm_wakeup_source_e wakeup_source, void *source_param)[](#_CPPv423bk_pm_wakeup_source_set18pm_wakeup_source_ePv "永久链接至目标")
:   set wakeup source

    set wakeup source(eg.rtc,gpio)


    **Attention**
    :   - This API set wakeup source,wifi and bt themselves not need set wakup source when in volatage

    参数
    :   **-wakeup_source:wake** – up source -source_param: the wakeup source parameter

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_module_vote_sleep_ctrl([pm_sleep_module_name_e](#_CPPv422pm_sleep_module_name_e "pm_sleep_module_name_e") module, uint32_t sleep_state, uint32_t sleep_time)[](#_CPPv428bk_pm_module_vote_sleep_ctrl22pm_sleep_module_name_e8uint32_t8uint32_t "永久链接至目标")
:   module vote sleep ctrl

    other module tell pm module, they have entered sleep.(eg.wifi or bt enter sleep,then call the function ,tell pm it have entered sleep)


    **Attention**
    :   - This API is used by wifi or bt… let pm module know them(wifi or bt…) enter sleep or exit sleep

        - if all the specific module enter sleep, the mcu will enter low voltage

    参数
    :   **-module:module** – name -sleep_state:0x1:enter sleep;0x0:exit sleep -sleep_time: sleep time

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_module_vote_power_ctrl(pm_power_module_name_e module, [pm_power_module_state_e](#_CPPv423pm_power_module_state_e "pm_power_module_state_e") power_state)[](#_CPPv428bk_pm_module_vote_power_ctrl22pm_power_module_name_e23pm_power_module_state_e "永久链接至目标")
:   pm module vote power ctrl

    ther module tell pm module, they can enter power on or power off


    **Attention**
    :   - This API is used for the module power on and power off.

        - if all the specific module power off, the mcu will enter deep sleep

    参数
    :   **-module:module** – name -power_state:0x1:power off;0x0:power on

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_pm_suppress_ticks_and_sleep(uint32_t sleep_ticks)[](#_CPPv430bk_pm_suppress_ticks_and_sleep8uint32_t "永久链接至目标")
:   pm suppress ticks and sleep

    when the rtos enter idle task and sleep time > 2*(time per tick),it will call the function enter power manager


    **Attention**
    :   - This API is used for power manager.

    参数
    :   **-sleep_ticks:sleep** – time using tick unit

    返回
    :   - BK_OK: succeed

        - others: other errors.

void bk_pm_enter_sleep()[](#_CPPv417bk_pm_enter_sleepv "永久链接至目标")
:   enter sleep

    the function is for adapting harmony os


    **Attention**
    :   - This API is used for power manager.

    参数
    :   **-** – void

    返回
    :   - void

static inline [bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") pm_sleep_vote_init()[](#_CPPv418pm_sleep_vote_initv "永久链接至目标")
:   sleep vote init

    the function is for init the enter low voltage sleep vote


    **Attention**
    :   - This API is used for init the enter low voltage sleep vote

    参数
    :   **-** – void

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") pm_clk_32k_source_switch([pm_lpo_src_e](#_CPPv412pm_lpo_src_e "pm_lpo_src_e") lpo_src)[](#_CPPv424pm_clk_32k_source_switch12pm_lpo_src_e "永久链接至目标")
:   32k source switch

    When the external 32k clock source is enabled, this api used to switch the 32k clock source

    参数
    :   **-** – pm_lpo_src_e taget 32k clock source

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") pm_extern32k_register_cb([pm_cb_extern32k_cfg_t](#_CPPv421pm_cb_extern32k_cfg_t "pm_cb_extern32k_cfg_t") *cfg)[](#_CPPv424pm_extern32k_register_cbP21pm_cb_extern32k_cfg_t "永久链接至目标")
:   register callback function

    BT WIFI module registered callback function, used to switch synchronization when switching clock source

    参数
    :   **-** – [pm_cb_extern32k_cfg_t](#structpm__cb__extern32k__cfg__t "#structpm__cb__extern32k__cfg__t") Structure pointer

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") pm_extern32k_unregister_cb([pm_cb_extern32k_cfg_t](#_CPPv421pm_cb_extern32k_cfg_t "pm_cb_extern32k_cfg_t") *cfg)[](#_CPPv426pm_extern32k_unregister_cbP21pm_cb_extern32k_cfg_t "永久链接至目标")
:   unregister callback function

    参数
    :   **-** – [pm_cb_extern32k_cfg_t](#structpm__cb__extern32k__cfg__t "#structpm__cb__extern32k__cfg__t") Structure pointer

    返回
    :   - BK_OK: succeed

        - others: other errors.


### Structures[](#structures "永久链接至标题")

struct gpio_wakeup_param_t[](#_CPPv419gpio_wakeup_param_t "永久链接至目标")

struct rtc_wakeup_param_t[](#_CPPv418rtc_wakeup_param_t "永久链接至目标")

struct system_wakeup_param_t[](#_CPPv421system_wakeup_param_t "永久链接至目标")

struct usbplug_wakeup_param_t[](#_CPPv422usbplug_wakeup_param_t "永久链接至目标")

struct touch_wakeup_param_t[](#_CPPv420touch_wakeup_param_t "永久链接至目标")

struct pm_cb_conf_t[](#_CPPv412pm_cb_conf_t "永久链接至目标")

struct pm_sleep_cb_t[](#_CPPv413pm_sleep_cb_t "永久链接至目标")

struct pm_cb_extern32k_cfg_t[](#_CPPv421pm_cb_extern32k_cfg_t "永久链接至目标")


### Macros[](#macros "永久链接至标题")

PARAM_DATA_VALID[](#c.PARAM_DATA_VALID "永久链接至目标")

PM_APP_AUTO_VOTE_ENABLE[](#c.PM_APP_AUTO_VOTE_ENABLE "永久链接至目标")

PM_APP_AUTO_VOTE_DISENABLE[](#c.PM_APP_AUTO_VOTE_DISENABLE "永久链接至目标")

PM_CP1_AUTO_POWER_DOWN_ENABLE[](#c.PM_CP1_AUTO_POWER_DOWN_ENABLE "永久链接至目标")

PM_CP1_AUTO_POWER_DOWN_DISENABLE[](#c.PM_CP1_AUTO_POWER_DOWN_DISENABLE "永久链接至目标")

pm_wakeup_source_e[](#c.pm_wakeup_source_e "永久链接至目标")

PM_WAKEUP_SOURCE_INT_GPIO[](#c.PM_WAKEUP_SOURCE_INT_GPIO "永久链接至目标")

PM_WAKEUP_SOURCE_INT_RTC[](#c.PM_WAKEUP_SOURCE_INT_RTC "永久链接至目标")

PM_WAKEUP_SOURCE_INT_TOUCHED[](#c.PM_WAKEUP_SOURCE_INT_TOUCHED "永久链接至目标")

PM_WAKEUP_SOURCE_INT_SYSTEM_WAKE[](#c.PM_WAKEUP_SOURCE_INT_SYSTEM_WAKE "永久链接至目标")

PM_WAKEUP_SOURCE_INT_WIFI[](#c.PM_WAKEUP_SOURCE_INT_WIFI "永久链接至目标")

PM_WAKEUP_SOURCE_INT_BT[](#c.PM_WAKEUP_SOURCE_INT_BT "永久链接至目标")

PM_WAKEUP_SOURCE_INT_USBPLUG[](#c.PM_WAKEUP_SOURCE_INT_USBPLUG "永久链接至目标")

PM_WAKEUP_SOURCE_INT_NONE[](#c.PM_WAKEUP_SOURCE_INT_NONE "永久链接至目标")

pm_power_module_name_e[](#c.pm_power_module_name_e "永久链接至目标")

PM_POWER_MODULE_NAME_MEM1[](#c.PM_POWER_MODULE_NAME_MEM1 "永久链接至目标")

PM_POWER_MODULE_NAME_MEM2[](#c.PM_POWER_MODULE_NAME_MEM2 "永久链接至目标")

PM_POWER_MODULE_NAME_MEM3[](#c.PM_POWER_MODULE_NAME_MEM3 "永久链接至目标")

PM_POWER_MODULE_NAME_ENCP[](#c.PM_POWER_MODULE_NAME_ENCP "永久链接至目标")

PM_POWER_MODULE_NAME_BAKP[](#c.PM_POWER_MODULE_NAME_BAKP "永久链接至目标")

PM_POWER_MODULE_NAME_AHBP[](#c.PM_POWER_MODULE_NAME_AHBP "永久链接至目标")

PM_POWER_MODULE_NAME_AUDP[](#c.PM_POWER_MODULE_NAME_AUDP "永久链接至目标")

PM_POWER_MODULE_NAME_VIDP[](#c.PM_POWER_MODULE_NAME_VIDP "永久链接至目标")

PM_POWER_MODULE_NAME_BTSP[](#c.PM_POWER_MODULE_NAME_BTSP "永久链接至目标")

PM_POWER_MODULE_NAME_WIFIP_MAC[](#c.PM_POWER_MODULE_NAME_WIFIP_MAC "永久链接至目标")

PM_POWER_MODULE_NAME_PHY[](#c.PM_POWER_MODULE_NAME_PHY "永久链接至目标")

PM_POWER_MODULE_NAME_MEM0[](#c.PM_POWER_MODULE_NAME_MEM0 "永久链接至目标")

PM_POWER_MODULE_NAME_MEM4[](#c.PM_POWER_MODULE_NAME_MEM4 "永久链接至目标")

PM_POWER_MODULE_NAME_OFDM[](#c.PM_POWER_MODULE_NAME_OFDM "永久链接至目标")

PM_POWER_MODULE_NAME_TCM0_PGEN[](#c.PM_POWER_MODULE_NAME_TCM0_PGEN "永久链接至目标")

PM_POWER_MODULE_NAME_ROM_PGEN[](#c.PM_POWER_MODULE_NAME_ROM_PGEN "永久链接至目标")

PM_POWER_MODULE_NAME_TCM1_PGEN[](#c.PM_POWER_MODULE_NAME_TCM1_PGEN "永久链接至目标")

PM_POWER_MODULE_NAME_CPU1[](#c.PM_POWER_MODULE_NAME_CPU1 "永久链接至目标")

PM_POWER_MODULE_NAME_CPU2[](#c.PM_POWER_MODULE_NAME_CPU2 "永久链接至目标")

PM_POWER_MODULE_NAME_APP[](#c.PM_POWER_MODULE_NAME_APP "永久链接至目标")

PM_POWER_MODULE_NAME_NONE[](#c.PM_POWER_MODULE_NAME_NONE "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_AUDP_FFT[](#c.PM_POWER_SUB_MODULE_NAME_AUDP_FFT "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_AUDP_SBC[](#c.PM_POWER_SUB_MODULE_NAME_AUDP_SBC "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_AUDP_AUDIO[](#c.PM_POWER_SUB_MODULE_NAME_AUDP_AUDIO "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_AUDP_I2S[](#c.PM_POWER_SUB_MODULE_NAME_AUDP_I2S "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_VIDP_DMA2D[](#c.PM_POWER_SUB_MODULE_NAME_VIDP_DMA2D "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_VIDP_YUVBUF[](#c.PM_POWER_SUB_MODULE_NAME_VIDP_YUVBUF "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_VIDP_JPEG_EN[](#c.PM_POWER_SUB_MODULE_NAME_VIDP_JPEG_EN "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_VIDP_JPEG_DE[](#c.PM_POWER_SUB_MODULE_NAME_VIDP_JPEG_DE "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_VIDP_LCD[](#c.PM_POWER_SUB_MODULE_NAME_VIDP_LCD "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_VIDP_ROTT[](#c.PM_POWER_SUB_MODULE_NAME_VIDP_ROTT "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_VIDP_SCAL0[](#c.PM_POWER_SUB_MODULE_NAME_VIDP_SCAL0 "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_VIDP_SCAL1[](#c.PM_POWER_SUB_MODULE_NAME_VIDP_SCAL1 "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_VIDP_H264[](#c.PM_POWER_SUB_MODULE_NAME_VIDP_H264 "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_PHY_BT[](#c.PM_POWER_SUB_MODULE_NAME_PHY_BT "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_PHY_WIFI[](#c.PM_POWER_SUB_MODULE_NAME_PHY_WIFI "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_PHY_RF[](#c.PM_POWER_SUB_MODULE_NAME_PHY_RF "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_AHBP_CAN[](#c.PM_POWER_SUB_MODULE_NAME_AHBP_CAN "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_AHBP_QSPI[](#c.PM_POWER_SUB_MODULE_NAME_AHBP_QSPI "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_AHBP_USB[](#c.PM_POWER_SUB_MODULE_NAME_AHBP_USB "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_AHBP_PSRAM[](#c.PM_POWER_SUB_MODULE_NAME_AHBP_PSRAM "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_AHBP_QSPI1[](#c.PM_POWER_SUB_MODULE_NAME_AHBP_QSPI1 "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_AHBP_ENET[](#c.PM_POWER_SUB_MODULE_NAME_AHBP_ENET "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_AHBP_SCR[](#c.PM_POWER_SUB_MODULE_NAME_AHBP_SCR "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_AHBP_LIN[](#c.PM_POWER_SUB_MODULE_NAME_AHBP_LIN "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_BAKP_TIMER1[](#c.PM_POWER_SUB_MODULE_NAME_BAKP_TIMER1 "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_BAKP_UART1[](#c.PM_POWER_SUB_MODULE_NAME_BAKP_UART1 "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_BAKP_UART2[](#c.PM_POWER_SUB_MODULE_NAME_BAKP_UART2 "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_BAKP_SPI1[](#c.PM_POWER_SUB_MODULE_NAME_BAKP_SPI1 "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_BAKP_I2C0[](#c.PM_POWER_SUB_MODULE_NAME_BAKP_I2C0 "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_BAKP_I2C1[](#c.PM_POWER_SUB_MODULE_NAME_BAKP_I2C1 "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_BAKP_SADC[](#c.PM_POWER_SUB_MODULE_NAME_BAKP_SADC "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_BAKP_PWM1[](#c.PM_POWER_SUB_MODULE_NAME_BAKP_PWM1 "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_BAKP_PWM0[](#c.PM_POWER_SUB_MODULE_NAME_BAKP_PWM0 "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_BAKP_TRNG[](#c.PM_POWER_SUB_MODULE_NAME_BAKP_TRNG "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_BAKP_IRDA[](#c.PM_POWER_SUB_MODULE_NAME_BAKP_IRDA "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_BAKP_SDIO[](#c.PM_POWER_SUB_MODULE_NAME_BAKP_SDIO "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_BAKP_COMSEG[](#c.PM_POWER_SUB_MODULE_NAME_BAKP_COMSEG "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_BAKP_DMA0[](#c.PM_POWER_SUB_MODULE_NAME_BAKP_DMA0 "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_BAKP_DMA1[](#c.PM_POWER_SUB_MODULE_NAME_BAKP_DMA1 "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_BAKP_LA[](#c.PM_POWER_SUB_MODULE_NAME_BAKP_LA "永久链接至目标")

PM_POWER_SUB_MODULE_NAME_BAKP_PM[](#c.PM_POWER_SUB_MODULE_NAME_BAKP_PM "永久链接至目标")

PM_ENTER_LOW_VOL_MODULES_CONFIG[](#c.PM_ENTER_LOW_VOL_MODULES_CONFIG "永久链接至目标")

PM_ENTER_DEEP_SLEEP_MODULES_CONFIG[](#c.PM_ENTER_DEEP_SLEEP_MODULES_CONFIG "永久链接至目标")

PM_VOLTAGE_OF_LOW_VOL[](#c.PM_VOLTAGE_OF_LOW_VOL "永久链接至目标")

PM_LPO_SOURCE[](#c.PM_LPO_SOURCE "永久链接至目标")

PM_APP_AUTO_VOTE_CTRL[](#c.PM_APP_AUTO_VOTE_CTRL "永久链接至目标")

PM_CP1_AUTO_POWER_DOWN_CTRL[](#c.PM_CP1_AUTO_POWER_DOWN_CTRL "永久链接至目标")


### Type Definitions[](#type-definitions "永久链接至标题")

typedef int (*pm_cb)(uint64_t sleep_time, void *args)[](#_CPPv45pm_cb "永久链接至目标")

typedef int (*pm_cb_notify)(void)[](#_CPPv412pm_cb_notify "永久链接至目标")

typedef int (*pm_cb_extern32k)([pm_sw_step_e](#_CPPv412pm_sw_step_e "pm_sw_step_e") sw_step, [pm_lpo_src_e](#_CPPv412pm_lpo_src_e "pm_lpo_src_e") lpo_src, [pm_cb_notify](#_CPPv412pm_cb_notify "pm_cb_notify") cb)[](#_CPPv415pm_cb_extern32k "永久链接至目标")


### Enumerations[](#enumerations "永久链接至标题")

enum pm_cp1_auto_ctrl_e[](#_CPPv418pm_cp1_auto_ctrl_e "永久链接至目标")
:   *Values:*

    enumerator PM_CP1_AUTO_CTRL_DISABLE[](#_CPPv4N18pm_cp1_auto_ctrl_e24PM_CP1_AUTO_CTRL_DISABLEE "永久链接至目标")

    enumerator PM_CP1_AUTO_CTRL_ENABLE[](#_CPPv4N18pm_cp1_auto_ctrl_e23PM_CP1_AUTO_CTRL_ENABLEE "永久链接至目标")

enum pm_mem_auto_ctrl_e[](#_CPPv418pm_mem_auto_ctrl_e "永久链接至目标")
:   *Values:*

    enumerator PM_MEM_AUTO_CTRL_DISABLE[](#_CPPv4N18pm_mem_auto_ctrl_e24PM_MEM_AUTO_CTRL_DISABLEE "永久链接至目标")

    enumerator PM_MEM_AUTO_CTRL_ENABLE[](#_CPPv4N18pm_mem_auto_ctrl_e23PM_MEM_AUTO_CTRL_ENABLEE "永久链接至目标")

enum gpio_trigger_interrupt_type_e[](#_CPPv429gpio_trigger_interrupt_type_e "永久链接至目标")
:   *Values:*

    enumerator GPIO_TRIGGER_INTERRUPE_LEVEL_LOW_ACTIVE[](#_CPPv4N29gpio_trigger_interrupt_type_e39GPIO_TRIGGER_INTERRUPE_LEVEL_LOW_ACTIVEE "永久链接至目标")

    enumerator GPIO_TRIGGER_INTERRUPE_LEVEL_HIGH_ACTIVE[](#_CPPv4N29gpio_trigger_interrupt_type_e40GPIO_TRIGGER_INTERRUPE_LEVEL_HIGH_ACTIVEE "永久链接至目标")

    enumerator GPIO_TRIGGER_INTERRUPE_EDGE_RISING[](#_CPPv4N29gpio_trigger_interrupt_type_e34GPIO_TRIGGER_INTERRUPE_EDGE_RISINGE "永久链接至目标")

    enumerator GPIO_TRIGGER_INTERRUPE_EDGE_FALLING[](#_CPPv4N29gpio_trigger_interrupt_type_e35GPIO_TRIGGER_INTERRUPE_EDGE_FALLINGE "永久链接至目标")

enum wifi_bt_wakeup_type_e[](#_CPPv421wifi_bt_wakeup_type_e "永久链接至目标")
:   *Values:*

    enumerator WIFI_WAKEUP[](#_CPPv4N21wifi_bt_wakeup_type_e11WIFI_WAKEUPE "永久链接至目标")

    enumerator BT_WAKEUP[](#_CPPv4N21wifi_bt_wakeup_type_e9BT_WAKEUPE "永久链接至目标")

enum pm_sleep_mode_e[](#_CPPv415pm_sleep_mode_e "永久链接至目标")
:   *Values:*

    enumerator PM_MODE_NORMAL_SLEEP[](#_CPPv4N15pm_sleep_mode_e20PM_MODE_NORMAL_SLEEPE "永久链接至目标")

    enumerator PM_MODE_LOW_VOLTAGE[](#_CPPv4N15pm_sleep_mode_e19PM_MODE_LOW_VOLTAGEE "永久链接至目标")

    enumerator PM_MODE_DEEP_SLEEP[](#_CPPv4N15pm_sleep_mode_e18PM_MODE_DEEP_SLEEPE "永久链接至目标")

    enumerator PM_MODE_SUPER_DEEP_SLEEP[](#_CPPv4N15pm_sleep_mode_e24PM_MODE_SUPER_DEEP_SLEEPE "永久链接至目标")

    enumerator PM_MODE_DEFAULT[](#_CPPv4N15pm_sleep_mode_e15PM_MODE_DEFAULTE "永久链接至目标")

enum pm_sleep_module_name_e[](#_CPPv422pm_sleep_module_name_e "永久链接至目标")
:   *Values:*

    enumerator PM_SLEEP_MODULE_NAME_I2C1[](#_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_I2C1E "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_SPI_1[](#_CPPv4N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_SPI_1E "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_UART1[](#_CPPv4N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_UART1E "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_PWM_1[](#_CPPv4N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_PWM_1E "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_TIMER_1[](#_CPPv4N22pm_sleep_module_name_e28PM_SLEEP_MODULE_NAME_TIMER_1E "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_SARADC[](#_CPPv4N22pm_sleep_module_name_e27PM_SLEEP_MODULE_NAME_SARADCE "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_AUDP[](#_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_AUDPE "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_VIDP[](#_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_VIDPE "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_BTSP[](#_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_BTSPE "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_WIFIP_MAC[](#_CPPv4N22pm_sleep_module_name_e30PM_SLEEP_MODULE_NAME_WIFIP_MACE "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_WIFI_PHY[](#_CPPv4N22pm_sleep_module_name_e29PM_SLEEP_MODULE_NAME_WIFI_PHYE "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_TIMER_2[](#_CPPv4N22pm_sleep_module_name_e28PM_SLEEP_MODULE_NAME_TIMER_2E "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_APP[](#_CPPv4N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_APPE "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_OTP[](#_CPPv4N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_OTPE "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_I2S_1[](#_CPPv4N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_I2S_1E "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_USB_1[](#_CPPv4N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_USB_1E "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_CAN[](#_CPPv4N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_CANE "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_PSRAM[](#_CPPv4N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_PSRAME "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_QSPI_1[](#_CPPv4N22pm_sleep_module_name_e27PM_SLEEP_MODULE_NAME_QSPI_1E "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_QSPI_2[](#_CPPv4N22pm_sleep_module_name_e27PM_SLEEP_MODULE_NAME_QSPI_2E "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_SDIO[](#_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_SDIOE "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_AUXS[](#_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_AUXSE "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_LOG[](#_CPPv4N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_LOGE "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_AT[](#_CPPv4N22pm_sleep_module_name_e23PM_SLEEP_MODULE_NAME_ATE "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_I2C2[](#_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_I2C2E "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_UART2[](#_CPPv4N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_UART2E "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_UART3[](#_CPPv4N22pm_sleep_module_name_e26PM_SLEEP_MODULE_NAME_UART3E "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_WDG[](#_CPPv4N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_WDGE "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_TIMER_3[](#_CPPv4N22pm_sleep_module_name_e28PM_SLEEP_MODULE_NAME_TIMER_3E "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_APP1[](#_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_APP1E "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_CPU1[](#_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_CPU1E "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_APP3[](#_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_APP3E "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_ROSC[](#_CPPv4N22pm_sleep_module_name_e25PM_SLEEP_MODULE_NAME_ROSCE "永久链接至目标")

    enumerator PM_SLEEP_MODULE_NAME_MAX[](#_CPPv4N22pm_sleep_module_name_e24PM_SLEEP_MODULE_NAME_MAXE "永久链接至目标")

enum pm_power_module_state_e[](#_CPPv423pm_power_module_state_e "永久链接至目标")
:   *Values:*

    enumerator PM_POWER_MODULE_STATE_ON[](#_CPPv4N23pm_power_module_state_e24PM_POWER_MODULE_STATE_ONE "永久链接至目标")

    enumerator PM_POWER_MODULE_STATE_OFF[](#_CPPv4N23pm_power_module_state_e25PM_POWER_MODULE_STATE_OFFE "永久链接至目标")

    enumerator PM_POWER_MODULE_STATE_NONE[](#_CPPv4N23pm_power_module_state_e26PM_POWER_MODULE_STATE_NONEE "永久链接至目标")

enum pm_module_name_e[](#_CPPv416pm_module_name_e "永久链接至目标")
:   *Values:*

    enumerator PM_MODULE_NAME_WIFI[](#_CPPv4N16pm_module_name_e19PM_MODULE_NAME_WIFIE "永久链接至目标")

    enumerator PM_MODULE_NAME_BT[](#_CPPv4N16pm_module_name_e17PM_MODULE_NAME_BTE "永久链接至目标")

    enumerator PM_MODULE_NAME_NONE[](#_CPPv4N16pm_module_name_e19PM_MODULE_NAME_NONEE "永久链接至目标")

enum pm_lpo_src_e[](#_CPPv412pm_lpo_src_e "永久链接至目标")
:   *Values:*

    enumerator PM_LPO_SRC_DIVD[](#_CPPv4N12pm_lpo_src_e15PM_LPO_SRC_DIVDE "永久链接至目标")

    enumerator PM_LPO_SRC_X32K[](#_CPPv4N12pm_lpo_src_e15PM_LPO_SRC_X32KE "永久链接至目标")

    enumerator PM_LPO_SRC_ROSC[](#_CPPv4N12pm_lpo_src_e15PM_LPO_SRC_ROSCE "永久链接至目标")

    enumerator PM_LPO_SRC_DEFAULT[](#_CPPv4N12pm_lpo_src_e18PM_LPO_SRC_DEFAULTE "永久链接至目标")

enum pm_dev_clk_e[](#_CPPv412pm_dev_clk_e "永久链接至目标")
:   *Values:*

    enumerator PM_CLK_ID_I2C1[](#_CPPv4N12pm_dev_clk_e14PM_CLK_ID_I2C1E "永久链接至目标")

    enumerator PM_CLK_ID_SPI_1[](#_CPPv4N12pm_dev_clk_e15PM_CLK_ID_SPI_1E "永久链接至目标")

    enumerator PM_CLK_ID_UART1[](#_CPPv4N12pm_dev_clk_e15PM_CLK_ID_UART1E "永久链接至目标")

    enumerator PM_CLK_ID_PWM_1[](#_CPPv4N12pm_dev_clk_e15PM_CLK_ID_PWM_1E "永久链接至目标")

    enumerator PM_CLK_ID_TIMER_1[](#_CPPv4N12pm_dev_clk_e17PM_CLK_ID_TIMER_1E "永久链接至目标")

    enumerator PM_CLK_ID_SARADC[](#_CPPv4N12pm_dev_clk_e16PM_CLK_ID_SARADCE "永久链接至目标")

    enumerator PM_CLK_ID_IRDA[](#_CPPv4N12pm_dev_clk_e14PM_CLK_ID_IRDAE "永久链接至目标")

    enumerator PM_CLK_ID_EFUSE[](#_CPPv4N12pm_dev_clk_e15PM_CLK_ID_EFUSEE "永久链接至目标")

    enumerator PM_CLK_ID_I2C2[](#_CPPv4N12pm_dev_clk_e14PM_CLK_ID_I2C2E "永久链接至目标")

    enumerator PM_CLK_ID_SPI_2[](#_CPPv4N12pm_dev_clk_e15PM_CLK_ID_SPI_2E "永久链接至目标")

    enumerator PM_CLK_ID_UART2[](#_CPPv4N12pm_dev_clk_e15PM_CLK_ID_UART2E "永久链接至目标")

    enumerator PM_CLK_ID_UART3[](#_CPPv4N12pm_dev_clk_e15PM_CLK_ID_UART3E "永久链接至目标")

    enumerator PM_CLK_ID_PWM_2[](#_CPPv4N12pm_dev_clk_e15PM_CLK_ID_PWM_2E "永久链接至目标")

    enumerator PM_CLK_ID_TIMER_2[](#_CPPv4N12pm_dev_clk_e17PM_CLK_ID_TIMER_2E "永久链接至目标")

    enumerator PM_CLK_ID_TIMER_3[](#_CPPv4N12pm_dev_clk_e17PM_CLK_ID_TIMER_3E "永久链接至目标")

    enumerator PM_CLK_ID_OTP[](#_CPPv4N12pm_dev_clk_e13PM_CLK_ID_OTPE "永久链接至目标")

    enumerator PM_CLK_ID_I2S_1[](#_CPPv4N12pm_dev_clk_e15PM_CLK_ID_I2S_1E "永久链接至目标")

    enumerator PM_CLK_ID_USB_1[](#_CPPv4N12pm_dev_clk_e15PM_CLK_ID_USB_1E "永久链接至目标")

    enumerator PM_CLK_ID_CAN[](#_CPPv4N12pm_dev_clk_e13PM_CLK_ID_CANE "永久链接至目标")

    enumerator PM_CLK_ID_PSRAM[](#_CPPv4N12pm_dev_clk_e15PM_CLK_ID_PSRAME "永久链接至目标")

    enumerator PM_CLK_ID_QSPI_1[](#_CPPv4N12pm_dev_clk_e16PM_CLK_ID_QSPI_1E "永久链接至目标")

    enumerator PM_CLK_ID_QSPI_2[](#_CPPv4N12pm_dev_clk_e16PM_CLK_ID_QSPI_2E "永久链接至目标")

    enumerator PM_CLK_ID_SDIO[](#_CPPv4N12pm_dev_clk_e14PM_CLK_ID_SDIOE "永久链接至目标")

    enumerator PM_CLK_ID_AUXS[](#_CPPv4N12pm_dev_clk_e14PM_CLK_ID_AUXSE "永久链接至目标")

    enumerator PM_CLK_ID_BTDM[](#_CPPv4N12pm_dev_clk_e14PM_CLK_ID_BTDME "永久链接至目标")

    enumerator PM_CLK_ID_XVR[](#_CPPv4N12pm_dev_clk_e13PM_CLK_ID_XVRE "永久链接至目标")

    enumerator PM_CLK_ID_MAC[](#_CPPv4N12pm_dev_clk_e13PM_CLK_ID_MACE "永久链接至目标")

    enumerator PM_CLK_ID_PHY[](#_CPPv4N12pm_dev_clk_e13PM_CLK_ID_PHYE "永久链接至目标")

    enumerator PM_CLK_ID_JPEG[](#_CPPv4N12pm_dev_clk_e14PM_CLK_ID_JPEGE "永久链接至目标")

    enumerator PM_CLK_ID_DISP[](#_CPPv4N12pm_dev_clk_e14PM_CLK_ID_DISPE "永久链接至目标")

    enumerator PM_CLK_ID_AUDIO[](#_CPPv4N12pm_dev_clk_e15PM_CLK_ID_AUDIOE "永久链接至目标")

    enumerator PM_CLK_ID_WDG_CPU[](#_CPPv4N12pm_dev_clk_e17PM_CLK_ID_WDG_CPUE "永久链接至目标")

    enumerator PM_CLK_ID_NONE[](#_CPPv4N12pm_dev_clk_e14PM_CLK_ID_NONEE "永久链接至目标")

enum pm_dev_clk_pwr_e[](#_CPPv416pm_dev_clk_pwr_e "永久链接至目标")
:   *Values:*

    enumerator PM_CLK_CTRL_PWR_DOWN[](#_CPPv4N16pm_dev_clk_pwr_e20PM_CLK_CTRL_PWR_DOWNE "永久链接至目标")

    enumerator PM_CLK_CTRL_PWR_UP[](#_CPPv4N16pm_dev_clk_pwr_e18PM_CLK_CTRL_PWR_UPE "永久链接至目标")

enum pm_dev_id_e[](#_CPPv411pm_dev_id_e "永久链接至目标")
:   *Values:*

    enumerator PM_DEV_ID_I2C1[](#_CPPv4N11pm_dev_id_e14PM_DEV_ID_I2C1E "永久链接至目标")

    enumerator PM_DEV_ID_SPI_1[](#_CPPv4N11pm_dev_id_e15PM_DEV_ID_SPI_1E "永久链接至目标")

    enumerator PM_DEV_ID_UART1[](#_CPPv4N11pm_dev_id_e15PM_DEV_ID_UART1E "永久链接至目标")

    enumerator PM_DEV_ID_WDG[](#_CPPv4N11pm_dev_id_e13PM_DEV_ID_WDGE "永久链接至目标")

    enumerator PM_DEV_ID_TIMER_1[](#_CPPv4N11pm_dev_id_e17PM_DEV_ID_TIMER_1E "永久链接至目标")

    enumerator PM_DEV_ID_SARADC[](#_CPPv4N11pm_dev_id_e16PM_DEV_ID_SARADCE "永久链接至目标")

    enumerator PM_DEV_ID_IRDA[](#_CPPv4N11pm_dev_id_e14PM_DEV_ID_IRDAE "永久链接至目标")

    enumerator PM_DEV_ID_EFUSE[](#_CPPv4N11pm_dev_id_e15PM_DEV_ID_EFUSEE "永久链接至目标")

    enumerator PM_DEV_ID_I2C2[](#_CPPv4N11pm_dev_id_e14PM_DEV_ID_I2C2E "永久链接至目标")

    enumerator PM_DEV_ID_SPI_2[](#_CPPv4N11pm_dev_id_e15PM_DEV_ID_SPI_2E "永久链接至目标")

    enumerator PM_DEV_ID_UART2[](#_CPPv4N11pm_dev_id_e15PM_DEV_ID_UART2E "永久链接至目标")

    enumerator PM_DEV_ID_UART3[](#_CPPv4N11pm_dev_id_e15PM_DEV_ID_UART3E "永久链接至目标")

    enumerator PM_DEV_ID_PWM_2[](#_CPPv4N11pm_dev_id_e15PM_DEV_ID_PWM_2E "永久链接至目标")

    enumerator PM_DEV_ID_TIMER_2[](#_CPPv4N11pm_dev_id_e17PM_DEV_ID_TIMER_2E "永久链接至目标")

    enumerator PM_DEV_ID_TIMER_3[](#_CPPv4N11pm_dev_id_e17PM_DEV_ID_TIMER_3E "永久链接至目标")

    enumerator PM_DEV_ID_TOUCH[](#_CPPv4N11pm_dev_id_e15PM_DEV_ID_TOUCHE "永久链接至目标")

    enumerator PM_DEV_ID_I2S_1[](#_CPPv4N11pm_dev_id_e15PM_DEV_ID_I2S_1E "永久链接至目标")

    enumerator PM_DEV_ID_USB_1[](#_CPPv4N11pm_dev_id_e15PM_DEV_ID_USB_1E "永久链接至目标")

    enumerator PM_DEV_ID_CAN[](#_CPPv4N11pm_dev_id_e13PM_DEV_ID_CANE "永久链接至目标")

    enumerator PM_DEV_ID_PSRAM[](#_CPPv4N11pm_dev_id_e15PM_DEV_ID_PSRAME "永久链接至目标")

    enumerator PM_DEV_ID_QSPI_1[](#_CPPv4N11pm_dev_id_e16PM_DEV_ID_QSPI_1E "永久链接至目标")

    enumerator PM_DEV_ID_QSPI_2[](#_CPPv4N11pm_dev_id_e16PM_DEV_ID_QSPI_2E "永久链接至目标")

    enumerator PM_DEV_ID_SDIO[](#_CPPv4N11pm_dev_id_e14PM_DEV_ID_SDIOE "永久链接至目标")

    enumerator PM_DEV_ID_AUXS[](#_CPPv4N11pm_dev_id_e14PM_DEV_ID_AUXSE "永久链接至目标")

    enumerator PM_DEV_ID_BTDM[](#_CPPv4N11pm_dev_id_e14PM_DEV_ID_BTDME "永久链接至目标")

    enumerator PM_DEV_ID_WPAS[](#_CPPv4N11pm_dev_id_e14PM_DEV_ID_WPASE "永久链接至目标")

    enumerator PM_DEV_ID_MAC[](#_CPPv4N11pm_dev_id_e13PM_DEV_ID_MACE "永久链接至目标")

    enumerator PM_DEV_ID_PHY[](#_CPPv4N11pm_dev_id_e13PM_DEV_ID_PHYE "永久链接至目标")

    enumerator PM_DEV_ID_JPEG[](#_CPPv4N11pm_dev_id_e14PM_DEV_ID_JPEGE "永久链接至目标")

    enumerator PM_DEV_ID_DISP[](#_CPPv4N11pm_dev_id_e14PM_DEV_ID_DISPE "永久链接至目标")

    enumerator PM_DEV_ID_AUDIO[](#_CPPv4N11pm_dev_id_e15PM_DEV_ID_AUDIOE "永久链接至目标")

    enumerator PM_DEV_ID_RTC[](#_CPPv4N11pm_dev_id_e13PM_DEV_ID_RTCE "永久链接至目标")

    enumerator PM_DEV_ID_GPIO[](#_CPPv4N11pm_dev_id_e14PM_DEV_ID_GPIOE "永久链接至目标")

    enumerator PM_DEV_ID_DECODER[](#_CPPv4N11pm_dev_id_e17PM_DEV_ID_DECODERE "永久链接至目标")

    enumerator PM_DEV_ID_LIN[](#_CPPv4N11pm_dev_id_e13PM_DEV_ID_LINE "永久链接至目标")

    enumerator PM_DEV_ID_PWM_1[](#_CPPv4N11pm_dev_id_e15PM_DEV_ID_PWM_1E "永久链接至目标")

    enumerator PM_DEV_ID_OTP_AHB[](#_CPPv4N11pm_dev_id_e17PM_DEV_ID_OTP_AHBE "永久链接至目标")

    enumerator PM_DEV_ID_OTP_APB[](#_CPPv4N11pm_dev_id_e17PM_DEV_ID_OTP_APBE "永久链接至目标")

    enumerator PM_DEV_ID_SHANHAI[](#_CPPv4N11pm_dev_id_e17PM_DEV_ID_SHANHAIE "永久链接至目标")

    enumerator PM_DEV_ID_KEY[](#_CPPv4N11pm_dev_id_e13PM_DEV_ID_KEYE "永久链接至目标")

    enumerator PM_DEV_ID_CPU1[](#_CPPv4N11pm_dev_id_e14PM_DEV_ID_CPU1E "永久链接至目标")

    enumerator PM_DEV_ID_DEFAULT[](#_CPPv4N11pm_dev_id_e17PM_DEV_ID_DEFAULTE "永久链接至目标")

    enumerator PM_DEV_ID_MAX[](#_CPPv4N11pm_dev_id_e13PM_DEV_ID_MAXE "永久链接至目标")

enum pm_cpu_freq_e[](#_CPPv413pm_cpu_freq_e "永久链接至目标")
:   *Values:*

    enumerator PM_CPU_FRQ_26M[](#_CPPv4N13pm_cpu_freq_e14PM_CPU_FRQ_26ME "永久链接至目标")

    enumerator PM_CPU_FRQ_60M[](#_CPPv4N13pm_cpu_freq_e14PM_CPU_FRQ_60ME "永久链接至目标")

    enumerator PM_CPU_FRQ_80M[](#_CPPv4N13pm_cpu_freq_e14PM_CPU_FRQ_80ME "永久链接至目标")

    enumerator PM_CPU_FRQ_120M[](#_CPPv4N13pm_cpu_freq_e15PM_CPU_FRQ_120ME "永久链接至目标")

    enumerator PM_CPU_FRQ_240M[](#_CPPv4N13pm_cpu_freq_e15PM_CPU_FRQ_240ME "永久链接至目标")

    enumerator PM_CPU_FRQ_320M[](#_CPPv4N13pm_cpu_freq_e15PM_CPU_FRQ_320ME "永久链接至目标")

    enumerator PM_CPU_FRQ_480M[](#_CPPv4N13pm_cpu_freq_e15PM_CPU_FRQ_480ME "永久链接至目标")

    enumerator PM_CPU_FRQ_DEFAULT[](#_CPPv4N13pm_cpu_freq_e18PM_CPU_FRQ_DEFAULTE "永久链接至目标")

enum pm_rosc_cali_mode_e[](#_CPPv419pm_rosc_cali_mode_e "永久链接至目标")
:   *Values:*

    enumerator PM_ROSC_CALI_AUTO[](#_CPPv4N19pm_rosc_cali_mode_e17PM_ROSC_CALI_AUTOE "永久链接至目标")

    enumerator PM_ROSC_CALI_MANUAL[](#_CPPv4N19pm_rosc_cali_mode_e19PM_ROSC_CALI_MANUALE "永久链接至目标")

    enumerator PM_ROSC_CALI_STOP[](#_CPPv4N19pm_rosc_cali_mode_e17PM_ROSC_CALI_STOPE "永久链接至目标")

enum pm_cb_priority_e[](#_CPPv416pm_cb_priority_e "永久链接至目标")
:   *Values:*

    enumerator PM_CB_PRIORITY_0[](#_CPPv4N16pm_cb_priority_e16PM_CB_PRIORITY_0E "永久链接至目标")

    enumerator PM_CB_PRIORITY_1[](#_CPPv4N16pm_cb_priority_e16PM_CB_PRIORITY_1E "永久链接至目标")

    enumerator PM_CB_PRIORITY_2[](#_CPPv4N16pm_cb_priority_e16PM_CB_PRIORITY_2E "永久链接至目标")

    enumerator PM_CB_PRIORITY_3[](#_CPPv4N16pm_cb_priority_e16PM_CB_PRIORITY_3E "永久链接至目标")

    enumerator PM_CB_PRIORITY_MAX[](#_CPPv4N16pm_cb_priority_e18PM_CB_PRIORITY_MAXE "永久链接至目标")

enum pm_cb_module_e[](#_CPPv414pm_cb_module_e "永久链接至目标")
:   *Values:*

    enumerator PM_32K_MODULE_BT[](#_CPPv4N14pm_cb_module_e16PM_32K_MODULE_BTE "永久链接至目标")

    enumerator PM_32K_MODULE_WIFI[](#_CPPv4N14pm_cb_module_e18PM_32K_MODULE_WIFIE "永久链接至目标")

    enumerator PM_32K_MODULE_MAX[](#_CPPv4N14pm_cb_module_e17PM_32K_MODULE_MAXE "永久链接至目标")

enum pm_sw_step_e[](#_CPPv412pm_sw_step_e "永久链接至目标")
:   *Values:*

    enumerator PM_32K_STEP_BEGIN[](#_CPPv4N12pm_sw_step_e17PM_32K_STEP_BEGINE "永久链接至目标")

    enumerator PM_32K_STEP_FINISH[](#_CPPv4N12pm_sw_step_e18PM_32K_STEP_FINISHE "永久链接至目标")

enum pm_low_vol_voltage_e[](#_CPPv420pm_low_vol_voltage_e "永久链接至目标")
:   *Values:*

    enumerator PM_LOW_VOL_VOLTAGE_0_6[](#_CPPv4N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_0_6E "永久链接至目标")

    enumerator PM_LOW_VOL_VOLTAGE_0_7[](#_CPPv4N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_0_7E "永久链接至目标")

    enumerator PM_LOW_VOL_VOLTAGE_0_8[](#_CPPv4N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_0_8E "永久链接至目标")

    enumerator PM_LOW_VOL_VOLTAGE_0_9[](#_CPPv4N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_0_9E "永久链接至目标")

    enumerator PM_LOW_VOL_VOLTAGE_1_0[](#_CPPv4N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_1_0E "永久链接至目标")

    enumerator PM_LOW_VOL_VOLTAGE_1_1[](#_CPPv4N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_1_1E "永久链接至目标")

    enumerator PM_LOW_VOL_VOLTAGE_1_2[](#_CPPv4N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_1_2E "永久链接至目标")

    enumerator PM_LOW_VOL_VOLTAGE_1_3[](#_CPPv4N20pm_low_vol_voltage_e22PM_LOW_VOL_VOLTAGE_1_3E "永久链接至目标")
