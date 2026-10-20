---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/api-reference/multi_media/bk_jpegdec_sw.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
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
:   - [`bk_jpeg_dec_sw_init()`](#_CPPv419bk_jpeg_dec_sw_initv "bk_jpeg_dec_sw_init") \- init jpeg decode software module
    - [`bk_jpeg_dec_sw_deinit()`](#_CPPv421bk_jpeg_dec_sw_deinitv "bk_jpeg_dec_sw_deinit") \- deinit jpeg decode software module
    - `bk_jpeg_sw_decoder_fun()` \- excute jpeg decode
    - `bk_jpeg_decode_sw_register_finish_callback()` \- register jpeg decode finish callback

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [jpeg\_decode.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/jpeg_decode.h)

<a id="functions"></a>

### Functions

<a id="_CPPv419bk_jpeg_dec_sw_initv"></a>

<a id="_CPPv319bk_jpeg_dec_sw_initv"></a> <a id="_CPPv219bk_jpeg_dec_sw_initv"></a> <a id="bk_jpeg_dec_sw_init__void"></a> <a id="jpeg__decode_8h_1a02c80d8fee6f16950c4f570dffbd4ac3"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_dec\_sw\_init(void)
:   JPEG\_DEC APIs Version 1.0.

    Init the jpeg\_dec

    This API init the jpeg\_dec

    - config jpeg\_dec image resoult, and simple\_rate
    - malloc buffer for jpeg\_dec

    **Attention**
    :   1\. only for software jpeg\_dec

    参数
    :   - **src\_buf** – input image address
        - **dst\_buf** – output decode image address

    返回
    :   - kNoErr: succeed
        - other: errors.

<a id="_CPPv421bk_jpeg_dec_sw_deinitv"></a>

<a id="_CPPv321bk_jpeg_dec_sw_deinitv"></a> <a id="_CPPv221bk_jpeg_dec_sw_deinitv"></a> <a id="bk_jpeg_dec_sw_deinit__void"></a> <a id="jpeg__decode_8h_1a1e772fdd541bd135ea967b06e06a06e5"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_dec\_sw\_deinit(void)
:   Deinit the jpeg\_dec.

    This API deinit the jpeg\_dec

    - clear all configure for jpeg\_dec
    - free buffer for jpeg\_dec

    **Attention**
    :   1\. only for software jpeg\_dec

    返回
    :   - kNoErr: succeed
        - other: errors.

<a id="_CPPv420bk_jpeg_dec_sw_start8uint32_tP7uint8_tP7uint8_tP17sw_jpeg_dec_res_t"></a>

<a id="_CPPv320bk_jpeg_dec_sw_start8uint32_tP7uint8_tP7uint8_tP17sw_jpeg_dec_res_t"></a> <a id="_CPPv220bk_jpeg_dec_sw_start8uint32_tP7uint8_tP7uint8_tP17sw_jpeg_dec_res_t"></a> <a id="bk_jpeg_dec_sw_start__uint32_t.uint8_tP.uint8_tP.sw_jpeg_dec_res_tP"></a> <a id="jpeg__decode_8h_1a9e841fd6029e6300b09dcf037e763793"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_dec\_sw\_start(uint32\_t frame\_size, uint8\_t \*src\_buf, uint8\_t \*dst\_buf, [sw\_jpeg\_dec\_res\_t](#_CPPv417sw_jpeg_dec_res_t "sw_jpeg_dec_res_t") \*result)
:   jpeg\_decoder\_fun

    This API jpeg\_decoder\_fun

    - jpeg\_prepare for jpeg\_dec
    - start jpeg\_dec

    **Attention**
    :   1\. only for software jpeg\_dec

    参数
    :   **frame\_size** – input image size

    返回
    :   - kNoErr: succeed
        - other: errors.

<a id="_CPPv420bk_jpeg_get_img_info8uint32_tP7uint8_tP17sw_jpeg_dec_res_t"></a>

<a id="_CPPv320bk_jpeg_get_img_info8uint32_tP7uint8_tP17sw_jpeg_dec_res_t"></a> <a id="_CPPv220bk_jpeg_get_img_info8uint32_tP7uint8_tP17sw_jpeg_dec_res_t"></a> <a id="bk_jpeg_get_img_info__uint32_t.uint8_tP.sw_jpeg_dec_res_tP"></a> <a id="jpeg__decode_8h_1a58a08286fb886b2399ae6114bab98650"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_get\_img\_info(uint32\_t frame\_size, uint8\_t \*src\_buf, [sw\_jpeg\_dec\_res\_t](#_CPPv417sw_jpeg_dec_res_t "sw_jpeg_dec_res_t") \*result)
:   jpeg\_decoder\_fun

    This API is used to get img width and size

    **Attention**
    :   1\. only for software jpeg\_dec

    参数
    :   **frame\_size** – input image size

    返回
    :   - kNoErr: succeed
        - other: errors.

<a id="_CPPv439bk_jpeg_dec_sw_register_finish_callbackPv"></a>

<a id="_CPPv339bk_jpeg_dec_sw_register_finish_callbackPv"></a> <a id="_CPPv239bk_jpeg_dec_sw_register_finish_callbackPv"></a> <a id="bk_jpeg_dec_sw_register_finish_callback__voidP"></a> <a id="jpeg__decode_8h_1abd2a52c16af84f1190b6e99609c08be1"></a> void bk\_jpeg\_dec\_sw\_register\_finish\_callback(void \*cb)
:   jpegdec register finish icallback\_func

    This API jpeg\_decoder\_fun, the callback function wiil execute when decode success

    **Attention**
    :   1\. only for software jpeg\_dec

    参数
    :   **cb** – finish jpeg\_dec callback function

    返回

<a id="structures"></a>

### Structures

<a id="_CPPv417sw_jpeg_dec_res_t"></a>

<a id="_CPPv317sw_jpeg_dec_res_t"></a> <a id="_CPPv217sw_jpeg_dec_res_t"></a> <a id="sw_jpeg_dec_res_t"></a> <a id="structsw__jpeg__dec__res__t"></a> struct sw\_jpeg\_dec\_res\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17sw_jpeg_dec_res_t2okE"></a>

    <a id="_CPPv3N17sw_jpeg_dec_res_t2okE"></a> <a id="_CPPv2N17sw_jpeg_dec_res_t2okE"></a> <a id="sw_jpeg_dec_res_t::ok__b"></a> <a id="structsw__jpeg__dec__res__t_1ad3da76c771e4e628d6677ad8a8ff6bbf"></a> bool ok
    :   jpeg decoder success

    <a id="_CPPv4N17sw_jpeg_dec_res_t7pixel_xE"></a>

    <a id="_CPPv3N17sw_jpeg_dec_res_t7pixel_xE"></a> <a id="_CPPv2N17sw_jpeg_dec_res_t7pixel_xE"></a> <a id="sw_jpeg_dec_res_t::pixel_x__uint16_t"></a> <a id="structsw__jpeg__dec__res__t_1ab877ec88e7392230cb1a2a80993c72d9"></a> uint16\_t pixel\_x
    :   jpeg x pixel

    <a id="_CPPv4N17sw_jpeg_dec_res_t7pixel_yE"></a>

    <a id="_CPPv3N17sw_jpeg_dec_res_t7pixel_yE"></a> <a id="_CPPv2N17sw_jpeg_dec_res_t7pixel_yE"></a> <a id="sw_jpeg_dec_res_t::pixel_y__uint16_t"></a> <a id="structsw__jpeg__dec__res__t_1abf453b1649e3d4860482f45f00774c21"></a> uint16\_t pixel\_y
    :   jpeg y pixel

    <a id="_CPPv4N17sw_jpeg_dec_res_t4sizeE"></a>

    <a id="_CPPv3N17sw_jpeg_dec_res_t4sizeE"></a> <a id="_CPPv2N17sw_jpeg_dec_res_t4sizeE"></a> <a id="sw_jpeg_dec_res_t::size__uint32_t"></a> <a id="structsw__jpeg__dec__res__t_1add4566d89c3af21acd5660df11d2807c"></a> uint32\_t size
    :   jpeg size

<a id="api-typedefs"></a>

## API Typedefs
