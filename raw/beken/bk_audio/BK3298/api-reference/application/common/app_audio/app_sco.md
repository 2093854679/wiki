---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_audio/app_sco.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="sco-application-functions"></a>

# SCO Application Functions

<a id="app-sco-api-brief"></a>

## APP\_SCO API Brief

| Application | Brief |
| --- | --- |
| [`app_sco_codec_init()`](#_CPPv418app_sco_codec_init8uint32_t7uint8_t "app_sco_codec_init") | initialize the voice relevant settings |
| [`app_sco_codec_deinit()`](#_CPPv420app_sco_codec_deinitv "app_sco_codec_deinit") | deinitialize the voice relevant settings |
| [`app_sco_data_process()`](#_CPPv420app_sco_data_processv "app_sco_data_process") | application for handling SCO data |
| [`app_sco_get_trigger_time()`](#_CPPv424app_sco_get_trigger_timev "app_sco_get_trigger_time") | get trigger time struct for start handing SCO data |

<a id="app-sco-api-reference"></a>

## APP\_SCO API Reference

<a id="header-file"></a>

### Header File

- [common/app\_audio/app\_sco.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_audio/app_sco.h)

<a id="functions"></a>

### Functions

<a id="_CPPv418app_sco_codec_init8uint32_t7uint8_t"></a>

<a id="_CPPv318app_sco_codec_init8uint32_t7uint8_t"></a> <a id="_CPPv218app_sco_codec_init8uint32_t7uint8_t"></a> <a id="app_sco_codec_init__uint32_t.uint8_t"></a> <a id="app__sco_8h_1a33bbe341503b246b110ae7d160718311"></a> void app\_sco\_codec\_init(uint32\_t codec\_type, uint8\_t vol)
:   initialize the voice relevant settings

    initialize audio module and set voice relevant data

    参数:
    :   - **codec\_type** – **\[in\]** codec Index @btif\_sco\_codec\_t
        - **vol** – **\[in\]** volume of voice

    返回:
    :   N/A

<a id="_CPPv420app_sco_codec_deinitv"></a>

<a id="_CPPv320app_sco_codec_deinitv"></a> <a id="_CPPv220app_sco_codec_deinitv"></a> <a id="app_sco_codec_deinit__void"></a> <a id="app__sco_8h_1a22206c1e41c5a134ede0a80619a63022"></a> void app\_sco\_codec\_deinit(void)
:   deinitialize the voice relevant settings

    reset audio module and free voice relevant settings

    返回:
    :   N/A

<a id="_CPPv420app_sco_data_processv"></a>

<a id="_CPPv320app_sco_data_processv"></a> <a id="_CPPv220app_sco_data_processv"></a> <a id="app_sco_data_process__void"></a> <a id="app__sco_8h_1abaacd31994913195ba9c1c8e1522885c"></a> uint32\_t app\_sco\_data\_process(void)
:   application for handling SCO data

    get data from ADC buff and encode to SCO data. After that, decode SCO data and put into DAC buff

    返回值:
    :   **0** – always 0

    返回:
    :   result

<a id="_CPPv424app_sco_get_trigger_timev"></a>

<a id="_CPPv324app_sco_get_trigger_timev"></a> <a id="_CPPv224app_sco_get_trigger_timev"></a> <a id="app_sco_get_trigger_time__void"></a> <a id="app__sco_8h_1a6f992c471239077d27dd52c464d97453"></a> bt\_clk\_t \*app\_sco\_get\_trigger\_time(void)
:   get trigger time struct for start handing SCO data

    return the BT time clock struct which start encode/decode SCO data

    返回:
    :   BT clock

<a id="macros"></a>

### Macros

<a id="c.APP_SCO_MSBC_FRAME_BUFFER_SIZE"></a>

<a id="app__sco_8h_1a9d620e02e36e82caf3547b49fa68ae65"></a> APP\_SCO\_MSBC\_FRAME\_BUFFER\_SIZE
:   Encoded buffer size in bytes per mSBC frame

<a id="c.APP_SCO_MSBC_SAMPLES_PER_FRAME"></a>

<a id="app__sco_8h_1a99cd77b283edcee9a27ac7de4d356bcd"></a> APP\_SCO\_MSBC\_SAMPLES\_PER\_FRAME
:   Encoded samples (mono) per mSBC frame

<a id="c.APP_SCO_CVSD_FRAME_BUFFER_SIZE"></a>

<a id="app__sco_8h_1a3be1bdb5267d32a22c329bac86c86f42"></a> APP\_SCO\_CVSD\_FRAME\_BUFFER\_SIZE
:   Raw buffer size in bytes per CVSD frame

<a id="c.APP_SCO_CVSD_SAMPLES_PER_FRAME"></a>

<a id="app__sco_8h_1a8d194708eea80cdadb927ef98b6c4d07"></a> APP\_SCO\_CVSD\_SAMPLES\_PER\_FRAME
:   Encoded samples (mono) per CVSD frame

<a id="c.PLC_CVSD_FS"></a>

<a id="app__sco_8h_1a46e68db5dbd8904536d5cf130d95916c"></a> PLC\_CVSD\_FS
:   CVSD Frame Size in samples

<a id="c.PLC_CVSD_N"></a>

<a id="app__sco_8h_1acabef9442ee3810cda50ac5379ffea74"></a> PLC\_CVSD\_N
:   CVSD Window Length in samples for pattern matching

<a id="c.PLC_CVSD_M"></a>

<a id="app__sco_8h_1a0b40964c8b18a13d02f812868d5e69f2"></a> PLC\_CVSD\_M
:   CVSD Template samples for matching

<a id="c.PLC_CVSD_LHIST"></a>

<a id="app__sco_8h_1ad7055b1ff1e5729f5602cb569292d62b"></a> PLC\_CVSD\_LHIST
:   CVSD Length of history buffer required in samples

<a id="c.PLC_CVSD_RT"></a>

<a id="app__sco_8h_1a73f137a5e34dae61290214187afb76dc"></a> PLC\_CVSD\_RT
:   CVSD Reconvergence Time in samples

<a id="c.PLC_CVSD_OLAL"></a>

<a id="app__sco_8h_1ad7b6aa6ecc29ad292e64c98adc52fb22"></a> PLC\_CVSD\_OLAL
:   CVSD OverLap-Add Length in samples

<a id="c.PLC_MSBC_FS"></a>

<a id="app__sco_8h_1a3010c981ca093209333b651c0709b5c8"></a> PLC\_MSBC\_FS
:   MSBC Frame Size in samples

<a id="c.PLC_MSBC_N"></a>

<a id="app__sco_8h_1a48218213cda94db82552f67682874f81"></a> PLC\_MSBC\_N
:   MSBC Window Length in samples for pattern matching

<a id="c.PLC_MSBC_M"></a>

<a id="app__sco_8h_1a4dd121a7e4e7ef161c7cf289f57450ed"></a> PLC\_MSBC\_M
:   MSBC Template samples for matching

<a id="c.PLC_MSBC_LHIST"></a>

<a id="app__sco_8h_1abd8f8ffb50a158707c8a441437139fec"></a> PLC\_MSBC\_LHIST
:   MSBC Length of history buffer required in samples

<a id="c.PLC_MSBC_RT"></a>

<a id="app__sco_8h_1ab2d07d6cb39734b1eb308181d00850ac"></a> PLC\_MSBC\_RT
:   MSBC Reconvergence Time in samples

<a id="c.PLC_MSBC_OLAL"></a>

<a id="app__sco_8h_1a641b7e0cdf6c5f8355e305f92a6cdbb6"></a> PLC\_MSBC\_OLAL
:   MSBC OverLap-Add Length in samples

<a id="c.PLC_VAD_DET_TH"></a>

<a id="app__sco_8h_1a21e94f320cfb81b2cd85dab2539a7539"></a> PLC\_VAD\_DET\_TH
:   PLC VAD detection threshold value
