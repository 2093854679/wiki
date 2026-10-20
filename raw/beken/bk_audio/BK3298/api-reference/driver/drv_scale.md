---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_scale.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-scale"></a>

# DRV\_SCALE

<a id="drv-scale-api-status"></a>

## DRV\_SCALE API Status

| API |
| --- |
| [`drv_scale_init()`](#_CPPv414drv_scale_initv "drv_scale_init") |
| [`drv_scale_deinit()`](#_CPPv416drv_scale_deinitv "drv_scale_deinit") |
| [`drv_scale_config()`](#_CPPv416drv_scale_configP12scale_info_t "drv_scale_config") |
| [`drv_scale_start()`](#_CPPv415drv_scale_startv "drv_scale_start") |
| [`drv_scale_int_enable()`](#_CPPv420drv_scale_int_enableb "drv_scale_int_enable") |
| [`drv_scale_int_cbk_register()`](#_CPPv426drv_scale_int_cbk_register20pfunc_drv_scale_cb_tPv "drv_scale_int_cbk_register") |

<a id="drv-scale-api-reference"></a>

## DRV\_SCALE API Reference

<a id="header-file"></a>

### Header File

- [driver/scale/drv\_scale.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/scale/drv_scale.h)

<a id="functions"></a>

### Functions

<a id="_CPPv414drv_scale_initv"></a>

<a id="_CPPv314drv_scale_initv"></a> <a id="_CPPv214drv_scale_initv"></a> <a id="drv_scale_init__void"></a> <a id="drv__scale_8h_1a913443a08a5dca845546831acbd6c9c8"></a> int32\_t drv\_scale\_init(void)

<a id="_CPPv416drv_scale_deinitv"></a>

<a id="_CPPv316drv_scale_deinitv"></a> <a id="_CPPv216drv_scale_deinitv"></a> <a id="drv_scale_deinit__void"></a> <a id="drv__scale_8h_1a7a0f58c43ff6786bea782cdaef64533f"></a> int32\_t drv\_scale\_deinit(void)

<a id="_CPPv416drv_scale_configP12scale_info_t"></a>

<a id="_CPPv316drv_scale_configP12scale_info_t"></a> <a id="_CPPv216drv_scale_configP12scale_info_t"></a> <a id="drv_scale_config__scale_info_tP"></a> <a id="drv__scale_8h_1a3688f6988593e723bbc08b8da63c2edd"></a> int32\_t drv\_scale\_config([scale\_info\_t](#_CPPv412scale_info_t "scale_info_t") \*p\_scale\_info)

<a id="_CPPv415drv_scale_startv"></a>

<a id="_CPPv315drv_scale_startv"></a> <a id="_CPPv215drv_scale_startv"></a> <a id="drv_scale_start__void"></a> <a id="drv__scale_8h_1add34c0e7e39dce31c409192267b51121"></a> int32\_t drv\_scale\_start(void)

<a id="_CPPv420drv_scale_int_enableb"></a>

<a id="_CPPv320drv_scale_int_enableb"></a> <a id="_CPPv220drv_scale_int_enableb"></a> <a id="drv_scale_int_enable__b"></a> <a id="drv__scale_8h_1ac6ab47f6b07b28f10b79f76ad86df5c9"></a> int32\_t drv\_scale\_int\_enable(bool en)

<a id="_CPPv426drv_scale_int_cbk_register20pfunc_drv_scale_cb_tPv"></a>

<a id="_CPPv326drv_scale_int_cbk_register20pfunc_drv_scale_cb_tPv"></a> <a id="_CPPv226drv_scale_int_cbk_register20pfunc_drv_scale_cb_tPv"></a> <a id="drv_scale_int_cbk_register__pfunc_drv_scale_cb_t.voidP"></a> <a id="drv__scale_8h_1a101a944b9d974a5d3e71dce17ce263b6"></a> int32\_t drv\_scale\_int\_cbk\_register([pfunc\_drv\_scale\_cb\_t](#_CPPv420pfunc_drv_scale_cb_t "pfunc_drv_scale_cb_t") pfn\_cb, void \*pv\_arg)

<a id="structures"></a>

### Structures

<a id="_CPPv412scale_info_t"></a>

<a id="_CPPv312scale_info_t"></a> <a id="_CPPv212scale_info_t"></a> <a id="scale_info_t"></a> <a id="structscale__info__t"></a> struct scale\_info\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N12scale_info_t6formatE"></a>

    <a id="_CPPv3N12scale_info_t6formatE"></a> <a id="_CPPv2N12scale_info_t6formatE"></a> <a id="scale_info_t::format__scale_pixel_format_e"></a> <a id="structscale__info__t_1aa8d6d3d31add7e3e93ece36e3c320a3c"></a> [scale\_pixel\_format\_e](#_CPPv420scale_pixel_format_e "scale_pixel_format_e") format
    :   scale module input data format , only select YUYV/RGB888/RGB565

    <a id="_CPPv4N12scale_info_t9src_widthE"></a>

    <a id="_CPPv3N12scale_info_t9src_widthE"></a> <a id="_CPPv2N12scale_info_t9src_widthE"></a> <a id="scale_info_t::src_width__uint16_t"></a> <a id="structscale__info__t_1a3ee400ff5c905b7ae65fecaf1278ae2e"></a> uint16\_t src\_width
    :   src image width

    <a id="_CPPv4N12scale_info_t10src_heightE"></a>

    <a id="_CPPv3N12scale_info_t10src_heightE"></a> <a id="_CPPv2N12scale_info_t10src_heightE"></a> <a id="scale_info_t::src_height__uint16_t"></a> <a id="structscale__info__t_1a023faf9aa7ffeda9c3f79a693ca8cbbe"></a> uint16\_t src\_height
    :   src image height

    <a id="_CPPv4N12scale_info_t9dst_widthE"></a>

    <a id="_CPPv3N12scale_info_t9dst_widthE"></a> <a id="_CPPv2N12scale_info_t9dst_widthE"></a> <a id="scale_info_t::dst_width__uint16_t"></a> <a id="structscale__info__t_1a65be3496057c0d0e1071645245c91f93"></a> uint16\_t dst\_width
    :   dst image width

    <a id="_CPPv4N12scale_info_t10dst_heightE"></a>

    <a id="_CPPv3N12scale_info_t10dst_heightE"></a> <a id="_CPPv2N12scale_info_t10dst_heightE"></a> <a id="scale_info_t::dst_height__uint16_t"></a> <a id="structscale__info__t_1a0824481c337e76d0368615dde9991f7f"></a> uint16\_t dst\_height
    :   dst image height

    <a id="_CPPv4N12scale_info_t8src_addrE"></a>

    <a id="_CPPv3N12scale_info_t8src_addrE"></a> <a id="_CPPv2N12scale_info_t8src_addrE"></a> <a id="scale_info_t::src_addr__voidP"></a> <a id="structscale__info__t_1a294f2822e23f7191c732cf868806c6c6"></a> void \*src\_addr
    :   image src addr

    <a id="_CPPv4N12scale_info_t8dst_addrE"></a>

    <a id="_CPPv3N12scale_info_t8dst_addrE"></a> <a id="_CPPv2N12scale_info_t8dst_addrE"></a> <a id="scale_info_t::dst_addr__voidP"></a> <a id="structscale__info__t_1aee3b0ef85064021b901d6669a46ff5f8"></a> void \*dst\_addr
    :   image dst addr

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv420pfunc_drv_scale_cb_t"></a>

<a id="_CPPv320pfunc_drv_scale_cb_t"></a> <a id="_CPPv220pfunc_drv_scale_cb_t"></a> <a id="pfunc_drv_scale_cb_t"></a> <a id="drv__scale_8h_1a692ad32a30325788ef1826244759c4e5"></a> typedef void (\*pfunc\_drv\_scale\_cb\_t)(void \*pv\_arg)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv420scale_pixel_format_e"></a>

<a id="_CPPv320scale_pixel_format_e"></a> <a id="_CPPv220scale_pixel_format_e"></a> <a id="drv__scale_8h_1a70fc5570e61671472b8fbe03e1ce94f8"></a> enum scale\_pixel\_format\_e
:   *Values:*

    <a id="_CPPv4N20scale_pixel_format_e12SCALE_RGB565E"></a>

    <a id="_CPPv3N20scale_pixel_format_e12SCALE_RGB565E"></a> <a id="_CPPv2N20scale_pixel_format_e12SCALE_RGB565E"></a> <a id="drv__scale_8h_1a70fc5570e61671472b8fbe03e1ce94f8a13c1be89cc626d66c836f2a10edc4b2f"></a> enumerator SCALE\_RGB565

    <a id="_CPPv4N20scale_pixel_format_e12SCALE_YUV422E"></a>

    <a id="_CPPv3N20scale_pixel_format_e12SCALE_YUV422E"></a> <a id="_CPPv2N20scale_pixel_format_e12SCALE_YUV422E"></a> <a id="drv__scale_8h_1a70fc5570e61671472b8fbe03e1ce94f8a2312e88dc769cd4d69101902f9c0fabf"></a> enumerator SCALE\_YUV422

    <a id="_CPPv4N20scale_pixel_format_e12SCALE_RGB888E"></a>

    <a id="_CPPv3N20scale_pixel_format_e12SCALE_RGB888E"></a> <a id="_CPPv2N20scale_pixel_format_e12SCALE_RGB888E"></a> <a id="drv__scale_8h_1a70fc5570e61671472b8fbe03e1ce94f8a98cb8afaa809836632afc075bfd57623"></a> enumerator SCALE\_RGB888
