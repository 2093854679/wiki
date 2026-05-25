# Aud_Intf APIs[](#aud-intf-apis "永久链接至标题")

[[English]](../../../../en/v1.5/api-reference/multi_media/bk_aud_intf.html "../../../../en/v1.5/api-reference/multi_media/bk_aud_intf.html")

重要

The Aud_Intf API v1.0 is the lastest and stable Audio interface APIs. All new applications should use Audio interface API v1.0.
And all Aud_Intf API cannot be called in mic and speaker callback registed in bk_aud_intf_drv_init .


## Audio Interface[](#audio-interface "永久链接至标题")

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


## Audio Interface API Categories[](#audio-interface-api-categories "永久链接至标题")

Most of Audio APIs can be categoried as:

> - Common APIs
>
>   The common APIs are prefixed with bk_aud_intf, the APIs may be common for General mode and Voice mode, e.g. bk_aud_intf_drv_init() etc.
> - Mic function APIs.
>
>   The APIs provide support for record function. e.g. bk_aud_intf_mic_init() etc.
> - Spk function APIs.
>
>   The APIs provide support for play function. e.g. bk_aud_intf_spk_init() etc.
> - Voc function APIs.
>
>   The APIs provide support for voice transfer function. e.g. bk_aud_intf_voc_init() etc.

Common APIs:
:   - [`bk_aud_intf_drv_init()`](#_CPPv420bk_aud_intf_drv_initP20aud_intf_drv_setup_t "bk_aud_intf_drv_init") - init the audio interface driver

    - [`bk_aud_intf_drv_deinit()`](#_CPPv422bk_aud_intf_drv_deinitv "bk_aud_intf_drv_deinit") - deinit the audio interface driver

    - [`bk_aud_intf_set_mode()`](#_CPPv420bk_aud_intf_set_mode20aud_intf_work_mode_t "bk_aud_intf_set_mode") - set audio interface work mode

    - [`bk_aud_intf_set_mic_gain()`](#_CPPv424bk_aud_intf_set_mic_gain7uint8_t "bk_aud_intf_set_mic_gain") - set audio mic gain

    - [`bk_aud_intf_set_spk_gain()`](#_CPPv424bk_aud_intf_set_spk_gain8uint32_t "bk_aud_intf_set_spk_gain") - set audio speaker gain

    - [`bk_aud_intf_write_spk_data()`](#_CPPv426bk_aud_intf_write_spk_dataP7uint8_t8uint32_t "bk_aud_intf_write_spk_data") - write data to sperker

Mic APIs:
:   - [`bk_aud_intf_mic_init()`](#_CPPv420bk_aud_intf_mic_initP20aud_intf_mic_setup_t "bk_aud_intf_mic_init") - init the mic function

    - [`bk_aud_intf_mic_deinit()`](#_CPPv422bk_aud_intf_mic_deinitv "bk_aud_intf_mic_deinit") - deinit the mic function

    - [`bk_aud_intf_mic_start()`](#_CPPv421bk_aud_intf_mic_startv "bk_aud_intf_mic_start") - start mic work

    - [`bk_aud_intf_mic_pause()`](#_CPPv421bk_aud_intf_mic_pausev "bk_aud_intf_mic_pause") - pause mic work

    - [`bk_aud_intf_mic_stop()`](#_CPPv420bk_aud_intf_mic_stopv "bk_aud_intf_mic_stop") - stop mic work

    - [`bk_aud_intf_set_mic_chl()`](#_CPPv423bk_aud_intf_set_mic_chl18aud_intf_mic_chl_t "bk_aud_intf_set_mic_chl") - set mic channel in work

    - [`bk_aud_intf_get_mic_chl()`](#_CPPv423bk_aud_intf_get_mic_chlP18aud_intf_mic_chl_t "bk_aud_intf_get_mic_chl") - get mic channel in work

    - [`bk_aud_intf_set_mic_samp_rate()`](#_CPPv429bk_aud_intf_set_mic_samp_rate19aud_adc_samp_rate_t "bk_aud_intf_set_mic_samp_rate") - set mic sample rate

    - [`bk_aud_intf_get_mic_samp_rate()`](#_CPPv429bk_aud_intf_get_mic_samp_rateP19aud_adc_samp_rate_t "bk_aud_intf_get_mic_samp_rate") - get mic sample rate

Spk APIs:
:   - [`bk_aud_intf_spk_init()`](#_CPPv420bk_aud_intf_spk_initP20aud_intf_spk_setup_t "bk_aud_intf_spk_init") - init the speaker function

    - [`bk_aud_intf_spk_deinit()`](#_CPPv422bk_aud_intf_spk_deinitv "bk_aud_intf_spk_deinit") - deinit the speaker function

    - [`bk_aud_intf_spk_start()`](#_CPPv421bk_aud_intf_spk_startv "bk_aud_intf_spk_start") - start speaker work

    - [`bk_aud_intf_spk_pause()`](#_CPPv421bk_aud_intf_spk_pausev "bk_aud_intf_spk_pause") - pause speaker work

    - [`bk_aud_intf_spk_stop()`](#_CPPv420bk_aud_intf_spk_stopv "bk_aud_intf_spk_stop") - stop speaker work

    - [`bk_aud_intf_set_spk_chl()`](#_CPPv423bk_aud_intf_set_spk_chl18aud_intf_spk_chl_t "bk_aud_intf_set_spk_chl") - set speaker channel in work

    - [`bk_aud_intf_get_spk_chl()`](#_CPPv423bk_aud_intf_get_spk_chlP18aud_intf_mic_chl_t "bk_aud_intf_get_spk_chl") - get speaker channel in work

    - [`bk_aud_intf_set_spk_samp_rate()`](#_CPPv429bk_aud_intf_set_spk_samp_rate19aud_dac_samp_rate_t "bk_aud_intf_set_spk_samp_rate") - set speaker sample rate

    - [`bk_aud_intf_get_spk_samp_rate()`](#_CPPv429bk_aud_intf_get_spk_samp_rateP19aud_dac_samp_rate_t "bk_aud_intf_get_spk_samp_rate") - get speaker sample rate

Voc APIs:
:   - [`bk_aud_intf_voc_init()`](#_CPPv420bk_aud_intf_voc_init20aud_intf_voc_setup_t "bk_aud_intf_voc_init") - init the voice transfer function

    - [`bk_aud_intf_voc_deinit()`](#_CPPv422bk_aud_intf_voc_deinitv "bk_aud_intf_voc_deinit") - deinit the voice transfer function

    - [`bk_aud_intf_voc_start()`](#_CPPv421bk_aud_intf_voc_startv "bk_aud_intf_voc_start") - start voice transfer

    - [`bk_aud_intf_voc_stop()`](#_CPPv420bk_aud_intf_voc_stopv "bk_aud_intf_voc_stop") - stop voice transfer

    - [`bk_aud_intf_set_aec_para()`](#_CPPv424bk_aud_intf_set_aec_para23aud_intf_voc_aec_para_t8uint32_t "bk_aud_intf_set_aec_para") - set aec parameter

    - [`bk_aud_intf_get_aec_para()`](#_CPPv424bk_aud_intf_get_aec_parav "bk_aud_intf_get_aec_para") - get aec parameter

    - [`bk_aud_intf_voc_tx_debug()`](#_CPPv424bk_aud_intf_voc_tx_debug27aud_intf_dump_data_callback "bk_aud_intf_voc_tx_debug") - register voice tx debug callback

    - [`bk_aud_intf_voc_rx_debug()`](#_CPPv424bk_aud_intf_voc_rx_debug27aud_intf_dump_data_callback "bk_aud_intf_voc_rx_debug") - register voice rx debug callback

    - [`bk_aud_intf_voc_aec_debug()`](#_CPPv425bk_aud_intf_voc_aec_debug27aud_intf_dump_data_callback "bk_aud_intf_voc_aec_debug") - register voice aec debug callback


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [aud_intf.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/aud_intf.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/aud_intf.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_drv_init([aud_intf_drv_setup_t](#_CPPv420aud_intf_drv_setup_t "aud_intf_drv_setup_t") *setup)[](#_CPPv420bk_aud_intf_drv_initP20aud_intf_drv_setup_t "永久链接至目标")
:   Init the AUD INTF driver.

    This API init the resoure common:


    - Creat AUD INTF task

    - Configure default work mode

    - Register read mic data and write speaker data callback

    This API should be called before any other AUD INTF APIs. This API cannot be called in mic and speaker callback.

    参数
    :   **setup** – audio interface driver init configuration

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_drv_deinit(void)[](#_CPPv422bk_aud_intf_drv_deinitv "永久链接至目标")
:   Deinit the AUD INTF driver.

    This API deinit the resoure common:


    - Delete AUD INTF task

    - Reset default work mode

    - Unregister read mic data and write speaker data callback

    This API should be called when audio is not needed. This API cannot be called in mic and speaker callback.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_set_mode([aud_intf_work_mode_t](#_CPPv420aud_intf_work_mode_t "aud_intf_work_mode_t") work_mode)[](#_CPPv420bk_aud_intf_set_mode20aud_intf_work_mode_t "永久链接至目标")
:   Set the AUD INTF work mode.

    This API cannot be called in mic and speaker callback.

    参数
    :   **work_mode** – audio interface work mode

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_set_mic_gain(uint8_t value)[](#_CPPv424bk_aud_intf_set_mic_gain7uint8_t "永久链接至目标")
:   Set the mic gain.

    This API should be called when onboard mic has been initialized. And this API should not be called when UAC mic has been used. This API cannot be called in mic and speaker callback.

    参数
    :   **value** – the gain value range:0x00 ~ 0x3f

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_set_spk_gain(uint32_t value)[](#_CPPv424bk_aud_intf_set_spk_gain8uint32_t "永久链接至目标")
:   Set the spk gain(volume)

    This API should be called when speaker has been initialized. And this API set board speaker gain and uac speaker volume. This API cannot be called in mic and speaker callback.

    参数
    :   **value** – the gain value -board speaker: range:0x00 ~ 0x3f -uac speaker: range:0x0000 ~ 0xffff

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_set_aec_para([aud_intf_voc_aec_para_t](#_CPPv423aud_intf_voc_aec_para_t "aud_intf_voc_aec_para_t") aec_para, uint32_t value)[](#_CPPv424bk_aud_intf_set_aec_para23aud_intf_voc_aec_para_t8uint32_t "永久链接至目标")
:   Set the aec parameter.

    This API should be called when voice has been initialized and AEC is enable. This API cannot be called in mic and speaker callback.

    参数
    :   - **aec_para** – the parameter

        - **value** – the parameter value

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_get_aec_para(void)[](#_CPPv424bk_aud_intf_get_aec_parav "永久链接至目标")
:   Get the aec parameter.

    This API should be called when voice has been initialized and AEC is enable. This API cannot be called in mic and speaker callback.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_mic_init([aud_intf_mic_setup_t](#_CPPv420aud_intf_mic_setup_t "aud_intf_mic_setup_t") *mic_setup)[](#_CPPv420bk_aud_intf_mic_initP20aud_intf_mic_setup_t "永久链接至目标")
:   Init the AUD INTF mic.

    This API init the resoure common:


    - Init AUD adc driver

    - Configure AUD adc paramter

    - Configure DMA to carry adc data

    - Configure UAC mic

    This API should be called after bk_aud_intf_drv_init. This API cannot be called in mic and speaker callback.

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
    :   **mic_setup** – audio adc setup configuration

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_mic_deinit(void)[](#_CPPv422bk_aud_intf_mic_deinitv "永久链接至目标")
:   Deinit the AUD INTF mic.

    This API deinit the resoure common:


    - Deinit AUD adc driver

    - Reset AUD adc paramter

    - Close DMA

    - Close UAC mic

    This API should be called after bk_aud_intf_mic_stop. This API cannot be called in mic and speaker callback.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_mic_start(void)[](#_CPPv421bk_aud_intf_mic_startv "永久链接至目标")
:   Start the AUD INTF mic work.

    This API cannot be called in mic and speaker callback.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_mic_pause(void)[](#_CPPv421bk_aud_intf_mic_pausev "永久链接至目标")
:   Pause the AUD INTF mic work.

    This API should be called after bk_aud_intf_mic_init. This API cannot be called in mic and speaker callback.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_mic_stop(void)[](#_CPPv420bk_aud_intf_mic_stopv "永久链接至目标")
:   Stop the AUD INTF mic work.

    This API cannot be called in mic and speaker callback.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_set_mic_chl([aud_intf_mic_chl_t](#_CPPv418aud_intf_mic_chl_t "aud_intf_mic_chl_t") mic_chl)[](#_CPPv423bk_aud_intf_set_mic_chl18aud_intf_mic_chl_t "永久链接至目标")
:   Set the AUD INTF mic channel.

    This API should be called after bk_aud_intf_mic_init. This API only support onboard mic, and not support UAC mic. This API cannot be called in mic and speaker callback.

    参数
    :   **mic_chl** – audio interface mic channel

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_get_mic_chl([aud_intf_mic_chl_t](#_CPPv418aud_intf_mic_chl_t "aud_intf_mic_chl_t") *mic_chl)[](#_CPPv423bk_aud_intf_get_mic_chlP18aud_intf_mic_chl_t "永久链接至目标")
:   Get the AUD INTF mic channel.

    This API should be called after bk_aud_intf_mic_init. This API only support onboard mic, and not support UAC mic. This API cannot be called in mic and speaker callback.

    参数
    :   **mic_chl** – save audio interface mic channel

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_set_mic_samp_rate([aud_adc_samp_rate_t](bk_audio.html#_CPPv419aud_adc_samp_rate_t "aud_adc_samp_rate_t") samp_rate)[](#_CPPv429bk_aud_intf_set_mic_samp_rate19aud_adc_samp_rate_t "永久链接至目标")
:   Set the AUD INTF mic sample rate.

    This API should be called after bk_aud_intf_mic_init. This API only support onboard mic, and not support UAC mic. This API cannot be called in mic and speaker callback.

    参数
    :   **samp_rate** – audio interface mic sample rate

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_get_mic_samp_rate([aud_adc_samp_rate_t](bk_audio.html#_CPPv419aud_adc_samp_rate_t "aud_adc_samp_rate_t") *samp_rate)[](#_CPPv429bk_aud_intf_get_mic_samp_rateP19aud_adc_samp_rate_t "永久链接至目标")
:   Get the AUD INTF mic sample rate.

    This API should be called after bk_aud_intf_mic_init. This API only support onboard mic, and not support UAC mic. This API cannot be called in mic and speaker callback.

    参数
    :   **samp_rate** – save audio interface mic sample rate

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_spk_init([aud_intf_spk_setup_t](#_CPPv420aud_intf_spk_setup_t "aud_intf_spk_setup_t") *spk_setup)[](#_CPPv420bk_aud_intf_spk_initP20aud_intf_spk_setup_t "永久链接至目标")
:   Init the AUD INTF speaker.

    This API init the resoure common:


    - Init AUD dac driver

    - Configure AUD dac paramter

    - Configure DMA to carry dac data

    - Configure UAC speaker

    This API should be called after bk_aud_intf_drv_init. This API cannot be called in mic and speaker callback.

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
    :   **spk_setup** – audio speaker setup configuration

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_spk_deinit(void)[](#_CPPv422bk_aud_intf_spk_deinitv "永久链接至目标")
:   Deinit the AUD INTF speaker.

    This API deinit the resoure common:


    - Deinit AUD dac driver

    - Reset AUD dac paramter

    - Close DMA

    - Close UAC speaker

    This API should be called after bk_aud_intf_spk_stop. This API cannot be called in mic and speaker callback.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_spk_start(void)[](#_CPPv421bk_aud_intf_spk_startv "永久链接至目标")
:   Start the AUD INTF speaker work.

    This API cannot be called in mic and speaker callback.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_spk_pause(void)[](#_CPPv421bk_aud_intf_spk_pausev "永久链接至目标")
:   Pause the AUD INTF speaker work.

    This API cannot be called in mic and speaker callback.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_spk_stop(void)[](#_CPPv420bk_aud_intf_spk_stopv "永久链接至目标")
:   Stop the AUD INTF speaker work.

    This API cannot be called in mic and speaker callback.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_set_spk_chl([aud_intf_spk_chl_t](#_CPPv418aud_intf_spk_chl_t "aud_intf_spk_chl_t") spk_chl)[](#_CPPv423bk_aud_intf_set_spk_chl18aud_intf_spk_chl_t "永久链接至目标")
:   Set the AUD INTF speaker channel.

    This API should be called after bk_aud_intf_spk_init. This API only support onboard speaker, and not support UAC speaker. This API cannot be called in mic and speaker callback.

    参数
    :   **spk_chl** – audio interface speaker channel

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_get_spk_chl([aud_intf_mic_chl_t](#_CPPv418aud_intf_mic_chl_t "aud_intf_mic_chl_t") *spk_chl)[](#_CPPv423bk_aud_intf_get_spk_chlP18aud_intf_mic_chl_t "永久链接至目标")
:   Get the AUD INTF speaker channel.

    This API should be called after bk_aud_intf_spk_init. This API only support onboard speaker, and not support UAC speaker. This API cannot be called in mic and speaker callback.

    参数
    :   **spk_chl** – save audio interface speaker channel

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_set_spk_samp_rate([aud_dac_samp_rate_t](bk_audio.html#_CPPv419aud_dac_samp_rate_t "aud_dac_samp_rate_t") samp_rate)[](#_CPPv429bk_aud_intf_set_spk_samp_rate19aud_dac_samp_rate_t "永久链接至目标")
:   Set the AUD INTF speaker sample rate.

    This API should be called after bk_aud_intf_spk_init. This API only support onboard speaker, and not support UAC speaker. This API cannot be called in mic and speaker callback.

    参数
    :   **samp_rate** – audio interface speaker sample rate

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_get_spk_samp_rate([aud_dac_samp_rate_t](bk_audio.html#_CPPv419aud_dac_samp_rate_t "aud_dac_samp_rate_t") *samp_rate)[](#_CPPv429bk_aud_intf_get_spk_samp_rateP19aud_dac_samp_rate_t "永久链接至目标")
:   Get the AUD INTF speaker sample rate.

    This API should be called after bk_aud_intf_spk_init. This API only support onboard speaker, and not support UAC speaker. This API cannot be called in mic and speaker callback.

    参数
    :   **samp_rate** – save audio interface speaker sample rate

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_register_uac_connect_state_cb(void *cb)[](#_CPPv441bk_aud_intf_register_uac_connect_state_cbPv "永久链接至目标")
:   Register callback of uac abnormal disconnection and connection recovery.

    This API should be called after bk_aud_intf_spk_init. This API only support uac mic and uac speaker. This API cannot be called in mic and speaker callback.

    参数
    :   **cb** – callback api

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_uac_auto_connect_ctrl(bool enable)[](#_CPPv433bk_aud_intf_uac_auto_connect_ctrlb "永久链接至目标")
:   Control uac automatical connect.

    If enable the feature, uac will automatic connect after uac abnormal disconnect. This API only support uac mic and uac speaker. This feature is enabled by default. This API cannot be called in mic and speaker callback.

    参数
    :   **enable** –


        - TRUE: enable uac automatic connnet

        - FALSE: disable uac automatic connent

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_voc_init([aud_intf_voc_setup_t](#_CPPv420aud_intf_voc_setup_t "aud_intf_voc_setup_t") setup)[](#_CPPv420bk_aud_intf_voc_init20aud_intf_voc_setup_t "永久链接至目标")
:   Init the AUD INTF voice.

    This API init the resoure common:


    - Init AUD voice transfer driver

    - Configure AUD dac and adc paramter

    - Configure DMA to carry adc and dac data

    - Configure UAC mic and speaker

    This API should be called after bk_aud_intf_drv_init. This API cannot be called in mic and speaker callback.

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
    :   **voc_setup** – audio voice setup configuration

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_voc_deinit(void)[](#_CPPv422bk_aud_intf_voc_deinitv "永久链接至目标")
:   Deinit the AUD INTF voice.

    This API deinit the resoure common:


    - Deinit AUD voice transfer driver

    - Reset AUD adc and dac paramter

    - Close DMA

    This API should be called after bk_aud_intf_voice_stop. This API cannot be called in mic and speaker callback.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_voc_start(void)[](#_CPPv421bk_aud_intf_voc_startv "永久链接至目标")
:   Start the AUD INTF voice work.

    This API cannot be called in mic and speaker callback.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_voc_stop(void)[](#_CPPv420bk_aud_intf_voc_stopv "永久链接至目标")
:   Stop the AUD INTF voice work.

    This API cannot be called in mic and speaker callback.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_voc_mic_ctrl([aud_intf_voc_mic_ctrl_t](#_CPPv423aud_intf_voc_mic_ctrl_t "aud_intf_voc_mic_ctrl_t") mic_en)[](#_CPPv424bk_aud_intf_voc_mic_ctrl23aud_intf_voc_mic_ctrl_t "永久链接至目标")
:   Control mic.

    This API should be called in voice work mode. This API cannot be called in mic and speaker callback.

    参数
    :   **mic_en** –


        - AUD_INTF_VOC_MIC_OPEN: enable mic

        - AUD_INTF_VOC_MIC_CLOSE: disable mic

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_voc_spk_ctrl([aud_intf_voc_spk_ctrl_t](#_CPPv423aud_intf_voc_spk_ctrl_t "aud_intf_voc_spk_ctrl_t") spk_en)[](#_CPPv424bk_aud_intf_voc_spk_ctrl23aud_intf_voc_spk_ctrl_t "永久链接至目标")
:   Control speaker.

    This API should be called in voice work mode. This API cannot be called in mic and speaker callback.

    参数
    :   **spk_en** –


        - AUD_INTF_VOC_SPK_OPEN: enable speaker

        - AUD_INTF_VOC_SPK_CLOSE: disable speaker

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_voc_aec_ctrl(bool aec_en)[](#_CPPv424bk_aud_intf_voc_aec_ctrlb "永久链接至目标")
:   Control aec enable or disable.

    This API should be called in voice work mode. This API cannot be called in mic and speaker callback.

    参数
    :   **aec_en** –


        - true: enable aec

        - false: disable aec

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_write_spk_data(uint8_t *dac_buff, uint32_t size)[](#_CPPv426bk_aud_intf_write_spk_dataP7uint8_t8uint32_t "永久链接至目标")
:   Write the speaker data to audio dac.

    This API should be called in general and voice work mode. This API cannot be called in mic and speaker callback.

    参数
    :   - **dac_buff** – the address of speaker data written

        - **size** – the data size (byte)

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_voc_tx_debug([aud_intf_dump_data_callback](#_CPPv427aud_intf_dump_data_callback "aud_intf_dump_data_callback") dump_callback)[](#_CPPv424bk_aud_intf_voc_tx_debug27aud_intf_dump_data_callback "永久链接至目标")
:   register callback to dump tx data in voice work mode

    This API should be called in voice work mode. And audio transfer driver will call the callback to save data. This API cannot be called in mic and speaker callback.

    参数
    :   **dump_callback** – callback

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_voc_rx_debug([aud_intf_dump_data_callback](#_CPPv427aud_intf_dump_data_callback "aud_intf_dump_data_callback") dump_callback)[](#_CPPv424bk_aud_intf_voc_rx_debug27aud_intf_dump_data_callback "永久链接至目标")
:   register callback to dump rx data in voice work mode

    This API should be called in voice work mode. And audio transfer driver will call the callback to save data. This API cannot be called in mic and speaker callback.

    参数
    :   **dump_callback** – callback

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_aud_intf_voc_aec_debug([aud_intf_dump_data_callback](#_CPPv427aud_intf_dump_data_callback "aud_intf_dump_data_callback") dump_callback)[](#_CPPv425bk_aud_intf_voc_aec_debug27aud_intf_dump_data_callback "永久链接至目标")
:   register callback to dump aec data(include mic data, ref data, and out data) in voice work mode

    This API should be called in voice work mode. And audio transfer driver will call the callback to save data. This API cannot be called in mic and speaker callback.

    参数
    :   **dump_callback** – callback

    返回
    :   - BK_OK: succeed

        - others: other errors.


## API Typedefs[](#api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [aud_intf_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/aud_intf_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/aud_intf_types.h")


### Structures[](#structures "永久链接至标题")

struct aud_intf_task_config_t[](#_CPPv422aud_intf_task_config_t "永久链接至目标")
:   Public Members

    uint8_t priority[](#_CPPv4N22aud_intf_task_config_t8priorityE "永久链接至目标")
    :   the priority of audio interface task

struct aud_intf_drv_setup_t[](#_CPPv420aud_intf_drv_setup_t "永久链接至目标")
:   Public Members

    int (*aud_intf_tx_mic_data)(unsigned char *data, unsigned int size)[](#_CPPv4N20aud_intf_drv_setup_t20aud_intf_tx_mic_dataE "永久链接至目标")
    :   the api is called when collecting a frame mic packet data is complete

    [bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") (*aud_intf_rx_spk_data)(unsigned int size)[](#_CPPv4N20aud_intf_drv_setup_t20aud_intf_rx_spk_dataE "永久链接至目标")
    :   the api is called when playing a frame speaker packet data is complete

struct aud_intf_mic_setup_t[](#_CPPv420aud_intf_mic_setup_t "永久链接至目标")
:   Public Members

    [aud_adc_samp_rate_t](bk_audio.html#_CPPv419aud_adc_samp_rate_t "aud_adc_samp_rate_t") samp_rate[](#_CPPv4N20aud_intf_mic_setup_t9samp_rateE "永久链接至目标")
    :   mic sample rate

    uint16_t frame_size[](#_CPPv4N20aud_intf_mic_setup_t10frame_sizeE "永久链接至目标")
    :   size: a frame packet mic data size(byte)

    uint8_t mic_gain[](#_CPPv4N20aud_intf_mic_setup_t8mic_gainE "永久链接至目标")
    :   audio adc gain: value range:0x0 ~ 0x3f, suggest:0x2d

    [aud_intf_mic_type_t](#_CPPv419aud_intf_mic_type_t "aud_intf_mic_type_t") mic_type[](#_CPPv4N20aud_intf_mic_setup_t8mic_typeE "永久链接至目标")
    :   audio mic type: uac or microphone

    [aud_adc_intf_mode_t](bk_audio.html#_CPPv419aud_adc_intf_mode_t "aud_adc_intf_mode_t") mic_mode[](#_CPPv4N20aud_intf_mic_setup_t8mic_modeE "永久链接至目标")
    :   audio mic mode: signal_ended/differen

struct aud_intf_spk_setup_t[](#_CPPv420aud_intf_spk_setup_t "永久链接至目标")
:   Public Members

    [aud_dac_samp_rate_t](bk_audio.html#_CPPv419aud_dac_samp_rate_t "aud_dac_samp_rate_t") samp_rate[](#_CPPv4N20aud_intf_spk_setup_t9samp_rateE "永久链接至目标")
    :   speaker sample rate

    uint16_t frame_size[](#_CPPv4N20aud_intf_spk_setup_t10frame_sizeE "永久链接至目标")
    :   size: a frame packet speaker data size(byte)

    uint8_t spk_gain[](#_CPPv4N20aud_intf_spk_setup_t8spk_gainE "永久链接至目标")
    :   audio dac gain: value range:0x0 ~ 0x3f, suggest:0x2d

    [aud_dac_work_mode_t](bk_audio.html#_CPPv419aud_dac_work_mode_t "aud_dac_work_mode_t") work_mode[](#_CPPv4N20aud_intf_spk_setup_t9work_modeE "永久链接至目标")
    :   audio dac mode: signal_ended/differen

    [aud_intf_spk_type_t](#_CPPv419aud_intf_spk_type_t "aud_intf_spk_type_t") spk_type[](#_CPPv4N20aud_intf_spk_setup_t8spk_typeE "永久链接至目标")
    :   audio speaker type: uac or speaker

struct aud_intf_voc_aec_cfg_t[](#_CPPv422aud_intf_voc_aec_cfg_t "永久链接至目标")
:   Public Members

    uint32_t ec_depth[](#_CPPv4N22aud_intf_voc_aec_cfg_t8ec_depthE "永久链接至目标")
    :   recommended value range: 1~50, the greater the echo, the greater the value setting

    uint32_t TxRxThr[](#_CPPv4N22aud_intf_voc_aec_cfg_t7TxRxThrE "永久链接至目标")
    :   the max amplitude of rx audio data

    uint32_t TxRxFlr[](#_CPPv4N22aud_intf_voc_aec_cfg_t7TxRxFlrE "永久链接至目标")
    :   the min amplitude of rx audio data

    uint8_t ref_scale[](#_CPPv4N22aud_intf_voc_aec_cfg_t9ref_scaleE "永久链接至目标")
    :   value range:0,1,2, the greater the signal amplitude, the greater the setting

    uint8_t ns_level[](#_CPPv4N22aud_intf_voc_aec_cfg_t8ns_levelE "永久链接至目标")
    :   recommended value range: 1~8, the lower the noise, the lower the level

    uint8_t ns_para[](#_CPPv4N22aud_intf_voc_aec_cfg_t7ns_paraE "永久链接至目标")
    :   value range:0,1,2, the lower the noise, the lower the level, the default valude is recommended

struct aud_intf_voc_setup_t[](#_CPPv420aud_intf_voc_setup_t "永久链接至目标")
:   Public Members

    bool aec_enable[](#_CPPv4N20aud_intf_voc_setup_t10aec_enableE "永久链接至目标")
    :   true: enable aec, false: disable aec

    [aud_intf_voc_samp_rate_t](#_CPPv424aud_intf_voc_samp_rate_t "aud_intf_voc_samp_rate_t") samp_rate[](#_CPPv4N20aud_intf_voc_setup_t9samp_rateE "永久链接至目标")
    :   voice transfer sample rate

    [aud_intf_voc_data_type_t](#_CPPv424aud_intf_voc_data_type_t "aud_intf_voc_data_type_t") data_type[](#_CPPv4N20aud_intf_voc_setup_t9data_typeE "永久链接至目标")
    :   voice data type

    uint8_t mic_gain[](#_CPPv4N20aud_intf_voc_setup_t8mic_gainE "永久链接至目标")
    :   mic gain: value range:0x0 ~ 0x3f, suggest:0x2d

    uint16_t spk_gain[](#_CPPv4N20aud_intf_voc_setup_t8spk_gainE "永久链接至目标")
    :   spk gain: value range:0x0 ~ 0x3f, suggest:0x2d

    [aud_dac_work_mode_t](bk_audio.html#_CPPv419aud_dac_work_mode_t "aud_dac_work_mode_t") spk_mode[](#_CPPv4N20aud_intf_voc_setup_t8spk_modeE "永久链接至目标")
    :   audio spk mode: signal_ended/differen

    [aud_intf_voc_mic_ctrl_t](#_CPPv423aud_intf_voc_mic_ctrl_t "aud_intf_voc_mic_ctrl_t") mic_en[](#_CPPv4N20aud_intf_voc_setup_t6mic_enE "永久链接至目标")
    :   mic default status

    [aud_intf_voc_spk_ctrl_t](#_CPPv423aud_intf_voc_spk_ctrl_t "aud_intf_voc_spk_ctrl_t") spk_en[](#_CPPv4N20aud_intf_voc_setup_t6spk_enE "永久链接至目标")
    :   spk default status

    [aud_intf_mic_type_t](#_CPPv419aud_intf_mic_type_t "aud_intf_mic_type_t") mic_type[](#_CPPv4N20aud_intf_voc_setup_t8mic_typeE "永久链接至目标")
    :   audio mic type: uac or microphone

    [aud_intf_spk_type_t](#_CPPv419aud_intf_spk_type_t "aud_intf_spk_type_t") spk_type[](#_CPPv4N20aud_intf_voc_setup_t8spk_typeE "永久链接至目标")
    :   audio speaker type: uac or speaker

    [aud_adc_intf_mode_t](bk_audio.html#_CPPv419aud_adc_intf_mode_t "aud_adc_intf_mode_t") mic_mode[](#_CPPv4N20aud_intf_voc_setup_t8mic_modeE "永久链接至目标")
    :   audio mic mode: signal_ended/differen

    uint8_t frame_num[](#_CPPv4N20aud_intf_voc_setup_t9frame_numE "永久链接至目标")
    :   the max number of frames in rx buffer to save rx data, the time of one frame is 20ms

    uint8_t fifo_frame_num[](#_CPPv4N20aud_intf_voc_setup_t14fifo_frame_numE "永久链接至目标")
    :   the number of frames in rx buffer before start voice transfer, the time of one frame is 20ms


### Macros[](#macros "永久链接至标题")

BK_ERR_AUD_INTF_BASE[](#c.BK_ERR_AUD_INTF_BASE "永久链接至目标")

BK_ERR_AUD_INTF_OK[](#c.BK_ERR_AUD_INTF_OK "永久链接至目标")
:   ok

BK_ERR_AUD_INTF_FAIL[](#c.BK_ERR_AUD_INTF_FAIL "永久链接至目标")
:   fail

BK_ERR_AUD_INTF_STA[](#c.BK_ERR_AUD_INTF_STA "永久链接至目标")
:   audio interface module status is error

BK_ERR_AUD_INTF_PARAM[](#c.BK_ERR_AUD_INTF_PARAM "永久链接至目标")
:   parameter is error

BK_ERR_AUD_INTF_MEMY[](#c.BK_ERR_AUD_INTF_MEMY "永久链接至目标")
:   malloc memory fail

BK_ERR_AUD_INTF_ADC[](#c.BK_ERR_AUD_INTF_ADC "永久链接至目标")
:   config audio adc fail

BK_ERR_AUD_INTF_DAC[](#c.BK_ERR_AUD_INTF_DAC "永久链接至目标")
:   config audio dac fail

BK_ERR_AUD_INTF_DMA[](#c.BK_ERR_AUD_INTF_DMA "永久链接至目标")
:   config dma fail

BK_ERR_AUD_INTF_AEC[](#c.BK_ERR_AUD_INTF_AEC "永久链接至目标")
:   config aec fail

BK_ERR_AUD_INTF_RING_BUFF[](#c.BK_ERR_AUD_INTF_RING_BUFF "永久链接至目标")
:   config ring buffer fail

BK_ERR_AUD_INTF_TIMEOUT[](#c.BK_ERR_AUD_INTF_TIMEOUT "永久链接至目标")
:   aud_intf api excute timeout

BK_ERR_AUD_INTF_TX_MSG[](#c.BK_ERR_AUD_INTF_TX_MSG "永久链接至目标")
:   aud_intf api send message fail

BK_ERR_AUD_INTF_BUSY[](#c.BK_ERR_AUD_INTF_BUSY "永久链接至目标")
:   aud_intf is busying

BK_ERR_AUD_INTF_FILE[](#c.BK_ERR_AUD_INTF_FILE "永久链接至目标")
:   aud_intf file operate fail

BK_ERR_AUD_INTF_UAC_DRV[](#c.BK_ERR_AUD_INTF_UAC_DRV "永久链接至目标")
:   aud_intf uac driver fail

BK_ERR_AUD_INTF_UAC_MIC[](#c.BK_ERR_AUD_INTF_UAC_MIC "永久链接至目标")
:   aud_intf uac mic fail

BK_ERR_AUD_INTF_UAC_SPK[](#c.BK_ERR_AUD_INTF_UAC_SPK "永久链接至目标")
:   aud_intf uac spk operate fail

DEFAULT_AUD_INTF_DRV_SETUP_CONFIG()[](#c.DEFAULT_AUD_INTF_DRV_SETUP_CONFIG "永久链接至目标")

DEFAULT_AUD_INTF_MIC_SETUP_CONFIG()[](#c.DEFAULT_AUD_INTF_MIC_SETUP_CONFIG "永久链接至目标")

DEFAULT_AUD_INTF_SPK_SETUP_CONFIG()[](#c.DEFAULT_AUD_INTF_SPK_SETUP_CONFIG "永久链接至目标")

DEFAULT_AUD_INTF_VOC_SETUP_CONFIG()[](#c.DEFAULT_AUD_INTF_VOC_SETUP_CONFIG "永久链接至目标")


### Type Definitions[](#type-definitions "永久链接至标题")

typedef [bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") (*aud_intf_dump_data_callback)(unsigned char *data, unsigned int size)[](#_CPPv427aud_intf_dump_data_callback "永久链接至目标")


### Enumerations[](#enumerations "永久链接至标题")

enum aud_intf_uac_sta_t[](#_CPPv418aud_intf_uac_sta_t "永久链接至目标")
:   *Values:*

    enumerator AUD_INTF_UAC_CONNECTED[](#_CPPv4N18aud_intf_uac_sta_t22AUD_INTF_UAC_CONNECTEDE "永久链接至目标")
    :   Connected: uac automatically restore connection after abnormal disconnection

    enumerator AUD_INTF_UAC_NORMAL_DISCONNECTED[](#_CPPv4N18aud_intf_uac_sta_t32AUD_INTF_UAC_NORMAL_DISCONNECTEDE "永久链接至目标")
    :   Normal disconnected: uac normal disconnection

    enumerator AUD_INTF_UAC_ABNORMAL_DISCONNECTED[](#_CPPv4N18aud_intf_uac_sta_t34AUD_INTF_UAC_ABNORMAL_DISCONNECTEDE "永久链接至目标")
    :   Abnormal disconnected: uac abnormal disconnection

    enumerator AUD_INTF_UAC_CANNOT_RECOVER_CONNECT[](#_CPPv4N18aud_intf_uac_sta_t35AUD_INTF_UAC_CANNOT_RECOVER_CONNECTE "永久链接至目标")
    :   Cannot automatically connect: uac automatically connect fail

enum aud_intf_work_mode_t[](#_CPPv420aud_intf_work_mode_t "永久链接至目标")
:   *Values:*

    enumerator AUD_INTF_WORK_MODE_NULL[](#_CPPv4N20aud_intf_work_mode_t23AUD_INTF_WORK_MODE_NULLE "永久链接至目标")

    enumerator AUD_INTF_WORK_MODE_GENERAL[](#_CPPv4N20aud_intf_work_mode_t26AUD_INTF_WORK_MODE_GENERALE "永久链接至目标")
    :   General mode: support record mic data and play speaker

    enumerator AUD_INTF_WORK_MODE_VOICE[](#_CPPv4N20aud_intf_work_mode_t24AUD_INTF_WORK_MODE_VOICEE "永久链接至目标")
    :   Voice mode: support voice transfer

    enumerator AUD_INTF_WORK_MODE_MAX[](#_CPPv4N20aud_intf_work_mode_t22AUD_INTF_WORK_MODE_MAXE "永久链接至目标")

enum aud_intf_mic_chl_t[](#_CPPv418aud_intf_mic_chl_t "永久链接至目标")
:   *Values:*

    enumerator AUD_INTF_MIC_CHL_MIC1[](#_CPPv4N18aud_intf_mic_chl_t21AUD_INTF_MIC_CHL_MIC1E "永久链接至目标")
    :   MIC1: only enable mic1 channel

    enumerator AUD_INTF_MIC_CHL_DUAL[](#_CPPv4N18aud_intf_mic_chl_t21AUD_INTF_MIC_CHL_DUALE "永久链接至目标")
    :   DUAL: enable mic1 channel both and MIC2 channel

    enumerator AUD_INTF_MIC_CHL_MAX[](#_CPPv4N18aud_intf_mic_chl_t20AUD_INTF_MIC_CHL_MAXE "永久链接至目标")

enum aud_intf_mic_type_t[](#_CPPv419aud_intf_mic_type_t "永久链接至目标")
:   *Values:*

    enumerator AUD_INTF_MIC_TYPE_BOARD[](#_CPPv4N19aud_intf_mic_type_t23AUD_INTF_MIC_TYPE_BOARDE "永久链接至目标")

    enumerator AUD_INTF_MIC_TYPE_UAC[](#_CPPv4N19aud_intf_mic_type_t21AUD_INTF_MIC_TYPE_UACE "永久链接至目标")

    enumerator AUD_INTF_MIC_TYPE_MAX[](#_CPPv4N19aud_intf_mic_type_t21AUD_INTF_MIC_TYPE_MAXE "永久链接至目标")

enum aud_intf_spk_chl_t[](#_CPPv418aud_intf_spk_chl_t "永久链接至目标")
:   *Values:*

    enumerator AUD_INTF_SPK_CHL_LEFT[](#_CPPv4N18aud_intf_spk_chl_t21AUD_INTF_SPK_CHL_LEFTE "永久链接至目标")
    :   LEFT: only enable SPK left channel

    enumerator AUD_INTF_SPK_CHL_DUAL[](#_CPPv4N18aud_intf_spk_chl_t21AUD_INTF_SPK_CHL_DUALE "永久链接至目标")
    :   DUAL: enable SPK left and right channel

    enumerator AUD_INTF_SPK_CHL_MAX[](#_CPPv4N18aud_intf_spk_chl_t20AUD_INTF_SPK_CHL_MAXE "永久链接至目标")

enum aud_intf_spk_type_t[](#_CPPv419aud_intf_spk_type_t "永久链接至目标")
:   *Values:*

    enumerator AUD_INTF_SPK_TYPE_BOARD[](#_CPPv4N19aud_intf_spk_type_t23AUD_INTF_SPK_TYPE_BOARDE "永久链接至目标")

    enumerator AUD_INTF_SPK_TYPE_UAC[](#_CPPv4N19aud_intf_spk_type_t21AUD_INTF_SPK_TYPE_UACE "永久链接至目标")

    enumerator AUD_INTF_SPK_TYPE_MAX[](#_CPPv4N19aud_intf_spk_type_t21AUD_INTF_SPK_TYPE_MAXE "永久链接至目标")

enum aud_intf_voc_samp_rate_t[](#_CPPv424aud_intf_voc_samp_rate_t "永久链接至目标")
:   *Values:*

    enumerator AUD_INTF_VOC_SAMP_RATE_8K[](#_CPPv4N24aud_intf_voc_samp_rate_t25AUD_INTF_VOC_SAMP_RATE_8KE "永久链接至目标")

    enumerator AUD_INTF_VOC_SAMP_RATE_16K[](#_CPPv4N24aud_intf_voc_samp_rate_t26AUD_INTF_VOC_SAMP_RATE_16KE "永久链接至目标")

    enumerator AUD_INTF_VOC_SAMP_RATE_MAX[](#_CPPv4N24aud_intf_voc_samp_rate_t26AUD_INTF_VOC_SAMP_RATE_MAXE "永久链接至目标")

enum aud_intf_voc_data_type_t[](#_CPPv424aud_intf_voc_data_type_t "永久链接至目标")
:   *Values:*

    enumerator AUD_INTF_VOC_DATA_TYPE_G711A[](#_CPPv4N24aud_intf_voc_data_type_t28AUD_INTF_VOC_DATA_TYPE_G711AE "永久链接至目标")
    :   the data of voice transfer encoded by G711A

    enumerator AUD_INTF_VOC_DATA_TYPE_PCM[](#_CPPv4N24aud_intf_voc_data_type_t26AUD_INTF_VOC_DATA_TYPE_PCME "永久链接至目标")
    :   the data of voice transfer is PCM

    enumerator AUD_INTF_VOC_DATA_TYPE_G711U[](#_CPPv4N24aud_intf_voc_data_type_t28AUD_INTF_VOC_DATA_TYPE_G711UE "永久链接至目标")
    :   the data of voice transfer encoded by G711U

    enumerator AUD_INTF_VOC_DATA_TYPE_MAX[](#_CPPv4N24aud_intf_voc_data_type_t26AUD_INTF_VOC_DATA_TYPE_MAXE "永久链接至目标")

enum aud_intf_voc_aec_para_t[](#_CPPv423aud_intf_voc_aec_para_t "永久链接至目标")
:   *Values:*

    enumerator AUD_INTF_VOC_AEC_NULL[](#_CPPv4N23aud_intf_voc_aec_para_t21AUD_INTF_VOC_AEC_NULLE "永久链接至目标")

    enumerator AUD_INTF_VOC_AEC_INIT_FLAG[](#_CPPv4N23aud_intf_voc_aec_para_t26AUD_INTF_VOC_AEC_INIT_FLAGE "永久链接至目标")
    :   init flag, aec module feature enable

    enumerator AUD_INTF_VOC_AEC_MIC_DELAY[](#_CPPv4N23aud_intf_voc_aec_para_t26AUD_INTF_VOC_AEC_MIC_DELAYE "永久链接至目标")
    :   mic_delay

    enumerator AUD_INTF_VOC_AEC_EC_DEPTH[](#_CPPv4N23aud_intf_voc_aec_para_t25AUD_INTF_VOC_AEC_EC_DEPTHE "永久链接至目标")
    :   ec_depth

    enumerator AUD_INTF_VOC_AEC_REF_SCALE[](#_CPPv4N23aud_intf_voc_aec_para_t26AUD_INTF_VOC_AEC_REF_SCALEE "永久链接至目标")
    :   ref_scale: 0/1/2

    enumerator AUD_INTF_VOC_AEC_VOICE_VOL[](#_CPPv4N23aud_intf_voc_aec_para_t26AUD_INTF_VOC_AEC_VOICE_VOLE "永久链接至目标")
    :   voice volume level

    enumerator AUD_INTF_VOC_AEC_TXRX_THR[](#_CPPv4N23aud_intf_voc_aec_para_t25AUD_INTF_VOC_AEC_TXRX_THRE "永久链接至目标")
    :   max amplitude of rx audio data

    enumerator AUD_INTF_VOC_AEC_TXRX_FLR[](#_CPPv4N23aud_intf_voc_aec_para_t25AUD_INTF_VOC_AEC_TXRX_FLRE "永久链接至目标")
    :   min amplitude of rx audio data

    enumerator AUD_INTF_VOC_AEC_NS_LEVEL[](#_CPPv4N23aud_intf_voc_aec_para_t25AUD_INTF_VOC_AEC_NS_LEVELE "永久链接至目标")
    :   noise level: 0/1/2

    enumerator AUD_INTF_VOC_AEC_NS_PARA[](#_CPPv4N23aud_intf_voc_aec_para_t24AUD_INTF_VOC_AEC_NS_PARAE "永久链接至目标")
    :   noise value, range:1~8

    enumerator AUD_INTF_VOC_AEC_DRC[](#_CPPv4N23aud_intf_voc_aec_para_t20AUD_INTF_VOC_AEC_DRCE "永久链接至目标")
    :   voice volume value, range:0x10~0x1f

    enumerator AUD_INTF_VOC_AEC_MAX[](#_CPPv4N23aud_intf_voc_aec_para_t20AUD_INTF_VOC_AEC_MAXE "永久链接至目标")

enum aud_intf_voc_mic_ctrl_t[](#_CPPv423aud_intf_voc_mic_ctrl_t "永久链接至目标")
:   *Values:*

    enumerator AUD_INTF_VOC_MIC_OPEN[](#_CPPv4N23aud_intf_voc_mic_ctrl_t21AUD_INTF_VOC_MIC_OPENE "永久链接至目标")
    :   open mic

    enumerator AUD_INTF_VOC_MIC_CLOSE[](#_CPPv4N23aud_intf_voc_mic_ctrl_t22AUD_INTF_VOC_MIC_CLOSEE "永久链接至目标")
    :   close spk

    enumerator AUD_INTF_VOC_MIC_MAX[](#_CPPv4N23aud_intf_voc_mic_ctrl_t20AUD_INTF_VOC_MIC_MAXE "永久链接至目标")

enum aud_intf_voc_spk_ctrl_t[](#_CPPv423aud_intf_voc_spk_ctrl_t "永久链接至目标")
:   *Values:*

    enumerator AUD_INTF_VOC_SPK_OPEN[](#_CPPv4N23aud_intf_voc_spk_ctrl_t21AUD_INTF_VOC_SPK_OPENE "永久链接至目标")
    :   open spk

    enumerator AUD_INTF_VOC_SPK_CLOSE[](#_CPPv4N23aud_intf_voc_spk_ctrl_t22AUD_INTF_VOC_SPK_CLOSEE "永久链接至目标")
    :   close spk

    enumerator AUD_INTF_VOC_SPK_MAX[](#_CPPv4N23aud_intf_voc_spk_ctrl_t20AUD_INTF_VOC_SPK_MAXE "永久链接至目标")
