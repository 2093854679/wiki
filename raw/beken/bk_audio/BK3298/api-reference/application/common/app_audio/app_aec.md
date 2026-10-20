---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_audio/app_aec.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="aec-application-functions"></a>

# AEC Application Functions

<a id="app-aec-api-brief"></a>

## APP\_AEC API Brief

| Application | Brief |
| --- | --- |
| [`app_aec_init()`](#_CPPv412app_aec_init7int32_t8uint32_t "app_aec_init") | application for AEC initialize |
| [`app_aec_deinit()`](#_CPPv414app_aec_deinitv "app_aec_deinit") | application for reset app\_aec\_env environment variable |
| [`app_aec_process_handle()`](#_CPPv422app_aec_process_handlev "app_aec_process_handle") | handle function of process AEC data |
| [`app_aec_fill_rin_buf()`](#_CPPv420app_aec_fill_rin_bufP7uint8_t8uint32_t "app_aec_fill_rin_buf") | fill output PCM data or rx\_sco\_data to p\_aec\_env-\>aec\_rin\_rb |
| [`app_aec_read_out_buf()`](#_CPPv420app_aec_read_out_bufP7uint8_t8uint32_t "app_aec_read_out_buf") | read out from p\_aec\_env-\>aec\_out\_rb |
| [`app_aec_get_fill_buffer_size()`](#_CPPv428app_aec_get_fill_buffer_sizev "app_aec_get_fill_buffer_size") | get filled size of app\_aec\_env.aec\_out\_rb ring buffer |

<a id="app-aec-api-reference"></a>

## APP\_AEC API Reference

<a id="header-file"></a>

### Header File

- [common/app\_audio/app\_aec.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_audio/app_aec.h)

<a id="functions"></a>

### Functions

<a id="_CPPv412app_aec_init7int32_t8uint32_t"></a>

<a id="_CPPv312app_aec_init7int32_t8uint32_t"></a> <a id="_CPPv212app_aec_init7int32_t8uint32_t"></a> <a id="app_aec_init__int32_t.uint32_t"></a> <a id="app__aec_8h_1a260e5b28f1dc1459244b9695e531fc6c"></a> void app\_aec\_init(int32\_t sample\_rate, uint32\_t adc\_enable\_ch)
:   application for AEC initialize

    参数:
    :   - **sample\_rate** – **\[in\]** microphone sample rate(etc 16000,8000)
        - **adc\_enable\_ch** – **\[in\]** microphone channel aec(acoustic echo cancellation) enable

    返回:
    :   N/A

<a id="_CPPv414app_aec_deinitv"></a>

<a id="_CPPv314app_aec_deinitv"></a> <a id="_CPPv214app_aec_deinitv"></a> <a id="app_aec_deinit__void"></a> <a id="app__aec_8h_1a97e94f134699059ee48912baab8b7d9d"></a> void app\_aec\_deinit(void)
:   application for reset app\_aec\_env environment variable

    返回:
    :   N/A

<a id="_CPPv422app_aec_process_handlev"></a>

<a id="_CPPv322app_aec_process_handlev"></a> <a id="_CPPv222app_aec_process_handlev"></a> <a id="app_aec_process_handle__void"></a> <a id="app__aec_8h_1a8801ae2b56b4d74f8679db37aac86f8d"></a> void app\_aec\_process\_handle(void)
:   handle function of process AEC data

    返回:
    :   N/A

<a id="_CPPv420app_aec_fill_rin_bufP7uint8_t8uint32_t"></a>

<a id="_CPPv320app_aec_fill_rin_bufP7uint8_t8uint32_t"></a> <a id="_CPPv220app_aec_fill_rin_bufP7uint8_t8uint32_t"></a> <a id="app_aec_fill_rin_buf__uint8_tP.uint32_t"></a> <a id="app__aec_8h_1ab5c62add0406a64895517af5abeadc10"></a> void app\_aec\_fill\_rin\_buf(uint8\_t \*buff, uint32\_t len)
:   fill output PCM data or rx\_sco\_data to p\_aec\_env-\>aec\_rin\_rb

    参数:
    :   - **buff** – **\[in\]** buffer to be write from
        - **len** – **\[in\]** write size

    返回:
    :   N/A

<a id="_CPPv420app_aec_read_out_bufP7uint8_t8uint32_t"></a>

<a id="_CPPv320app_aec_read_out_bufP7uint8_t8uint32_t"></a> <a id="_CPPv220app_aec_read_out_bufP7uint8_t8uint32_t"></a> <a id="app_aec_read_out_buf__uint8_tP.uint32_t"></a> <a id="app__aec_8h_1a289e04078735b79136ff4612a93cedfa"></a> uint32\_t app\_aec\_read\_out\_buf(uint8\_t \*buff, uint32\_t len)
:   read out from p\_aec\_env-\>aec\_out\_rb

    Data produced after the AEC to write p\_aec\_env-\>aec\_out\_rb ring buffer

    参数:
    :   - **buff** – **\[out\]** buffer to be read into
        - **len** – **\[out\]** read size

    返回:
    :   actually read size

<a id="_CPPv428app_aec_get_fill_buffer_sizev"></a>

<a id="_CPPv328app_aec_get_fill_buffer_sizev"></a> <a id="_CPPv228app_aec_get_fill_buffer_sizev"></a> <a id="app_aec_get_fill_buffer_size__void"></a> <a id="app__aec_8h_1a6c8745e97eb7d124b415b4824d830f14"></a> uint32\_t app\_aec\_get\_fill\_buffer\_size(void)
:   get filled size of app\_aec\_env.aec\_out\_rb ring buffer

    返回:
    :   the filled size of ring buffer

<a id="structures"></a>

### Structures

<a id="_CPPv413app_aec_env_t"></a>

<a id="_CPPv313app_aec_env_t"></a> <a id="_CPPv213app_aec_env_t"></a> <a id="app_aec_env_t"></a> <a id="structapp__aec__env__t"></a> struct app\_aec\_env\_t

<a id="macros"></a>

### Macros

<a id="c.AEC_ROM"></a>

<a id="app__aec_8h_1a39dbe87196447b8f88f2adc44c5f8121"></a> AEC\_ROM

<a id="c.AEC_FLASH"></a>

<a id="app__aec_8h_1a2655cf895f718ec803e3d2b4c44504b1"></a> AEC\_FLASH

<a id="c.AEC_MIX"></a>

<a id="app__aec_8h_1ac498e429c02c61f338373a20b2d31a5c"></a> AEC\_MIX

<a id="c.AEC_VER"></a>

<a id="app__aec_8h_1a8c1c61e4894e9c13697b019667fd4ea0"></a> AEC\_VER

<a id="c.AEC_FRAME_LEN"></a>

<a id="app__aec_8h_1ae7fb5e40cc3b54bac4f71e8bbfdd4352"></a> AEC\_FRAME\_LEN

<a id="c.TEST1_START"></a>

<a id="app__aec_8h_1a9bccbeccdc50972a5a2dc7b005f6fd24"></a> TEST1\_START

<a id="c.TEST1_STOP"></a>

<a id="app__aec_8h_1a157ba558dbdbc3337ed185b223ccc355"></a> TEST1\_STOP

<a id="c.TEST2_START"></a>

<a id="app__aec_8h_1ab377915d32aea77ddc40f7a66d82cf6c"></a> TEST2\_START

<a id="c.TEST2_STOP"></a>

<a id="app__aec_8h_1a694e03129187c03d21796f82bcdf0313"></a> TEST2\_STOP
