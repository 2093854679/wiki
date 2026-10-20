---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/api-reference/multi_media/bk_audio.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
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
:   - `bk_aud_driver_init()` \- init the audio driver
    - `bk_aud_driver_deinit()` \- deinit the audio driver
    - `bk_aud_register_aud_isr()` \- register audio isr

Adc APIs:
:   - `bk_aud_adc_init()` \- init the adc module of audio
    - `bk_aud_adc_deinit()` \- deinit the adc module of audio
    - `bk_aud_set_adc_samp_rate()` \- set the sample rate in adc work mode
    - `bk_aud_get_adc_fifo_addr()` \- get the adc fifo address in adc work mode
    - `bk_aud_get_dtmf_fifo_addr()` \- get the dtmf fifo address in adc work mode
    - `bk_aud_get_adc_status()` \- get the adc status information in adc work mode
    - `bk_aud_get_dtmf_status()` \- get the dtmf status information in dtmf work mode
    - `bk_aud_enable_adc_int()` \- enable adc interrupt
    - `bk_aud_disable_adc_int()` \- disable adc interrupt
    - `bk_aud_start_adc()` \- start adc function
    - `bk_aud_stop_adc()` \- stop adc function
    - `bk_aud_get_adc_fifo_data()` \- get adc data
    - `bk_aud_get_dtmf_fifo_data()` \- get dtmf data

Dac APIs:
:   - `bk_aud_dac_init()` \- init the dac module of audio
    - `bk_aud_dac_deinit()` \- deinit the dac module of audio
    - `bk_aud_set_dac_samp_rate()` \- set the sample rate of audio dac function
    - `bk_aud_get_dac_fifo_addr()` \- get the dac fifo address
    - `bk_aud_enable_dac_int()` \- enable dac interrupt function
    - `bk_aud_disable_dac_int()` \- disable dac interrupt function
    - `bk_aud_get_dac_status()` \- get the dac fifo status information
    - `bk_aud_start_dac()` \- start dac function
    - `bk_aud_stop_dac()` \- stop dac function

Eq APIs:
:   - `bk_aud_eq_init()` \- init the eq module of audio
    - `bk_aud_eq_deinit()` \- deinit the eq module of audio

<a id="api-reference"></a>

## API Reference

#.. include:: ../../\_build/inc/aud.inc

<a id="api-typedefs"></a>

## API Typedefs

#.. include:: ../../\_build/inc/aud\_types.inc
