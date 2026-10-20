---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_audio/app_lc3.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="lc3-application-functions"></a>

# LC3 Application Functions

<a id="app-lc3-api-brief"></a>

## APP\_LC3 API Brief

| Application | Brief |
| --- | --- |
| [`app_audio_lc3_init()`](#_CPPv418app_audio_lc3_initv "app_audio_lc3_init") | initialize the LC3 codec relevant settings |
| [`app_audio_lc3_downlink_stream_init()`](#_CPPv434app_audio_lc3_downlink_stream_initP26le_audio_lc3_stream_info_t7uint8_t "app_audio_lc3_downlink_stream_init") | initialize the downlink stream settings |
| [`app_audio_lc3_downlink_stream_buffering()`](#_CPPv439app_audio_lc3_downlink_stream_bufferingP7uint8_t8uint32_t8uint32_t "app_audio_lc3_downlink_stream_buffering") | push LC3 downlink stream data into queue |
| [`app_audio_lc3_downlink_stream_deinit()`](#_CPPv436app_audio_lc3_downlink_stream_deinit8uint16_t "app_audio_lc3_downlink_stream_deinit") | deinitialize the downlink stream settings |
| [`app_audio_lc3_set_dec_start()`](#_CPPv427app_audio_lc3_set_dec_startb "app_audio_lc3_set_dec_start") | update LC3 decoder environment member value |
| [`app_audio_lc3_rx_downlink_data()`](#_CPPv430app_audio_lc3_rx_downlink_dataP21le_audio_lc3_stream_t "app_audio_lc3_rx_downlink_data") | handle LC3 downlink stream data |
| [`app_audio_lc3_uplink_stream_init()`](#_CPPv432app_audio_lc3_uplink_stream_initP26le_audio_lc3_stream_info_t "app_audio_lc3_uplink_stream_init") | initialize the uplink stream settings |
| [`app_audio_lc3_uplink_stream_deinit()`](#_CPPv434app_audio_lc3_uplink_stream_deinit8uint16_t "app_audio_lc3_uplink_stream_deinit") | deinitialize the uplink stream settings |

<a id="app-lc3-api-reference"></a>

## APP\_LC3 API Reference

<a id="header-file"></a>

### Header File

- [common/app\_audio/app\_lc3.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_audio/app_lc3.h)

<a id="functions"></a>

### Functions

<a id="_CPPv418app_audio_lc3_initv"></a>

<a id="_CPPv318app_audio_lc3_initv"></a> <a id="_CPPv218app_audio_lc3_initv"></a> <a id="app_audio_lc3_init__void"></a> <a id="app__lc3_8h_1ac608b479fff4e872535184cb60bf18df"></a> void app\_audio\_lc3\_init(void)
:   initialize the LC3 codec relevant settings

    set codec to LC3 and initialize audio environment settings

    返回:
    :   N/A

<a id="_CPPv434app_audio_lc3_downlink_stream_initP26le_audio_lc3_stream_info_t7uint8_t"></a>

<a id="_CPPv334app_audio_lc3_downlink_stream_initP26le_audio_lc3_stream_info_t7uint8_t"></a> <a id="_CPPv234app_audio_lc3_downlink_stream_initP26le_audio_lc3_stream_info_t7uint8_t"></a> <a id="app_audio_lc3_downlink_stream_init__le_audio_lc3_stream_info_tP.uint8_t"></a> <a id="app__lc3_8h_1a6b18c362fcd4f395321cf07ab4e5b746"></a> void app\_audio\_lc3\_downlink\_stream\_init(le\_audio\_lc3\_stream\_info\_t \*p\_lc3\_stream\_info, uint8\_t vol)
:   initialize the downlink stream settings

    set LC3 decoder relevant parameters and initialize LC3 decoder

    参数:
    :   - **p\_lc3\_stream\_info** – **\[in\]** stream information strcut @le\_audio\_lc3\_stream\_info\_t
        - **vol** – **\[in\]** stream volume information

    返回:
    :   N/A

<a id="_CPPv439app_audio_lc3_downlink_stream_bufferingP7uint8_t8uint32_t8uint32_t"></a>

<a id="_CPPv339app_audio_lc3_downlink_stream_bufferingP7uint8_t8uint32_t8uint32_t"></a> <a id="_CPPv239app_audio_lc3_downlink_stream_bufferingP7uint8_t8uint32_t8uint32_t"></a> <a id="app_audio_lc3_downlink_stream_buffering__uint8_tP.uint32_t.uint32_t"></a> <a id="app__lc3_8h_1ace2f41c5d40e7645330110ac4280c672"></a> void app\_audio\_lc3\_downlink\_stream\_buffering(uint8\_t \*p\_data, uint32\_t dlen, uint32\_t seq)
:   push LC3 downlink stream data into queue

    make a copy of LC3 downlink stream data, push it into decoder queue

    参数:
    :   - **p\_data** – **\[in\]** pointer to LC3 downlink stream data
        - **dlen** – **\[in\]** data length
        - **seq** – **\[in\]** sequential number

    返回:
    :   N/A

<a id="_CPPv436app_audio_lc3_downlink_stream_deinit8uint16_t"></a>

<a id="_CPPv336app_audio_lc3_downlink_stream_deinit8uint16_t"></a> <a id="_CPPv236app_audio_lc3_downlink_stream_deinit8uint16_t"></a> <a id="app_audio_lc3_downlink_stream_deinit__uint16_t"></a> <a id="app__lc3_8h_1acb08a5f28e8451d63d2f5e53ae90223a"></a> void app\_audio\_lc3\_downlink\_stream\_deinit(uint16\_t iso\_handle)
:   deinitialize the downlink stream settings

    reset audio environment settings and free LC3 decoder relevant parameters

    参数:
    :   **iso\_handle** – **\[in\]** ISO handle index

    返回:
    :   N/A

<a id="_CPPv427app_audio_lc3_set_dec_startb"></a>

<a id="_CPPv327app_audio_lc3_set_dec_startb"></a> <a id="_CPPv227app_audio_lc3_set_dec_startb"></a> <a id="app_audio_lc3_set_dec_start__b"></a> <a id="app__lc3_8h_1a3b33bdb5f9b130d2f74a0f80dd0c84ea"></a> void app\_audio\_lc3\_set\_dec\_start(bool start)
:   update LC3 decoder environment member value

    update LC3 decoder environment member value, need set it start before receive downlink stream data

    参数:
    :   **start** – **\[in\]** boolean value for start or not

    返回:
    :   N/A

<a id="_CPPv430app_audio_lc3_rx_downlink_dataP21le_audio_lc3_stream_t"></a>

<a id="_CPPv330app_audio_lc3_rx_downlink_dataP21le_audio_lc3_stream_t"></a> <a id="_CPPv230app_audio_lc3_rx_downlink_dataP21le_audio_lc3_stream_t"></a> <a id="app_audio_lc3_rx_downlink_data__le_audio_lc3_stream_tP"></a> <a id="app__lc3_8h_1a841967d6e7168cd93ec15509634655af"></a> void app\_audio\_lc3\_rx\_downlink\_data(le\_audio\_lc3\_stream\_t \*p\_lc3\_stream)
:   handle LC3 downlink stream data

    push data into queue by using @app\_audio\_lc3\_downlink\_stream\_buffering and start decode when queue buffer size large than threshold

    参数:
    :   **p\_lc3\_stream** – **\[in\]** LC3 downlink stream data send by lower layer

    返回:
    :   N/A

<a id="_CPPv432app_audio_lc3_uplink_stream_initP26le_audio_lc3_stream_info_t"></a>

<a id="_CPPv332app_audio_lc3_uplink_stream_initP26le_audio_lc3_stream_info_t"></a> <a id="_CPPv232app_audio_lc3_uplink_stream_initP26le_audio_lc3_stream_info_t"></a> <a id="app_audio_lc3_uplink_stream_init__le_audio_lc3_stream_info_tP"></a> <a id="app__lc3_8h_1ade60f78ee95bac3cfe92570f494a9b25"></a> void app\_audio\_lc3\_uplink\_stream\_init(le\_audio\_lc3\_stream\_info\_t \*p\_lc3\_stream\_info)
:   initialize the uplink stream settings

    set LC3 encoder relevant parameters and initialize LC3 encoder

    参数:
    :   **p\_lc3\_stream\_info** – **\[in\]** stream information strcut @le\_audio\_lc3\_stream\_info\_t

    返回:
    :   N/A

<a id="_CPPv434app_audio_lc3_uplink_stream_deinit8uint16_t"></a>

<a id="_CPPv334app_audio_lc3_uplink_stream_deinit8uint16_t"></a> <a id="_CPPv234app_audio_lc3_uplink_stream_deinit8uint16_t"></a> <a id="app_audio_lc3_uplink_stream_deinit__uint16_t"></a> <a id="app__lc3_8h_1abc27e3a12bc741cf680e7c72784c00a3"></a> void app\_audio\_lc3\_uplink\_stream\_deinit(uint16\_t iso\_handle)
:   deinitialize the uplink stream settings

    reset audio environment settings and free LC3 encoder relevant parameters

    参数:
    :   **iso\_handle** – **\[in\]** ISO handle index

    返回:
    :   N/A
