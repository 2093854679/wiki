# Audio APIs[](#audio-apis "永久链接至标题")


重要

The Audio API v1.0 is the lastest and stable Audio APIs. All new applications should use Audio API v1.0.


## Audio Interface[](#audio-interface "永久链接至标题")

The BK Audio Driver supports following functions:

> - adc function
> - dac function
> - eq function

The adc and dac function can be operated independently. However the eq function need to use with dac function together.


## Audio API Categories[](#audio-api-categories "永久链接至标题")

Most of Audio APIs can be categoried as:

> - Common APIs
>
>   The common APIs are prefixed with bk_aud, the APIs may be common for adc and dac interfaces, e.g. bk_aud_driver_init() etc.
> - Adc function APIs.
>
>   The APIs provide support for adc function. e.g. bk_aud_adc_init() etc.
> - Dac function APIs.
>
>   The APIs provide support for dac function. e.g. bk_aud_dac_init() etc.
> - Eq function APIs.
>
>   The APIs provide support for eq function. e.g. bk_aud_eq_init() etc.

Common APIs:
:   - [`bk_aud_driver_init()`](#_CPPv418bk_aud_driver_initv "bk_aud_driver_init") - init the audio driver

    - [`bk_aud_driver_deinit()`](#_CPPv420bk_aud_driver_deinitv "bk_aud_driver_deinit") - deinit the audio driver

    - [`bk_aud_register_aud_isr()`](#_CPPv423bk_aud_register_aud_isr12aud_isr_id_t9aud_isr_tPv "bk_aud_register_aud_isr") - register audio isr

Adc APIs:
:   - [`bk_aud_adc_init()`](#_CPPv415bk_aud_adc_init19aud_adc_work_mode_tPK16aud_adc_config_tPK17aud_dtmf_config_t "bk_aud_adc_init") - init the adc module of audio

    - [`bk_aud_adc_deinit()`](#_CPPv417bk_aud_adc_deinitv "bk_aud_adc_deinit") - deinit the adc module of audio

    - [`bk_aud_set_adc_samp_rate()`](#_CPPv424bk_aud_set_adc_samp_rate19aud_adc_samp_rate_t "bk_aud_set_adc_samp_rate") - set the sample rate in adc work mode

    - [`bk_aud_get_adc_fifo_addr()`](#_CPPv424bk_aud_get_adc_fifo_addrP8uint32_t "bk_aud_get_adc_fifo_addr") - get the adc fifo address in adc work mode

    - [`bk_aud_get_dtmf_fifo_addr()`](#_CPPv425bk_aud_get_dtmf_fifo_addrP8uint32_t "bk_aud_get_dtmf_fifo_addr") - get the dtmf fifo address in adc work mode

    - [`bk_aud_get_adc_status()`](#_CPPv421bk_aud_get_adc_statusP8uint32_t "bk_aud_get_adc_status") - get the adc status information in adc work mode

    - [`bk_aud_get_dtmf_status()`](#_CPPv422bk_aud_get_dtmf_statusP8uint32_t "bk_aud_get_dtmf_status") - get the dtmf status information in dtmf work mode

    - [`bk_aud_enable_adc_int()`](#_CPPv421bk_aud_enable_adc_intv "bk_aud_enable_adc_int") - enable adc interrupt

    - [`bk_aud_disable_adc_int()`](#_CPPv422bk_aud_disable_adc_intv "bk_aud_disable_adc_int") - disable adc interrupt

    - [`bk_aud_start_adc()`](#_CPPv416bk_aud_start_adcv "bk_aud_start_adc") - start adc function

    - [`bk_aud_stop_adc()`](#_CPPv415bk_aud_stop_adcv "bk_aud_stop_adc") - stop adc function

    - [`bk_aud_get_adc_fifo_data()`](#_CPPv424bk_aud_get_adc_fifo_dataP8uint32_t "bk_aud_get_adc_fifo_data") - get adc data

    - [`bk_aud_get_dtmf_fifo_data()`](#_CPPv425bk_aud_get_dtmf_fifo_dataP8uint32_t "bk_aud_get_dtmf_fifo_data") - get dtmf data

Dac APIs:
:   - [`bk_aud_dac_init()`](#_CPPv415bk_aud_dac_initPK16aud_dac_config_t "bk_aud_dac_init") - init the dac module of audio

    - [`bk_aud_dac_deinit()`](#_CPPv417bk_aud_dac_deinitv "bk_aud_dac_deinit") - deinit the dac module of audio

    - [`bk_aud_set_dac_samp_rate()`](#_CPPv424bk_aud_set_dac_samp_rate19aud_dac_samp_rate_t "bk_aud_set_dac_samp_rate") - set the sample rate of audio dac function

    - [`bk_aud_get_dac_fifo_addr()`](#_CPPv424bk_aud_get_dac_fifo_addrP8uint32_t "bk_aud_get_dac_fifo_addr") - get the dac fifo address

    - [`bk_aud_enable_dac_int()`](#_CPPv421bk_aud_enable_dac_intv "bk_aud_enable_dac_int") - enable dac interrupt function

    - [`bk_aud_disable_dac_int()`](#_CPPv422bk_aud_disable_dac_intv "bk_aud_disable_dac_int") - disable dac interrupt function

    - [`bk_aud_get_dac_status()`](#_CPPv421bk_aud_get_dac_statusP8uint32_t "bk_aud_get_dac_status") - get the dac fifo status information

    - [`bk_aud_start_dac()`](#_CPPv416bk_aud_start_dacv "bk_aud_start_dac") - start dac function

    - [`bk_aud_stop_dac()`](#_CPPv415bk_aud_stop_dacv "bk_aud_stop_dac") - stop dac function

Eq APIs:
:   - [`bk_aud_eq_init()`](#_CPPv414bk_aud_eq_initPK15aud_eq_config_t "bk_aud_eq_init") - init the eq module of audio

    - [`bk_aud_eq_deinit()`](#_CPPv416bk_aud_eq_deinitP15aud_eq_config_t "bk_aud_eq_deinit") - deinit the eq module of audio


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [aud.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/aud.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/aud.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_driver_init(void)[](#_CPPv418bk_aud_driver_initv "永久链接至目标")
:   Init the AUD driver.

    This API init the resoure common:


    - Init AUD driver control memory

    - Configure clock and power

    - Configure mic enable

    - Register AUD isr interrupt

    This API should be called before any other AUD APIs.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_driver_deinit(void)[](#_CPPv420bk_aud_driver_deinitv "永久链接至目标")
:   Deinit the AUD driver.

    This API free all resource related to AUD, power down AUD and mic.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_adc_init([aud_adc_work_mode_t](#_CPPv419aud_adc_work_mode_t "aud_adc_work_mode_t") adc_work_mode, const [aud_adc_config_t](#_CPPv416aud_adc_config_t "aud_adc_config_t") *adc_config, const [aud_dtmf_config_t](#_CPPv417aud_dtmf_config_t "aud_dtmf_config_t") *dtmf_config)[](#_CPPv415bk_aud_adc_init19aud_adc_work_mode_tPK16aud_adc_config_tPK17aud_dtmf_config_t "永久链接至目标")
:   Init the adc module of audio.

    This API init the adc module:


    - Set adc work mode: adc/dtmf

    - Configure the adc/dtmf parameters

    - disable adc/dtmf

    - disable adc/dtmf interrupts

    参数
    :   - **adc_work_mode** – adc work mode adc/dtmf

        - **adc_config** – adc configure of adc work mode

        - **dtmf_config** – dtmf configure of dtmf work mode

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_ADC_MODE: adc work mode is error

        - BK_ERR_NULL_PARAM: config is NULL

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_adc_deinit(void)[](#_CPPv417bk_aud_adc_deinitv "永久链接至目标")
:   Deinit adc module.

    This API deinit the adc module of audio:


    - Disable adc and dtmf

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_set_adc_samp_rate([aud_adc_samp_rate_t](#_CPPv419aud_adc_samp_rate_t "aud_adc_samp_rate_t") samp_rate)[](#_CPPv424bk_aud_set_adc_samp_rate19aud_adc_samp_rate_t "永久链接至目标")
:   Set the sample rate in adc work mode.

    参数
    :   **samp_rate** – adc sample rate of adc work mode

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_set_adc_gain(uint32_t value)[](#_CPPv419bk_aud_set_adc_gain8uint32_t "永久链接至目标")
:   Set the adc gain in adc work mode.

    参数
    :   **value** – the gain value of adc work mode

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_set_mic_chl([aud_mic_enable_t](#_CPPv416aud_mic_enable_t "aud_mic_enable_t") mic_chl)[](#_CPPv418bk_aud_set_mic_chl16aud_mic_enable_t "永久链接至目标")
:   Set the adc gain in adc work mode.

    参数
    :   **mic_chl** – the mic channel value of adc work mode

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_set_mic_intf_mode([aud_mic_id_t](#_CPPv412aud_mic_id_t "aud_mic_id_t") mic_id, [aud_adc_intf_mode_t](#_CPPv419aud_adc_intf_mode_t "aud_adc_intf_mode_t") intf_mode)[](#_CPPv424bk_aud_set_mic_intf_mode12aud_mic_id_t19aud_adc_intf_mode_t "永久链接至目标")
:   Set the mic external interface mode in adc work mode.

    参数
    :   - **mic_id** – the mic id

        - **intf_mode** – signal end or difference

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_get_adc_fifo_addr(uint32_t *adc_fifo_addr)[](#_CPPv424bk_aud_get_adc_fifo_addrP8uint32_t "永久链接至目标")
:   Get the adc fifo address in adc work mode.

    参数
    :   **adc_fifo_addr** – adc fifo address of adc work mode

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_get_dtmf_fifo_addr(uint32_t *dtmf_fifo_addr)[](#_CPPv425bk_aud_get_dtmf_fifo_addrP8uint32_t "永久链接至目标")
:   Get the dtmf fifo address in adc work mode.

    参数
    :   **dtmf_fifo_addr** – dtmf fifo address of dtmf work mode

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_get_dac_fifo_addr(uint32_t *dac_fifo_addr)[](#_CPPv424bk_aud_get_dac_fifo_addrP8uint32_t "永久链接至目标")
:   Get the dac fifo address.

    参数
    :   **dac_fifo_addr, :** – dac fifo address

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_get_adc_status(uint32_t *adc_status)[](#_CPPv421bk_aud_get_adc_statusP8uint32_t "永久链接至目标")
:   Get the adc status information in adc work mode.

    This API get the adc status of adc work mode:


    - Get fifo status

    参数
    :   **adc_status** – adc fifo status and agc status

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_get_dtmf_status(uint32_t *dtmf_status)[](#_CPPv422bk_aud_get_dtmf_statusP8uint32_t "永久链接至目标")
:   Get the dtmf status information in dtmf work mode.

    This API get the adc status of dtmf work mode:


    - Get fifo status

    参数
    :   **dtmf_status** – dtmf fifo status

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_enable_adc_int(void)[](#_CPPv421bk_aud_enable_adc_intv "永久链接至目标")
:   Enable adc interrupt.

    This API enable adc interrupt:


    - Enable adc interrupt if work mode is adc work mode

    - Enable dtmf interrupt if work mode is dtmf work mode

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_disable_adc_int(void)[](#_CPPv422bk_aud_disable_adc_intv "永久链接至目标")
:   Disable adc interrupt.

    This API disable adc interrupt:


    - Disable adc interrupt if work mode is adc work mode

    - Disable dtmf interrupt if work mode is dtmf work mode

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_start_adc(void)[](#_CPPv416bk_aud_start_adcv "永久链接至目标")
:   Start adc.

    This API start adc:


    - Enable adc if work mode is adc work mode

    - Enable dtmf if work mode is dtmf work mode

    Usage example:

    ```
    //init audio driver
    bk_aud_driver_init();

    //init adc configuration
    aud_adc_config_t adc_config;
    adc_config.samp_rate = AUD_ADC_SAMP_RATE_8K;
    adc_config.adc_enable = AUD_ADC_DISABLE;
    adc_config.line_enable = AUD_ADC_LINE_DISABLE;
    adc_config.dtmf_enable = AUD_DTMF_DISABLE;
    adc_config.adc_hpf2_coef_B2 = 0;
    adc_config.adc_hpf2_bypass_enable = AUD_ADC_HPF_BYPASS_ENABLE;
    adc_config.adc_hpf1_bypass_enable = AUD_ADC_HPF_BYPASS_ENABLE;
    adc_config.adc_set_gain = 0x2d;
    adc_config.adc_samp_edge = AUD_ADC_SAMP_EDGE_RISING;
    adc_config.adc_hpf2_coef_B0 = 0;
    adc_config.adc_hpf2_coef_B1 = 0;
    adc_config.adc_hpf2_coef_A0 = 0;
    adc_config.adc_hpf2_coef_A1 = 0;
    adc_config.dtmf_wr_threshold = 8;
    adc_config.adcl_wr_threshold = 8;
    adc_config.dtmf_int_enable = AUD_DTMF_INT_DISABLE;
    adc_config.adcl_int_enable = AUD_ADCL_INT_DISABLE;
    adc_config.loop_adc2dac = AUD_LOOP_ADC2DAC_DISABLE;
    adc_config.agc_noise_thrd = 101;
    adc_config.agc_noise_high = 101;
    adc_config.agc_noise_low = 160;
    adc_config.agc_noise_min = 1;
    adc_config.agc_noise_tout = 0;
    adc_config.agc_high_dur = 3;
    adc_config.agc_low_dur = 3;
    adc_config.agc_min = 1;
    adc_config.agc_max = 4;
    adc_config.agc_ng_method = AUD_AGC_NG_METHOD_MUTE;
    adc_config.agc_ng_enable = AUD_AGC_NG_DISABLE;
    adc_config.agc_decay_time = AUD_AGC_DECAY_TIME_128;
    adc_config.agc_attack_time = AUD_AGC_ATTACK_TIME_128;
    adc_config.agc_high_thrd = 18;
    adc_config.agc_low_thrd = 0;
    adc_config.agc_iir_coef = AUD_AGC_IIR_COEF_1_1024;
    adc_config.agc_enable = AUD_AGC_DISABLE;
    adc_config.manual_pga_value = 0;
    adc_config.manual_pga_enable = AUD_GAC_MANUAL_PGA_DISABLE;
    bk_aud_adc_init(AUD_ADC_WORK_MODE_ADC, &adc_config, NULL);
    CLI_LOGI("init adc successful\n");

    //start adc and dac
    bk_aud_start_adc();
    ```

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_ADC_MODE: adc work mode is NULL

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_stop_adc(void)[](#_CPPv415bk_aud_stop_adcv "永久链接至目标")
:   Stop adc.

    This API stop adc:


    - Disable adc if work mode is adc work mode

    - Disable dtmf if work mode is dtmf work mode

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_ADC_MODE: adc work mode is NULL

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_get_adc_fifo_data(uint32_t *adc_data)[](#_CPPv424bk_aud_get_adc_fifo_dataP8uint32_t "永久链接至目标")
:   Get adc data.

    This API get adc fifo data

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_ADC_MODE: adc work mode is NULL

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_get_dtmf_fifo_data(uint32_t *dtmf_data)[](#_CPPv425bk_aud_get_dtmf_fifo_dataP8uint32_t "永久链接至目标")
:   Get dtmf data.

    This API get dtmf fifo data

    参数
    :   **dtmf_data, :** – save dtmf data

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_ADC_MODE: dtmf work mode is NULL

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_dac_init(const [aud_dac_config_t](#_CPPv416aud_dac_config_t "aud_dac_config_t") *dac_config)[](#_CPPv415bk_aud_dac_initPK16aud_dac_config_t "永久链接至目标")
:   Init the dac module of audio.

    This API init the dac module:


    - Configure the dac parameters to enable dac function.

    参数
    :   **dac_config, :** – dac parameters configure

    返回
    :   - BK_OK: succeed

        - BK_ERR_NULL_PARAM: config is NULL

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_dac_deinit(void)[](#_CPPv417bk_aud_dac_deinitv "永久链接至目标")
:   Deinit dac module of audio.

    This API deinit the dac module:


    - Configure the dac parameters to default value.

    参数
    :   **None** –

    返回
    :   - BK_OK: succeed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_set_dac_samp_rate([aud_dac_samp_rate_t](#_CPPv419aud_dac_samp_rate_t "aud_dac_samp_rate_t") samp_rate)[](#_CPPv424bk_aud_set_dac_samp_rate19aud_dac_samp_rate_t "永久链接至目标")
:   Set the dac sample rate.

    This API set the dac sample rate value.

    参数
    :   **samp_rate, :** – dac sample rate

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_set_dac_gain(uint32_t value)[](#_CPPv419bk_aud_set_dac_gain8uint32_t "永久链接至目标")
:   Set the dac gain.

    参数
    :   **value** – the gain value, range:0x00 ~ 0x3f

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_set_dac_chl([aud_dac_chl_enable_t](#_CPPv420aud_dac_chl_enable_t "aud_dac_chl_enable_t") dac_chl)[](#_CPPv418bk_aud_set_dac_chl20aud_dac_chl_enable_t "永久链接至目标")
:   Set the dac channel.

    参数
    :   **dac_chl** – the channel value

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_enable_dac_int(void)[](#_CPPv421bk_aud_enable_dac_intv "永久链接至目标")
:   Enable dac interrupt.

    This API enable dac interrupt:

    参数
    :   **None** –

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_disable_dac_int(void)[](#_CPPv422bk_aud_disable_dac_intv "永久链接至目标")
:   Disable dac interrupt.

    This API disable dac interrupt:

    参数
    :   **None** –

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_get_dac_status(uint32_t *dac_status)[](#_CPPv421bk_aud_get_dac_statusP8uint32_t "永久链接至目标")
:   Get the dac status information.

    This API get the dac fifo status.

    Usage example:

    uint32_t dac_fifo_status = 0; bk_aud_get_dac_status(&dac_fifo_status); if (dac_fifo_status & AUD_DACL_NEAR_EMPTY_MASK) { }

    参数
    :   **dac_status, :** – dac fifo status

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_start_dac(void)[](#_CPPv416bk_aud_start_dacv "永久链接至目标")
:   Start dac.

    This API start dac function.

    参数
    :   **None** –

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_stop_dac(void)[](#_CPPv415bk_aud_stop_dacv "永久链接至目标")
:   Stop dac.

    This API stop dac function.

    参数
    :   **None** –

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_eq_init(const [aud_eq_config_t](#_CPPv415aud_eq_config_t "aud_eq_config_t") *eq_config)[](#_CPPv414bk_aud_eq_initPK15aud_eq_config_t "永久链接至目标")
:   Init the eq module of audio.

    This API init the eq module:


    - Configure the eq parameters to enable the eq function.

    参数
    :   **eq_config, :** – eq parameter configure

    返回
    :   - BK_OK: succeed

        - BK_ERR_NULL_PARAM: config is NULL

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_eq_deinit([aud_eq_config_t](#_CPPv415aud_eq_config_t "aud_eq_config_t") *eq_config)[](#_CPPv416bk_aud_eq_deinitP15aud_eq_config_t "永久链接至目标")
:   Deinit the eq module of audio.

    This API deinit the eq module:


    - Configure the eq parameters to default value.

    参数
    :   **eq_config, :** – eq parameter configure

    返回
    :   - BK_OK: succeed

        - BK_ERR_NULL_PARAM: config is NULL

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_register_aud_isr([aud_isr_id_t](#_CPPv412aud_isr_id_t "aud_isr_id_t") isr_id, [aud_isr_t](#_CPPv49aud_isr_t "aud_isr_t") isr, void *param)[](#_CPPv423bk_aud_register_aud_isr12aud_isr_id_t9aud_isr_tPv "永久链接至目标")
:   Register audio isr.

    This API register audio isr:


    - Disable adc if work mode is adc work mode

    - Disable dtmf if work mode is dtmf work mode

    Usage example:

    ```
    void cli_aud_adcl_isr(void *param)
    {
        uint32_t adc_data;
        uint32_t adc_status;

        bk_aud_get_adc_status(&adc_status);
        if (adc_status & AUD_ADCL_NEAR_FULL_MASK) {
            bk_aud_get_adc_fifo_data(&adc_data);
            bk_aud_dac_write(adc_data);
        }
    }

    //register isr
    ret = bk_aud_register_aud_isr(AUD_ISR_ADCL, cli_aud_adcl_isr, NULL);
    CLI_LOGI("register adc isr successful\n");

    //enable audio interrupt
    bk_aud_enable_adc_int();
    CLI_LOGI("enable adc interrupt successful\n");
    ```

    参数
    :   - **isr_id** – adc work mode adc/dtmf

        - **isr** – audio isr callback

        - **param** – audio isr callback parameter

    返回
    :   - BK_OK: succeed

        - BK_ERR_AUD_ADC_MODE: adc work mode is NULL

        - BK_ERR_AUD_NOT_INIT: audio driver is not init

        - others: other errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_dac_dwa_bypass_control(uint8_t value)[](#_CPPv429bk_aud_dac_dwa_bypass_control7uint8_t "永久链接至目标")

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_dac_set_ana_gain(uint8_t value)[](#_CPPv423bk_aud_dac_set_ana_gain7uint8_t "永久链接至目标")

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_aud_dac_get_ana_gain(uint32_t *gain)[](#_CPPv423bk_aud_dac_get_ana_gainP8uint32_t "永久链接至目标")


## API Typedefs[](#api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [aud_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/aud_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/aud_types.h")


### Structures[](#structures "永久链接至标题")

struct aud_int_config_t[](#_CPPv416aud_int_config_t "永久链接至目标")

struct aud_dtmf_config_t[](#_CPPv417aud_dtmf_config_t "永久链接至目标")
:   Public Members

    [aud_adc_enable_t](#_CPPv416aud_adc_enable_t "aud_adc_enable_t") adc_enable[](#_CPPv4N17aud_dtmf_config_t10adc_enableE "永久链接至目标")
    :   AUD adc enable

    [aud_adc_line_enable_t](#_CPPv421aud_adc_line_enable_t "aud_adc_line_enable_t") line_enable[](#_CPPv4N17aud_dtmf_config_t11line_enableE "永久链接至目标")
    :   AUD line in enable

    [aud_dtmf_enable_t](#_CPPv417aud_dtmf_enable_t "aud_dtmf_enable_t") dtmf_enable[](#_CPPv4N17aud_dtmf_config_t11dtmf_enableE "永久链接至目标")
    :   AUD dtmf enable

    [aud_dtmf_tone_pattern_t](#_CPPv423aud_dtmf_tone_pattern_t "aud_dtmf_tone_pattern_t") tone_pattern[](#_CPPv4N17aud_dtmf_config_t12tone_patternE "永久链接至目标")
    :   AUD dtmf tone pattern

    [aud_dtmf_tone_mode_t](#_CPPv420aud_dtmf_tone_mode_t "aud_dtmf_tone_mode_t") tone_mode[](#_CPPv4N17aud_dtmf_config_t9tone_modeE "永久链接至目标")
    :   AUD dtmf tone mode

    uint32_t tone_pause_time[](#_CPPv4N17aud_dtmf_config_t15tone_pause_timeE "永久链接至目标")
    :   AUD dtmf tone pause time

    uint32_t tone_active_time[](#_CPPv4N17aud_dtmf_config_t16tone_active_timeE "永久链接至目标")
    :   AUD dtmf tone active time

    uint32_t tone1_step[](#_CPPv4N17aud_dtmf_config_t10tone1_stepE "永久链接至目标")
    :   AUD dtmf Tone1 frequency set Step = F(KHz) * 8191

    [aud_dtmf_tone_attu_t](#_CPPv420aud_dtmf_tone_attu_t "aud_dtmf_tone_attu_t") tone1_attu[](#_CPPv4N17aud_dtmf_config_t10tone1_attuE "永久链接至目标")
    :   AUD dtmf Tone1 damp set 0 ：-1 ：-15 dB

    [aud_dtmf_tone_enable_t](#_CPPv422aud_dtmf_tone_enable_t "aud_dtmf_tone_enable_t") tone1_enable[](#_CPPv4N17aud_dtmf_config_t12tone1_enableE "永久链接至目标")
    :   AUD dtmf tone1 enable

    uint32_t tone2_step[](#_CPPv4N17aud_dtmf_config_t10tone2_stepE "永久链接至目标")
    :   AUD dtmf Tone2 frequency set Step = F(KHz) * 8191

    [aud_dtmf_tone_attu_t](#_CPPv420aud_dtmf_tone_attu_t "aud_dtmf_tone_attu_t") tone2_attu[](#_CPPv4N17aud_dtmf_config_t10tone2_attuE "永久链接至目标")
    :   AUD dtmf Tone2 damp set 0 ：-1 ：-15 dB

    [aud_dtmf_tone_enable_t](#_CPPv422aud_dtmf_tone_enable_t "aud_dtmf_tone_enable_t") tone2_enable[](#_CPPv4N17aud_dtmf_config_t12tone2_enableE "永久链接至目标")
    :   AUD dtmf tone2 enable

    uint32_t dtmf_wr_threshold[](#_CPPv4N17aud_dtmf_config_t17dtmf_wr_thresholdE "永久链接至目标")
    :   AUD dtmf write threshold value

    [aud_dtmf_int_t](#_CPPv414aud_dtmf_int_t "aud_dtmf_int_t") dtmf_int_enable[](#_CPPv4N17aud_dtmf_config_t15dtmf_int_enableE "永久链接至目标")
    :   AUD dtmf interrupt request enable

    [aud_loop_dtmf2dac_t](#_CPPv419aud_loop_dtmf2dac_t "aud_loop_dtmf2dac_t") loop_ton2dac[](#_CPPv4N17aud_dtmf_config_t12loop_ton2dacE "永久链接至目标")
    :   AUD dtmf to DAC loop test enable

struct aud_adc_config_t[](#_CPPv416aud_adc_config_t "永久链接至目标")
:   Public Members

    [aud_adc_samp_rate_t](#_CPPv419aud_adc_samp_rate_t "aud_adc_samp_rate_t") samp_rate[](#_CPPv4N16aud_adc_config_t9samp_rateE "永久链接至目标")
    :   AUD adc sample rate

    [aud_adc_enable_t](#_CPPv416aud_adc_enable_t "aud_adc_enable_t") adc_enable[](#_CPPv4N16aud_adc_config_t10adc_enableE "永久链接至目标")
    :   AUD adc enable

    [aud_adc_line_enable_t](#_CPPv421aud_adc_line_enable_t "aud_adc_line_enable_t") line_enable[](#_CPPv4N16aud_adc_config_t11line_enableE "永久链接至目标")
    :   AUD line in enable

    [aud_dtmf_enable_t](#_CPPv417aud_dtmf_enable_t "aud_dtmf_enable_t") dtmf_enable[](#_CPPv4N16aud_adc_config_t11dtmf_enableE "永久链接至目标")
    :   AUD dtmf enable

    uint32_t adc_hpf2_coef_B2[](#_CPPv4N16aud_adc_config_t16adc_hpf2_coef_B2E "永久链接至目标")
    :   AUD adc HPF2 coefficient B2

    [aud_adc_hpf_bypass_t](#_CPPv420aud_adc_hpf_bypass_t "aud_adc_hpf_bypass_t") adc_hpf2_bypass_enable[](#_CPPv4N16aud_adc_config_t22adc_hpf2_bypass_enableE "永久链接至目标")
    :   AUD adc hpf2 disable

    [aud_adc_hpf_bypass_t](#_CPPv420aud_adc_hpf_bypass_t "aud_adc_hpf_bypass_t") adc_hpf1_bypass_enable[](#_CPPv4N16aud_adc_config_t22adc_hpf1_bypass_enableE "永久链接至目标")
    :   AUD adc hpf1 disable

    uint32_t adc_set_gain[](#_CPPv4N16aud_adc_config_t12adc_set_gainE "永久链接至目标")
    :   AUD adc gain set

    [aud_adc_samp_edge_t](#_CPPv419aud_adc_samp_edge_t "aud_adc_samp_edge_t") adc_samp_edge[](#_CPPv4N16aud_adc_config_t13adc_samp_edgeE "永久链接至目标")
    :   ADC data sampling clock edge select rising/falling

    uint32_t adc_hpf2_coef_B0[](#_CPPv4N16aud_adc_config_t16adc_hpf2_coef_B0E "永久链接至目标")
    :   AUD adc HPF2 coefficient B0

    uint32_t adc_hpf2_coef_B1[](#_CPPv4N16aud_adc_config_t16adc_hpf2_coef_B1E "永久链接至目标")
    :   AUD adc HPF2 coefficient B1

    uint32_t adc_hpf2_coef_A0[](#_CPPv4N16aud_adc_config_t16adc_hpf2_coef_A0E "永久链接至目标")
    :   AUD adc HPF2 coefficient A0

    uint32_t adc_hpf2_coef_A1[](#_CPPv4N16aud_adc_config_t16adc_hpf2_coef_A1E "永久链接至目标")
    :   AUD adc HPF2 coefficient A1

    uint32_t dtmf_wr_threshold[](#_CPPv4N16aud_adc_config_t17dtmf_wr_thresholdE "永久链接至目标")
    :   AUD dtmf write threshold value

    uint32_t adcl_wr_threshold[](#_CPPv4N16aud_adc_config_t17adcl_wr_thresholdE "永久链接至目标")
    :   AUD adcl write threshold value

    [aud_dtmf_int_t](#_CPPv414aud_dtmf_int_t "aud_dtmf_int_t") dtmf_int_enable[](#_CPPv4N16aud_adc_config_t15dtmf_int_enableE "永久链接至目标")
    :   AUD dtmf interrupt request enable

    [aud_adcl_int_t](#_CPPv414aud_adcl_int_t "aud_adcl_int_t") adcl_int_enable[](#_CPPv4N16aud_adc_config_t15adcl_int_enableE "永久链接至目标")
    :   AUD adcl interrupt request enable

    [aud_loop_adc2dac_t](#_CPPv418aud_loop_adc2dac_t "aud_loop_adc2dac_t") loop_adc2dac[](#_CPPv4N16aud_adc_config_t12loop_adc2dacE "永久链接至目标")
    :   AUD adc to DAC loop test enable

    uint32_t agc_noise_thrd[](#_CPPv4N16aud_adc_config_t14agc_noise_thrdE "永久链接至目标")
    :   AUD AGC noise gating of excute，noise gating work when audio value is little

    uint32_t agc_noise_high[](#_CPPv4N16aud_adc_config_t14agc_noise_highE "永久链接至目标")
    :   AUD AGC corresponding MIC_RSSI low 10 bit

    uint32_t agc_noise_low[](#_CPPv4N16aud_adc_config_t13agc_noise_lowE "永久链接至目标")
    :   AUD AGC corresponding MIC_RSSI low 10 bit

    uint32_t agc_noise_min[](#_CPPv4N16aud_adc_config_t13agc_noise_minE "永久链接至目标")
    :   AUD AGC {GAIN2[2:0] GAIN1[3:0]} when signal level below NOISE_LOW, when noise gating is enabled

    [aud_gac_noise_tout_t](#_CPPv420aud_gac_noise_tout_t "aud_gac_noise_tout_t") agc_noise_tout[](#_CPPv4N16aud_adc_config_t14agc_noise_toutE "永久链接至目标")
    :   AUD AGC noise tout

    [aud_gac_high_dur_t](#_CPPv418aud_gac_high_dur_t "aud_gac_high_dur_t") agc_high_dur[](#_CPPv4N16aud_adc_config_t12agc_high_durE "永久链接至目标")
    :   AUD AGC high noise gating work duration

    [aud_gac_low_dur_t](#_CPPv417aud_gac_low_dur_t "aud_gac_low_dur_t") agc_low_dur[](#_CPPv4N16aud_adc_config_t11agc_low_durE "永久链接至目标")
    :   AUD AGC low noise gating work duration

    uint32_t agc_min[](#_CPPv4N16aud_adc_config_t7agc_minE "永久链接至目标")
    :   AUD AGC Minimum value of {GAIN2[2:0] GAIN1[3:0]}

    uint32_t agc_max[](#_CPPv4N16aud_adc_config_t7agc_maxE "永久链接至目标")
    :   AUD AGC Maximum value of {GAIN2[2:0] GAIN1[3:0]} Also the default gain setting when AGC is disabled

    [aud_agc_method_t](#_CPPv416aud_agc_method_t "aud_agc_method_t") agc_ng_method[](#_CPPv4N16aud_adc_config_t13agc_ng_methodE "永久链接至目标")
    :   AUD AGC noise gating method

    [aud_agc_ng_enable_t](#_CPPv419aud_agc_ng_enable_t "aud_agc_ng_enable_t") agc_ng_enable[](#_CPPv4N16aud_adc_config_t13agc_ng_enableE "永久链接至目标")
    :   AUD AGC enable noise gating

    [aud_agc_decay_time_t](#_CPPv420aud_agc_decay_time_t "aud_agc_decay_time_t") agc_decay_time[](#_CPPv4N16aud_adc_config_t14agc_decay_timeE "永久链接至目标")
    :   AUD AGC agc decay time

    [aud_agc_attack_time_t](#_CPPv421aud_agc_attack_time_t "aud_agc_attack_time_t") agc_attack_time[](#_CPPv4N16aud_adc_config_t15agc_attack_timeE "永久链接至目标")
    :   AUD AGC agc attack time

    uint32_t agc_high_thrd[](#_CPPv4N16aud_adc_config_t13agc_high_thrdE "永久链接至目标")
    :   AUD AGC coefficient high five bit of MIC_RSSI

    uint32_t agc_low_thrd[](#_CPPv4N16aud_adc_config_t12agc_low_thrdE "永久链接至目标")
    :   AUD AGC coefficient low five bit of MIC_RSSI

    [aud_agc_iir_coef_t](#_CPPv418aud_agc_iir_coef_t "aud_agc_iir_coef_t") agc_iir_coef[](#_CPPv4N16aud_adc_config_t12agc_iir_coefE "永久链接至目标")
    :   AUD AGC iir coefficient select

    [aud_agc_enable_t](#_CPPv416aud_agc_enable_t "aud_agc_enable_t") agc_enable[](#_CPPv4N16aud_adc_config_t10agc_enableE "永久链接至目标")
    :   AUD AGC enable

    uint32_t manual_pga_value[](#_CPPv4N16aud_adc_config_t16manual_pga_valueE "永久链接至目标")
    :   AUD AGC manual set PGA value

    [aud_agc_manual_pga_en_t](#_CPPv423aud_agc_manual_pga_en_t "aud_agc_manual_pga_en_t") manual_pga_enable[](#_CPPv4N16aud_adc_config_t17manual_pga_enableE "永久链接至目标")
    :   AUD AGC manual set PGA enable

struct aud_dac_config_t[](#_CPPv416aud_dac_config_t "永久链接至目标")
:   Public Members

    [aud_dac_enable_t](#_CPPv416aud_dac_enable_t "aud_dac_enable_t") dac_enable[](#_CPPv4N16aud_dac_config_t10dac_enableE "永久链接至目标")
    :   AUD dac enable

    [aud_dac_samp_rate_t](#_CPPv419aud_dac_samp_rate_t "aud_dac_samp_rate_t") samp_rate[](#_CPPv4N16aud_dac_config_t9samp_rateE "永久链接至目标")
    :   AUD dac sample rate

    [aud_dac_chl_enable_t](#_CPPv420aud_dac_chl_enable_t "aud_dac_chl_enable_t") dac_chl[](#_CPPv4N16aud_dac_config_t7dac_chlE "永久链接至目标")
    :   AUD dac channel

    [aud_dac_work_mode_t](#_CPPv419aud_dac_work_mode_t "aud_dac_work_mode_t") work_mode[](#_CPPv4N16aud_dac_config_t9work_modeE "永久链接至目标")
    :   AUD dac work mode

    uint16_t dac_hpf2_coef_B2[](#_CPPv4N16aud_dac_config_t16dac_hpf2_coef_B2E "永久链接至目标")
    :   AUD dac HPF2 coefficient B2

    [aud_dac_hpf_bypass_t](#_CPPv420aud_dac_hpf_bypass_t "aud_dac_hpf_bypass_t") dac_hpf2_bypass_enable[](#_CPPv4N16aud_dac_config_t22dac_hpf2_bypass_enableE "永久链接至目标")
    :   AUD dac hpf2 disable

    [aud_dac_hpf_bypass_t](#_CPPv420aud_dac_hpf_bypass_t "aud_dac_hpf_bypass_t") dac_hpf1_bypass_enable[](#_CPPv4N16aud_dac_config_t22dac_hpf1_bypass_enableE "永久链接至目标")
    :   AUD dac hpf1 disable

    uint16_t dac_set_gain[](#_CPPv4N16aud_dac_config_t12dac_set_gainE "永久链接至目标")
    :   AUD dac gain set

    [aud_dac_clk_invert_t](#_CPPv420aud_dac_clk_invert_t "aud_dac_clk_invert_t") dac_clk_invert[](#_CPPv4N16aud_dac_config_t14dac_clk_invertE "永久链接至目标")
    :   AUD dac output clock edge select

    uint16_t dac_hpf2_coef_B0[](#_CPPv4N16aud_dac_config_t16dac_hpf2_coef_B0E "永久链接至目标")
    :   AUD dac HPF2 coefficient B0

    uint16_t dac_hpf2_coef_B1[](#_CPPv4N16aud_dac_config_t16dac_hpf2_coef_B1E "永久链接至目标")
    :   AUD dac HPF2 coefficient B1

    uint16_t dac_hpf2_coef_A1[](#_CPPv4N16aud_dac_config_t16dac_hpf2_coef_A1E "永久链接至目标")
    :   AUD dac HPF2 coefficient A1

    uint16_t dac_hpf2_coef_A2[](#_CPPv4N16aud_dac_config_t16dac_hpf2_coef_A2E "永久链接至目标")
    :   AUD dac HPF2 coefficient A2

    uint8_t dacr_rd_threshold[](#_CPPv4N16aud_dac_config_t17dacr_rd_thresholdE "永久链接至目标")
    :   AUD dacl read threshold value

    uint8_t dacl_rd_threshold[](#_CPPv4N16aud_dac_config_t17dacl_rd_thresholdE "永久链接至目标")
    :   AUD dacr read threshold value

    uint8_t dacr_int_enable[](#_CPPv4N16aud_dac_config_t15dacr_int_enableE "永久链接至目标")
    :   AUD dacr interrupt request enable

    uint8_t dacl_int_enable[](#_CPPv4N16aud_dac_config_t15dacl_int_enableE "永久链接至目标")
    :   AUD dacl interrupt request enable

    [aud_dac_filt_enable_t](#_CPPv421aud_dac_filt_enable_t "aud_dac_filt_enable_t") dac_filt_enable[](#_CPPv4N16aud_dac_config_t15dac_filt_enableE "永久链接至目标")
    :   AUD dac filter enable

struct aud_eq_config_t[](#_CPPv415aud_eq_config_t "永久链接至目标")


### Macros[](#macros "永久链接至标题")

BK_ERR_AUD_NOT_INIT[](#c.BK_ERR_AUD_NOT_INIT "永久链接至目标")
:   AUD driver not init

BK_ERR_AUD_ISR_ID[](#c.BK_ERR_AUD_ISR_ID "永久链接至目标")
:   AUD isr id is invalid

BK_ERR_AUD_ADC_MODE[](#c.BK_ERR_AUD_ADC_MODE "永久链接至目标")
:   AUD adc work mode is invalid

AUD_HAL_REG_BASE[](#c.AUD_HAL_REG_BASE "永久链接至目标")

AUD_DAC_FIFO_ADDR[](#c.AUD_DAC_FIFO_ADDR "永久链接至目标")


### Type Definitions[](#type-definitions "永久链接至标题")

typedef void (*aud_isr_t)(void *param)[](#_CPPv49aud_isr_t "永久链接至目标")


### Enumerations[](#enumerations "永久链接至标题")

enum aud_isr_id_t[](#_CPPv412aud_isr_id_t "永久链接至目标")
:   *Values:*

    enumerator AUD_ISR_DTMF[](#_CPPv4N12aud_isr_id_t12AUD_ISR_DTMFE "永久链接至目标")
    :   dtmf_int_en

    enumerator AUD_ISR_ADCL[](#_CPPv4N12aud_isr_id_t12AUD_ISR_ADCLE "永久链接至目标")
    :   adcl_int_en

    enumerator AUD_ISR_DACR[](#_CPPv4N12aud_isr_id_t12AUD_ISR_DACRE "永久链接至目标")
    :   dacr_int_en

    enumerator AUD_ISR_DACL[](#_CPPv4N12aud_isr_id_t12AUD_ISR_DACLE "永久链接至目标")
    :   dacl_int_en

    enumerator AUD_ISR_MAX[](#_CPPv4N12aud_isr_id_t11AUD_ISR_MAXE "永久链接至目标")
    :   AUD isr id max

enum aud_adc_work_mode_t[](#_CPPv419aud_adc_work_mode_t "永久链接至目标")
:   *Values:*

    enumerator AUD_ADC_WORK_MODE_NULL[](#_CPPv4N19aud_adc_work_mode_t22AUD_ADC_WORK_MODE_NULLE "永久链接至目标")
    :   no mode

    enumerator AUD_ADC_WORK_MODE_ADC[](#_CPPv4N19aud_adc_work_mode_t21AUD_ADC_WORK_MODE_ADCE "永久链接至目标")
    :   ADC mode

    enumerator AUD_ADC_WORK_MODE_DTMF[](#_CPPv4N19aud_adc_work_mode_t22AUD_ADC_WORK_MODE_DTMFE "永久链接至目标")
    :   DTMF mode

    enumerator AUD_ADC_WORK_MODE_MAX[](#_CPPv4N19aud_adc_work_mode_t21AUD_ADC_WORK_MODE_MAXE "永久链接至目标")

enum aud_adc_intf_mode_t[](#_CPPv419aud_adc_intf_mode_t "永久链接至目标")
:   *Values:*

    enumerator AUD_ADC_INTF_MODE_DIFFEN[](#_CPPv4N19aud_adc_intf_mode_t24AUD_ADC_INTF_MODE_DIFFENE "永久链接至目标")

    enumerator AUD_ADC_INTF_MODE_SIGNAL_END[](#_CPPv4N19aud_adc_intf_mode_t28AUD_ADC_INTF_MODE_SIGNAL_ENDE "永久链接至目标")

    enumerator AUD_ADC_INTF_MODE_MAX[](#_CPPv4N19aud_adc_intf_mode_t21AUD_ADC_INTF_MODE_MAXE "永久链接至目标")

enum aud_adc_samp_rate_t[](#_CPPv419aud_adc_samp_rate_t "永久链接至目标")
:   *Values:*

    enumerator AUD_ADC_SAMP_RATE_8K[](#_CPPv4N19aud_adc_samp_rate_t20AUD_ADC_SAMP_RATE_8KE "永久链接至目标")
    :   ADC sample rate : 8k

    enumerator AUD_ADC_SAMP_RATE_11_025K[](#_CPPv4N19aud_adc_samp_rate_t25AUD_ADC_SAMP_RATE_11_025KE "永久链接至目标")
    :   ADC sample rate : 11.025k

    enumerator AUD_ADC_SAMP_RATE_12K[](#_CPPv4N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_12KE "永久链接至目标")
    :   ADC sample rate : 12k

    enumerator AUD_ADC_SAMP_RATE_16K[](#_CPPv4N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_16KE "永久链接至目标")
    :   ADC sample rate : 16k

    enumerator AUD_ADC_SAMP_RATE_22_05K[](#_CPPv4N19aud_adc_samp_rate_t24AUD_ADC_SAMP_RATE_22_05KE "永久链接至目标")
    :   ADC sample rate : 22.05k

    enumerator AUD_ADC_SAMP_RATE_24K[](#_CPPv4N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_24KE "永久链接至目标")
    :   ADC sample rate : 24k

    enumerator AUD_ADC_SAMP_RATE_32K[](#_CPPv4N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_32KE "永久链接至目标")
    :   ADC sample rate : 32k

    enumerator AUD_ADC_SAMP_RATE_44_1K[](#_CPPv4N19aud_adc_samp_rate_t23AUD_ADC_SAMP_RATE_44_1KE "永久链接至目标")
    :   ADC sample rate : 44.1k

    enumerator AUD_ADC_SAMP_RATE_48K[](#_CPPv4N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_48KE "永久链接至目标")
    :   ADC sample rate : 48k

    enumerator AUD_ADC_SAMP_RATE_MAX[](#_CPPv4N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_MAXE "永久链接至目标")

enum aud_adc_hpf_bypass_t[](#_CPPv420aud_adc_hpf_bypass_t "永久链接至目标")
:   *Values:*

    enumerator AUD_ADC_HPF_BYPASS_DISABLE[](#_CPPv4N20aud_adc_hpf_bypass_t26AUD_ADC_HPF_BYPASS_DISABLEE "永久链接至目标")
    :   AUD ADC hpf bypass disable

    enumerator AUD_ADC_HPF_BYPASS_ENABLE[](#_CPPv4N20aud_adc_hpf_bypass_t25AUD_ADC_HPF_BYPASS_ENABLEE "永久链接至目标")
    :   AUD ADC hpf bypass enable

    enumerator AUD_ADC_HPF_BYPASS_MAX[](#_CPPv4N20aud_adc_hpf_bypass_t22AUD_ADC_HPF_BYPASS_MAXE "永久链接至目标")

enum aud_adc_samp_edge_t[](#_CPPv419aud_adc_samp_edge_t "永久链接至目标")
:   *Values:*

    enumerator AUD_ADC_SAMP_EDGE_RISING[](#_CPPv4N19aud_adc_samp_edge_t24AUD_ADC_SAMP_EDGE_RISINGE "永久链接至目标")
    :   AUD ADC sampling clock edge : rising edge

    enumerator AUD_ADC_SAMP_EDGE_FALLING[](#_CPPv4N19aud_adc_samp_edge_t25AUD_ADC_SAMP_EDGE_FALLINGE "永久链接至目标")
    :   AUD ADC sampling clock edge : falling edge

    enumerator AUD_ADC_SAMP_EDGE_MAX[](#_CPPv4N19aud_adc_samp_edge_t21AUD_ADC_SAMP_EDGE_MAXE "永久链接至目标")

enum aud_adcl_int_t[](#_CPPv414aud_adcl_int_t "永久链接至目标")
:   *Values:*

    enumerator AUD_ADCL_INT_DISABLE[](#_CPPv4N14aud_adcl_int_t20AUD_ADCL_INT_DISABLEE "永久链接至目标")
    :   AUD ADCL interrupt disable

    enumerator AUD_ADCL_INT_ENABLE[](#_CPPv4N14aud_adcl_int_t19AUD_ADCL_INT_ENABLEE "永久链接至目标")
    :   AUD ADCL interrupt enable

    enumerator AUD_ADCL_INT_MAX[](#_CPPv4N14aud_adcl_int_t16AUD_ADCL_INT_MAXE "永久链接至目标")

enum aud_dtmf_int_t[](#_CPPv414aud_dtmf_int_t "永久链接至目标")
:   *Values:*

    enumerator AUD_DTMF_INT_DISABLE[](#_CPPv4N14aud_dtmf_int_t20AUD_DTMF_INT_DISABLEE "永久链接至目标")
    :   AUD DTMF interrupt disable

    enumerator AUD_DTMF_INT_ENABLE[](#_CPPv4N14aud_dtmf_int_t19AUD_DTMF_INT_ENABLEE "永久链接至目标")
    :   AUD DTMF interrupt enable

    enumerator AUD_DTMF_INT_MAX[](#_CPPv4N14aud_dtmf_int_t16AUD_DTMF_INT_MAXE "永久链接至目标")

enum aud_loop_adc2dac_t[](#_CPPv418aud_loop_adc2dac_t "永久链接至目标")
:   *Values:*

    enumerator AUD_LOOP_ADC2DAC_DISABLE[](#_CPPv4N18aud_loop_adc2dac_t24AUD_LOOP_ADC2DAC_DISABLEE "永久链接至目标")
    :   ADC to DAC loop test disable

    enumerator AUD_LOOP_ADC2DAC_ENABLE[](#_CPPv4N18aud_loop_adc2dac_t23AUD_LOOP_ADC2DAC_ENABLEE "永久链接至目标")
    :   ADC to DAC loop test enable

    enumerator AUD_LOOP_ADC2DAC_MAX[](#_CPPv4N18aud_loop_adc2dac_t20AUD_LOOP_ADC2DAC_MAXE "永久链接至目标")

enum aud_loop_dtmf2dac_t[](#_CPPv419aud_loop_dtmf2dac_t "永久链接至目标")
:   *Values:*

    enumerator AUD_LOOP_DTMF2DAC_DISABLE[](#_CPPv4N19aud_loop_dtmf2dac_t25AUD_LOOP_DTMF2DAC_DISABLEE "永久链接至目标")
    :   DTMF to DAC loop test disable

    enumerator AUD_LOOP_DTMF2DAC_ENABLE[](#_CPPv4N19aud_loop_dtmf2dac_t24AUD_LOOP_DTMF2DAC_ENABLEE "永久链接至目标")
    :   DTMF to DAC loop test enable

    enumerator AUD_LOOP_DTMF2DAC_MAX[](#_CPPv4N19aud_loop_dtmf2dac_t21AUD_LOOP_DTMF2DAC_MAXE "永久链接至目标")

enum aud_agc_ng_enable_t[](#_CPPv419aud_agc_ng_enable_t "永久链接至目标")
:   *Values:*

    enumerator AUD_AGC_NG_DISABLE[](#_CPPv4N19aud_agc_ng_enable_t18AUD_AGC_NG_DISABLEE "永久链接至目标")
    :   disable noise gating

    enumerator AUD_AGC_NG_ENABLE[](#_CPPv4N19aud_agc_ng_enable_t17AUD_AGC_NG_ENABLEE "永久链接至目标")
    :   enable noise gating

    enumerator AUD_AGC_NG_MAX[](#_CPPv4N19aud_agc_ng_enable_t14AUD_AGC_NG_MAXE "永久链接至目标")

enum aud_agc_method_t[](#_CPPv416aud_agc_method_t "永久链接至目标")
:   *Values:*

    enumerator AUD_AGC_NG_METHOD_MUTE[](#_CPPv4N16aud_agc_method_t22AUD_AGC_NG_METHOD_MUTEE "永久链接至目标")
    :   mute or demute : default

    enumerator AUD_AGC_NG_METHOD_CREASE[](#_CPPv4N16aud_agc_method_t24AUD_AGC_NG_METHOD_CREASEE "永久链接至目标")
    :   gradually increase or decrease gac

    enumerator AUD_AGC_NG_METHOD_MAX[](#_CPPv4N16aud_agc_method_t21AUD_AGC_NG_METHOD_MAXE "永久链接至目标")

enum aud_agc_decay_time_t[](#_CPPv420aud_agc_decay_time_t "永久链接至目标")
:   *Values:*

    enumerator AUD_AGC_DECAY_TIME_128[](#_CPPv4N20aud_agc_decay_time_t22AUD_AGC_DECAY_TIME_128E "永久链接至目标")
    :   AGC decay time :128 2.7ms

    enumerator AUD_AGC_DECAY_TIME_256[](#_CPPv4N20aud_agc_decay_time_t22AUD_AGC_DECAY_TIME_256E "永久链接至目标")
    :   AGC decay time :256

    enumerator AUD_AGC_DECAY_TIME_512[](#_CPPv4N20aud_agc_decay_time_t22AUD_AGC_DECAY_TIME_512E "永久链接至目标")
    :   AGC decay time :512

    enumerator AUD_AGC_DECAY_TIME_1024[](#_CPPv4N20aud_agc_decay_time_t23AUD_AGC_DECAY_TIME_1024E "永久链接至目标")
    :   AGC decay time :1024

    enumerator AUD_AGC_DECAY_TIME_2048[](#_CPPv4N20aud_agc_decay_time_t23AUD_AGC_DECAY_TIME_2048E "永久链接至目标")
    :   AGC decay time :2048

    enumerator AUD_AGC_DECAY_TIME_4096[](#_CPPv4N20aud_agc_decay_time_t23AUD_AGC_DECAY_TIME_4096E "永久链接至目标")
    :   AGC decay time :4096

    enumerator AUD_AGC_DECAY_TIME_8192[](#_CPPv4N20aud_agc_decay_time_t23AUD_AGC_DECAY_TIME_8192E "永久链接至目标")
    :   AGC decay time :8192

    enumerator AUD_AGC_DECAY_TIME_16384[](#_CPPv4N20aud_agc_decay_time_t24AUD_AGC_DECAY_TIME_16384E "永久链接至目标")
    :   AGC decay time :16384 340ms

    enumerator AUD_AGC_DECAY_TIME_MAX[](#_CPPv4N20aud_agc_decay_time_t22AUD_AGC_DECAY_TIME_MAXE "永久链接至目标")

enum aud_agc_attack_time_t[](#_CPPv421aud_agc_attack_time_t "永久链接至目标")
:   *Values:*

    enumerator AUD_AGC_ATTACK_TIME_8[](#_CPPv4N21aud_agc_attack_time_t21AUD_AGC_ATTACK_TIME_8E "永久链接至目标")
    :   AGC attack time :8 0.1667ms

    enumerator AUD_AGC_ATTACK_TIME_16[](#_CPPv4N21aud_agc_attack_time_t22AUD_AGC_ATTACK_TIME_16E "永久链接至目标")
    :   AGC attack time :16

    enumerator AUD_AGC_ATTACK_TIME_32[](#_CPPv4N21aud_agc_attack_time_t22AUD_AGC_ATTACK_TIME_32E "永久链接至目标")
    :   AGC attack time :32

    enumerator AUD_AGC_ATTACK_TIME_64[](#_CPPv4N21aud_agc_attack_time_t22AUD_AGC_ATTACK_TIME_64E "永久链接至目标")
    :   AGC attack time :64

    enumerator AUD_AGC_ATTACK_TIME_128[](#_CPPv4N21aud_agc_attack_time_t23AUD_AGC_ATTACK_TIME_128E "永久链接至目标")
    :   AGC attack time :128

    enumerator AUD_AGC_ATTACK_TIME_256[](#_CPPv4N21aud_agc_attack_time_t23AUD_AGC_ATTACK_TIME_256E "永久链接至目标")
    :   AGC attack time :256

    enumerator AUD_AGC_ATTACK_TIME_512[](#_CPPv4N21aud_agc_attack_time_t23AUD_AGC_ATTACK_TIME_512E "永久链接至目标")
    :   AGC attack time :512

    enumerator AUD_AGC_ATTACK_TIME_1024[](#_CPPv4N21aud_agc_attack_time_t24AUD_AGC_ATTACK_TIME_1024E "永久链接至目标")
    :   AGC attack time :1024 21 ms

    enumerator AUD_AGC_ATTACK_TIME_MAX[](#_CPPv4N21aud_agc_attack_time_t23AUD_AGC_ATTACK_TIME_MAXE "永久链接至目标")

enum aud_agc_iir_coef_t[](#_CPPv418aud_agc_iir_coef_t "永久链接至目标")
:   *Values:*

    enumerator AUD_AGC_IIR_COEF_1_32[](#_CPPv4N18aud_agc_iir_coef_t21AUD_AGC_IIR_COEF_1_32E "永久链接至目标")
    :   AGC IRR coefficient : 1/32

    enumerator AUD_AGC_IIR_COEF_1_64[](#_CPPv4N18aud_agc_iir_coef_t21AUD_AGC_IIR_COEF_1_64E "永久链接至目标")
    :   AGC IRR coefficient : 1/64

    enumerator AUD_AGC_IIR_COEF_1_128[](#_CPPv4N18aud_agc_iir_coef_t22AUD_AGC_IIR_COEF_1_128E "永久链接至目标")
    :   AGC IRR coefficient : 1/128

    enumerator AUD_AGC_IIR_COEF_1_256[](#_CPPv4N18aud_agc_iir_coef_t22AUD_AGC_IIR_COEF_1_256E "永久链接至目标")
    :   AGC IRR coefficient : 1/256

    enumerator AUD_AGC_IIR_COEF_1_512[](#_CPPv4N18aud_agc_iir_coef_t22AUD_AGC_IIR_COEF_1_512E "永久链接至目标")
    :   AGC IRR coefficient : 1/512

    enumerator AUD_AGC_IIR_COEF_1_1024[](#_CPPv4N18aud_agc_iir_coef_t23AUD_AGC_IIR_COEF_1_1024E "永久链接至目标")
    :   AGC IRR coefficient : 1/1024

    enumerator AUD_AGC_IIR_COEF_1_2048[](#_CPPv4N18aud_agc_iir_coef_t23AUD_AGC_IIR_COEF_1_2048E "永久链接至目标")
    :   AGC IRR coefficient : 1/2048

    enumerator AUD_AGC_IIR_COEF_1_4096[](#_CPPv4N18aud_agc_iir_coef_t23AUD_AGC_IIR_COEF_1_4096E "永久链接至目标")
    :   AGC IRR coefficient : 1/4096

    enumerator AUD_AGC_IIR_COEF_MAX[](#_CPPv4N18aud_agc_iir_coef_t20AUD_AGC_IIR_COEF_MAXE "永久链接至目标")

enum aud_agc_enable_t[](#_CPPv416aud_agc_enable_t "永久链接至目标")
:   *Values:*

    enumerator AUD_AGC_DISABLE[](#_CPPv4N16aud_agc_enable_t15AUD_AGC_DISABLEE "永久链接至目标")
    :   disable AGC

    enumerator AUD_AGC_ENABLE[](#_CPPv4N16aud_agc_enable_t14AUD_AGC_ENABLEE "永久链接至目标")
    :   enable AGC

    enumerator AUD_AGC_MAX[](#_CPPv4N16aud_agc_enable_t11AUD_AGC_MAXE "永久链接至目标")

enum aud_agc_manual_pga_en_t[](#_CPPv423aud_agc_manual_pga_en_t "永久链接至目标")
:   *Values:*

    enumerator AUD_GAC_MANUAL_PGA_DISABLE[](#_CPPv4N23aud_agc_manual_pga_en_t26AUD_GAC_MANUAL_PGA_DISABLEE "永久链接至目标")
    :   disable AGC manual set pga

    enumerator AUD_GAC_MANUAL_PGA_ENABLE[](#_CPPv4N23aud_agc_manual_pga_en_t25AUD_GAC_MANUAL_PGA_ENABLEE "永久链接至目标")
    :   enable AGC manual set pga

    enumerator AUD_GAC_MANUAL_PGA_MAX[](#_CPPv4N23aud_agc_manual_pga_en_t22AUD_GAC_MANUAL_PGA_MAXE "永久链接至目标")

enum aud_adc_enable_t[](#_CPPv416aud_adc_enable_t "永久链接至目标")
:   *Values:*

    enumerator AUD_ADC_DISABLE[](#_CPPv4N16aud_adc_enable_t15AUD_ADC_DISABLEE "永久链接至目标")
    :   disable adc

    enumerator AUD_ADC_ENABLE[](#_CPPv4N16aud_adc_enable_t14AUD_ADC_ENABLEE "永久链接至目标")
    :   enable adc

    enumerator AUD_ADC_ENABLE_MAX[](#_CPPv4N16aud_adc_enable_t18AUD_ADC_ENABLE_MAXE "永久链接至目标")

enum aud_adc_line_enable_t[](#_CPPv421aud_adc_line_enable_t "永久链接至目标")
:   *Values:*

    enumerator AUD_ADC_LINE_DISABLE[](#_CPPv4N21aud_adc_line_enable_t20AUD_ADC_LINE_DISABLEE "永久链接至目标")
    :   disable line in

    enumerator AUD_ADC_LINE_ENABLE[](#_CPPv4N21aud_adc_line_enable_t19AUD_ADC_LINE_ENABLEE "永久链接至目标")
    :   enable line in

    enumerator AUD_ADC_LINE_ENABLE_MAX[](#_CPPv4N21aud_adc_line_enable_t23AUD_ADC_LINE_ENABLE_MAXE "永久链接至目标")

enum aud_mic_enable_t[](#_CPPv416aud_mic_enable_t "永久链接至目标")
:   *Values:*

    enumerator AUD_MIC_DISABLE[](#_CPPv4N16aud_mic_enable_t15AUD_MIC_DISABLEE "永久链接至目标")
    :   disable all mic

    enumerator AUD_MIC_MIC1_ENABLE[](#_CPPv4N16aud_mic_enable_t19AUD_MIC_MIC1_ENABLEE "永久链接至目标")
    :   enable mic1

    enumerator AUD_MIC_MIC2_ENABLE[](#_CPPv4N16aud_mic_enable_t19AUD_MIC_MIC2_ENABLEE "永久链接至目标")
    :   enable mic2

    enumerator AUD_MIC_ALL_ENABLE[](#_CPPv4N16aud_mic_enable_t18AUD_MIC_ALL_ENABLEE "永久链接至目标")
    :   enable all mic

    enumerator AUD_MIC_MAX[](#_CPPv4N16aud_mic_enable_t11AUD_MIC_MAXE "永久链接至目标")

enum aud_mic_id_t[](#_CPPv412aud_mic_id_t "永久链接至目标")
:   *Values:*

    enumerator AUD_MIC_MIC1[](#_CPPv4N12aud_mic_id_t12AUD_MIC_MIC1E "永久链接至目标")
    :   enable mic1

    enumerator AUD_MIC_MIC2[](#_CPPv4N12aud_mic_id_t12AUD_MIC_MIC2E "永久链接至目标")
    :   enable mic2

    enumerator AUD_MIC_BOTH[](#_CPPv4N12aud_mic_id_t12AUD_MIC_BOTHE "永久链接至目标")
    :   enable mic1 and mic2

enum aud_gac_noise_tout_t[](#_CPPv420aud_gac_noise_tout_t "永久链接至目标")
:   *Values:*

    enumerator AUD_GAC_NOISE_TOUT_0[](#_CPPv4N20aud_gac_noise_tout_t20AUD_GAC_NOISE_TOUT_0E "永久链接至目标")
    :   AGC noise tout: 0 0ms

    enumerator AUD_GAC_NOISE_TOUT_4[](#_CPPv4N20aud_gac_noise_tout_t20AUD_GAC_NOISE_TOUT_4E "永久链接至目标")
    :   AGC noise tout: 4 0.5ms

    enumerator AUD_GAC_NOISE_TOUT_8[](#_CPPv4N20aud_gac_noise_tout_t20AUD_GAC_NOISE_TOUT_8E "永久链接至目标")
    :   AGC noise tout: 8

    enumerator AUD_GAC_NOISE_TOUT_16[](#_CPPv4N20aud_gac_noise_tout_t21AUD_GAC_NOISE_TOUT_16E "永久链接至目标")
    :   AGC noise tout: 16

    enumerator AUD_GAC_NOISE_TOUT_32[](#_CPPv4N20aud_gac_noise_tout_t21AUD_GAC_NOISE_TOUT_32E "永久链接至目标")
    :   AGC noise tout: 32

    enumerator AUD_GAC_NOISE_TOUT_64[](#_CPPv4N20aud_gac_noise_tout_t21AUD_GAC_NOISE_TOUT_64E "永久链接至目标")
    :   AGC noise tout: 64

    enumerator AUD_GAC_NOISE_TOUT_128[](#_CPPv4N20aud_gac_noise_tout_t22AUD_GAC_NOISE_TOUT_128E "永久链接至目标")
    :   AGC noise tout: 128

    enumerator AUD_GAC_NOISE_TOUT_256[](#_CPPv4N20aud_gac_noise_tout_t22AUD_GAC_NOISE_TOUT_256E "永久链接至目标")
    :   AGC noise tout: 256 32ms

    enumerator AUD_GAC_NOISE_TOUT_MAX[](#_CPPv4N20aud_gac_noise_tout_t22AUD_GAC_NOISE_TOUT_MAXE "永久链接至目标")

enum aud_gac_high_dur_t[](#_CPPv418aud_gac_high_dur_t "永久链接至目标")
:   *Values:*

    enumerator AUD_GAC_HIGH_DUR_0[](#_CPPv4N18aud_gac_high_dur_t18AUD_GAC_HIGH_DUR_0E "永久链接至目标")
    :   AGC 0 ms，as soon as MIC_RSSI value higher than NOISE_HIGH，Noise gating work，leave off noise status

    enumerator AUD_GAC_HIGH_DUR_4[](#_CPPv4N18aud_gac_high_dur_t18AUD_GAC_HIGH_DUR_4E "永久链接至目标")
    :   AGC high duration: 4 0.5ms

    enumerator AUD_GAC_HIGH_DUR_8[](#_CPPv4N18aud_gac_high_dur_t18AUD_GAC_HIGH_DUR_8E "永久链接至目标")
    :   AGC high duration: 8

    enumerator AUD_GAC_HIGH_DUR_16[](#_CPPv4N18aud_gac_high_dur_t19AUD_GAC_HIGH_DUR_16E "永久链接至目标")
    :   AGC high duration: 16

    enumerator AUD_GAC_HIGH_DUR_32[](#_CPPv4N18aud_gac_high_dur_t19AUD_GAC_HIGH_DUR_32E "永久链接至目标")
    :   AGC high duration: 32

    enumerator AUD_GAC_HIGH_DUR_64[](#_CPPv4N18aud_gac_high_dur_t19AUD_GAC_HIGH_DUR_64E "永久链接至目标")
    :   AGC high duration: 64

    enumerator AUD_GAC_HIGH_DUR_128[](#_CPPv4N18aud_gac_high_dur_t20AUD_GAC_HIGH_DUR_128E "永久链接至目标")
    :   AGC high duration: 128

    enumerator AUD_GAC_HIGH_DUR_256[](#_CPPv4N18aud_gac_high_dur_t20AUD_GAC_HIGH_DUR_256E "永久链接至目标")
    :   AGC high duration: 256 32ms

    enumerator AUD_GAC_HIGH_DUR_MAX[](#_CPPv4N18aud_gac_high_dur_t20AUD_GAC_HIGH_DUR_MAXE "永久链接至目标")

enum aud_gac_low_dur_t[](#_CPPv417aud_gac_low_dur_t "永久链接至目标")
:   *Values:*

    enumerator AUD_GAC_LOW_DUR_0[](#_CPPv4N17aud_gac_low_dur_t17AUD_GAC_LOW_DUR_0E "永久链接至目标")
    :   AGC 0 ms，as soon as MIC_RSSI value lower than NOISE_HIGH，Noise gating work，leave off noise status

    enumerator AUD_GAC_LOW_DUR_4[](#_CPPv4N17aud_gac_low_dur_t17AUD_GAC_LOW_DUR_4E "永久链接至目标")
    :   AGC low duration: 4 0.5ms

    enumerator AUD_GAC_LOW_DUR_8[](#_CPPv4N17aud_gac_low_dur_t17AUD_GAC_LOW_DUR_8E "永久链接至目标")
    :   AGC low duration: 8

    enumerator AUD_GAC_LOW_DUR_16[](#_CPPv4N17aud_gac_low_dur_t18AUD_GAC_LOW_DUR_16E "永久链接至目标")
    :   AGC low duration: 16

    enumerator AUD_GAC_LOW_DUR_32[](#_CPPv4N17aud_gac_low_dur_t18AUD_GAC_LOW_DUR_32E "永久链接至目标")
    :   AGC low duration: 32

    enumerator AUD_GAC_LOW_DUR_64[](#_CPPv4N17aud_gac_low_dur_t18AUD_GAC_LOW_DUR_64E "永久链接至目标")
    :   AGC low duration: 64

    enumerator AUD_GAC_LOW_DUR_128[](#_CPPv4N17aud_gac_low_dur_t19AUD_GAC_LOW_DUR_128E "永久链接至目标")
    :   AGC low duration: 128

    enumerator AUD_GAC_LOW_DUR_256[](#_CPPv4N17aud_gac_low_dur_t19AUD_GAC_LOW_DUR_256E "永久链接至目标")
    :   AGC low duration: 256 32ms

    enumerator AUD_GAC_LOW_DUR_MAX[](#_CPPv4N17aud_gac_low_dur_t19AUD_GAC_LOW_DUR_MAXE "永久链接至目标")

enum aud_dtmf_enable_t[](#_CPPv417aud_dtmf_enable_t "永久链接至目标")
:   *Values:*

    enumerator AUD_DTMF_DISABLE[](#_CPPv4N17aud_dtmf_enable_t16AUD_DTMF_DISABLEE "永久链接至目标")
    :   disable dtmf

    enumerator AUD_DTMF_ENABLE[](#_CPPv4N17aud_dtmf_enable_t15AUD_DTMF_ENABLEE "永久链接至目标")
    :   enable dtmf

    enumerator AUD_DTMF_ENABLE_MAX[](#_CPPv4N17aud_dtmf_enable_t19AUD_DTMF_ENABLE_MAXE "永久链接至目标")

enum aud_dtmf_tone_pattern_t[](#_CPPv423aud_dtmf_tone_pattern_t "永久链接至目标")
:   *Values:*

    enumerator AUD_DTMF_TONE_PATTERN_DTMF[](#_CPPv4N23aud_dtmf_tone_pattern_t26AUD_DTMF_TONE_PATTERN_DTMFE "永久链接至目标")
    :   0: DTMF(Active_Time) + Zeros(Pause_Time)

    enumerator AUD_DTMF_TONE_PATTERN_TONE[](#_CPPv4N23aud_dtmf_tone_pattern_t26AUD_DTMF_TONE_PATTERN_TONEE "永久链接至目标")
    :   1：Tone1(Active_Time) + Tone2(Pause_Time)

    enumerator AUD_DTMF_TONE_PATTERN_MAX[](#_CPPv4N23aud_dtmf_tone_pattern_t25AUD_DTMF_TONE_PATTERN_MAXE "永久链接至目标")

enum aud_dtmf_tone_mode_t[](#_CPPv420aud_dtmf_tone_mode_t "永久链接至目标")
:   *Values:*

    enumerator AUD_DTMF_TONE_MODE_SIGNAL[](#_CPPv4N20aud_dtmf_tone_mode_t25AUD_DTMF_TONE_MODE_SIGNALE "永久链接至目标")
    :   0：signal mode

    enumerator AUD_DTMF_TONE_MODE_CONTIUS[](#_CPPv4N20aud_dtmf_tone_mode_t26AUD_DTMF_TONE_MODE_CONTIUSE "永久链接至目标")
    :   1：continuous mode

    enumerator AUD_DTMF_TONE_MODE_MAX[](#_CPPv4N20aud_dtmf_tone_mode_t22AUD_DTMF_TONE_MODE_MAXE "永久链接至目标")

enum aud_dtmf_tone_attu_t[](#_CPPv420aud_dtmf_tone_attu_t "永久链接至目标")
:   *Values:*

    enumerator AUD_DTMF_TONE_ATTU_MINUS_1[](#_CPPv4N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_1E "永久链接至目标")
    :   Tone1 damp set: -1 db

    enumerator AUD_DTMF_TONE_ATTU_MINUS_2[](#_CPPv4N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_2E "永久链接至目标")
    :   Tone1 damp set: -2 db

    enumerator AUD_DTMF_TONE_ATTU_MINUS_3[](#_CPPv4N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_3E "永久链接至目标")
    :   Tone1 damp set: -3 db

    enumerator AUD_DTMF_TONE_ATTU_MINUS_4[](#_CPPv4N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_4E "永久链接至目标")
    :   Tone1 damp set: -4 db

    enumerator AUD_DTMF_TONE_ATTU_MINUS_5[](#_CPPv4N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_5E "永久链接至目标")
    :   Tone1 damp set: -5 db

    enumerator AUD_DTMF_TONE_ATTU_MINUS_6[](#_CPPv4N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_6E "永久链接至目标")
    :   Tone1 damp set: -6 db

    enumerator AUD_DTMF_TONE_ATTU_MINUS_7[](#_CPPv4N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_7E "永久链接至目标")
    :   Tone1 damp set: -7 db

    enumerator AUD_DTMF_TONE_ATTU_MINUS_8[](#_CPPv4N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_8E "永久链接至目标")
    :   Tone1 damp set: -8 db

    enumerator AUD_DTMF_TONE_ATTU_MINUS_9[](#_CPPv4N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_9E "永久链接至目标")
    :   Tone1 damp set: -9 db

    enumerator AUD_DTMF_TONE_ATTU_MINUS_10[](#_CPPv4N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_10E "永久链接至目标")
    :   Tone1 damp set: -10 db

    enumerator AUD_DTMF_TONE_ATTU_MINUS_11[](#_CPPv4N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_11E "永久链接至目标")
    :   Tone1 damp set: -11 db

    enumerator AUD_DTMF_TONE_ATTU_MINUS_12[](#_CPPv4N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_12E "永久链接至目标")
    :   Tone1 damp set: -12 db

    enumerator AUD_DTMF_TONE_ATTU_MINUS_13[](#_CPPv4N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_13E "永久链接至目标")
    :   Tone1 damp set: -13 db

    enumerator AUD_DTMF_TONE_ATTU_MINUS_14[](#_CPPv4N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_14E "永久链接至目标")
    :   Tone1 damp set: -14 db

    enumerator AUD_DTMF_TONE_ATTU_MINUS_15[](#_CPPv4N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_15E "永久链接至目标")
    :   Tone1 damp set: -15 db

    enumerator AUD_DTMF_TONE_ATTU_MINUS_MAX[](#_CPPv4N20aud_dtmf_tone_attu_t28AUD_DTMF_TONE_ATTU_MINUS_MAXE "永久链接至目标")

enum aud_dtmf_tone_enable_t[](#_CPPv422aud_dtmf_tone_enable_t "永久链接至目标")
:   *Values:*

    enumerator AUD_DTMF_TONE_DISABLE[](#_CPPv4N22aud_dtmf_tone_enable_t21AUD_DTMF_TONE_DISABLEE "永久链接至目标")
    :   0：disable tone

    enumerator AUD_DTMF_TONE_ENABLE[](#_CPPv4N22aud_dtmf_tone_enable_t20AUD_DTMF_TONE_ENABLEE "永久链接至目标")
    :   1：enable tone

    enumerator AUD_DTMF_TONE_ENABLE_MAX[](#_CPPv4N22aud_dtmf_tone_enable_t24AUD_DTMF_TONE_ENABLE_MAXE "永久链接至目标")

enum aud_adc_fracmod_manual_en_t[](#_CPPv427aud_adc_fracmod_manual_en_t "永久链接至目标")
:   *Values:*

    enumerator AUD_ADC_TRACMOD_MANUAL_DISABLE[](#_CPPv4N27aud_adc_fracmod_manual_en_t30AUD_ADC_TRACMOD_MANUAL_DISABLEE "永久链接至目标")
    :   0：disable ADC fractional frequency division of manual set

    enumerator AUD_ADC_TRACMOD_MANUAL_ENABLE[](#_CPPv4N27aud_adc_fracmod_manual_en_t29AUD_ADC_TRACMOD_MANUAL_ENABLEE "永久链接至目标")
    :   1：enable ADC fractional frequency division of manual set

    enumerator AUD_ADC_TRACMOD_MANUAL_EN_MAX[](#_CPPv4N27aud_adc_fracmod_manual_en_t29AUD_ADC_TRACMOD_MANUAL_EN_MAXE "永久链接至目标")

enum aud_dac_enable_t[](#_CPPv416aud_dac_enable_t "永久链接至目标")
:   dac enum


    *Values:*

    enumerator AUD_DAC_DISABLE[](#_CPPv4N16aud_dac_enable_t15AUD_DAC_DISABLEE "永久链接至目标")
    :   0：disable dac

    enumerator AUD_DAC_ENABLE[](#_CPPv4N16aud_dac_enable_t14AUD_DAC_ENABLEE "永久链接至目标")
    :   1：enable dac

    enumerator AUD_DAC_OTHERS[](#_CPPv4N16aud_dac_enable_t14AUD_DAC_OTHERSE "永久链接至目标")

enum aud_dac_chl_enable_t[](#_CPPv420aud_dac_chl_enable_t "永久链接至目标")
:   *Values:*

    enumerator AUD_DAC_CHL_DISABLE[](#_CPPv4N20aud_dac_chl_enable_t19AUD_DAC_CHL_DISABLEE "永久链接至目标")
    :   disable all dac channel

    enumerator AUD_DAC_CHL_L_ENABLE[](#_CPPv4N20aud_dac_chl_enable_t20AUD_DAC_CHL_L_ENABLEE "永久链接至目标")
    :   enable dac left channel

    enumerator AUD_DAC_CHL_R_ENABLE[](#_CPPv4N20aud_dac_chl_enable_t20AUD_DAC_CHL_R_ENABLEE "永久链接至目标")
    :   enable dac right channel

    enumerator AUD_DAC_CHL_LR_ENABLE[](#_CPPv4N20aud_dac_chl_enable_t21AUD_DAC_CHL_LR_ENABLEE "永久链接至目标")
    :   enable dac left and right channel

    enumerator AUD_DAC_CHL_MAX[](#_CPPv4N20aud_dac_chl_enable_t15AUD_DAC_CHL_MAXE "永久链接至目标")

enum aud_dac_work_mode_t[](#_CPPv419aud_dac_work_mode_t "永久链接至目标")
:   *Values:*

    enumerator AUD_DAC_WORK_MODE_SIGNAL_END[](#_CPPv4N19aud_dac_work_mode_t28AUD_DAC_WORK_MODE_SIGNAL_ENDE "永久链接至目标")

    enumerator AUD_DAC_WORK_MODE_DIFFEN[](#_CPPv4N19aud_dac_work_mode_t24AUD_DAC_WORK_MODE_DIFFENE "永久链接至目标")

    enumerator AUD_DAC_WORK_MODE_MAX[](#_CPPv4N19aud_dac_work_mode_t21AUD_DAC_WORK_MODE_MAXE "永久链接至目标")

enum aud_dac_samp_rate_t[](#_CPPv419aud_dac_samp_rate_t "永久链接至目标")
:   *Values:*

    enumerator AUD_DAC_SAMP_RATE_8K[](#_CPPv4N19aud_dac_samp_rate_t20AUD_DAC_SAMP_RATE_8KE "永久链接至目标")
    :   DAC sample rate : 8k

    enumerator AUD_DAC_SAMP_RATE_11_025K[](#_CPPv4N19aud_dac_samp_rate_t25AUD_DAC_SAMP_RATE_11_025KE "永久链接至目标")
    :   DAC sample rate : 11.025k

    enumerator AUD_DAC_SAMP_RATE_12K[](#_CPPv4N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_12KE "永久链接至目标")
    :   DAC sample rate : 12k

    enumerator AUD_DAC_SAMP_RATE_16K[](#_CPPv4N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_16KE "永久链接至目标")
    :   DAC sample rate : 16k

    enumerator AUD_DAC_SAMP_RATE_22_05K[](#_CPPv4N19aud_dac_samp_rate_t24AUD_DAC_SAMP_RATE_22_05KE "永久链接至目标")
    :   DAC sample rate : 22.05k

    enumerator AUD_DAC_SAMP_RATE_24K[](#_CPPv4N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_24KE "永久链接至目标")
    :   DAC sample rate : 24k

    enumerator AUD_DAC_SAMP_RATE_32K[](#_CPPv4N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_32KE "永久链接至目标")
    :   DAC sample rate : 32k

    enumerator AUD_DAC_SAMP_RATE_44_1K[](#_CPPv4N19aud_dac_samp_rate_t23AUD_DAC_SAMP_RATE_44_1KE "永久链接至目标")
    :   DAC sample rate : 44.1k

    enumerator AUD_DAC_SAMP_RATE_48K[](#_CPPv4N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_48KE "永久链接至目标")
    :   DAC sample rate : 48k

    enumerator AUD_DAC_SAMP_RATE_MAX[](#_CPPv4N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_MAXE "永久链接至目标")

enum aud_dac_hpf_bypass_t[](#_CPPv420aud_dac_hpf_bypass_t "永久链接至目标")
:   *Values:*

    enumerator AUD_DAC_HPF_BYPASS_DISABLE[](#_CPPv4N20aud_dac_hpf_bypass_t26AUD_DAC_HPF_BYPASS_DISABLEE "永久链接至目标")
    :   AUD DAC hpf bypass disable

    enumerator AUD_DAC_HPF_BYPASS_ENABLE[](#_CPPv4N20aud_dac_hpf_bypass_t25AUD_DAC_HPF_BYPASS_ENABLEE "永久链接至目标")
    :   AUD DAC hpf bypass enable

    enumerator AUD_DAC_HPF_BYPASS_OTHERS[](#_CPPv4N20aud_dac_hpf_bypass_t25AUD_DAC_HPF_BYPASS_OTHERSE "永久链接至目标")

enum aud_dac_clk_invert_t[](#_CPPv420aud_dac_clk_invert_t "永久链接至目标")
:   *Values:*

    enumerator AUD_DAC_CLK_INVERT_RISING[](#_CPPv4N20aud_dac_clk_invert_t25AUD_DAC_CLK_INVERT_RISINGE "永久链接至目标")
    :   AUD dac output clock edge rising

    enumerator AUD_DAC_CLK_INVERT_FALLING[](#_CPPv4N20aud_dac_clk_invert_t26AUD_DAC_CLK_INVERT_FALLINGE "永久链接至目标")
    :   AUD dac output clock edge falling

    enumerator AUD_DAC_CLK_INVERT_OTHERS[](#_CPPv4N20aud_dac_clk_invert_t25AUD_DAC_CLK_INVERT_OTHERSE "永久链接至目标")

enum aud_dac_int_enable_t[](#_CPPv420aud_dac_int_enable_t "永久链接至目标")
:   *Values:*

    enumerator AUD_DACR_INT_DISABLE[](#_CPPv4N20aud_dac_int_enable_t20AUD_DACR_INT_DISABLEE "永久链接至目标")
    :   AUD dac right channel interrupt disable

    enumerator AUD_DACR_INT_ENABLE[](#_CPPv4N20aud_dac_int_enable_t19AUD_DACR_INT_ENABLEE "永久链接至目标")
    :   AUD dac right channel interrupt enable

    enumerator AUD_DACL_INT_DISABLE[](#_CPPv4N20aud_dac_int_enable_t20AUD_DACL_INT_DISABLEE "永久链接至目标")
    :   AUD dac left channel interrupt disable

    enumerator AUD_DACL_INT_ENABLE[](#_CPPv4N20aud_dac_int_enable_t19AUD_DACL_INT_ENABLEE "永久链接至目标")
    :   AUD dac left channel interrupt enable

    enumerator AUD_DAC_INT_OTHERS[](#_CPPv4N20aud_dac_int_enable_t18AUD_DAC_INT_OTHERSE "永久链接至目标")

enum aud_dac_filt_enable_t[](#_CPPv421aud_dac_filt_enable_t "永久链接至目标")
:   *Values:*

    enumerator AUD_DAC_FILT_DISABLE[](#_CPPv4N21aud_dac_filt_enable_t20AUD_DAC_FILT_DISABLEE "永久链接至目标")
    :   AUD dac filter disable

    enumerator AUD_DAC_FILT_ENABLE[](#_CPPv4N21aud_dac_filt_enable_t19AUD_DAC_FILT_ENABLEE "永久链接至目标")
    :   AUD dac filter enable

    enumerator AUD_DAC_FILT_OTHERS[](#_CPPv4N21aud_dac_filt_enable_t19AUD_DAC_FILT_OTHERSE "永久链接至目标")

enum aud_dac_fracmod_manual_t[](#_CPPv424aud_dac_fracmod_manual_t "永久链接至目标")
:   *Values:*

    enumerator AUD_DAC_FRACMOD_MANUAL_DISABLE[](#_CPPv4N24aud_dac_fracmod_manual_t30AUD_DAC_FRACMOD_MANUAL_DISABLEE "永久链接至目标")
    :   disable dac fractional frequency division of manual set

    enumerator AUD_DAC_FRACMOD_MANUAL_ENABLE[](#_CPPv4N24aud_dac_fracmod_manual_t29AUD_DAC_FRACMOD_MANUAL_ENABLEE "永久链接至目标")
    :   enable ADC fractional frequency division of manual set

    enumerator ADU_DAC_FRACMOD_MANUAL_OTHERS[](#_CPPv4N24aud_dac_fracmod_manual_t29ADU_DAC_FRACMOD_MANUAL_OTHERSE "永久链接至目标")

enum aud_adc_status_mask_t[](#_CPPv421aud_adc_status_mask_t "永久链接至目标")
:   *Values:*

    enumerator AUD_ADCL_NEAR_FULL_MASK[](#_CPPv4N21aud_adc_status_mask_t23AUD_ADCL_NEAR_FULL_MASKE "永久链接至目标")
    :   AUD ADC left channel FIFO near full

    enumerator AUD_DTMF_NEAR_FULL_MASK[](#_CPPv4N21aud_adc_status_mask_t23AUD_DTMF_NEAR_FULL_MASKE "永久链接至目标")
    :   AUD DTMF FIFO near full

    enumerator AUD_ADCL_NEAR_EMPTY_MASK[](#_CPPv4N21aud_adc_status_mask_t24AUD_ADCL_NEAR_EMPTY_MASKE "永久链接至目标")
    :   AUD ADC left channel FIFO near empty

    enumerator AUD_DTMF_NEAR_EMPTY_MASK[](#_CPPv4N21aud_adc_status_mask_t24AUD_DTMF_NEAR_EMPTY_MASKE "永久链接至目标")
    :   AUD DTMF FIFO near empty

    enumerator AUD_ADCL_FIFO_FULL_MASK[](#_CPPv4N21aud_adc_status_mask_t23AUD_ADCL_FIFO_FULL_MASKE "永久链接至目标")
    :   AUD ADC left channel FIFO full

    enumerator AUD_DTMF_FIFO_FULL_MASK[](#_CPPv4N21aud_adc_status_mask_t23AUD_DTMF_FIFO_FULL_MASKE "永久链接至目标")
    :   AUD DTMF FIFO full

    enumerator AUD_ADCL_FIFO_EMPTY_MASK[](#_CPPv4N21aud_adc_status_mask_t24AUD_ADCL_FIFO_EMPTY_MASKE "永久链接至目标")
    :   AUD ADC left channel FIFO empty

    enumerator AUD_DTMF_FIFO_EMPTY_MASK[](#_CPPv4N21aud_adc_status_mask_t24AUD_DTMF_FIFO_EMPTY_MASKE "永久链接至目标")
    :   AUD DTMF FIFO empty

enum aud_dac_status_mask_t[](#_CPPv421aud_dac_status_mask_t "永久链接至目标")
:   *Values:*

    enumerator AUD_DACR_NEAR_FULL_MASK[](#_CPPv4N21aud_dac_status_mask_t23AUD_DACR_NEAR_FULL_MASKE "永久链接至目标")
    :   AUD DAC right channel fifo near full

    enumerator AUD_DACL_NEAR_FULL_MASK[](#_CPPv4N21aud_dac_status_mask_t23AUD_DACL_NEAR_FULL_MASKE "永久链接至目标")
    :   AUD DAC left channel fifo near full

    enumerator AUD_DACR_NEAR_EMPTY_MASK[](#_CPPv4N21aud_dac_status_mask_t24AUD_DACR_NEAR_EMPTY_MASKE "永久链接至目标")
    :   AUD DAC right channel fifo near empty

    enumerator AUD_DACL_NEAR_EMPTY_MASK[](#_CPPv4N21aud_dac_status_mask_t24AUD_DACL_NEAR_EMPTY_MASKE "永久链接至目标")
    :   AUD DAC left channel fifo near empty

    enumerator AUD_DACR_FIFO_FULL_MASK[](#_CPPv4N21aud_dac_status_mask_t23AUD_DACR_FIFO_FULL_MASKE "永久链接至目标")
    :   AUD DAC right channel fifo full

    enumerator AUD_DACL_FIFO_FULL_MASK[](#_CPPv4N21aud_dac_status_mask_t23AUD_DACL_FIFO_FULL_MASKE "永久链接至目标")
    :   AUD DAC left channel fifo full

    enumerator AUD_DACR_FIFO_EMPTY_MASK[](#_CPPv4N21aud_dac_status_mask_t24AUD_DACR_FIFO_EMPTY_MASKE "永久链接至目标")
    :   AUD DAC right channel fifo empty

    enumerator AUD_DACL_FIFO_EMPTY_MASK[](#_CPPv4N21aud_dac_status_mask_t24AUD_DACL_FIFO_EMPTY_MASKE "永久链接至目标")
    :   AUD DAC left channel fifo empty
