---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_jpeg_dec.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-jpeg-dec"></a>

# DRV\_JPEG\_DEC

<a id="drv-jpeg-dec-api-status"></a>

## DRV\_JPEG\_DEC API Status

| API |
| --- |
| [`drv_jpeg_dec_init()`](#_CPPv417drv_jpeg_dec_initP7uint8_t8uint32_t "drv_jpeg_dec_init") |
| [`drv_jpeg_dec_deinit()`](#_CPPv419drv_jpeg_dec_deinitv "drv_jpeg_dec_deinit") |
| [`drv_jpeg_dec_config()`](#_CPPv419drv_jpeg_dec_config8uint32_tPhPh "drv_jpeg_dec_config") |
| [`drv_jpeg_dec_start()`](#_CPPv418drv_jpeg_dec_startv "drv_jpeg_dec_start") |
| [`drv_jpeg_dec_stop()`](#_CPPv417drv_jpeg_dec_stopv "drv_jpeg_dec_stop") |
| [`drv_jpeg_dec_int_cbk_register()`](#_CPPv429drv_jpeg_dec_int_cbk_register22jpeg_dec_hw_isr_type_e23pfunc_drv_jpeg_dec_cb_t "drv_jpeg_dec_int_cbk_register") |

<a id="drv-jpeg-dec-api-reference"></a>

## DRV\_JPEG\_DEC API Reference

<a id="header-file"></a>

### Header File

- [driver/jpeg\_dec/drv\_jpeg\_dec.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/jpeg_dec/drv_jpeg_dec.h)

<a id="functions"></a>

### Functions

<a id="_CPPv417drv_jpeg_dec_initP7uint8_t8uint32_t"></a>

<a id="_CPPv317drv_jpeg_dec_initP7uint8_t8uint32_t"></a> <a id="_CPPv217drv_jpeg_dec_initP7uint8_t8uint32_t"></a> <a id="drv_jpeg_dec_init__uint8_tP.uint32_t"></a> <a id="drv__jpeg__dec_8h_1ad9b69ecdc3b4e10d4b2d0037243da6d4"></a> int32\_t drv\_jpeg\_dec\_init(uint8\_t \*work\_buf, uint32\_t buf\_size)
:   init a jpeg decoder device.

    jpeg硬件解码器初始化，在使用jpeg decoder功能前需要调用

    参数:
    :   - **work\_buf** – **\[in\]** 指向解码所需要的临时空间地址
        - **buf\_size** – **\[in\]** size \> WORK\_AREA\_SIZE

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419drv_jpeg_dec_deinitv"></a>

<a id="_CPPv319drv_jpeg_dec_deinitv"></a> <a id="_CPPv219drv_jpeg_dec_deinitv"></a> <a id="drv_jpeg_dec_deinit__void"></a> <a id="drv__jpeg__dec_8h_1a7e859a9e435021173b592e25ebd03386"></a> int32\_t drv\_jpeg\_dec\_deinit(void)
:   deinit a jpeg decoder device.

    反初始化jpeg decoder设备，对drv\_jpeg\_dec\_init()进行反向操作

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419drv_jpeg_dec_config8uint32_tPhPh"></a>

<a id="_CPPv319drv_jpeg_dec_config8uint32_tPhPh"></a> <a id="_CPPv219drv_jpeg_dec_config8uint32_tPhPh"></a> <a id="drv_jpeg_dec_config__uint32_t.unsigned-cP.unsigned-cP"></a> <a id="drv__jpeg__dec_8h_1a27ba1395873179521ea56adffae14661"></a> int32\_t drv\_jpeg\_dec\_config(uint32\_t length, unsigned char \*input\_buf, unsigned char \*output\_buf)
:   config jpeg decoder parameter

    对解码器进行配置 此硬件只支持解码特定的jpeg格式(yuv4:2:2)，其格式如下： jpeg格式中, FFC0字段中参数： 图像组件数 \= 3 组件\[1\]: ID\=0x01, Samp Fac\=0x21 (Subsamp 1 x 1), Quant Tbl Sel\=0x00 (Lum: Y) 组件\[2\]: ID\=0x02, Samp Fac\=0x11 (Subsamp 2 x 1), Quant Tbl Sel\=0x01 (Chrom: Cb) 组件\[3\]: ID\=0x03, Samp Fac\=0x11 (Subsamp 2 x 1), Quant Tbl Sel\=0x01 (Chrom: Cr) 解码器输出的格式为：Y0UY1V-\&#8212;{Y0\[31:24\],U\[23:16\],Y1\[15:8\],V\[7:0\]}

    参数:
    :   - **length** – **\[in\]** jpeg图片数据大小
        - **input\_buf** – **\[in\]** 指向需要解码的数据空间
        - **output\_buf** – **\[in\]** 指向存储解码数据的空间

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv418drv_jpeg_dec_startv"></a>

<a id="_CPPv318drv_jpeg_dec_startv"></a> <a id="_CPPv218drv_jpeg_dec_startv"></a> <a id="drv_jpeg_dec_start__void"></a> <a id="drv__jpeg__dec_8h_1af6b6cf136e883ce15016b61a6afa4376"></a> int32\_t drv\_jpeg\_dec\_start(void)
:   start jpeg decode

    开始解码

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv417drv_jpeg_dec_stopv"></a>

<a id="_CPPv317drv_jpeg_dec_stopv"></a> <a id="_CPPv217drv_jpeg_dec_stopv"></a> <a id="drv_jpeg_dec_stop__void"></a> <a id="drv__jpeg__dec_8h_1a4a6cea913214f2a885a7bdf340f31ea7"></a> int32\_t drv\_jpeg\_dec\_stop(void)
:   stop jpeg decode

    停止解码

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv429drv_jpeg_dec_int_cbk_register22jpeg_dec_hw_isr_type_e23pfunc_drv_jpeg_dec_cb_t"></a>

<a id="_CPPv329drv_jpeg_dec_int_cbk_register22jpeg_dec_hw_isr_type_e23pfunc_drv_jpeg_dec_cb_t"></a> <a id="_CPPv229drv_jpeg_dec_int_cbk_register22jpeg_dec_hw_isr_type_e23pfunc_drv_jpeg_dec_cb_t"></a> <a id="drv_jpeg_dec_int_cbk_register__jpeg_dec_hw_isr_type_e.pfunc_drv_jpeg_dec_cb_t"></a> <a id="drv__jpeg__dec_8h_1a57f2ac7e0d044d69b438c3b6c5bf83c7"></a> int32\_t drv\_jpeg\_dec\_int\_cbk\_register([jpeg\_dec\_hw\_isr\_type\_e](#_CPPv422jpeg_dec_hw_isr_type_e "jpeg_dec_hw_isr_type_e") isr\_id, [pfunc\_drv\_jpeg\_dec\_cb\_t](#_CPPv423pfunc_drv_jpeg_dec_cb_t "pfunc_drv_jpeg_dec_cb_t") pfn\_cb)
:   register intrrupt callback function

    注册中断回调函数

    参数:
    :   - **isr\_id** – **\[in\]** DEC\_END\_OF\_FRAME\&#8212;解码完成中断 DEC\_END\_OF\_LINE\_NUM\&#8212;按行解码中断，默认是解码2行来一次中断
        - **pfn\_cb** – **\[in\]** 回调函数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv417jpeg_dec_hw_res_t"></a>

<a id="_CPPv317jpeg_dec_hw_res_t"></a> <a id="_CPPv217jpeg_dec_hw_res_t"></a> <a id="jpeg_dec_hw_res_t"></a> <a id="structjpeg__dec__hw__res__t"></a> struct jpeg\_dec\_hw\_res\_t
:   jpeg dec isr return value

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17jpeg_dec_hw_res_t2okE"></a>

    <a id="_CPPv3N17jpeg_dec_hw_res_t2okE"></a> <a id="_CPPv2N17jpeg_dec_hw_res_t2okE"></a> <a id="jpeg_dec_hw_res_t::ok__b"></a> <a id="structjpeg__dec__hw__res__t_1a37ae840dacd204a9d7394af21c33d873"></a> bool ok
    :   jpeg decoder success

    <a id="_CPPv4N17jpeg_dec_hw_res_t7pixel_xE"></a>

    <a id="_CPPv3N17jpeg_dec_hw_res_t7pixel_xE"></a> <a id="_CPPv2N17jpeg_dec_hw_res_t7pixel_xE"></a> <a id="jpeg_dec_hw_res_t::pixel_x__uint16_t"></a> <a id="structjpeg__dec__hw__res__t_1a247ef1924320e09e87a3b6021f0ec1ff"></a> uint16\_t pixel\_x
    :   jpeg x pixel

    <a id="_CPPv4N17jpeg_dec_hw_res_t7pixel_yE"></a>

    <a id="_CPPv3N17jpeg_dec_hw_res_t7pixel_yE"></a> <a id="_CPPv2N17jpeg_dec_hw_res_t7pixel_yE"></a> <a id="jpeg_dec_hw_res_t::pixel_y__uint16_t"></a> <a id="structjpeg__dec__hw__res__t_1a5901fb518e9d632be65996123ddb2299"></a> uint16\_t pixel\_y
    :   jpeg y pixel

    <a id="_CPPv4N17jpeg_dec_hw_res_t4sizeE"></a>

    <a id="_CPPv3N17jpeg_dec_hw_res_t4sizeE"></a> <a id="_CPPv2N17jpeg_dec_hw_res_t4sizeE"></a> <a id="jpeg_dec_hw_res_t::size__uint32_t"></a> <a id="structjpeg__dec__hw__res__t_1ae870a72303381a1132482e613a621669"></a> uint32\_t size
    :   jpeg size

<a id="macros"></a>

### Macros

<a id="c.JPEG_DEC_STRIP"></a>

<a id="drv__jpeg__dec_8h_1a746e70b6ceecd1d64dadb0f337934085"></a> JPEG\_DEC\_STRIP

<a id="c.USE_LINE_INT_JPEG_DEC"></a>

<a id="drv__jpeg__dec_8h_1af2135316694e1c1fc6207db32274d02a"></a> USE\_LINE\_INT\_JPEG\_DEC

<a id="c.WORK_AREA_SIZE"></a>

<a id="drv__jpeg__dec_8h_1aaf0f6e9bf01cf26252ebface130e8764"></a> WORK\_AREA\_SIZE

<a id="c.JD_SZBUF"></a>

<a id="drv__jpeg__dec_8h_1a678f40366757172a8aafec48c308b657"></a> JD\_SZBUF

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv423pfunc_drv_jpeg_dec_cb_t"></a>

<a id="_CPPv323pfunc_drv_jpeg_dec_cb_t"></a> <a id="_CPPv223pfunc_drv_jpeg_dec_cb_t"></a> <a id="pfunc_drv_jpeg_dec_cb_t"></a> <a id="drv__jpeg__dec_8h_1a15ba3290661b1bd2c7f8d96679e0102a"></a> typedef void (\*pfunc\_drv\_jpeg\_dec\_cb\_t)([jpeg\_dec\_hw\_res\_t](#_CPPv417jpeg_dec_hw_res_t "jpeg_dec_hw_res_t") \*p\_result)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv422jpeg_dec_hw_isr_type_e"></a>

<a id="_CPPv322jpeg_dec_hw_isr_type_e"></a> <a id="_CPPv222jpeg_dec_hw_isr_type_e"></a> <a id="drv__jpeg__dec_8h_1a13820bd1997f050fcab90d7a97540988"></a> enum jpeg\_dec\_hw\_isr\_type\_e
:   *Values:*

    <a id="_CPPv4N22jpeg_dec_hw_isr_type_e16DEC_END_OF_FRAMEE"></a>

    <a id="_CPPv3N22jpeg_dec_hw_isr_type_e16DEC_END_OF_FRAMEE"></a> <a id="_CPPv2N22jpeg_dec_hw_isr_type_e16DEC_END_OF_FRAMEE"></a> <a id="drv__jpeg__dec_8h_1a13820bd1997f050fcab90d7a97540988a2a86ddc1a50843dcfcd91710e772ba9f"></a> enumerator DEC\_END\_OF\_FRAME
    :   select jpeg decode a complete frame enter isr callback

    <a id="_CPPv4N22jpeg_dec_hw_isr_type_e19DEC_END_OF_LINE_NUME"></a>

    <a id="_CPPv3N22jpeg_dec_hw_isr_type_e19DEC_END_OF_LINE_NUME"></a> <a id="_CPPv2N22jpeg_dec_hw_isr_type_e19DEC_END_OF_LINE_NUME"></a> <a id="drv__jpeg__dec_8h_1a13820bd1997f050fcab90d7a97540988ae94cc3b6f30d4ca239ff37a5e574613f"></a> enumerator DEC\_END\_OF\_LINE\_NUM
    :   select jpeg decode line num enter isr callback, used with api line\_en

    <a id="_CPPv4N22jpeg_dec_hw_isr_type_e11DEC_ISR_MAXE"></a>

    <a id="_CPPv3N22jpeg_dec_hw_isr_type_e11DEC_ISR_MAXE"></a> <a id="_CPPv2N22jpeg_dec_hw_isr_type_e11DEC_ISR_MAXE"></a> <a id="drv__jpeg__dec_8h_1a13820bd1997f050fcab90d7a97540988aeedf1b35b37bb22dbe07c948c7973ebd"></a> enumerator DEC\_ISR\_MAX
