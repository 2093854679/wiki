# JPEGDEC APIs[](#jpegdec-apis "永久链接至标题")


重要

The JPEGDEC API v1.0 is the lastest stable JPEGDEC APIs. All new applications should use JPEGDEC API v1.0. This component is software decode not hardware decode


## JPEGDEC API Categories[](#jpegdec-api-categories "永久链接至标题")

Most of JPEGDEC APIs can be categoried as:

> - JPEGDEC APIs
>
>   The common APIs are prefixed with bk_jpeg_dec_sw, e.g. bk_jpeg_dec_sw_init() etc.

JPEGDEC APIs:
:   - [`bk_jpeg_dec_sw_init()`](#_CPPv419bk_jpeg_dec_sw_initv "bk_jpeg_dec_sw_init") - init jpeg decode software module

    - [`bk_jpeg_dec_sw_deinit()`](#_CPPv421bk_jpeg_dec_sw_deinitv "bk_jpeg_dec_sw_deinit") - deinit jpeg decode software module

    - `bk_jpeg_sw_decoder_fun()` - excute jpeg decode

    - `bk_jpeg_decode_sw_register_finish_callback()` - register jpeg decode finish callback


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [jpeg_decode.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/jpeg_decode.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/jpeg_decode.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_jpeg_dec_sw_init(void)[](#_CPPv419bk_jpeg_dec_sw_initv "永久链接至目标")
:   JPEG_DEC APIs Version 1.0.

    Init the jpeg_dec

    This API init the jpeg_dec


    - config jpeg_dec image resoult, and simple_rate

    - malloc buffer for jpeg_dec


    **Attention**
    :   1. only for software jpeg_dec

    参数
    :   - **src_buf** – input image address

        - **dst_buf** – output decode image address

    返回
    :   - kNoErr: succeed

        - other: errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_jpeg_dec_sw_deinit(void)[](#_CPPv421bk_jpeg_dec_sw_deinitv "永久链接至目标")
:   Deinit the jpeg_dec.

    This API deinit the jpeg_dec


    - clear all configure for jpeg_dec

    - free buffer for jpeg_dec


    **Attention**
    :   1. only for software jpeg_dec

    返回
    :   - kNoErr: succeed

        - other: errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_jpeg_dec_sw_start(uint32_t frame_size, uint8_t *src_buf, uint8_t *dst_buf, [sw_jpeg_dec_res_t](#_CPPv417sw_jpeg_dec_res_t "sw_jpeg_dec_res_t") *result)[](#_CPPv420bk_jpeg_dec_sw_start8uint32_tP7uint8_tP7uint8_tP17sw_jpeg_dec_res_t "永久链接至目标")
:   jpeg_decoder_fun

    This API jpeg_decoder_fun


    - jpeg_prepare for jpeg_dec

    - start jpeg_dec


    **Attention**
    :   1. only for software jpeg_dec

    参数
    :   **frame_size** – input image size

    返回
    :   - kNoErr: succeed

        - other: errors.

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_jpeg_get_img_info(uint32_t frame_size, uint8_t *src_buf, [sw_jpeg_dec_res_t](#_CPPv417sw_jpeg_dec_res_t "sw_jpeg_dec_res_t") *result)[](#_CPPv420bk_jpeg_get_img_info8uint32_tP7uint8_tP17sw_jpeg_dec_res_t "永久链接至目标")
:   jpeg_decoder_fun

    This API is used to get img width and size


    **Attention**
    :   1. only for software jpeg_dec

    参数
    :   **frame_size** – input image size

    返回
    :   - kNoErr: succeed

        - other: errors.

void bk_jpeg_dec_sw_register_finish_callback(void *cb)[](#_CPPv439bk_jpeg_dec_sw_register_finish_callbackPv "永久链接至目标")
:   jpegdec register finish icallback_func

    This API jpeg_decoder_fun, the callback function wiil execute when decode success


    **Attention**
    :   1. only for software jpeg_dec

    参数
    :   **cb** – finish jpeg_dec callback function

    返回


### Structures[](#structures "永久链接至标题")

struct sw_jpeg_dec_res_t[](#_CPPv417sw_jpeg_dec_res_t "永久链接至目标")
:   Public Members

    bool ok[](#_CPPv4N17sw_jpeg_dec_res_t2okE "永久链接至目标")
    :   jpeg decoder success

    uint16_t pixel_x[](#_CPPv4N17sw_jpeg_dec_res_t7pixel_xE "永久链接至目标")
    :   jpeg x pixel

    uint16_t pixel_y[](#_CPPv4N17sw_jpeg_dec_res_t7pixel_yE "永久链接至目标")
    :   jpeg y pixel

    uint32_t size[](#_CPPv4N17sw_jpeg_dec_res_t4sizeE "永久链接至目标")
    :   jpeg size


## API Typedefs[](#api-typedefs "永久链接至标题")
