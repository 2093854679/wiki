---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/api-reference/multi_media/bk_aud_intf.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="aud-intf-apis"></a>

# Aud\_Intf APIs

重要

The Aud\_Intf API v1.0 is the lastest and stable Audio interface APIs. All new applications should use Audio interface API v1.0.

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
:   - `bk_aud_intf_drv_init()` \- init the audio interface driver
    - `bk_aud_intf_drv_deinit()` \- deinit the audio interface driver
    - `bk_aud_intf_set_mode()` \- set audio interface work mode
    - `bk_aud_intf_set_mic_gain()` \- set audio mic gain
    - `bk_aud_intf_set_spk_gain()` \- set audio speaker gain
    - `bk_aud_intf_write_spk_data()` \- write data to sperker

Mic APIs:
:   - `bk_aud_intf_mic_init()` \- init the mic function
    - `bk_aud_intf_mic_deinit()` \- deinit the mic function
    - `bk_aud_intf_mic_start()` \- start mic work
    - `bk_aud_intf_mic_pause()` \- pause mic work
    - `bk_aud_intf_mic_stop()` \- stop mic work
    - `bk_aud_intf_set_mic_chl()` \- set mic channel in work
    - `bk_aud_intf_get_mic_chl()` \- get mic channel in work
    - `bk_aud_intf_set_mic_samp_rate()` \- set mic sample rate
    - `bk_aud_intf_get_mic_samp_rate()` \- get mic sample rate

Spk APIs:
:   - `bk_aud_intf_spk_init()` \- init the speaker function
    - `bk_aud_intf_spk_deinit()` \- deinit the speaker function
    - `bk_aud_intf_spk_start()` \- start speaker work
    - `bk_aud_intf_spk_pause()` \- pause speaker work
    - `bk_aud_intf_spk_stop()` \- stop speaker work
    - `bk_aud_intf_set_spk_chl()` \- set speaker channel in work
    - `bk_aud_intf_get_spk_chl()` \- get speaker channel in work
    - `bk_aud_intf_set_spk_samp_rate()` \- set speaker sample rate
    - `bk_aud_intf_get_spk_samp_rate()` \- get speaker sample rate

Voc APIs:
:   - `bk_aud_intf_voc_init()` \- init the voice transfer function
    - `bk_aud_intf_voc_deinit()` \- deinit the voice transfer function
    - `bk_aud_intf_voc_start()` \- start voice transfer
    - `bk_aud_intf_voc_stop()` \- stop voice transfer
    - `bk_aud_intf_set_aec_para()` \- set aec parameter
    - `bk_aud_intf_get_aec_para()` \- get aec parameter
    - `bk_aud_intf_voc_tx_debug()` \- register voice tx debug callback
    - `bk_aud_intf_voc_rx_debug()` \- register voice rx debug callback
    - `bk_aud_intf_voc_aec_debug()` \- register voice aec debug callback

<a id="api-reference"></a>

## API Reference

#.. include:: ../../\_build/inc/aud\_intf.inc

<a id="api-typedefs"></a>

## API Typedefs

#.. include:: ../../\_build/inc/aud\_intf\_types.inc
