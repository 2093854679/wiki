---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/api-reference/multi_media/bk_audio.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="audio-apis"></a>

# Audio APIs

重要

The Audio API v1.0 is the lastest and stable Audio APIs. All new applications should use Audio API v1.0.

<a id="audio-interface"></a>

## Audio Interface

The BK Audio Driver supports following functions:

> - adc function
> - dac function
> - eq function

The adc and dac function can be operated independently. However the eq function need to use with dac function together.

<a id="audio-api-categories"></a>

## Audio API Categories

Most of Audio APIs can be categoried as:

> - Common APIs
>
>   The common APIs are prefixed with bk\_aud, the APIs may be common for adc and dac interfaces, e.g. bk\_aud\_driver\_init() etc.
> - Adc function APIs.
>
>   The APIs provide support for adc function. e.g. bk\_aud\_adc\_init() etc.
> - Dac function APIs.
>
>   The APIs provide support for dac function. e.g. bk\_aud\_dac\_init() etc.
> - Eq function APIs.
>
>   The APIs provide support for eq function. e.g. bk\_aud\_eq\_init() etc.

Common APIs:
:   - [`bk_aud_driver_init()`](#_CPPv418bk_aud_driver_initv "bk_aud_driver_init") \- init the audio driver
    - [`bk_aud_driver_deinit()`](#_CPPv420bk_aud_driver_deinitv "bk_aud_driver_deinit") \- deinit the audio driver
    - [`bk_aud_register_aud_isr()`](#_CPPv423bk_aud_register_aud_isr12aud_isr_id_t9aud_isr_tPv "bk_aud_register_aud_isr") \- register audio isr

Adc APIs:
:   - [`bk_aud_adc_init()`](#_CPPv415bk_aud_adc_init19aud_adc_work_mode_tPK16aud_adc_config_tPK17aud_dtmf_config_t "bk_aud_adc_init") \- init the adc module of audio
    - [`bk_aud_adc_deinit()`](#_CPPv417bk_aud_adc_deinitv "bk_aud_adc_deinit") \- deinit the adc module of audio
    - [`bk_aud_set_adc_samp_rate()`](#_CPPv424bk_aud_set_adc_samp_rate19aud_adc_samp_rate_t "bk_aud_set_adc_samp_rate") \- set the sample rate in adc work mode
    - [`bk_aud_get_adc_fifo_addr()`](#_CPPv424bk_aud_get_adc_fifo_addrP8uint32_t "bk_aud_get_adc_fifo_addr") \- get the adc fifo address in adc work mode
    - [`bk_aud_get_dtmf_fifo_addr()`](#_CPPv425bk_aud_get_dtmf_fifo_addrP8uint32_t "bk_aud_get_dtmf_fifo_addr") \- get the dtmf fifo address in adc work mode
    - [`bk_aud_get_adc_status()`](#_CPPv421bk_aud_get_adc_statusP8uint32_t "bk_aud_get_adc_status") \- get the adc status information in adc work mode
    - [`bk_aud_get_dtmf_status()`](#_CPPv422bk_aud_get_dtmf_statusP8uint32_t "bk_aud_get_dtmf_status") \- get the dtmf status information in dtmf work mode
    - [`bk_aud_enable_adc_int()`](#_CPPv421bk_aud_enable_adc_intv "bk_aud_enable_adc_int") \- enable adc interrupt
    - [`bk_aud_disable_adc_int()`](#_CPPv422bk_aud_disable_adc_intv "bk_aud_disable_adc_int") \- disable adc interrupt
    - [`bk_aud_start_adc()`](#_CPPv416bk_aud_start_adcv "bk_aud_start_adc") \- start adc function
    - [`bk_aud_stop_adc()`](#_CPPv415bk_aud_stop_adcv "bk_aud_stop_adc") \- stop adc function
    - [`bk_aud_get_adc_fifo_data()`](#_CPPv424bk_aud_get_adc_fifo_dataP8uint32_t "bk_aud_get_adc_fifo_data") \- get adc data
    - [`bk_aud_get_dtmf_fifo_data()`](#_CPPv425bk_aud_get_dtmf_fifo_dataP8uint32_t "bk_aud_get_dtmf_fifo_data") \- get dtmf data

Dac APIs:
:   - [`bk_aud_dac_init()`](#_CPPv415bk_aud_dac_initPK16aud_dac_config_t "bk_aud_dac_init") \- init the dac module of audio
    - [`bk_aud_dac_deinit()`](#_CPPv417bk_aud_dac_deinitv "bk_aud_dac_deinit") \- deinit the dac module of audio
    - [`bk_aud_set_dac_samp_rate()`](#_CPPv424bk_aud_set_dac_samp_rate19aud_dac_samp_rate_t "bk_aud_set_dac_samp_rate") \- set the sample rate of audio dac function
    - [`bk_aud_get_dac_fifo_addr()`](#_CPPv424bk_aud_get_dac_fifo_addrP8uint32_t "bk_aud_get_dac_fifo_addr") \- get the dac fifo address
    - [`bk_aud_enable_dac_int()`](#_CPPv421bk_aud_enable_dac_intv "bk_aud_enable_dac_int") \- enable dac interrupt function
    - [`bk_aud_disable_dac_int()`](#_CPPv422bk_aud_disable_dac_intv "bk_aud_disable_dac_int") \- disable dac interrupt function
    - [`bk_aud_get_dac_status()`](#_CPPv421bk_aud_get_dac_statusP8uint32_t "bk_aud_get_dac_status") \- get the dac fifo status information
    - [`bk_aud_start_dac()`](#_CPPv416bk_aud_start_dacv "bk_aud_start_dac") \- start dac function
    - [`bk_aud_stop_dac()`](#_CPPv415bk_aud_stop_dacv "bk_aud_stop_dac") \- stop dac function

Eq APIs:
:   - [`bk_aud_eq_init()`](#_CPPv414bk_aud_eq_initPK15aud_eq_config_t "bk_aud_eq_init") \- init the eq module of audio
    - [`bk_aud_eq_deinit()`](#_CPPv416bk_aud_eq_deinitP15aud_eq_config_t "bk_aud_eq_deinit") \- deinit the eq module of audio

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [aud.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/aud.h)

<a id="functions"></a>

### Functions

<a id="_CPPv418bk_aud_driver_initv"></a>

<a id="_CPPv318bk_aud_driver_initv"></a> <a id="_CPPv218bk_aud_driver_initv"></a> <a id="bk_aud_driver_init__void"></a> <a id="group__bk__api__aud_1ga18ad26490ed46ed2eeddbd1625edcc18"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_driver\_init(void)
:   Init the AUD driver.

    This API init the resoure common:

    - Init AUD driver control memory
    - Configure clock and power
    - Configure mic enable
    - Register AUD isr interrupt

    This API should be called before any other AUD APIs.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_aud_driver_deinitv"></a>

<a id="_CPPv320bk_aud_driver_deinitv"></a> <a id="_CPPv220bk_aud_driver_deinitv"></a> <a id="bk_aud_driver_deinit__void"></a> <a id="group__bk__api__aud_1ga482c69843eb37cb9a65fed7195b603f3"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_driver\_deinit(void)
:   Deinit the AUD driver.

    This API free all resource related to AUD, power down AUD and mic.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv415bk_aud_adc_init19aud_adc_work_mode_tPK16aud_adc_config_tPK17aud_dtmf_config_t"></a>

<a id="_CPPv315bk_aud_adc_init19aud_adc_work_mode_tPK16aud_adc_config_tPK17aud_dtmf_config_t"></a> <a id="_CPPv215bk_aud_adc_init19aud_adc_work_mode_tPK16aud_adc_config_tPK17aud_dtmf_config_t"></a> <a id="bk_aud_adc_init__aud_adc_work_mode_t.aud_adc_config_tCP.aud_dtmf_config_tCP"></a> <a id="group__bk__api__aud_1ga5b1a3e3a44a0a678b3015262f9b1052c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_adc\_init([aud\_adc\_work\_mode\_t](#_CPPv419aud_adc_work_mode_t "aud_adc_work_mode_t") adc\_work\_mode, const [aud\_adc\_config\_t](#_CPPv416aud_adc_config_t "aud_adc_config_t") \*adc\_config, const [aud\_dtmf\_config\_t](#_CPPv417aud_dtmf_config_t "aud_dtmf_config_t") \*dtmf\_config)
:   Init the adc module of audio.

    This API init the adc module:

    - Set adc work mode: adc/dtmf
    - Configure the adc/dtmf parameters
    - disable adc/dtmf
    - disable adc/dtmf interrupts

    参数
    :   - **adc\_work\_mode** – adc work mode adc/dtmf
        - **adc\_config** – adc configure of adc work mode
        - **dtmf\_config** – dtmf configure of dtmf work mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_ADC\_MODE: adc work mode is error
        - BK\_ERR\_NULL\_PARAM: config is NULL
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init
        - others: other errors.

<a id="_CPPv417bk_aud_adc_deinitv"></a>

<a id="_CPPv317bk_aud_adc_deinitv"></a> <a id="_CPPv217bk_aud_adc_deinitv"></a> <a id="bk_aud_adc_deinit__void"></a> <a id="group__bk__api__aud_1ga75d436ff00b669d03700e58709a6fa3f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_adc\_deinit(void)
:   Deinit adc module.

    This API deinit the adc module of audio:

    - Disable adc and dtmf

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_aud_set_adc_samp_rate19aud_adc_samp_rate_t"></a>

<a id="_CPPv324bk_aud_set_adc_samp_rate19aud_adc_samp_rate_t"></a> <a id="_CPPv224bk_aud_set_adc_samp_rate19aud_adc_samp_rate_t"></a> <a id="bk_aud_set_adc_samp_rate__aud_adc_samp_rate_t"></a> <a id="group__bk__api__aud_1gaadf0ce41663884731fe2d4e7319f999a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_set\_adc\_samp\_rate([aud\_adc\_samp\_rate\_t](#_CPPv419aud_adc_samp_rate_t "aud_adc_samp_rate_t") samp\_rate)
:   Set the sample rate in adc work mode.

    参数
    :   **samp\_rate** – adc sample rate of adc work mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init
        - others: other errors.

<a id="_CPPv419bk_aud_set_adc_gain8uint32_t"></a>

<a id="_CPPv319bk_aud_set_adc_gain8uint32_t"></a> <a id="_CPPv219bk_aud_set_adc_gain8uint32_t"></a> <a id="bk_aud_set_adc_gain__uint32_t"></a> <a id="group__bk__api__aud_1gab6db056c492a840d4324b9dbc93cb942"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_set\_adc\_gain(uint32\_t value)
:   Set the adc gain in adc work mode.

    参数
    :   **value** – the gain value of adc work mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init
        - others: other errors.

<a id="_CPPv418bk_aud_set_mic_chl16aud_mic_enable_t"></a>

<a id="_CPPv318bk_aud_set_mic_chl16aud_mic_enable_t"></a> <a id="_CPPv218bk_aud_set_mic_chl16aud_mic_enable_t"></a> <a id="bk_aud_set_mic_chl__aud_mic_enable_t"></a> <a id="group__bk__api__aud_1ga69dabefe287b929420680450713379d2"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_set\_mic\_chl([aud\_mic\_enable\_t](#_CPPv416aud_mic_enable_t "aud_mic_enable_t") mic\_chl)
:   Set the adc gain in adc work mode.

    参数
    :   **mic\_chl** – the mic channel value of adc work mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init
        - others: other errors.

<a id="_CPPv424bk_aud_set_mic_intf_mode12aud_mic_id_t19aud_adc_intf_mode_t"></a>

<a id="_CPPv324bk_aud_set_mic_intf_mode12aud_mic_id_t19aud_adc_intf_mode_t"></a> <a id="_CPPv224bk_aud_set_mic_intf_mode12aud_mic_id_t19aud_adc_intf_mode_t"></a> <a id="bk_aud_set_mic_intf_mode__aud_mic_id_t.aud_adc_intf_mode_t"></a> <a id="group__bk__api__aud_1ga8274601ad2403b55d0883f7b1701dfdc"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_set\_mic\_intf\_mode([aud\_mic\_id\_t](#_CPPv412aud_mic_id_t "aud_mic_id_t") mic\_id, [aud\_adc\_intf\_mode\_t](#_CPPv419aud_adc_intf_mode_t "aud_adc_intf_mode_t") intf\_mode)
:   Set the mic external interface mode in adc work mode.

    参数
    :   - **mic\_id** – the mic id
        - **intf\_mode** – signal end or difference

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init
        - others: other errors.

<a id="_CPPv424bk_aud_get_adc_fifo_addrP8uint32_t"></a>

<a id="_CPPv324bk_aud_get_adc_fifo_addrP8uint32_t"></a> <a id="_CPPv224bk_aud_get_adc_fifo_addrP8uint32_t"></a> <a id="bk_aud_get_adc_fifo_addr__uint32_tP"></a> <a id="group__bk__api__aud_1ga2bcde189c59bb723e6aa88f10ea85ef0"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_get\_adc\_fifo\_addr(uint32\_t \*adc\_fifo\_addr)
:   Get the adc fifo address in adc work mode.

    参数
    :   **adc\_fifo\_addr** – adc fifo address of adc work mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init
        - others: other errors.

<a id="_CPPv425bk_aud_get_dtmf_fifo_addrP8uint32_t"></a>

<a id="_CPPv325bk_aud_get_dtmf_fifo_addrP8uint32_t"></a> <a id="_CPPv225bk_aud_get_dtmf_fifo_addrP8uint32_t"></a> <a id="bk_aud_get_dtmf_fifo_addr__uint32_tP"></a> <a id="group__bk__api__aud_1gae66e05fed2d65bd96a133dac872ec074"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_get\_dtmf\_fifo\_addr(uint32\_t \*dtmf\_fifo\_addr)
:   Get the dtmf fifo address in adc work mode.

    参数
    :   **dtmf\_fifo\_addr** – dtmf fifo address of dtmf work mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init
        - others: other errors.

<a id="_CPPv424bk_aud_get_dac_fifo_addrP8uint32_t"></a>

<a id="_CPPv324bk_aud_get_dac_fifo_addrP8uint32_t"></a> <a id="_CPPv224bk_aud_get_dac_fifo_addrP8uint32_t"></a> <a id="bk_aud_get_dac_fifo_addr__uint32_tP"></a> <a id="group__bk__api__aud_1gadf3e398c71c8dca98f77c6b68cbb8bcd"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_get\_dac\_fifo\_addr(uint32\_t \*dac\_fifo\_addr)
:   Get the dac fifo address.

    参数
    :   **dac\_fifo\_addr, :** – dac fifo address

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init
        - others: other errors.

<a id="_CPPv421bk_aud_get_adc_statusP8uint32_t"></a>

<a id="_CPPv321bk_aud_get_adc_statusP8uint32_t"></a> <a id="_CPPv221bk_aud_get_adc_statusP8uint32_t"></a> <a id="bk_aud_get_adc_status__uint32_tP"></a> <a id="group__bk__api__aud_1ga1d81ecffc5c32bd0c7042d22177a752a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_get\_adc\_status(uint32\_t \*adc\_status)
:   Get the adc status information in adc work mode.

    This API get the adc status of adc work mode:

    - Get fifo status

    参数
    :   **adc\_status** – adc fifo status and agc status

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init
        - others: other errors.

<a id="_CPPv422bk_aud_get_dtmf_statusP8uint32_t"></a>

<a id="_CPPv322bk_aud_get_dtmf_statusP8uint32_t"></a> <a id="_CPPv222bk_aud_get_dtmf_statusP8uint32_t"></a> <a id="bk_aud_get_dtmf_status__uint32_tP"></a> <a id="group__bk__api__aud_1ga34b427603c98d45f8eba7ba614a4e172"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_get\_dtmf\_status(uint32\_t \*dtmf\_status)
:   Get the dtmf status information in dtmf work mode.

    This API get the adc status of dtmf work mode:

    - Get fifo status

    参数
    :   **dtmf\_status** – dtmf fifo status

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init
        - others: other errors.

<a id="_CPPv421bk_aud_enable_adc_intv"></a>

<a id="_CPPv321bk_aud_enable_adc_intv"></a> <a id="_CPPv221bk_aud_enable_adc_intv"></a> <a id="bk_aud_enable_adc_int__void"></a> <a id="group__bk__api__aud_1gac858eac00987c8fbb78dc3b7368e2449"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_enable\_adc\_int(void)
:   Enable adc interrupt.

    This API enable adc interrupt:

    - Enable adc interrupt if work mode is adc work mode
    - Enable dtmf interrupt if work mode is dtmf work mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init
        - others: other errors.

<a id="_CPPv422bk_aud_disable_adc_intv"></a>

<a id="_CPPv322bk_aud_disable_adc_intv"></a> <a id="_CPPv222bk_aud_disable_adc_intv"></a> <a id="bk_aud_disable_adc_int__void"></a> <a id="group__bk__api__aud_1ga70cfd7a3ca787cab3633bb9949d0ee78"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_disable\_adc\_int(void)
:   Disable adc interrupt.

    This API disable adc interrupt:

    - Disable adc interrupt if work mode is adc work mode
    - Disable dtmf interrupt if work mode is dtmf work mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init
        - others: other errors.

<a id="_CPPv416bk_aud_start_adcv"></a>

<a id="_CPPv316bk_aud_start_adcv"></a> <a id="_CPPv216bk_aud_start_adcv"></a> <a id="bk_aud_start_adc__void"></a> <a id="group__bk__api__aud_1ga3fe7b8ddedf98fecacd1403c62e0de33"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_start\_adc(void)
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
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_ADC\_MODE: adc work mode is NULL
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init
        - others: other errors.

<a id="_CPPv415bk_aud_stop_adcv"></a>

<a id="_CPPv315bk_aud_stop_adcv"></a> <a id="_CPPv215bk_aud_stop_adcv"></a> <a id="bk_aud_stop_adc__void"></a> <a id="group__bk__api__aud_1gaa70132367cfcb37f9a6c21c36aff137a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_stop\_adc(void)
:   Stop adc.

    This API stop adc:

    - Disable adc if work mode is adc work mode
    - Disable dtmf if work mode is dtmf work mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_ADC\_MODE: adc work mode is NULL
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init
        - others: other errors.

<a id="_CPPv424bk_aud_get_adc_fifo_dataP8uint32_t"></a>

<a id="_CPPv324bk_aud_get_adc_fifo_dataP8uint32_t"></a> <a id="_CPPv224bk_aud_get_adc_fifo_dataP8uint32_t"></a> <a id="bk_aud_get_adc_fifo_data__uint32_tP"></a> <a id="group__bk__api__aud_1ga1feba26f850807093bf0014a7b301515"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_get\_adc\_fifo\_data(uint32\_t \*adc\_data)
:   Get adc data.

    This API get adc fifo data

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_ADC\_MODE: adc work mode is NULL
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init
        - others: other errors.

<a id="_CPPv425bk_aud_get_dtmf_fifo_dataP8uint32_t"></a>

<a id="_CPPv325bk_aud_get_dtmf_fifo_dataP8uint32_t"></a> <a id="_CPPv225bk_aud_get_dtmf_fifo_dataP8uint32_t"></a> <a id="bk_aud_get_dtmf_fifo_data__uint32_tP"></a> <a id="group__bk__api__aud_1ga262a97a27705f4b42e713c687b218cc2"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_get\_dtmf\_fifo\_data(uint32\_t \*dtmf\_data)
:   Get dtmf data.

    This API get dtmf fifo data

    参数
    :   **dtmf\_data, :** – save dtmf data

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_ADC\_MODE: dtmf work mode is NULL
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init
        - others: other errors.

<a id="_CPPv415bk_aud_dac_initPK16aud_dac_config_t"></a>

<a id="_CPPv315bk_aud_dac_initPK16aud_dac_config_t"></a> <a id="_CPPv215bk_aud_dac_initPK16aud_dac_config_t"></a> <a id="bk_aud_dac_init__aud_dac_config_tCP"></a> <a id="group__bk__api__aud_1ga6fb92f7cfb7b1afa3404ff0242e4154e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_dac\_init(const [aud\_dac\_config\_t](#_CPPv416aud_dac_config_t "aud_dac_config_t") \*dac\_config)
:   Init the dac module of audio.

    This API init the dac module:

    - Configure the dac parameters to enable dac function.

    参数
    :   **dac\_config, :** – dac parameters configure

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: config is NULL
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init

<a id="_CPPv417bk_aud_dac_deinitv"></a>

<a id="_CPPv317bk_aud_dac_deinitv"></a> <a id="_CPPv217bk_aud_dac_deinitv"></a> <a id="bk_aud_dac_deinit__void"></a> <a id="group__bk__api__aud_1ga313b9fde2f0492a1a3b45533859ea5b6"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_dac\_deinit(void)
:   Deinit dac module of audio.

    This API deinit the dac module:

    - Configure the dac parameters to default value.

    参数
    :   **None** –

    返回
    :   - BK\_OK: succeed

<a id="_CPPv424bk_aud_set_dac_samp_rate19aud_dac_samp_rate_t"></a>

<a id="_CPPv324bk_aud_set_dac_samp_rate19aud_dac_samp_rate_t"></a> <a id="_CPPv224bk_aud_set_dac_samp_rate19aud_dac_samp_rate_t"></a> <a id="bk_aud_set_dac_samp_rate__aud_dac_samp_rate_t"></a> <a id="group__bk__api__aud_1gaa93f5c60d3923a965efd99e8f6a4f38e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_set\_dac\_samp\_rate([aud\_dac\_samp\_rate\_t](#_CPPv419aud_dac_samp_rate_t "aud_dac_samp_rate_t") samp\_rate)
:   Set the dac sample rate.

    This API set the dac sample rate value.

    参数
    :   **samp\_rate, :** – dac sample rate

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init

<a id="_CPPv419bk_aud_set_dac_gain8uint32_t"></a>

<a id="_CPPv319bk_aud_set_dac_gain8uint32_t"></a> <a id="_CPPv219bk_aud_set_dac_gain8uint32_t"></a> <a id="bk_aud_set_dac_gain__uint32_t"></a> <a id="group__bk__api__aud_1ga62a45c78ce4538e28e76d56602636202"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_set\_dac\_gain(uint32\_t value)
:   Set the dac gain.

    参数
    :   **value** – the gain value, range:0x00 \~ 0x3f

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init
        - others: other errors.

<a id="_CPPv418bk_aud_set_dac_chl20aud_dac_chl_enable_t"></a>

<a id="_CPPv318bk_aud_set_dac_chl20aud_dac_chl_enable_t"></a> <a id="_CPPv218bk_aud_set_dac_chl20aud_dac_chl_enable_t"></a> <a id="bk_aud_set_dac_chl__aud_dac_chl_enable_t"></a> <a id="group__bk__api__aud_1ga28bec5f73146bb346dbf61c96832b06c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_set\_dac\_chl([aud\_dac\_chl\_enable\_t](#_CPPv420aud_dac_chl_enable_t "aud_dac_chl_enable_t") dac\_chl)
:   Set the dac channel.

    参数
    :   **dac\_chl** – the channel value

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init
        - others: other errors.

<a id="_CPPv421bk_aud_enable_dac_intv"></a>

<a id="_CPPv321bk_aud_enable_dac_intv"></a> <a id="_CPPv221bk_aud_enable_dac_intv"></a> <a id="bk_aud_enable_dac_int__void"></a> <a id="group__bk__api__aud_1ga22549295a1a8aa26a068c268096df45c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_enable\_dac\_int(void)
:   Enable dac interrupt.

    This API enable dac interrupt:

    参数
    :   **None** –

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init

<a id="_CPPv422bk_aud_disable_dac_intv"></a>

<a id="_CPPv322bk_aud_disable_dac_intv"></a> <a id="_CPPv222bk_aud_disable_dac_intv"></a> <a id="bk_aud_disable_dac_int__void"></a> <a id="group__bk__api__aud_1ga657e73f349c8097d4350f737f1758a5d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_disable\_dac\_int(void)
:   Disable dac interrupt.

    This API disable dac interrupt:

    参数
    :   **None** –

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init

<a id="_CPPv421bk_aud_get_dac_statusP8uint32_t"></a>

<a id="_CPPv321bk_aud_get_dac_statusP8uint32_t"></a> <a id="_CPPv221bk_aud_get_dac_statusP8uint32_t"></a> <a id="bk_aud_get_dac_status__uint32_tP"></a> <a id="group__bk__api__aud_1ga710416338994f8bb0bdd0e81aa6a347d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_get\_dac\_status(uint32\_t \*dac\_status)
:   Get the dac status information.

    This API get the dac fifo status.

    Usage example:

    uint32\_t dac\_fifo\_status \= 0; bk\_aud\_get\_dac\_status(\&dac\_fifo\_status); if (dac\_fifo\_status \& AUD\_DACL\_NEAR\_EMPTY\_MASK) { }

    参数
    :   **dac\_status, :** – dac fifo status

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init

<a id="_CPPv416bk_aud_start_dacv"></a>

<a id="_CPPv316bk_aud_start_dacv"></a> <a id="_CPPv216bk_aud_start_dacv"></a> <a id="bk_aud_start_dac__void"></a> <a id="group__bk__api__aud_1ga072fe26dbdd3b8b6b7a986d5fff119d5"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_start\_dac(void)
:   Start dac.

    This API start dac function.

    参数
    :   **None** –

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init

<a id="_CPPv415bk_aud_stop_dacv"></a>

<a id="_CPPv315bk_aud_stop_dacv"></a> <a id="_CPPv215bk_aud_stop_dacv"></a> <a id="bk_aud_stop_dac__void"></a> <a id="group__bk__api__aud_1gae90be39660476aef58ac4bd57c19d114"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_stop\_dac(void)
:   Stop dac.

    This API stop dac function.

    参数
    :   **None** –

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init

<a id="_CPPv414bk_aud_eq_initPK15aud_eq_config_t"></a>

<a id="_CPPv314bk_aud_eq_initPK15aud_eq_config_t"></a> <a id="_CPPv214bk_aud_eq_initPK15aud_eq_config_t"></a> <a id="bk_aud_eq_init__aud_eq_config_tCP"></a> <a id="group__bk__api__aud_1ga5a0ba6f811daf714764e1a62532b0732"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_eq\_init(const [aud\_eq\_config\_t](#_CPPv415aud_eq_config_t "aud_eq_config_t") \*eq\_config)
:   Init the eq module of audio.

    This API init the eq module:

    - Configure the eq parameters to enable the eq function.

    参数
    :   **eq\_config, :** – eq parameter configure

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: config is NULL
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init

<a id="_CPPv416bk_aud_eq_deinitP15aud_eq_config_t"></a>

<a id="_CPPv316bk_aud_eq_deinitP15aud_eq_config_t"></a> <a id="_CPPv216bk_aud_eq_deinitP15aud_eq_config_t"></a> <a id="bk_aud_eq_deinit__aud_eq_config_tP"></a> <a id="group__bk__api__aud_1ga87bfc19354167f56287ec749ca0a4eee"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_eq\_deinit([aud\_eq\_config\_t](#_CPPv415aud_eq_config_t "aud_eq_config_t") \*eq\_config)
:   Deinit the eq module of audio.

    This API deinit the eq module:

    - Configure the eq parameters to default value.

    参数
    :   **eq\_config, :** – eq parameter configure

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: config is NULL

<a id="_CPPv423bk_aud_register_aud_isr12aud_isr_id_t9aud_isr_tPv"></a>

<a id="_CPPv323bk_aud_register_aud_isr12aud_isr_id_t9aud_isr_tPv"></a> <a id="_CPPv223bk_aud_register_aud_isr12aud_isr_id_t9aud_isr_tPv"></a> <a id="bk_aud_register_aud_isr__aud_isr_id_t.aud_isr_t.voidP"></a> <a id="group__bk__api__aud_1ga54b59db8afefcd9f8404ab661b5cb8b0"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_register\_aud\_isr([aud\_isr\_id\_t](#_CPPv412aud_isr_id_t "aud_isr_id_t") isr\_id, [aud\_isr\_t](#_CPPv49aud_isr_t "aud_isr_t") isr, void \*param)
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
    :   - **isr\_id** – adc work mode adc/dtmf
        - **isr** – audio isr callback
        - **param** – audio isr callback parameter

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_AUD\_ADC\_MODE: adc work mode is NULL
        - BK\_ERR\_AUD\_NOT\_INIT: audio driver is not init
        - others: other errors.

<a id="_CPPv429bk_aud_dac_dwa_bypass_control7uint8_t"></a>

<a id="_CPPv329bk_aud_dac_dwa_bypass_control7uint8_t"></a> <a id="_CPPv229bk_aud_dac_dwa_bypass_control7uint8_t"></a> <a id="bk_aud_dac_dwa_bypass_control__uint8_t"></a> <a id="group__bk__api__aud_1ga8d4ed3ffd7790051a5bb187b9e70066a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_dac\_dwa\_bypass\_control(uint8\_t value)

<a id="_CPPv423bk_aud_dac_set_ana_gain7uint8_t"></a>

<a id="_CPPv323bk_aud_dac_set_ana_gain7uint8_t"></a> <a id="_CPPv223bk_aud_dac_set_ana_gain7uint8_t"></a> <a id="bk_aud_dac_set_ana_gain__uint8_t"></a> <a id="group__bk__api__aud_1ga254f909f3e66ced3fd122703e2aeb512"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_dac\_set\_ana\_gain(uint8\_t value)

<a id="_CPPv423bk_aud_dac_get_ana_gainP8uint32_t"></a>

<a id="_CPPv323bk_aud_dac_get_ana_gainP8uint32_t"></a> <a id="_CPPv223bk_aud_dac_get_ana_gainP8uint32_t"></a> <a id="bk_aud_dac_get_ana_gain__uint32_tP"></a> <a id="group__bk__api__aud_1ga0dd3044b902e634d695f6c6e7aac37e9"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_dac\_get\_ana\_gain(uint32\_t \*gain)

<a id="api-typedefs"></a>

## API Typedefs

<a id="id1"></a>

### Header File

- [aud\_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/aud_types.h)

<a id="structures"></a>

### Structures

<a id="_CPPv416aud_int_config_t"></a>

<a id="_CPPv316aud_int_config_t"></a> <a id="_CPPv216aud_int_config_t"></a> <a id="aud_int_config_t"></a> <a id="structaud__int__config__t"></a> struct aud\_int\_config\_t

<a id="_CPPv417aud_dtmf_config_t"></a>

<a id="_CPPv317aud_dtmf_config_t"></a> <a id="_CPPv217aud_dtmf_config_t"></a> <a id="aud_dtmf_config_t"></a> <a id="structaud__dtmf__config__t"></a> struct aud\_dtmf\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17aud_dtmf_config_t10adc_enableE"></a>

    <a id="_CPPv3N17aud_dtmf_config_t10adc_enableE"></a> <a id="_CPPv2N17aud_dtmf_config_t10adc_enableE"></a> <a id="aud_dtmf_config_t::adc_enable__aud_adc_enable_t"></a> <a id="structaud__dtmf__config__t_1aea7a3ca778faee4dcd81d5649caf956f"></a> [aud\_adc\_enable\_t](#_CPPv416aud_adc_enable_t "aud_adc_enable_t") adc\_enable
    :   AUD adc enable

    <a id="_CPPv4N17aud_dtmf_config_t11line_enableE"></a>

    <a id="_CPPv3N17aud_dtmf_config_t11line_enableE"></a> <a id="_CPPv2N17aud_dtmf_config_t11line_enableE"></a> <a id="aud_dtmf_config_t::line_enable__aud_adc_line_enable_t"></a> <a id="structaud__dtmf__config__t_1ae618b715413779dc20c32fbbb8cafc57"></a> [aud\_adc\_line\_enable\_t](#_CPPv421aud_adc_line_enable_t "aud_adc_line_enable_t") line\_enable
    :   AUD line in enable

    <a id="_CPPv4N17aud_dtmf_config_t11dtmf_enableE"></a>

    <a id="_CPPv3N17aud_dtmf_config_t11dtmf_enableE"></a> <a id="_CPPv2N17aud_dtmf_config_t11dtmf_enableE"></a> <a id="aud_dtmf_config_t::dtmf_enable__aud_dtmf_enable_t"></a> <a id="structaud__dtmf__config__t_1a713db6a85c8da776900fdf8f5189963b"></a> [aud\_dtmf\_enable\_t](#_CPPv417aud_dtmf_enable_t "aud_dtmf_enable_t") dtmf\_enable
    :   AUD dtmf enable

    <a id="_CPPv4N17aud_dtmf_config_t12tone_patternE"></a>

    <a id="_CPPv3N17aud_dtmf_config_t12tone_patternE"></a> <a id="_CPPv2N17aud_dtmf_config_t12tone_patternE"></a> <a id="aud_dtmf_config_t::tone_pattern__aud_dtmf_tone_pattern_t"></a> <a id="structaud__dtmf__config__t_1a85d6c4d125702cc597ead2586fa69c38"></a> [aud\_dtmf\_tone\_pattern\_t](#_CPPv423aud_dtmf_tone_pattern_t "aud_dtmf_tone_pattern_t") tone\_pattern
    :   AUD dtmf tone pattern

    <a id="_CPPv4N17aud_dtmf_config_t9tone_modeE"></a>

    <a id="_CPPv3N17aud_dtmf_config_t9tone_modeE"></a> <a id="_CPPv2N17aud_dtmf_config_t9tone_modeE"></a> <a id="aud_dtmf_config_t::tone_mode__aud_dtmf_tone_mode_t"></a> <a id="structaud__dtmf__config__t_1afa9e12c8006e14375183fd5e171ca498"></a> [aud\_dtmf\_tone\_mode\_t](#_CPPv420aud_dtmf_tone_mode_t "aud_dtmf_tone_mode_t") tone\_mode
    :   AUD dtmf tone mode

    <a id="_CPPv4N17aud_dtmf_config_t15tone_pause_timeE"></a>

    <a id="_CPPv3N17aud_dtmf_config_t15tone_pause_timeE"></a> <a id="_CPPv2N17aud_dtmf_config_t15tone_pause_timeE"></a> <a id="aud_dtmf_config_t::tone_pause_time__uint32_t"></a> <a id="structaud__dtmf__config__t_1ab6c5ccc9ee8ab421635b5fa9a03bb672"></a> uint32\_t tone\_pause\_time
    :   AUD dtmf tone pause time

    <a id="_CPPv4N17aud_dtmf_config_t16tone_active_timeE"></a>

    <a id="_CPPv3N17aud_dtmf_config_t16tone_active_timeE"></a> <a id="_CPPv2N17aud_dtmf_config_t16tone_active_timeE"></a> <a id="aud_dtmf_config_t::tone_active_time__uint32_t"></a> <a id="structaud__dtmf__config__t_1ab331cb5ac7b05610b9c06a265b657cb2"></a> uint32\_t tone\_active\_time
    :   AUD dtmf tone active time

    <a id="_CPPv4N17aud_dtmf_config_t10tone1_stepE"></a>

    <a id="_CPPv3N17aud_dtmf_config_t10tone1_stepE"></a> <a id="_CPPv2N17aud_dtmf_config_t10tone1_stepE"></a> <a id="aud_dtmf_config_t::tone1_step__uint32_t"></a> <a id="structaud__dtmf__config__t_1a6cabcbda99befe54e8318ef10c53235c"></a> uint32\_t tone1\_step
    :   AUD dtmf Tone1 frequency set Step \= F(KHz) \* 8191

    <a id="_CPPv4N17aud_dtmf_config_t10tone1_attuE"></a>

    <a id="_CPPv3N17aud_dtmf_config_t10tone1_attuE"></a> <a id="_CPPv2N17aud_dtmf_config_t10tone1_attuE"></a> <a id="aud_dtmf_config_t::tone1_attu__aud_dtmf_tone_attu_t"></a> <a id="structaud__dtmf__config__t_1ad5c20d8820e9dca6f0cc79fa1060c606"></a> [aud\_dtmf\_tone\_attu\_t](#_CPPv420aud_dtmf_tone_attu_t "aud_dtmf_tone_attu_t") tone1\_attu
    :   AUD dtmf Tone1 damp set 0 ：-1 ：-15 dB

    <a id="_CPPv4N17aud_dtmf_config_t12tone1_enableE"></a>

    <a id="_CPPv3N17aud_dtmf_config_t12tone1_enableE"></a> <a id="_CPPv2N17aud_dtmf_config_t12tone1_enableE"></a> <a id="aud_dtmf_config_t::tone1_enable__aud_dtmf_tone_enable_t"></a> <a id="structaud__dtmf__config__t_1a97ed7d1ce53c334a15285bcbfbf4711f"></a> [aud\_dtmf\_tone\_enable\_t](#_CPPv422aud_dtmf_tone_enable_t "aud_dtmf_tone_enable_t") tone1\_enable
    :   AUD dtmf tone1 enable

    <a id="_CPPv4N17aud_dtmf_config_t10tone2_stepE"></a>

    <a id="_CPPv3N17aud_dtmf_config_t10tone2_stepE"></a> <a id="_CPPv2N17aud_dtmf_config_t10tone2_stepE"></a> <a id="aud_dtmf_config_t::tone2_step__uint32_t"></a> <a id="structaud__dtmf__config__t_1adba78e3af1eb4ffa9d13654ac4fb3a16"></a> uint32\_t tone2\_step
    :   AUD dtmf Tone2 frequency set Step \= F(KHz) \* 8191

    <a id="_CPPv4N17aud_dtmf_config_t10tone2_attuE"></a>

    <a id="_CPPv3N17aud_dtmf_config_t10tone2_attuE"></a> <a id="_CPPv2N17aud_dtmf_config_t10tone2_attuE"></a> <a id="aud_dtmf_config_t::tone2_attu__aud_dtmf_tone_attu_t"></a> <a id="structaud__dtmf__config__t_1a5bea009e7f36750275de63a3ad53c927"></a> [aud\_dtmf\_tone\_attu\_t](#_CPPv420aud_dtmf_tone_attu_t "aud_dtmf_tone_attu_t") tone2\_attu
    :   AUD dtmf Tone2 damp set 0 ：-1 ：-15 dB

    <a id="_CPPv4N17aud_dtmf_config_t12tone2_enableE"></a>

    <a id="_CPPv3N17aud_dtmf_config_t12tone2_enableE"></a> <a id="_CPPv2N17aud_dtmf_config_t12tone2_enableE"></a> <a id="aud_dtmf_config_t::tone2_enable__aud_dtmf_tone_enable_t"></a> <a id="structaud__dtmf__config__t_1aa4ddd35650190843051d1c5a1586283f"></a> [aud\_dtmf\_tone\_enable\_t](#_CPPv422aud_dtmf_tone_enable_t "aud_dtmf_tone_enable_t") tone2\_enable
    :   AUD dtmf tone2 enable

    <a id="_CPPv4N17aud_dtmf_config_t17dtmf_wr_thresholdE"></a>

    <a id="_CPPv3N17aud_dtmf_config_t17dtmf_wr_thresholdE"></a> <a id="_CPPv2N17aud_dtmf_config_t17dtmf_wr_thresholdE"></a> <a id="aud_dtmf_config_t::dtmf_wr_threshold__uint32_t"></a> <a id="structaud__dtmf__config__t_1a6b6e8bc062f67d9aa42cbefc61e04426"></a> uint32\_t dtmf\_wr\_threshold
    :   AUD dtmf write threshold value

    <a id="_CPPv4N17aud_dtmf_config_t15dtmf_int_enableE"></a>

    <a id="_CPPv3N17aud_dtmf_config_t15dtmf_int_enableE"></a> <a id="_CPPv2N17aud_dtmf_config_t15dtmf_int_enableE"></a> <a id="aud_dtmf_config_t::dtmf_int_enable__aud_dtmf_int_t"></a> <a id="structaud__dtmf__config__t_1a14ba352fc4604f8f55ef4aa2cafef2bc"></a> [aud\_dtmf\_int\_t](#_CPPv414aud_dtmf_int_t "aud_dtmf_int_t") dtmf\_int\_enable
    :   AUD dtmf interrupt request enable

    <a id="_CPPv4N17aud_dtmf_config_t12loop_ton2dacE"></a>

    <a id="_CPPv3N17aud_dtmf_config_t12loop_ton2dacE"></a> <a id="_CPPv2N17aud_dtmf_config_t12loop_ton2dacE"></a> <a id="aud_dtmf_config_t::loop_ton2dac__aud_loop_dtmf2dac_t"></a> <a id="structaud__dtmf__config__t_1a375f79c5109f30fb0adf15e8518a6bc9"></a> [aud\_loop\_dtmf2dac\_t](#_CPPv419aud_loop_dtmf2dac_t "aud_loop_dtmf2dac_t") loop\_ton2dac
    :   AUD dtmf to DAC loop test enable

<a id="_CPPv416aud_adc_config_t"></a>

<a id="_CPPv316aud_adc_config_t"></a> <a id="_CPPv216aud_adc_config_t"></a> <a id="aud_adc_config_t"></a> <a id="structaud__adc__config__t"></a> struct aud\_adc\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N16aud_adc_config_t9samp_rateE"></a>

    <a id="_CPPv3N16aud_adc_config_t9samp_rateE"></a> <a id="_CPPv2N16aud_adc_config_t9samp_rateE"></a> <a id="aud_adc_config_t::samp_rate__aud_adc_samp_rate_t"></a> <a id="structaud__adc__config__t_1a9dddff814f47e6c9580dae66133dc798"></a> [aud\_adc\_samp\_rate\_t](#_CPPv419aud_adc_samp_rate_t "aud_adc_samp_rate_t") samp\_rate
    :   AUD adc sample rate

    <a id="_CPPv4N16aud_adc_config_t10adc_enableE"></a>

    <a id="_CPPv3N16aud_adc_config_t10adc_enableE"></a> <a id="_CPPv2N16aud_adc_config_t10adc_enableE"></a> <a id="aud_adc_config_t::adc_enable__aud_adc_enable_t"></a> <a id="structaud__adc__config__t_1a46d22d2d191fefc2b14e372da0c48242"></a> [aud\_adc\_enable\_t](#_CPPv416aud_adc_enable_t "aud_adc_enable_t") adc\_enable
    :   AUD adc enable

    <a id="_CPPv4N16aud_adc_config_t11line_enableE"></a>

    <a id="_CPPv3N16aud_adc_config_t11line_enableE"></a> <a id="_CPPv2N16aud_adc_config_t11line_enableE"></a> <a id="aud_adc_config_t::line_enable__aud_adc_line_enable_t"></a> <a id="structaud__adc__config__t_1a4249b6b9314b56dc40464c0796438da0"></a> [aud\_adc\_line\_enable\_t](#_CPPv421aud_adc_line_enable_t "aud_adc_line_enable_t") line\_enable
    :   AUD line in enable

    <a id="_CPPv4N16aud_adc_config_t11dtmf_enableE"></a>

    <a id="_CPPv3N16aud_adc_config_t11dtmf_enableE"></a> <a id="_CPPv2N16aud_adc_config_t11dtmf_enableE"></a> <a id="aud_adc_config_t::dtmf_enable__aud_dtmf_enable_t"></a> <a id="structaud__adc__config__t_1a74ecf0255b9b37890fbf6ef6bee4ba9c"></a> [aud\_dtmf\_enable\_t](#_CPPv417aud_dtmf_enable_t "aud_dtmf_enable_t") dtmf\_enable
    :   AUD dtmf enable

    <a id="_CPPv4N16aud_adc_config_t16adc_hpf2_coef_B2E"></a>

    <a id="_CPPv3N16aud_adc_config_t16adc_hpf2_coef_B2E"></a> <a id="_CPPv2N16aud_adc_config_t16adc_hpf2_coef_B2E"></a> <a id="aud_adc_config_t::adc_hpf2_coef_B2__uint32_t"></a> <a id="structaud__adc__config__t_1a330e437df6d13fbe4e35b0ef6394226a"></a> uint32\_t adc\_hpf2\_coef\_B2
    :   AUD adc HPF2 coefficient B2

    <a id="_CPPv4N16aud_adc_config_t22adc_hpf2_bypass_enableE"></a>

    <a id="_CPPv3N16aud_adc_config_t22adc_hpf2_bypass_enableE"></a> <a id="_CPPv2N16aud_adc_config_t22adc_hpf2_bypass_enableE"></a> <a id="aud_adc_config_t::adc_hpf2_bypass_enable__aud_adc_hpf_bypass_t"></a> <a id="structaud__adc__config__t_1a97a5a13b50b24e5d3aa6498743b75f18"></a> [aud\_adc\_hpf\_bypass\_t](#_CPPv420aud_adc_hpf_bypass_t "aud_adc_hpf_bypass_t") adc\_hpf2\_bypass\_enable
    :   AUD adc hpf2 disable

    <a id="_CPPv4N16aud_adc_config_t22adc_hpf1_bypass_enableE"></a>

    <a id="_CPPv3N16aud_adc_config_t22adc_hpf1_bypass_enableE"></a> <a id="_CPPv2N16aud_adc_config_t22adc_hpf1_bypass_enableE"></a> <a id="aud_adc_config_t::adc_hpf1_bypass_enable__aud_adc_hpf_bypass_t"></a> <a id="structaud__adc__config__t_1a1fcd966e90b6c74d8bc934f8c69d7874"></a> [aud\_adc\_hpf\_bypass\_t](#_CPPv420aud_adc_hpf_bypass_t "aud_adc_hpf_bypass_t") adc\_hpf1\_bypass\_enable
    :   AUD adc hpf1 disable

    <a id="_CPPv4N16aud_adc_config_t12adc_set_gainE"></a>

    <a id="_CPPv3N16aud_adc_config_t12adc_set_gainE"></a> <a id="_CPPv2N16aud_adc_config_t12adc_set_gainE"></a> <a id="aud_adc_config_t::adc_set_gain__uint32_t"></a> <a id="structaud__adc__config__t_1ab62444ea137cb02f765f92eb25359a70"></a> uint32\_t adc\_set\_gain
    :   AUD adc gain set

    <a id="_CPPv4N16aud_adc_config_t13adc_samp_edgeE"></a>

    <a id="_CPPv3N16aud_adc_config_t13adc_samp_edgeE"></a> <a id="_CPPv2N16aud_adc_config_t13adc_samp_edgeE"></a> <a id="aud_adc_config_t::adc_samp_edge__aud_adc_samp_edge_t"></a> <a id="structaud__adc__config__t_1a045eca3e42f63fd82452b9d7150a0dc4"></a> [aud\_adc\_samp\_edge\_t](#_CPPv419aud_adc_samp_edge_t "aud_adc_samp_edge_t") adc\_samp\_edge
    :   ADC data sampling clock edge select rising/falling

    <a id="_CPPv4N16aud_adc_config_t16adc_hpf2_coef_B0E"></a>

    <a id="_CPPv3N16aud_adc_config_t16adc_hpf2_coef_B0E"></a> <a id="_CPPv2N16aud_adc_config_t16adc_hpf2_coef_B0E"></a> <a id="aud_adc_config_t::adc_hpf2_coef_B0__uint32_t"></a> <a id="structaud__adc__config__t_1ae53bbb301e72ce2ec64f9acb466a0ef1"></a> uint32\_t adc\_hpf2\_coef\_B0
    :   AUD adc HPF2 coefficient B0

    <a id="_CPPv4N16aud_adc_config_t16adc_hpf2_coef_B1E"></a>

    <a id="_CPPv3N16aud_adc_config_t16adc_hpf2_coef_B1E"></a> <a id="_CPPv2N16aud_adc_config_t16adc_hpf2_coef_B1E"></a> <a id="aud_adc_config_t::adc_hpf2_coef_B1__uint32_t"></a> <a id="structaud__adc__config__t_1a9fc8b3a7dba60a8550c36c16d7c2c8e1"></a> uint32\_t adc\_hpf2\_coef\_B1
    :   AUD adc HPF2 coefficient B1

    <a id="_CPPv4N16aud_adc_config_t16adc_hpf2_coef_A0E"></a>

    <a id="_CPPv3N16aud_adc_config_t16adc_hpf2_coef_A0E"></a> <a id="_CPPv2N16aud_adc_config_t16adc_hpf2_coef_A0E"></a> <a id="aud_adc_config_t::adc_hpf2_coef_A0__uint32_t"></a> <a id="structaud__adc__config__t_1aeb570253b53524cd3d77a3ccddd2e336"></a> uint32\_t adc\_hpf2\_coef\_A0
    :   AUD adc HPF2 coefficient A0

    <a id="_CPPv4N16aud_adc_config_t16adc_hpf2_coef_A1E"></a>

    <a id="_CPPv3N16aud_adc_config_t16adc_hpf2_coef_A1E"></a> <a id="_CPPv2N16aud_adc_config_t16adc_hpf2_coef_A1E"></a> <a id="aud_adc_config_t::adc_hpf2_coef_A1__uint32_t"></a> <a id="structaud__adc__config__t_1ac717d652f37ddb8900acf12d3efe9888"></a> uint32\_t adc\_hpf2\_coef\_A1
    :   AUD adc HPF2 coefficient A1

    <a id="_CPPv4N16aud_adc_config_t17dtmf_wr_thresholdE"></a>

    <a id="_CPPv3N16aud_adc_config_t17dtmf_wr_thresholdE"></a> <a id="_CPPv2N16aud_adc_config_t17dtmf_wr_thresholdE"></a> <a id="aud_adc_config_t::dtmf_wr_threshold__uint32_t"></a> <a id="structaud__adc__config__t_1a1820453b7d0b77d93b4bdabf4eabe5ef"></a> uint32\_t dtmf\_wr\_threshold
    :   AUD dtmf write threshold value

    <a id="_CPPv4N16aud_adc_config_t17adcl_wr_thresholdE"></a>

    <a id="_CPPv3N16aud_adc_config_t17adcl_wr_thresholdE"></a> <a id="_CPPv2N16aud_adc_config_t17adcl_wr_thresholdE"></a> <a id="aud_adc_config_t::adcl_wr_threshold__uint32_t"></a> <a id="structaud__adc__config__t_1aa149e15b434e20a97c0169d40dd91ada"></a> uint32\_t adcl\_wr\_threshold
    :   AUD adcl write threshold value

    <a id="_CPPv4N16aud_adc_config_t15dtmf_int_enableE"></a>

    <a id="_CPPv3N16aud_adc_config_t15dtmf_int_enableE"></a> <a id="_CPPv2N16aud_adc_config_t15dtmf_int_enableE"></a> <a id="aud_adc_config_t::dtmf_int_enable__aud_dtmf_int_t"></a> <a id="structaud__adc__config__t_1a0357b0dd27ac8ebf1d5a74211057a498"></a> [aud\_dtmf\_int\_t](#_CPPv414aud_dtmf_int_t "aud_dtmf_int_t") dtmf\_int\_enable
    :   AUD dtmf interrupt request enable

    <a id="_CPPv4N16aud_adc_config_t15adcl_int_enableE"></a>

    <a id="_CPPv3N16aud_adc_config_t15adcl_int_enableE"></a> <a id="_CPPv2N16aud_adc_config_t15adcl_int_enableE"></a> <a id="aud_adc_config_t::adcl_int_enable__aud_adcl_int_t"></a> <a id="structaud__adc__config__t_1a4f4b5900f73dfede61ac655e104c9e95"></a> [aud\_adcl\_int\_t](#_CPPv414aud_adcl_int_t "aud_adcl_int_t") adcl\_int\_enable
    :   AUD adcl interrupt request enable

    <a id="_CPPv4N16aud_adc_config_t12loop_adc2dacE"></a>

    <a id="_CPPv3N16aud_adc_config_t12loop_adc2dacE"></a> <a id="_CPPv2N16aud_adc_config_t12loop_adc2dacE"></a> <a id="aud_adc_config_t::loop_adc2dac__aud_loop_adc2dac_t"></a> <a id="structaud__adc__config__t_1a612b1f695f9d61e490a4bb08dcd006ac"></a> [aud\_loop\_adc2dac\_t](#_CPPv418aud_loop_adc2dac_t "aud_loop_adc2dac_t") loop\_adc2dac
    :   AUD adc to DAC loop test enable

    <a id="_CPPv4N16aud_adc_config_t14agc_noise_thrdE"></a>

    <a id="_CPPv3N16aud_adc_config_t14agc_noise_thrdE"></a> <a id="_CPPv2N16aud_adc_config_t14agc_noise_thrdE"></a> <a id="aud_adc_config_t::agc_noise_thrd__uint32_t"></a> <a id="structaud__adc__config__t_1ae78e2a70ee8642b746d87584e665e097"></a> uint32\_t agc\_noise\_thrd
    :   AUD AGC noise gating of excute，noise gating work when audio value is little

    <a id="_CPPv4N16aud_adc_config_t14agc_noise_highE"></a>

    <a id="_CPPv3N16aud_adc_config_t14agc_noise_highE"></a> <a id="_CPPv2N16aud_adc_config_t14agc_noise_highE"></a> <a id="aud_adc_config_t::agc_noise_high__uint32_t"></a> <a id="structaud__adc__config__t_1a146a5124c4d858f105d25d482ef3882f"></a> uint32\_t agc\_noise\_high
    :   AUD AGC corresponding MIC\_RSSI low 10 bit

    <a id="_CPPv4N16aud_adc_config_t13agc_noise_lowE"></a>

    <a id="_CPPv3N16aud_adc_config_t13agc_noise_lowE"></a> <a id="_CPPv2N16aud_adc_config_t13agc_noise_lowE"></a> <a id="aud_adc_config_t::agc_noise_low__uint32_t"></a> <a id="structaud__adc__config__t_1a078141063c942cc3c52ab3709d15e4c2"></a> uint32\_t agc\_noise\_low
    :   AUD AGC corresponding MIC\_RSSI low 10 bit

    <a id="_CPPv4N16aud_adc_config_t13agc_noise_minE"></a>

    <a id="_CPPv3N16aud_adc_config_t13agc_noise_minE"></a> <a id="_CPPv2N16aud_adc_config_t13agc_noise_minE"></a> <a id="aud_adc_config_t::agc_noise_min__uint32_t"></a> <a id="structaud__adc__config__t_1ae6e8b9945f5ebd59fab072c35cba3b9a"></a> uint32\_t agc\_noise\_min
    :   AUD AGC {GAIN2\[2:0\] GAIN1\[3:0\]} when signal level below NOISE\_LOW, when noise gating is enabled

    <a id="_CPPv4N16aud_adc_config_t14agc_noise_toutE"></a>

    <a id="_CPPv3N16aud_adc_config_t14agc_noise_toutE"></a> <a id="_CPPv2N16aud_adc_config_t14agc_noise_toutE"></a> <a id="aud_adc_config_t::agc_noise_tout__aud_gac_noise_tout_t"></a> <a id="structaud__adc__config__t_1a91cbbc8e1fa71b903a69fc584bc09826"></a> [aud\_gac\_noise\_tout\_t](#_CPPv420aud_gac_noise_tout_t "aud_gac_noise_tout_t") agc\_noise\_tout
    :   AUD AGC noise tout

    <a id="_CPPv4N16aud_adc_config_t12agc_high_durE"></a>

    <a id="_CPPv3N16aud_adc_config_t12agc_high_durE"></a> <a id="_CPPv2N16aud_adc_config_t12agc_high_durE"></a> <a id="aud_adc_config_t::agc_high_dur__aud_gac_high_dur_t"></a> <a id="structaud__adc__config__t_1a2e157eab679cbaaddb328bf4974f443c"></a> [aud\_gac\_high\_dur\_t](#_CPPv418aud_gac_high_dur_t "aud_gac_high_dur_t") agc\_high\_dur
    :   AUD AGC high noise gating work duration

    <a id="_CPPv4N16aud_adc_config_t11agc_low_durE"></a>

    <a id="_CPPv3N16aud_adc_config_t11agc_low_durE"></a> <a id="_CPPv2N16aud_adc_config_t11agc_low_durE"></a> <a id="aud_adc_config_t::agc_low_dur__aud_gac_low_dur_t"></a> <a id="structaud__adc__config__t_1a1978f8f579044b9050223dd50d7102f9"></a> [aud\_gac\_low\_dur\_t](#_CPPv417aud_gac_low_dur_t "aud_gac_low_dur_t") agc\_low\_dur
    :   AUD AGC low noise gating work duration

    <a id="_CPPv4N16aud_adc_config_t7agc_minE"></a>

    <a id="_CPPv3N16aud_adc_config_t7agc_minE"></a> <a id="_CPPv2N16aud_adc_config_t7agc_minE"></a> <a id="aud_adc_config_t::agc_min__uint32_t"></a> <a id="structaud__adc__config__t_1a308c9dc1420a4269057a2e67b400c966"></a> uint32\_t agc\_min
    :   AUD AGC Minimum value of {GAIN2\[2:0\] GAIN1\[3:0\]}

    <a id="_CPPv4N16aud_adc_config_t7agc_maxE"></a>

    <a id="_CPPv3N16aud_adc_config_t7agc_maxE"></a> <a id="_CPPv2N16aud_adc_config_t7agc_maxE"></a> <a id="aud_adc_config_t::agc_max__uint32_t"></a> <a id="structaud__adc__config__t_1ac94fbd1ba72797fc5567abfb1a0c4fef"></a> uint32\_t agc\_max
    :   AUD AGC Maximum value of {GAIN2\[2:0\] GAIN1\[3:0\]} Also the default gain setting when AGC is disabled

    <a id="_CPPv4N16aud_adc_config_t13agc_ng_methodE"></a>

    <a id="_CPPv3N16aud_adc_config_t13agc_ng_methodE"></a> <a id="_CPPv2N16aud_adc_config_t13agc_ng_methodE"></a> <a id="aud_adc_config_t::agc_ng_method__aud_agc_method_t"></a> <a id="structaud__adc__config__t_1a697d2eb3ed9681e68cc051762ba8f705"></a> [aud\_agc\_method\_t](#_CPPv416aud_agc_method_t "aud_agc_method_t") agc\_ng\_method
    :   AUD AGC noise gating method

    <a id="_CPPv4N16aud_adc_config_t13agc_ng_enableE"></a>

    <a id="_CPPv3N16aud_adc_config_t13agc_ng_enableE"></a> <a id="_CPPv2N16aud_adc_config_t13agc_ng_enableE"></a> <a id="aud_adc_config_t::agc_ng_enable__aud_agc_ng_enable_t"></a> <a id="structaud__adc__config__t_1a5193dec7c4e086b45f578b5ffb301f8d"></a> [aud\_agc\_ng\_enable\_t](#_CPPv419aud_agc_ng_enable_t "aud_agc_ng_enable_t") agc\_ng\_enable
    :   AUD AGC enable noise gating

    <a id="_CPPv4N16aud_adc_config_t14agc_decay_timeE"></a>

    <a id="_CPPv3N16aud_adc_config_t14agc_decay_timeE"></a> <a id="_CPPv2N16aud_adc_config_t14agc_decay_timeE"></a> <a id="aud_adc_config_t::agc_decay_time__aud_agc_decay_time_t"></a> <a id="structaud__adc__config__t_1ae53b1d29eab253b61ce04c512903d0d7"></a> [aud\_agc\_decay\_time\_t](#_CPPv420aud_agc_decay_time_t "aud_agc_decay_time_t") agc\_decay\_time
    :   AUD AGC agc decay time

    <a id="_CPPv4N16aud_adc_config_t15agc_attack_timeE"></a>

    <a id="_CPPv3N16aud_adc_config_t15agc_attack_timeE"></a> <a id="_CPPv2N16aud_adc_config_t15agc_attack_timeE"></a> <a id="aud_adc_config_t::agc_attack_time__aud_agc_attack_time_t"></a> <a id="structaud__adc__config__t_1ade2376c12a758efb0d2a47e7f872d707"></a> [aud\_agc\_attack\_time\_t](#_CPPv421aud_agc_attack_time_t "aud_agc_attack_time_t") agc\_attack\_time
    :   AUD AGC agc attack time

    <a id="_CPPv4N16aud_adc_config_t13agc_high_thrdE"></a>

    <a id="_CPPv3N16aud_adc_config_t13agc_high_thrdE"></a> <a id="_CPPv2N16aud_adc_config_t13agc_high_thrdE"></a> <a id="aud_adc_config_t::agc_high_thrd__uint32_t"></a> <a id="structaud__adc__config__t_1a90cf4dea78bf7122f3c6911f0176ff90"></a> uint32\_t agc\_high\_thrd
    :   AUD AGC coefficient high five bit of MIC\_RSSI

    <a id="_CPPv4N16aud_adc_config_t12agc_low_thrdE"></a>

    <a id="_CPPv3N16aud_adc_config_t12agc_low_thrdE"></a> <a id="_CPPv2N16aud_adc_config_t12agc_low_thrdE"></a> <a id="aud_adc_config_t::agc_low_thrd__uint32_t"></a> <a id="structaud__adc__config__t_1afd21657e64fc353fd4bd59f45c31d471"></a> uint32\_t agc\_low\_thrd
    :   AUD AGC coefficient low five bit of MIC\_RSSI

    <a id="_CPPv4N16aud_adc_config_t12agc_iir_coefE"></a>

    <a id="_CPPv3N16aud_adc_config_t12agc_iir_coefE"></a> <a id="_CPPv2N16aud_adc_config_t12agc_iir_coefE"></a> <a id="aud_adc_config_t::agc_iir_coef__aud_agc_iir_coef_t"></a> <a id="structaud__adc__config__t_1af9b6f05cc27df1783d32a83958634502"></a> [aud\_agc\_iir\_coef\_t](#_CPPv418aud_agc_iir_coef_t "aud_agc_iir_coef_t") agc\_iir\_coef
    :   AUD AGC iir coefficient select

    <a id="_CPPv4N16aud_adc_config_t10agc_enableE"></a>

    <a id="_CPPv3N16aud_adc_config_t10agc_enableE"></a> <a id="_CPPv2N16aud_adc_config_t10agc_enableE"></a> <a id="aud_adc_config_t::agc_enable__aud_agc_enable_t"></a> <a id="structaud__adc__config__t_1a4a39286a13cdac17783d01406a0bffcf"></a> [aud\_agc\_enable\_t](#_CPPv416aud_agc_enable_t "aud_agc_enable_t") agc\_enable
    :   AUD AGC enable

    <a id="_CPPv4N16aud_adc_config_t16manual_pga_valueE"></a>

    <a id="_CPPv3N16aud_adc_config_t16manual_pga_valueE"></a> <a id="_CPPv2N16aud_adc_config_t16manual_pga_valueE"></a> <a id="aud_adc_config_t::manual_pga_value__uint32_t"></a> <a id="structaud__adc__config__t_1ac8727729364c9fb1e66d92a32d63e5e1"></a> uint32\_t manual\_pga\_value
    :   AUD AGC manual set PGA value

    <a id="_CPPv4N16aud_adc_config_t17manual_pga_enableE"></a>

    <a id="_CPPv3N16aud_adc_config_t17manual_pga_enableE"></a> <a id="_CPPv2N16aud_adc_config_t17manual_pga_enableE"></a> <a id="aud_adc_config_t::manual_pga_enable__aud_agc_manual_pga_en_t"></a> <a id="structaud__adc__config__t_1a24235499cc0e79244435e9e8254b84e9"></a> [aud\_agc\_manual\_pga\_en\_t](#_CPPv423aud_agc_manual_pga_en_t "aud_agc_manual_pga_en_t") manual\_pga\_enable
    :   AUD AGC manual set PGA enable

<a id="_CPPv416aud_dac_config_t"></a>

<a id="_CPPv316aud_dac_config_t"></a> <a id="_CPPv216aud_dac_config_t"></a> <a id="aud_dac_config_t"></a> <a id="structaud__dac__config__t"></a> struct aud\_dac\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N16aud_dac_config_t10dac_enableE"></a>

    <a id="_CPPv3N16aud_dac_config_t10dac_enableE"></a> <a id="_CPPv2N16aud_dac_config_t10dac_enableE"></a> <a id="aud_dac_config_t::dac_enable__aud_dac_enable_t"></a> <a id="structaud__dac__config__t_1aca90a12b4b716ad5d69efdfc9b6b549a"></a> [aud\_dac\_enable\_t](#_CPPv416aud_dac_enable_t "aud_dac_enable_t") dac\_enable
    :   AUD dac enable

    <a id="_CPPv4N16aud_dac_config_t9samp_rateE"></a>

    <a id="_CPPv3N16aud_dac_config_t9samp_rateE"></a> <a id="_CPPv2N16aud_dac_config_t9samp_rateE"></a> <a id="aud_dac_config_t::samp_rate__aud_dac_samp_rate_t"></a> <a id="structaud__dac__config__t_1a892311ba13efb670f4027663c0b75a5f"></a> [aud\_dac\_samp\_rate\_t](#_CPPv419aud_dac_samp_rate_t "aud_dac_samp_rate_t") samp\_rate
    :   AUD dac sample rate

    <a id="_CPPv4N16aud_dac_config_t7dac_chlE"></a>

    <a id="_CPPv3N16aud_dac_config_t7dac_chlE"></a> <a id="_CPPv2N16aud_dac_config_t7dac_chlE"></a> <a id="aud_dac_config_t::dac_chl__aud_dac_chl_enable_t"></a> <a id="structaud__dac__config__t_1afd8de4a3fbe7805aa9057a1fc2ee6a1a"></a> [aud\_dac\_chl\_enable\_t](#_CPPv420aud_dac_chl_enable_t "aud_dac_chl_enable_t") dac\_chl
    :   AUD dac channel

    <a id="_CPPv4N16aud_dac_config_t9work_modeE"></a>

    <a id="_CPPv3N16aud_dac_config_t9work_modeE"></a> <a id="_CPPv2N16aud_dac_config_t9work_modeE"></a> <a id="aud_dac_config_t::work_mode__aud_dac_work_mode_t"></a> <a id="structaud__dac__config__t_1a9938827b5ecc1b7f6fcf018c1abed349"></a> [aud\_dac\_work\_mode\_t](#_CPPv419aud_dac_work_mode_t "aud_dac_work_mode_t") work\_mode
    :   AUD dac work mode

    <a id="_CPPv4N16aud_dac_config_t16dac_hpf2_coef_B2E"></a>

    <a id="_CPPv3N16aud_dac_config_t16dac_hpf2_coef_B2E"></a> <a id="_CPPv2N16aud_dac_config_t16dac_hpf2_coef_B2E"></a> <a id="aud_dac_config_t::dac_hpf2_coef_B2__uint16_t"></a> <a id="structaud__dac__config__t_1a7dd6056921892325709fb719249bef15"></a> uint16\_t dac\_hpf2\_coef\_B2
    :   AUD dac HPF2 coefficient B2

    <a id="_CPPv4N16aud_dac_config_t22dac_hpf2_bypass_enableE"></a>

    <a id="_CPPv3N16aud_dac_config_t22dac_hpf2_bypass_enableE"></a> <a id="_CPPv2N16aud_dac_config_t22dac_hpf2_bypass_enableE"></a> <a id="aud_dac_config_t::dac_hpf2_bypass_enable__aud_dac_hpf_bypass_t"></a> <a id="structaud__dac__config__t_1a0a9cd04cec848a5e8d50d160a5de0b50"></a> [aud\_dac\_hpf\_bypass\_t](#_CPPv420aud_dac_hpf_bypass_t "aud_dac_hpf_bypass_t") dac\_hpf2\_bypass\_enable
    :   AUD dac hpf2 disable

    <a id="_CPPv4N16aud_dac_config_t22dac_hpf1_bypass_enableE"></a>

    <a id="_CPPv3N16aud_dac_config_t22dac_hpf1_bypass_enableE"></a> <a id="_CPPv2N16aud_dac_config_t22dac_hpf1_bypass_enableE"></a> <a id="aud_dac_config_t::dac_hpf1_bypass_enable__aud_dac_hpf_bypass_t"></a> <a id="structaud__dac__config__t_1ab391e25df1baebdad6b291e114f9e275"></a> [aud\_dac\_hpf\_bypass\_t](#_CPPv420aud_dac_hpf_bypass_t "aud_dac_hpf_bypass_t") dac\_hpf1\_bypass\_enable
    :   AUD dac hpf1 disable

    <a id="_CPPv4N16aud_dac_config_t12dac_set_gainE"></a>

    <a id="_CPPv3N16aud_dac_config_t12dac_set_gainE"></a> <a id="_CPPv2N16aud_dac_config_t12dac_set_gainE"></a> <a id="aud_dac_config_t::dac_set_gain__uint16_t"></a> <a id="structaud__dac__config__t_1a11627d9a45823062a32032606841a9ee"></a> uint16\_t dac\_set\_gain
    :   AUD dac gain set

    <a id="_CPPv4N16aud_dac_config_t14dac_clk_invertE"></a>

    <a id="_CPPv3N16aud_dac_config_t14dac_clk_invertE"></a> <a id="_CPPv2N16aud_dac_config_t14dac_clk_invertE"></a> <a id="aud_dac_config_t::dac_clk_invert__aud_dac_clk_invert_t"></a> <a id="structaud__dac__config__t_1a8801992347f319b61bcd8a481dd0379b"></a> [aud\_dac\_clk\_invert\_t](#_CPPv420aud_dac_clk_invert_t "aud_dac_clk_invert_t") dac\_clk\_invert
    :   AUD dac output clock edge select

    <a id="_CPPv4N16aud_dac_config_t16dac_hpf2_coef_B0E"></a>

    <a id="_CPPv3N16aud_dac_config_t16dac_hpf2_coef_B0E"></a> <a id="_CPPv2N16aud_dac_config_t16dac_hpf2_coef_B0E"></a> <a id="aud_dac_config_t::dac_hpf2_coef_B0__uint16_t"></a> <a id="structaud__dac__config__t_1ad22526e09b254547f8f24e8ddf186b8e"></a> uint16\_t dac\_hpf2\_coef\_B0
    :   AUD dac HPF2 coefficient B0

    <a id="_CPPv4N16aud_dac_config_t16dac_hpf2_coef_B1E"></a>

    <a id="_CPPv3N16aud_dac_config_t16dac_hpf2_coef_B1E"></a> <a id="_CPPv2N16aud_dac_config_t16dac_hpf2_coef_B1E"></a> <a id="aud_dac_config_t::dac_hpf2_coef_B1__uint16_t"></a> <a id="structaud__dac__config__t_1afeb6d2f385977fb892cc9564be40a2e5"></a> uint16\_t dac\_hpf2\_coef\_B1
    :   AUD dac HPF2 coefficient B1

    <a id="_CPPv4N16aud_dac_config_t16dac_hpf2_coef_A1E"></a>

    <a id="_CPPv3N16aud_dac_config_t16dac_hpf2_coef_A1E"></a> <a id="_CPPv2N16aud_dac_config_t16dac_hpf2_coef_A1E"></a> <a id="aud_dac_config_t::dac_hpf2_coef_A1__uint16_t"></a> <a id="structaud__dac__config__t_1a419674a39957c027e0f4a0da899287c7"></a> uint16\_t dac\_hpf2\_coef\_A1
    :   AUD dac HPF2 coefficient A1

    <a id="_CPPv4N16aud_dac_config_t16dac_hpf2_coef_A2E"></a>

    <a id="_CPPv3N16aud_dac_config_t16dac_hpf2_coef_A2E"></a> <a id="_CPPv2N16aud_dac_config_t16dac_hpf2_coef_A2E"></a> <a id="aud_dac_config_t::dac_hpf2_coef_A2__uint16_t"></a> <a id="structaud__dac__config__t_1a349cbcd34eb2b0070758630d94446553"></a> uint16\_t dac\_hpf2\_coef\_A2
    :   AUD dac HPF2 coefficient A2

    <a id="_CPPv4N16aud_dac_config_t17dacr_rd_thresholdE"></a>

    <a id="_CPPv3N16aud_dac_config_t17dacr_rd_thresholdE"></a> <a id="_CPPv2N16aud_dac_config_t17dacr_rd_thresholdE"></a> <a id="aud_dac_config_t::dacr_rd_threshold__uint8_t"></a> <a id="structaud__dac__config__t_1ad22cc1c2aa5bf517eb494eb1ace48392"></a> uint8\_t dacr\_rd\_threshold
    :   AUD dacl read threshold value

    <a id="_CPPv4N16aud_dac_config_t17dacl_rd_thresholdE"></a>

    <a id="_CPPv3N16aud_dac_config_t17dacl_rd_thresholdE"></a> <a id="_CPPv2N16aud_dac_config_t17dacl_rd_thresholdE"></a> <a id="aud_dac_config_t::dacl_rd_threshold__uint8_t"></a> <a id="structaud__dac__config__t_1a9f541623c3ee59df635738522ea343fe"></a> uint8\_t dacl\_rd\_threshold
    :   AUD dacr read threshold value

    <a id="_CPPv4N16aud_dac_config_t15dacr_int_enableE"></a>

    <a id="_CPPv3N16aud_dac_config_t15dacr_int_enableE"></a> <a id="_CPPv2N16aud_dac_config_t15dacr_int_enableE"></a> <a id="aud_dac_config_t::dacr_int_enable__uint8_t"></a> <a id="structaud__dac__config__t_1a18f1f799c2004bd1618720615620e04d"></a> uint8\_t dacr\_int\_enable
    :   AUD dacr interrupt request enable

    <a id="_CPPv4N16aud_dac_config_t15dacl_int_enableE"></a>

    <a id="_CPPv3N16aud_dac_config_t15dacl_int_enableE"></a> <a id="_CPPv2N16aud_dac_config_t15dacl_int_enableE"></a> <a id="aud_dac_config_t::dacl_int_enable__uint8_t"></a> <a id="structaud__dac__config__t_1a67ab230267829b6be46cca2eb87b1545"></a> uint8\_t dacl\_int\_enable
    :   AUD dacl interrupt request enable

    <a id="_CPPv4N16aud_dac_config_t15dac_filt_enableE"></a>

    <a id="_CPPv3N16aud_dac_config_t15dac_filt_enableE"></a> <a id="_CPPv2N16aud_dac_config_t15dac_filt_enableE"></a> <a id="aud_dac_config_t::dac_filt_enable__aud_dac_filt_enable_t"></a> <a id="structaud__dac__config__t_1acb220ad2f65f7e41ba07ce8941e74a73"></a> [aud\_dac\_filt\_enable\_t](#_CPPv421aud_dac_filt_enable_t "aud_dac_filt_enable_t") dac\_filt\_enable
    :   AUD dac filter enable

<a id="_CPPv415aud_eq_config_t"></a>

<a id="_CPPv315aud_eq_config_t"></a> <a id="_CPPv215aud_eq_config_t"></a> <a id="aud_eq_config_t"></a> <a id="structaud__eq__config__t"></a> struct aud\_eq\_config\_t

<a id="macros"></a>

### Macros

<a id="c.BK_ERR_AUD_NOT_INIT"></a>

<a id="group__bk__api__aud__defs_1ga7eef4f15e761f208d40e9571a1b39422"></a> BK\_ERR\_AUD\_NOT\_INIT
:   AUD driver not init

<a id="c.BK_ERR_AUD_ISR_ID"></a>

<a id="group__bk__api__aud__defs_1gad345f2f08ab44b75baa002e73606a9ff"></a> BK\_ERR\_AUD\_ISR\_ID
:   AUD isr id is invalid

<a id="c.BK_ERR_AUD_ADC_MODE"></a>

<a id="group__bk__api__aud__defs_1ga747ba697d3bde695a8fa94ed41ef6f69"></a> BK\_ERR\_AUD\_ADC\_MODE
:   AUD adc work mode is invalid

<a id="c.AUD_HAL_REG_BASE"></a>

<a id="group__bk__api__aud__defs_1ga929299ce098a0fb16ec164a7d1b6fb9b"></a> AUD\_HAL\_REG\_BASE

<a id="c.AUD_DAC_FIFO_ADDR"></a>

<a id="group__bk__api__aud__defs_1gae9bd7ac9406b5371f4fe3752e52d11b4"></a> AUD\_DAC\_FIFO\_ADDR

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv49aud_isr_t"></a>

<a id="_CPPv39aud_isr_t"></a> <a id="_CPPv29aud_isr_t"></a> <a id="aud_isr_t"></a> <a id="aud__types_8h_1afafc9dd97fba40ebb84729c903010eee"></a> typedef void (\*aud\_isr\_t)(void \*param)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv412aud_isr_id_t"></a>

<a id="_CPPv312aud_isr_id_t"></a> <a id="_CPPv212aud_isr_id_t"></a> <a id="group__bk__api__aud__enum_1gaea1aa729e7e2dc4b39f12f1ea8693054"></a> enum aud\_isr\_id\_t
:   *Values:*

    <a id="_CPPv4N12aud_isr_id_t12AUD_ISR_DTMFE"></a>

    <a id="_CPPv3N12aud_isr_id_t12AUD_ISR_DTMFE"></a> <a id="_CPPv2N12aud_isr_id_t12AUD_ISR_DTMFE"></a> <a id="group__bk__api__aud__enum_1ggaea1aa729e7e2dc4b39f12f1ea8693054ade123a1156f742f38790fd82a252e6dd"></a> enumerator AUD\_ISR\_DTMF
    :   dtmf\_int\_en

    <a id="_CPPv4N12aud_isr_id_t12AUD_ISR_ADCLE"></a>

    <a id="_CPPv3N12aud_isr_id_t12AUD_ISR_ADCLE"></a> <a id="_CPPv2N12aud_isr_id_t12AUD_ISR_ADCLE"></a> <a id="group__bk__api__aud__enum_1ggaea1aa729e7e2dc4b39f12f1ea8693054ad521d62db99d4b1a0b7accb116a8be78"></a> enumerator AUD\_ISR\_ADCL
    :   adcl\_int\_en

    <a id="_CPPv4N12aud_isr_id_t12AUD_ISR_DACRE"></a>

    <a id="_CPPv3N12aud_isr_id_t12AUD_ISR_DACRE"></a> <a id="_CPPv2N12aud_isr_id_t12AUD_ISR_DACRE"></a> <a id="group__bk__api__aud__enum_1ggaea1aa729e7e2dc4b39f12f1ea8693054a588596956b0197402b79351791692326"></a> enumerator AUD\_ISR\_DACR
    :   dacr\_int\_en

    <a id="_CPPv4N12aud_isr_id_t12AUD_ISR_DACLE"></a>

    <a id="_CPPv3N12aud_isr_id_t12AUD_ISR_DACLE"></a> <a id="_CPPv2N12aud_isr_id_t12AUD_ISR_DACLE"></a> <a id="group__bk__api__aud__enum_1ggaea1aa729e7e2dc4b39f12f1ea8693054a3744cb7a7a4f4eabb082ee0700010c0f"></a> enumerator AUD\_ISR\_DACL
    :   dacl\_int\_en

    <a id="_CPPv4N12aud_isr_id_t11AUD_ISR_MAXE"></a>

    <a id="_CPPv3N12aud_isr_id_t11AUD_ISR_MAXE"></a> <a id="_CPPv2N12aud_isr_id_t11AUD_ISR_MAXE"></a> <a id="group__bk__api__aud__enum_1ggaea1aa729e7e2dc4b39f12f1ea8693054a731ddd163b3ba2599b7e993ac92f6b04"></a> enumerator AUD\_ISR\_MAX
    :   AUD isr id max

<a id="_CPPv419aud_adc_work_mode_t"></a>

<a id="_CPPv319aud_adc_work_mode_t"></a> <a id="_CPPv219aud_adc_work_mode_t"></a> <a id="group__bk__api__aud__enum_1gaf316e32a31aac186d5c095e872b3fe62"></a> enum aud\_adc\_work\_mode\_t
:   *Values:*

    <a id="_CPPv4N19aud_adc_work_mode_t22AUD_ADC_WORK_MODE_NULLE"></a>

    <a id="_CPPv3N19aud_adc_work_mode_t22AUD_ADC_WORK_MODE_NULLE"></a> <a id="_CPPv2N19aud_adc_work_mode_t22AUD_ADC_WORK_MODE_NULLE"></a> <a id="group__bk__api__aud__enum_1ggaf316e32a31aac186d5c095e872b3fe62ab3b1d2557e52e05f63aefec6c238ae0a"></a> enumerator AUD\_ADC\_WORK\_MODE\_NULL
    :   no mode

    <a id="_CPPv4N19aud_adc_work_mode_t21AUD_ADC_WORK_MODE_ADCE"></a>

    <a id="_CPPv3N19aud_adc_work_mode_t21AUD_ADC_WORK_MODE_ADCE"></a> <a id="_CPPv2N19aud_adc_work_mode_t21AUD_ADC_WORK_MODE_ADCE"></a> <a id="group__bk__api__aud__enum_1ggaf316e32a31aac186d5c095e872b3fe62a7f95cbc6f8668368b755736b11131029"></a> enumerator AUD\_ADC\_WORK\_MODE\_ADC
    :   ADC mode

    <a id="_CPPv4N19aud_adc_work_mode_t22AUD_ADC_WORK_MODE_DTMFE"></a>

    <a id="_CPPv3N19aud_adc_work_mode_t22AUD_ADC_WORK_MODE_DTMFE"></a> <a id="_CPPv2N19aud_adc_work_mode_t22AUD_ADC_WORK_MODE_DTMFE"></a> <a id="group__bk__api__aud__enum_1ggaf316e32a31aac186d5c095e872b3fe62ab53c49da5f44e86eab5debcb169bc493"></a> enumerator AUD\_ADC\_WORK\_MODE\_DTMF
    :   DTMF mode

    <a id="_CPPv4N19aud_adc_work_mode_t21AUD_ADC_WORK_MODE_MAXE"></a>

    <a id="_CPPv3N19aud_adc_work_mode_t21AUD_ADC_WORK_MODE_MAXE"></a> <a id="_CPPv2N19aud_adc_work_mode_t21AUD_ADC_WORK_MODE_MAXE"></a> <a id="group__bk__api__aud__enum_1ggaf316e32a31aac186d5c095e872b3fe62ad07dc326d3246c6b04de2f75aa637058"></a> enumerator AUD\_ADC\_WORK\_MODE\_MAX

<a id="_CPPv419aud_adc_intf_mode_t"></a>

<a id="_CPPv319aud_adc_intf_mode_t"></a> <a id="_CPPv219aud_adc_intf_mode_t"></a> <a id="group__bk__api__aud__enum_1gab54a0b60ad5da3cf612b68a74667880a"></a> enum aud\_adc\_intf\_mode\_t
:   *Values:*

    <a id="_CPPv4N19aud_adc_intf_mode_t24AUD_ADC_INTF_MODE_DIFFENE"></a>

    <a id="_CPPv3N19aud_adc_intf_mode_t24AUD_ADC_INTF_MODE_DIFFENE"></a> <a id="_CPPv2N19aud_adc_intf_mode_t24AUD_ADC_INTF_MODE_DIFFENE"></a> <a id="group__bk__api__aud__enum_1ggab54a0b60ad5da3cf612b68a74667880aa28b7570750d8f0393205230ee5acc105"></a> enumerator AUD\_ADC\_INTF\_MODE\_DIFFEN

    <a id="_CPPv4N19aud_adc_intf_mode_t28AUD_ADC_INTF_MODE_SIGNAL_ENDE"></a>

    <a id="_CPPv3N19aud_adc_intf_mode_t28AUD_ADC_INTF_MODE_SIGNAL_ENDE"></a> <a id="_CPPv2N19aud_adc_intf_mode_t28AUD_ADC_INTF_MODE_SIGNAL_ENDE"></a> <a id="group__bk__api__aud__enum_1ggab54a0b60ad5da3cf612b68a74667880aa2dc627f9edc0e37ebca66cfcab9b6394"></a> enumerator AUD\_ADC\_INTF\_MODE\_SIGNAL\_END

    <a id="_CPPv4N19aud_adc_intf_mode_t21AUD_ADC_INTF_MODE_MAXE"></a>

    <a id="_CPPv3N19aud_adc_intf_mode_t21AUD_ADC_INTF_MODE_MAXE"></a> <a id="_CPPv2N19aud_adc_intf_mode_t21AUD_ADC_INTF_MODE_MAXE"></a> <a id="group__bk__api__aud__enum_1ggab54a0b60ad5da3cf612b68a74667880aac975645df43d247571491bb0ee9f631f"></a> enumerator AUD\_ADC\_INTF\_MODE\_MAX

<a id="_CPPv419aud_adc_samp_rate_t"></a>

<a id="_CPPv319aud_adc_samp_rate_t"></a> <a id="_CPPv219aud_adc_samp_rate_t"></a> <a id="group__bk__api__aud__enum_1gacd2c411863ca49cd2d9e84fa6d62a7f2"></a> enum aud\_adc\_samp\_rate\_t
:   *Values:*

    <a id="_CPPv4N19aud_adc_samp_rate_t20AUD_ADC_SAMP_RATE_8KE"></a>

    <a id="_CPPv3N19aud_adc_samp_rate_t20AUD_ADC_SAMP_RATE_8KE"></a> <a id="_CPPv2N19aud_adc_samp_rate_t20AUD_ADC_SAMP_RATE_8KE"></a> <a id="group__bk__api__aud__enum_1ggacd2c411863ca49cd2d9e84fa6d62a7f2a77cdf6e807f4d370a873a760a7ad5e33"></a> enumerator AUD\_ADC\_SAMP\_RATE\_8K
    :   ADC sample rate : 8k

    <a id="_CPPv4N19aud_adc_samp_rate_t25AUD_ADC_SAMP_RATE_11_025KE"></a>

    <a id="_CPPv3N19aud_adc_samp_rate_t25AUD_ADC_SAMP_RATE_11_025KE"></a> <a id="_CPPv2N19aud_adc_samp_rate_t25AUD_ADC_SAMP_RATE_11_025KE"></a> <a id="group__bk__api__aud__enum_1ggacd2c411863ca49cd2d9e84fa6d62a7f2a4ff8bef6cd6d4b1048f0370e4aa4768c"></a> enumerator AUD\_ADC\_SAMP\_RATE\_11\_025K
    :   ADC sample rate : 11.025k

    <a id="_CPPv4N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_12KE"></a>

    <a id="_CPPv3N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_12KE"></a> <a id="_CPPv2N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_12KE"></a> <a id="group__bk__api__aud__enum_1ggacd2c411863ca49cd2d9e84fa6d62a7f2a66e08ce5164aa72a794572851029726c"></a> enumerator AUD\_ADC\_SAMP\_RATE\_12K
    :   ADC sample rate : 12k

    <a id="_CPPv4N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_16KE"></a>

    <a id="_CPPv3N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_16KE"></a> <a id="_CPPv2N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_16KE"></a> <a id="group__bk__api__aud__enum_1ggacd2c411863ca49cd2d9e84fa6d62a7f2aa78b54fb2444e56bea52cfdb481b3d24"></a> enumerator AUD\_ADC\_SAMP\_RATE\_16K
    :   ADC sample rate : 16k

    <a id="_CPPv4N19aud_adc_samp_rate_t24AUD_ADC_SAMP_RATE_22_05KE"></a>

    <a id="_CPPv3N19aud_adc_samp_rate_t24AUD_ADC_SAMP_RATE_22_05KE"></a> <a id="_CPPv2N19aud_adc_samp_rate_t24AUD_ADC_SAMP_RATE_22_05KE"></a> <a id="group__bk__api__aud__enum_1ggacd2c411863ca49cd2d9e84fa6d62a7f2ac29fcd0f517e3e37cf9bf6bba57a8358"></a> enumerator AUD\_ADC\_SAMP\_RATE\_22\_05K
    :   ADC sample rate : 22.05k

    <a id="_CPPv4N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_24KE"></a>

    <a id="_CPPv3N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_24KE"></a> <a id="_CPPv2N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_24KE"></a> <a id="group__bk__api__aud__enum_1ggacd2c411863ca49cd2d9e84fa6d62a7f2a6286d72ab3b0eadbf690d2c5622afee9"></a> enumerator AUD\_ADC\_SAMP\_RATE\_24K
    :   ADC sample rate : 24k

    <a id="_CPPv4N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_32KE"></a>

    <a id="_CPPv3N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_32KE"></a> <a id="_CPPv2N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_32KE"></a> <a id="group__bk__api__aud__enum_1ggacd2c411863ca49cd2d9e84fa6d62a7f2a7cf4e842b7b01bb0d851e5ba6ba9c317"></a> enumerator AUD\_ADC\_SAMP\_RATE\_32K
    :   ADC sample rate : 32k

    <a id="_CPPv4N19aud_adc_samp_rate_t23AUD_ADC_SAMP_RATE_44_1KE"></a>

    <a id="_CPPv3N19aud_adc_samp_rate_t23AUD_ADC_SAMP_RATE_44_1KE"></a> <a id="_CPPv2N19aud_adc_samp_rate_t23AUD_ADC_SAMP_RATE_44_1KE"></a> <a id="group__bk__api__aud__enum_1ggacd2c411863ca49cd2d9e84fa6d62a7f2a1a721f6fed65d13effe049f642ba7c29"></a> enumerator AUD\_ADC\_SAMP\_RATE\_44\_1K
    :   ADC sample rate : 44.1k

    <a id="_CPPv4N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_48KE"></a>

    <a id="_CPPv3N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_48KE"></a> <a id="_CPPv2N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_48KE"></a> <a id="group__bk__api__aud__enum_1ggacd2c411863ca49cd2d9e84fa6d62a7f2a9df5576bc45a03f80b7f37fd60f6008e"></a> enumerator AUD\_ADC\_SAMP\_RATE\_48K
    :   ADC sample rate : 48k

    <a id="_CPPv4N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_MAXE"></a>

    <a id="_CPPv3N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_MAXE"></a> <a id="_CPPv2N19aud_adc_samp_rate_t21AUD_ADC_SAMP_RATE_MAXE"></a> <a id="group__bk__api__aud__enum_1ggacd2c411863ca49cd2d9e84fa6d62a7f2acdb38825baa46e73bca27d519ec3e4b6"></a> enumerator AUD\_ADC\_SAMP\_RATE\_MAX

<a id="_CPPv420aud_adc_hpf_bypass_t"></a>

<a id="_CPPv320aud_adc_hpf_bypass_t"></a> <a id="_CPPv220aud_adc_hpf_bypass_t"></a> <a id="group__bk__api__aud__enum_1ga67bea4a32281a6e38ac6752517619c4d"></a> enum aud\_adc\_hpf\_bypass\_t
:   *Values:*

    <a id="_CPPv4N20aud_adc_hpf_bypass_t26AUD_ADC_HPF_BYPASS_DISABLEE"></a>

    <a id="_CPPv3N20aud_adc_hpf_bypass_t26AUD_ADC_HPF_BYPASS_DISABLEE"></a> <a id="_CPPv2N20aud_adc_hpf_bypass_t26AUD_ADC_HPF_BYPASS_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga67bea4a32281a6e38ac6752517619c4da19a795ec9128bdc769137c2fd128420d"></a> enumerator AUD\_ADC\_HPF\_BYPASS\_DISABLE
    :   AUD ADC hpf bypass disable

    <a id="_CPPv4N20aud_adc_hpf_bypass_t25AUD_ADC_HPF_BYPASS_ENABLEE"></a>

    <a id="_CPPv3N20aud_adc_hpf_bypass_t25AUD_ADC_HPF_BYPASS_ENABLEE"></a> <a id="_CPPv2N20aud_adc_hpf_bypass_t25AUD_ADC_HPF_BYPASS_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga67bea4a32281a6e38ac6752517619c4dad32ed4259f85b96182a655158619c710"></a> enumerator AUD\_ADC\_HPF\_BYPASS\_ENABLE
    :   AUD ADC hpf bypass enable

    <a id="_CPPv4N20aud_adc_hpf_bypass_t22AUD_ADC_HPF_BYPASS_MAXE"></a>

    <a id="_CPPv3N20aud_adc_hpf_bypass_t22AUD_ADC_HPF_BYPASS_MAXE"></a> <a id="_CPPv2N20aud_adc_hpf_bypass_t22AUD_ADC_HPF_BYPASS_MAXE"></a> <a id="group__bk__api__aud__enum_1gga67bea4a32281a6e38ac6752517619c4daf887e714c7484b6db2cdc6b5b56f1d09"></a> enumerator AUD\_ADC\_HPF\_BYPASS\_MAX

<a id="_CPPv419aud_adc_samp_edge_t"></a>

<a id="_CPPv319aud_adc_samp_edge_t"></a> <a id="_CPPv219aud_adc_samp_edge_t"></a> <a id="group__bk__api__aud__enum_1ga88eab049efd681337a138bc58cd05b42"></a> enum aud\_adc\_samp\_edge\_t
:   *Values:*

    <a id="_CPPv4N19aud_adc_samp_edge_t24AUD_ADC_SAMP_EDGE_RISINGE"></a>

    <a id="_CPPv3N19aud_adc_samp_edge_t24AUD_ADC_SAMP_EDGE_RISINGE"></a> <a id="_CPPv2N19aud_adc_samp_edge_t24AUD_ADC_SAMP_EDGE_RISINGE"></a> <a id="group__bk__api__aud__enum_1gga88eab049efd681337a138bc58cd05b42a6982c49c697b5ffaedc9a5f3da269a66"></a> enumerator AUD\_ADC\_SAMP\_EDGE\_RISING
    :   AUD ADC sampling clock edge : rising edge

    <a id="_CPPv4N19aud_adc_samp_edge_t25AUD_ADC_SAMP_EDGE_FALLINGE"></a>

    <a id="_CPPv3N19aud_adc_samp_edge_t25AUD_ADC_SAMP_EDGE_FALLINGE"></a> <a id="_CPPv2N19aud_adc_samp_edge_t25AUD_ADC_SAMP_EDGE_FALLINGE"></a> <a id="group__bk__api__aud__enum_1gga88eab049efd681337a138bc58cd05b42a3dec3e1a4f38922c582b26411a8b6688"></a> enumerator AUD\_ADC\_SAMP\_EDGE\_FALLING
    :   AUD ADC sampling clock edge : falling edge

    <a id="_CPPv4N19aud_adc_samp_edge_t21AUD_ADC_SAMP_EDGE_MAXE"></a>

    <a id="_CPPv3N19aud_adc_samp_edge_t21AUD_ADC_SAMP_EDGE_MAXE"></a> <a id="_CPPv2N19aud_adc_samp_edge_t21AUD_ADC_SAMP_EDGE_MAXE"></a> <a id="group__bk__api__aud__enum_1gga88eab049efd681337a138bc58cd05b42a0de9ce4d42b52064997df00aa47e91be"></a> enumerator AUD\_ADC\_SAMP\_EDGE\_MAX

<a id="_CPPv414aud_adcl_int_t"></a>

<a id="_CPPv314aud_adcl_int_t"></a> <a id="_CPPv214aud_adcl_int_t"></a> <a id="group__bk__api__aud__enum_1gae6baacfd43801a70b3cfb59c6a242f9a"></a> enum aud\_adcl\_int\_t
:   *Values:*

    <a id="_CPPv4N14aud_adcl_int_t20AUD_ADCL_INT_DISABLEE"></a>

    <a id="_CPPv3N14aud_adcl_int_t20AUD_ADCL_INT_DISABLEE"></a> <a id="_CPPv2N14aud_adcl_int_t20AUD_ADCL_INT_DISABLEE"></a> <a id="group__bk__api__aud__enum_1ggae6baacfd43801a70b3cfb59c6a242f9aa5f6030d97320bb8c706a8e6003b92a4b"></a> enumerator AUD\_ADCL\_INT\_DISABLE
    :   AUD ADCL interrupt disable

    <a id="_CPPv4N14aud_adcl_int_t19AUD_ADCL_INT_ENABLEE"></a>

    <a id="_CPPv3N14aud_adcl_int_t19AUD_ADCL_INT_ENABLEE"></a> <a id="_CPPv2N14aud_adcl_int_t19AUD_ADCL_INT_ENABLEE"></a> <a id="group__bk__api__aud__enum_1ggae6baacfd43801a70b3cfb59c6a242f9aa4606f71233f13c1acdb9fa044b9279d3"></a> enumerator AUD\_ADCL\_INT\_ENABLE
    :   AUD ADCL interrupt enable

    <a id="_CPPv4N14aud_adcl_int_t16AUD_ADCL_INT_MAXE"></a>

    <a id="_CPPv3N14aud_adcl_int_t16AUD_ADCL_INT_MAXE"></a> <a id="_CPPv2N14aud_adcl_int_t16AUD_ADCL_INT_MAXE"></a> <a id="group__bk__api__aud__enum_1ggae6baacfd43801a70b3cfb59c6a242f9aa9bdbb92f30743c4f82023832ae8c06b5"></a> enumerator AUD\_ADCL\_INT\_MAX

<a id="_CPPv414aud_dtmf_int_t"></a>

<a id="_CPPv314aud_dtmf_int_t"></a> <a id="_CPPv214aud_dtmf_int_t"></a> <a id="group__bk__api__aud__enum_1ga70f41f39e1d35c9a337eb7f0e40e461b"></a> enum aud\_dtmf\_int\_t
:   *Values:*

    <a id="_CPPv4N14aud_dtmf_int_t20AUD_DTMF_INT_DISABLEE"></a>

    <a id="_CPPv3N14aud_dtmf_int_t20AUD_DTMF_INT_DISABLEE"></a> <a id="_CPPv2N14aud_dtmf_int_t20AUD_DTMF_INT_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga70f41f39e1d35c9a337eb7f0e40e461ba3a5873ed7f274b2effda97c59f315a52"></a> enumerator AUD\_DTMF\_INT\_DISABLE
    :   AUD DTMF interrupt disable

    <a id="_CPPv4N14aud_dtmf_int_t19AUD_DTMF_INT_ENABLEE"></a>

    <a id="_CPPv3N14aud_dtmf_int_t19AUD_DTMF_INT_ENABLEE"></a> <a id="_CPPv2N14aud_dtmf_int_t19AUD_DTMF_INT_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga70f41f39e1d35c9a337eb7f0e40e461ba273c3f0a686df1c12a42f0ba901e1686"></a> enumerator AUD\_DTMF\_INT\_ENABLE
    :   AUD DTMF interrupt enable

    <a id="_CPPv4N14aud_dtmf_int_t16AUD_DTMF_INT_MAXE"></a>

    <a id="_CPPv3N14aud_dtmf_int_t16AUD_DTMF_INT_MAXE"></a> <a id="_CPPv2N14aud_dtmf_int_t16AUD_DTMF_INT_MAXE"></a> <a id="group__bk__api__aud__enum_1gga70f41f39e1d35c9a337eb7f0e40e461ba26817036bfe9910de8da1fb62f8e17fd"></a> enumerator AUD\_DTMF\_INT\_MAX

<a id="_CPPv418aud_loop_adc2dac_t"></a>

<a id="_CPPv318aud_loop_adc2dac_t"></a> <a id="_CPPv218aud_loop_adc2dac_t"></a> <a id="group__bk__api__aud__enum_1ga22dc9e20f398c15c637fd9077c96c562"></a> enum aud\_loop\_adc2dac\_t
:   *Values:*

    <a id="_CPPv4N18aud_loop_adc2dac_t24AUD_LOOP_ADC2DAC_DISABLEE"></a>

    <a id="_CPPv3N18aud_loop_adc2dac_t24AUD_LOOP_ADC2DAC_DISABLEE"></a> <a id="_CPPv2N18aud_loop_adc2dac_t24AUD_LOOP_ADC2DAC_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga22dc9e20f398c15c637fd9077c96c562a7d9046b34319bde9726b6267ee8b210e"></a> enumerator AUD\_LOOP\_ADC2DAC\_DISABLE
    :   ADC to DAC loop test disable

    <a id="_CPPv4N18aud_loop_adc2dac_t23AUD_LOOP_ADC2DAC_ENABLEE"></a>

    <a id="_CPPv3N18aud_loop_adc2dac_t23AUD_LOOP_ADC2DAC_ENABLEE"></a> <a id="_CPPv2N18aud_loop_adc2dac_t23AUD_LOOP_ADC2DAC_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga22dc9e20f398c15c637fd9077c96c562a32a786c289a4748eacfb3a7736d44baf"></a> enumerator AUD\_LOOP\_ADC2DAC\_ENABLE
    :   ADC to DAC loop test enable

    <a id="_CPPv4N18aud_loop_adc2dac_t20AUD_LOOP_ADC2DAC_MAXE"></a>

    <a id="_CPPv3N18aud_loop_adc2dac_t20AUD_LOOP_ADC2DAC_MAXE"></a> <a id="_CPPv2N18aud_loop_adc2dac_t20AUD_LOOP_ADC2DAC_MAXE"></a> <a id="group__bk__api__aud__enum_1gga22dc9e20f398c15c637fd9077c96c562a5a01c33759f9df66f6897c38c7858e6a"></a> enumerator AUD\_LOOP\_ADC2DAC\_MAX

<a id="_CPPv419aud_loop_dtmf2dac_t"></a>

<a id="_CPPv319aud_loop_dtmf2dac_t"></a> <a id="_CPPv219aud_loop_dtmf2dac_t"></a> <a id="group__bk__api__aud__enum_1ga78dcff31918ae81fc035efcc8e6e8d25"></a> enum aud\_loop\_dtmf2dac\_t
:   *Values:*

    <a id="_CPPv4N19aud_loop_dtmf2dac_t25AUD_LOOP_DTMF2DAC_DISABLEE"></a>

    <a id="_CPPv3N19aud_loop_dtmf2dac_t25AUD_LOOP_DTMF2DAC_DISABLEE"></a> <a id="_CPPv2N19aud_loop_dtmf2dac_t25AUD_LOOP_DTMF2DAC_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga78dcff31918ae81fc035efcc8e6e8d25a883f7a3c8969a0f19e9f7eaddc445f08"></a> enumerator AUD\_LOOP\_DTMF2DAC\_DISABLE
    :   DTMF to DAC loop test disable

    <a id="_CPPv4N19aud_loop_dtmf2dac_t24AUD_LOOP_DTMF2DAC_ENABLEE"></a>

    <a id="_CPPv3N19aud_loop_dtmf2dac_t24AUD_LOOP_DTMF2DAC_ENABLEE"></a> <a id="_CPPv2N19aud_loop_dtmf2dac_t24AUD_LOOP_DTMF2DAC_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga78dcff31918ae81fc035efcc8e6e8d25a7c0a4573473a2ad81236dce41bf392bb"></a> enumerator AUD\_LOOP\_DTMF2DAC\_ENABLE
    :   DTMF to DAC loop test enable

    <a id="_CPPv4N19aud_loop_dtmf2dac_t21AUD_LOOP_DTMF2DAC_MAXE"></a>

    <a id="_CPPv3N19aud_loop_dtmf2dac_t21AUD_LOOP_DTMF2DAC_MAXE"></a> <a id="_CPPv2N19aud_loop_dtmf2dac_t21AUD_LOOP_DTMF2DAC_MAXE"></a> <a id="group__bk__api__aud__enum_1gga78dcff31918ae81fc035efcc8e6e8d25a66003f8c1ddede1fe4438576f6e9fabd"></a> enumerator AUD\_LOOP\_DTMF2DAC\_MAX

<a id="_CPPv419aud_agc_ng_enable_t"></a>

<a id="_CPPv319aud_agc_ng_enable_t"></a> <a id="_CPPv219aud_agc_ng_enable_t"></a> <a id="group__bk__api__aud__enum_1ga3f30f114a4eae1f7dd4bc03dd9b7581f"></a> enum aud\_agc\_ng\_enable\_t
:   *Values:*

    <a id="_CPPv4N19aud_agc_ng_enable_t18AUD_AGC_NG_DISABLEE"></a>

    <a id="_CPPv3N19aud_agc_ng_enable_t18AUD_AGC_NG_DISABLEE"></a> <a id="_CPPv2N19aud_agc_ng_enable_t18AUD_AGC_NG_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga3f30f114a4eae1f7dd4bc03dd9b7581fa06cc6e76c367ba18feafbfb2bcd7f63a"></a> enumerator AUD\_AGC\_NG\_DISABLE
    :   disable noise gating

    <a id="_CPPv4N19aud_agc_ng_enable_t17AUD_AGC_NG_ENABLEE"></a>

    <a id="_CPPv3N19aud_agc_ng_enable_t17AUD_AGC_NG_ENABLEE"></a> <a id="_CPPv2N19aud_agc_ng_enable_t17AUD_AGC_NG_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga3f30f114a4eae1f7dd4bc03dd9b7581fad8c46c257eaf84022eb684b75c720935"></a> enumerator AUD\_AGC\_NG\_ENABLE
    :   enable noise gating

    <a id="_CPPv4N19aud_agc_ng_enable_t14AUD_AGC_NG_MAXE"></a>

    <a id="_CPPv3N19aud_agc_ng_enable_t14AUD_AGC_NG_MAXE"></a> <a id="_CPPv2N19aud_agc_ng_enable_t14AUD_AGC_NG_MAXE"></a> <a id="group__bk__api__aud__enum_1gga3f30f114a4eae1f7dd4bc03dd9b7581fa667219a85547497d3b890b3a44841045"></a> enumerator AUD\_AGC\_NG\_MAX

<a id="_CPPv416aud_agc_method_t"></a>

<a id="_CPPv316aud_agc_method_t"></a> <a id="_CPPv216aud_agc_method_t"></a> <a id="group__bk__api__aud__enum_1ga566398b99f02741fe40b396901a0294d"></a> enum aud\_agc\_method\_t
:   *Values:*

    <a id="_CPPv4N16aud_agc_method_t22AUD_AGC_NG_METHOD_MUTEE"></a>

    <a id="_CPPv3N16aud_agc_method_t22AUD_AGC_NG_METHOD_MUTEE"></a> <a id="_CPPv2N16aud_agc_method_t22AUD_AGC_NG_METHOD_MUTEE"></a> <a id="group__bk__api__aud__enum_1gga566398b99f02741fe40b396901a0294da50fd6b1ea8fd1d23953efddd90faa79f"></a> enumerator AUD\_AGC\_NG\_METHOD\_MUTE
    :   mute or demute : default

    <a id="_CPPv4N16aud_agc_method_t24AUD_AGC_NG_METHOD_CREASEE"></a>

    <a id="_CPPv3N16aud_agc_method_t24AUD_AGC_NG_METHOD_CREASEE"></a> <a id="_CPPv2N16aud_agc_method_t24AUD_AGC_NG_METHOD_CREASEE"></a> <a id="group__bk__api__aud__enum_1gga566398b99f02741fe40b396901a0294daf7d2cc7a681b4db977cbd012a2a1a59a"></a> enumerator AUD\_AGC\_NG\_METHOD\_CREASE
    :   gradually increase or decrease gac

    <a id="_CPPv4N16aud_agc_method_t21AUD_AGC_NG_METHOD_MAXE"></a>

    <a id="_CPPv3N16aud_agc_method_t21AUD_AGC_NG_METHOD_MAXE"></a> <a id="_CPPv2N16aud_agc_method_t21AUD_AGC_NG_METHOD_MAXE"></a> <a id="group__bk__api__aud__enum_1gga566398b99f02741fe40b396901a0294daae3dbdc973f6a1aea3ae3aca608891b5"></a> enumerator AUD\_AGC\_NG\_METHOD\_MAX

<a id="_CPPv420aud_agc_decay_time_t"></a>

<a id="_CPPv320aud_agc_decay_time_t"></a> <a id="_CPPv220aud_agc_decay_time_t"></a> <a id="group__bk__api__aud__enum_1ga1070f34487509f67b5e4b9598e5b8ec4"></a> enum aud\_agc\_decay\_time\_t
:   *Values:*

    <a id="_CPPv4N20aud_agc_decay_time_t22AUD_AGC_DECAY_TIME_128E"></a>

    <a id="_CPPv3N20aud_agc_decay_time_t22AUD_AGC_DECAY_TIME_128E"></a> <a id="_CPPv2N20aud_agc_decay_time_t22AUD_AGC_DECAY_TIME_128E"></a> <a id="group__bk__api__aud__enum_1gga1070f34487509f67b5e4b9598e5b8ec4a939333a380e659203bbc1818a6560e87"></a> enumerator AUD\_AGC\_DECAY\_TIME\_128
    :   AGC decay time :128 2.7ms

    <a id="_CPPv4N20aud_agc_decay_time_t22AUD_AGC_DECAY_TIME_256E"></a>

    <a id="_CPPv3N20aud_agc_decay_time_t22AUD_AGC_DECAY_TIME_256E"></a> <a id="_CPPv2N20aud_agc_decay_time_t22AUD_AGC_DECAY_TIME_256E"></a> <a id="group__bk__api__aud__enum_1gga1070f34487509f67b5e4b9598e5b8ec4ac8cac9b1978639f00ed08c89da6c0283"></a> enumerator AUD\_AGC\_DECAY\_TIME\_256
    :   AGC decay time :256

    <a id="_CPPv4N20aud_agc_decay_time_t22AUD_AGC_DECAY_TIME_512E"></a>

    <a id="_CPPv3N20aud_agc_decay_time_t22AUD_AGC_DECAY_TIME_512E"></a> <a id="_CPPv2N20aud_agc_decay_time_t22AUD_AGC_DECAY_TIME_512E"></a> <a id="group__bk__api__aud__enum_1gga1070f34487509f67b5e4b9598e5b8ec4a83fd3a14b3122cdc43b195d3dfac3920"></a> enumerator AUD\_AGC\_DECAY\_TIME\_512
    :   AGC decay time :512

    <a id="_CPPv4N20aud_agc_decay_time_t23AUD_AGC_DECAY_TIME_1024E"></a>

    <a id="_CPPv3N20aud_agc_decay_time_t23AUD_AGC_DECAY_TIME_1024E"></a> <a id="_CPPv2N20aud_agc_decay_time_t23AUD_AGC_DECAY_TIME_1024E"></a> <a id="group__bk__api__aud__enum_1gga1070f34487509f67b5e4b9598e5b8ec4af98be5a87f0d9e424f0d04d5b3c9c7bc"></a> enumerator AUD\_AGC\_DECAY\_TIME\_1024
    :   AGC decay time :1024

    <a id="_CPPv4N20aud_agc_decay_time_t23AUD_AGC_DECAY_TIME_2048E"></a>

    <a id="_CPPv3N20aud_agc_decay_time_t23AUD_AGC_DECAY_TIME_2048E"></a> <a id="_CPPv2N20aud_agc_decay_time_t23AUD_AGC_DECAY_TIME_2048E"></a> <a id="group__bk__api__aud__enum_1gga1070f34487509f67b5e4b9598e5b8ec4ad1146fa00b83c01e14aa8a7484b4ac10"></a> enumerator AUD\_AGC\_DECAY\_TIME\_2048
    :   AGC decay time :2048

    <a id="_CPPv4N20aud_agc_decay_time_t23AUD_AGC_DECAY_TIME_4096E"></a>

    <a id="_CPPv3N20aud_agc_decay_time_t23AUD_AGC_DECAY_TIME_4096E"></a> <a id="_CPPv2N20aud_agc_decay_time_t23AUD_AGC_DECAY_TIME_4096E"></a> <a id="group__bk__api__aud__enum_1gga1070f34487509f67b5e4b9598e5b8ec4a1cbc3a33f438314d19fbe8ddd797c766"></a> enumerator AUD\_AGC\_DECAY\_TIME\_4096
    :   AGC decay time :4096

    <a id="_CPPv4N20aud_agc_decay_time_t23AUD_AGC_DECAY_TIME_8192E"></a>

    <a id="_CPPv3N20aud_agc_decay_time_t23AUD_AGC_DECAY_TIME_8192E"></a> <a id="_CPPv2N20aud_agc_decay_time_t23AUD_AGC_DECAY_TIME_8192E"></a> <a id="group__bk__api__aud__enum_1gga1070f34487509f67b5e4b9598e5b8ec4a8e0dad3cefd6a81bafd140a707fc9a45"></a> enumerator AUD\_AGC\_DECAY\_TIME\_8192
    :   AGC decay time :8192

    <a id="_CPPv4N20aud_agc_decay_time_t24AUD_AGC_DECAY_TIME_16384E"></a>

    <a id="_CPPv3N20aud_agc_decay_time_t24AUD_AGC_DECAY_TIME_16384E"></a> <a id="_CPPv2N20aud_agc_decay_time_t24AUD_AGC_DECAY_TIME_16384E"></a> <a id="group__bk__api__aud__enum_1gga1070f34487509f67b5e4b9598e5b8ec4a99411ca01fb200d73aef1a6e260210cc"></a> enumerator AUD\_AGC\_DECAY\_TIME\_16384
    :   AGC decay time :16384 340ms

    <a id="_CPPv4N20aud_agc_decay_time_t22AUD_AGC_DECAY_TIME_MAXE"></a>

    <a id="_CPPv3N20aud_agc_decay_time_t22AUD_AGC_DECAY_TIME_MAXE"></a> <a id="_CPPv2N20aud_agc_decay_time_t22AUD_AGC_DECAY_TIME_MAXE"></a> <a id="group__bk__api__aud__enum_1gga1070f34487509f67b5e4b9598e5b8ec4a815f6360d577f6ebb8c85be3ee1bc978"></a> enumerator AUD\_AGC\_DECAY\_TIME\_MAX

<a id="_CPPv421aud_agc_attack_time_t"></a>

<a id="_CPPv321aud_agc_attack_time_t"></a> <a id="_CPPv221aud_agc_attack_time_t"></a> <a id="group__bk__api__aud__enum_1ga80b58d510f606935847382219581aafe"></a> enum aud\_agc\_attack\_time\_t
:   *Values:*

    <a id="_CPPv4N21aud_agc_attack_time_t21AUD_AGC_ATTACK_TIME_8E"></a>

    <a id="_CPPv3N21aud_agc_attack_time_t21AUD_AGC_ATTACK_TIME_8E"></a> <a id="_CPPv2N21aud_agc_attack_time_t21AUD_AGC_ATTACK_TIME_8E"></a> <a id="group__bk__api__aud__enum_1gga80b58d510f606935847382219581aafea3f0c25e72afd72f116c22328d8c126d5"></a> enumerator AUD\_AGC\_ATTACK\_TIME\_8
    :   AGC attack time :8 0.1667ms

    <a id="_CPPv4N21aud_agc_attack_time_t22AUD_AGC_ATTACK_TIME_16E"></a>

    <a id="_CPPv3N21aud_agc_attack_time_t22AUD_AGC_ATTACK_TIME_16E"></a> <a id="_CPPv2N21aud_agc_attack_time_t22AUD_AGC_ATTACK_TIME_16E"></a> <a id="group__bk__api__aud__enum_1gga80b58d510f606935847382219581aafeaffb4c669ef719b9c8830747d87771c3d"></a> enumerator AUD\_AGC\_ATTACK\_TIME\_16
    :   AGC attack time :16

    <a id="_CPPv4N21aud_agc_attack_time_t22AUD_AGC_ATTACK_TIME_32E"></a>

    <a id="_CPPv3N21aud_agc_attack_time_t22AUD_AGC_ATTACK_TIME_32E"></a> <a id="_CPPv2N21aud_agc_attack_time_t22AUD_AGC_ATTACK_TIME_32E"></a> <a id="group__bk__api__aud__enum_1gga80b58d510f606935847382219581aafeae4b33c163daf20bd3d5b161bff560a53"></a> enumerator AUD\_AGC\_ATTACK\_TIME\_32
    :   AGC attack time :32

    <a id="_CPPv4N21aud_agc_attack_time_t22AUD_AGC_ATTACK_TIME_64E"></a>

    <a id="_CPPv3N21aud_agc_attack_time_t22AUD_AGC_ATTACK_TIME_64E"></a> <a id="_CPPv2N21aud_agc_attack_time_t22AUD_AGC_ATTACK_TIME_64E"></a> <a id="group__bk__api__aud__enum_1gga80b58d510f606935847382219581aafeab6c1afc2d21ea909303a22102513868e"></a> enumerator AUD\_AGC\_ATTACK\_TIME\_64
    :   AGC attack time :64

    <a id="_CPPv4N21aud_agc_attack_time_t23AUD_AGC_ATTACK_TIME_128E"></a>

    <a id="_CPPv3N21aud_agc_attack_time_t23AUD_AGC_ATTACK_TIME_128E"></a> <a id="_CPPv2N21aud_agc_attack_time_t23AUD_AGC_ATTACK_TIME_128E"></a> <a id="group__bk__api__aud__enum_1gga80b58d510f606935847382219581aafea4228fbc9795a3912f0d4c59dd8e1ff20"></a> enumerator AUD\_AGC\_ATTACK\_TIME\_128
    :   AGC attack time :128

    <a id="_CPPv4N21aud_agc_attack_time_t23AUD_AGC_ATTACK_TIME_256E"></a>

    <a id="_CPPv3N21aud_agc_attack_time_t23AUD_AGC_ATTACK_TIME_256E"></a> <a id="_CPPv2N21aud_agc_attack_time_t23AUD_AGC_ATTACK_TIME_256E"></a> <a id="group__bk__api__aud__enum_1gga80b58d510f606935847382219581aafead5373e5142fe1c3d5611b4d82a707051"></a> enumerator AUD\_AGC\_ATTACK\_TIME\_256
    :   AGC attack time :256

    <a id="_CPPv4N21aud_agc_attack_time_t23AUD_AGC_ATTACK_TIME_512E"></a>

    <a id="_CPPv3N21aud_agc_attack_time_t23AUD_AGC_ATTACK_TIME_512E"></a> <a id="_CPPv2N21aud_agc_attack_time_t23AUD_AGC_ATTACK_TIME_512E"></a> <a id="group__bk__api__aud__enum_1gga80b58d510f606935847382219581aafea86016c5bc92b31f8206b724894072f6e"></a> enumerator AUD\_AGC\_ATTACK\_TIME\_512
    :   AGC attack time :512

    <a id="_CPPv4N21aud_agc_attack_time_t24AUD_AGC_ATTACK_TIME_1024E"></a>

    <a id="_CPPv3N21aud_agc_attack_time_t24AUD_AGC_ATTACK_TIME_1024E"></a> <a id="_CPPv2N21aud_agc_attack_time_t24AUD_AGC_ATTACK_TIME_1024E"></a> <a id="group__bk__api__aud__enum_1gga80b58d510f606935847382219581aafea0989f1a438c9ac4497e7075b8c31befc"></a> enumerator AUD\_AGC\_ATTACK\_TIME\_1024
    :   AGC attack time :1024 21 ms

    <a id="_CPPv4N21aud_agc_attack_time_t23AUD_AGC_ATTACK_TIME_MAXE"></a>

    <a id="_CPPv3N21aud_agc_attack_time_t23AUD_AGC_ATTACK_TIME_MAXE"></a> <a id="_CPPv2N21aud_agc_attack_time_t23AUD_AGC_ATTACK_TIME_MAXE"></a> <a id="group__bk__api__aud__enum_1gga80b58d510f606935847382219581aafea3da800cb4d40afae427de8ad3344500d"></a> enumerator AUD\_AGC\_ATTACK\_TIME\_MAX

<a id="_CPPv418aud_agc_iir_coef_t"></a>

<a id="_CPPv318aud_agc_iir_coef_t"></a> <a id="_CPPv218aud_agc_iir_coef_t"></a> <a id="group__bk__api__aud__enum_1ga993473f7be2953771cbaf110ed09297a"></a> enum aud\_agc\_iir\_coef\_t
:   *Values:*

    <a id="_CPPv4N18aud_agc_iir_coef_t21AUD_AGC_IIR_COEF_1_32E"></a>

    <a id="_CPPv3N18aud_agc_iir_coef_t21AUD_AGC_IIR_COEF_1_32E"></a> <a id="_CPPv2N18aud_agc_iir_coef_t21AUD_AGC_IIR_COEF_1_32E"></a> <a id="group__bk__api__aud__enum_1gga993473f7be2953771cbaf110ed09297aad36cf31de6fe8838858e7148918230b3"></a> enumerator AUD\_AGC\_IIR\_COEF\_1\_32
    :   AGC IRR coefficient : 1/32

    <a id="_CPPv4N18aud_agc_iir_coef_t21AUD_AGC_IIR_COEF_1_64E"></a>

    <a id="_CPPv3N18aud_agc_iir_coef_t21AUD_AGC_IIR_COEF_1_64E"></a> <a id="_CPPv2N18aud_agc_iir_coef_t21AUD_AGC_IIR_COEF_1_64E"></a> <a id="group__bk__api__aud__enum_1gga993473f7be2953771cbaf110ed09297aa807394be8189532b85754ea0d0f2b15f"></a> enumerator AUD\_AGC\_IIR\_COEF\_1\_64
    :   AGC IRR coefficient : 1/64

    <a id="_CPPv4N18aud_agc_iir_coef_t22AUD_AGC_IIR_COEF_1_128E"></a>

    <a id="_CPPv3N18aud_agc_iir_coef_t22AUD_AGC_IIR_COEF_1_128E"></a> <a id="_CPPv2N18aud_agc_iir_coef_t22AUD_AGC_IIR_COEF_1_128E"></a> <a id="group__bk__api__aud__enum_1gga993473f7be2953771cbaf110ed09297aae5550a7766ac77672f855f9a4df49f33"></a> enumerator AUD\_AGC\_IIR\_COEF\_1\_128
    :   AGC IRR coefficient : 1/128

    <a id="_CPPv4N18aud_agc_iir_coef_t22AUD_AGC_IIR_COEF_1_256E"></a>

    <a id="_CPPv3N18aud_agc_iir_coef_t22AUD_AGC_IIR_COEF_1_256E"></a> <a id="_CPPv2N18aud_agc_iir_coef_t22AUD_AGC_IIR_COEF_1_256E"></a> <a id="group__bk__api__aud__enum_1gga993473f7be2953771cbaf110ed09297aa92101c4d2b527b64b0e092d2ac59c92b"></a> enumerator AUD\_AGC\_IIR\_COEF\_1\_256
    :   AGC IRR coefficient : 1/256

    <a id="_CPPv4N18aud_agc_iir_coef_t22AUD_AGC_IIR_COEF_1_512E"></a>

    <a id="_CPPv3N18aud_agc_iir_coef_t22AUD_AGC_IIR_COEF_1_512E"></a> <a id="_CPPv2N18aud_agc_iir_coef_t22AUD_AGC_IIR_COEF_1_512E"></a> <a id="group__bk__api__aud__enum_1gga993473f7be2953771cbaf110ed09297aa4d1dbdccde5097a383a4e4df08c8201e"></a> enumerator AUD\_AGC\_IIR\_COEF\_1\_512
    :   AGC IRR coefficient : 1/512

    <a id="_CPPv4N18aud_agc_iir_coef_t23AUD_AGC_IIR_COEF_1_1024E"></a>

    <a id="_CPPv3N18aud_agc_iir_coef_t23AUD_AGC_IIR_COEF_1_1024E"></a> <a id="_CPPv2N18aud_agc_iir_coef_t23AUD_AGC_IIR_COEF_1_1024E"></a> <a id="group__bk__api__aud__enum_1gga993473f7be2953771cbaf110ed09297aad4625b66b90daa79d0486a52c05dab34"></a> enumerator AUD\_AGC\_IIR\_COEF\_1\_1024
    :   AGC IRR coefficient : 1/1024

    <a id="_CPPv4N18aud_agc_iir_coef_t23AUD_AGC_IIR_COEF_1_2048E"></a>

    <a id="_CPPv3N18aud_agc_iir_coef_t23AUD_AGC_IIR_COEF_1_2048E"></a> <a id="_CPPv2N18aud_agc_iir_coef_t23AUD_AGC_IIR_COEF_1_2048E"></a> <a id="group__bk__api__aud__enum_1gga993473f7be2953771cbaf110ed09297aadfbbeb08b8f0455f9e840b1e8720a17b"></a> enumerator AUD\_AGC\_IIR\_COEF\_1\_2048
    :   AGC IRR coefficient : 1/2048

    <a id="_CPPv4N18aud_agc_iir_coef_t23AUD_AGC_IIR_COEF_1_4096E"></a>

    <a id="_CPPv3N18aud_agc_iir_coef_t23AUD_AGC_IIR_COEF_1_4096E"></a> <a id="_CPPv2N18aud_agc_iir_coef_t23AUD_AGC_IIR_COEF_1_4096E"></a> <a id="group__bk__api__aud__enum_1gga993473f7be2953771cbaf110ed09297aace8fa494d07d54c96628515149679eb2"></a> enumerator AUD\_AGC\_IIR\_COEF\_1\_4096
    :   AGC IRR coefficient : 1/4096

    <a id="_CPPv4N18aud_agc_iir_coef_t20AUD_AGC_IIR_COEF_MAXE"></a>

    <a id="_CPPv3N18aud_agc_iir_coef_t20AUD_AGC_IIR_COEF_MAXE"></a> <a id="_CPPv2N18aud_agc_iir_coef_t20AUD_AGC_IIR_COEF_MAXE"></a> <a id="group__bk__api__aud__enum_1gga993473f7be2953771cbaf110ed09297aaf7cc58f284ef24ce21bb6841a60149e4"></a> enumerator AUD\_AGC\_IIR\_COEF\_MAX

<a id="_CPPv416aud_agc_enable_t"></a>

<a id="_CPPv316aud_agc_enable_t"></a> <a id="_CPPv216aud_agc_enable_t"></a> <a id="group__bk__api__aud__enum_1gada5717bdbc67506dbbbb9d8ff6a1ccde"></a> enum aud\_agc\_enable\_t
:   *Values:*

    <a id="_CPPv4N16aud_agc_enable_t15AUD_AGC_DISABLEE"></a>

    <a id="_CPPv3N16aud_agc_enable_t15AUD_AGC_DISABLEE"></a> <a id="_CPPv2N16aud_agc_enable_t15AUD_AGC_DISABLEE"></a> <a id="group__bk__api__aud__enum_1ggada5717bdbc67506dbbbb9d8ff6a1ccdea3930037070bcafda822ba7249dd62bfc"></a> enumerator AUD\_AGC\_DISABLE
    :   disable AGC

    <a id="_CPPv4N16aud_agc_enable_t14AUD_AGC_ENABLEE"></a>

    <a id="_CPPv3N16aud_agc_enable_t14AUD_AGC_ENABLEE"></a> <a id="_CPPv2N16aud_agc_enable_t14AUD_AGC_ENABLEE"></a> <a id="group__bk__api__aud__enum_1ggada5717bdbc67506dbbbb9d8ff6a1ccdea0a9d442523fb662761075d333cda1f0f"></a> enumerator AUD\_AGC\_ENABLE
    :   enable AGC

    <a id="_CPPv4N16aud_agc_enable_t11AUD_AGC_MAXE"></a>

    <a id="_CPPv3N16aud_agc_enable_t11AUD_AGC_MAXE"></a> <a id="_CPPv2N16aud_agc_enable_t11AUD_AGC_MAXE"></a> <a id="group__bk__api__aud__enum_1ggada5717bdbc67506dbbbb9d8ff6a1ccdea515cb3543c1eb574c2772d7f4bb85202"></a> enumerator AUD\_AGC\_MAX

<a id="_CPPv423aud_agc_manual_pga_en_t"></a>

<a id="_CPPv323aud_agc_manual_pga_en_t"></a> <a id="_CPPv223aud_agc_manual_pga_en_t"></a> <a id="group__bk__api__aud__enum_1gacec49eabbf13df25f4c6763357f1da3c"></a> enum aud\_agc\_manual\_pga\_en\_t
:   *Values:*

    <a id="_CPPv4N23aud_agc_manual_pga_en_t26AUD_GAC_MANUAL_PGA_DISABLEE"></a>

    <a id="_CPPv3N23aud_agc_manual_pga_en_t26AUD_GAC_MANUAL_PGA_DISABLEE"></a> <a id="_CPPv2N23aud_agc_manual_pga_en_t26AUD_GAC_MANUAL_PGA_DISABLEE"></a> <a id="group__bk__api__aud__enum_1ggacec49eabbf13df25f4c6763357f1da3ca0f9b37c014aaa606d5ab36eda5719a5c"></a> enumerator AUD\_GAC\_MANUAL\_PGA\_DISABLE
    :   disable AGC manual set pga

    <a id="_CPPv4N23aud_agc_manual_pga_en_t25AUD_GAC_MANUAL_PGA_ENABLEE"></a>

    <a id="_CPPv3N23aud_agc_manual_pga_en_t25AUD_GAC_MANUAL_PGA_ENABLEE"></a> <a id="_CPPv2N23aud_agc_manual_pga_en_t25AUD_GAC_MANUAL_PGA_ENABLEE"></a> <a id="group__bk__api__aud__enum_1ggacec49eabbf13df25f4c6763357f1da3cac0f24758aa305d3b469e36573bd91298"></a> enumerator AUD\_GAC\_MANUAL\_PGA\_ENABLE
    :   enable AGC manual set pga

    <a id="_CPPv4N23aud_agc_manual_pga_en_t22AUD_GAC_MANUAL_PGA_MAXE"></a>

    <a id="_CPPv3N23aud_agc_manual_pga_en_t22AUD_GAC_MANUAL_PGA_MAXE"></a> <a id="_CPPv2N23aud_agc_manual_pga_en_t22AUD_GAC_MANUAL_PGA_MAXE"></a> <a id="group__bk__api__aud__enum_1ggacec49eabbf13df25f4c6763357f1da3cad47b7a1be1e4e2d030c86eed82874dc9"></a> enumerator AUD\_GAC\_MANUAL\_PGA\_MAX

<a id="_CPPv416aud_adc_enable_t"></a>

<a id="_CPPv316aud_adc_enable_t"></a> <a id="_CPPv216aud_adc_enable_t"></a> <a id="group__bk__api__aud__enum_1ga5fac3d82b546d00dcc8374bb76e7c7ea"></a> enum aud\_adc\_enable\_t
:   *Values:*

    <a id="_CPPv4N16aud_adc_enable_t15AUD_ADC_DISABLEE"></a>

    <a id="_CPPv3N16aud_adc_enable_t15AUD_ADC_DISABLEE"></a> <a id="_CPPv2N16aud_adc_enable_t15AUD_ADC_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga5fac3d82b546d00dcc8374bb76e7c7eaaafae5b202dd1b9af7005ce77ee5a590d"></a> enumerator AUD\_ADC\_DISABLE
    :   disable adc

    <a id="_CPPv4N16aud_adc_enable_t14AUD_ADC_ENABLEE"></a>

    <a id="_CPPv3N16aud_adc_enable_t14AUD_ADC_ENABLEE"></a> <a id="_CPPv2N16aud_adc_enable_t14AUD_ADC_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga5fac3d82b546d00dcc8374bb76e7c7eaa1092cc5147160b0dd057ba77bc5b6187"></a> enumerator AUD\_ADC\_ENABLE
    :   enable adc

    <a id="_CPPv4N16aud_adc_enable_t18AUD_ADC_ENABLE_MAXE"></a>

    <a id="_CPPv3N16aud_adc_enable_t18AUD_ADC_ENABLE_MAXE"></a> <a id="_CPPv2N16aud_adc_enable_t18AUD_ADC_ENABLE_MAXE"></a> <a id="group__bk__api__aud__enum_1gga5fac3d82b546d00dcc8374bb76e7c7eaa5b67fae3908a93f23d45b0336eae6513"></a> enumerator AUD\_ADC\_ENABLE\_MAX

<a id="_CPPv421aud_adc_line_enable_t"></a>

<a id="_CPPv321aud_adc_line_enable_t"></a> <a id="_CPPv221aud_adc_line_enable_t"></a> <a id="group__bk__api__aud__enum_1ga07752c350150d50827848f0725313f43"></a> enum aud\_adc\_line\_enable\_t
:   *Values:*

    <a id="_CPPv4N21aud_adc_line_enable_t20AUD_ADC_LINE_DISABLEE"></a>

    <a id="_CPPv3N21aud_adc_line_enable_t20AUD_ADC_LINE_DISABLEE"></a> <a id="_CPPv2N21aud_adc_line_enable_t20AUD_ADC_LINE_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga07752c350150d50827848f0725313f43a5c3ffa65515f4194e3d0b7a235a17817"></a> enumerator AUD\_ADC\_LINE\_DISABLE
    :   disable line in

    <a id="_CPPv4N21aud_adc_line_enable_t19AUD_ADC_LINE_ENABLEE"></a>

    <a id="_CPPv3N21aud_adc_line_enable_t19AUD_ADC_LINE_ENABLEE"></a> <a id="_CPPv2N21aud_adc_line_enable_t19AUD_ADC_LINE_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga07752c350150d50827848f0725313f43a555b8456248e5422db14568d49ef88e1"></a> enumerator AUD\_ADC\_LINE\_ENABLE
    :   enable line in

    <a id="_CPPv4N21aud_adc_line_enable_t23AUD_ADC_LINE_ENABLE_MAXE"></a>

    <a id="_CPPv3N21aud_adc_line_enable_t23AUD_ADC_LINE_ENABLE_MAXE"></a> <a id="_CPPv2N21aud_adc_line_enable_t23AUD_ADC_LINE_ENABLE_MAXE"></a> <a id="group__bk__api__aud__enum_1gga07752c350150d50827848f0725313f43a661dda0162bde99946801c3eca0da27e"></a> enumerator AUD\_ADC\_LINE\_ENABLE\_MAX

<a id="_CPPv416aud_mic_enable_t"></a>

<a id="_CPPv316aud_mic_enable_t"></a> <a id="_CPPv216aud_mic_enable_t"></a> <a id="group__bk__api__aud__enum_1ga07d499e76692573980b02ea6e98ea464"></a> enum aud\_mic\_enable\_t
:   *Values:*

    <a id="_CPPv4N16aud_mic_enable_t15AUD_MIC_DISABLEE"></a>

    <a id="_CPPv3N16aud_mic_enable_t15AUD_MIC_DISABLEE"></a> <a id="_CPPv2N16aud_mic_enable_t15AUD_MIC_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga07d499e76692573980b02ea6e98ea464a77182edadda497a9824951219e9e674b"></a> enumerator AUD\_MIC\_DISABLE
    :   disable all mic

    <a id="_CPPv4N16aud_mic_enable_t19AUD_MIC_MIC1_ENABLEE"></a>

    <a id="_CPPv3N16aud_mic_enable_t19AUD_MIC_MIC1_ENABLEE"></a> <a id="_CPPv2N16aud_mic_enable_t19AUD_MIC_MIC1_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga07d499e76692573980b02ea6e98ea464a792e8c497bcc888e653f880c10474fa3"></a> enumerator AUD\_MIC\_MIC1\_ENABLE
    :   enable mic1

    <a id="_CPPv4N16aud_mic_enable_t19AUD_MIC_MIC2_ENABLEE"></a>

    <a id="_CPPv3N16aud_mic_enable_t19AUD_MIC_MIC2_ENABLEE"></a> <a id="_CPPv2N16aud_mic_enable_t19AUD_MIC_MIC2_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga07d499e76692573980b02ea6e98ea464a62fcb362f9872644c20d3de26eb172c8"></a> enumerator AUD\_MIC\_MIC2\_ENABLE
    :   enable mic2

    <a id="_CPPv4N16aud_mic_enable_t18AUD_MIC_ALL_ENABLEE"></a>

    <a id="_CPPv3N16aud_mic_enable_t18AUD_MIC_ALL_ENABLEE"></a> <a id="_CPPv2N16aud_mic_enable_t18AUD_MIC_ALL_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga07d499e76692573980b02ea6e98ea464a5bc7f1cb30841928611f52c03743f83a"></a> enumerator AUD\_MIC\_ALL\_ENABLE
    :   enable all mic

    <a id="_CPPv4N16aud_mic_enable_t11AUD_MIC_MAXE"></a>

    <a id="_CPPv3N16aud_mic_enable_t11AUD_MIC_MAXE"></a> <a id="_CPPv2N16aud_mic_enable_t11AUD_MIC_MAXE"></a> <a id="group__bk__api__aud__enum_1gga07d499e76692573980b02ea6e98ea464a9fde8a73ceb8c00892f20b9f84698257"></a> enumerator AUD\_MIC\_MAX

<a id="_CPPv412aud_mic_id_t"></a>

<a id="_CPPv312aud_mic_id_t"></a> <a id="_CPPv212aud_mic_id_t"></a> <a id="group__bk__api__aud__enum_1gac88edcb1df8da15308c089432af225f2"></a> enum aud\_mic\_id\_t
:   *Values:*

    <a id="_CPPv4N12aud_mic_id_t12AUD_MIC_MIC1E"></a>

    <a id="_CPPv3N12aud_mic_id_t12AUD_MIC_MIC1E"></a> <a id="_CPPv2N12aud_mic_id_t12AUD_MIC_MIC1E"></a> <a id="group__bk__api__aud__enum_1ggac88edcb1df8da15308c089432af225f2a784090839d776dd3c0a501a527599572"></a> enumerator AUD\_MIC\_MIC1
    :   enable mic1

    <a id="_CPPv4N12aud_mic_id_t12AUD_MIC_MIC2E"></a>

    <a id="_CPPv3N12aud_mic_id_t12AUD_MIC_MIC2E"></a> <a id="_CPPv2N12aud_mic_id_t12AUD_MIC_MIC2E"></a> <a id="group__bk__api__aud__enum_1ggac88edcb1df8da15308c089432af225f2aa5062be04736f3bd28ad7dfda905fd73"></a> enumerator AUD\_MIC\_MIC2
    :   enable mic2

    <a id="_CPPv4N12aud_mic_id_t12AUD_MIC_BOTHE"></a>

    <a id="_CPPv3N12aud_mic_id_t12AUD_MIC_BOTHE"></a> <a id="_CPPv2N12aud_mic_id_t12AUD_MIC_BOTHE"></a> <a id="group__bk__api__aud__enum_1ggac88edcb1df8da15308c089432af225f2a7f5d9368ed9b2177ff0fdf142927fe6b"></a> enumerator AUD\_MIC\_BOTH
    :   enable mic1 and mic2

<a id="_CPPv420aud_gac_noise_tout_t"></a>

<a id="_CPPv320aud_gac_noise_tout_t"></a> <a id="_CPPv220aud_gac_noise_tout_t"></a> <a id="group__bk__api__aud__enum_1gad40273c727ea3d6d03fb66588069f257"></a> enum aud\_gac\_noise\_tout\_t
:   *Values:*

    <a id="_CPPv4N20aud_gac_noise_tout_t20AUD_GAC_NOISE_TOUT_0E"></a>

    <a id="_CPPv3N20aud_gac_noise_tout_t20AUD_GAC_NOISE_TOUT_0E"></a> <a id="_CPPv2N20aud_gac_noise_tout_t20AUD_GAC_NOISE_TOUT_0E"></a> <a id="group__bk__api__aud__enum_1ggad40273c727ea3d6d03fb66588069f257a923ccd0d755c08d90d47a46d9f158052"></a> enumerator AUD\_GAC\_NOISE\_TOUT\_0
    :   AGC noise tout: 0 0ms

    <a id="_CPPv4N20aud_gac_noise_tout_t20AUD_GAC_NOISE_TOUT_4E"></a>

    <a id="_CPPv3N20aud_gac_noise_tout_t20AUD_GAC_NOISE_TOUT_4E"></a> <a id="_CPPv2N20aud_gac_noise_tout_t20AUD_GAC_NOISE_TOUT_4E"></a> <a id="group__bk__api__aud__enum_1ggad40273c727ea3d6d03fb66588069f257afd0a3fb2c0bba41955113ba28f1f18f0"></a> enumerator AUD\_GAC\_NOISE\_TOUT\_4
    :   AGC noise tout: 4 0.5ms

    <a id="_CPPv4N20aud_gac_noise_tout_t20AUD_GAC_NOISE_TOUT_8E"></a>

    <a id="_CPPv3N20aud_gac_noise_tout_t20AUD_GAC_NOISE_TOUT_8E"></a> <a id="_CPPv2N20aud_gac_noise_tout_t20AUD_GAC_NOISE_TOUT_8E"></a> <a id="group__bk__api__aud__enum_1ggad40273c727ea3d6d03fb66588069f257aba8a0ba868d4f6dd56b8ef669235e8b0"></a> enumerator AUD\_GAC\_NOISE\_TOUT\_8
    :   AGC noise tout: 8

    <a id="_CPPv4N20aud_gac_noise_tout_t21AUD_GAC_NOISE_TOUT_16E"></a>

    <a id="_CPPv3N20aud_gac_noise_tout_t21AUD_GAC_NOISE_TOUT_16E"></a> <a id="_CPPv2N20aud_gac_noise_tout_t21AUD_GAC_NOISE_TOUT_16E"></a> <a id="group__bk__api__aud__enum_1ggad40273c727ea3d6d03fb66588069f257aa14da293f4f2b60ad8d416aebd237b34"></a> enumerator AUD\_GAC\_NOISE\_TOUT\_16
    :   AGC noise tout: 16

    <a id="_CPPv4N20aud_gac_noise_tout_t21AUD_GAC_NOISE_TOUT_32E"></a>

    <a id="_CPPv3N20aud_gac_noise_tout_t21AUD_GAC_NOISE_TOUT_32E"></a> <a id="_CPPv2N20aud_gac_noise_tout_t21AUD_GAC_NOISE_TOUT_32E"></a> <a id="group__bk__api__aud__enum_1ggad40273c727ea3d6d03fb66588069f257a28b22d97d93491c4a2803dd60887fed3"></a> enumerator AUD\_GAC\_NOISE\_TOUT\_32
    :   AGC noise tout: 32

    <a id="_CPPv4N20aud_gac_noise_tout_t21AUD_GAC_NOISE_TOUT_64E"></a>

    <a id="_CPPv3N20aud_gac_noise_tout_t21AUD_GAC_NOISE_TOUT_64E"></a> <a id="_CPPv2N20aud_gac_noise_tout_t21AUD_GAC_NOISE_TOUT_64E"></a> <a id="group__bk__api__aud__enum_1ggad40273c727ea3d6d03fb66588069f257a39ee43f5d27fe728f276e8bb386c6a55"></a> enumerator AUD\_GAC\_NOISE\_TOUT\_64
    :   AGC noise tout: 64

    <a id="_CPPv4N20aud_gac_noise_tout_t22AUD_GAC_NOISE_TOUT_128E"></a>

    <a id="_CPPv3N20aud_gac_noise_tout_t22AUD_GAC_NOISE_TOUT_128E"></a> <a id="_CPPv2N20aud_gac_noise_tout_t22AUD_GAC_NOISE_TOUT_128E"></a> <a id="group__bk__api__aud__enum_1ggad40273c727ea3d6d03fb66588069f257a8f95df8e2e3df7735ac34591396cfed8"></a> enumerator AUD\_GAC\_NOISE\_TOUT\_128
    :   AGC noise tout: 128

    <a id="_CPPv4N20aud_gac_noise_tout_t22AUD_GAC_NOISE_TOUT_256E"></a>

    <a id="_CPPv3N20aud_gac_noise_tout_t22AUD_GAC_NOISE_TOUT_256E"></a> <a id="_CPPv2N20aud_gac_noise_tout_t22AUD_GAC_NOISE_TOUT_256E"></a> <a id="group__bk__api__aud__enum_1ggad40273c727ea3d6d03fb66588069f257a8663eac3a1089515202000cfe7a74970"></a> enumerator AUD\_GAC\_NOISE\_TOUT\_256
    :   AGC noise tout: 256 32ms

    <a id="_CPPv4N20aud_gac_noise_tout_t22AUD_GAC_NOISE_TOUT_MAXE"></a>

    <a id="_CPPv3N20aud_gac_noise_tout_t22AUD_GAC_NOISE_TOUT_MAXE"></a> <a id="_CPPv2N20aud_gac_noise_tout_t22AUD_GAC_NOISE_TOUT_MAXE"></a> <a id="group__bk__api__aud__enum_1ggad40273c727ea3d6d03fb66588069f257ace136d9c3714fd8a35ba3e741fdbf91f"></a> enumerator AUD\_GAC\_NOISE\_TOUT\_MAX

<a id="_CPPv418aud_gac_high_dur_t"></a>

<a id="_CPPv318aud_gac_high_dur_t"></a> <a id="_CPPv218aud_gac_high_dur_t"></a> <a id="group__bk__api__aud__enum_1gabc8becf0d55841a2277c75fb4d80e16c"></a> enum aud\_gac\_high\_dur\_t
:   *Values:*

    <a id="_CPPv4N18aud_gac_high_dur_t18AUD_GAC_HIGH_DUR_0E"></a>

    <a id="_CPPv3N18aud_gac_high_dur_t18AUD_GAC_HIGH_DUR_0E"></a> <a id="_CPPv2N18aud_gac_high_dur_t18AUD_GAC_HIGH_DUR_0E"></a> <a id="group__bk__api__aud__enum_1ggabc8becf0d55841a2277c75fb4d80e16ca614544ed6af7f3899f54ee69df63767c"></a> enumerator AUD\_GAC\_HIGH\_DUR\_0
    :   AGC 0 ms，as soon as MIC\_RSSI value higher than NOISE\_HIGH，Noise gating work，leave off noise status

    <a id="_CPPv4N18aud_gac_high_dur_t18AUD_GAC_HIGH_DUR_4E"></a>

    <a id="_CPPv3N18aud_gac_high_dur_t18AUD_GAC_HIGH_DUR_4E"></a> <a id="_CPPv2N18aud_gac_high_dur_t18AUD_GAC_HIGH_DUR_4E"></a> <a id="group__bk__api__aud__enum_1ggabc8becf0d55841a2277c75fb4d80e16ca558985df0fa6632c2dbd8332fcffd558"></a> enumerator AUD\_GAC\_HIGH\_DUR\_4
    :   AGC high duration: 4 0.5ms

    <a id="_CPPv4N18aud_gac_high_dur_t18AUD_GAC_HIGH_DUR_8E"></a>

    <a id="_CPPv3N18aud_gac_high_dur_t18AUD_GAC_HIGH_DUR_8E"></a> <a id="_CPPv2N18aud_gac_high_dur_t18AUD_GAC_HIGH_DUR_8E"></a> <a id="group__bk__api__aud__enum_1ggabc8becf0d55841a2277c75fb4d80e16cab24eafda70186ce2ba0e8bd28a66efda"></a> enumerator AUD\_GAC\_HIGH\_DUR\_8
    :   AGC high duration: 8

    <a id="_CPPv4N18aud_gac_high_dur_t19AUD_GAC_HIGH_DUR_16E"></a>

    <a id="_CPPv3N18aud_gac_high_dur_t19AUD_GAC_HIGH_DUR_16E"></a> <a id="_CPPv2N18aud_gac_high_dur_t19AUD_GAC_HIGH_DUR_16E"></a> <a id="group__bk__api__aud__enum_1ggabc8becf0d55841a2277c75fb4d80e16cae9a3cef9a62f3c1b8a3ab5442cdfc8e2"></a> enumerator AUD\_GAC\_HIGH\_DUR\_16
    :   AGC high duration: 16

    <a id="_CPPv4N18aud_gac_high_dur_t19AUD_GAC_HIGH_DUR_32E"></a>

    <a id="_CPPv3N18aud_gac_high_dur_t19AUD_GAC_HIGH_DUR_32E"></a> <a id="_CPPv2N18aud_gac_high_dur_t19AUD_GAC_HIGH_DUR_32E"></a> <a id="group__bk__api__aud__enum_1ggabc8becf0d55841a2277c75fb4d80e16ca1c958ed23fa5c8adb4c12c51bc45746c"></a> enumerator AUD\_GAC\_HIGH\_DUR\_32
    :   AGC high duration: 32

    <a id="_CPPv4N18aud_gac_high_dur_t19AUD_GAC_HIGH_DUR_64E"></a>

    <a id="_CPPv3N18aud_gac_high_dur_t19AUD_GAC_HIGH_DUR_64E"></a> <a id="_CPPv2N18aud_gac_high_dur_t19AUD_GAC_HIGH_DUR_64E"></a> <a id="group__bk__api__aud__enum_1ggabc8becf0d55841a2277c75fb4d80e16caaae0b7b604675c196cf0e630e7af7060"></a> enumerator AUD\_GAC\_HIGH\_DUR\_64
    :   AGC high duration: 64

    <a id="_CPPv4N18aud_gac_high_dur_t20AUD_GAC_HIGH_DUR_128E"></a>

    <a id="_CPPv3N18aud_gac_high_dur_t20AUD_GAC_HIGH_DUR_128E"></a> <a id="_CPPv2N18aud_gac_high_dur_t20AUD_GAC_HIGH_DUR_128E"></a> <a id="group__bk__api__aud__enum_1ggabc8becf0d55841a2277c75fb4d80e16ca46b50825181b05f74c0adf10bda967fb"></a> enumerator AUD\_GAC\_HIGH\_DUR\_128
    :   AGC high duration: 128

    <a id="_CPPv4N18aud_gac_high_dur_t20AUD_GAC_HIGH_DUR_256E"></a>

    <a id="_CPPv3N18aud_gac_high_dur_t20AUD_GAC_HIGH_DUR_256E"></a> <a id="_CPPv2N18aud_gac_high_dur_t20AUD_GAC_HIGH_DUR_256E"></a> <a id="group__bk__api__aud__enum_1ggabc8becf0d55841a2277c75fb4d80e16ca658d1e4243b96f71c37947c0175287a2"></a> enumerator AUD\_GAC\_HIGH\_DUR\_256
    :   AGC high duration: 256 32ms

    <a id="_CPPv4N18aud_gac_high_dur_t20AUD_GAC_HIGH_DUR_MAXE"></a>

    <a id="_CPPv3N18aud_gac_high_dur_t20AUD_GAC_HIGH_DUR_MAXE"></a> <a id="_CPPv2N18aud_gac_high_dur_t20AUD_GAC_HIGH_DUR_MAXE"></a> <a id="group__bk__api__aud__enum_1ggabc8becf0d55841a2277c75fb4d80e16ca7c16c41dcc0440b2f21578e024e98eeb"></a> enumerator AUD\_GAC\_HIGH\_DUR\_MAX

<a id="_CPPv417aud_gac_low_dur_t"></a>

<a id="_CPPv317aud_gac_low_dur_t"></a> <a id="_CPPv217aud_gac_low_dur_t"></a> <a id="group__bk__api__aud__enum_1gad6db7972d03b0d2579936215f22cc97d"></a> enum aud\_gac\_low\_dur\_t
:   *Values:*

    <a id="_CPPv4N17aud_gac_low_dur_t17AUD_GAC_LOW_DUR_0E"></a>

    <a id="_CPPv3N17aud_gac_low_dur_t17AUD_GAC_LOW_DUR_0E"></a> <a id="_CPPv2N17aud_gac_low_dur_t17AUD_GAC_LOW_DUR_0E"></a> <a id="group__bk__api__aud__enum_1ggad6db7972d03b0d2579936215f22cc97da766a7e378c53ecab2bdeb66d666a6ada"></a> enumerator AUD\_GAC\_LOW\_DUR\_0
    :   AGC 0 ms，as soon as MIC\_RSSI value lower than NOISE\_HIGH，Noise gating work，leave off noise status

    <a id="_CPPv4N17aud_gac_low_dur_t17AUD_GAC_LOW_DUR_4E"></a>

    <a id="_CPPv3N17aud_gac_low_dur_t17AUD_GAC_LOW_DUR_4E"></a> <a id="_CPPv2N17aud_gac_low_dur_t17AUD_GAC_LOW_DUR_4E"></a> <a id="group__bk__api__aud__enum_1ggad6db7972d03b0d2579936215f22cc97da7ddff7e0e4be804989f9b580a7847b9a"></a> enumerator AUD\_GAC\_LOW\_DUR\_4
    :   AGC low duration: 4 0.5ms

    <a id="_CPPv4N17aud_gac_low_dur_t17AUD_GAC_LOW_DUR_8E"></a>

    <a id="_CPPv3N17aud_gac_low_dur_t17AUD_GAC_LOW_DUR_8E"></a> <a id="_CPPv2N17aud_gac_low_dur_t17AUD_GAC_LOW_DUR_8E"></a> <a id="group__bk__api__aud__enum_1ggad6db7972d03b0d2579936215f22cc97da43ba3e295ce580d58b282b289f8703f6"></a> enumerator AUD\_GAC\_LOW\_DUR\_8
    :   AGC low duration: 8

    <a id="_CPPv4N17aud_gac_low_dur_t18AUD_GAC_LOW_DUR_16E"></a>

    <a id="_CPPv3N17aud_gac_low_dur_t18AUD_GAC_LOW_DUR_16E"></a> <a id="_CPPv2N17aud_gac_low_dur_t18AUD_GAC_LOW_DUR_16E"></a> <a id="group__bk__api__aud__enum_1ggad6db7972d03b0d2579936215f22cc97dab16c6654a054a5ae3c9a07433e2ea80c"></a> enumerator AUD\_GAC\_LOW\_DUR\_16
    :   AGC low duration: 16

    <a id="_CPPv4N17aud_gac_low_dur_t18AUD_GAC_LOW_DUR_32E"></a>

    <a id="_CPPv3N17aud_gac_low_dur_t18AUD_GAC_LOW_DUR_32E"></a> <a id="_CPPv2N17aud_gac_low_dur_t18AUD_GAC_LOW_DUR_32E"></a> <a id="group__bk__api__aud__enum_1ggad6db7972d03b0d2579936215f22cc97daa8ae920679538b56bc05f7f2827b85ed"></a> enumerator AUD\_GAC\_LOW\_DUR\_32
    :   AGC low duration: 32

    <a id="_CPPv4N17aud_gac_low_dur_t18AUD_GAC_LOW_DUR_64E"></a>

    <a id="_CPPv3N17aud_gac_low_dur_t18AUD_GAC_LOW_DUR_64E"></a> <a id="_CPPv2N17aud_gac_low_dur_t18AUD_GAC_LOW_DUR_64E"></a> <a id="group__bk__api__aud__enum_1ggad6db7972d03b0d2579936215f22cc97da0e66900aa6f03a5519660c9571433c95"></a> enumerator AUD\_GAC\_LOW\_DUR\_64
    :   AGC low duration: 64

    <a id="_CPPv4N17aud_gac_low_dur_t19AUD_GAC_LOW_DUR_128E"></a>

    <a id="_CPPv3N17aud_gac_low_dur_t19AUD_GAC_LOW_DUR_128E"></a> <a id="_CPPv2N17aud_gac_low_dur_t19AUD_GAC_LOW_DUR_128E"></a> <a id="group__bk__api__aud__enum_1ggad6db7972d03b0d2579936215f22cc97da54cd85b794f320e3de4dc44c3ba974bf"></a> enumerator AUD\_GAC\_LOW\_DUR\_128
    :   AGC low duration: 128

    <a id="_CPPv4N17aud_gac_low_dur_t19AUD_GAC_LOW_DUR_256E"></a>

    <a id="_CPPv3N17aud_gac_low_dur_t19AUD_GAC_LOW_DUR_256E"></a> <a id="_CPPv2N17aud_gac_low_dur_t19AUD_GAC_LOW_DUR_256E"></a> <a id="group__bk__api__aud__enum_1ggad6db7972d03b0d2579936215f22cc97da97140524e8f0b7811a17505f57eb465a"></a> enumerator AUD\_GAC\_LOW\_DUR\_256
    :   AGC low duration: 256 32ms

    <a id="_CPPv4N17aud_gac_low_dur_t19AUD_GAC_LOW_DUR_MAXE"></a>

    <a id="_CPPv3N17aud_gac_low_dur_t19AUD_GAC_LOW_DUR_MAXE"></a> <a id="_CPPv2N17aud_gac_low_dur_t19AUD_GAC_LOW_DUR_MAXE"></a> <a id="group__bk__api__aud__enum_1ggad6db7972d03b0d2579936215f22cc97da8e342ace719fed9c0e443030bfdb850a"></a> enumerator AUD\_GAC\_LOW\_DUR\_MAX

<a id="_CPPv417aud_dtmf_enable_t"></a>

<a id="_CPPv317aud_dtmf_enable_t"></a> <a id="_CPPv217aud_dtmf_enable_t"></a> <a id="group__bk__api__aud__enum_1gad461c4436b2f3a1d79b0945cbda545bc"></a> enum aud\_dtmf\_enable\_t
:   *Values:*

    <a id="_CPPv4N17aud_dtmf_enable_t16AUD_DTMF_DISABLEE"></a>

    <a id="_CPPv3N17aud_dtmf_enable_t16AUD_DTMF_DISABLEE"></a> <a id="_CPPv2N17aud_dtmf_enable_t16AUD_DTMF_DISABLEE"></a> <a id="group__bk__api__aud__enum_1ggad461c4436b2f3a1d79b0945cbda545bca62c43ef04a977fe75b76d2edc187339b"></a> enumerator AUD\_DTMF\_DISABLE
    :   disable dtmf

    <a id="_CPPv4N17aud_dtmf_enable_t15AUD_DTMF_ENABLEE"></a>

    <a id="_CPPv3N17aud_dtmf_enable_t15AUD_DTMF_ENABLEE"></a> <a id="_CPPv2N17aud_dtmf_enable_t15AUD_DTMF_ENABLEE"></a> <a id="group__bk__api__aud__enum_1ggad461c4436b2f3a1d79b0945cbda545bca5181138fe10fca27665ec6cb407808e4"></a> enumerator AUD\_DTMF\_ENABLE
    :   enable dtmf

    <a id="_CPPv4N17aud_dtmf_enable_t19AUD_DTMF_ENABLE_MAXE"></a>

    <a id="_CPPv3N17aud_dtmf_enable_t19AUD_DTMF_ENABLE_MAXE"></a> <a id="_CPPv2N17aud_dtmf_enable_t19AUD_DTMF_ENABLE_MAXE"></a> <a id="group__bk__api__aud__enum_1ggad461c4436b2f3a1d79b0945cbda545bcafdc69791104e4001ed54183a230bb078"></a> enumerator AUD\_DTMF\_ENABLE\_MAX

<a id="_CPPv423aud_dtmf_tone_pattern_t"></a>

<a id="_CPPv323aud_dtmf_tone_pattern_t"></a> <a id="_CPPv223aud_dtmf_tone_pattern_t"></a> <a id="group__bk__api__aud__enum_1ga476cd21d27a3691c8c1b58e716320cc6"></a> enum aud\_dtmf\_tone\_pattern\_t
:   *Values:*

    <a id="_CPPv4N23aud_dtmf_tone_pattern_t26AUD_DTMF_TONE_PATTERN_DTMFE"></a>

    <a id="_CPPv3N23aud_dtmf_tone_pattern_t26AUD_DTMF_TONE_PATTERN_DTMFE"></a> <a id="_CPPv2N23aud_dtmf_tone_pattern_t26AUD_DTMF_TONE_PATTERN_DTMFE"></a> <a id="group__bk__api__aud__enum_1gga476cd21d27a3691c8c1b58e716320cc6a4aea0d6cbe61952fcf9c2eeae28665c0"></a> enumerator AUD\_DTMF\_TONE\_PATTERN\_DTMF
    :   0: DTMF(Active\_Time) \+ Zeros(Pause\_Time)

    <a id="_CPPv4N23aud_dtmf_tone_pattern_t26AUD_DTMF_TONE_PATTERN_TONEE"></a>

    <a id="_CPPv3N23aud_dtmf_tone_pattern_t26AUD_DTMF_TONE_PATTERN_TONEE"></a> <a id="_CPPv2N23aud_dtmf_tone_pattern_t26AUD_DTMF_TONE_PATTERN_TONEE"></a> <a id="group__bk__api__aud__enum_1gga476cd21d27a3691c8c1b58e716320cc6acd5f945d1d45b514c331375fd429d8e7"></a> enumerator AUD\_DTMF\_TONE\_PATTERN\_TONE
    :   1：Tone1(Active\_Time) \+ Tone2(Pause\_Time)

    <a id="_CPPv4N23aud_dtmf_tone_pattern_t25AUD_DTMF_TONE_PATTERN_MAXE"></a>

    <a id="_CPPv3N23aud_dtmf_tone_pattern_t25AUD_DTMF_TONE_PATTERN_MAXE"></a> <a id="_CPPv2N23aud_dtmf_tone_pattern_t25AUD_DTMF_TONE_PATTERN_MAXE"></a> <a id="group__bk__api__aud__enum_1gga476cd21d27a3691c8c1b58e716320cc6a062cca1c935530b94ee89e67eb1e8cec"></a> enumerator AUD\_DTMF\_TONE\_PATTERN\_MAX

<a id="_CPPv420aud_dtmf_tone_mode_t"></a>

<a id="_CPPv320aud_dtmf_tone_mode_t"></a> <a id="_CPPv220aud_dtmf_tone_mode_t"></a> <a id="group__bk__api__aud__enum_1ga623537f3353b129a9ca9473876aa2418"></a> enum aud\_dtmf\_tone\_mode\_t
:   *Values:*

    <a id="_CPPv4N20aud_dtmf_tone_mode_t25AUD_DTMF_TONE_MODE_SIGNALE"></a>

    <a id="_CPPv3N20aud_dtmf_tone_mode_t25AUD_DTMF_TONE_MODE_SIGNALE"></a> <a id="_CPPv2N20aud_dtmf_tone_mode_t25AUD_DTMF_TONE_MODE_SIGNALE"></a> <a id="group__bk__api__aud__enum_1gga623537f3353b129a9ca9473876aa2418a7e5e94c7d810fd0f703f217fb4b61776"></a> enumerator AUD\_DTMF\_TONE\_MODE\_SIGNAL
    :   0：signal mode

    <a id="_CPPv4N20aud_dtmf_tone_mode_t26AUD_DTMF_TONE_MODE_CONTIUSE"></a>

    <a id="_CPPv3N20aud_dtmf_tone_mode_t26AUD_DTMF_TONE_MODE_CONTIUSE"></a> <a id="_CPPv2N20aud_dtmf_tone_mode_t26AUD_DTMF_TONE_MODE_CONTIUSE"></a> <a id="group__bk__api__aud__enum_1gga623537f3353b129a9ca9473876aa2418a3d03f2d06989983468ec5ef6b7a779e9"></a> enumerator AUD\_DTMF\_TONE\_MODE\_CONTIUS
    :   1：continuous mode

    <a id="_CPPv4N20aud_dtmf_tone_mode_t22AUD_DTMF_TONE_MODE_MAXE"></a>

    <a id="_CPPv3N20aud_dtmf_tone_mode_t22AUD_DTMF_TONE_MODE_MAXE"></a> <a id="_CPPv2N20aud_dtmf_tone_mode_t22AUD_DTMF_TONE_MODE_MAXE"></a> <a id="group__bk__api__aud__enum_1gga623537f3353b129a9ca9473876aa2418ad439258c705e85ae771320ef6641f91b"></a> enumerator AUD\_DTMF\_TONE\_MODE\_MAX

<a id="_CPPv420aud_dtmf_tone_attu_t"></a>

<a id="_CPPv320aud_dtmf_tone_attu_t"></a> <a id="_CPPv220aud_dtmf_tone_attu_t"></a> <a id="group__bk__api__aud__enum_1gaad0f1062f7ff0dd15c066e2c7fb1b43d"></a> enum aud\_dtmf\_tone\_attu\_t
:   *Values:*

    <a id="_CPPv4N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_1E"></a>

    <a id="_CPPv3N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_1E"></a> <a id="_CPPv2N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_1E"></a> <a id="group__bk__api__aud__enum_1ggaad0f1062f7ff0dd15c066e2c7fb1b43dac80f3783b2d507ca036a630f3947b995"></a> enumerator AUD\_DTMF\_TONE\_ATTU\_MINUS\_1
    :   Tone1 damp set: -1 db

    <a id="_CPPv4N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_2E"></a>

    <a id="_CPPv3N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_2E"></a> <a id="_CPPv2N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_2E"></a> <a id="group__bk__api__aud__enum_1ggaad0f1062f7ff0dd15c066e2c7fb1b43da2f413e63f05c621c45ae7bb6b2b62472"></a> enumerator AUD\_DTMF\_TONE\_ATTU\_MINUS\_2
    :   Tone1 damp set: -2 db

    <a id="_CPPv4N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_3E"></a>

    <a id="_CPPv3N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_3E"></a> <a id="_CPPv2N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_3E"></a> <a id="group__bk__api__aud__enum_1ggaad0f1062f7ff0dd15c066e2c7fb1b43da54cfc1e87b2cb3ebbaf4250009bd15c1"></a> enumerator AUD\_DTMF\_TONE\_ATTU\_MINUS\_3
    :   Tone1 damp set: -3 db

    <a id="_CPPv4N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_4E"></a>

    <a id="_CPPv3N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_4E"></a> <a id="_CPPv2N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_4E"></a> <a id="group__bk__api__aud__enum_1ggaad0f1062f7ff0dd15c066e2c7fb1b43dabc7f7b634d516325a7b2a3cdbb6eee22"></a> enumerator AUD\_DTMF\_TONE\_ATTU\_MINUS\_4
    :   Tone1 damp set: -4 db

    <a id="_CPPv4N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_5E"></a>

    <a id="_CPPv3N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_5E"></a> <a id="_CPPv2N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_5E"></a> <a id="group__bk__api__aud__enum_1ggaad0f1062f7ff0dd15c066e2c7fb1b43da6f934ce695e9ae4c351ec0aa19669f21"></a> enumerator AUD\_DTMF\_TONE\_ATTU\_MINUS\_5
    :   Tone1 damp set: -5 db

    <a id="_CPPv4N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_6E"></a>

    <a id="_CPPv3N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_6E"></a> <a id="_CPPv2N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_6E"></a> <a id="group__bk__api__aud__enum_1ggaad0f1062f7ff0dd15c066e2c7fb1b43da47fa7e27d08ee8d135e340976acc8ffb"></a> enumerator AUD\_DTMF\_TONE\_ATTU\_MINUS\_6
    :   Tone1 damp set: -6 db

    <a id="_CPPv4N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_7E"></a>

    <a id="_CPPv3N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_7E"></a> <a id="_CPPv2N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_7E"></a> <a id="group__bk__api__aud__enum_1ggaad0f1062f7ff0dd15c066e2c7fb1b43da6c548065dc9617bf909e86b0d4b9478d"></a> enumerator AUD\_DTMF\_TONE\_ATTU\_MINUS\_7
    :   Tone1 damp set: -7 db

    <a id="_CPPv4N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_8E"></a>

    <a id="_CPPv3N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_8E"></a> <a id="_CPPv2N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_8E"></a> <a id="group__bk__api__aud__enum_1ggaad0f1062f7ff0dd15c066e2c7fb1b43dac18bb391e0c87dda72722c804be35b38"></a> enumerator AUD\_DTMF\_TONE\_ATTU\_MINUS\_8
    :   Tone1 damp set: -8 db

    <a id="_CPPv4N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_9E"></a>

    <a id="_CPPv3N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_9E"></a> <a id="_CPPv2N20aud_dtmf_tone_attu_t26AUD_DTMF_TONE_ATTU_MINUS_9E"></a> <a id="group__bk__api__aud__enum_1ggaad0f1062f7ff0dd15c066e2c7fb1b43dacc8a2196d3bdba3dda18ad362318a8f8"></a> enumerator AUD\_DTMF\_TONE\_ATTU\_MINUS\_9
    :   Tone1 damp set: -9 db

    <a id="_CPPv4N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_10E"></a>

    <a id="_CPPv3N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_10E"></a> <a id="_CPPv2N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_10E"></a> <a id="group__bk__api__aud__enum_1ggaad0f1062f7ff0dd15c066e2c7fb1b43dadce0db1bd31dad4ec53dcfa5a90fb1cb"></a> enumerator AUD\_DTMF\_TONE\_ATTU\_MINUS\_10
    :   Tone1 damp set: -10 db

    <a id="_CPPv4N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_11E"></a>

    <a id="_CPPv3N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_11E"></a> <a id="_CPPv2N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_11E"></a> <a id="group__bk__api__aud__enum_1ggaad0f1062f7ff0dd15c066e2c7fb1b43daff9f4969762bdeb06752e22c83c5a804"></a> enumerator AUD\_DTMF\_TONE\_ATTU\_MINUS\_11
    :   Tone1 damp set: -11 db

    <a id="_CPPv4N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_12E"></a>

    <a id="_CPPv3N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_12E"></a> <a id="_CPPv2N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_12E"></a> <a id="group__bk__api__aud__enum_1ggaad0f1062f7ff0dd15c066e2c7fb1b43daf21e6d402dca059278ab6c7c0c06c88f"></a> enumerator AUD\_DTMF\_TONE\_ATTU\_MINUS\_12
    :   Tone1 damp set: -12 db

    <a id="_CPPv4N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_13E"></a>

    <a id="_CPPv3N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_13E"></a> <a id="_CPPv2N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_13E"></a> <a id="group__bk__api__aud__enum_1ggaad0f1062f7ff0dd15c066e2c7fb1b43daac1d77de783f03a832c719e4e68c8040"></a> enumerator AUD\_DTMF\_TONE\_ATTU\_MINUS\_13
    :   Tone1 damp set: -13 db

    <a id="_CPPv4N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_14E"></a>

    <a id="_CPPv3N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_14E"></a> <a id="_CPPv2N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_14E"></a> <a id="group__bk__api__aud__enum_1ggaad0f1062f7ff0dd15c066e2c7fb1b43dabb12a6f461f71ea5016bb43893f081f6"></a> enumerator AUD\_DTMF\_TONE\_ATTU\_MINUS\_14
    :   Tone1 damp set: -14 db

    <a id="_CPPv4N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_15E"></a>

    <a id="_CPPv3N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_15E"></a> <a id="_CPPv2N20aud_dtmf_tone_attu_t27AUD_DTMF_TONE_ATTU_MINUS_15E"></a> <a id="group__bk__api__aud__enum_1ggaad0f1062f7ff0dd15c066e2c7fb1b43dabd971248219caf87e3a0702f06fac96c"></a> enumerator AUD\_DTMF\_TONE\_ATTU\_MINUS\_15
    :   Tone1 damp set: -15 db

    <a id="_CPPv4N20aud_dtmf_tone_attu_t28AUD_DTMF_TONE_ATTU_MINUS_MAXE"></a>

    <a id="_CPPv3N20aud_dtmf_tone_attu_t28AUD_DTMF_TONE_ATTU_MINUS_MAXE"></a> <a id="_CPPv2N20aud_dtmf_tone_attu_t28AUD_DTMF_TONE_ATTU_MINUS_MAXE"></a> <a id="group__bk__api__aud__enum_1ggaad0f1062f7ff0dd15c066e2c7fb1b43daf620e7b2e95cd861aefb25696e8aca0c"></a> enumerator AUD\_DTMF\_TONE\_ATTU\_MINUS\_MAX

<a id="_CPPv422aud_dtmf_tone_enable_t"></a>

<a id="_CPPv322aud_dtmf_tone_enable_t"></a> <a id="_CPPv222aud_dtmf_tone_enable_t"></a> <a id="group__bk__api__aud__enum_1ga5e78974640be4110354c2f8ca11ddffb"></a> enum aud\_dtmf\_tone\_enable\_t
:   *Values:*

    <a id="_CPPv4N22aud_dtmf_tone_enable_t21AUD_DTMF_TONE_DISABLEE"></a>

    <a id="_CPPv3N22aud_dtmf_tone_enable_t21AUD_DTMF_TONE_DISABLEE"></a> <a id="_CPPv2N22aud_dtmf_tone_enable_t21AUD_DTMF_TONE_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga5e78974640be4110354c2f8ca11ddffba44faef06569a4b4b6abadb8f080324dd"></a> enumerator AUD\_DTMF\_TONE\_DISABLE
    :   0：disable tone

    <a id="_CPPv4N22aud_dtmf_tone_enable_t20AUD_DTMF_TONE_ENABLEE"></a>

    <a id="_CPPv3N22aud_dtmf_tone_enable_t20AUD_DTMF_TONE_ENABLEE"></a> <a id="_CPPv2N22aud_dtmf_tone_enable_t20AUD_DTMF_TONE_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga5e78974640be4110354c2f8ca11ddffba6ffa0af189071d45eccaa78f3a01d252"></a> enumerator AUD\_DTMF\_TONE\_ENABLE
    :   1：enable tone

    <a id="_CPPv4N22aud_dtmf_tone_enable_t24AUD_DTMF_TONE_ENABLE_MAXE"></a>

    <a id="_CPPv3N22aud_dtmf_tone_enable_t24AUD_DTMF_TONE_ENABLE_MAXE"></a> <a id="_CPPv2N22aud_dtmf_tone_enable_t24AUD_DTMF_TONE_ENABLE_MAXE"></a> <a id="group__bk__api__aud__enum_1gga5e78974640be4110354c2f8ca11ddffba2b50d055c7e0f965d138a36d4f7c0d71"></a> enumerator AUD\_DTMF\_TONE\_ENABLE\_MAX

<a id="_CPPv427aud_adc_fracmod_manual_en_t"></a>

<a id="_CPPv327aud_adc_fracmod_manual_en_t"></a> <a id="_CPPv227aud_adc_fracmod_manual_en_t"></a> <a id="group__bk__api__aud__enum_1ga903fdec7a387be667de82542ba8b3b55"></a> enum aud\_adc\_fracmod\_manual\_en\_t
:   *Values:*

    <a id="_CPPv4N27aud_adc_fracmod_manual_en_t30AUD_ADC_TRACMOD_MANUAL_DISABLEE"></a>

    <a id="_CPPv3N27aud_adc_fracmod_manual_en_t30AUD_ADC_TRACMOD_MANUAL_DISABLEE"></a> <a id="_CPPv2N27aud_adc_fracmod_manual_en_t30AUD_ADC_TRACMOD_MANUAL_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga903fdec7a387be667de82542ba8b3b55a94dd62671cc6ae2eddb63ebaced3713b"></a> enumerator AUD\_ADC\_TRACMOD\_MANUAL\_DISABLE
    :   0：disable ADC fractional frequency division of manual set

    <a id="_CPPv4N27aud_adc_fracmod_manual_en_t29AUD_ADC_TRACMOD_MANUAL_ENABLEE"></a>

    <a id="_CPPv3N27aud_adc_fracmod_manual_en_t29AUD_ADC_TRACMOD_MANUAL_ENABLEE"></a> <a id="_CPPv2N27aud_adc_fracmod_manual_en_t29AUD_ADC_TRACMOD_MANUAL_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga903fdec7a387be667de82542ba8b3b55a611d82cf471ef241c73eeab9ee24131a"></a> enumerator AUD\_ADC\_TRACMOD\_MANUAL\_ENABLE
    :   1：enable ADC fractional frequency division of manual set

    <a id="_CPPv4N27aud_adc_fracmod_manual_en_t29AUD_ADC_TRACMOD_MANUAL_EN_MAXE"></a>

    <a id="_CPPv3N27aud_adc_fracmod_manual_en_t29AUD_ADC_TRACMOD_MANUAL_EN_MAXE"></a> <a id="_CPPv2N27aud_adc_fracmod_manual_en_t29AUD_ADC_TRACMOD_MANUAL_EN_MAXE"></a> <a id="group__bk__api__aud__enum_1gga903fdec7a387be667de82542ba8b3b55a592425d76a1e4959b00ec22f5ab5e10d"></a> enumerator AUD\_ADC\_TRACMOD\_MANUAL\_EN\_MAX

<a id="_CPPv416aud_dac_enable_t"></a>

<a id="_CPPv316aud_dac_enable_t"></a> <a id="_CPPv216aud_dac_enable_t"></a> <a id="group__bk__api__aud__enum_1ga54f6b47ab8a5c179963d18e4cc1c717b"></a> enum aud\_dac\_enable\_t
:   dac enum

    *Values:*

    <a id="_CPPv4N16aud_dac_enable_t15AUD_DAC_DISABLEE"></a>

    <a id="_CPPv3N16aud_dac_enable_t15AUD_DAC_DISABLEE"></a> <a id="_CPPv2N16aud_dac_enable_t15AUD_DAC_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga54f6b47ab8a5c179963d18e4cc1c717ba93d3e0dc767ddfb0e2eb451cb63a013e"></a> enumerator AUD\_DAC\_DISABLE
    :   0：disable dac

    <a id="_CPPv4N16aud_dac_enable_t14AUD_DAC_ENABLEE"></a>

    <a id="_CPPv3N16aud_dac_enable_t14AUD_DAC_ENABLEE"></a> <a id="_CPPv2N16aud_dac_enable_t14AUD_DAC_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga54f6b47ab8a5c179963d18e4cc1c717bac144dbe2a551e57f2478c41be055fd5e"></a> enumerator AUD\_DAC\_ENABLE
    :   1：enable dac

    <a id="_CPPv4N16aud_dac_enable_t14AUD_DAC_OTHERSE"></a>

    <a id="_CPPv3N16aud_dac_enable_t14AUD_DAC_OTHERSE"></a> <a id="_CPPv2N16aud_dac_enable_t14AUD_DAC_OTHERSE"></a> <a id="group__bk__api__aud__enum_1gga54f6b47ab8a5c179963d18e4cc1c717ba1eb4a411c146e2056a29eef9bcf61660"></a> enumerator AUD\_DAC\_OTHERS

<a id="_CPPv420aud_dac_chl_enable_t"></a>

<a id="_CPPv320aud_dac_chl_enable_t"></a> <a id="_CPPv220aud_dac_chl_enable_t"></a> <a id="group__bk__api__aud__enum_1ga8acb78a0c4aac7cf978e25c1da6738d6"></a> enum aud\_dac\_chl\_enable\_t
:   *Values:*

    <a id="_CPPv4N20aud_dac_chl_enable_t19AUD_DAC_CHL_DISABLEE"></a>

    <a id="_CPPv3N20aud_dac_chl_enable_t19AUD_DAC_CHL_DISABLEE"></a> <a id="_CPPv2N20aud_dac_chl_enable_t19AUD_DAC_CHL_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga8acb78a0c4aac7cf978e25c1da6738d6adbc4688ddfcbf1a00cf5ecc12340a9cf"></a> enumerator AUD\_DAC\_CHL\_DISABLE
    :   disable all dac channel

    <a id="_CPPv4N20aud_dac_chl_enable_t20AUD_DAC_CHL_L_ENABLEE"></a>

    <a id="_CPPv3N20aud_dac_chl_enable_t20AUD_DAC_CHL_L_ENABLEE"></a> <a id="_CPPv2N20aud_dac_chl_enable_t20AUD_DAC_CHL_L_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga8acb78a0c4aac7cf978e25c1da6738d6a0381d4fe4975b5bff104c397af0d9b6f"></a> enumerator AUD\_DAC\_CHL\_L\_ENABLE
    :   enable dac left channel

    <a id="_CPPv4N20aud_dac_chl_enable_t20AUD_DAC_CHL_R_ENABLEE"></a>

    <a id="_CPPv3N20aud_dac_chl_enable_t20AUD_DAC_CHL_R_ENABLEE"></a> <a id="_CPPv2N20aud_dac_chl_enable_t20AUD_DAC_CHL_R_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga8acb78a0c4aac7cf978e25c1da6738d6a7ec9f9716e9c35619ab6d8ab93a2001b"></a> enumerator AUD\_DAC\_CHL\_R\_ENABLE
    :   enable dac right channel

    <a id="_CPPv4N20aud_dac_chl_enable_t21AUD_DAC_CHL_LR_ENABLEE"></a>

    <a id="_CPPv3N20aud_dac_chl_enable_t21AUD_DAC_CHL_LR_ENABLEE"></a> <a id="_CPPv2N20aud_dac_chl_enable_t21AUD_DAC_CHL_LR_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga8acb78a0c4aac7cf978e25c1da6738d6a24f429abe92036bd67ac04994aeda594"></a> enumerator AUD\_DAC\_CHL\_LR\_ENABLE
    :   enable dac left and right channel

    <a id="_CPPv4N20aud_dac_chl_enable_t15AUD_DAC_CHL_MAXE"></a>

    <a id="_CPPv3N20aud_dac_chl_enable_t15AUD_DAC_CHL_MAXE"></a> <a id="_CPPv2N20aud_dac_chl_enable_t15AUD_DAC_CHL_MAXE"></a> <a id="group__bk__api__aud__enum_1gga8acb78a0c4aac7cf978e25c1da6738d6abc873bad568a7357413fefc639dca810"></a> enumerator AUD\_DAC\_CHL\_MAX

<a id="_CPPv419aud_dac_work_mode_t"></a>

<a id="_CPPv319aud_dac_work_mode_t"></a> <a id="_CPPv219aud_dac_work_mode_t"></a> <a id="group__bk__api__aud__enum_1ga1b762153b25976b2352cc881ca773631"></a> enum aud\_dac\_work\_mode\_t
:   *Values:*

    <a id="_CPPv4N19aud_dac_work_mode_t28AUD_DAC_WORK_MODE_SIGNAL_ENDE"></a>

    <a id="_CPPv3N19aud_dac_work_mode_t28AUD_DAC_WORK_MODE_SIGNAL_ENDE"></a> <a id="_CPPv2N19aud_dac_work_mode_t28AUD_DAC_WORK_MODE_SIGNAL_ENDE"></a> <a id="group__bk__api__aud__enum_1gga1b762153b25976b2352cc881ca773631a9762fdadd6d38690a8017c1d8f707b7d"></a> enumerator AUD\_DAC\_WORK\_MODE\_SIGNAL\_END

    <a id="_CPPv4N19aud_dac_work_mode_t24AUD_DAC_WORK_MODE_DIFFENE"></a>

    <a id="_CPPv3N19aud_dac_work_mode_t24AUD_DAC_WORK_MODE_DIFFENE"></a> <a id="_CPPv2N19aud_dac_work_mode_t24AUD_DAC_WORK_MODE_DIFFENE"></a> <a id="group__bk__api__aud__enum_1gga1b762153b25976b2352cc881ca773631ad7500cb92a019f3c7ce6d022997d05e0"></a> enumerator AUD\_DAC\_WORK\_MODE\_DIFFEN

    <a id="_CPPv4N19aud_dac_work_mode_t21AUD_DAC_WORK_MODE_MAXE"></a>

    <a id="_CPPv3N19aud_dac_work_mode_t21AUD_DAC_WORK_MODE_MAXE"></a> <a id="_CPPv2N19aud_dac_work_mode_t21AUD_DAC_WORK_MODE_MAXE"></a> <a id="group__bk__api__aud__enum_1gga1b762153b25976b2352cc881ca773631a001857ad476d83b7439f1015c0f82c21"></a> enumerator AUD\_DAC\_WORK\_MODE\_MAX

<a id="_CPPv419aud_dac_samp_rate_t"></a>

<a id="_CPPv319aud_dac_samp_rate_t"></a> <a id="_CPPv219aud_dac_samp_rate_t"></a> <a id="group__bk__api__aud__enum_1gadb75ad63ed7dec151054b9a24961abb4"></a> enum aud\_dac\_samp\_rate\_t
:   *Values:*

    <a id="_CPPv4N19aud_dac_samp_rate_t20AUD_DAC_SAMP_RATE_8KE"></a>

    <a id="_CPPv3N19aud_dac_samp_rate_t20AUD_DAC_SAMP_RATE_8KE"></a> <a id="_CPPv2N19aud_dac_samp_rate_t20AUD_DAC_SAMP_RATE_8KE"></a> <a id="group__bk__api__aud__enum_1ggadb75ad63ed7dec151054b9a24961abb4ab0a1096cd52b7d4fa692b4972f49957f"></a> enumerator AUD\_DAC\_SAMP\_RATE\_8K
    :   DAC sample rate : 8k

    <a id="_CPPv4N19aud_dac_samp_rate_t25AUD_DAC_SAMP_RATE_11_025KE"></a>

    <a id="_CPPv3N19aud_dac_samp_rate_t25AUD_DAC_SAMP_RATE_11_025KE"></a> <a id="_CPPv2N19aud_dac_samp_rate_t25AUD_DAC_SAMP_RATE_11_025KE"></a> <a id="group__bk__api__aud__enum_1ggadb75ad63ed7dec151054b9a24961abb4af452f0abec0da14ab709b0c2884039a8"></a> enumerator AUD\_DAC\_SAMP\_RATE\_11\_025K
    :   DAC sample rate : 11.025k

    <a id="_CPPv4N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_12KE"></a>

    <a id="_CPPv3N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_12KE"></a> <a id="_CPPv2N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_12KE"></a> <a id="group__bk__api__aud__enum_1ggadb75ad63ed7dec151054b9a24961abb4af42fd44c0851fa1b9e8f836989e2bd49"></a> enumerator AUD\_DAC\_SAMP\_RATE\_12K
    :   DAC sample rate : 12k

    <a id="_CPPv4N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_16KE"></a>

    <a id="_CPPv3N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_16KE"></a> <a id="_CPPv2N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_16KE"></a> <a id="group__bk__api__aud__enum_1ggadb75ad63ed7dec151054b9a24961abb4a8cbd3cbbbc562d4ffaeef27f431ec133"></a> enumerator AUD\_DAC\_SAMP\_RATE\_16K
    :   DAC sample rate : 16k

    <a id="_CPPv4N19aud_dac_samp_rate_t24AUD_DAC_SAMP_RATE_22_05KE"></a>

    <a id="_CPPv3N19aud_dac_samp_rate_t24AUD_DAC_SAMP_RATE_22_05KE"></a> <a id="_CPPv2N19aud_dac_samp_rate_t24AUD_DAC_SAMP_RATE_22_05KE"></a> <a id="group__bk__api__aud__enum_1ggadb75ad63ed7dec151054b9a24961abb4a3efec74a85a1ac4c584a32c84bf1a28a"></a> enumerator AUD\_DAC\_SAMP\_RATE\_22\_05K
    :   DAC sample rate : 22.05k

    <a id="_CPPv4N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_24KE"></a>

    <a id="_CPPv3N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_24KE"></a> <a id="_CPPv2N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_24KE"></a> <a id="group__bk__api__aud__enum_1ggadb75ad63ed7dec151054b9a24961abb4a8a02e3712ccaabdc05414787f1eecc84"></a> enumerator AUD\_DAC\_SAMP\_RATE\_24K
    :   DAC sample rate : 24k

    <a id="_CPPv4N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_32KE"></a>

    <a id="_CPPv3N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_32KE"></a> <a id="_CPPv2N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_32KE"></a> <a id="group__bk__api__aud__enum_1ggadb75ad63ed7dec151054b9a24961abb4ade2f45ef78e3a73fb15603dbddfcf3ff"></a> enumerator AUD\_DAC\_SAMP\_RATE\_32K
    :   DAC sample rate : 32k

    <a id="_CPPv4N19aud_dac_samp_rate_t23AUD_DAC_SAMP_RATE_44_1KE"></a>

    <a id="_CPPv3N19aud_dac_samp_rate_t23AUD_DAC_SAMP_RATE_44_1KE"></a> <a id="_CPPv2N19aud_dac_samp_rate_t23AUD_DAC_SAMP_RATE_44_1KE"></a> <a id="group__bk__api__aud__enum_1ggadb75ad63ed7dec151054b9a24961abb4a2a99b0441071d195894199f9a2bca28e"></a> enumerator AUD\_DAC\_SAMP\_RATE\_44\_1K
    :   DAC sample rate : 44.1k

    <a id="_CPPv4N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_48KE"></a>

    <a id="_CPPv3N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_48KE"></a> <a id="_CPPv2N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_48KE"></a> <a id="group__bk__api__aud__enum_1ggadb75ad63ed7dec151054b9a24961abb4a857a8c1c7d99438e0baffbf3a34281f8"></a> enumerator AUD\_DAC\_SAMP\_RATE\_48K
    :   DAC sample rate : 48k

    <a id="_CPPv4N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_MAXE"></a>

    <a id="_CPPv3N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_MAXE"></a> <a id="_CPPv2N19aud_dac_samp_rate_t21AUD_DAC_SAMP_RATE_MAXE"></a> <a id="group__bk__api__aud__enum_1ggadb75ad63ed7dec151054b9a24961abb4ae8e868a97d791a24be51346efa6aaff8"></a> enumerator AUD\_DAC\_SAMP\_RATE\_MAX

<a id="_CPPv420aud_dac_hpf_bypass_t"></a>

<a id="_CPPv320aud_dac_hpf_bypass_t"></a> <a id="_CPPv220aud_dac_hpf_bypass_t"></a> <a id="group__bk__api__aud__enum_1gac60ae3204e62ed417e9865793ffad79b"></a> enum aud\_dac\_hpf\_bypass\_t
:   *Values:*

    <a id="_CPPv4N20aud_dac_hpf_bypass_t26AUD_DAC_HPF_BYPASS_DISABLEE"></a>

    <a id="_CPPv3N20aud_dac_hpf_bypass_t26AUD_DAC_HPF_BYPASS_DISABLEE"></a> <a id="_CPPv2N20aud_dac_hpf_bypass_t26AUD_DAC_HPF_BYPASS_DISABLEE"></a> <a id="group__bk__api__aud__enum_1ggac60ae3204e62ed417e9865793ffad79baeb52ab980c3bf4f9ff3435f59ef815c2"></a> enumerator AUD\_DAC\_HPF\_BYPASS\_DISABLE
    :   AUD DAC hpf bypass disable

    <a id="_CPPv4N20aud_dac_hpf_bypass_t25AUD_DAC_HPF_BYPASS_ENABLEE"></a>

    <a id="_CPPv3N20aud_dac_hpf_bypass_t25AUD_DAC_HPF_BYPASS_ENABLEE"></a> <a id="_CPPv2N20aud_dac_hpf_bypass_t25AUD_DAC_HPF_BYPASS_ENABLEE"></a> <a id="group__bk__api__aud__enum_1ggac60ae3204e62ed417e9865793ffad79bace2af2d0faed7edf2079caa46839ceba"></a> enumerator AUD\_DAC\_HPF\_BYPASS\_ENABLE
    :   AUD DAC hpf bypass enable

    <a id="_CPPv4N20aud_dac_hpf_bypass_t25AUD_DAC_HPF_BYPASS_OTHERSE"></a>

    <a id="_CPPv3N20aud_dac_hpf_bypass_t25AUD_DAC_HPF_BYPASS_OTHERSE"></a> <a id="_CPPv2N20aud_dac_hpf_bypass_t25AUD_DAC_HPF_BYPASS_OTHERSE"></a> <a id="group__bk__api__aud__enum_1ggac60ae3204e62ed417e9865793ffad79ba976bfe1f8819bb2d8a5d7274007651ef"></a> enumerator AUD\_DAC\_HPF\_BYPASS\_OTHERS

<a id="_CPPv420aud_dac_clk_invert_t"></a>

<a id="_CPPv320aud_dac_clk_invert_t"></a> <a id="_CPPv220aud_dac_clk_invert_t"></a> <a id="group__bk__api__aud__enum_1ga40fa516cd51874985f1f253e749af850"></a> enum aud\_dac\_clk\_invert\_t
:   *Values:*

    <a id="_CPPv4N20aud_dac_clk_invert_t25AUD_DAC_CLK_INVERT_RISINGE"></a>

    <a id="_CPPv3N20aud_dac_clk_invert_t25AUD_DAC_CLK_INVERT_RISINGE"></a> <a id="_CPPv2N20aud_dac_clk_invert_t25AUD_DAC_CLK_INVERT_RISINGE"></a> <a id="group__bk__api__aud__enum_1gga40fa516cd51874985f1f253e749af850a0e617e3e9b09137a96f19993e1f13f9f"></a> enumerator AUD\_DAC\_CLK\_INVERT\_RISING
    :   AUD dac output clock edge rising

    <a id="_CPPv4N20aud_dac_clk_invert_t26AUD_DAC_CLK_INVERT_FALLINGE"></a>

    <a id="_CPPv3N20aud_dac_clk_invert_t26AUD_DAC_CLK_INVERT_FALLINGE"></a> <a id="_CPPv2N20aud_dac_clk_invert_t26AUD_DAC_CLK_INVERT_FALLINGE"></a> <a id="group__bk__api__aud__enum_1gga40fa516cd51874985f1f253e749af850a33d4e9cc299d5b09d54e5bd37fb77204"></a> enumerator AUD\_DAC\_CLK\_INVERT\_FALLING
    :   AUD dac output clock edge falling

    <a id="_CPPv4N20aud_dac_clk_invert_t25AUD_DAC_CLK_INVERT_OTHERSE"></a>

    <a id="_CPPv3N20aud_dac_clk_invert_t25AUD_DAC_CLK_INVERT_OTHERSE"></a> <a id="_CPPv2N20aud_dac_clk_invert_t25AUD_DAC_CLK_INVERT_OTHERSE"></a> <a id="group__bk__api__aud__enum_1gga40fa516cd51874985f1f253e749af850a87f1e991231c8a32ea52b88f8a7a9878"></a> enumerator AUD\_DAC\_CLK\_INVERT\_OTHERS

<a id="_CPPv420aud_dac_int_enable_t"></a>

<a id="_CPPv320aud_dac_int_enable_t"></a> <a id="_CPPv220aud_dac_int_enable_t"></a> <a id="group__bk__api__aud__enum_1ga14eb74ae7556b6e77de2c40e0cfedf04"></a> enum aud\_dac\_int\_enable\_t
:   *Values:*

    <a id="_CPPv4N20aud_dac_int_enable_t20AUD_DACR_INT_DISABLEE"></a>

    <a id="_CPPv3N20aud_dac_int_enable_t20AUD_DACR_INT_DISABLEE"></a> <a id="_CPPv2N20aud_dac_int_enable_t20AUD_DACR_INT_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga14eb74ae7556b6e77de2c40e0cfedf04a97eac9170173baf27e7fbf61ddaa9e7a"></a> enumerator AUD\_DACR\_INT\_DISABLE
    :   AUD dac right channel interrupt disable

    <a id="_CPPv4N20aud_dac_int_enable_t19AUD_DACR_INT_ENABLEE"></a>

    <a id="_CPPv3N20aud_dac_int_enable_t19AUD_DACR_INT_ENABLEE"></a> <a id="_CPPv2N20aud_dac_int_enable_t19AUD_DACR_INT_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga14eb74ae7556b6e77de2c40e0cfedf04abeb7d1f0ee04b5f4edb77dde6773fa29"></a> enumerator AUD\_DACR\_INT\_ENABLE
    :   AUD dac right channel interrupt enable

    <a id="_CPPv4N20aud_dac_int_enable_t20AUD_DACL_INT_DISABLEE"></a>

    <a id="_CPPv3N20aud_dac_int_enable_t20AUD_DACL_INT_DISABLEE"></a> <a id="_CPPv2N20aud_dac_int_enable_t20AUD_DACL_INT_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga14eb74ae7556b6e77de2c40e0cfedf04a56b0bc10e4dcf9dd482dd1cdff290ef8"></a> enumerator AUD\_DACL\_INT\_DISABLE
    :   AUD dac left channel interrupt disable

    <a id="_CPPv4N20aud_dac_int_enable_t19AUD_DACL_INT_ENABLEE"></a>

    <a id="_CPPv3N20aud_dac_int_enable_t19AUD_DACL_INT_ENABLEE"></a> <a id="_CPPv2N20aud_dac_int_enable_t19AUD_DACL_INT_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga14eb74ae7556b6e77de2c40e0cfedf04ad0bc35e3be896fe3e01dd37b9b701e79"></a> enumerator AUD\_DACL\_INT\_ENABLE
    :   AUD dac left channel interrupt enable

    <a id="_CPPv4N20aud_dac_int_enable_t18AUD_DAC_INT_OTHERSE"></a>

    <a id="_CPPv3N20aud_dac_int_enable_t18AUD_DAC_INT_OTHERSE"></a> <a id="_CPPv2N20aud_dac_int_enable_t18AUD_DAC_INT_OTHERSE"></a> <a id="group__bk__api__aud__enum_1gga14eb74ae7556b6e77de2c40e0cfedf04a84c7a571cdb58db5dc5088e057cc4675"></a> enumerator AUD\_DAC\_INT\_OTHERS

<a id="_CPPv421aud_dac_filt_enable_t"></a>

<a id="_CPPv321aud_dac_filt_enable_t"></a> <a id="_CPPv221aud_dac_filt_enable_t"></a> <a id="group__bk__api__aud__enum_1ga3ce14978bb5d223c405b225188ac39df"></a> enum aud\_dac\_filt\_enable\_t
:   *Values:*

    <a id="_CPPv4N21aud_dac_filt_enable_t20AUD_DAC_FILT_DISABLEE"></a>

    <a id="_CPPv3N21aud_dac_filt_enable_t20AUD_DAC_FILT_DISABLEE"></a> <a id="_CPPv2N21aud_dac_filt_enable_t20AUD_DAC_FILT_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga3ce14978bb5d223c405b225188ac39dfaccbab30dd2a52cd198607a0ab96b346c"></a> enumerator AUD\_DAC\_FILT\_DISABLE
    :   AUD dac filter disable

    <a id="_CPPv4N21aud_dac_filt_enable_t19AUD_DAC_FILT_ENABLEE"></a>

    <a id="_CPPv3N21aud_dac_filt_enable_t19AUD_DAC_FILT_ENABLEE"></a> <a id="_CPPv2N21aud_dac_filt_enable_t19AUD_DAC_FILT_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga3ce14978bb5d223c405b225188ac39dfaa74fa9b6ea70efaa33a35ac96c11b61f"></a> enumerator AUD\_DAC\_FILT\_ENABLE
    :   AUD dac filter enable

    <a id="_CPPv4N21aud_dac_filt_enable_t19AUD_DAC_FILT_OTHERSE"></a>

    <a id="_CPPv3N21aud_dac_filt_enable_t19AUD_DAC_FILT_OTHERSE"></a> <a id="_CPPv2N21aud_dac_filt_enable_t19AUD_DAC_FILT_OTHERSE"></a> <a id="group__bk__api__aud__enum_1gga3ce14978bb5d223c405b225188ac39dfa519c45b802c2c37e5824d6520d2f8eea"></a> enumerator AUD\_DAC\_FILT\_OTHERS

<a id="_CPPv424aud_dac_fracmod_manual_t"></a>

<a id="_CPPv324aud_dac_fracmod_manual_t"></a> <a id="_CPPv224aud_dac_fracmod_manual_t"></a> <a id="group__bk__api__aud__enum_1ga413a13bf151b0af58d5f7cf5c8bf221f"></a> enum aud\_dac\_fracmod\_manual\_t
:   *Values:*

    <a id="_CPPv4N24aud_dac_fracmod_manual_t30AUD_DAC_FRACMOD_MANUAL_DISABLEE"></a>

    <a id="_CPPv3N24aud_dac_fracmod_manual_t30AUD_DAC_FRACMOD_MANUAL_DISABLEE"></a> <a id="_CPPv2N24aud_dac_fracmod_manual_t30AUD_DAC_FRACMOD_MANUAL_DISABLEE"></a> <a id="group__bk__api__aud__enum_1gga413a13bf151b0af58d5f7cf5c8bf221fa8dbc6f646c0216311f646e5d0ccefc0d"></a> enumerator AUD\_DAC\_FRACMOD\_MANUAL\_DISABLE
    :   disable dac fractional frequency division of manual set

    <a id="_CPPv4N24aud_dac_fracmod_manual_t29AUD_DAC_FRACMOD_MANUAL_ENABLEE"></a>

    <a id="_CPPv3N24aud_dac_fracmod_manual_t29AUD_DAC_FRACMOD_MANUAL_ENABLEE"></a> <a id="_CPPv2N24aud_dac_fracmod_manual_t29AUD_DAC_FRACMOD_MANUAL_ENABLEE"></a> <a id="group__bk__api__aud__enum_1gga413a13bf151b0af58d5f7cf5c8bf221fadbed3efe91557f1a8f606c35b957447c"></a> enumerator AUD\_DAC\_FRACMOD\_MANUAL\_ENABLE
    :   enable ADC fractional frequency division of manual set

    <a id="_CPPv4N24aud_dac_fracmod_manual_t29ADU_DAC_FRACMOD_MANUAL_OTHERSE"></a>

    <a id="_CPPv3N24aud_dac_fracmod_manual_t29ADU_DAC_FRACMOD_MANUAL_OTHERSE"></a> <a id="_CPPv2N24aud_dac_fracmod_manual_t29ADU_DAC_FRACMOD_MANUAL_OTHERSE"></a> <a id="group__bk__api__aud__enum_1gga413a13bf151b0af58d5f7cf5c8bf221fa60a3d1ae816186a29139b94e46fcc13e"></a> enumerator ADU\_DAC\_FRACMOD\_MANUAL\_OTHERS

<a id="_CPPv421aud_adc_status_mask_t"></a>

<a id="_CPPv321aud_adc_status_mask_t"></a> <a id="_CPPv221aud_adc_status_mask_t"></a> <a id="group__bk__api__aud__enum_1gad3a9b167a604dd0c95764f5cdbf6a13e"></a> enum aud\_adc\_status\_mask\_t
:   *Values:*

    <a id="_CPPv4N21aud_adc_status_mask_t23AUD_ADCL_NEAR_FULL_MASKE"></a>

    <a id="_CPPv3N21aud_adc_status_mask_t23AUD_ADCL_NEAR_FULL_MASKE"></a> <a id="_CPPv2N21aud_adc_status_mask_t23AUD_ADCL_NEAR_FULL_MASKE"></a> <a id="group__bk__api__aud__enum_1ggad3a9b167a604dd0c95764f5cdbf6a13ea3f3c460133cddb8003de90a433d6c125"></a> enumerator AUD\_ADCL\_NEAR\_FULL\_MASK
    :   AUD ADC left channel FIFO near full

    <a id="_CPPv4N21aud_adc_status_mask_t23AUD_DTMF_NEAR_FULL_MASKE"></a>

    <a id="_CPPv3N21aud_adc_status_mask_t23AUD_DTMF_NEAR_FULL_MASKE"></a> <a id="_CPPv2N21aud_adc_status_mask_t23AUD_DTMF_NEAR_FULL_MASKE"></a> <a id="group__bk__api__aud__enum_1ggad3a9b167a604dd0c95764f5cdbf6a13ea3a3c33acb8526a09cd889e88cd174755"></a> enumerator AUD\_DTMF\_NEAR\_FULL\_MASK
    :   AUD DTMF FIFO near full

    <a id="_CPPv4N21aud_adc_status_mask_t24AUD_ADCL_NEAR_EMPTY_MASKE"></a>

    <a id="_CPPv3N21aud_adc_status_mask_t24AUD_ADCL_NEAR_EMPTY_MASKE"></a> <a id="_CPPv2N21aud_adc_status_mask_t24AUD_ADCL_NEAR_EMPTY_MASKE"></a> <a id="group__bk__api__aud__enum_1ggad3a9b167a604dd0c95764f5cdbf6a13ea7860d19d87f6d528765e1fe47abf5194"></a> enumerator AUD\_ADCL\_NEAR\_EMPTY\_MASK
    :   AUD ADC left channel FIFO near empty

    <a id="_CPPv4N21aud_adc_status_mask_t24AUD_DTMF_NEAR_EMPTY_MASKE"></a>

    <a id="_CPPv3N21aud_adc_status_mask_t24AUD_DTMF_NEAR_EMPTY_MASKE"></a> <a id="_CPPv2N21aud_adc_status_mask_t24AUD_DTMF_NEAR_EMPTY_MASKE"></a> <a id="group__bk__api__aud__enum_1ggad3a9b167a604dd0c95764f5cdbf6a13eae56988f9a95535de025b0f2544fc511b"></a> enumerator AUD\_DTMF\_NEAR\_EMPTY\_MASK
    :   AUD DTMF FIFO near empty

    <a id="_CPPv4N21aud_adc_status_mask_t23AUD_ADCL_FIFO_FULL_MASKE"></a>

    <a id="_CPPv3N21aud_adc_status_mask_t23AUD_ADCL_FIFO_FULL_MASKE"></a> <a id="_CPPv2N21aud_adc_status_mask_t23AUD_ADCL_FIFO_FULL_MASKE"></a> <a id="group__bk__api__aud__enum_1ggad3a9b167a604dd0c95764f5cdbf6a13eaf20d1dc0f4e3db371929e91c49ad67be"></a> enumerator AUD\_ADCL\_FIFO\_FULL\_MASK
    :   AUD ADC left channel FIFO full

    <a id="_CPPv4N21aud_adc_status_mask_t23AUD_DTMF_FIFO_FULL_MASKE"></a>

    <a id="_CPPv3N21aud_adc_status_mask_t23AUD_DTMF_FIFO_FULL_MASKE"></a> <a id="_CPPv2N21aud_adc_status_mask_t23AUD_DTMF_FIFO_FULL_MASKE"></a> <a id="group__bk__api__aud__enum_1ggad3a9b167a604dd0c95764f5cdbf6a13ea2486ab6b4d45701fe183dd98fdcb65a4"></a> enumerator AUD\_DTMF\_FIFO\_FULL\_MASK
    :   AUD DTMF FIFO full

    <a id="_CPPv4N21aud_adc_status_mask_t24AUD_ADCL_FIFO_EMPTY_MASKE"></a>

    <a id="_CPPv3N21aud_adc_status_mask_t24AUD_ADCL_FIFO_EMPTY_MASKE"></a> <a id="_CPPv2N21aud_adc_status_mask_t24AUD_ADCL_FIFO_EMPTY_MASKE"></a> <a id="group__bk__api__aud__enum_1ggad3a9b167a604dd0c95764f5cdbf6a13ea2377f029fdfe6ab3e69404f4624797ca"></a> enumerator AUD\_ADCL\_FIFO\_EMPTY\_MASK
    :   AUD ADC left channel FIFO empty

    <a id="_CPPv4N21aud_adc_status_mask_t24AUD_DTMF_FIFO_EMPTY_MASKE"></a>

    <a id="_CPPv3N21aud_adc_status_mask_t24AUD_DTMF_FIFO_EMPTY_MASKE"></a> <a id="_CPPv2N21aud_adc_status_mask_t24AUD_DTMF_FIFO_EMPTY_MASKE"></a> <a id="group__bk__api__aud__enum_1ggad3a9b167a604dd0c95764f5cdbf6a13ea00d3f0690fbb5f335255148ff0be1505"></a> enumerator AUD\_DTMF\_FIFO\_EMPTY\_MASK
    :   AUD DTMF FIFO empty

<a id="_CPPv421aud_dac_status_mask_t"></a>

<a id="_CPPv321aud_dac_status_mask_t"></a> <a id="_CPPv221aud_dac_status_mask_t"></a> <a id="group__bk__api__aud__enum_1ga76aa61164a2e7c641acbd08501be0bd3"></a> enum aud\_dac\_status\_mask\_t
:   *Values:*

    <a id="_CPPv4N21aud_dac_status_mask_t23AUD_DACR_NEAR_FULL_MASKE"></a>

    <a id="_CPPv3N21aud_dac_status_mask_t23AUD_DACR_NEAR_FULL_MASKE"></a> <a id="_CPPv2N21aud_dac_status_mask_t23AUD_DACR_NEAR_FULL_MASKE"></a> <a id="group__bk__api__aud__enum_1gga76aa61164a2e7c641acbd08501be0bd3a716d7bfbab135bfe3899d1113d4efa8a"></a> enumerator AUD\_DACR\_NEAR\_FULL\_MASK
    :   AUD DAC right channel fifo near full

    <a id="_CPPv4N21aud_dac_status_mask_t23AUD_DACL_NEAR_FULL_MASKE"></a>

    <a id="_CPPv3N21aud_dac_status_mask_t23AUD_DACL_NEAR_FULL_MASKE"></a> <a id="_CPPv2N21aud_dac_status_mask_t23AUD_DACL_NEAR_FULL_MASKE"></a> <a id="group__bk__api__aud__enum_1gga76aa61164a2e7c641acbd08501be0bd3a7548eeba7487c62a6bcfa1a664f45ba3"></a> enumerator AUD\_DACL\_NEAR\_FULL\_MASK
    :   AUD DAC left channel fifo near full

    <a id="_CPPv4N21aud_dac_status_mask_t24AUD_DACR_NEAR_EMPTY_MASKE"></a>

    <a id="_CPPv3N21aud_dac_status_mask_t24AUD_DACR_NEAR_EMPTY_MASKE"></a> <a id="_CPPv2N21aud_dac_status_mask_t24AUD_DACR_NEAR_EMPTY_MASKE"></a> <a id="group__bk__api__aud__enum_1gga76aa61164a2e7c641acbd08501be0bd3a04d564cd687ffde1c74c34c3015b9287"></a> enumerator AUD\_DACR\_NEAR\_EMPTY\_MASK
    :   AUD DAC right channel fifo near empty

    <a id="_CPPv4N21aud_dac_status_mask_t24AUD_DACL_NEAR_EMPTY_MASKE"></a>

    <a id="_CPPv3N21aud_dac_status_mask_t24AUD_DACL_NEAR_EMPTY_MASKE"></a> <a id="_CPPv2N21aud_dac_status_mask_t24AUD_DACL_NEAR_EMPTY_MASKE"></a> <a id="group__bk__api__aud__enum_1gga76aa61164a2e7c641acbd08501be0bd3ae4c8e1196da2f19a9d99375050924932"></a> enumerator AUD\_DACL\_NEAR\_EMPTY\_MASK
    :   AUD DAC left channel fifo near empty

    <a id="_CPPv4N21aud_dac_status_mask_t23AUD_DACR_FIFO_FULL_MASKE"></a>

    <a id="_CPPv3N21aud_dac_status_mask_t23AUD_DACR_FIFO_FULL_MASKE"></a> <a id="_CPPv2N21aud_dac_status_mask_t23AUD_DACR_FIFO_FULL_MASKE"></a> <a id="group__bk__api__aud__enum_1gga76aa61164a2e7c641acbd08501be0bd3ae043c3766b2087969758c3e73e7cd0df"></a> enumerator AUD\_DACR\_FIFO\_FULL\_MASK
    :   AUD DAC right channel fifo full

    <a id="_CPPv4N21aud_dac_status_mask_t23AUD_DACL_FIFO_FULL_MASKE"></a>

    <a id="_CPPv3N21aud_dac_status_mask_t23AUD_DACL_FIFO_FULL_MASKE"></a> <a id="_CPPv2N21aud_dac_status_mask_t23AUD_DACL_FIFO_FULL_MASKE"></a> <a id="group__bk__api__aud__enum_1gga76aa61164a2e7c641acbd08501be0bd3ab6470df0ce6b5fec39f6d90606073389"></a> enumerator AUD\_DACL\_FIFO\_FULL\_MASK
    :   AUD DAC left channel fifo full

    <a id="_CPPv4N21aud_dac_status_mask_t24AUD_DACR_FIFO_EMPTY_MASKE"></a>

    <a id="_CPPv3N21aud_dac_status_mask_t24AUD_DACR_FIFO_EMPTY_MASKE"></a> <a id="_CPPv2N21aud_dac_status_mask_t24AUD_DACR_FIFO_EMPTY_MASKE"></a> <a id="group__bk__api__aud__enum_1gga76aa61164a2e7c641acbd08501be0bd3a71ceebb81a2c5fc7f592409dc67b388f"></a> enumerator AUD\_DACR\_FIFO\_EMPTY\_MASK
    :   AUD DAC right channel fifo empty

    <a id="_CPPv4N21aud_dac_status_mask_t24AUD_DACL_FIFO_EMPTY_MASKE"></a>

    <a id="_CPPv3N21aud_dac_status_mask_t24AUD_DACL_FIFO_EMPTY_MASKE"></a> <a id="_CPPv2N21aud_dac_status_mask_t24AUD_DACL_FIFO_EMPTY_MASKE"></a> <a id="group__bk__api__aud__enum_1gga76aa61164a2e7c641acbd08501be0bd3a7fc66057e65797471e19538fa902ee4f"></a> enumerator AUD\_DACL\_FIFO\_EMPTY\_MASK
    :   AUD DAC left channel fifo empty
