---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/component/bk_jpeg_dec_sw.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk-jpeg-dec-sw"></a>

# BK\_JPEG\_DEC\_SW

<a id="bk-jpeg-dec-sw-api-status"></a>

## BK\_JPEG\_DEC\_SW API Status

| API |
| --- |
| [`bk_jpeg_dec_sw_init()`](#_CPPv419bk_jpeg_dec_sw_initv "bk_jpeg_dec_sw_init") |
| [`bk_jpeg_dec_sw_deinit()`](#_CPPv421bk_jpeg_dec_sw_deinitv "bk_jpeg_dec_sw_deinit") |
| [`bk_jpeg_dec_sw_start()`](#_CPPv420bk_jpeg_dec_sw_start8uint32_tP7uint8_tP7uint8_tP20bk_jpeg_dec_sw_res_t "bk_jpeg_dec_sw_start") |
| [`bk_jpeg_dec_sw_get_img_info()`](#_CPPv427bk_jpeg_dec_sw_get_img_info8uint32_tP7uint8_tP20bk_jpeg_dec_sw_res_t "bk_jpeg_dec_sw_get_img_info") |
| [`bk_jpeg_dec_sw_register_finish_callback()`](#_CPPv439bk_jpeg_dec_sw_register_finish_callbackPv "bk_jpeg_dec_sw_register_finish_callback") |

<a id="bk-jpeg-dec-sw-api-reference"></a>

## BK\_JPEG\_DEC\_SW API Reference

<a id="header-file"></a>

### Header File

- [component/jpeg\_dec\_sw/bk\_jpeg\_dec\_sw.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/component/jpeg_dec_sw/bk_jpeg_dec_sw.h)

<a id="functions"></a>

### Functions

<a id="_CPPv419bk_jpeg_dec_sw_initv"></a>

<a id="_CPPv319bk_jpeg_dec_sw_initv"></a> <a id="_CPPv219bk_jpeg_dec_sw_initv"></a> <a id="bk_jpeg_dec_sw_init__void"></a> <a id="bk__jpeg__dec__sw_8h_1add0653e789be497f6c16564b41e9d5d0"></a> int32\_t bk\_jpeg\_dec\_sw\_init(void)
:   JPEG\_DEC APIs Version 1.0.

    Init the jpeg\_dec

    This API init the jpeg\_dec

    - config jpeg\_dec image resoult, and simple\_rate
    - malloc buffer for jpeg\_dec

    **Attention**
    :   1\. only for software jpeg\_dec

    参数:
    :   - **src\_buf** – input image address
        - **dst\_buf** – output decode image address

    返回:
    :   - kNoErr: succeed
        - other: errors.

<a id="_CPPv421bk_jpeg_dec_sw_deinitv"></a>

<a id="_CPPv321bk_jpeg_dec_sw_deinitv"></a> <a id="_CPPv221bk_jpeg_dec_sw_deinitv"></a> <a id="bk_jpeg_dec_sw_deinit__void"></a> <a id="bk__jpeg__dec__sw_8h_1aef4da92479afba510d3b972a21ab1bd9"></a> int32\_t bk\_jpeg\_dec\_sw\_deinit(void)
:   Deinit the jpeg\_dec.

    This API deinit the jpeg\_dec

    - clear all configure for jpeg\_dec
    - free buffer for jpeg\_dec

    **Attention**
    :   1\. only for software jpeg\_dec

    返回:
    :   - kNoErr: succeed
        - other: errors.

<a id="_CPPv420bk_jpeg_dec_sw_start8uint32_tP7uint8_tP7uint8_tP20bk_jpeg_dec_sw_res_t"></a>

<a id="_CPPv320bk_jpeg_dec_sw_start8uint32_tP7uint8_tP7uint8_tP20bk_jpeg_dec_sw_res_t"></a> <a id="_CPPv220bk_jpeg_dec_sw_start8uint32_tP7uint8_tP7uint8_tP20bk_jpeg_dec_sw_res_t"></a> <a id="bk_jpeg_dec_sw_start__uint32_t.uint8_tP.uint8_tP.bk_jpeg_dec_sw_res_tP"></a> <a id="bk__jpeg__dec__sw_8h_1ad0b4f40040ca73f712a21f69893b173c"></a> int32\_t bk\_jpeg\_dec\_sw\_start(uint32\_t frame\_size, uint8\_t \*src\_buf, uint8\_t \*dst\_buf, [bk\_jpeg\_dec\_sw\_res\_t](#_CPPv420bk_jpeg_dec_sw_res_t "bk_jpeg_dec_sw_res_t") \*result)
:   jpeg\_decoder\_fun

    This API jpeg\_decoder\_fun

    - jpeg\_prepare for jpeg\_dec
    - start jpeg\_dec

    **Attention**
    :   1\. only for software jpeg\_dec

    参数:
    :   **frame\_size** – input image size

    返回:
    :   - kNoErr: succeed
        - other: errors.

<a id="_CPPv427bk_jpeg_dec_sw_get_img_info8uint32_tP7uint8_tP20bk_jpeg_dec_sw_res_t"></a>

<a id="_CPPv327bk_jpeg_dec_sw_get_img_info8uint32_tP7uint8_tP20bk_jpeg_dec_sw_res_t"></a> <a id="_CPPv227bk_jpeg_dec_sw_get_img_info8uint32_tP7uint8_tP20bk_jpeg_dec_sw_res_t"></a> <a id="bk_jpeg_dec_sw_get_img_info__uint32_t.uint8_tP.bk_jpeg_dec_sw_res_tP"></a> <a id="bk__jpeg__dec__sw_8h_1a4047e386b7d2eb0029795577bb9249cf"></a> int32\_t bk\_jpeg\_dec\_sw\_get\_img\_info(uint32\_t frame\_size, uint8\_t \*src\_buf, [bk\_jpeg\_dec\_sw\_res\_t](#_CPPv420bk_jpeg_dec_sw_res_t "bk_jpeg_dec_sw_res_t") \*result)
:   jpeg\_decoder\_fun

    This API is used to get img width and size

    **Attention**
    :   1\. only for software jpeg\_dec

    参数:
    :   **frame\_size** – input image size

    返回:
    :   - kNoErr: succeed
        - other: errors.

<a id="_CPPv439bk_jpeg_dec_sw_register_finish_callbackPv"></a>

<a id="_CPPv339bk_jpeg_dec_sw_register_finish_callbackPv"></a> <a id="_CPPv239bk_jpeg_dec_sw_register_finish_callbackPv"></a> <a id="bk_jpeg_dec_sw_register_finish_callback__voidP"></a> <a id="bk__jpeg__dec__sw_8h_1abd2a52c16af84f1190b6e99609c08be1"></a> void bk\_jpeg\_dec\_sw\_register\_finish\_callback(void \*cb)
:   jpegdec register finish icallback\_func

    This API jpeg\_decoder\_fun, the callback function wiil execute when decode success

    **Attention**
    :   1\. only for software jpeg\_dec

    参数:
    :   **cb** – finish jpeg\_dec callback function

    返回:

<a id="structures"></a>

### Structures

<a id="_CPPv420bk_jpeg_dec_sw_res_t"></a>

<a id="_CPPv320bk_jpeg_dec_sw_res_t"></a> <a id="_CPPv220bk_jpeg_dec_sw_res_t"></a> <a id="bk_jpeg_dec_sw_res_t"></a> <a id="structbk__jpeg__dec__sw__res__t"></a> struct bk\_jpeg\_dec\_sw\_res\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20bk_jpeg_dec_sw_res_t2okE"></a>

    <a id="_CPPv3N20bk_jpeg_dec_sw_res_t2okE"></a> <a id="_CPPv2N20bk_jpeg_dec_sw_res_t2okE"></a> <a id="bk_jpeg_dec_sw_res_t::ok__b"></a> <a id="structbk__jpeg__dec__sw__res__t_1addc8f2db0ff420207611b18accd3182f"></a> bool ok
    :   jpeg decoder success

    <a id="_CPPv4N20bk_jpeg_dec_sw_res_t7pixel_xE"></a>

    <a id="_CPPv3N20bk_jpeg_dec_sw_res_t7pixel_xE"></a> <a id="_CPPv2N20bk_jpeg_dec_sw_res_t7pixel_xE"></a> <a id="bk_jpeg_dec_sw_res_t::pixel_x__uint16_t"></a> <a id="structbk__jpeg__dec__sw__res__t_1a604d4e9447afa3a7e05b079b626743cf"></a> uint16\_t pixel\_x
    :   jpeg x pixel

    <a id="_CPPv4N20bk_jpeg_dec_sw_res_t7pixel_yE"></a>

    <a id="_CPPv3N20bk_jpeg_dec_sw_res_t7pixel_yE"></a> <a id="_CPPv2N20bk_jpeg_dec_sw_res_t7pixel_yE"></a> <a id="bk_jpeg_dec_sw_res_t::pixel_y__uint16_t"></a> <a id="structbk__jpeg__dec__sw__res__t_1a5f7cc45b98fa28112ef91c96ad485a5f"></a> uint16\_t pixel\_y
    :   jpeg y pixel

    <a id="_CPPv4N20bk_jpeg_dec_sw_res_t4sizeE"></a>

    <a id="_CPPv3N20bk_jpeg_dec_sw_res_t4sizeE"></a> <a id="_CPPv2N20bk_jpeg_dec_sw_res_t4sizeE"></a> <a id="bk_jpeg_dec_sw_res_t::size__uint32_t"></a> <a id="structbk__jpeg__dec__sw__res__t_1ac56c500a5f90badfd6975280bedadff7"></a> uint32\_t size
    :   jpeg size
