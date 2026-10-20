---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/api-reference/multi_media/bk_jpegdec_sw.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="jpegdec-apis"></a>

# JPEGDEC APIs

重要

The JPEGDEC API v1.0 is the lastest stable JPEGDEC APIs. All new applications should use JPEGDEC API v1.0. This component is software decode not hardware decode

<a id="jpegdec-api-categories"></a>

## JPEGDEC API Categories

Most of JPEGDEC APIs can be categoried as:

> - JPEGDEC APIs
>
>   The common APIs are prefixed with bk\_jpeg\_dec\_sw, e.g. bk\_jpeg\_dec\_sw\_init() etc.

JPEGDEC APIs:
:   - [`bk_jpeg_dec_sw_init()`](#_CPPv419bk_jpeg_dec_sw_initPv8uint32_t "bk_jpeg_dec_sw_init") \- init jpeg decode software module
    - [`bk_jpeg_dec_sw_deinit()`](#_CPPv421bk_jpeg_dec_sw_deinitv "bk_jpeg_dec_sw_deinit") \- deinit jpeg decode software module
    - [`bk_jpeg_dec_sw_start()`](#_CPPv420bk_jpeg_dec_sw_start7uint8_tP7uint8_tP7uint8_t8uint32_t8uint32_tP17sw_jpeg_dec_res_t "bk_jpeg_dec_sw_start") \- excute jpeg decode
    - [`bk_jpeg_dec_sw_register_finish_callback()`](#_CPPv439bk_jpeg_dec_sw_register_finish_callbackPv "bk_jpeg_dec_sw_register_finish_callback") \- register jpeg decode finish callback
    - [`bk_jpeg_dec_sw_start_one_time()`](#_CPPv429bk_jpeg_dec_sw_start_one_time7uint8_tP7uint8_tP7uint8_t8uint32_t8uint32_tP17sw_jpeg_dec_res_t7uint8_t16JD_FORMAT_OUTPUT14media_rotate_tP7uint8_tP7uint8_t "bk_jpeg_dec_sw_start_one_time") \- excute jpeg decode without relying on initalization

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [jpeg\_decode\_sw.h](https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/_header_files/bk_idk/include/modules/jpeg_decode_sw.h)

<a id="functions"></a>

### Functions

<a id="_CPPv419bk_jpeg_dec_sw_initPv8uint32_t"></a>

<a id="_CPPv319bk_jpeg_dec_sw_initPv8uint32_t"></a> <a id="_CPPv219bk_jpeg_dec_sw_initPv8uint32_t"></a> <a id="bk_jpeg_dec_sw_init__voidP.uint32_t"></a> <a id="jpeg__decode__sw_8h_1a7f06bfe0f62d6d74437ae45597a8f309"></a> bk\_err\_t bk\_jpeg\_dec\_sw\_init(void \*jd\_in, uint32\_t len)
:   JPEG\_DEC APIs Version 1.0.

    Init the jpeg\_dec

    This API init the jpeg\_dec

    - config jpeg\_dec image resoult, and simple\_rate
    - malloc buffer for jpeg\_dec

    **Attention**
    :   1\. only for software jpeg\_dec

    参数
    :   - **jd\_in** – inter buffer
        - **len** – buffer length

    返回
    :   - BK\_OK: succeed
        - other: errors.

<a id="_CPPv421bk_jpeg_dec_sw_deinitv"></a>

<a id="_CPPv321bk_jpeg_dec_sw_deinitv"></a> <a id="_CPPv221bk_jpeg_dec_sw_deinitv"></a> <a id="bk_jpeg_dec_sw_deinit__void"></a> <a id="jpeg__decode__sw_8h_1a1e772fdd541bd135ea967b06e06a06e5"></a> bk\_err\_t bk\_jpeg\_dec\_sw\_deinit(void)
:   Deinit the jpeg\_dec.

    This API deinit the jpeg\_dec

    - clear all configure for jpeg\_dec
    - free buffer for jpeg\_dec

    **Attention**
    :   1\. only for software jpeg\_dec

    返回
    :   - BK\_OK: succeed
        - other: errors.

<a id="_CPPv420bk_jpeg_dec_sw_start7uint8_tP7uint8_tP7uint8_t8uint32_t8uint32_tP17sw_jpeg_dec_res_t"></a>

<a id="_CPPv320bk_jpeg_dec_sw_start7uint8_tP7uint8_tP7uint8_t8uint32_t8uint32_tP17sw_jpeg_dec_res_t"></a> <a id="_CPPv220bk_jpeg_dec_sw_start7uint8_tP7uint8_tP7uint8_t8uint32_t8uint32_tP17sw_jpeg_dec_res_t"></a> <a id="bk_jpeg_dec_sw_start__uint8_t.uint8_tP.uint8_tP.uint32_t.uint32_t.sw_jpeg_dec_res_tP"></a> <a id="jpeg__decode__sw_8h_1a8f9fb7e3a1e8b04ee72ff5eb4461496a"></a> bk\_err\_t bk\_jpeg\_dec\_sw\_start(uint8\_t decode\_type, uint8\_t \*src\_buf, uint8\_t \*dst\_buf, uint32\_t jpeg\_size, uint32\_t outbuf\_size, sw\_jpeg\_dec\_res\_t \*result)
:   jpeg\_decoder\_fun

    This API jpeg\_decoder\_fun

    - jpeg\_prepare for jpeg\_dec
    - start jpeg\_dec

    **Attention**
    :   1\. only for software jpeg\_dec

    **Attention**
    :   2\. outbuf\_size only work for decode\_type\=0, decode by frame, and outbuf size must 2 times for decode 16line

    参数
    :   - **decode\_type** – 0:decode by line, one time decode 16line; 1:decode by frame
        - **src\_buf** – jpeg image address
        - **dst\_buf** – decode output buffer address
        - **outbuf\_size** – decode output buffer size
        - **result** – decode image info

    返回
    :   - BK\_OK: succeed
        - other: errors.

<a id="_CPPv425bk_jpeg_dec_sw_start_linev"></a>

<a id="_CPPv325bk_jpeg_dec_sw_start_linev"></a> <a id="_CPPv225bk_jpeg_dec_sw_start_linev"></a> <a id="bk_jpeg_dec_sw_start_line__void"></a> <a id="jpeg__decode__sw_8h_1a689ea8785c549c1fc05f6c4f1c0aa834"></a> bk\_err\_t bk\_jpeg\_dec\_sw\_start\_line(void)
:   start line jpeg decode sw

    This API is used to decode go on

    **Attention**
    :   1\. only for software jpeg\_dec by line

    返回
    :   - BK\_OK: succeed
        - other: errors.

<a id="_CPPv420bk_jpeg_get_img_info8uint32_tP7uint8_tP17sw_jpeg_dec_res_t"></a>

<a id="_CPPv320bk_jpeg_get_img_info8uint32_tP7uint8_tP17sw_jpeg_dec_res_t"></a> <a id="_CPPv220bk_jpeg_get_img_info8uint32_tP7uint8_tP17sw_jpeg_dec_res_t"></a> <a id="bk_jpeg_get_img_info__uint32_t.uint8_tP.sw_jpeg_dec_res_tP"></a> <a id="jpeg__decode__sw_8h_1a58a08286fb886b2399ae6114bab98650"></a> bk\_err\_t bk\_jpeg\_get\_img\_info(uint32\_t frame\_size, uint8\_t \*src\_buf, sw\_jpeg\_dec\_res\_t \*result)
:   jpeg\_decoder\_fun

    This API is used to get img width and size

    **Attention**
    :   1\. only for software jpeg\_dec

    参数
    :   - **frame\_size** – input image size
        - **src\_buf** – jpeg image address
        - **result** – decode image info

    返回
    :   - BK\_OK: succeed
        - other: errors.

<a id="_CPPv439bk_jpeg_dec_sw_register_finish_callbackPv"></a>

<a id="_CPPv339bk_jpeg_dec_sw_register_finish_callbackPv"></a> <a id="_CPPv239bk_jpeg_dec_sw_register_finish_callbackPv"></a> <a id="bk_jpeg_dec_sw_register_finish_callback__voidP"></a> <a id="jpeg__decode__sw_8h_1abd2a52c16af84f1190b6e99609c08be1"></a> void bk\_jpeg\_dec\_sw\_register\_finish\_callback(void \*cb)
:   jpegdec register finish icallback\_func

    This API jpeg\_decoder\_fun, the callback function wiil execute when decode success

    **Attention**
    :   1\. only for software jpeg\_dec

    参数
    :   **cb** – finish jpeg\_dec callback function

    返回

<a id="_CPPv429bk_jpeg_dec_sw_start_one_time7uint8_tP7uint8_tP7uint8_t8uint32_t8uint32_tP17sw_jpeg_dec_res_t7uint8_t16JD_FORMAT_OUTPUT14media_rotate_tP7uint8_tP7uint8_t"></a>

<a id="_CPPv329bk_jpeg_dec_sw_start_one_time7uint8_tP7uint8_tP7uint8_t8uint32_t8uint32_tP17sw_jpeg_dec_res_t7uint8_t16JD_FORMAT_OUTPUT14media_rotate_tP7uint8_tP7uint8_t"></a> <a id="_CPPv229bk_jpeg_dec_sw_start_one_time7uint8_tP7uint8_tP7uint8_t8uint32_t8uint32_tP17sw_jpeg_dec_res_t7uint8_t16JD_FORMAT_OUTPUT14media_rotate_tP7uint8_tP7uint8_t"></a> <a id="bk_jpeg_dec_sw_start_one_time__uint8_t.uint8_tP.uint8_tP.uint32_t.uint32_t.sw_jpeg_dec_res_tP.uint8_t.JD_FORMAT_OUTPUT.media_rotate_t.uint8_tP.uint8_tP"></a> <a id="jpeg__decode__sw_8h_1a2cf9f979dd5cc15722639e11bb253354"></a> bk\_err\_t bk\_jpeg\_dec\_sw\_start\_one\_time(uint8\_t decode\_type, uint8\_t \*src\_buf, uint8\_t \*dst\_buf, uint32\_t jpeg\_size, uint32\_t outbuf\_size, sw\_jpeg\_dec\_res\_t \*result, uint8\_t scale, JD\_FORMAT\_OUTPUT format, media\_rotate\_t rotate\_angle, uint8\_t \*work\_buffer, uint8\_t \*rotate\_buffer)
:   jpeg\_decoder\_fun

    This API jpeg\_decoder\_fun

    - jpeg\_prepare for jpeg\_dec
    - start jpeg\_dec

    **Attention**
    :   1\. only for software jpeg\_dec

    **Attention**
    :   2\. outbuf\_size only work for decode\_type\=0, decode by frame, and outbuf size must 2 times for decode 16line

    参数
    :   - **decode\_type** – 0:decode by line, one time decode 16line; 1:decode by frame
        - **src\_buf** – jpeg image address
        - **dst\_buf** – decode output buffer address
        - **outbuf\_size** – decode output buffer size
        - **result** – decode image info
        - **scaling** – of decode image
        - **format** – of decode image
        - **rotate\_angle** – of decode image
        - **work\_buffer** – inter workbuffer
        - **rotate\_buffer** – rotate need buffer

    返回
    :   - BK\_OK: succeed
        - other: errors.

<a id="api-typedefs"></a>

## API Typedefs
