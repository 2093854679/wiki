# JPEGDEC APIs[](#jpegdec-apis "永久链接至标题")


重要

The JPEGDEC API v1.0 is the lastest stable JPEGDEC APIs. All new applications should use JPEGDEC API v1.0. This component is software decode not hardware decode


## JPEGDEC API Categories[](#jpegdec-api-categories "永久链接至标题")

Most of JPEGDEC APIs can be categoried as:

> - JPEGDEC APIs
>
>   The common APIs are prefixed with bk_jpeg_dec_sw, e.g. bk_jpeg_dec_sw_init() etc.

JPEGDEC APIs:
:   - [`bk_jpeg_dec_sw_init()`](#_CPPv419bk_jpeg_dec_sw_initPv8uint32_t "bk_jpeg_dec_sw_init") - init jpeg decode software module

    - [`bk_jpeg_dec_sw_deinit()`](#_CPPv421bk_jpeg_dec_sw_deinitv "bk_jpeg_dec_sw_deinit") - deinit jpeg decode software module

    - [`bk_jpeg_dec_sw_start()`](#_CPPv420bk_jpeg_dec_sw_start7uint8_tP7uint8_tP7uint8_t8uint32_t8uint32_tP17sw_jpeg_dec_res_t "bk_jpeg_dec_sw_start") - excute jpeg decode

    - [`bk_jpeg_dec_sw_register_finish_callback()`](#_CPPv439bk_jpeg_dec_sw_register_finish_callbackPv "bk_jpeg_dec_sw_register_finish_callback") - register jpeg decode finish callback

    - [`bk_jpeg_dec_sw_start_one_time()`](#_CPPv429bk_jpeg_dec_sw_start_one_time7uint8_tP7uint8_tP7uint8_t8uint32_t8uint32_tP17sw_jpeg_dec_res_t7uint8_t16JD_FORMAT_OUTPUT14media_rotate_tP7uint8_tP7uint8_t "bk_jpeg_dec_sw_start_one_time") - excute jpeg decode without relying on initalization


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [jpeg_decode_sw.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/jpeg_decode_sw.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/jpeg_decode_sw.h")


### Functions[](#functions "永久链接至标题")

bk_err_t bk_jpeg_dec_sw_init(void *jd_in, uint32_t len)[](#_CPPv419bk_jpeg_dec_sw_initPv8uint32_t "永久链接至目标")
:   JPEG_DEC APIs Version 1.0.

    Init the jpeg_dec

    This API init the jpeg_dec


    - config jpeg_dec image resoult, and simple_rate

    - malloc buffer for jpeg_dec


    **Attention**
    :   1. only for software jpeg_dec

    参数
    :   - **jd_in** – inter buffer

        - **len** – buffer length

    返回
    :   - BK_OK: succeed

        - other: errors.

bk_err_t bk_jpeg_dec_sw_deinit(void)[](#_CPPv421bk_jpeg_dec_sw_deinitv "永久链接至目标")
:   Deinit the jpeg_dec.

    This API deinit the jpeg_dec


    - clear all configure for jpeg_dec

    - free buffer for jpeg_dec


    **Attention**
    :   1. only for software jpeg_dec

    返回
    :   - BK_OK: succeed

        - other: errors.

bk_err_t bk_jpeg_dec_sw_start(uint8_t decode_type, uint8_t *src_buf, uint8_t *dst_buf, uint32_t jpeg_size, uint32_t outbuf_size, sw_jpeg_dec_res_t *result)[](#_CPPv420bk_jpeg_dec_sw_start7uint8_tP7uint8_tP7uint8_t8uint32_t8uint32_tP17sw_jpeg_dec_res_t "永久链接至目标")
:   jpeg_decoder_fun

    This API jpeg_decoder_fun


    - jpeg_prepare for jpeg_dec

    - start jpeg_dec


    **Attention**
    :   1. only for software jpeg_dec


    **Attention**
    :   2. outbuf_size only work for decode_type=0, decode by frame, and outbuf size must 2 times for decode 16line

    参数
    :   - **decode_type** – 0:decode by line, one time decode 16line; 1:decode by frame

        - **src_buf** – jpeg image address

        - **dst_buf** – decode output buffer address

        - **outbuf_size** – decode output buffer size

        - **result** – decode image info

    返回
    :   - BK_OK: succeed

        - other: errors.

bk_err_t bk_jpeg_dec_sw_start_line(void)[](#_CPPv425bk_jpeg_dec_sw_start_linev "永久链接至目标")
:   start line jpeg decode sw

    This API is used to decode go on


    **Attention**
    :   1. only for software jpeg_dec by line

    返回
    :   - BK_OK: succeed

        - other: errors.

bk_err_t bk_jpeg_get_img_info(uint32_t frame_size, uint8_t *src_buf, sw_jpeg_dec_res_t *result)[](#_CPPv420bk_jpeg_get_img_info8uint32_tP7uint8_tP17sw_jpeg_dec_res_t "永久链接至目标")
:   jpeg_decoder_fun

    This API is used to get img width and size


    **Attention**
    :   1. only for software jpeg_dec

    参数
    :   - **frame_size** – input image size

        - **src_buf** – jpeg image address

        - **result** – decode image info

    返回
    :   - BK_OK: succeed

        - other: errors.

void bk_jpeg_dec_sw_register_finish_callback(void *cb)[](#_CPPv439bk_jpeg_dec_sw_register_finish_callbackPv "永久链接至目标")
:   jpegdec register finish icallback_func

    This API jpeg_decoder_fun, the callback function wiil execute when decode success


    **Attention**
    :   1. only for software jpeg_dec

    参数
    :   **cb** – finish jpeg_dec callback function

    返回

bk_err_t bk_jpeg_dec_sw_start_one_time(uint8_t decode_type, uint8_t *src_buf, uint8_t *dst_buf, uint32_t jpeg_size, uint32_t outbuf_size, sw_jpeg_dec_res_t *result, uint8_t scale, JD_FORMAT_OUTPUT format, media_rotate_t rotate_angle, uint8_t *work_buffer, uint8_t *rotate_buffer)[](#_CPPv429bk_jpeg_dec_sw_start_one_time7uint8_tP7uint8_tP7uint8_t8uint32_t8uint32_tP17sw_jpeg_dec_res_t7uint8_t16JD_FORMAT_OUTPUT14media_rotate_tP7uint8_tP7uint8_t "永久链接至目标")
:   jpeg_decoder_fun

    This API jpeg_decoder_fun


    - jpeg_prepare for jpeg_dec

    - start jpeg_dec


    **Attention**
    :   1. only for software jpeg_dec


    **Attention**
    :   2. outbuf_size only work for decode_type=0, decode by frame, and outbuf size must 2 times for decode 16line

    参数
    :   - **decode_type** – 0:decode by line, one time decode 16line; 1:decode by frame

        - **src_buf** – jpeg image address

        - **dst_buf** – decode output buffer address

        - **outbuf_size** – decode output buffer size

        - **result** – decode image info

        - **scaling** – of decode image

        - **format** – of decode image

        - **rotate_angle** – of decode image

        - **work_buffer** – inter workbuffer

        - **rotate_buffer** – rotate need buffer

    返回
    :   - BK_OK: succeed

        - other: errors.


## API Typedefs[](#api-typedefs "永久链接至标题")
