---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_audio/app_a2dp.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="a2dp-application-functions"></a>

# A2DP Application Functions

<a id="app-a2dp-api-brief"></a>

## APP\_A2DP API Brief

| Application | Brief |
| --- | --- |
| [`app_a2dp_dac_fill_music_buffer_start()`](#_CPPv436app_a2dp_dac_fill_music_buffer_startb "app_a2dp_dac_fill_music_buffer_start") | application for setting stream data fill buffer address |
| [`app_a2dp_stream_codec_deinit()`](#_CPPv428app_a2dp_stream_codec_deinitv "app_a2dp_stream_codec_deinit") | stream codec close and the other related variables reset |
| [`app_a2dp_reset_playback_buffer()`](#_CPPv430app_a2dp_reset_playback_buffer8uint32_t "app_a2dp_reset_playback_buffer") | application for reset ring buffer and related variables |
| [`app_a2dp_stream_codec_init()`](#_CPPv426app_a2dp_stream_codec_init8uint32_t8uint32_t8uint32_t8uint16_t7uint8_t "app_a2dp_stream_codec_init") | application for stream codec initialize |
| [`app_a2dp_stream_process()`](#_CPPv423app_a2dp_stream_process20audio_trigger_type_t "app_a2dp_stream_process") | application for stream data process |
| [`app_a2dp_get_samples_per_frame()`](#_CPPv430app_a2dp_get_samples_per_framev "app_a2dp_get_samples_per_frame") | application to get samples of per frame |
| [`app_a2dp_get_music_sample_rate()`](#_CPPv430app_a2dp_get_music_sample_ratev "app_a2dp_get_music_sample_rate") | application to get samples rate |
| [`app_a2dp_get_samples_per_packet()`](#_CPPv431app_a2dp_get_samples_per_packetv "app_a2dp_get_samples_per_packet") | application to get samples of per packet |
| [`app_a2dp_get_frames_per_packet()`](#_CPPv430app_a2dp_get_frames_per_packetv "app_a2dp_get_frames_per_packet") | application to get frames of per packet |
| [`app_a2dp_get_filled_frame()`](#_CPPv425app_a2dp_get_filled_framev "app_a2dp_get_filled_frame") | application to get filled number of nodes in ring buffer |
| [`app_a2dp_stream_codec_deinit()`](#_CPPv428app_a2dp_stream_codec_deinitv "app_a2dp_stream_codec_deinit") | stream codec close and the other related variables reset |
| [`app_a2dp_dac_get_free_music_buffer_size()`](#_CPPv439app_a2dp_dac_get_free_music_buffer_sizev "app_a2dp_dac_get_free_music_buffer_size") | application to get filled number of nodes in ring buffer |
| [`app_a2dp_dac_get_fill_music_buffer_size()`](#_CPPv439app_a2dp_dac_get_fill_music_buffer_sizev "app_a2dp_dac_get_fill_music_buffer_size") | application to get size of filled data from dac dma buffer |
| [`app_a2dp_fill_stream_buffering()`](#_CPPv430app_a2dp_fill_stream_buffering8uint32_tP7uint8_t8uint32_t8uint32_t8uint32_t7uint8_t "app_a2dp_fill_stream_buffering") | application to fill stream data to ring buffer |
| [`app_a2dp_init_decode_seq()`](#_CPPv424app_a2dp_init_decode_seq8uint32_t8uint32_t "app_a2dp_init_decode_seq") | application to set packet sequence number and frame sequence number |
| [`app_a2dp_get_last_seq()`](#_CPPv421app_a2dp_get_last_seqv "app_a2dp_get_last_seq") | application to get last filled in p\_audio\_env-\>audio\_a2dp\_frame\_nodes ring buffer sequence number |
| [`app_a2dp_async_get_frame_seq()`](#_CPPv428app_a2dp_async_get_frame_seqv "app_a2dp_async_get_frame_seq") | application to get start frame sequence number from app\_a2dp\_audio\_ctrl |
| [`app_a2dp_resync_is_ongoing()`](#_CPPv426app_a2dp_resync_is_ongoingv "app_a2dp_resync_is_ongoing") | application to get resync status |
| [`app_a2dp_resync_get_tws_resync()`](#_CPPv430app_a2dp_resync_get_tws_resyncv "app_a2dp_resync_get_tws_resync") | application to get local currently tws link exist or not status |
| [`app_a2dp_resync_is_tws_resync()`](#_CPPv429app_a2dp_resync_is_tws_resyncv "app_a2dp_resync_is_tws_resync") | application to get from app\_a2dp\_audio\_ctrl.async\_ctrl.tws\_resync |
| [`app_a2dp_rx_stream_data()`](#_CPPv423app_a2dp_rx_stream_dataPK7uint8_t8uint16_t8uint32_t8uint32_t7uint8_t "app_a2dp_rx_stream_data") | application to received a2dp stream data |

<a id="app-a2dp-api-reference"></a>

## APP\_A2DP API Reference

<a id="header-file"></a>

### Header File

- [common/app\_audio/app\_a2dp.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_audio/app_a2dp.h)

<a id="functions"></a>

### Functions

<a id="_CPPv436app_a2dp_dac_fill_music_buffer_startb"></a>

<a id="_CPPv336app_a2dp_dac_fill_music_buffer_startb"></a> <a id="_CPPv236app_a2dp_dac_fill_music_buffer_startb"></a> <a id="app_a2dp_dac_fill_music_buffer_start__b"></a> <a id="app__a2dp_8h_1acda24d7d12b6cfc5084cb7cc20768a92"></a> void app\_a2dp\_dac\_fill\_music\_buffer\_start(bool from\_start)
:   application for setting stream data fill buffer address

    参数:
    :   **from\_start** – **\[in\]** true is copy audio\_dac\_music\_rb start address to audio\_dac\_music\_rb false is copy audio\_dac\_music\_rb middle address of audio\_dac\_music\_rb

    返回:
    :   N/A

<a id="_CPPv428app_a2dp_stream_codec_deinitv"></a>

<a id="_CPPv328app_a2dp_stream_codec_deinitv"></a> <a id="_CPPv228app_a2dp_stream_codec_deinitv"></a> <a id="app_a2dp_stream_codec_deinit__void"></a> <a id="app__a2dp_8h_1a120304ac46d7897af02a00cd5a9cbc40"></a> void app\_a2dp\_stream\_codec\_deinit(void)
:   stream codec close and the other related variables reset

    返回:
    :   N/A

<a id="_CPPv430app_a2dp_reset_playback_buffer8uint32_t"></a>

<a id="_CPPv330app_a2dp_reset_playback_buffer8uint32_t"></a> <a id="_CPPv230app_a2dp_reset_playback_buffer8uint32_t"></a> <a id="app_a2dp_reset_playback_buffer__uint32_t"></a> <a id="app__a2dp_8h_1a11e86b172613ef35996919c92f757d1d"></a> void app\_a2dp\_reset\_playback\_buffer(uint32\_t codec\_type)
:   application for reset ring buffer and related variables

    参数:
    :   **codec\_type** – **\[in\]** codec type,[btif\_a2dp\_codec\_type\_t](../../../btif/btif_type.md#btif__type_8h_1a77726b9d0e30f3bb4ccb4949be12f401)

    返回:
    :   N/A

<a id="_CPPv426app_a2dp_stream_codec_init8uint32_t8uint32_t8uint32_t8uint16_t7uint8_t"></a>

<a id="_CPPv326app_a2dp_stream_codec_init8uint32_t8uint32_t8uint32_t8uint16_t7uint8_t"></a> <a id="_CPPv226app_a2dp_stream_codec_init8uint32_t8uint32_t8uint32_t8uint16_t7uint8_t"></a> <a id="app_a2dp_stream_codec_init__uint32_t.uint32_t.uint32_t.uint16_t.uint8_t"></a> <a id="app__a2dp_8h_1a7d2dfa132e4cf8df5e7ab1897c839951"></a> void app\_a2dp\_stream\_codec\_init(uint32\_t codec\_type, uint32\_t sample\_rate, uint32\_t channels, uint16\_t frame\_cnt\_per\_pkt, uint8\_t vol)
:   application for stream codec initialize

    include app\_audio\_init,app\_audio\_dac\_open,ring\_buffer\_node\_init,bt\_a2dp\_aac\_decoder\_init

    参数:
    :   - **codec\_type** – **\[in\]** codec type,[btif\_a2dp\_codec\_type\_t](../../../btif/btif_type.md#btif__type_8h_1a77726b9d0e30f3bb4ccb4949be12f401)
        - **sample\_rate** – **\[in\]** sampling rate(etc 44100,48000,96000) depends on cell phone setting
        - **channels** – **\[in\]** audio channel(etc 1,2) channels depends on cell phone setting
        - **frame\_cnt\_per\_pkt** – **\[in\]** frame count per sbc media packet.
        - **vol** – **\[in\]** music volume

    返回:
    :   N/A

<a id="_CPPv423app_a2dp_stream_process20audio_trigger_type_t"></a>

<a id="_CPPv323app_a2dp_stream_process20audio_trigger_type_t"></a> <a id="_CPPv223app_a2dp_stream_process20audio_trigger_type_t"></a> <a id="app_a2dp_stream_process__audio_trigger_type_t"></a> <a id="app__a2dp_8h_1a6807757c90eb78aae41f1d819150f109"></a> uint32\_t app\_a2dp\_stream\_process([audio\_trigger\_type\_t](app_audio.md#_CPPv420audio_trigger_type_t "audio_trigger_type_t") trigger\_type)
:   application for stream data process

    参数:
    :   **trigger\_type** – **\[in\]** BTIF\_A2DP\_CODEC\_SBC,BTIF\_A2DP\_CODEC\_MPEG\_2\_4\_AAC,BTIF\_A2DP\_CODEC\_LDAC

    返回值:
    :   - **1** – codec already initialize can process stream data
        - **0** – can not process stream data

    返回:
    :   result

<a id="_CPPv430app_a2dp_get_samples_per_framev"></a>

<a id="_CPPv330app_a2dp_get_samples_per_framev"></a> <a id="_CPPv230app_a2dp_get_samples_per_framev"></a> <a id="app_a2dp_get_samples_per_frame__void"></a> <a id="app__a2dp_8h_1a88944f5cdccea9c8cacc03fd215cc457"></a> uint32\_t app\_a2dp\_get\_samples\_per\_frame(void)
:   application to get samples of per frame

    返回:
    :   samples samples of per frame(etc: AUDIO\_A2DP\_SBC\_SAMPLES\_PER\_FRAME)

<a id="_CPPv430app_a2dp_get_music_sample_ratev"></a>

<a id="_CPPv330app_a2dp_get_music_sample_ratev"></a> <a id="_CPPv230app_a2dp_get_music_sample_ratev"></a> <a id="app_a2dp_get_music_sample_rate__void"></a> <a id="app__a2dp_8h_1a441b168355911500088ea8557ea29357"></a> uint32\_t app\_a2dp\_get\_music\_sample\_rate(void)
:   application to get samples rate

    get from g\_audio\_env.audio\_dac\_music\_sample\_rate variable

    返回值:
    :   - **44100** – 44.1K sampling rate
        - **48000** – 48K sampling rate
        - **96000** – 96K sampling rate

    返回:
    :   samples rate

<a id="_CPPv431app_a2dp_get_samples_per_packetv"></a>

<a id="_CPPv331app_a2dp_get_samples_per_packetv"></a> <a id="_CPPv231app_a2dp_get_samples_per_packetv"></a> <a id="app_a2dp_get_samples_per_packet__void"></a> <a id="app__a2dp_8h_1ac78c104b8d94c5b8aa1b5e6b943a4fe9"></a> uint32\_t app\_a2dp\_get\_samples\_per\_packet(void)
:   application to get samples of per packet

    get from (g\_audio\_env.frames\_per\_packet \* [app\_a2dp\_get\_samples\_per\_frame()](#app__a2dp_8h_1a88944f5cdccea9c8cacc03fd215cc457))

    返回值:
    :   **This** – is dynamic value from cell phone,when each call app\_a2dp\_fill\_stream\_buffering to fresh

    返回:
    :   samples\_per\_packet

<a id="_CPPv430app_a2dp_get_frames_per_packetv"></a>

<a id="_CPPv330app_a2dp_get_frames_per_packetv"></a> <a id="_CPPv230app_a2dp_get_frames_per_packetv"></a> <a id="app_a2dp_get_frames_per_packet__void"></a> <a id="app__a2dp_8h_1af810c4141af8c2152ce6aaacf1ac389b"></a> uint32\_t app\_a2dp\_get\_frames\_per\_packet(void)
:   application to get frames of per packet

    get from (g\_audio\_env.frames\_per\_packet)

    返回值:
    :   **This** – is dynamic value from cell phone,when each call app\_a2dp\_fill\_stream\_buffering to fresh

    返回:
    :   frames\_per\_packet

<a id="_CPPv425app_a2dp_get_filled_framev"></a>

<a id="_CPPv325app_a2dp_get_filled_framev"></a> <a id="_CPPv225app_a2dp_get_filled_framev"></a> <a id="app_a2dp_get_filled_frame__void"></a> <a id="app__a2dp_8h_1a277c8436eb566d8c7b1998f9968f880d"></a> uint32\_t app\_a2dp\_get\_filled\_frame(void)
:   application to get filled number of nodes in ring buffer

    get from filled nodes of g\_audio\_env.audio\_a2dp\_frame\_nodes ring buffer

    返回:
    :   number of filled nodes

<a id="_CPPv439app_a2dp_dac_get_free_music_buffer_sizev"></a>

<a id="_CPPv339app_a2dp_dac_get_free_music_buffer_sizev"></a> <a id="_CPPv239app_a2dp_dac_get_free_music_buffer_sizev"></a> <a id="app_a2dp_dac_get_free_music_buffer_size__void"></a> <a id="app__a2dp_8h_1a0d77de90c5ac63791ba93648acd10498"></a> uint32\_t app\_a2dp\_dac\_get\_free\_music\_buffer\_size(void)
:   application to get filled number of nodes in ring buffer

    get from free nodes of g\_audio\_env.audio\_dac\_music\_rb ring buffer free\_size \= rb-\>capacity \- ring\_buffer\_get\_fill\_size(rb);

    返回:
    :   number of free nodes

<a id="_CPPv439app_a2dp_dac_get_fill_music_buffer_sizev"></a>

<a id="_CPPv339app_a2dp_dac_get_fill_music_buffer_sizev"></a> <a id="_CPPv239app_a2dp_dac_get_fill_music_buffer_sizev"></a> <a id="app_a2dp_dac_get_fill_music_buffer_size__void"></a> <a id="app__a2dp_8h_1aa7f8d0ed27921dfeaf6a90c6f34e47d8"></a> uint32\_t app\_a2dp\_dac\_get\_fill\_music\_buffer\_size(void)
:   application to get size of filled data from dac dma buffer

    返回:
    :   filled data size of DAC DMA buffer

<a id="_CPPv430app_a2dp_fill_stream_buffering8uint32_tP7uint8_t8uint32_t8uint32_t8uint32_t7uint8_t"></a>

<a id="_CPPv330app_a2dp_fill_stream_buffering8uint32_tP7uint8_t8uint32_t8uint32_t8uint32_t7uint8_t"></a> <a id="_CPPv230app_a2dp_fill_stream_buffering8uint32_tP7uint8_t8uint32_t8uint32_t8uint32_t7uint8_t"></a> <a id="app_a2dp_fill_stream_buffering__uint32_t.uint8_tP.uint32_t.uint32_t.uint32_t.uint8_t"></a> <a id="app__a2dp_8h_1ab29639579c10bc6d4472c97307b0465f"></a> void app\_a2dp\_fill\_stream\_buffering(uint32\_t codec\_type, uint8\_t \*p\_data, uint32\_t dlen, uint32\_t pac\_seq, uint32\_t frame\_seq, uint8\_t cp\_len)
:   application to fill stream data to ring buffer

    fill stream data to p\_audio\_env-\>audio\_a2dp\_frame\_nodes of ring buffer packet format : Media Packet Header(12Bytes) \+ Content Protection Header(1Byte) \+ mdia Payload

    参数:
    :   - **codec\_type** – **\[in\]** codec type [btif\_a2dp\_codec\_type\_t](../../../btif/btif_type.md#btif__type_8h_1a77726b9d0e30f3bb4ccb4949be12f401)
        - **\*p\_data** – **\[in\]** store a2dp rx stream packet data address
        - **dlen** – **\[in\]** a2dp rx stream data length include stream data packet header length
        - **pac\_seq** – **\[in\]** packet sequence number
        - **frame\_seq** – **\[in\]** frame sequence number
        - **cp\_len** – **\[in\]** Content Protection Header length

    返回:
    :   N/A

<a id="_CPPv424app_a2dp_init_decode_seq8uint32_t8uint32_t"></a>

<a id="_CPPv324app_a2dp_init_decode_seq8uint32_t8uint32_t"></a> <a id="_CPPv224app_a2dp_init_decode_seq8uint32_t8uint32_t"></a> <a id="app_a2dp_init_decode_seq__uint32_t.uint32_t"></a> <a id="app__a2dp_8h_1a17ea3f6b1b8b06d51f6de30cd6345b21"></a> void app\_a2dp\_init\_decode\_seq(uint32\_t pac\_seq, uint32\_t frame\_seq)
:   application to set packet sequence number and frame sequence number

    set packet sequence and frame sequence number to g\_audio\_env environment variable

    参数:
    :   - **pac\_seq** – **\[in\]** packet sequence number
        - **frame\_seq** – **\[in\]** frame sequence number

    返回:
    :   N/A

<a id="_CPPv421app_a2dp_get_last_seqv"></a>

<a id="_CPPv321app_a2dp_get_last_seqv"></a> <a id="_CPPv221app_a2dp_get_last_seqv"></a> <a id="app_a2dp_get_last_seq__void"></a> <a id="app__a2dp_8h_1ae31ad50745ef633d683ed7522b705d00"></a> uint32\_t app\_a2dp\_get\_last\_seq(void)
:   application to get last filled in p\_audio\_env-\>audio\_a2dp\_frame\_nodes ring buffer sequence number

    返回:
    :   last sequence number

<a id="_CPPv428app_a2dp_async_get_frame_seqv"></a>

<a id="_CPPv328app_a2dp_async_get_frame_seqv"></a> <a id="_CPPv228app_a2dp_async_get_frame_seqv"></a> <a id="app_a2dp_async_get_frame_seq__void"></a> <a id="app__a2dp_8h_1a4002d82c746fb15215e63c581724d1a4"></a> uint16\_t app\_a2dp\_async\_get\_frame\_seq(void)
:   application to get start frame sequence number from app\_a2dp\_audio\_ctrl

    usually used in TWS\_SLAVE and TWS\_MASTER sync music stream

    返回:
    :   start frame sequence number of app\_a2dp\_audio\_ctrl

<a id="_CPPv426app_a2dp_resync_is_ongoingv"></a>

<a id="_CPPv326app_a2dp_resync_is_ongoingv"></a> <a id="_CPPv226app_a2dp_resync_is_ongoingv"></a> <a id="app_a2dp_resync_is_ongoing__void"></a> <a id="app__a2dp_8h_1ab0ca5cee2f6d32dd39e7bd67a830876b"></a> bool app\_a2dp\_resync\_is\_ongoing(void)
:   application to get resync status

    返回值:
    :   - **true** – currently re-sync
        - **false** – currently not re-sync

    返回:
    :   resync status

<a id="_CPPv430app_a2dp_resync_get_tws_resyncv"></a>

<a id="_CPPv330app_a2dp_resync_get_tws_resyncv"></a> <a id="_CPPv230app_a2dp_resync_get_tws_resyncv"></a> <a id="app_a2dp_resync_get_tws_resync__void"></a> <a id="app__a2dp_8h_1a86c013ef5dddf3a3e1cacd5a65ab9981"></a> bool app\_a2dp\_resync\_get\_tws\_resync(void)
:   application to get local currently tws link exist or not status

    返回值:
    :   - **true** – tws link exist only or tws link exist and mobile profile sync done
        - **false** – tws link not exist or tws link exist but mobile profile sync not done

    返回:
    :   tws link exist status

<a id="_CPPv429app_a2dp_resync_is_tws_resyncv"></a>

<a id="_CPPv329app_a2dp_resync_is_tws_resyncv"></a> <a id="_CPPv229app_a2dp_resync_is_tws_resyncv"></a> <a id="app_a2dp_resync_is_tws_resync__void"></a> <a id="app__a2dp_8h_1a1988b402a7b90a26085c1cbb52f1c12b"></a> bool app\_a2dp\_resync\_is\_tws\_resync(void)
:   application to get from app\_a2dp\_audio\_ctrl.async\_ctrl.tws\_resync

    Usage Scenarios : Identify tws link is from disconnected to connected(tws sync profile done)

    返回值:
    :   - **true** – app\_a2dp\_audio\_ctrl.async\_ctrl.tws\_resync is true
        - **false** – app\_a2dp\_audio\_ctrl.async\_ctrl.tws\_resync is false

    返回:
    :   tws\_resync

<a id="_CPPv423app_a2dp_rx_stream_dataPK7uint8_t8uint16_t8uint32_t8uint32_t7uint8_t"></a>

<a id="_CPPv323app_a2dp_rx_stream_dataPK7uint8_t8uint16_t8uint32_t8uint32_t7uint8_t"></a> <a id="_CPPv223app_a2dp_rx_stream_dataPK7uint8_t8uint16_t8uint32_t8uint32_t7uint8_t"></a> <a id="app_a2dp_rx_stream_data__uint8_tCP.uint16_t.uint32_t.uint32_t.uint8_t"></a> <a id="app__a2dp_8h_1a86f5ca9c243b4c0f0e6dc6e5f9957e48"></a> void app\_a2dp\_rx\_stream\_data(const uint8\_t \*p\_data, uint16\_t len, uint32\_t pac\_seq, uint32\_t frame\_seq, uint8\_t cp\_len)
:   application to received a2dp stream data

    upper caller is bt\_audio\_dsp\_rx\_a2dp\_stream\_data Media Packet Header(12Bytes) \+ Content Protection Header(1Byte) \+ mdia Payload

    参数:
    :   - **\*p\_data** – **\[in\]** store a2dp rx stream packet data address
        - **len** – **\[in\]** rx stream data length include header length
        - **pac\_seq** – **\[in\]** packet sequence number
        - **frame\_seq** – **\[in\]** frame sequence number
        - **cp\_len** – **\[in\]** Content Protection Header length

    返回:
    :   N/A

<a id="structures"></a>

### Structures

<a id="_CPPv420app_a2dp_sync_ctrl_t"></a>

<a id="_CPPv320app_a2dp_sync_ctrl_t"></a> <a id="_CPPv220app_a2dp_sync_ctrl_t"></a> <a id="app_a2dp_sync_ctrl_t"></a> <a id="structapp__a2dp__sync__ctrl__t"></a> struct app\_a2dp\_sync\_ctrl\_t

<a id="macros"></a>

### Macros

<a id="c.DAC_SBC_RING_BUFF_SIZE"></a>

<a id="app__a2dp_8h_1af2439ec72b680e7b40c330fb369fa9f5"></a> DAC\_SBC\_RING\_BUFF\_SIZE

<a id="c.DAC_AAC_RING_BUFF_SIZE"></a>

<a id="app__a2dp_8h_1a4c7401c067a1703e9914488d2ed8ffe2"></a> DAC\_AAC\_RING\_BUFF\_SIZE

<a id="c.DAC_LDAC_RING_BUFF_SIZE"></a>

<a id="app__a2dp_8h_1ace40bcdc8a9d31ffabe9f641c542c32e"></a> DAC\_LDAC\_RING\_BUFF\_SIZE

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv421app_a2dp_async_type_t"></a>

<a id="_CPPv321app_a2dp_async_type_t"></a> <a id="_CPPv221app_a2dp_async_type_t"></a> <a id="app__a2dp_8h_1ae4ae3581d257b19d7fa6947f06911949"></a> enum app\_a2dp\_async\_type\_t
:   *Values:*

    <a id="_CPPv4N21app_a2dp_async_type_t10PLAY_STARTE"></a>

    <a id="_CPPv3N21app_a2dp_async_type_t10PLAY_STARTE"></a> <a id="_CPPv2N21app_a2dp_async_type_t10PLAY_STARTE"></a> <a id="app__a2dp_8h_1ae4ae3581d257b19d7fa6947f06911949a46a6b00996777617c66fc64325fe7976"></a> enumerator PLAY\_START

    <a id="_CPPv4N21app_a2dp_async_type_t4JOINE"></a>

    <a id="_CPPv3N21app_a2dp_async_type_t4JOINE"></a> <a id="_CPPv2N21app_a2dp_async_type_t4JOINE"></a> <a id="app__a2dp_8h_1ae4ae3581d257b19d7fa6947f06911949a4925a399dab94b9b58f6d1b5cd246af7"></a> enumerator JOIN

    <a id="_CPPv4N21app_a2dp_async_type_t9RETRIGGERE"></a>

    <a id="_CPPv3N21app_a2dp_async_type_t9RETRIGGERE"></a> <a id="_CPPv2N21app_a2dp_async_type_t9RETRIGGERE"></a> <a id="app__a2dp_8h_1ae4ae3581d257b19d7fa6947f06911949aa27bee0df744244364ce5432703b86eb"></a> enumerator RETRIGGER

    <a id="_CPPv4N21app_a2dp_async_type_t12INVALID_TYPEE"></a>

    <a id="_CPPv3N21app_a2dp_async_type_t12INVALID_TYPEE"></a> <a id="_CPPv2N21app_a2dp_async_type_t12INVALID_TYPEE"></a> <a id="app__a2dp_8h_1ae4ae3581d257b19d7fa6947f06911949a7314b0d0e4638eaaeb8690b8555a6546"></a> enumerator INVALID\_TYPE

<a id="_CPPv419_audio_ctrl_state_t"></a>

<a id="_CPPv319_audio_ctrl_state_t"></a> <a id="_CPPv219_audio_ctrl_state_t"></a> <a id="app__a2dp_8h_1a0f3fc4ba4f4a69e7dea09c9f88fc330f"></a> enum \_audio\_ctrl\_state\_t
:   *Values:*

    <a id="_CPPv4N19_audio_ctrl_state_t10ASYNC_IDLEE"></a>

    <a id="_CPPv3N19_audio_ctrl_state_t10ASYNC_IDLEE"></a> <a id="_CPPv2N19_audio_ctrl_state_t10ASYNC_IDLEE"></a> <a id="app__a2dp_8h_1a0f3fc4ba4f4a69e7dea09c9f88fc330fa8656936306a2b76ece5040edbf01e324"></a> enumerator ASYNC\_IDLE

    <a id="_CPPv4N19_audio_ctrl_state_t16ASYNC_W4_PAC_SEQE"></a>

    <a id="_CPPv3N19_audio_ctrl_state_t16ASYNC_W4_PAC_SEQE"></a> <a id="_CPPv2N19_audio_ctrl_state_t16ASYNC_W4_PAC_SEQE"></a> <a id="app__a2dp_8h_1a0f3fc4ba4f4a69e7dea09c9f88fc330fa566110f3adc8f3b25d1df28ce69f9123"></a> enumerator ASYNC\_W4\_PAC\_SEQ

    <a id="_CPPv4N19_audio_ctrl_state_t23ASYNC_W4_SEND_AUDIO_MSGE"></a>

    <a id="_CPPv3N19_audio_ctrl_state_t23ASYNC_W4_SEND_AUDIO_MSGE"></a> <a id="_CPPv2N19_audio_ctrl_state_t23ASYNC_W4_SEND_AUDIO_MSGE"></a> <a id="app__a2dp_8h_1a0f3fc4ba4f4a69e7dea09c9f88fc330fa67e29e61b92d16d4e429ece5d34efafe"></a> enumerator ASYNC\_W4\_SEND\_AUDIO\_MSG

    <a id="_CPPv4N19_audio_ctrl_state_t18ASYNC_RESYNC_STARTE"></a>

    <a id="_CPPv3N19_audio_ctrl_state_t18ASYNC_RESYNC_STARTE"></a> <a id="_CPPv2N19_audio_ctrl_state_t18ASYNC_RESYNC_STARTE"></a> <a id="app__a2dp_8h_1a0f3fc4ba4f4a69e7dea09c9f88fc330faead703da43074692dfaf6ee0c8d0c829"></a> enumerator ASYNC\_RESYNC\_START

    <a id="_CPPv4N19_audio_ctrl_state_t15ASYNC_SYNC_DONEE"></a>

    <a id="_CPPv3N19_audio_ctrl_state_t15ASYNC_SYNC_DONEE"></a> <a id="_CPPv2N19_audio_ctrl_state_t15ASYNC_SYNC_DONEE"></a> <a id="app__a2dp_8h_1a0f3fc4ba4f4a69e7dea09c9f88fc330faf364e3861e71c57879290a75a0063780"></a> enumerator ASYNC\_SYNC\_DONE
