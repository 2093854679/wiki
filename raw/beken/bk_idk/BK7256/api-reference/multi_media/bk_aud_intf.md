---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/api-reference/multi_media/bk_aud_intf.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="aud-intf-apis"></a>

# Aud\_Intf APIs

重要

The Aud\_Intf API v1.0 is the lastest and stable Audio interface APIs. All new applications should use Audio interface API v1.0.
And all Aud\_Intf API cannot be called in mic and speaker callback registed in bk\_aud\_intf\_drv\_init .

<a id="audio-interface"></a>

## Audio Interface

The BK Audio interface supports two work mode:
:   - General mode
    - Voice mode

The general work mode supports general functions, and the Voice mode supports voice transfer functions. However, the audio only work in one mode at a time.

The General mode supports following functions:
:   - record function
    - play function

The record and play function can be operated independently.

The Voice mode supports following features:
:   - voice transfer by G711A data
    - voice transfer by PCM data
    - 8k and 16k sample rate
    - software AEC
    - set mic gain
    - set speaker gain
    - onboard mic and speaker
    - UAC mic and speaker

<a id="audio-interface-api-categories"></a>

## Audio Interface API Categories

Most of Audio APIs can be categoried as:

> - Common APIs
>
>   The common APIs are prefixed with bk\_aud\_intf, the APIs may be common for General mode and Voice mode, e.g. bk\_aud\_intf\_drv\_init() etc.
> - Mic function APIs.
>
>   The APIs provide support for record function. e.g. bk\_aud\_intf\_mic\_init() etc.
> - Spk function APIs.
>
>   The APIs provide support for play function. e.g. bk\_aud\_intf\_spk\_init() etc.
> - Voc function APIs.
>
>   The APIs provide support for voice transfer function. e.g. bk\_aud\_intf\_voc\_init() etc.

Common APIs:
:   - [`bk_aud_intf_drv_init()`](#_CPPv420bk_aud_intf_drv_initP20aud_intf_drv_setup_t "bk_aud_intf_drv_init") \- init the audio interface driver
    - [`bk_aud_intf_drv_deinit()`](#_CPPv422bk_aud_intf_drv_deinitv "bk_aud_intf_drv_deinit") \- deinit the audio interface driver
    - [`bk_aud_intf_set_mode()`](#_CPPv420bk_aud_intf_set_mode20aud_intf_work_mode_t "bk_aud_intf_set_mode") \- set audio interface work mode
    - [`bk_aud_intf_set_mic_gain()`](#_CPPv424bk_aud_intf_set_mic_gain7uint8_t "bk_aud_intf_set_mic_gain") \- set audio mic gain
    - [`bk_aud_intf_set_spk_gain()`](#_CPPv424bk_aud_intf_set_spk_gain8uint32_t "bk_aud_intf_set_spk_gain") \- set audio speaker gain
    - [`bk_aud_intf_write_spk_data()`](#_CPPv426bk_aud_intf_write_spk_dataP7uint8_t8uint32_t "bk_aud_intf_write_spk_data") \- write data to sperker

Mic APIs:
:   - [`bk_aud_intf_mic_init()`](#_CPPv420bk_aud_intf_mic_initP20aud_intf_mic_setup_t "bk_aud_intf_mic_init") \- init the mic function
    - [`bk_aud_intf_mic_deinit()`](#_CPPv422bk_aud_intf_mic_deinitv "bk_aud_intf_mic_deinit") \- deinit the mic function
    - [`bk_aud_intf_mic_start()`](#_CPPv421bk_aud_intf_mic_startv "bk_aud_intf_mic_start") \- start mic work
    - [`bk_aud_intf_mic_pause()`](#_CPPv421bk_aud_intf_mic_pausev "bk_aud_intf_mic_pause") \- pause mic work
    - [`bk_aud_intf_mic_stop()`](#_CPPv420bk_aud_intf_mic_stopv "bk_aud_intf_mic_stop") \- stop mic work
    - [`bk_aud_intf_set_mic_chl()`](#_CPPv423bk_aud_intf_set_mic_chl18aud_intf_mic_chl_t "bk_aud_intf_set_mic_chl") \- set mic channel in work
    - [`bk_aud_intf_get_mic_chl()`](#_CPPv423bk_aud_intf_get_mic_chlP18aud_intf_mic_chl_t "bk_aud_intf_get_mic_chl") \- get mic channel in work
    - [`bk_aud_intf_set_mic_samp_rate()`](#_CPPv429bk_aud_intf_set_mic_samp_rate19aud_adc_samp_rate_t "bk_aud_intf_set_mic_samp_rate") \- set mic sample rate
    - [`bk_aud_intf_get_mic_samp_rate()`](#_CPPv429bk_aud_intf_get_mic_samp_rateP19aud_adc_samp_rate_t "bk_aud_intf_get_mic_samp_rate") \- get mic sample rate

Spk APIs:
:   - [`bk_aud_intf_spk_init()`](#_CPPv420bk_aud_intf_spk_initP20aud_intf_spk_setup_t "bk_aud_intf_spk_init") \- init the speaker function
    - [`bk_aud_intf_spk_deinit()`](#_CPPv422bk_aud_intf_spk_deinitv "bk_aud_intf_spk_deinit") \- deinit the speaker function
    - [`bk_aud_intf_spk_start()`](#_CPPv421bk_aud_intf_spk_startv "bk_aud_intf_spk_start") \- start speaker work
    - [`bk_aud_intf_spk_pause()`](#_CPPv421bk_aud_intf_spk_pausev "bk_aud_intf_spk_pause") \- pause speaker work
    - [`bk_aud_intf_spk_stop()`](#_CPPv420bk_aud_intf_spk_stopv "bk_aud_intf_spk_stop") \- stop speaker work
    - [`bk_aud_intf_set_spk_chl()`](#_CPPv423bk_aud_intf_set_spk_chl18aud_intf_spk_chl_t "bk_aud_intf_set_spk_chl") \- set speaker channel in work
    - [`bk_aud_intf_get_spk_chl()`](#_CPPv423bk_aud_intf_get_spk_chlP18aud_intf_mic_chl_t "bk_aud_intf_get_spk_chl") \- get speaker channel in work
    - [`bk_aud_intf_set_spk_samp_rate()`](#_CPPv429bk_aud_intf_set_spk_samp_rate19aud_dac_samp_rate_t "bk_aud_intf_set_spk_samp_rate") \- set speaker sample rate
    - [`bk_aud_intf_get_spk_samp_rate()`](#_CPPv429bk_aud_intf_get_spk_samp_rateP19aud_dac_samp_rate_t "bk_aud_intf_get_spk_samp_rate") \- get speaker sample rate

Voc APIs:
:   - [`bk_aud_intf_voc_init()`](#_CPPv420bk_aud_intf_voc_init20aud_intf_voc_setup_t "bk_aud_intf_voc_init") \- init the voice transfer function
    - [`bk_aud_intf_voc_deinit()`](#_CPPv422bk_aud_intf_voc_deinitv "bk_aud_intf_voc_deinit") \- deinit the voice transfer function
    - [`bk_aud_intf_voc_start()`](#_CPPv421bk_aud_intf_voc_startv "bk_aud_intf_voc_start") \- start voice transfer
    - [`bk_aud_intf_voc_stop()`](#_CPPv420bk_aud_intf_voc_stopv "bk_aud_intf_voc_stop") \- stop voice transfer
    - [`bk_aud_intf_set_aec_para()`](#_CPPv424bk_aud_intf_set_aec_para23aud_intf_voc_aec_para_t8uint32_t "bk_aud_intf_set_aec_para") \- set aec parameter
    - [`bk_aud_intf_get_aec_para()`](#_CPPv424bk_aud_intf_get_aec_parav "bk_aud_intf_get_aec_para") \- get aec parameter
    - [`bk_aud_intf_voc_tx_debug()`](#_CPPv424bk_aud_intf_voc_tx_debug27aud_intf_dump_data_callback "bk_aud_intf_voc_tx_debug") \- register voice tx debug callback
    - [`bk_aud_intf_voc_rx_debug()`](#_CPPv424bk_aud_intf_voc_rx_debug27aud_intf_dump_data_callback "bk_aud_intf_voc_rx_debug") \- register voice rx debug callback
    - [`bk_aud_intf_voc_aec_debug()`](#_CPPv425bk_aud_intf_voc_aec_debug27aud_intf_dump_data_callback "bk_aud_intf_voc_aec_debug") \- register voice aec debug callback

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [aud\_intf.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/aud_intf.h)

<a id="functions"></a>

### Functions

<a id="_CPPv420bk_aud_intf_drv_initP20aud_intf_drv_setup_t"></a>

<a id="_CPPv320bk_aud_intf_drv_initP20aud_intf_drv_setup_t"></a> <a id="_CPPv220bk_aud_intf_drv_initP20aud_intf_drv_setup_t"></a> <a id="bk_aud_intf_drv_init__aud_intf_drv_setup_tP"></a> <a id="group__bk__aud__intf__api_1ga84b200fb68d698a882d0b9c5071e295b"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_drv\_init([aud\_intf\_drv\_setup\_t](#_CPPv420aud_intf_drv_setup_t "aud_intf_drv_setup_t") \*setup)
:   Init the AUD INTF driver.

    This API init the resoure common:

    - Creat AUD INTF task
    - Configure default work mode
    - Register read mic data and write speaker data callback

    This API should be called before any other AUD INTF APIs. This API cannot be called in mic and speaker callback.

    参数
    :   **setup** – audio interface driver init configuration

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv422bk_aud_intf_drv_deinitv"></a>

<a id="_CPPv322bk_aud_intf_drv_deinitv"></a> <a id="_CPPv222bk_aud_intf_drv_deinitv"></a> <a id="bk_aud_intf_drv_deinit__void"></a> <a id="group__bk__aud__intf__api_1ga63d950fca1c9c131f89f7c8c1b069ded"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_drv\_deinit(void)
:   Deinit the AUD INTF driver.

    This API deinit the resoure common:

    - Delete AUD INTF task
    - Reset default work mode
    - Unregister read mic data and write speaker data callback

    This API should be called when audio is not needed. This API cannot be called in mic and speaker callback.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_aud_intf_set_mode20aud_intf_work_mode_t"></a>

<a id="_CPPv320bk_aud_intf_set_mode20aud_intf_work_mode_t"></a> <a id="_CPPv220bk_aud_intf_set_mode20aud_intf_work_mode_t"></a> <a id="bk_aud_intf_set_mode__aud_intf_work_mode_t"></a> <a id="group__bk__aud__intf__api_1ga73d297a84993cc7c1a05c8c110f67194"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_set\_mode([aud\_intf\_work\_mode\_t](#_CPPv420aud_intf_work_mode_t "aud_intf_work_mode_t") work\_mode)
:   Set the AUD INTF work mode.

    This API cannot be called in mic and speaker callback.

    参数
    :   **work\_mode** – audio interface work mode

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_aud_intf_set_mic_gain7uint8_t"></a>

<a id="_CPPv324bk_aud_intf_set_mic_gain7uint8_t"></a> <a id="_CPPv224bk_aud_intf_set_mic_gain7uint8_t"></a> <a id="bk_aud_intf_set_mic_gain__uint8_t"></a> <a id="group__bk__aud__intf__api_1ga13fbb661ad091bff2bf4b95206dba6d0"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_set\_mic\_gain(uint8\_t value)
:   Set the mic gain.

    This API should be called when onboard mic has been initialized. And this API should not be called when UAC mic has been used. This API cannot be called in mic and speaker callback.

    参数
    :   **value** – the gain value range:0x00 \~ 0x3f

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_aud_intf_set_spk_gain8uint32_t"></a>

<a id="_CPPv324bk_aud_intf_set_spk_gain8uint32_t"></a> <a id="_CPPv224bk_aud_intf_set_spk_gain8uint32_t"></a> <a id="bk_aud_intf_set_spk_gain__uint32_t"></a> <a id="group__bk__aud__intf__api_1ga08167372cefe6f8f39d2ff0378bec0df"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_set\_spk\_gain(uint32\_t value)
:   Set the spk gain(volume)

    This API should be called when speaker has been initialized. And this API set board speaker gain and uac speaker volume. This API cannot be called in mic and speaker callback.

    参数
    :   **value** – the gain value -board speaker: range:0x00 \~ 0x3f -uac speaker: range:0x0000 \~ 0xffff

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_aud_intf_set_aec_para23aud_intf_voc_aec_para_t8uint32_t"></a>

<a id="_CPPv324bk_aud_intf_set_aec_para23aud_intf_voc_aec_para_t8uint32_t"></a> <a id="_CPPv224bk_aud_intf_set_aec_para23aud_intf_voc_aec_para_t8uint32_t"></a> <a id="bk_aud_intf_set_aec_para__aud_intf_voc_aec_para_t.uint32_t"></a> <a id="group__bk__aud__intf__api_1ga6308cb91f4a55a295fb468c826858849"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_set\_aec\_para([aud\_intf\_voc\_aec\_para\_t](#_CPPv423aud_intf_voc_aec_para_t "aud_intf_voc_aec_para_t") aec\_para, uint32\_t value)
:   Set the aec parameter.

    This API should be called when voice has been initialized and AEC is enable. This API cannot be called in mic and speaker callback.

    参数
    :   - **aec\_para** – the parameter
        - **value** – the parameter value

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_aud_intf_get_aec_parav"></a>

<a id="_CPPv324bk_aud_intf_get_aec_parav"></a> <a id="_CPPv224bk_aud_intf_get_aec_parav"></a> <a id="bk_aud_intf_get_aec_para__void"></a> <a id="group__bk__aud__intf__api_1ga2298e74d80b1e1c80403e8ce45497073"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_get\_aec\_para(void)
:   Get the aec parameter.

    This API should be called when voice has been initialized and AEC is enable. This API cannot be called in mic and speaker callback.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_aud_intf_mic_initP20aud_intf_mic_setup_t"></a>

<a id="_CPPv320bk_aud_intf_mic_initP20aud_intf_mic_setup_t"></a> <a id="_CPPv220bk_aud_intf_mic_initP20aud_intf_mic_setup_t"></a> <a id="bk_aud_intf_mic_init__aud_intf_mic_setup_tP"></a> <a id="group__bk__aud__intf__api_1gad1b940c3b5527db6f669614571b557c0"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_mic\_init([aud\_intf\_mic\_setup\_t](#_CPPv420aud_intf_mic_setup_t "aud_intf_mic_setup_t") \*mic\_setup)
:   Init the AUD INTF mic.

    This API init the resoure common:

    - Init AUD adc driver
    - Configure AUD adc paramter
    - Configure DMA to carry adc data
    - Configure UAC mic

    This API should be called after bk\_aud\_intf\_drv\_init. This API cannot be called in mic and speaker callback.

    Usage example:

    ```
    audio_tras_setup_t aud_tras_setup = DEFAULT_AUD_INTF_DRV_SETUP_CONFIG();
    aud_intf_mic_setup_t aud_mic_setup = DEFAULT_AUD_INTF_MIC_SETUP_CONFIG();

    aud_intf_drv_setup.work_mode = AUD_INTF_WORK_MODE_NULL;
    aud_intf_drv_setup.aud_intf_tx_mic_data = demo_udp_voice_send_packet;
    bk_aud_intf_drv_init(&aud_intf_drv_setup);

    aud_work_mode = AUD_INTF_WORK_MODE_GENERAL;
    bk_aud_intf_set_mode(aud_work_mode);

    bk_aud_intf_mic_init(&aud_intf_mic_setup);
    ```

    参数
    :   **mic\_setup** – audio adc setup configuration

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv422bk_aud_intf_mic_deinitv"></a>

<a id="_CPPv322bk_aud_intf_mic_deinitv"></a> <a id="_CPPv222bk_aud_intf_mic_deinitv"></a> <a id="bk_aud_intf_mic_deinit__void"></a> <a id="group__bk__aud__intf__api_1ga933d97e950688a4a24f73dab814f6dd8"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_mic\_deinit(void)
:   Deinit the AUD INTF mic.

    This API deinit the resoure common:

    - Deinit AUD adc driver
    - Reset AUD adc paramter
    - Close DMA
    - Close UAC mic

    This API should be called after bk\_aud\_intf\_mic\_stop. This API cannot be called in mic and speaker callback.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_aud_intf_mic_startv"></a>

<a id="_CPPv321bk_aud_intf_mic_startv"></a> <a id="_CPPv221bk_aud_intf_mic_startv"></a> <a id="bk_aud_intf_mic_start__void"></a> <a id="group__bk__aud__intf__api_1ga5423319747f78127219e9ec061e5b1b4"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_mic\_start(void)
:   Start the AUD INTF mic work.

    This API cannot be called in mic and speaker callback.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_aud_intf_mic_pausev"></a>

<a id="_CPPv321bk_aud_intf_mic_pausev"></a> <a id="_CPPv221bk_aud_intf_mic_pausev"></a> <a id="bk_aud_intf_mic_pause__void"></a> <a id="group__bk__aud__intf__api_1gab2a81efdb476c67d24218a172cf1fc52"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_mic\_pause(void)
:   Pause the AUD INTF mic work.

    This API should be called after bk\_aud\_intf\_mic\_init. This API cannot be called in mic and speaker callback.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_aud_intf_mic_stopv"></a>

<a id="_CPPv320bk_aud_intf_mic_stopv"></a> <a id="_CPPv220bk_aud_intf_mic_stopv"></a> <a id="bk_aud_intf_mic_stop__void"></a> <a id="group__bk__aud__intf__api_1ga734d66a632e2de5f88b7716c99998e2f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_mic\_stop(void)
:   Stop the AUD INTF mic work.

    This API cannot be called in mic and speaker callback.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv423bk_aud_intf_set_mic_chl18aud_intf_mic_chl_t"></a>

<a id="_CPPv323bk_aud_intf_set_mic_chl18aud_intf_mic_chl_t"></a> <a id="_CPPv223bk_aud_intf_set_mic_chl18aud_intf_mic_chl_t"></a> <a id="bk_aud_intf_set_mic_chl__aud_intf_mic_chl_t"></a> <a id="group__bk__aud__intf__api_1ga3de9000330b840f22034dd4389fd657d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_set\_mic\_chl([aud\_intf\_mic\_chl\_t](#_CPPv418aud_intf_mic_chl_t "aud_intf_mic_chl_t") mic\_chl)
:   Set the AUD INTF mic channel.

    This API should be called after bk\_aud\_intf\_mic\_init. This API only support onboard mic, and not support UAC mic. This API cannot be called in mic and speaker callback.

    参数
    :   **mic\_chl** – audio interface mic channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv423bk_aud_intf_get_mic_chlP18aud_intf_mic_chl_t"></a>

<a id="_CPPv323bk_aud_intf_get_mic_chlP18aud_intf_mic_chl_t"></a> <a id="_CPPv223bk_aud_intf_get_mic_chlP18aud_intf_mic_chl_t"></a> <a id="bk_aud_intf_get_mic_chl__aud_intf_mic_chl_tP"></a> <a id="group__bk__aud__intf__api_1ga4fab21e7a510d656f5cf9b8f7942a826"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_get\_mic\_chl([aud\_intf\_mic\_chl\_t](#_CPPv418aud_intf_mic_chl_t "aud_intf_mic_chl_t") \*mic\_chl)
:   Get the AUD INTF mic channel.

    This API should be called after bk\_aud\_intf\_mic\_init. This API only support onboard mic, and not support UAC mic. This API cannot be called in mic and speaker callback.

    参数
    :   **mic\_chl** – save audio interface mic channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv429bk_aud_intf_set_mic_samp_rate19aud_adc_samp_rate_t"></a>

<a id="_CPPv329bk_aud_intf_set_mic_samp_rate19aud_adc_samp_rate_t"></a> <a id="_CPPv229bk_aud_intf_set_mic_samp_rate19aud_adc_samp_rate_t"></a> <a id="bk_aud_intf_set_mic_samp_rate__aud_adc_samp_rate_t"></a> <a id="group__bk__aud__intf__api_1gaec84b24cb0dcf5070adb32da540ad4e6"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_set\_mic\_samp\_rate([aud\_adc\_samp\_rate\_t](bk_audio.md#_CPPv419aud_adc_samp_rate_t "aud_adc_samp_rate_t") samp\_rate)
:   Set the AUD INTF mic sample rate.

    This API should be called after bk\_aud\_intf\_mic\_init. This API only support onboard mic, and not support UAC mic. This API cannot be called in mic and speaker callback.

    参数
    :   **samp\_rate** – audio interface mic sample rate

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv429bk_aud_intf_get_mic_samp_rateP19aud_adc_samp_rate_t"></a>

<a id="_CPPv329bk_aud_intf_get_mic_samp_rateP19aud_adc_samp_rate_t"></a> <a id="_CPPv229bk_aud_intf_get_mic_samp_rateP19aud_adc_samp_rate_t"></a> <a id="bk_aud_intf_get_mic_samp_rate__aud_adc_samp_rate_tP"></a> <a id="group__bk__aud__intf__api_1gadac4550d2d2211b88ad1a2986365bd79"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_get\_mic\_samp\_rate([aud\_adc\_samp\_rate\_t](bk_audio.md#_CPPv419aud_adc_samp_rate_t "aud_adc_samp_rate_t") \*samp\_rate)
:   Get the AUD INTF mic sample rate.

    This API should be called after bk\_aud\_intf\_mic\_init. This API only support onboard mic, and not support UAC mic. This API cannot be called in mic and speaker callback.

    参数
    :   **samp\_rate** – save audio interface mic sample rate

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_aud_intf_spk_initP20aud_intf_spk_setup_t"></a>

<a id="_CPPv320bk_aud_intf_spk_initP20aud_intf_spk_setup_t"></a> <a id="_CPPv220bk_aud_intf_spk_initP20aud_intf_spk_setup_t"></a> <a id="bk_aud_intf_spk_init__aud_intf_spk_setup_tP"></a> <a id="group__bk__aud__intf__api_1ga7d54cf95643b73f181671d010e759114"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_spk\_init([aud\_intf\_spk\_setup\_t](#_CPPv420aud_intf_spk_setup_t "aud_intf_spk_setup_t") \*spk\_setup)
:   Init the AUD INTF speaker.

    This API init the resoure common:

    - Init AUD dac driver
    - Configure AUD dac paramter
    - Configure DMA to carry dac data
    - Configure UAC speaker

    This API should be called after bk\_aud\_intf\_drv\_init. This API cannot be called in mic and speaker callback.

    Usage example:

    ```
    audio_tras_setup_t aud_tras_setup = DEFAULT_AUD_INTF_DRV_SETUP_CONFIG();
    aud_intf_spk_setup_t aud_spk_setup = DEFAULT_AUD_INTF_SPK_SETUP_CONFIG();

    aud_intf_drv_setup.aud_intf_rx_spk_data = aud_read_pcm_data_from_sd;
    bk_aud_intf_drv_init(&aud_intf_drv_setup);

    aud_work_mode = AUD_INTF_WORK_MODE_GENERAL;
    bk_aud_intf_set_mode(aud_work_mode);

    aud_intf_spk_setup.frame_size = 640;
    bk_aud_intf_spk_init(&aud_intf_spk_setup);
    ```

    参数
    :   **spk\_setup** – audio speaker setup configuration

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv422bk_aud_intf_spk_deinitv"></a>

<a id="_CPPv322bk_aud_intf_spk_deinitv"></a> <a id="_CPPv222bk_aud_intf_spk_deinitv"></a> <a id="bk_aud_intf_spk_deinit__void"></a> <a id="group__bk__aud__intf__api_1ga52d05e015ebae16859b25250e974d43f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_spk\_deinit(void)
:   Deinit the AUD INTF speaker.

    This API deinit the resoure common:

    - Deinit AUD dac driver
    - Reset AUD dac paramter
    - Close DMA
    - Close UAC speaker

    This API should be called after bk\_aud\_intf\_spk\_stop. This API cannot be called in mic and speaker callback.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_aud_intf_spk_startv"></a>

<a id="_CPPv321bk_aud_intf_spk_startv"></a> <a id="_CPPv221bk_aud_intf_spk_startv"></a> <a id="bk_aud_intf_spk_start__void"></a> <a id="group__bk__aud__intf__api_1ga0a2f0c7b9d13a344921c138c9002d4c8"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_spk\_start(void)
:   Start the AUD INTF speaker work.

    This API cannot be called in mic and speaker callback.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_aud_intf_spk_pausev"></a>

<a id="_CPPv321bk_aud_intf_spk_pausev"></a> <a id="_CPPv221bk_aud_intf_spk_pausev"></a> <a id="bk_aud_intf_spk_pause__void"></a> <a id="group__bk__aud__intf__api_1ga8035f23b29e5581fa8c51b59ef2a3907"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_spk\_pause(void)
:   Pause the AUD INTF speaker work.

    This API cannot be called in mic and speaker callback.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_aud_intf_spk_stopv"></a>

<a id="_CPPv320bk_aud_intf_spk_stopv"></a> <a id="_CPPv220bk_aud_intf_spk_stopv"></a> <a id="bk_aud_intf_spk_stop__void"></a> <a id="group__bk__aud__intf__api_1ga8498c3a714bdfa43e8c5ea5add604ef0"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_spk\_stop(void)
:   Stop the AUD INTF speaker work.

    This API cannot be called in mic and speaker callback.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv423bk_aud_intf_set_spk_chl18aud_intf_spk_chl_t"></a>

<a id="_CPPv323bk_aud_intf_set_spk_chl18aud_intf_spk_chl_t"></a> <a id="_CPPv223bk_aud_intf_set_spk_chl18aud_intf_spk_chl_t"></a> <a id="bk_aud_intf_set_spk_chl__aud_intf_spk_chl_t"></a> <a id="group__bk__aud__intf__api_1ga782c9e4a5d6f4ba43b14a4ed36572c52"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_set\_spk\_chl([aud\_intf\_spk\_chl\_t](#_CPPv418aud_intf_spk_chl_t "aud_intf_spk_chl_t") spk\_chl)
:   Set the AUD INTF speaker channel.

    This API should be called after bk\_aud\_intf\_spk\_init. This API only support onboard speaker, and not support UAC speaker. This API cannot be called in mic and speaker callback.

    参数
    :   **spk\_chl** – audio interface speaker channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv423bk_aud_intf_get_spk_chlP18aud_intf_mic_chl_t"></a>

<a id="_CPPv323bk_aud_intf_get_spk_chlP18aud_intf_mic_chl_t"></a> <a id="_CPPv223bk_aud_intf_get_spk_chlP18aud_intf_mic_chl_t"></a> <a id="bk_aud_intf_get_spk_chl__aud_intf_mic_chl_tP"></a> <a id="group__bk__aud__intf__api_1ga7624a4ddfebf0031c252d79c4e3fa9ec"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_get\_spk\_chl([aud\_intf\_mic\_chl\_t](#_CPPv418aud_intf_mic_chl_t "aud_intf_mic_chl_t") \*spk\_chl)
:   Get the AUD INTF speaker channel.

    This API should be called after bk\_aud\_intf\_spk\_init. This API only support onboard speaker, and not support UAC speaker. This API cannot be called in mic and speaker callback.

    参数
    :   **spk\_chl** – save audio interface speaker channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv429bk_aud_intf_set_spk_samp_rate19aud_dac_samp_rate_t"></a>

<a id="_CPPv329bk_aud_intf_set_spk_samp_rate19aud_dac_samp_rate_t"></a> <a id="_CPPv229bk_aud_intf_set_spk_samp_rate19aud_dac_samp_rate_t"></a> <a id="bk_aud_intf_set_spk_samp_rate__aud_dac_samp_rate_t"></a> <a id="group__bk__aud__intf__api_1ga0cc8e4536db3e1e5f8b0b7f894187578"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_set\_spk\_samp\_rate([aud\_dac\_samp\_rate\_t](bk_audio.md#_CPPv419aud_dac_samp_rate_t "aud_dac_samp_rate_t") samp\_rate)
:   Set the AUD INTF speaker sample rate.

    This API should be called after bk\_aud\_intf\_spk\_init. This API only support onboard speaker, and not support UAC speaker. This API cannot be called in mic and speaker callback.

    参数
    :   **samp\_rate** – audio interface speaker sample rate

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv429bk_aud_intf_get_spk_samp_rateP19aud_dac_samp_rate_t"></a>

<a id="_CPPv329bk_aud_intf_get_spk_samp_rateP19aud_dac_samp_rate_t"></a> <a id="_CPPv229bk_aud_intf_get_spk_samp_rateP19aud_dac_samp_rate_t"></a> <a id="bk_aud_intf_get_spk_samp_rate__aud_dac_samp_rate_tP"></a> <a id="group__bk__aud__intf__api_1ga0db5adc8f47fe8df33668f7c3cd66ee0"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_get\_spk\_samp\_rate([aud\_dac\_samp\_rate\_t](bk_audio.md#_CPPv419aud_dac_samp_rate_t "aud_dac_samp_rate_t") \*samp\_rate)
:   Get the AUD INTF speaker sample rate.

    This API should be called after bk\_aud\_intf\_spk\_init. This API only support onboard speaker, and not support UAC speaker. This API cannot be called in mic and speaker callback.

    参数
    :   **samp\_rate** – save audio interface speaker sample rate

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv441bk_aud_intf_register_uac_connect_state_cbPv"></a>

<a id="_CPPv341bk_aud_intf_register_uac_connect_state_cbPv"></a> <a id="_CPPv241bk_aud_intf_register_uac_connect_state_cbPv"></a> <a id="bk_aud_intf_register_uac_connect_state_cb__voidP"></a> <a id="group__bk__aud__intf__api_1gad83d82c4bda5738cab4396516fd172a0"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_register\_uac\_connect\_state\_cb(void \*cb)
:   Register callback of uac abnormal disconnection and connection recovery.

    This API should be called after bk\_aud\_intf\_spk\_init. This API only support uac mic and uac speaker. This API cannot be called in mic and speaker callback.

    参数
    :   **cb** – callback api

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv433bk_aud_intf_uac_auto_connect_ctrlb"></a>

<a id="_CPPv333bk_aud_intf_uac_auto_connect_ctrlb"></a> <a id="_CPPv233bk_aud_intf_uac_auto_connect_ctrlb"></a> <a id="bk_aud_intf_uac_auto_connect_ctrl__b"></a> <a id="group__bk__aud__intf__api_1ga1b9eb0db5d906859d91d5175f7e3b072"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_uac\_auto\_connect\_ctrl(bool enable)
:   Control uac automatical connect.

    If enable the feature, uac will automatic connect after uac abnormal disconnect. This API only support uac mic and uac speaker. This feature is enabled by default. This API cannot be called in mic and speaker callback.

    参数
    :   **enable** –

        - TRUE: enable uac automatic connnet
        - FALSE: disable uac automatic connent

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_aud_intf_voc_init20aud_intf_voc_setup_t"></a>

<a id="_CPPv320bk_aud_intf_voc_init20aud_intf_voc_setup_t"></a> <a id="_CPPv220bk_aud_intf_voc_init20aud_intf_voc_setup_t"></a> <a id="bk_aud_intf_voc_init__aud_intf_voc_setup_t"></a> <a id="group__bk__aud__intf__api_1ga2dbae5eae3e91bad107da15e36598251"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_voc\_init([aud\_intf\_voc\_setup\_t](#_CPPv420aud_intf_voc_setup_t "aud_intf_voc_setup_t") setup)
:   Init the AUD INTF voice.

    This API init the resoure common:

    - Init AUD voice transfer driver
    - Configure AUD dac and adc paramter
    - Configure DMA to carry adc and dac data
    - Configure UAC mic and speaker

    This API should be called after bk\_aud\_intf\_drv\_init. This API cannot be called in mic and speaker callback.

    Usage example:

    ```
    audio_tras_setup_t aud_tras_setup = DEFAULT_AUD_INTF_DRV_SETUP_CONFIG();
    aud_intf_voc_setup_t aud_voc_setup = DEFAULT_AUD_INTF_VOC_SETUP_CONFIG();

    aud_intf_drv_setup.aud_intf_tx_mic_data = demo_udp_voice_send_packet;
    bk_aud_intf_drv_init(&aud_intf_drv_setup);

    aud_work_mode = AUD_INTF_WORK_MODE_VOICE;
    bk_aud_intf_set_mode(aud_work_mode);

    bk_aud_intf_voc_init(aud_voc_setup);
    ```

    参数
    :   **voc\_setup** – audio voice setup configuration

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv422bk_aud_intf_voc_deinitv"></a>

<a id="_CPPv322bk_aud_intf_voc_deinitv"></a> <a id="_CPPv222bk_aud_intf_voc_deinitv"></a> <a id="bk_aud_intf_voc_deinit__void"></a> <a id="group__bk__aud__intf__api_1ga0e692a9331192b542434293d8498fdd3"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_voc\_deinit(void)
:   Deinit the AUD INTF voice.

    This API deinit the resoure common:

    - Deinit AUD voice transfer driver
    - Reset AUD adc and dac paramter
    - Close DMA

    This API should be called after bk\_aud\_intf\_voice\_stop. This API cannot be called in mic and speaker callback.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_aud_intf_voc_startv"></a>

<a id="_CPPv321bk_aud_intf_voc_startv"></a> <a id="_CPPv221bk_aud_intf_voc_startv"></a> <a id="bk_aud_intf_voc_start__void"></a> <a id="group__bk__aud__intf__api_1gabd00d0b82e6373e7e80e81abc07dce5a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_voc\_start(void)
:   Start the AUD INTF voice work.

    This API cannot be called in mic and speaker callback.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_aud_intf_voc_stopv"></a>

<a id="_CPPv320bk_aud_intf_voc_stopv"></a> <a id="_CPPv220bk_aud_intf_voc_stopv"></a> <a id="bk_aud_intf_voc_stop__void"></a> <a id="group__bk__aud__intf__api_1gaa9a70f8f6268742c997e776a81258383"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_voc\_stop(void)
:   Stop the AUD INTF voice work.

    This API cannot be called in mic and speaker callback.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_aud_intf_voc_mic_ctrl23aud_intf_voc_mic_ctrl_t"></a>

<a id="_CPPv324bk_aud_intf_voc_mic_ctrl23aud_intf_voc_mic_ctrl_t"></a> <a id="_CPPv224bk_aud_intf_voc_mic_ctrl23aud_intf_voc_mic_ctrl_t"></a> <a id="bk_aud_intf_voc_mic_ctrl__aud_intf_voc_mic_ctrl_t"></a> <a id="group__bk__aud__intf__api_1ga1cae4cbd1111ea7ed30a856fefc71179"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_voc\_mic\_ctrl([aud\_intf\_voc\_mic\_ctrl\_t](#_CPPv423aud_intf_voc_mic_ctrl_t "aud_intf_voc_mic_ctrl_t") mic\_en)
:   Control mic.

    This API should be called in voice work mode. This API cannot be called in mic and speaker callback.

    参数
    :   **mic\_en** –

        - AUD\_INTF\_VOC\_MIC\_OPEN: enable mic
        - AUD\_INTF\_VOC\_MIC\_CLOSE: disable mic

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_aud_intf_voc_spk_ctrl23aud_intf_voc_spk_ctrl_t"></a>

<a id="_CPPv324bk_aud_intf_voc_spk_ctrl23aud_intf_voc_spk_ctrl_t"></a> <a id="_CPPv224bk_aud_intf_voc_spk_ctrl23aud_intf_voc_spk_ctrl_t"></a> <a id="bk_aud_intf_voc_spk_ctrl__aud_intf_voc_spk_ctrl_t"></a> <a id="group__bk__aud__intf__api_1ga64364d0863faa5a961b936dba0c068a0"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_voc\_spk\_ctrl([aud\_intf\_voc\_spk\_ctrl\_t](#_CPPv423aud_intf_voc_spk_ctrl_t "aud_intf_voc_spk_ctrl_t") spk\_en)
:   Control speaker.

    This API should be called in voice work mode. This API cannot be called in mic and speaker callback.

    参数
    :   **spk\_en** –

        - AUD\_INTF\_VOC\_SPK\_OPEN: enable speaker
        - AUD\_INTF\_VOC\_SPK\_CLOSE: disable speaker

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_aud_intf_voc_aec_ctrlb"></a>

<a id="_CPPv324bk_aud_intf_voc_aec_ctrlb"></a> <a id="_CPPv224bk_aud_intf_voc_aec_ctrlb"></a> <a id="bk_aud_intf_voc_aec_ctrl__b"></a> <a id="group__bk__aud__intf__api_1ga3b56eefb3a83382ade65a5cf56621e08"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_voc\_aec\_ctrl(bool aec\_en)
:   Control aec enable or disable.

    This API should be called in voice work mode. This API cannot be called in mic and speaker callback.

    参数
    :   **aec\_en** –

        - true: enable aec
        - false: disable aec

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv426bk_aud_intf_write_spk_dataP7uint8_t8uint32_t"></a>

<a id="_CPPv326bk_aud_intf_write_spk_dataP7uint8_t8uint32_t"></a> <a id="_CPPv226bk_aud_intf_write_spk_dataP7uint8_t8uint32_t"></a> <a id="bk_aud_intf_write_spk_data__uint8_tP.uint32_t"></a> <a id="group__bk__aud__intf__api_1gab301b6b456acf8a05b8fe1d72f7de7ea"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_write\_spk\_data(uint8\_t \*dac\_buff, uint32\_t size)
:   Write the speaker data to audio dac.

    This API should be called in general and voice work mode. This API cannot be called in mic and speaker callback.

    参数
    :   - **dac\_buff** – the address of speaker data written
        - **size** – the data size (byte)

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_aud_intf_voc_tx_debug27aud_intf_dump_data_callback"></a>

<a id="_CPPv324bk_aud_intf_voc_tx_debug27aud_intf_dump_data_callback"></a> <a id="_CPPv224bk_aud_intf_voc_tx_debug27aud_intf_dump_data_callback"></a> <a id="bk_aud_intf_voc_tx_debug__aud_intf_dump_data_callback"></a> <a id="group__bk__aud__intf__api_1ga35347b6c05ddfea08606423a81f44e8e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_voc\_tx\_debug([aud\_intf\_dump\_data\_callback](#_CPPv427aud_intf_dump_data_callback "aud_intf_dump_data_callback") dump\_callback)
:   register callback to dump tx data in voice work mode

    This API should be called in voice work mode. And audio transfer driver will call the callback to save data. This API cannot be called in mic and speaker callback.

    参数
    :   **dump\_callback** – callback

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_aud_intf_voc_rx_debug27aud_intf_dump_data_callback"></a>

<a id="_CPPv324bk_aud_intf_voc_rx_debug27aud_intf_dump_data_callback"></a> <a id="_CPPv224bk_aud_intf_voc_rx_debug27aud_intf_dump_data_callback"></a> <a id="bk_aud_intf_voc_rx_debug__aud_intf_dump_data_callback"></a> <a id="group__bk__aud__intf__api_1gacde63f4c9394e927bb9adcb56715bdbc"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_voc\_rx\_debug([aud\_intf\_dump\_data\_callback](#_CPPv427aud_intf_dump_data_callback "aud_intf_dump_data_callback") dump\_callback)
:   register callback to dump rx data in voice work mode

    This API should be called in voice work mode. And audio transfer driver will call the callback to save data. This API cannot be called in mic and speaker callback.

    参数
    :   **dump\_callback** – callback

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv425bk_aud_intf_voc_aec_debug27aud_intf_dump_data_callback"></a>

<a id="_CPPv325bk_aud_intf_voc_aec_debug27aud_intf_dump_data_callback"></a> <a id="_CPPv225bk_aud_intf_voc_aec_debug27aud_intf_dump_data_callback"></a> <a id="bk_aud_intf_voc_aec_debug__aud_intf_dump_data_callback"></a> <a id="group__bk__aud__intf__api_1ga27b081f28f825457301837e3298a3173"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_aud\_intf\_voc\_aec\_debug([aud\_intf\_dump\_data\_callback](#_CPPv427aud_intf_dump_data_callback "aud_intf_dump_data_callback") dump\_callback)
:   register callback to dump aec data(include mic data, ref data, and out data) in voice work mode

    This API should be called in voice work mode. And audio transfer driver will call the callback to save data. This API cannot be called in mic and speaker callback.

    参数
    :   **dump\_callback** – callback

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="api-typedefs"></a>

## API Typedefs

<a id="id1"></a>

### Header File

- [aud\_intf\_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/aud_intf_types.h)

<a id="structures"></a>

### Structures

<a id="_CPPv422aud_intf_task_config_t"></a>

<a id="_CPPv322aud_intf_task_config_t"></a> <a id="_CPPv222aud_intf_task_config_t"></a> <a id="aud_intf_task_config_t"></a> <a id="structaud__intf__task__config__t"></a> struct aud\_intf\_task\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N22aud_intf_task_config_t8priorityE"></a>

    <a id="_CPPv3N22aud_intf_task_config_t8priorityE"></a> <a id="_CPPv2N22aud_intf_task_config_t8priorityE"></a> <a id="aud_intf_task_config_t::priority__uint8_t"></a> <a id="structaud__intf__task__config__t_1a47970d61409ed21d987b1edf025f0ca7"></a> uint8\_t priority
    :   the priority of audio interface task

<a id="_CPPv420aud_intf_drv_setup_t"></a>

<a id="_CPPv320aud_intf_drv_setup_t"></a> <a id="_CPPv220aud_intf_drv_setup_t"></a> <a id="aud_intf_drv_setup_t"></a> <a id="structaud__intf__drv__setup__t"></a> struct aud\_intf\_drv\_setup\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20aud_intf_drv_setup_t20aud_intf_tx_mic_dataE"></a>

    <a id="_CPPv3N20aud_intf_drv_setup_t20aud_intf_tx_mic_dataE"></a> <a id="_CPPv2N20aud_intf_drv_setup_t20aud_intf_tx_mic_dataE"></a> <a id="structaud__intf__drv__setup__t_1af1aa039eb81855af944d8335ea7ec7bb"></a> int (\*aud\_intf\_tx\_mic\_data)(unsigned char \*data, unsigned int size)
    :   the api is called when collecting a frame mic packet data is complete

    <a id="_CPPv4N20aud_intf_drv_setup_t20aud_intf_rx_spk_dataE"></a>

    <a id="_CPPv3N20aud_intf_drv_setup_t20aud_intf_rx_spk_dataE"></a> <a id="_CPPv2N20aud_intf_drv_setup_t20aud_intf_rx_spk_dataE"></a> <a id="structaud__intf__drv__setup__t_1a8cd3b593afd64a90e69d35154c1958e5"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") (\*aud\_intf\_rx\_spk\_data)(unsigned int size)
    :   the api is called when playing a frame speaker packet data is complete

<a id="_CPPv420aud_intf_mic_setup_t"></a>

<a id="_CPPv320aud_intf_mic_setup_t"></a> <a id="_CPPv220aud_intf_mic_setup_t"></a> <a id="aud_intf_mic_setup_t"></a> <a id="structaud__intf__mic__setup__t"></a> struct aud\_intf\_mic\_setup\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20aud_intf_mic_setup_t9samp_rateE"></a>

    <a id="_CPPv3N20aud_intf_mic_setup_t9samp_rateE"></a> <a id="_CPPv2N20aud_intf_mic_setup_t9samp_rateE"></a> <a id="aud_intf_mic_setup_t::samp_rate__aud_adc_samp_rate_t"></a> <a id="structaud__intf__mic__setup__t_1aadb2dcde3f99dd5df38ae6a35a927ca2"></a> [aud\_adc\_samp\_rate\_t](bk_audio.md#_CPPv419aud_adc_samp_rate_t "aud_adc_samp_rate_t") samp\_rate
    :   mic sample rate

    <a id="_CPPv4N20aud_intf_mic_setup_t10frame_sizeE"></a>

    <a id="_CPPv3N20aud_intf_mic_setup_t10frame_sizeE"></a> <a id="_CPPv2N20aud_intf_mic_setup_t10frame_sizeE"></a> <a id="aud_intf_mic_setup_t::frame_size__uint16_t"></a> <a id="structaud__intf__mic__setup__t_1ae64bbd304514d9ede47728b9078d2e1a"></a> uint16\_t frame\_size
    :   size: a frame packet mic data size(byte)

    <a id="_CPPv4N20aud_intf_mic_setup_t8mic_gainE"></a>

    <a id="_CPPv3N20aud_intf_mic_setup_t8mic_gainE"></a> <a id="_CPPv2N20aud_intf_mic_setup_t8mic_gainE"></a> <a id="aud_intf_mic_setup_t::mic_gain__uint8_t"></a> <a id="structaud__intf__mic__setup__t_1a8c9a05f9f8282c942b454dcd0682978a"></a> uint8\_t mic\_gain
    :   audio adc gain: value range:0x0 \~ 0x3f, suggest:0x2d

    <a id="_CPPv4N20aud_intf_mic_setup_t8mic_typeE"></a>

    <a id="_CPPv3N20aud_intf_mic_setup_t8mic_typeE"></a> <a id="_CPPv2N20aud_intf_mic_setup_t8mic_typeE"></a> <a id="aud_intf_mic_setup_t::mic_type__aud_intf_mic_type_t"></a> <a id="structaud__intf__mic__setup__t_1a5f21257907d316871b8ea7882650528b"></a> [aud\_intf\_mic\_type\_t](#_CPPv419aud_intf_mic_type_t "aud_intf_mic_type_t") mic\_type
    :   audio mic type: uac or microphone

    <a id="_CPPv4N20aud_intf_mic_setup_t8mic_modeE"></a>

    <a id="_CPPv3N20aud_intf_mic_setup_t8mic_modeE"></a> <a id="_CPPv2N20aud_intf_mic_setup_t8mic_modeE"></a> <a id="aud_intf_mic_setup_t::mic_mode__aud_adc_intf_mode_t"></a> <a id="structaud__intf__mic__setup__t_1a239c20db7d8499c6a2464e733c060c80"></a> [aud\_adc\_intf\_mode\_t](bk_audio.md#_CPPv419aud_adc_intf_mode_t "aud_adc_intf_mode_t") mic\_mode
    :   audio mic mode: signal\_ended/differen

<a id="_CPPv420aud_intf_spk_setup_t"></a>

<a id="_CPPv320aud_intf_spk_setup_t"></a> <a id="_CPPv220aud_intf_spk_setup_t"></a> <a id="aud_intf_spk_setup_t"></a> <a id="structaud__intf__spk__setup__t"></a> struct aud\_intf\_spk\_setup\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20aud_intf_spk_setup_t9samp_rateE"></a>

    <a id="_CPPv3N20aud_intf_spk_setup_t9samp_rateE"></a> <a id="_CPPv2N20aud_intf_spk_setup_t9samp_rateE"></a> <a id="aud_intf_spk_setup_t::samp_rate__aud_dac_samp_rate_t"></a> <a id="structaud__intf__spk__setup__t_1a91dc3a8f38277924ff3406de07c5ece6"></a> [aud\_dac\_samp\_rate\_t](bk_audio.md#_CPPv419aud_dac_samp_rate_t "aud_dac_samp_rate_t") samp\_rate
    :   speaker sample rate

    <a id="_CPPv4N20aud_intf_spk_setup_t10frame_sizeE"></a>

    <a id="_CPPv3N20aud_intf_spk_setup_t10frame_sizeE"></a> <a id="_CPPv2N20aud_intf_spk_setup_t10frame_sizeE"></a> <a id="aud_intf_spk_setup_t::frame_size__uint16_t"></a> <a id="structaud__intf__spk__setup__t_1acc59be04de5d73f6c3b38ee3538bda9e"></a> uint16\_t frame\_size
    :   size: a frame packet speaker data size(byte)

    <a id="_CPPv4N20aud_intf_spk_setup_t8spk_gainE"></a>

    <a id="_CPPv3N20aud_intf_spk_setup_t8spk_gainE"></a> <a id="_CPPv2N20aud_intf_spk_setup_t8spk_gainE"></a> <a id="aud_intf_spk_setup_t::spk_gain__uint8_t"></a> <a id="structaud__intf__spk__setup__t_1ac672f5335a19170d9b99d687fa786e52"></a> uint8\_t spk\_gain
    :   audio dac gain: value range:0x0 \~ 0x3f, suggest:0x2d

    <a id="_CPPv4N20aud_intf_spk_setup_t9work_modeE"></a>

    <a id="_CPPv3N20aud_intf_spk_setup_t9work_modeE"></a> <a id="_CPPv2N20aud_intf_spk_setup_t9work_modeE"></a> <a id="aud_intf_spk_setup_t::work_mode__aud_dac_work_mode_t"></a> <a id="structaud__intf__spk__setup__t_1ae78274fd35e803c8055229aa90095fa5"></a> [aud\_dac\_work\_mode\_t](bk_audio.md#_CPPv419aud_dac_work_mode_t "aud_dac_work_mode_t") work\_mode
    :   audio dac mode: signal\_ended/differen

    <a id="_CPPv4N20aud_intf_spk_setup_t8spk_typeE"></a>

    <a id="_CPPv3N20aud_intf_spk_setup_t8spk_typeE"></a> <a id="_CPPv2N20aud_intf_spk_setup_t8spk_typeE"></a> <a id="aud_intf_spk_setup_t::spk_type__aud_intf_spk_type_t"></a> <a id="structaud__intf__spk__setup__t_1aa602f2ba63526252a17bee0643239757"></a> [aud\_intf\_spk\_type\_t](#_CPPv419aud_intf_spk_type_t "aud_intf_spk_type_t") spk\_type
    :   audio speaker type: uac or speaker

<a id="_CPPv422aud_intf_voc_aec_cfg_t"></a>

<a id="_CPPv322aud_intf_voc_aec_cfg_t"></a> <a id="_CPPv222aud_intf_voc_aec_cfg_t"></a> <a id="aud_intf_voc_aec_cfg_t"></a> <a id="structaud__intf__voc__aec__cfg__t"></a> struct aud\_intf\_voc\_aec\_cfg\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N22aud_intf_voc_aec_cfg_t8ec_depthE"></a>

    <a id="_CPPv3N22aud_intf_voc_aec_cfg_t8ec_depthE"></a> <a id="_CPPv2N22aud_intf_voc_aec_cfg_t8ec_depthE"></a> <a id="aud_intf_voc_aec_cfg_t::ec_depth__uint32_t"></a> <a id="structaud__intf__voc__aec__cfg__t_1a4ca5bd097a27f13f0e456b6491d96e88"></a> uint32\_t ec\_depth
    :   recommended value range: 1\~50, the greater the echo, the greater the value setting

    <a id="_CPPv4N22aud_intf_voc_aec_cfg_t7TxRxThrE"></a>

    <a id="_CPPv3N22aud_intf_voc_aec_cfg_t7TxRxThrE"></a> <a id="_CPPv2N22aud_intf_voc_aec_cfg_t7TxRxThrE"></a> <a id="aud_intf_voc_aec_cfg_t::TxRxThr__uint32_t"></a> <a id="structaud__intf__voc__aec__cfg__t_1aceaebef8ae78707be0e2edfa2f0d1e36"></a> uint32\_t TxRxThr
    :   the max amplitude of rx audio data

    <a id="_CPPv4N22aud_intf_voc_aec_cfg_t7TxRxFlrE"></a>

    <a id="_CPPv3N22aud_intf_voc_aec_cfg_t7TxRxFlrE"></a> <a id="_CPPv2N22aud_intf_voc_aec_cfg_t7TxRxFlrE"></a> <a id="aud_intf_voc_aec_cfg_t::TxRxFlr__uint32_t"></a> <a id="structaud__intf__voc__aec__cfg__t_1aaa0b84800cc71b286cc8198423ec1c3c"></a> uint32\_t TxRxFlr
    :   the min amplitude of rx audio data

    <a id="_CPPv4N22aud_intf_voc_aec_cfg_t9ref_scaleE"></a>

    <a id="_CPPv3N22aud_intf_voc_aec_cfg_t9ref_scaleE"></a> <a id="_CPPv2N22aud_intf_voc_aec_cfg_t9ref_scaleE"></a> <a id="aud_intf_voc_aec_cfg_t::ref_scale__uint8_t"></a> <a id="structaud__intf__voc__aec__cfg__t_1a9ab89182d53d59e2ba8e933e6e74dbdc"></a> uint8\_t ref\_scale
    :   value range:0,1,2, the greater the signal amplitude, the greater the setting

    <a id="_CPPv4N22aud_intf_voc_aec_cfg_t8ns_levelE"></a>

    <a id="_CPPv3N22aud_intf_voc_aec_cfg_t8ns_levelE"></a> <a id="_CPPv2N22aud_intf_voc_aec_cfg_t8ns_levelE"></a> <a id="aud_intf_voc_aec_cfg_t::ns_level__uint8_t"></a> <a id="structaud__intf__voc__aec__cfg__t_1a3ff5ef31b223d6aeb58d653778d1a845"></a> uint8\_t ns\_level
    :   recommended value range: 1\~8, the lower the noise, the lower the level

    <a id="_CPPv4N22aud_intf_voc_aec_cfg_t7ns_paraE"></a>

    <a id="_CPPv3N22aud_intf_voc_aec_cfg_t7ns_paraE"></a> <a id="_CPPv2N22aud_intf_voc_aec_cfg_t7ns_paraE"></a> <a id="aud_intf_voc_aec_cfg_t::ns_para__uint8_t"></a> <a id="structaud__intf__voc__aec__cfg__t_1a82a10c5e7575ddca2257f17b1bcf245d"></a> uint8\_t ns\_para
    :   value range:0,1,2, the lower the noise, the lower the level, the default valude is recommended

<a id="_CPPv420aud_intf_voc_setup_t"></a>

<a id="_CPPv320aud_intf_voc_setup_t"></a> <a id="_CPPv220aud_intf_voc_setup_t"></a> <a id="aud_intf_voc_setup_t"></a> <a id="structaud__intf__voc__setup__t"></a> struct aud\_intf\_voc\_setup\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20aud_intf_voc_setup_t10aec_enableE"></a>

    <a id="_CPPv3N20aud_intf_voc_setup_t10aec_enableE"></a> <a id="_CPPv2N20aud_intf_voc_setup_t10aec_enableE"></a> <a id="aud_intf_voc_setup_t::aec_enable__b"></a> <a id="structaud__intf__voc__setup__t_1a6e5ac3f767286c0d4563ba9e7d971d8c"></a> bool aec\_enable
    :   true: enable aec, false: disable aec

    <a id="_CPPv4N20aud_intf_voc_setup_t9samp_rateE"></a>

    <a id="_CPPv3N20aud_intf_voc_setup_t9samp_rateE"></a> <a id="_CPPv2N20aud_intf_voc_setup_t9samp_rateE"></a> <a id="aud_intf_voc_setup_t::samp_rate__aud_intf_voc_samp_rate_t"></a> <a id="structaud__intf__voc__setup__t_1a055ca9b4131a0e030e4393e6a5eb82c6"></a> [aud\_intf\_voc\_samp\_rate\_t](#_CPPv424aud_intf_voc_samp_rate_t "aud_intf_voc_samp_rate_t") samp\_rate
    :   voice transfer sample rate

    <a id="_CPPv4N20aud_intf_voc_setup_t9data_typeE"></a>

    <a id="_CPPv3N20aud_intf_voc_setup_t9data_typeE"></a> <a id="_CPPv2N20aud_intf_voc_setup_t9data_typeE"></a> <a id="aud_intf_voc_setup_t::data_type__aud_intf_voc_data_type_t"></a> <a id="structaud__intf__voc__setup__t_1a1da448e84030c7dab239e45ece2e60c0"></a> [aud\_intf\_voc\_data\_type\_t](#_CPPv424aud_intf_voc_data_type_t "aud_intf_voc_data_type_t") data\_type
    :   voice data type

    <a id="_CPPv4N20aud_intf_voc_setup_t8mic_gainE"></a>

    <a id="_CPPv3N20aud_intf_voc_setup_t8mic_gainE"></a> <a id="_CPPv2N20aud_intf_voc_setup_t8mic_gainE"></a> <a id="aud_intf_voc_setup_t::mic_gain__uint8_t"></a> <a id="structaud__intf__voc__setup__t_1a52047f78362fb91a941fbed6d25629ab"></a> uint8\_t mic\_gain
    :   mic gain: value range:0x0 \~ 0x3f, suggest:0x2d

    <a id="_CPPv4N20aud_intf_voc_setup_t8spk_gainE"></a>

    <a id="_CPPv3N20aud_intf_voc_setup_t8spk_gainE"></a> <a id="_CPPv2N20aud_intf_voc_setup_t8spk_gainE"></a> <a id="aud_intf_voc_setup_t::spk_gain__uint16_t"></a> <a id="structaud__intf__voc__setup__t_1a45b6204d4f2749d53996c0b1a903685f"></a> uint16\_t spk\_gain
    :   spk gain: value range:0x0 \~ 0x3f, suggest:0x2d

    <a id="_CPPv4N20aud_intf_voc_setup_t8spk_modeE"></a>

    <a id="_CPPv3N20aud_intf_voc_setup_t8spk_modeE"></a> <a id="_CPPv2N20aud_intf_voc_setup_t8spk_modeE"></a> <a id="aud_intf_voc_setup_t::spk_mode__aud_dac_work_mode_t"></a> <a id="structaud__intf__voc__setup__t_1a0ca9a0eb7ea46fe8c805c6303a7af393"></a> [aud\_dac\_work\_mode\_t](bk_audio.md#_CPPv419aud_dac_work_mode_t "aud_dac_work_mode_t") spk\_mode
    :   audio spk mode: signal\_ended/differen

    <a id="_CPPv4N20aud_intf_voc_setup_t6mic_enE"></a>

    <a id="_CPPv3N20aud_intf_voc_setup_t6mic_enE"></a> <a id="_CPPv2N20aud_intf_voc_setup_t6mic_enE"></a> <a id="aud_intf_voc_setup_t::mic_en__aud_intf_voc_mic_ctrl_t"></a> <a id="structaud__intf__voc__setup__t_1af75d560961fa1ebad3007604141d0575"></a> [aud\_intf\_voc\_mic\_ctrl\_t](#_CPPv423aud_intf_voc_mic_ctrl_t "aud_intf_voc_mic_ctrl_t") mic\_en
    :   mic default status

    <a id="_CPPv4N20aud_intf_voc_setup_t6spk_enE"></a>

    <a id="_CPPv3N20aud_intf_voc_setup_t6spk_enE"></a> <a id="_CPPv2N20aud_intf_voc_setup_t6spk_enE"></a> <a id="aud_intf_voc_setup_t::spk_en__aud_intf_voc_spk_ctrl_t"></a> <a id="structaud__intf__voc__setup__t_1ad93b1b9c2ae7cce3cffbec73fa75b720"></a> [aud\_intf\_voc\_spk\_ctrl\_t](#_CPPv423aud_intf_voc_spk_ctrl_t "aud_intf_voc_spk_ctrl_t") spk\_en
    :   spk default status

    <a id="_CPPv4N20aud_intf_voc_setup_t8mic_typeE"></a>

    <a id="_CPPv3N20aud_intf_voc_setup_t8mic_typeE"></a> <a id="_CPPv2N20aud_intf_voc_setup_t8mic_typeE"></a> <a id="aud_intf_voc_setup_t::mic_type__aud_intf_mic_type_t"></a> <a id="structaud__intf__voc__setup__t_1a10619a5d6f049967b5a2d15e8cdac1db"></a> [aud\_intf\_mic\_type\_t](#_CPPv419aud_intf_mic_type_t "aud_intf_mic_type_t") mic\_type
    :   audio mic type: uac or microphone

    <a id="_CPPv4N20aud_intf_voc_setup_t8spk_typeE"></a>

    <a id="_CPPv3N20aud_intf_voc_setup_t8spk_typeE"></a> <a id="_CPPv2N20aud_intf_voc_setup_t8spk_typeE"></a> <a id="aud_intf_voc_setup_t::spk_type__aud_intf_spk_type_t"></a> <a id="structaud__intf__voc__setup__t_1a4c245106d99ad091bc92d683b4ffa91d"></a> [aud\_intf\_spk\_type\_t](#_CPPv419aud_intf_spk_type_t "aud_intf_spk_type_t") spk\_type
    :   audio speaker type: uac or speaker

    <a id="_CPPv4N20aud_intf_voc_setup_t8mic_modeE"></a>

    <a id="_CPPv3N20aud_intf_voc_setup_t8mic_modeE"></a> <a id="_CPPv2N20aud_intf_voc_setup_t8mic_modeE"></a> <a id="aud_intf_voc_setup_t::mic_mode__aud_adc_intf_mode_t"></a> <a id="structaud__intf__voc__setup__t_1acbf2f832d333ebbabeb77d0bda3ee8e0"></a> [aud\_adc\_intf\_mode\_t](bk_audio.md#_CPPv419aud_adc_intf_mode_t "aud_adc_intf_mode_t") mic\_mode
    :   audio mic mode: signal\_ended/differen

    <a id="_CPPv4N20aud_intf_voc_setup_t9frame_numE"></a>

    <a id="_CPPv3N20aud_intf_voc_setup_t9frame_numE"></a> <a id="_CPPv2N20aud_intf_voc_setup_t9frame_numE"></a> <a id="aud_intf_voc_setup_t::frame_num__uint8_t"></a> <a id="structaud__intf__voc__setup__t_1ab6774580ea9c6fcef85ca8d3c6b9de58"></a> uint8\_t frame\_num
    :   the max number of frames in rx buffer to save rx data, the time of one frame is 20ms

    <a id="_CPPv4N20aud_intf_voc_setup_t14fifo_frame_numE"></a>

    <a id="_CPPv3N20aud_intf_voc_setup_t14fifo_frame_numE"></a> <a id="_CPPv2N20aud_intf_voc_setup_t14fifo_frame_numE"></a> <a id="aud_intf_voc_setup_t::fifo_frame_num__uint8_t"></a> <a id="structaud__intf__voc__setup__t_1aeee8693a8f46aa37641f4548866a3205"></a> uint8\_t fifo\_frame\_num
    :   the number of frames in rx buffer before start voice transfer, the time of one frame is 20ms

<a id="macros"></a>

### Macros

<a id="c.BK_ERR_AUD_INTF_BASE"></a>

<a id="aud__intf__types_8h_1a34fdd7adaa05da2b466e975a37953b5f"></a> BK\_ERR\_AUD\_INTF\_BASE

<a id="c.BK_ERR_AUD_INTF_OK"></a>

<a id="aud__intf__types_8h_1aeeb84c1bf5f17403d35e301ec46793f2"></a> BK\_ERR\_AUD\_INTF\_OK
:   ok

<a id="c.BK_ERR_AUD_INTF_FAIL"></a>

<a id="aud__intf__types_8h_1af49d9f6b6c2cc469feebdb94ac624d4a"></a> BK\_ERR\_AUD\_INTF\_FAIL
:   fail

<a id="c.BK_ERR_AUD_INTF_STA"></a>

<a id="aud__intf__types_8h_1a1262cef8cf7df3fd5b063774259e1c70"></a> BK\_ERR\_AUD\_INTF\_STA
:   audio interface module status is error

<a id="c.BK_ERR_AUD_INTF_PARAM"></a>

<a id="aud__intf__types_8h_1a158b505cb437d92fa61f131446ef0f53"></a> BK\_ERR\_AUD\_INTF\_PARAM
:   parameter is error

<a id="c.BK_ERR_AUD_INTF_MEMY"></a>

<a id="aud__intf__types_8h_1a4d94f2d418296753d97cc578c10dbc69"></a> BK\_ERR\_AUD\_INTF\_MEMY
:   malloc memory fail

<a id="c.BK_ERR_AUD_INTF_ADC"></a>

<a id="aud__intf__types_8h_1a18bdf4dc995890b2186f917f39d99190"></a> BK\_ERR\_AUD\_INTF\_ADC
:   config audio adc fail

<a id="c.BK_ERR_AUD_INTF_DAC"></a>

<a id="aud__intf__types_8h_1ac06cb593e6c6c8a6b8b7f4ac06afafb8"></a> BK\_ERR\_AUD\_INTF\_DAC
:   config audio dac fail

<a id="c.BK_ERR_AUD_INTF_DMA"></a>

<a id="aud__intf__types_8h_1ab5e1a0084dbba8588c4f5fdb11c24be1"></a> BK\_ERR\_AUD\_INTF\_DMA
:   config dma fail

<a id="c.BK_ERR_AUD_INTF_AEC"></a>

<a id="aud__intf__types_8h_1ad02fe32ab7dbede9ec59323946cd93d3"></a> BK\_ERR\_AUD\_INTF\_AEC
:   config aec fail

<a id="c.BK_ERR_AUD_INTF_RING_BUFF"></a>

<a id="aud__intf__types_8h_1ab09633d888a4a36947b22a605e7642d0"></a> BK\_ERR\_AUD\_INTF\_RING\_BUFF
:   config ring buffer fail

<a id="c.BK_ERR_AUD_INTF_TIMEOUT"></a>

<a id="aud__intf__types_8h_1a653ec85e13df731e80c049dd91d19dde"></a> BK\_ERR\_AUD\_INTF\_TIMEOUT
:   aud\_intf api excute timeout

<a id="c.BK_ERR_AUD_INTF_TX_MSG"></a>

<a id="aud__intf__types_8h_1aeef5357d53fe23fe1a4d98a4c1dc306e"></a> BK\_ERR\_AUD\_INTF\_TX\_MSG
:   aud\_intf api send message fail

<a id="c.BK_ERR_AUD_INTF_BUSY"></a>

<a id="aud__intf__types_8h_1a6c6fa5543b5de0b3561ec2cb19030d2d"></a> BK\_ERR\_AUD\_INTF\_BUSY
:   aud\_intf is busying

<a id="c.BK_ERR_AUD_INTF_FILE"></a>

<a id="aud__intf__types_8h_1ad5a1f838f645c5a3ea7051ed6f6e1123"></a> BK\_ERR\_AUD\_INTF\_FILE
:   aud\_intf file operate fail

<a id="c.BK_ERR_AUD_INTF_UAC_DRV"></a>

<a id="aud__intf__types_8h_1aa2fcd2e2534029b9d0c9294fbb2a4ec5"></a> BK\_ERR\_AUD\_INTF\_UAC\_DRV
:   aud\_intf uac driver fail

<a id="c.BK_ERR_AUD_INTF_UAC_MIC"></a>

<a id="aud__intf__types_8h_1a2ba65938084a4f3471b50ac0a6f07c77"></a> BK\_ERR\_AUD\_INTF\_UAC\_MIC
:   aud\_intf uac mic fail

<a id="c.BK_ERR_AUD_INTF_UAC_SPK"></a>

<a id="aud__intf__types_8h_1ad4962cf2312c94f088555134e7b82a48"></a> BK\_ERR\_AUD\_INTF\_UAC\_SPK
:   aud\_intf uac spk operate fail

<a id="c.DEFAULT_AUD_INTF_DRV_SETUP_CONFIG"></a>

<a id="aud__intf__types_8h_1ac0c63207ac192cab655d97b2e2a0828d"></a> DEFAULT\_AUD\_INTF\_DRV\_SETUP\_CONFIG()

<a id="c.DEFAULT_AUD_INTF_MIC_SETUP_CONFIG"></a>

<a id="aud__intf__types_8h_1a403115e0278a5639967450e50889ab46"></a> DEFAULT\_AUD\_INTF\_MIC\_SETUP\_CONFIG()

<a id="c.DEFAULT_AUD_INTF_SPK_SETUP_CONFIG"></a>

<a id="aud__intf__types_8h_1a41205272deee4e00bccf6be95fcfeace"></a> DEFAULT\_AUD\_INTF\_SPK\_SETUP\_CONFIG()

<a id="c.DEFAULT_AUD_INTF_VOC_SETUP_CONFIG"></a>

<a id="aud__intf__types_8h_1ad34301a0d6023d998b7b030e709b2e48"></a> DEFAULT\_AUD\_INTF\_VOC\_SETUP\_CONFIG()

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv427aud_intf_dump_data_callback"></a>

<a id="_CPPv327aud_intf_dump_data_callback"></a> <a id="_CPPv227aud_intf_dump_data_callback"></a> <a id="aud_intf_dump_data_callback"></a> <a id="aud__intf__types_8h_1a26887ba75c79e2a2558fdb3e1a96a6ec"></a> typedef [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") (\*aud\_intf\_dump\_data\_callback)(unsigned char \*data, unsigned int size)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv418aud_intf_uac_sta_t"></a>

<a id="_CPPv318aud_intf_uac_sta_t"></a> <a id="_CPPv218aud_intf_uac_sta_t"></a> <a id="aud__intf__types_8h_1a51a283f1f0414f7fcefe454585cd5710"></a> enum aud\_intf\_uac\_sta\_t
:   *Values:*

    <a id="_CPPv4N18aud_intf_uac_sta_t22AUD_INTF_UAC_CONNECTEDE"></a>

    <a id="_CPPv3N18aud_intf_uac_sta_t22AUD_INTF_UAC_CONNECTEDE"></a> <a id="_CPPv2N18aud_intf_uac_sta_t22AUD_INTF_UAC_CONNECTEDE"></a> <a id="aud__intf__types_8h_1a51a283f1f0414f7fcefe454585cd5710aab4ce77dca4adcb843f98298a5a15b33"></a> enumerator AUD\_INTF\_UAC\_CONNECTED
    :   Connected: uac automatically restore connection after abnormal disconnection

    <a id="_CPPv4N18aud_intf_uac_sta_t32AUD_INTF_UAC_NORMAL_DISCONNECTEDE"></a>

    <a id="_CPPv3N18aud_intf_uac_sta_t32AUD_INTF_UAC_NORMAL_DISCONNECTEDE"></a> <a id="_CPPv2N18aud_intf_uac_sta_t32AUD_INTF_UAC_NORMAL_DISCONNECTEDE"></a> <a id="aud__intf__types_8h_1a51a283f1f0414f7fcefe454585cd5710a41e1d8fdc0eab7e25f803642fb4c5209"></a> enumerator AUD\_INTF\_UAC\_NORMAL\_DISCONNECTED
    :   Normal disconnected: uac normal disconnection

    <a id="_CPPv4N18aud_intf_uac_sta_t34AUD_INTF_UAC_ABNORMAL_DISCONNECTEDE"></a>

    <a id="_CPPv3N18aud_intf_uac_sta_t34AUD_INTF_UAC_ABNORMAL_DISCONNECTEDE"></a> <a id="_CPPv2N18aud_intf_uac_sta_t34AUD_INTF_UAC_ABNORMAL_DISCONNECTEDE"></a> <a id="aud__intf__types_8h_1a51a283f1f0414f7fcefe454585cd5710a6b8c9d4eb2d7d13745e7002f49a9a119"></a> enumerator AUD\_INTF\_UAC\_ABNORMAL\_DISCONNECTED
    :   Abnormal disconnected: uac abnormal disconnection

    <a id="_CPPv4N18aud_intf_uac_sta_t35AUD_INTF_UAC_CANNOT_RECOVER_CONNECTE"></a>

    <a id="_CPPv3N18aud_intf_uac_sta_t35AUD_INTF_UAC_CANNOT_RECOVER_CONNECTE"></a> <a id="_CPPv2N18aud_intf_uac_sta_t35AUD_INTF_UAC_CANNOT_RECOVER_CONNECTE"></a> <a id="aud__intf__types_8h_1a51a283f1f0414f7fcefe454585cd5710ab6e5356f6800cd2d66fd4cfaa2845bfe"></a> enumerator AUD\_INTF\_UAC\_CANNOT\_RECOVER\_CONNECT
    :   Cannot automatically connect: uac automatically connect fail

<a id="_CPPv420aud_intf_work_mode_t"></a>

<a id="_CPPv320aud_intf_work_mode_t"></a> <a id="_CPPv220aud_intf_work_mode_t"></a> <a id="aud__intf__types_8h_1a3ceedeec875d13254fec1ee7d66e6c4f"></a> enum aud\_intf\_work\_mode\_t
:   *Values:*

    <a id="_CPPv4N20aud_intf_work_mode_t23AUD_INTF_WORK_MODE_NULLE"></a>

    <a id="_CPPv3N20aud_intf_work_mode_t23AUD_INTF_WORK_MODE_NULLE"></a> <a id="_CPPv2N20aud_intf_work_mode_t23AUD_INTF_WORK_MODE_NULLE"></a> <a id="aud__intf__types_8h_1a3ceedeec875d13254fec1ee7d66e6c4fa9d850662651c10d579203bfd5b45f7f9"></a> enumerator AUD\_INTF\_WORK\_MODE\_NULL

    <a id="_CPPv4N20aud_intf_work_mode_t26AUD_INTF_WORK_MODE_GENERALE"></a>

    <a id="_CPPv3N20aud_intf_work_mode_t26AUD_INTF_WORK_MODE_GENERALE"></a> <a id="_CPPv2N20aud_intf_work_mode_t26AUD_INTF_WORK_MODE_GENERALE"></a> <a id="aud__intf__types_8h_1a3ceedeec875d13254fec1ee7d66e6c4fa383995400b861b6b11f72a388a33ea66"></a> enumerator AUD\_INTF\_WORK\_MODE\_GENERAL
    :   General mode: support record mic data and play speaker

    <a id="_CPPv4N20aud_intf_work_mode_t24AUD_INTF_WORK_MODE_VOICEE"></a>

    <a id="_CPPv3N20aud_intf_work_mode_t24AUD_INTF_WORK_MODE_VOICEE"></a> <a id="_CPPv2N20aud_intf_work_mode_t24AUD_INTF_WORK_MODE_VOICEE"></a> <a id="aud__intf__types_8h_1a3ceedeec875d13254fec1ee7d66e6c4fa423edd8cc3dbec55c8c91abe031f2da5"></a> enumerator AUD\_INTF\_WORK\_MODE\_VOICE
    :   Voice mode: support voice transfer

    <a id="_CPPv4N20aud_intf_work_mode_t22AUD_INTF_WORK_MODE_MAXE"></a>

    <a id="_CPPv3N20aud_intf_work_mode_t22AUD_INTF_WORK_MODE_MAXE"></a> <a id="_CPPv2N20aud_intf_work_mode_t22AUD_INTF_WORK_MODE_MAXE"></a> <a id="aud__intf__types_8h_1a3ceedeec875d13254fec1ee7d66e6c4fa4ae3abe4a8733e220cdf9efb122d61cd"></a> enumerator AUD\_INTF\_WORK\_MODE\_MAX

<a id="_CPPv418aud_intf_mic_chl_t"></a>

<a id="_CPPv318aud_intf_mic_chl_t"></a> <a id="_CPPv218aud_intf_mic_chl_t"></a> <a id="aud__intf__types_8h_1a36a63898656faabd5259360fbe6c316c"></a> enum aud\_intf\_mic\_chl\_t
:   *Values:*

    <a id="_CPPv4N18aud_intf_mic_chl_t21AUD_INTF_MIC_CHL_MIC1E"></a>

    <a id="_CPPv3N18aud_intf_mic_chl_t21AUD_INTF_MIC_CHL_MIC1E"></a> <a id="_CPPv2N18aud_intf_mic_chl_t21AUD_INTF_MIC_CHL_MIC1E"></a> <a id="aud__intf__types_8h_1a36a63898656faabd5259360fbe6c316ca7a98a6dfebfdbce79394fa32445f3b8b"></a> enumerator AUD\_INTF\_MIC\_CHL\_MIC1
    :   MIC1: only enable mic1 channel

    <a id="_CPPv4N18aud_intf_mic_chl_t21AUD_INTF_MIC_CHL_DUALE"></a>

    <a id="_CPPv3N18aud_intf_mic_chl_t21AUD_INTF_MIC_CHL_DUALE"></a> <a id="_CPPv2N18aud_intf_mic_chl_t21AUD_INTF_MIC_CHL_DUALE"></a> <a id="aud__intf__types_8h_1a36a63898656faabd5259360fbe6c316cacbd61b17e3482e6522a7f60c3ff8c48d"></a> enumerator AUD\_INTF\_MIC\_CHL\_DUAL
    :   DUAL: enable mic1 channel both and MIC2 channel

    <a id="_CPPv4N18aud_intf_mic_chl_t20AUD_INTF_MIC_CHL_MAXE"></a>

    <a id="_CPPv3N18aud_intf_mic_chl_t20AUD_INTF_MIC_CHL_MAXE"></a> <a id="_CPPv2N18aud_intf_mic_chl_t20AUD_INTF_MIC_CHL_MAXE"></a> <a id="aud__intf__types_8h_1a36a63898656faabd5259360fbe6c316ca0a1f607bd98dd74480ff0288daba689b"></a> enumerator AUD\_INTF\_MIC\_CHL\_MAX

<a id="_CPPv419aud_intf_mic_type_t"></a>

<a id="_CPPv319aud_intf_mic_type_t"></a> <a id="_CPPv219aud_intf_mic_type_t"></a> <a id="aud__intf__types_8h_1aa4e6580b2cfcbccd62ed93a613b340e4"></a> enum aud\_intf\_mic\_type\_t
:   *Values:*

    <a id="_CPPv4N19aud_intf_mic_type_t23AUD_INTF_MIC_TYPE_BOARDE"></a>

    <a id="_CPPv3N19aud_intf_mic_type_t23AUD_INTF_MIC_TYPE_BOARDE"></a> <a id="_CPPv2N19aud_intf_mic_type_t23AUD_INTF_MIC_TYPE_BOARDE"></a> <a id="aud__intf__types_8h_1aa4e6580b2cfcbccd62ed93a613b340e4ab001c528eb119059d32bf0d476b81360"></a> enumerator AUD\_INTF\_MIC\_TYPE\_BOARD

    <a id="_CPPv4N19aud_intf_mic_type_t21AUD_INTF_MIC_TYPE_UACE"></a>

    <a id="_CPPv3N19aud_intf_mic_type_t21AUD_INTF_MIC_TYPE_UACE"></a> <a id="_CPPv2N19aud_intf_mic_type_t21AUD_INTF_MIC_TYPE_UACE"></a> <a id="aud__intf__types_8h_1aa4e6580b2cfcbccd62ed93a613b340e4ac4d151c9cc48588eed06d90eb98c2840"></a> enumerator AUD\_INTF\_MIC\_TYPE\_UAC

    <a id="_CPPv4N19aud_intf_mic_type_t21AUD_INTF_MIC_TYPE_MAXE"></a>

    <a id="_CPPv3N19aud_intf_mic_type_t21AUD_INTF_MIC_TYPE_MAXE"></a> <a id="_CPPv2N19aud_intf_mic_type_t21AUD_INTF_MIC_TYPE_MAXE"></a> <a id="aud__intf__types_8h_1aa4e6580b2cfcbccd62ed93a613b340e4a2e9f4154f60262d20751f90fca7ede0a"></a> enumerator AUD\_INTF\_MIC\_TYPE\_MAX

<a id="_CPPv418aud_intf_spk_chl_t"></a>

<a id="_CPPv318aud_intf_spk_chl_t"></a> <a id="_CPPv218aud_intf_spk_chl_t"></a> <a id="aud__intf__types_8h_1a01d4cb48246723b190207e667c661651"></a> enum aud\_intf\_spk\_chl\_t
:   *Values:*

    <a id="_CPPv4N18aud_intf_spk_chl_t21AUD_INTF_SPK_CHL_LEFTE"></a>

    <a id="_CPPv3N18aud_intf_spk_chl_t21AUD_INTF_SPK_CHL_LEFTE"></a> <a id="_CPPv2N18aud_intf_spk_chl_t21AUD_INTF_SPK_CHL_LEFTE"></a> <a id="aud__intf__types_8h_1a01d4cb48246723b190207e667c661651a1b7cc8b391d6f44ae1eaaca523608913"></a> enumerator AUD\_INTF\_SPK\_CHL\_LEFT
    :   LEFT: only enable SPK left channel

    <a id="_CPPv4N18aud_intf_spk_chl_t21AUD_INTF_SPK_CHL_DUALE"></a>

    <a id="_CPPv3N18aud_intf_spk_chl_t21AUD_INTF_SPK_CHL_DUALE"></a> <a id="_CPPv2N18aud_intf_spk_chl_t21AUD_INTF_SPK_CHL_DUALE"></a> <a id="aud__intf__types_8h_1a01d4cb48246723b190207e667c661651a4d94cb67276c54968817fa0d75491e7f"></a> enumerator AUD\_INTF\_SPK\_CHL\_DUAL
    :   DUAL: enable SPK left and right channel

    <a id="_CPPv4N18aud_intf_spk_chl_t20AUD_INTF_SPK_CHL_MAXE"></a>

    <a id="_CPPv3N18aud_intf_spk_chl_t20AUD_INTF_SPK_CHL_MAXE"></a> <a id="_CPPv2N18aud_intf_spk_chl_t20AUD_INTF_SPK_CHL_MAXE"></a> <a id="aud__intf__types_8h_1a01d4cb48246723b190207e667c661651a580ea92ffab1927ee6c39260ec454c31"></a> enumerator AUD\_INTF\_SPK\_CHL\_MAX

<a id="_CPPv419aud_intf_spk_type_t"></a>

<a id="_CPPv319aud_intf_spk_type_t"></a> <a id="_CPPv219aud_intf_spk_type_t"></a> <a id="aud__intf__types_8h_1a0c5eb5368b66c063b6d3741bbf64377d"></a> enum aud\_intf\_spk\_type\_t
:   *Values:*

    <a id="_CPPv4N19aud_intf_spk_type_t23AUD_INTF_SPK_TYPE_BOARDE"></a>

    <a id="_CPPv3N19aud_intf_spk_type_t23AUD_INTF_SPK_TYPE_BOARDE"></a> <a id="_CPPv2N19aud_intf_spk_type_t23AUD_INTF_SPK_TYPE_BOARDE"></a> <a id="aud__intf__types_8h_1a0c5eb5368b66c063b6d3741bbf64377da0d6a81eca52925cd33098320febc78d2"></a> enumerator AUD\_INTF\_SPK\_TYPE\_BOARD

    <a id="_CPPv4N19aud_intf_spk_type_t21AUD_INTF_SPK_TYPE_UACE"></a>

    <a id="_CPPv3N19aud_intf_spk_type_t21AUD_INTF_SPK_TYPE_UACE"></a> <a id="_CPPv2N19aud_intf_spk_type_t21AUD_INTF_SPK_TYPE_UACE"></a> <a id="aud__intf__types_8h_1a0c5eb5368b66c063b6d3741bbf64377dad634a23c952b3448d158780ddd0024ef"></a> enumerator AUD\_INTF\_SPK\_TYPE\_UAC

    <a id="_CPPv4N19aud_intf_spk_type_t21AUD_INTF_SPK_TYPE_MAXE"></a>

    <a id="_CPPv3N19aud_intf_spk_type_t21AUD_INTF_SPK_TYPE_MAXE"></a> <a id="_CPPv2N19aud_intf_spk_type_t21AUD_INTF_SPK_TYPE_MAXE"></a> <a id="aud__intf__types_8h_1a0c5eb5368b66c063b6d3741bbf64377da65b472fc8287238cee009ef64b728e96"></a> enumerator AUD\_INTF\_SPK\_TYPE\_MAX

<a id="_CPPv424aud_intf_voc_samp_rate_t"></a>

<a id="_CPPv324aud_intf_voc_samp_rate_t"></a> <a id="_CPPv224aud_intf_voc_samp_rate_t"></a> <a id="aud__intf__types_8h_1a85cbc5b292159b5bac1da734ce1950c0"></a> enum aud\_intf\_voc\_samp\_rate\_t
:   *Values:*

    <a id="_CPPv4N24aud_intf_voc_samp_rate_t25AUD_INTF_VOC_SAMP_RATE_8KE"></a>

    <a id="_CPPv3N24aud_intf_voc_samp_rate_t25AUD_INTF_VOC_SAMP_RATE_8KE"></a> <a id="_CPPv2N24aud_intf_voc_samp_rate_t25AUD_INTF_VOC_SAMP_RATE_8KE"></a> <a id="aud__intf__types_8h_1a85cbc5b292159b5bac1da734ce1950c0a9421b9e20dc4acdff5787b9cb1f95eea"></a> enumerator AUD\_INTF\_VOC\_SAMP\_RATE\_8K

    <a id="_CPPv4N24aud_intf_voc_samp_rate_t26AUD_INTF_VOC_SAMP_RATE_16KE"></a>

    <a id="_CPPv3N24aud_intf_voc_samp_rate_t26AUD_INTF_VOC_SAMP_RATE_16KE"></a> <a id="_CPPv2N24aud_intf_voc_samp_rate_t26AUD_INTF_VOC_SAMP_RATE_16KE"></a> <a id="aud__intf__types_8h_1a85cbc5b292159b5bac1da734ce1950c0aafe6813ba2f18775ea757fe7ca282f4d"></a> enumerator AUD\_INTF\_VOC\_SAMP\_RATE\_16K

    <a id="_CPPv4N24aud_intf_voc_samp_rate_t26AUD_INTF_VOC_SAMP_RATE_MAXE"></a>

    <a id="_CPPv3N24aud_intf_voc_samp_rate_t26AUD_INTF_VOC_SAMP_RATE_MAXE"></a> <a id="_CPPv2N24aud_intf_voc_samp_rate_t26AUD_INTF_VOC_SAMP_RATE_MAXE"></a> <a id="aud__intf__types_8h_1a85cbc5b292159b5bac1da734ce1950c0ac78b8e7d68e0cab6986406988b8cbf15"></a> enumerator AUD\_INTF\_VOC\_SAMP\_RATE\_MAX

<a id="_CPPv424aud_intf_voc_data_type_t"></a>

<a id="_CPPv324aud_intf_voc_data_type_t"></a> <a id="_CPPv224aud_intf_voc_data_type_t"></a> <a id="aud__intf__types_8h_1ae43cc1fabccaa8cdf1b4b0905a1cbe4c"></a> enum aud\_intf\_voc\_data\_type\_t
:   *Values:*

    <a id="_CPPv4N24aud_intf_voc_data_type_t28AUD_INTF_VOC_DATA_TYPE_G711AE"></a>

    <a id="_CPPv3N24aud_intf_voc_data_type_t28AUD_INTF_VOC_DATA_TYPE_G711AE"></a> <a id="_CPPv2N24aud_intf_voc_data_type_t28AUD_INTF_VOC_DATA_TYPE_G711AE"></a> <a id="aud__intf__types_8h_1ae43cc1fabccaa8cdf1b4b0905a1cbe4caa3c068aa5b42ae382c177aca91dbf6dc"></a> enumerator AUD\_INTF\_VOC\_DATA\_TYPE\_G711A
    :   the data of voice transfer encoded by G711A

    <a id="_CPPv4N24aud_intf_voc_data_type_t26AUD_INTF_VOC_DATA_TYPE_PCME"></a>

    <a id="_CPPv3N24aud_intf_voc_data_type_t26AUD_INTF_VOC_DATA_TYPE_PCME"></a> <a id="_CPPv2N24aud_intf_voc_data_type_t26AUD_INTF_VOC_DATA_TYPE_PCME"></a> <a id="aud__intf__types_8h_1ae43cc1fabccaa8cdf1b4b0905a1cbe4caee43d199e95b10c500b6007355541158"></a> enumerator AUD\_INTF\_VOC\_DATA\_TYPE\_PCM
    :   the data of voice transfer is PCM

    <a id="_CPPv4N24aud_intf_voc_data_type_t28AUD_INTF_VOC_DATA_TYPE_G711UE"></a>

    <a id="_CPPv3N24aud_intf_voc_data_type_t28AUD_INTF_VOC_DATA_TYPE_G711UE"></a> <a id="_CPPv2N24aud_intf_voc_data_type_t28AUD_INTF_VOC_DATA_TYPE_G711UE"></a> <a id="aud__intf__types_8h_1ae43cc1fabccaa8cdf1b4b0905a1cbe4ca427861d0a73c43cec52c53c34914f82a"></a> enumerator AUD\_INTF\_VOC\_DATA\_TYPE\_G711U
    :   the data of voice transfer encoded by G711U

    <a id="_CPPv4N24aud_intf_voc_data_type_t26AUD_INTF_VOC_DATA_TYPE_MAXE"></a>

    <a id="_CPPv3N24aud_intf_voc_data_type_t26AUD_INTF_VOC_DATA_TYPE_MAXE"></a> <a id="_CPPv2N24aud_intf_voc_data_type_t26AUD_INTF_VOC_DATA_TYPE_MAXE"></a> <a id="aud__intf__types_8h_1ae43cc1fabccaa8cdf1b4b0905a1cbe4ca78bf0bcf04c9259cb9c8acc96f55a8f5"></a> enumerator AUD\_INTF\_VOC\_DATA\_TYPE\_MAX

<a id="_CPPv423aud_intf_voc_aec_para_t"></a>

<a id="_CPPv323aud_intf_voc_aec_para_t"></a> <a id="_CPPv223aud_intf_voc_aec_para_t"></a> <a id="aud__intf__types_8h_1a2318cca3b5827df956e961816fb30f04"></a> enum aud\_intf\_voc\_aec\_para\_t
:   *Values:*

    <a id="_CPPv4N23aud_intf_voc_aec_para_t21AUD_INTF_VOC_AEC_NULLE"></a>

    <a id="_CPPv3N23aud_intf_voc_aec_para_t21AUD_INTF_VOC_AEC_NULLE"></a> <a id="_CPPv2N23aud_intf_voc_aec_para_t21AUD_INTF_VOC_AEC_NULLE"></a> <a id="aud__intf__types_8h_1a2318cca3b5827df956e961816fb30f04af01601250a3cc279832756ce19c37ab4"></a> enumerator AUD\_INTF\_VOC\_AEC\_NULL

    <a id="_CPPv4N23aud_intf_voc_aec_para_t26AUD_INTF_VOC_AEC_INIT_FLAGE"></a>

    <a id="_CPPv3N23aud_intf_voc_aec_para_t26AUD_INTF_VOC_AEC_INIT_FLAGE"></a> <a id="_CPPv2N23aud_intf_voc_aec_para_t26AUD_INTF_VOC_AEC_INIT_FLAGE"></a> <a id="aud__intf__types_8h_1a2318cca3b5827df956e961816fb30f04a3b187623fd90255a04139c772d3125e3"></a> enumerator AUD\_INTF\_VOC\_AEC\_INIT\_FLAG
    :   init flag, aec module feature enable

    <a id="_CPPv4N23aud_intf_voc_aec_para_t26AUD_INTF_VOC_AEC_MIC_DELAYE"></a>

    <a id="_CPPv3N23aud_intf_voc_aec_para_t26AUD_INTF_VOC_AEC_MIC_DELAYE"></a> <a id="_CPPv2N23aud_intf_voc_aec_para_t26AUD_INTF_VOC_AEC_MIC_DELAYE"></a> <a id="aud__intf__types_8h_1a2318cca3b5827df956e961816fb30f04a8ee8771188c20230910ab5922a072e73"></a> enumerator AUD\_INTF\_VOC\_AEC\_MIC\_DELAY
    :   mic\_delay

    <a id="_CPPv4N23aud_intf_voc_aec_para_t25AUD_INTF_VOC_AEC_EC_DEPTHE"></a>

    <a id="_CPPv3N23aud_intf_voc_aec_para_t25AUD_INTF_VOC_AEC_EC_DEPTHE"></a> <a id="_CPPv2N23aud_intf_voc_aec_para_t25AUD_INTF_VOC_AEC_EC_DEPTHE"></a> <a id="aud__intf__types_8h_1a2318cca3b5827df956e961816fb30f04add28be0adb2c34417245b8f7aabd5cec"></a> enumerator AUD\_INTF\_VOC\_AEC\_EC\_DEPTH
    :   ec\_depth

    <a id="_CPPv4N23aud_intf_voc_aec_para_t26AUD_INTF_VOC_AEC_REF_SCALEE"></a>

    <a id="_CPPv3N23aud_intf_voc_aec_para_t26AUD_INTF_VOC_AEC_REF_SCALEE"></a> <a id="_CPPv2N23aud_intf_voc_aec_para_t26AUD_INTF_VOC_AEC_REF_SCALEE"></a> <a id="aud__intf__types_8h_1a2318cca3b5827df956e961816fb30f04aa1b9e2cb82f1d1bc8b33a1afbb69e392"></a> enumerator AUD\_INTF\_VOC\_AEC\_REF\_SCALE
    :   ref\_scale: 0/1/2

    <a id="_CPPv4N23aud_intf_voc_aec_para_t26AUD_INTF_VOC_AEC_VOICE_VOLE"></a>

    <a id="_CPPv3N23aud_intf_voc_aec_para_t26AUD_INTF_VOC_AEC_VOICE_VOLE"></a> <a id="_CPPv2N23aud_intf_voc_aec_para_t26AUD_INTF_VOC_AEC_VOICE_VOLE"></a> <a id="aud__intf__types_8h_1a2318cca3b5827df956e961816fb30f04a6298e24443a485ccb659289a7dbfa167"></a> enumerator AUD\_INTF\_VOC\_AEC\_VOICE\_VOL
    :   voice volume level

    <a id="_CPPv4N23aud_intf_voc_aec_para_t25AUD_INTF_VOC_AEC_TXRX_THRE"></a>

    <a id="_CPPv3N23aud_intf_voc_aec_para_t25AUD_INTF_VOC_AEC_TXRX_THRE"></a> <a id="_CPPv2N23aud_intf_voc_aec_para_t25AUD_INTF_VOC_AEC_TXRX_THRE"></a> <a id="aud__intf__types_8h_1a2318cca3b5827df956e961816fb30f04ae7f17ed9227cbde917b8ba803e01c70f"></a> enumerator AUD\_INTF\_VOC\_AEC\_TXRX\_THR
    :   max amplitude of rx audio data

    <a id="_CPPv4N23aud_intf_voc_aec_para_t25AUD_INTF_VOC_AEC_TXRX_FLRE"></a>

    <a id="_CPPv3N23aud_intf_voc_aec_para_t25AUD_INTF_VOC_AEC_TXRX_FLRE"></a> <a id="_CPPv2N23aud_intf_voc_aec_para_t25AUD_INTF_VOC_AEC_TXRX_FLRE"></a> <a id="aud__intf__types_8h_1a2318cca3b5827df956e961816fb30f04a50f8bd2d2f28edad4bdac116ec0d6336"></a> enumerator AUD\_INTF\_VOC\_AEC\_TXRX\_FLR
    :   min amplitude of rx audio data

    <a id="_CPPv4N23aud_intf_voc_aec_para_t25AUD_INTF_VOC_AEC_NS_LEVELE"></a>

    <a id="_CPPv3N23aud_intf_voc_aec_para_t25AUD_INTF_VOC_AEC_NS_LEVELE"></a> <a id="_CPPv2N23aud_intf_voc_aec_para_t25AUD_INTF_VOC_AEC_NS_LEVELE"></a> <a id="aud__intf__types_8h_1a2318cca3b5827df956e961816fb30f04aa9a61bddaf58ff04e2b08b63007c4d15"></a> enumerator AUD\_INTF\_VOC\_AEC\_NS\_LEVEL
    :   noise level: 0/1/2

    <a id="_CPPv4N23aud_intf_voc_aec_para_t24AUD_INTF_VOC_AEC_NS_PARAE"></a>

    <a id="_CPPv3N23aud_intf_voc_aec_para_t24AUD_INTF_VOC_AEC_NS_PARAE"></a> <a id="_CPPv2N23aud_intf_voc_aec_para_t24AUD_INTF_VOC_AEC_NS_PARAE"></a> <a id="aud__intf__types_8h_1a2318cca3b5827df956e961816fb30f04a155b8fce75f9885d036492ec2dc7adf7"></a> enumerator AUD\_INTF\_VOC\_AEC\_NS\_PARA
    :   noise value, range:1\~8

    <a id="_CPPv4N23aud_intf_voc_aec_para_t20AUD_INTF_VOC_AEC_DRCE"></a>

    <a id="_CPPv3N23aud_intf_voc_aec_para_t20AUD_INTF_VOC_AEC_DRCE"></a> <a id="_CPPv2N23aud_intf_voc_aec_para_t20AUD_INTF_VOC_AEC_DRCE"></a> <a id="aud__intf__types_8h_1a2318cca3b5827df956e961816fb30f04a6aaf5881bf178922d920404e58aa87cd"></a> enumerator AUD\_INTF\_VOC\_AEC\_DRC
    :   voice volume value, range:0x10\~0x1f

    <a id="_CPPv4N23aud_intf_voc_aec_para_t20AUD_INTF_VOC_AEC_MAXE"></a>

    <a id="_CPPv3N23aud_intf_voc_aec_para_t20AUD_INTF_VOC_AEC_MAXE"></a> <a id="_CPPv2N23aud_intf_voc_aec_para_t20AUD_INTF_VOC_AEC_MAXE"></a> <a id="aud__intf__types_8h_1a2318cca3b5827df956e961816fb30f04a456317365f5c3ae93e87e91eff39c288"></a> enumerator AUD\_INTF\_VOC\_AEC\_MAX

<a id="_CPPv423aud_intf_voc_mic_ctrl_t"></a>

<a id="_CPPv323aud_intf_voc_mic_ctrl_t"></a> <a id="_CPPv223aud_intf_voc_mic_ctrl_t"></a> <a id="aud__intf__types_8h_1ab4ec21268a70221470255ac0fe5ce24b"></a> enum aud\_intf\_voc\_mic\_ctrl\_t
:   *Values:*

    <a id="_CPPv4N23aud_intf_voc_mic_ctrl_t21AUD_INTF_VOC_MIC_OPENE"></a>

    <a id="_CPPv3N23aud_intf_voc_mic_ctrl_t21AUD_INTF_VOC_MIC_OPENE"></a> <a id="_CPPv2N23aud_intf_voc_mic_ctrl_t21AUD_INTF_VOC_MIC_OPENE"></a> <a id="aud__intf__types_8h_1ab4ec21268a70221470255ac0fe5ce24bafc6f80872b10f8992c3a47c72860dbfc"></a> enumerator AUD\_INTF\_VOC\_MIC\_OPEN
    :   open mic

    <a id="_CPPv4N23aud_intf_voc_mic_ctrl_t22AUD_INTF_VOC_MIC_CLOSEE"></a>

    <a id="_CPPv3N23aud_intf_voc_mic_ctrl_t22AUD_INTF_VOC_MIC_CLOSEE"></a> <a id="_CPPv2N23aud_intf_voc_mic_ctrl_t22AUD_INTF_VOC_MIC_CLOSEE"></a> <a id="aud__intf__types_8h_1ab4ec21268a70221470255ac0fe5ce24ba9c2c6acd5bcd5056e55011bc3f4b1c14"></a> enumerator AUD\_INTF\_VOC\_MIC\_CLOSE
    :   close spk

    <a id="_CPPv4N23aud_intf_voc_mic_ctrl_t20AUD_INTF_VOC_MIC_MAXE"></a>

    <a id="_CPPv3N23aud_intf_voc_mic_ctrl_t20AUD_INTF_VOC_MIC_MAXE"></a> <a id="_CPPv2N23aud_intf_voc_mic_ctrl_t20AUD_INTF_VOC_MIC_MAXE"></a> <a id="aud__intf__types_8h_1ab4ec21268a70221470255ac0fe5ce24bab7ee99fc447ecd759642793fffa5d800"></a> enumerator AUD\_INTF\_VOC\_MIC\_MAX

<a id="_CPPv423aud_intf_voc_spk_ctrl_t"></a>

<a id="_CPPv323aud_intf_voc_spk_ctrl_t"></a> <a id="_CPPv223aud_intf_voc_spk_ctrl_t"></a> <a id="aud__intf__types_8h_1a6dbfcf3c36c3470b0bd83e3c77fc88b8"></a> enum aud\_intf\_voc\_spk\_ctrl\_t
:   *Values:*

    <a id="_CPPv4N23aud_intf_voc_spk_ctrl_t21AUD_INTF_VOC_SPK_OPENE"></a>

    <a id="_CPPv3N23aud_intf_voc_spk_ctrl_t21AUD_INTF_VOC_SPK_OPENE"></a> <a id="_CPPv2N23aud_intf_voc_spk_ctrl_t21AUD_INTF_VOC_SPK_OPENE"></a> <a id="aud__intf__types_8h_1a6dbfcf3c36c3470b0bd83e3c77fc88b8a93a51b6dd1b34707a078c0af409b5499"></a> enumerator AUD\_INTF\_VOC\_SPK\_OPEN
    :   open spk

    <a id="_CPPv4N23aud_intf_voc_spk_ctrl_t22AUD_INTF_VOC_SPK_CLOSEE"></a>

    <a id="_CPPv3N23aud_intf_voc_spk_ctrl_t22AUD_INTF_VOC_SPK_CLOSEE"></a> <a id="_CPPv2N23aud_intf_voc_spk_ctrl_t22AUD_INTF_VOC_SPK_CLOSEE"></a> <a id="aud__intf__types_8h_1a6dbfcf3c36c3470b0bd83e3c77fc88b8a0b659b507629b674b9be9030883363ec"></a> enumerator AUD\_INTF\_VOC\_SPK\_CLOSE
    :   close spk

    <a id="_CPPv4N23aud_intf_voc_spk_ctrl_t20AUD_INTF_VOC_SPK_MAXE"></a>

    <a id="_CPPv3N23aud_intf_voc_spk_ctrl_t20AUD_INTF_VOC_SPK_MAXE"></a> <a id="_CPPv2N23aud_intf_voc_spk_ctrl_t20AUD_INTF_VOC_SPK_MAXE"></a> <a id="aud__intf__types_8h_1a6dbfcf3c36c3470b0bd83e3c77fc88b8a9375f16fed885735d9d53c1a4e9caa78"></a> enumerator AUD\_INTF\_VOC\_SPK\_MAX
