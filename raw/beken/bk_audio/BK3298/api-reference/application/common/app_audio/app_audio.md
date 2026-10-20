---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_audio/app_audio.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="audio-application-functions"></a>

# AUDIO Application Functions

<a id="app-audio-api-brief"></a>

## APP\_AUDIO API Brief

| Application | Brief |
| --- | --- |
| [`app_audio_init()`](#_CPPv414app_audio_initv "app_audio_init") | application for audio initialization |
| [`app_audio_deinit()`](#_CPPv416app_audio_deinitv "app_audio_deinit") | application for audio de-initialization |
| [`app_audio_dac_open()`](#_CPPv418app_audio_dac_open15AUDIO_SOURCE_ID8uint32_t8uint32_t8uint32_t "app_audio_dac_open") | application for audio dac open |
| [`app_audio_dac_close()`](#_CPPv419app_audio_dac_close15AUDIO_SOURCE_ID "app_audio_dac_close") | application for audio DAC close |
| [`app_audio_dac_set_volume()`](#_CPPv424app_audio_dac_set_volume15AUDIO_SOURCE_ID8uint32_t "app_audio_dac_set_volume") | application for audio dac set volume |
| [`app_audio_dac_is_open()`](#_CPPv421app_audio_dac_is_open15AUDIO_SOURCE_ID "app_audio_dac_is_open") | application for check whether audio DAC for the specified source id is opened |
| [`app_audio_dac_get_fill_voice_buffer_size()`](#_CPPv440app_audio_dac_get_fill_voice_buffer_sizev "app_audio_dac_get_fill_voice_buffer_size") | application for audio DAC get filled size of voice |
| [`app_audio_adc_open()`](#_CPPv418app_audio_adc_open8uint32_t8uint32_t8uint32_tPv "app_audio_adc_open") | application for audio adc open |
| [`app_audio_adc_close()`](#_CPPv419app_audio_adc_closev "app_audio_adc_close") | application for audio ADC close |
| [`app_audio_adc_get_fill_buffer_size()`](#_CPPv434app_audio_adc_get_fill_buffer_sizev "app_audio_adc_get_fill_buffer_size") | application for reading audio ADC buffer filled size |
| [`app_audio_adc_read_buffer()`](#_CPPv425app_audio_adc_read_bufferP7uint8_t8uint32_t "app_audio_adc_read_buffer") | read data form ADC buffer |
| [`app_audio_send_msg()`](#_CPPv418app_audio_send_msg16audio_msg_type_t20audio_trigger_type_t "app_audio_send_msg") | application send audio msg to audio task |
| [`app_audio_start_decoder()`](#_CPPv423app_audio_start_decoderv "app_audio_start_decoder") | start decoder to audio task |
| [`app_audio_get_dma_isr_cnt()`](#_CPPv425app_audio_get_dma_isr_cntP8uint32_tP8uint32_t "app_audio_get_dma_isr_cnt") | get DMA count value |
| [`app_audio_get_dma_decode_info()`](#_CPPv429app_audio_get_dma_decode_infoPfP8uint32_t "app_audio_get_dma_decode_info") | get DMA decode information |
| [`app_audio_set_dma_isr_cnt()`](#_CPPv425app_audio_set_dma_isr_cnt8uint32_t8uint32_t "app_audio_set_dma_isr_cnt") | set DMA count value |
| [`app_audio_dac_reopen()`](#_CPPv420app_audio_dac_reopen15AUDIO_SOURCE_ID "app_audio_dac_reopen") | reopen DAC |
| [`app_audio_env_init()`](#_CPPv418app_audio_env_initv "app_audio_env_init") | initialize audio environment settings |
| [`app_audio_hw_init()`](#_CPPv417app_audio_hw_initv "app_audio_hw_init") | initialize audio hardware |
| [`app_mic_ana_stable_timeout()`](#_CPPv426app_mic_ana_stable_timeoutPv "app_mic_ana_stable_timeout") | set ANC/AEC parameter and trigger ADC to work |
| [`app_audio_spp_init()`](#_CPPv418app_audio_spp_initv "app_audio_spp_init") | initialize BEKEN\_AUDIO service |
| [`app_audio_send_spp_rsp()`](#_CPPv422app_audio_send_spp_rsp8uint16_t "app_audio_send_spp_rsp") | send response data by using SPP |
| [`app_audio_dac_eq_enable()`](#_CPPv423app_audio_dac_eq_enable8uint32_tb "app_audio_dac_eq_enable") | eq enable |
| [`app_audio_task_free()`](#_CPPv419app_audio_task_freev "app_audio_task_free") | destroy audio |

<a id="app-audio-api-reference"></a>

## APP\_AUDIO API Reference

<a id="header-file"></a>

### Header File

- [common/app\_audio/app\_audio.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_audio/app_audio.h)

<a id="functions"></a>

### Functions

<a id="_CPPv414app_audio_initv"></a>

<a id="_CPPv314app_audio_initv"></a> <a id="_CPPv214app_audio_initv"></a> <a id="app_audio_init__void"></a> <a id="app__audio_8h_1a8f704deced6f62b0494721cab9b6399f"></a> void app\_audio\_init(void)
:   application for audio initialization

    initialize audio relevant setting, it will set audio hardware

    返回:
    :   N/A

<a id="_CPPv416app_audio_deinitv"></a>

<a id="_CPPv316app_audio_deinitv"></a> <a id="_CPPv216app_audio_deinitv"></a> <a id="app_audio_deinit__void"></a> <a id="app__audio_8h_1a3599021f1f90f80ce33fe879f880f7dc"></a> void app\_audio\_deinit(void)
:   application for audio de-initialization

    de-initialize audio relevant setting, make sure already release other audio related module before call this funcion

    返回:
    :   N/A

<a id="_CPPv418app_audio_dac_open15AUDIO_SOURCE_ID8uint32_t8uint32_t8uint32_t"></a>

<a id="_CPPv318app_audio_dac_open15AUDIO_SOURCE_ID8uint32_t8uint32_t8uint32_t"></a> <a id="_CPPv218app_audio_dac_open15AUDIO_SOURCE_ID8uint32_t8uint32_t8uint32_t"></a> <a id="app_audio_dac_open__AUDIO_SOURCE_ID.uint32_t.uint32_t.uint32_t"></a> <a id="app__audio_8h_1a0e56c08c2e2c77e0d5b440cb0e1bc96d"></a> void app\_audio\_dac\_open(AUDIO\_SOURCE\_ID id, uint32\_t freq, uint32\_t channels, uint32\_t buff\_size)
:   application for audio dac open

    enable DAC moudle for AUDIO\_SOURCE\_ID

    参数:
    :   - **id** – **\[in\]** audio souce ID, AUDIO\_SOURCE\_ID
        - **freq** – **\[in\]** audio souce sampling rate
        - **channels** – **\[in\]** audio souce channels

    返回:
    :   N/A

<a id="_CPPv419app_audio_dac_close15AUDIO_SOURCE_ID"></a>

<a id="_CPPv319app_audio_dac_close15AUDIO_SOURCE_ID"></a> <a id="_CPPv219app_audio_dac_close15AUDIO_SOURCE_ID"></a> <a id="app_audio_dac_close__AUDIO_SOURCE_ID"></a> <a id="app__audio_8h_1abdca6b622b2b0c597794744baa6fd39e"></a> void app\_audio\_dac\_close(AUDIO\_SOURCE\_ID id)
:   application for audio DAC close

    diable DAC moudle for AUDIO\_SOURCE\_ID

    参数:
    :   **id** – **\[in\]** audio souce ID, AUDIO\_SOURCE\_ID

    返回:
    :   N/A

<a id="_CPPv424app_audio_dac_set_volume15AUDIO_SOURCE_ID8uint32_t"></a>

<a id="_CPPv324app_audio_dac_set_volume15AUDIO_SOURCE_ID8uint32_t"></a> <a id="_CPPv224app_audio_dac_set_volume15AUDIO_SOURCE_ID8uint32_t"></a> <a id="app_audio_dac_set_volume__AUDIO_SOURCE_ID.uint32_t"></a> <a id="app__audio_8h_1a8a97fc2b642c2df1fdc78dcdce425eda"></a> void app\_audio\_dac\_set\_volume(AUDIO\_SOURCE\_ID id, uint32\_t volume)
:   application for audio dac set volume

    set volume value for specific DAC source ID

    参数:
    :   - **id** – **\[in\]** audio souce ID, AUDIO\_SOURCE\_ID
        - **volume** – **\[in\]** DAC volume index to set

    返回:
    :   N/A

<a id="_CPPv421app_audio_dac_is_open15AUDIO_SOURCE_ID"></a>

<a id="_CPPv321app_audio_dac_is_open15AUDIO_SOURCE_ID"></a> <a id="_CPPv221app_audio_dac_is_open15AUDIO_SOURCE_ID"></a> <a id="app_audio_dac_is_open__AUDIO_SOURCE_ID"></a> <a id="app__audio_8h_1a4670da4c6f6abded4bf67cbe8e39e39c"></a> uint32\_t app\_audio\_dac\_is\_open(AUDIO\_SOURCE\_ID id)
:   application for check whether audio DAC for the specified source id is opened

    check audio DAC for the specified source is opened or not

    参数:
    :   **id** – **\[in\]** audio souce id, AUDIO\_SOURCE\_ID

    返回值:
    :   - **0** – not opened
        - **other** – opened

    返回:
    :   result

<a id="_CPPv440app_audio_dac_get_fill_voice_buffer_sizev"></a>

<a id="_CPPv340app_audio_dac_get_fill_voice_buffer_sizev"></a> <a id="_CPPv240app_audio_dac_get_fill_voice_buffer_sizev"></a> <a id="app_audio_dac_get_fill_voice_buffer_size__void"></a> <a id="app__audio_8h_1a0c4928413479eb450ac043a5197df142"></a> uint32\_t app\_audio\_dac\_get\_fill\_voice\_buffer\_size(void)
:   application for audio DAC get filled size of voice

    get filled size of voice DAC buffer

    返回:
    :   voice DAC buffer filled size

<a id="_CPPv418app_audio_adc_open8uint32_t8uint32_t8uint32_tPv"></a>

<a id="_CPPv318app_audio_adc_open8uint32_t8uint32_t8uint32_tPv"></a> <a id="_CPPv218app_audio_adc_open8uint32_t8uint32_t8uint32_tPv"></a> <a id="app_audio_adc_open__uint32_t.uint32_t.uint32_t.voidP"></a> <a id="app__audio_8h_1a2df5ee3b0fa95555121b05df983dcbeb"></a> void app\_audio\_adc\_open(uint32\_t freq, uint32\_t adc\_buff\_size, uint32\_t enable\_channel, void \*p\_dms\_isr\_cb)
:   application for audio adc open

    set ADC relevant settings and enable it

    参数:
    :   - **freq** – **\[in\]** simping rate for ADC
        - **adc\_buff\_size** – **\[in\]** set ADC buffer size
        - **enable\_channel** – **\[in\]** ADC channel @AUDIO\_ADC\_CHANNEL
        - **p\_dms\_isr\_cb** – **\[in\]** callback function for low layer

    返回:
    :   N/A

<a id="_CPPv419app_audio_adc_closev"></a>

<a id="_CPPv319app_audio_adc_closev"></a> <a id="_CPPv219app_audio_adc_closev"></a> <a id="app_audio_adc_close__void"></a> <a id="app__audio_8h_1a5330e03de11707565cc034429088c16b"></a> void app\_audio\_adc\_close(void)
:   application for audio ADC close

    close audio ADC

    返回:
    :   N/A

<a id="_CPPv434app_audio_adc_get_fill_buffer_sizev"></a>

<a id="_CPPv334app_audio_adc_get_fill_buffer_sizev"></a> <a id="_CPPv234app_audio_adc_get_fill_buffer_sizev"></a> <a id="app_audio_adc_get_fill_buffer_size__void"></a> <a id="app__audio_8h_1a7157fb3fe951f71c513a33b558989741"></a> uint32\_t app\_audio\_adc\_get\_fill\_buffer\_size(void)
:   application for reading audio ADC buffer filled size

    get ADC buffer filled size

    返回:
    :   ADC buffer filled size

<a id="_CPPv425app_audio_adc_read_bufferP7uint8_t8uint32_t"></a>

<a id="_CPPv325app_audio_adc_read_bufferP7uint8_t8uint32_t"></a> <a id="_CPPv225app_audio_adc_read_bufferP7uint8_t8uint32_t"></a> <a id="app_audio_adc_read_buffer__uint8_tP.uint32_t"></a> <a id="app__audio_8h_1a94fe3e5afb3463dc16796bd81fbd4849"></a> uint32\_t app\_audio\_adc\_read\_buffer(uint8\_t \*buf, uint32\_t len)
:   read data form ADC buffer

    read data form ADC buffer, return value is length of data got

    参数:
    :   - **buf** – **\[out\]** pointer to read buffer
        - **len** – **\[in\]** required data length

    返回值:
    :   - **0** – not data got
        - **other** – length of data got

    返回:
    :   data length

<a id="_CPPv418app_audio_send_msg16audio_msg_type_t20audio_trigger_type_t"></a>

<a id="_CPPv318app_audio_send_msg16audio_msg_type_t20audio_trigger_type_t"></a> <a id="_CPPv218app_audio_send_msg16audio_msg_type_t20audio_trigger_type_t"></a> <a id="app_audio_send_msg__audio_msg_type_t.audio_trigger_type_t"></a> <a id="app__audio_8h_1a7d9506deb9c4e37c9dfcfb29579d7f86"></a> void app\_audio\_send\_msg([audio\_msg\_type\_t](#_CPPv416audio_msg_type_t "audio_msg_type_t") msg\_type, [audio\_trigger\_type\_t](#_CPPv420audio_trigger_type_t "audio_trigger_type_t") trigger\_type)
:   application send audio msg to audio task

    package up audio message and send to AUDIO task

    参数:
    :   - **msg\_type** – **\[in\]** audio message type @audio\_msg\_type\_t
        - **trigger\_type** – **\[in\]** audio trigger type @audio\_trigger\_type\_t

    返回:
    :   N/A

<a id="_CPPv423app_audio_start_decoderv"></a>

<a id="_CPPv323app_audio_start_decoderv"></a> <a id="_CPPv223app_audio_start_decoderv"></a> <a id="app_audio_start_decoder__void"></a> <a id="app__audio_8h_1a107e4a25e718246caa28a287a4be6890"></a> void app\_audio\_start\_decoder(void)
:   start decoder to audio task

    send a start decode message to AUDIO task

    返回:
    :   N/A

<a id="_CPPv425app_audio_get_dma_isr_cntP8uint32_tP8uint32_t"></a>

<a id="_CPPv325app_audio_get_dma_isr_cntP8uint32_tP8uint32_t"></a> <a id="_CPPv225app_audio_get_dma_isr_cntP8uint32_tP8uint32_t"></a> <a id="app_audio_get_dma_isr_cnt__uint32_tP.uint32_tP"></a> <a id="app__audio_8h_1a511b6435e9ebf330d4bd658ae949bd26"></a> void app\_audio\_get\_dma\_isr\_cnt(uint32\_t \*p\_music\_dma\_cnt, uint32\_t \*p\_voice\_dma\_cnt)
:   get DMA count value

    get music DMA count and voice DMA count

    参数:
    :   - **p\_music\_dma\_cnt** – **\[out\]** value of music DMA count
        - **p\_voice\_dma\_cnt** – **\[out\]** value of voice DMA count

    返回:
    :   N/A

<a id="_CPPv429app_audio_get_dma_decode_infoPfP8uint32_t"></a>

<a id="_CPPv329app_audio_get_dma_decode_infoPfP8uint32_t"></a> <a id="_CPPv229app_audio_get_dma_decode_infoPfP8uint32_t"></a> <a id="app_audio_get_dma_decode_info__floatP.uint32_tP"></a> <a id="app__audio_8h_1a5ae0d8a4953bf2715e0a14ca08cff7e9"></a> void app\_audio\_get\_dma\_decode\_info(float \*p\_pac\_seq, uint32\_t \*p\_frame\_seq)
:   get DMA decode information

    get sequeunce number and from DMA decode

    参数:
    :   - **p\_pac\_seq** – **\[out\]** value of sequeunce number
        - **p\_frame\_seq** – **\[out\]** value of frame number

    返回:
    :   N/A

<a id="_CPPv425app_audio_set_dma_isr_cnt8uint32_t8uint32_t"></a>

<a id="_CPPv325app_audio_set_dma_isr_cnt8uint32_t8uint32_t"></a> <a id="_CPPv225app_audio_set_dma_isr_cnt8uint32_t8uint32_t"></a> <a id="app_audio_set_dma_isr_cnt__uint32_t.uint32_t"></a> <a id="app__audio_8h_1a45019ca051faed32378822846a6f0f5a"></a> void app\_audio\_set\_dma\_isr\_cnt(uint32\_t p\_music\_dma\_cnt, uint32\_t p\_voice\_dma\_cnt)
:   set DMA count value

    update music DMA count and voice DMA count

    参数:
    :   - **p\_music\_dma\_cnt** – **\[in\]** new value for music DMA count
        - **p\_voice\_dma\_cnt** – **\[in\]** new value for voice DMA count

    返回:
    :   N/A

<a id="_CPPv420app_audio_dac_reopen15AUDIO_SOURCE_ID"></a>

<a id="_CPPv320app_audio_dac_reopen15AUDIO_SOURCE_ID"></a> <a id="_CPPv220app_audio_dac_reopen15AUDIO_SOURCE_ID"></a> <a id="app_audio_dac_reopen__AUDIO_SOURCE_ID"></a> <a id="app__audio_8h_1a52cd978e5a2756853ee3453c6ff75afc"></a> void app\_audio\_dac\_reopen(AUDIO\_SOURCE\_ID id)
:   reopen DAC

    close DAC, reinitialize and update audio relevant settings, open DAC again

    参数:
    :   **id** – **\[in\]** audio source id @AUDIO\_SOURCE\_ID

    返回:
    :   N/A

<a id="_CPPv418app_audio_env_initv"></a>

<a id="_CPPv318app_audio_env_initv"></a> <a id="_CPPv218app_audio_env_initv"></a> <a id="app_audio_env_init__void"></a> <a id="app__audio_8h_1a6cfa5cc6ca9cbab07634d1d5e92114c0"></a> void app\_audio\_env\_init(void)
:   initialize audio environment settings

    initialize audio environment relevant settings, set callback functions for DSP module. Lastly, start AUDIO task

    返回:
    :   N/A

<a id="_CPPv417app_audio_hw_initv"></a>

<a id="_CPPv317app_audio_hw_initv"></a> <a id="_CPPv217app_audio_hw_initv"></a> <a id="app_audio_hw_init__void"></a> <a id="app__audio_8h_1a2c355f872790c0a9e552866ffac33824"></a> void app\_audio\_hw\_init(void)
:   initialize audio hardware

    initialize audio hardware relevant settings

    返回:
    :   N/A

<a id="_CPPv426app_mic_ana_stable_timeoutPv"></a>

<a id="_CPPv326app_mic_ana_stable_timeoutPv"></a> <a id="_CPPv226app_mic_ana_stable_timeoutPv"></a> <a id="app_mic_ana_stable_timeout__voidP"></a> <a id="app__audio_8h_1a7e4286d2205f26c9d1f6d428be3dfd25"></a> int32\_t app\_mic\_ana\_stable\_timeout(void \*pv\_arg)
:   set ANC/AEC parameter and trigger ADC to work

    callback function for timer task, it set ANC/AEC parameter and trigger to get MIC data

    参数:
    :   **pv\_arg** – **\[in\]** MIC ana relevant parameters @ana\_para\_t

    返回值:
    :   **0** – always 0

    返回:
    :   result

<a id="_CPPv418app_audio_spp_initv"></a>

<a id="_CPPv318app_audio_spp_initv"></a> <a id="_CPPv218app_audio_spp_initv"></a> <a id="app_audio_spp_init__void"></a> <a id="app__audio_8h_1a5ce9675809f6a82e59e160581f162243"></a> void app\_audio\_spp\_init(void)
:   initialize BEKEN\_AUDIO service

    initialize BEKEN\_AUDIO service relevant setting and hook up SPP service

    返回:
    :   N/A

<a id="_CPPv422app_audio_send_spp_rsp8uint16_t"></a>

<a id="_CPPv322app_audio_send_spp_rsp8uint16_t"></a> <a id="_CPPv222app_audio_send_spp_rsp8uint16_t"></a> <a id="app_audio_send_spp_rsp__uint16_t"></a> <a id="app__audio_8h_1a6bc397b524ca4fbeb8494224555273f7"></a> void app\_audio\_send\_spp\_rsp(uint16\_t length)
:   send response data by using SPP

    end response data by using SPP after adjusting EQ settings

    参数:
    :   **length** – **\[in\]** of spp response

    返回:
    :   N/A

<a id="_CPPv423app_audio_dac_eq_enable8uint32_tb"></a>

<a id="_CPPv323app_audio_dac_eq_enable8uint32_tb"></a> <a id="_CPPv223app_audio_dac_eq_enable8uint32_tb"></a> <a id="app_audio_dac_eq_enable__uint32_t.b"></a> <a id="app__audio_8h_1a64af13763114b33e501d59361cdc215b"></a> void app\_audio\_dac\_eq\_enable(uint32\_t enable, bool dac\_en)
:   eq enable

    eq enable function

    参数:
    :   - **enable** – **\[in\]**
        - **dac** – **\[in\]** enable

    返回:
    :   N/A

<a id="_CPPv419app_audio_task_freev"></a>

<a id="_CPPv319app_audio_task_freev"></a> <a id="_CPPv219app_audio_task_freev"></a> <a id="app_audio_task_free__void"></a> <a id="app__audio_8h_1ae7bce075333f9960158a2f03100b925e"></a> void app\_audio\_task\_free(void)
:   destroy audio

    destroy audio function

    参数:
    :   **NA** – **\[in\]**

    返回:
    :   N/A

<a id="structures"></a>

### Structures

<a id="_CPPv411audio_msg_t"></a>

<a id="_CPPv311audio_msg_t"></a> <a id="_CPPv211audio_msg_t"></a> <a id="audio_msg_t"></a> <a id="structaudio__msg__t"></a> struct audio\_msg\_t
:   AUDIO task messger struct defintion.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N11audio_msg_t8msg_typeE"></a>

    <a id="_CPPv3N11audio_msg_t8msg_typeE"></a> <a id="_CPPv2N11audio_msg_t8msg_typeE"></a> <a id="audio_msg_t::msg_type__audio_msg_type_t"></a> <a id="structaudio__msg__t_1a06a83f87196ee498a59f6f6c74d51585"></a> [audio\_msg\_type\_t](#_CPPv416audio_msg_type_t "audio_msg_type_t") msg\_type
    :   message type @audio\_msg\_type\_t

    <a id="_CPPv4N11audio_msg_t12trigger_typeE"></a>

    <a id="_CPPv3N11audio_msg_t12trigger_typeE"></a> <a id="_CPPv2N11audio_msg_t12trigger_typeE"></a> <a id="audio_msg_t::trigger_type__audio_trigger_type_t"></a> <a id="structaudio__msg__t_1a5edc11a9ff92c6b3ffd746744d9b9ae8"></a> [audio\_trigger\_type\_t](#_CPPv420audio_trigger_type_t "audio_trigger_type_t") trigger\_type
    :   trigger type @audio\_trigger\_type\_t

    <a id="_CPPv4N11audio_msg_t7hint_idE"></a>

    <a id="_CPPv3N11audio_msg_t7hint_idE"></a> <a id="_CPPv2N11audio_msg_t7hint_idE"></a> <a id="audio_msg_t::hint_id__uint8_t"></a> <a id="structaudio__msg__t_1a5bde44eea4f04caba79d0adc5598969b"></a> uint8\_t hint\_id
    :   hints ID

<a id="_CPPv410aac_temp_t"></a>

<a id="_CPPv310aac_temp_t"></a> <a id="_CPPv210aac_temp_t"></a> <a id="aac_temp_t"></a> <a id="structaac__temp__t"></a> struct aac\_temp\_t
:   AAC temp store struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N10aac_temp_t16p_aac_temp_storeE"></a>

    <a id="_CPPv3N10aac_temp_t16p_aac_temp_storeE"></a> <a id="_CPPv2N10aac_temp_t16p_aac_temp_storeE"></a> <a id="aac_temp_t::p_aac_temp_store__uint8_tP"></a> <a id="structaac__temp__t_1ae5a3d5861a4e8f6eff75257c27091af2"></a> uint8\_t \*p\_aac\_temp\_store
    :   pointer to AAC temp store buffer

    <a id="_CPPv4N10aac_temp_t8p_aac_rdE"></a>

    <a id="_CPPv3N10aac_temp_t8p_aac_rdE"></a> <a id="_CPPv2N10aac_temp_t8p_aac_rdE"></a> <a id="aac_temp_t::p_aac_rd__uint8_tP"></a> <a id="structaac__temp__t_1a362d09f701ebc6e318d1fd6f08aebeb8"></a> uint8\_t \*p\_aac\_rd
    :   AAC read pointer

    <a id="_CPPv4N10aac_temp_t6lengthE"></a>

    <a id="_CPPv3N10aac_temp_t6lengthE"></a> <a id="_CPPv2N10aac_temp_t6lengthE"></a> <a id="aac_temp_t::length__uint32_t"></a> <a id="structaac__temp__t_1a05681fd89609140d24861db18181d15c"></a> uint32\_t length
    :   left data length which need to be processed

<a id="_CPPv410ana_para_t"></a>

<a id="_CPPv310ana_para_t"></a> <a id="_CPPv210ana_para_t"></a> <a id="ana_para_t"></a> <a id="structana__para__t"></a> struct ana\_para\_t
:   ANA paramreter strcut definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N10ana_para_t8channelsE"></a>

    <a id="_CPPv3N10ana_para_t8channelsE"></a> <a id="_CPPv2N10ana_para_t8channelsE"></a> <a id="ana_para_t::channels__uint32_t"></a> <a id="structana__para__t_1a811bd72c5ed033aebe6014d0d539918f"></a> uint32\_t channels
    :   using ANC channel index

    <a id="_CPPv4N10ana_para_t5pathsE"></a>

    <a id="_CPPv3N10ana_para_t5pathsE"></a> <a id="_CPPv2N10ana_para_t5pathsE"></a> <a id="ana_para_t::paths__uint32_t"></a> <a id="structana__para__t_1affe2c3cef9befd520e57f561ecc2e4fa"></a> uint32\_t paths
    :   ANC path index

    <a id="_CPPv4N10ana_para_t4typeE"></a>

    <a id="_CPPv3N10ana_para_t4typeE"></a> <a id="_CPPv2N10ana_para_t4typeE"></a> <a id="ana_para_t::type__uint8_t"></a> <a id="structana__para__t_1a4c699d4132d7d5b0692c6c2d0b0086e3"></a> uint8\_t type
    :   ANA type @ANA\_EN\_ANC @ANA\_EN\_AEC

    <a id="_CPPv4N10ana_para_t13need_open_dacE"></a>

    <a id="_CPPv3N10ana_para_t13need_open_dacE"></a> <a id="_CPPv2N10ana_para_t13need_open_dacE"></a> <a id="ana_para_t::need_open_dac__b"></a> <a id="structana__para__t_1a6bc10ed914d2da80c7fb3fc4e82d48be"></a> bool need\_open\_dac
    :   bool value for need to open DAC

<a id="_CPPv411audio_spp_t"></a>

<a id="_CPPv311audio_spp_t"></a> <a id="_CPPv211audio_spp_t"></a> <a id="audio_spp_t"></a> <a id="structaudio__spp__t"></a> struct audio\_spp\_t
:   BEKEN AUDIO service struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N11audio_spp_t10spp_serverE"></a>

    <a id="_CPPv3N11audio_spp_t10spp_serverE"></a> <a id="_CPPv2N11audio_spp_t10spp_serverE"></a> <a id="audio_spp_t::spp_server__spp_server_t"></a> <a id="structaudio__spp__t_1a47fcdbca8fb26ace78c17ab4a00d1d60"></a> [spp\_server\_t](../../../btif/spp_if.md#_CPPv412spp_server_t "spp_server_t") spp\_server
    :   SPP server information @spp\_server\_t

    <a id="_CPPv4N11audio_spp_t12is_connectedE"></a>

    <a id="_CPPv3N11audio_spp_t12is_connectedE"></a> <a id="_CPPv2N11audio_spp_t12is_connectedE"></a> <a id="audio_spp_t::is_connected__b"></a> <a id="structaudio__spp__t_1a40f5f2067e319ac2a49a5a4c598e07cd"></a> bool is\_connected
    :   is connected or not

    <a id="_CPPv4N11audio_spp_t6handleE"></a>

    <a id="_CPPv3N11audio_spp_t6handleE"></a> <a id="_CPPv2N11audio_spp_t6handleE"></a> <a id="audio_spp_t::handle__uint16_t"></a> <a id="structaudio__spp__t_1a0ea632ecc5a283e8d049b492bde30ca4"></a> uint16\_t handle
    :   connection handle index

    <a id="_CPPv4N11audio_spp_t8p_tx_bufE"></a>

    <a id="_CPPv3N11audio_spp_t8p_tx_bufE"></a> <a id="_CPPv2N11audio_spp_t8p_tx_bufE"></a> <a id="audio_spp_t::p_tx_buf__uint8_tP"></a> <a id="structaudio__spp__t_1a57bf5adf9d313c7e98c8c430e6476e77"></a> uint8\_t \*p\_tx\_buf
    :   data buffer which need to be sent

<a id="_CPPv411plc_state_t"></a>

<a id="_CPPv311plc_state_t"></a> <a id="_CPPv211plc_state_t"></a> <a id="plc_state_t"></a> <a id="structplc__state__t"></a> struct plc\_state\_t
:   PLC state struct definition.

<a id="_CPPv412voice_info_t"></a>

<a id="_CPPv312voice_info_t"></a> <a id="_CPPv212voice_info_t"></a> <a id="voice_info_t"></a> <a id="structvoice__info__t"></a> struct voice\_info\_t
:   voice information struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N12voice_info_t11recv_statusE"></a>

    <a id="_CPPv3N12voice_info_t11recv_statusE"></a> <a id="_CPPv2N12voice_info_t11recv_statusE"></a> <a id="voice_info_t::recv_status__uint8_t"></a> <a id="structvoice__info__t_1a822e9c1148ef8308cda81469375413e4"></a> uint8\_t recv\_status
    :   controller recive SCO data result, 0: no error

    <a id="_CPPv4N12voice_info_t11rx_sco_dataE"></a>

    <a id="_CPPv3N12voice_info_t11rx_sco_dataE"></a> <a id="_CPPv2N12voice_info_t11rx_sco_dataE"></a> <a id="voice_info_t::rx_sco_data__uint8_tA"></a> <a id="structvoice__info__t_1af2ee72d49962531c450a038ba14c078e"></a> uint8\_t rx\_sco\_data\[120\]
    :   data buffer for recviced SCO data

    <a id="_CPPv4N12voice_info_t9msbc_dataE"></a>

    <a id="_CPPv3N12voice_info_t9msbc_dataE"></a> <a id="_CPPv2N12voice_info_t9msbc_dataE"></a> <a id="voice_info_t::msbc_data__uint8_tA"></a> <a id="structvoice__info__t_1ad43c9b79f976a132416b3613a46f41f7"></a> uint8\_t msbc\_data\[60\]
    :   data buffer for recviced mSBC data

    <a id="_CPPv4N12voice_info_t9p_tx_addrE"></a>

    <a id="_CPPv3N12voice_info_t9p_tx_addrE"></a> <a id="_CPPv2N12voice_info_t9p_tx_addrE"></a> <a id="voice_info_t::p_tx_addr__uint8_tP"></a> <a id="structvoice__info__t_1a5902f2e08bb4cb125792dad62523dd92"></a> uint8\_t \*p\_tx\_addr
    :   data buffer for tx SCO data can be stored

    <a id="_CPPv4N12voice_info_t7pkt_lenE"></a>

    <a id="_CPPv3N12voice_info_t7pkt_lenE"></a> <a id="_CPPv2N12voice_info_t7pkt_lenE"></a> <a id="voice_info_t::pkt_len__uint16_t"></a> <a id="structvoice__info__t_1ae69eb11abc3937f182a72d6c89d8810c"></a> uint16\_t pkt\_len
    :   data length for SCO data

    <a id="_CPPv4N12voice_info_t9plc_stateE"></a>

    <a id="_CPPv3N12voice_info_t9plc_stateE"></a> <a id="_CPPv2N12voice_info_t9plc_stateE"></a> <a id="voice_info_t::plc_state__plc_state_t"></a> <a id="structvoice__info__t_1ac95bbda23fc0b9d9f05c42bc7fc471c7"></a> [plc\_state\_t](#_CPPv411plc_state_t "plc_state_t") plc\_state
    :   PLC state @plc\_state\_t

    <a id="_CPPv4N12voice_info_t15msbc_encode_cntE"></a>

    <a id="_CPPv3N12voice_info_t15msbc_encode_cntE"></a> <a id="_CPPv2N12voice_info_t15msbc_encode_cntE"></a> <a id="voice_info_t::msbc_encode_cnt__uint32_t"></a> <a id="structvoice__info__t_1adfd82b8bac989d794ed55f7e4d9d759e"></a> uint32\_t msbc\_encode\_cnt
    :   mSBC encode count

    <a id="_CPPv4N12voice_info_t15msbc_decode_cntE"></a>

    <a id="_CPPv3N12voice_info_t15msbc_decode_cntE"></a> <a id="_CPPv2N12voice_info_t15msbc_decode_cntE"></a> <a id="voice_info_t::msbc_decode_cnt__uint32_t"></a> <a id="structvoice__info__t_1a461681c6bfad57f75b4ef95b868c2f71"></a> uint32\_t msbc\_decode\_cnt
    :   mSBC decode count

    <a id="_CPPv4N12voice_info_t15cvsd_encode_cntE"></a>

    <a id="_CPPv3N12voice_info_t15cvsd_encode_cntE"></a> <a id="_CPPv2N12voice_info_t15cvsd_encode_cntE"></a> <a id="voice_info_t::cvsd_encode_cnt__uint32_t"></a> <a id="structvoice__info__t_1a601b8e22741e5c9d664fc9166555548a"></a> uint32\_t cvsd\_encode\_cnt
    :   CVSD encode count

    <a id="_CPPv4N12voice_info_t15cvsd_decode_cntE"></a>

    <a id="_CPPv3N12voice_info_t15cvsd_decode_cntE"></a> <a id="_CPPv2N12voice_info_t15cvsd_decode_cntE"></a> <a id="voice_info_t::cvsd_decode_cnt__uint32_t"></a> <a id="structvoice__info__t_1a8ca7ef26204e8aff73db4ae7bb44aea4"></a> uint32\_t cvsd\_decode\_cnt
    :   CVSD decode count

    <a id="_CPPv4N12voice_info_t21msbc_decode_error_cntE"></a>

    <a id="_CPPv3N12voice_info_t21msbc_decode_error_cntE"></a> <a id="_CPPv2N12voice_info_t21msbc_decode_error_cntE"></a> <a id="voice_info_t::msbc_decode_error_cnt__uint32_t"></a> <a id="structvoice__info__t_1a54c641a5c22b3e6df9c1aaa2b114a8e8"></a> uint32\_t msbc\_decode\_error\_cnt
    :   mSBC decode error count

    <a id="_CPPv4N12voice_info_t21msbc_encode_error_cntE"></a>

    <a id="_CPPv3N12voice_info_t21msbc_encode_error_cntE"></a> <a id="_CPPv2N12voice_info_t21msbc_encode_error_cntE"></a> <a id="voice_info_t::msbc_encode_error_cnt__uint32_t"></a> <a id="structvoice__info__t_1ae0d2d1f81654a6dc16d402cd14bb46b1"></a> uint32\_t msbc\_encode\_error\_cnt
    :   mSBC encode error count

    <a id="_CPPv4N12voice_info_t17mic_underflow_cntE"></a>

    <a id="_CPPv3N12voice_info_t17mic_underflow_cntE"></a> <a id="_CPPv2N12voice_info_t17mic_underflow_cntE"></a> <a id="voice_info_t::mic_underflow_cnt__uint32_t"></a> <a id="structvoice__info__t_1a2e94d192c19fc74d85f97c13c4d159ab"></a> uint32\_t mic\_underflow\_cnt
    :   fail to get ADC data count

    <a id="_CPPv4N12voice_info_t16bt_voice_isr_cntE"></a>

    <a id="_CPPv3N12voice_info_t16bt_voice_isr_cntE"></a> <a id="_CPPv2N12voice_info_t16bt_voice_isr_cntE"></a> <a id="voice_info_t::bt_voice_isr_cnt__uint32_t"></a> <a id="structvoice__info__t_1a9b2f1db471038ecacb573a42c5865189"></a> uint32\_t bt\_voice\_isr\_cnt
    :   system ISR count for handling BT voice data

    <a id="_CPPv4N12voice_info_t18bt_voice_triggeredE"></a>

    <a id="_CPPv3N12voice_info_t18bt_voice_triggeredE"></a> <a id="_CPPv2N12voice_info_t18bt_voice_triggeredE"></a> <a id="voice_info_t::bt_voice_triggered__b"></a> <a id="structvoice__info__t_1a530156898e957e90a3f5e78bc932fd3c"></a> bool bt\_voice\_triggered
    :   boolean value for start processing BT voice data

<a id="_CPPv411audio_env_t"></a>

<a id="_CPPv311audio_env_t"></a> <a id="_CPPv211audio_env_t"></a> <a id="audio_env_t"></a> <a id="structaudio__env__t"></a> struct audio\_env\_t
:   audio environment data struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N11audio_env_t18audio_hw_init_doneE"></a>

    <a id="_CPPv3N11audio_env_t18audio_hw_init_doneE"></a> <a id="_CPPv2N11audio_env_t18audio_hw_init_doneE"></a> <a id="audio_env_t::audio_hw_init_done__b"></a> <a id="structaudio__env__t_1a18be4ea1d23017e729b37d1e77e5baea"></a> bool audio\_hw\_init\_done
    :   boolean value for audio hardware module initialize done

    <a id="_CPPv4N11audio_env_t15audio_init_doneE"></a>

    <a id="_CPPv3N11audio_env_t15audio_init_doneE"></a> <a id="_CPPv2N11audio_env_t15audio_init_doneE"></a> <a id="audio_env_t::audio_init_done__b"></a> <a id="structaudio__env__t_1a07a12dfad1238c9c41df47376bf0dbd7"></a> bool audio\_init\_done
    :   boolean value for audio initialize done

    <a id="_CPPv4N11audio_env_t12audio_src_idE"></a>

    <a id="_CPPv3N11audio_env_t12audio_src_idE"></a> <a id="_CPPv2N11audio_env_t12audio_src_idE"></a> <a id="audio_env_t::audio_src_id__uint8_t"></a> <a id="structaudio__env__t_1ac19f0568fe87183a828f2b469f1b802c"></a> uint8\_t audio\_src\_id
    :   audio SRC ID @AUDIO\_SOURCE\_ID

    <a id="_CPPv4N11audio_env_t10audio_chanE"></a>

    <a id="_CPPv3N11audio_env_t10audio_chanE"></a> <a id="_CPPv2N11audio_env_t10audio_chanE"></a> <a id="audio_env_t::audio_chan__uint8_t"></a> <a id="structaudio__env__t_1ae4f4528215663d932d7e46f8173bc3b2"></a> uint8\_t audio\_chan
    :   audio channel number

    <a id="_CPPv4N11audio_env_t16audio_codec_typeE"></a>

    <a id="_CPPv3N11audio_env_t16audio_codec_typeE"></a> <a id="_CPPv2N11audio_env_t16audio_codec_typeE"></a> <a id="audio_env_t::audio_codec_type__uint8_t"></a> <a id="structaudio__env__t_1a7930d3b2a74028dffee2178e489b3e7f"></a> uint8\_t audio\_codec\_type
    :   audcio codec type

    <a id="_CPPv4N11audio_env_t27audio_dac_music_sample_rateE"></a>

    <a id="_CPPv3N11audio_env_t27audio_dac_music_sample_rateE"></a> <a id="_CPPv2N11audio_env_t27audio_dac_music_sample_rateE"></a> <a id="audio_env_t::audio_dac_music_sample_rate__uint32_t"></a> <a id="structaudio__env__t_1a5f19d353da9528b8ddbdc82f1b1eb0be"></a> uint32\_t audio\_dac\_music\_sample\_rate
    :   dac samping rate for music

    <a id="_CPPv4N11audio_env_t27audio_dac_voice_sample_rateE"></a>

    <a id="_CPPv3N11audio_env_t27audio_dac_voice_sample_rateE"></a> <a id="_CPPv2N11audio_env_t27audio_dac_voice_sample_rateE"></a> <a id="audio_env_t::audio_dac_voice_sample_rate__uint32_t"></a> <a id="structaudio__env__t_1a86f13cddea37feba411fe49e8d68ad41"></a> uint32\_t audio\_dac\_voice\_sample\_rate
    :   dac samping rate for voice

    <a id="_CPPv4N11audio_env_t27audio_dac_hints_sample_rateE"></a>

    <a id="_CPPv3N11audio_env_t27audio_dac_hints_sample_rateE"></a> <a id="_CPPv2N11audio_env_t27audio_dac_hints_sample_rateE"></a> <a id="audio_env_t::audio_dac_hints_sample_rate__uint32_t"></a> <a id="structaudio__env__t_1ab19198e5d78bcb78201eddab9eda7971"></a> uint32\_t audio\_dac\_hints\_sample\_rate
    :   dac samping rate for hints

    <a id="_CPPv4N11audio_env_t18audio_music_volumeE"></a>

    <a id="_CPPv3N11audio_env_t18audio_music_volumeE"></a> <a id="_CPPv2N11audio_env_t18audio_music_volumeE"></a> <a id="audio_env_t::audio_music_volume__int32_t"></a> <a id="structaudio__env__t_1a75df522c2bec186d119621c8d3f83dc6"></a> int32\_t audio\_music\_volume
    :   volume for music

    <a id="_CPPv4N11audio_env_t19audio_music_volume2E"></a>

    <a id="_CPPv3N11audio_env_t19audio_music_volume2E"></a> <a id="_CPPv2N11audio_env_t19audio_music_volume2E"></a> <a id="audio_env_t::audio_music_volume2__int32_t"></a> <a id="structaudio__env__t_1a824f464d44f41108bf48adbea6f5ca75"></a> int32\_t audio\_music\_volume2
    :   not used

    <a id="_CPPv4N11audio_env_t18audio_voice_volumeE"></a>

    <a id="_CPPv3N11audio_env_t18audio_voice_volumeE"></a> <a id="_CPPv2N11audio_env_t18audio_voice_volumeE"></a> <a id="audio_env_t::audio_voice_volume__int32_t"></a> <a id="structaudio__env__t_1a33591715f8762df3051cf6d7eb68f80e"></a> int32\_t audio\_voice\_volume
    :   volume for voice

    <a id="_CPPv4N11audio_env_t19audio_voice_volume2E"></a>

    <a id="_CPPv3N11audio_env_t19audio_voice_volume2E"></a> <a id="_CPPv2N11audio_env_t19audio_voice_volume2E"></a> <a id="audio_env_t::audio_voice_volume2__int32_t"></a> <a id="structaudio__env__t_1a9045e6e41bab8b41dc4d0240f75cb6ff"></a> int32\_t audio\_voice\_volume2
    :   not used

    <a id="_CPPv4N11audio_env_t18audio_hints_volumeE"></a>

    <a id="_CPPv3N11audio_env_t18audio_hints_volumeE"></a> <a id="_CPPv2N11audio_env_t18audio_hints_volumeE"></a> <a id="audio_env_t::audio_hints_volume__int32_t"></a> <a id="structaudio__env__t_1a924711e02b8c50b2d4112a6980bc4562"></a> int32\_t audio\_hints\_volume
    :   volume for hints

    <a id="_CPPv4N11audio_env_t19audio_hints_volume2E"></a>

    <a id="_CPPv3N11audio_env_t19audio_hints_volume2E"></a> <a id="_CPPv2N11audio_env_t19audio_hints_volume2E"></a> <a id="audio_env_t::audio_hints_volume2__int32_t"></a> <a id="structaudio__env__t_1a8f35c3010631e6114f035c9a75b76741"></a> int32\_t audio\_hints\_volume2
    :   not used

    <a id="_CPPv4N11audio_env_t7adc_dmaE"></a>

    <a id="_CPPv3N11audio_env_t7adc_dmaE"></a> <a id="_CPPv2N11audio_env_t7adc_dmaE"></a> <a id="audio_env_t::adc_dma__uint32_t"></a> <a id="structaudio__env__t_1a089947c23a7b56f4c9ad6cfe32ab8407"></a> uint32\_t adc\_dma
    :   DMA channel value for ADC

    <a id="_CPPv4N11audio_env_t13dac_music_dmaE"></a>

    <a id="_CPPv3N11audio_env_t13dac_music_dmaE"></a> <a id="_CPPv2N11audio_env_t13dac_music_dmaE"></a> <a id="audio_env_t::dac_music_dma__uint32_t"></a> <a id="structaudio__env__t_1a600e46bbde39d435f0f367f4ff0ad0e1"></a> uint32\_t dac\_music\_dma
    :   DMA channel value for music DAC

    <a id="_CPPv4N11audio_env_t13dac_voice_dmaE"></a>

    <a id="_CPPv3N11audio_env_t13dac_voice_dmaE"></a> <a id="_CPPv2N11audio_env_t13dac_voice_dmaE"></a> <a id="audio_env_t::dac_voice_dma__uint32_t"></a> <a id="structaudio__env__t_1a35a9488e9e609e262a99f0da04a738dc"></a> uint32\_t dac\_voice\_dma
    :   DMA channel value for voice DAC

    <a id="_CPPv4N11audio_env_t13dac_hints_dmaE"></a>

    <a id="_CPPv3N11audio_env_t13dac_hints_dmaE"></a> <a id="_CPPv2N11audio_env_t13dac_hints_dmaE"></a> <a id="audio_env_t::dac_hints_dma__uint32_t"></a> <a id="structaudio__env__t_1a7b4b8bf2e17aa56a6abcf760e6012e81"></a> uint32\_t dac\_hints\_dma
    :   DMA channel value for hints DAC

    <a id="_CPPv4N11audio_env_t10linein_dmaE"></a>

    <a id="_CPPv3N11audio_env_t10linein_dmaE"></a> <a id="_CPPv2N11audio_env_t10linein_dmaE"></a> <a id="audio_env_t::linein_dma__uint32_t"></a> <a id="structaudio__env__t_1a0010af884e3e4b6c96e106bbaddd5765"></a> uint32\_t linein\_dma
    :   DMA channel value for line in

    <a id="_CPPv4N11audio_env_t12audio_adc_rbE"></a>

    <a id="_CPPv3N11audio_env_t12audio_adc_rbE"></a> <a id="_CPPv2N11audio_env_t12audio_adc_rbE"></a> <a id="audio_env_t::audio_adc_rb__ring_buffer_t"></a> <a id="structaudio__env__t_1ad4aa626b365c9204e36bd7ab794e3758"></a> ring\_buffer\_t audio\_adc\_rb
    :   ringbuffer for ADC

    <a id="_CPPv4N11audio_env_t18audio_dac_music_rbE"></a>

    <a id="_CPPv3N11audio_env_t18audio_dac_music_rbE"></a> <a id="_CPPv2N11audio_env_t18audio_dac_music_rbE"></a> <a id="audio_env_t::audio_dac_music_rb__ring_buffer_t"></a> <a id="structaudio__env__t_1a99a1abd4fb18edf6c36561006645ba33"></a> ring\_buffer\_t audio\_dac\_music\_rb
    :   ringbuffer for music DAC

    <a id="_CPPv4N11audio_env_t18audio_dac_voice_rbE"></a>

    <a id="_CPPv3N11audio_env_t18audio_dac_voice_rbE"></a> <a id="_CPPv2N11audio_env_t18audio_dac_voice_rbE"></a> <a id="audio_env_t::audio_dac_voice_rb__ring_buffer_t"></a> <a id="structaudio__env__t_1a49810f32857d4b39fb27f27e300a3819"></a> ring\_buffer\_t audio\_dac\_voice\_rb
    :   ringbuffer for voice DAC

    <a id="_CPPv4N11audio_env_t18audio_dac_hints_rbE"></a>

    <a id="_CPPv3N11audio_env_t18audio_dac_hints_rbE"></a> <a id="_CPPv2N11audio_env_t18audio_dac_hints_rbE"></a> <a id="audio_env_t::audio_dac_hints_rb__ring_buffer_t"></a> <a id="structaudio__env__t_1a34fe8f6377ff1088515ce4bd774540ba"></a> ring\_buffer\_t audio\_dac\_hints\_rb
    :   ringbuffer for hints DAC

    <a id="_CPPv4N11audio_env_t22audio_a2dp_frame_nodesE"></a>

    <a id="_CPPv3N11audio_env_t22audio_a2dp_frame_nodesE"></a> <a id="_CPPv2N11audio_env_t22audio_a2dp_frame_nodesE"></a> <a id="audio_env_t::audio_a2dp_frame_nodes__ring_buffer_node_t"></a> <a id="structaudio__env__t_1af03e14407d616b6a487e8e19512376a1"></a> ring\_buffer\_node\_t audio\_a2dp\_frame\_nodes
    :   A2DP ringbuffer node

    <a id="_CPPv4N11audio_env_t23audio_hints_frame_nodesE"></a>

    <a id="_CPPv3N11audio_env_t23audio_hints_frame_nodesE"></a> <a id="_CPPv2N11audio_env_t23audio_hints_frame_nodesE"></a> <a id="audio_env_t::audio_hints_frame_nodes__ring_buffer_node_t"></a> <a id="structaudio__env__t_1ac97135acb677e58c8f277877176f26b0"></a> ring\_buffer\_node\_t audio\_hints\_frame\_nodes
    :   hints ringbuffer node

    <a id="_CPPv4N11audio_env_t25audio_a2dp_decoder_handleE"></a>

    <a id="_CPPv3N11audio_env_t25audio_a2dp_decoder_handleE"></a> <a id="_CPPv2N11audio_env_t25audio_a2dp_decoder_handleE"></a> <a id="audio_env_t::audio_a2dp_decoder_handle__voidP"></a> <a id="structaudio__env__t_1a21b1c93d013c9db0c50e2a8815cf4a95"></a> void \*audio\_a2dp\_decoder\_handle
    :   address function for A2DP decoder

    <a id="_CPPv4N11audio_env_t29audio_a2dp_frame_nodes_bufferE"></a>

    <a id="_CPPv3N11audio_env_t29audio_a2dp_frame_nodes_bufferE"></a> <a id="_CPPv2N11audio_env_t29audio_a2dp_frame_nodes_bufferE"></a> <a id="audio_env_t::audio_a2dp_frame_nodes_buffer__voidP"></a> <a id="structaudio__env__t_1ab6ae2e49c0437110b2d5621b10b8e818"></a> void \*audio\_a2dp\_frame\_nodes\_buffer
    :   address for A2DP data buffer

    <a id="_CPPv4N11audio_env_t30audio_hints_frame_nodes_bufferE"></a>

    <a id="_CPPv3N11audio_env_t30audio_hints_frame_nodes_bufferE"></a> <a id="_CPPv2N11audio_env_t30audio_hints_frame_nodes_bufferE"></a> <a id="audio_env_t::audio_hints_frame_nodes_buffer__voidP"></a> <a id="structaudio__env__t_1acd24df5a3786e57d25f06f28316b33c1"></a> void \*audio\_hints\_frame\_nodes\_buffer
    :   address for hints data buffer

    <a id="_CPPv4N11audio_env_t26audio_hints_decoder_handleE"></a>

    <a id="_CPPv3N11audio_env_t26audio_hints_decoder_handleE"></a> <a id="_CPPv2N11audio_env_t26audio_hints_decoder_handleE"></a> <a id="audio_env_t::audio_hints_decoder_handle__voidP"></a> <a id="structaudio__env__t_1af99c930f8a12b363d7f347d24ab0f8b0"></a> void \*audio\_hints\_decoder\_handle
    :   address for hints decoder

    <a id="_CPPv4N11audio_env_t24audio_hfp_decoder_handleE"></a>

    <a id="_CPPv3N11audio_env_t24audio_hfp_decoder_handleE"></a> <a id="_CPPv2N11audio_env_t24audio_hfp_decoder_handleE"></a> <a id="audio_env_t::audio_hfp_decoder_handle__voidP"></a> <a id="structaudio__env__t_1a0af13b8b11f90ef262b1f613865ea53a"></a> void \*audio\_hfp\_decoder\_handle
    :   address for voice decoder

    <a id="_CPPv4N11audio_env_t24audio_hfp_encoder_handleE"></a>

    <a id="_CPPv3N11audio_env_t24audio_hfp_encoder_handleE"></a> <a id="_CPPv2N11audio_env_t24audio_hfp_encoder_handleE"></a> <a id="audio_env_t::audio_hfp_encoder_handle__voidP"></a> <a id="structaudio__env__t_1ac4702c83ae7deb157dd7d7f7e94a825e"></a> void \*audio\_hfp\_encoder\_handle
    :   address for voice encoder

    <a id="_CPPv4N11audio_env_t11audio_msg_qE"></a>

    <a id="_CPPv3N11audio_env_t11audio_msg_qE"></a> <a id="_CPPv2N11audio_env_t11audio_msg_qE"></a> <a id="audio_env_t::audio_msg_q__uint32_t"></a> <a id="structaudio__env__t_1a6c2c1b2aaf4e074f72394a46698217a6"></a> uint32\_t audio\_msg\_q
    :   address for AUDIO task message queue

    <a id="_CPPv4N11audio_env_t17audio_task_handleE"></a>

    <a id="_CPPv3N11audio_env_t17audio_task_handleE"></a> <a id="_CPPv2N11audio_env_t17audio_task_handleE"></a> <a id="audio_env_t::audio_task_handle__uint32_t"></a> <a id="structaudio__env__t_1a320e627f9f5b3b1a658fa6bd1d3f05d1"></a> uint32\_t audio\_task\_handle
    :   address for AUDIO task thread

    <a id="_CPPv4N11audio_env_t10voice_infoE"></a>

    <a id="_CPPv3N11audio_env_t10voice_infoE"></a> <a id="_CPPv2N11audio_env_t10voice_infoE"></a> <a id="audio_env_t::voice_info__voice_info_t"></a> <a id="structaudio__env__t_1a6273e47fb2abfceda2abc1ec178a5ebb"></a> [voice\_info\_t](#_CPPv412voice_info_t "voice_info_t") voice\_info
    :   voice information struct @voice\_info\_t

    <a id="_CPPv4N11audio_env_t16decoding_pac_seqE"></a>

    <a id="_CPPv3N11audio_env_t16decoding_pac_seqE"></a> <a id="_CPPv2N11audio_env_t16decoding_pac_seqE"></a> <a id="audio_env_t::decoding_pac_seq__float"></a> <a id="structaudio__env__t_1a9c32dcd2d6c83f5688b75cd902f1ece9"></a> float decoding\_pac\_seq
    :   decoding sequence number

    <a id="_CPPv4N11audio_env_t18decoding_frame_seqE"></a>

    <a id="_CPPv3N11audio_env_t18decoding_frame_seqE"></a> <a id="_CPPv2N11audio_env_t18decoding_frame_seqE"></a> <a id="audio_env_t::decoding_frame_seq__uint32_t"></a> <a id="structaudio__env__t_1affff314afd7c16b9d3fa35d8f22b5d82"></a> uint32\_t decoding\_frame\_seq
    :   decoding frame number

    <a id="_CPPv4N11audio_env_t17music_dma_isr_cntE"></a>

    <a id="_CPPv3N11audio_env_t17music_dma_isr_cntE"></a> <a id="_CPPv2N11audio_env_t17music_dma_isr_cntE"></a> <a id="audio_env_t::music_dma_isr_cnt__uint32_t"></a> <a id="structaudio__env__t_1ac85465a730601bbf30b8501fb0743b4a"></a> uint32\_t music\_dma\_isr\_cnt
    :   DMA ISR count for music

    <a id="_CPPv4N11audio_env_t17voice_dma_isr_cntE"></a>

    <a id="_CPPv3N11audio_env_t17voice_dma_isr_cntE"></a> <a id="_CPPv2N11audio_env_t17voice_dma_isr_cntE"></a> <a id="audio_env_t::voice_dma_isr_cnt__uint32_t"></a> <a id="structaudio__env__t_1a53fca548bf3d7c6e8751d36b599f314b"></a> uint32\_t voice\_dma\_isr\_cnt
    :   DMA ISR count for voice

    <a id="_CPPv4N11audio_env_t17hints_dma_isr_cntE"></a>

    <a id="_CPPv3N11audio_env_t17hints_dma_isr_cntE"></a> <a id="_CPPv2N11audio_env_t17hints_dma_isr_cntE"></a> <a id="audio_env_t::hints_dma_isr_cnt__uint32_t"></a> <a id="structaudio__env__t_1a908ea95b699dc322fddbc3d17bd5d525"></a> uint32\_t hints\_dma\_isr\_cnt
    :   DMA ISR count for hints

    <a id="_CPPv4N11audio_env_t17frames_per_packetE"></a>

    <a id="_CPPv3N11audio_env_t17frames_per_packetE"></a> <a id="_CPPv2N11audio_env_t17frames_per_packetE"></a> <a id="audio_env_t::frames_per_packet__uint32_t"></a> <a id="structaudio__env__t_1a8b91e54806dc534840cec6e225cc4d58"></a> uint32\_t frames\_per\_packet
    :   number of Frames per A2DP media data

    <a id="_CPPv4N11audio_env_t14frames_per_isrE"></a>

    <a id="_CPPv3N11audio_env_t14frames_per_isrE"></a> <a id="_CPPv2N11audio_env_t14frames_per_isrE"></a> <a id="audio_env_t::frames_per_isr__uint32_t"></a> <a id="structaudio__env__t_1a0e83a6dd94142ece5805eb951bcc17d0"></a> uint32\_t frames\_per\_isr
    :   consume frames every dma isr

    <a id="_CPPv4N11audio_env_t14decode_pac_seqE"></a>

    <a id="_CPPv3N11audio_env_t14decode_pac_seqE"></a> <a id="_CPPv2N11audio_env_t14decode_pac_seqE"></a> <a id="audio_env_t::decode_pac_seq__uint16_t"></a> <a id="structaudio__env__t_1aa8b10b9102cba86d35e122693905d104"></a> uint16\_t decode\_pac\_seq
    :   pac dma isr should decode

    <a id="_CPPv4N11audio_env_t16decode_frame_seqE"></a>

    <a id="_CPPv3N11audio_env_t16decode_frame_seqE"></a> <a id="_CPPv2N11audio_env_t16decode_frame_seqE"></a> <a id="audio_env_t::decode_frame_seq__uint16_t"></a> <a id="structaudio__env__t_1aac48ac9111eaac926672d0234b448073"></a> uint16\_t decode\_frame\_seq
    :   frame dma isr should decode

    <a id="_CPPv4N11audio_env_t23continuous_overflow_cntE"></a>

    <a id="_CPPv3N11audio_env_t23continuous_overflow_cntE"></a> <a id="_CPPv2N11audio_env_t23continuous_overflow_cntE"></a> <a id="audio_env_t::continuous_overflow_cnt__uint32_t"></a> <a id="structaudio__env__t_1ab8990c1948aaf81af9b2445e8f9745f8"></a> uint32\_t continuous\_overflow\_cnt
    :   count for continuous fill media data failed

    <a id="_CPPv4N11audio_env_t13underflow_cntE"></a>

    <a id="_CPPv3N11audio_env_t13underflow_cntE"></a> <a id="_CPPv2N11audio_env_t13underflow_cntE"></a> <a id="audio_env_t::underflow_cnt__uint32_t"></a> <a id="structaudio__env__t_1a94c410694d386667edc24ecf2766fb83"></a> uint32\_t underflow\_cnt
    :   count for get filled media data fail

    <a id="_CPPv4N11audio_env_t12slow_pac_cntE"></a>

    <a id="_CPPv3N11audio_env_t12slow_pac_cntE"></a> <a id="_CPPv2N11audio_env_t12slow_pac_cntE"></a> <a id="audio_env_t::slow_pac_cnt__uint32_t"></a> <a id="structaudio__env__t_1a80692bb718dfc75d48c712a14c5e7734"></a> uint32\_t slow\_pac\_cnt
    :   gap for the packect seq which slower than system expected

    <a id="_CPPv4N11audio_env_t14slow_times_cntE"></a>

    <a id="_CPPv3N11audio_env_t14slow_times_cntE"></a> <a id="_CPPv2N11audio_env_t14slow_times_cntE"></a> <a id="audio_env_t::slow_times_cnt__uint32_t"></a> <a id="structaudio__env__t_1a44200bf3c32726581904dab7c3259ad5"></a> uint32\_t slow\_times\_cnt
    :   threshold value for trigger retrigger mechanism

    <a id="_CPPv4N11audio_env_t13retrigger_cntE"></a>

    <a id="_CPPv3N11audio_env_t13retrigger_cntE"></a> <a id="_CPPv2N11audio_env_t13retrigger_cntE"></a> <a id="audio_env_t::retrigger_cnt__uint32_t"></a> <a id="structaudio__env__t_1a9ccdfaa21783ab6c428b8c33316f41a4"></a> uint32\_t retrigger\_cnt
    :   count for retrigger times

    <a id="_CPPv4N11audio_env_t17hint_used_chan_idE"></a>

    <a id="_CPPv3N11audio_env_t17hint_used_chan_idE"></a> <a id="_CPPv2N11audio_env_t17hint_used_chan_idE"></a> <a id="audio_env_t::hint_used_chan_id__uint32_t"></a> <a id="structaudio__env__t_1acfcb94f738e29952fe8f08c890dc1954"></a> uint32\_t hint\_used\_chan\_id
    :   hints used DAC channel ID

    <a id="_CPPv4N11audio_env_t17p_music_fill_buffE"></a>

    <a id="_CPPv3N11audio_env_t17p_music_fill_buffE"></a> <a id="_CPPv2N11audio_env_t17p_music_fill_buffE"></a> <a id="audio_env_t::p_music_fill_buff__uint8_tP"></a> <a id="structaudio__env__t_1afdb1d82af1ce2ba7434b0975a1324e9d"></a> uint8\_t \*p\_music\_fill\_buff
    :   buffer data for music fill data

    <a id="_CPPv4N11audio_env_t17p_hints_fill_buffE"></a>

    <a id="_CPPv3N11audio_env_t17p_hints_fill_buffE"></a> <a id="_CPPv2N11audio_env_t17p_hints_fill_buffE"></a> <a id="audio_env_t::p_hints_fill_buff__uint8_tP"></a> <a id="structaudio__env__t_1a1e036e012af96ffac9b726526517162f"></a> uint8\_t \*p\_hints\_fill\_buff
    :   buffer data for hints fill data

    <a id="_CPPv4N11audio_env_t15music_fill_sizeE"></a>

    <a id="_CPPv3N11audio_env_t15music_fill_sizeE"></a> <a id="_CPPv2N11audio_env_t15music_fill_sizeE"></a> <a id="audio_env_t::music_fill_size__uint32_t"></a> <a id="structaudio__env__t_1a1024b4a0011c960b0c3933f9135ba997"></a> uint32\_t music\_fill\_size
    :   filled data size of music

    <a id="_CPPv4N11audio_env_t15hints_fill_sizeE"></a>

    <a id="_CPPv3N11audio_env_t15hints_fill_sizeE"></a> <a id="_CPPv2N11audio_env_t15hints_fill_sizeE"></a> <a id="audio_env_t::hints_fill_size__uint32_t"></a> <a id="structaudio__env__t_1a4be17f64fd005ad475c3cb1eef70fd2e"></a> uint32\_t hints\_fill\_size
    :   filled data size of hints

    <a id="_CPPv4N11audio_env_t17decoder_error_cntE"></a>

    <a id="_CPPv3N11audio_env_t17decoder_error_cntE"></a> <a id="_CPPv2N11audio_env_t17decoder_error_cntE"></a> <a id="audio_env_t::decoder_error_cnt__uint32_t"></a> <a id="structaudio__env__t_1ac32709fc4c2d8dbf90fb05150f986b28"></a> uint32\_t decoder\_error\_cnt
    :   count for decoder decode error

    <a id="_CPPv4N11audio_env_t8aac_tempE"></a>

    <a id="_CPPv3N11audio_env_t8aac_tempE"></a> <a id="_CPPv2N11audio_env_t8aac_tempE"></a> <a id="audio_env_t::aac_temp__aac_temp_t"></a> <a id="structaudio__env__t_1a0bc7fdf451752ee3bb5a21bfc3981d4a"></a> [aac\_temp\_t](#_CPPv410aac_temp_t "aac_temp_t") aac\_temp
    :   aac temp struc @aac\_temp\_t

    <a id="_CPPv4N11audio_env_t18audio_buffer_nodesE"></a>

    <a id="_CPPv3N11audio_env_t18audio_buffer_nodesE"></a> <a id="_CPPv2N11audio_env_t18audio_buffer_nodesE"></a> <a id="audio_env_t::audio_buffer_nodes__uint16_t"></a> <a id="structaudio__env__t_1a342646fe9fecd50226dbcd88da50faf8"></a> uint16\_t audio\_buffer\_nodes
    :   filled node size of music buffer

    <a id="_CPPv4N11audio_env_t8anc_pathE"></a>

    <a id="_CPPv3N11audio_env_t8anc_pathE"></a> <a id="_CPPv2N11audio_env_t8anc_pathE"></a> <a id="audio_env_t::anc_path__uint32_t"></a> <a id="structaudio__env__t_1a77feaaa797d1d6816f640edc75164537"></a> uint32\_t anc\_path
    :   ANC path index

<a id="macros"></a>

### Macros

<a id="c.AUDIO_SPP_PORT"></a>

<a id="app__audio_8h_1ad252fe23e596d39a8936dc7378a03c83"></a> AUDIO\_SPP\_PORT

<a id="c.AUDIO_SPP_MAX_TX_BUF_SIZE"></a>

<a id="app__audio_8h_1ad959035890d3c164803116ca1645a516"></a> AUDIO\_SPP\_MAX\_TX\_BUF\_SIZE

<a id="c.ANA_EN_ANC"></a>

<a id="app__audio_8h_1a36e1ac8bd4e4068d032fb09d5b178c73"></a> ANA\_EN\_ANC

<a id="c.ANA_EN_AEC"></a>

<a id="app__audio_8h_1ae64ca73a99fed78fb04db74c5bd16271"></a> ANA\_EN\_AEC

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv416audio_msg_type_t"></a>

<a id="_CPPv316audio_msg_type_t"></a> <a id="_CPPv216audio_msg_type_t"></a> <a id="app__audio_8h_1adb9eff1c076e22c8f617c1282b5113f0"></a> enum audio\_msg\_type\_t
:   index of ADUIO task message definition

    *Values:*

    <a id="_CPPv4N16audio_msg_type_t13AUD_MSG_STARTE"></a>

    <a id="_CPPv3N16audio_msg_type_t13AUD_MSG_STARTE"></a> <a id="_CPPv2N16audio_msg_type_t13AUD_MSG_STARTE"></a> <a id="app__audio_8h_1adb9eff1c076e22c8f617c1282b5113f0a19a6937fcb7e9bfeba095792a792cc46"></a> enumerator AUD\_MSG\_START

    <a id="_CPPv4N16audio_msg_type_t21AUD_MSG_RX_MEDIA_DATAE"></a>

    <a id="_CPPv3N16audio_msg_type_t21AUD_MSG_RX_MEDIA_DATAE"></a> <a id="_CPPv2N16audio_msg_type_t21AUD_MSG_RX_MEDIA_DATAE"></a> <a id="app__audio_8h_1adb9eff1c076e22c8f617c1282b5113f0ac7228f5d7a530c9ad5883203c30c7ab9"></a> enumerator AUD\_MSG\_RX\_MEDIA\_DATA

    <a id="_CPPv4N16audio_msg_type_t22AUD_MSG_RX_SPEECH_DATAE"></a>

    <a id="_CPPv3N16audio_msg_type_t22AUD_MSG_RX_SPEECH_DATAE"></a> <a id="_CPPv2N16audio_msg_type_t22AUD_MSG_RX_SPEECH_DATAE"></a> <a id="app__audio_8h_1adb9eff1c076e22c8f617c1282b5113f0ac881c4344ba30b0dc1dd1c8824e4006a"></a> enumerator AUD\_MSG\_RX\_SPEECH\_DATA

    <a id="_CPPv4N16audio_msg_type_t20AUD_MSG_RX_HINT_DATAE"></a>

    <a id="_CPPv3N16audio_msg_type_t20AUD_MSG_RX_HINT_DATAE"></a> <a id="_CPPv2N16audio_msg_type_t20AUD_MSG_RX_HINT_DATAE"></a> <a id="app__audio_8h_1adb9eff1c076e22c8f617c1282b5113f0ae6427f77ec3f85d80a391a67f715fa61"></a> enumerator AUD\_MSG\_RX\_HINT\_DATA

    <a id="_CPPv4N16audio_msg_type_t22AUD_MSG_TX_SPEECH_DATAE"></a>

    <a id="_CPPv3N16audio_msg_type_t22AUD_MSG_TX_SPEECH_DATAE"></a> <a id="_CPPv2N16audio_msg_type_t22AUD_MSG_TX_SPEECH_DATAE"></a> <a id="app__audio_8h_1adb9eff1c076e22c8f617c1282b5113f0a574dd951974b7ad469c2007df803dfdf"></a> enumerator AUD\_MSG\_TX\_SPEECH\_DATA

    <a id="_CPPv4N16audio_msg_type_t19AUD_MSG_TX_AEC_DATAE"></a>

    <a id="_CPPv3N16audio_msg_type_t19AUD_MSG_TX_AEC_DATAE"></a> <a id="_CPPv2N16audio_msg_type_t19AUD_MSG_TX_AEC_DATAE"></a> <a id="app__audio_8h_1adb9eff1c076e22c8f617c1282b5113f0a5fb3680bf33e401d9a9899bc7b7fb562"></a> enumerator AUD\_MSG\_TX\_AEC\_DATA

    <a id="_CPPv4N16audio_msg_type_t21AUD_MSG_MUSIC_TRIGGERE"></a>

    <a id="_CPPv3N16audio_msg_type_t21AUD_MSG_MUSIC_TRIGGERE"></a> <a id="_CPPv2N16audio_msg_type_t21AUD_MSG_MUSIC_TRIGGERE"></a> <a id="app__audio_8h_1adb9eff1c076e22c8f617c1282b5113f0a17ec7828fc5ebd304751f526772acf0c"></a> enumerator AUD\_MSG\_MUSIC\_TRIGGER

    <a id="_CPPv4N16audio_msg_type_t20AUD_MSG_CALL_TRIGGERE"></a>

    <a id="_CPPv3N16audio_msg_type_t20AUD_MSG_CALL_TRIGGERE"></a> <a id="_CPPv2N16audio_msg_type_t20AUD_MSG_CALL_TRIGGERE"></a> <a id="app__audio_8h_1adb9eff1c076e22c8f617c1282b5113f0a89a8923815d93ed11e00e8f4db811b36"></a> enumerator AUD\_MSG\_CALL\_TRIGGER

    <a id="_CPPv4N16audio_msg_type_t16AUD_MSG_SHUTDOWNE"></a>

    <a id="_CPPv3N16audio_msg_type_t16AUD_MSG_SHUTDOWNE"></a> <a id="_CPPv2N16audio_msg_type_t16AUD_MSG_SHUTDOWNE"></a> <a id="app__audio_8h_1adb9eff1c076e22c8f617c1282b5113f0aab279f2cf163948bf2cf0211568b3e0d"></a> enumerator AUD\_MSG\_SHUTDOWN

    <a id="_CPPv4N16audio_msg_type_t19AUD_MSG_ANC_FADE_INE"></a>

    <a id="_CPPv3N16audio_msg_type_t19AUD_MSG_ANC_FADE_INE"></a> <a id="_CPPv2N16audio_msg_type_t19AUD_MSG_ANC_FADE_INE"></a> <a id="app__audio_8h_1adb9eff1c076e22c8f617c1282b5113f0a2753eddd371f5aa8caecc9cbaae8e4e0"></a> enumerator AUD\_MSG\_ANC\_FADE\_IN

    <a id="_CPPv4N16audio_msg_type_t14AUD_MSG_ANC_ONE"></a>

    <a id="_CPPv3N16audio_msg_type_t14AUD_MSG_ANC_ONE"></a> <a id="_CPPv2N16audio_msg_type_t14AUD_MSG_ANC_ONE"></a> <a id="app__audio_8h_1adb9eff1c076e22c8f617c1282b5113f0a2d71e93dd4f042dee6749f33d19bb4df"></a> enumerator AUD\_MSG\_ANC\_ON

    <a id="_CPPv4N16audio_msg_type_t21AUD_MSG_ANC_TRANSPANTE"></a>

    <a id="_CPPv3N16audio_msg_type_t21AUD_MSG_ANC_TRANSPANTE"></a> <a id="_CPPv2N16audio_msg_type_t21AUD_MSG_ANC_TRANSPANTE"></a> <a id="app__audio_8h_1adb9eff1c076e22c8f617c1282b5113f0a359294567e2a2017221c453c6e39a020"></a> enumerator AUD\_MSG\_ANC\_TRANSPANT

    <a id="_CPPv4N16audio_msg_type_t15AUD_MSG_ANC_OFFE"></a>

    <a id="_CPPv3N16audio_msg_type_t15AUD_MSG_ANC_OFFE"></a> <a id="_CPPv2N16audio_msg_type_t15AUD_MSG_ANC_OFFE"></a> <a id="app__audio_8h_1adb9eff1c076e22c8f617c1282b5113f0a3c7e8c43783c80050b34ff6a874c6034"></a> enumerator AUD\_MSG\_ANC\_OFF

    <a id="_CPPv4N16audio_msg_type_t18AUD_MSG_PLAY_HINTSE"></a>

    <a id="_CPPv3N16audio_msg_type_t18AUD_MSG_PLAY_HINTSE"></a> <a id="_CPPv2N16audio_msg_type_t18AUD_MSG_PLAY_HINTSE"></a> <a id="app__audio_8h_1adb9eff1c076e22c8f617c1282b5113f0ab58b34807342c9943f25cf51686e57e1"></a> enumerator AUD\_MSG\_PLAY\_HINTS

    <a id="_CPPv4N16audio_msg_type_t11AUD_MSG_ENDE"></a>

    <a id="_CPPv3N16audio_msg_type_t11AUD_MSG_ENDE"></a> <a id="_CPPv2N16audio_msg_type_t11AUD_MSG_ENDE"></a> <a id="app__audio_8h_1adb9eff1c076e22c8f617c1282b5113f0a82591becd1b0cdd99057ac7d085f92ce"></a> enumerator AUD\_MSG\_END

<a id="_CPPv420audio_trigger_type_t"></a>

<a id="_CPPv320audio_trigger_type_t"></a> <a id="_CPPv220audio_trigger_type_t"></a> <a id="app__audio_8h_1a64240e3e2a8aa98f1ecfa0ae8c1c89c5"></a> enum audio\_trigger\_type\_t
:   index of audio trigger type definition

    *Values:*

    <a id="_CPPv4N20audio_trigger_type_t20DMA_HALF_ISR_TRIGGERE"></a>

    <a id="_CPPv3N20audio_trigger_type_t20DMA_HALF_ISR_TRIGGERE"></a> <a id="_CPPv2N20audio_trigger_type_t20DMA_HALF_ISR_TRIGGERE"></a> <a id="app__audio_8h_1a64240e3e2a8aa98f1ecfa0ae8c1c89c5a24d6f9e3cbb60db6be6d216695319a0d"></a> enumerator DMA\_HALF\_ISR\_TRIGGER

    <a id="_CPPv4N20audio_trigger_type_t22DMA_FINISH_ISR_TRIGGERE"></a>

    <a id="_CPPv3N20audio_trigger_type_t22DMA_FINISH_ISR_TRIGGERE"></a> <a id="_CPPv2N20audio_trigger_type_t22DMA_FINISH_ISR_TRIGGERE"></a> <a id="app__audio_8h_1a64240e3e2a8aa98f1ecfa0ae8c1c89c5aa0058452e09343d5d3cfc65c11e5ec7e"></a> enumerator DMA\_FINISH\_ISR\_TRIGGER

    <a id="_CPPv4N20audio_trigger_type_t19BT_DATA_RCV_TRIGGERE"></a>

    <a id="_CPPv3N20audio_trigger_type_t19BT_DATA_RCV_TRIGGERE"></a> <a id="_CPPv2N20audio_trigger_type_t19BT_DATA_RCV_TRIGGERE"></a> <a id="app__audio_8h_1a64240e3e2a8aa98f1ecfa0ae8c1c89c5aa095d363c4ac7447c8d0c2e345023a5e"></a> enumerator BT\_DATA\_RCV\_TRIGGER

    <a id="_CPPv4N20audio_trigger_type_t18AUDIO_TRIGGER_NULLE"></a>

    <a id="_CPPv3N20audio_trigger_type_t18AUDIO_TRIGGER_NULLE"></a> <a id="_CPPv2N20audio_trigger_type_t18AUDIO_TRIGGER_NULLE"></a> <a id="app__audio_8h_1a64240e3e2a8aa98f1ecfa0ae8c1c89c5ab352d52e5461f59aa4b67c86f5844b77"></a> enumerator AUDIO\_TRIGGER\_NULL

<a id="_CPPv48PLC_MODE"></a>

<a id="_CPPv38PLC_MODE"></a> <a id="_CPPv28PLC_MODE"></a> <a id="app__audio_8h_1afece6fbcf599c23626563f4867a74e4a"></a> enum PLC\_MODE
:   PLC mode index definition.

    *Values:*

    <a id="_CPPv4N8PLC_MODE13PLC_MODE_NULLE"></a>

    <a id="_CPPv3N8PLC_MODE13PLC_MODE_NULLE"></a> <a id="_CPPv2N8PLC_MODE13PLC_MODE_NULLE"></a> <a id="app__audio_8h_1afece6fbcf599c23626563f4867a74e4aa89334e494555c2355e29aa4d4b65f7ce"></a> enumerator PLC\_MODE\_NULL
    :   PLC for NULL

    <a id="_CPPv4N8PLC_MODE13PLC_MODE_CVSDE"></a>

    <a id="_CPPv3N8PLC_MODE13PLC_MODE_CVSDE"></a> <a id="_CPPv2N8PLC_MODE13PLC_MODE_CVSDE"></a> <a id="app__audio_8h_1afece6fbcf599c23626563f4867a74e4aa387c16c2abb9d21c314be1747ea42a27"></a> enumerator PLC\_MODE\_CVSD
    :   PLC for CVSD

    <a id="_CPPv4N8PLC_MODE13PLC_MODE_MSBCE"></a>

    <a id="_CPPv3N8PLC_MODE13PLC_MODE_MSBCE"></a> <a id="_CPPv2N8PLC_MODE13PLC_MODE_MSBCE"></a> <a id="app__audio_8h_1afece6fbcf599c23626563f4867a74e4aad835bc8c53862d0848fad324a5d07175"></a> enumerator PLC\_MODE\_MSBC
    :   PLC for mSBC
