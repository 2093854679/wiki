---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/api-reference/multi_media/bk_hw_scale.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="hardware-scale-apis"></a>

# hardware scale APIs

<a id="scale-interface"></a>

## SCALE Interface

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [hw\_scale.h](https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/_header_files/bk_idk/include/driver/hw_scale.h)

<a id="functions"></a>

### Functions

<a id="_CPPv423bk_hw_scale_driver_init10scale_id_t"></a>

<a id="_CPPv323bk_hw_scale_driver_init10scale_id_t"></a> <a id="_CPPv223bk_hw_scale_driver_init10scale_id_t"></a> <a id="bk_hw_scale_driver_init__scale_id_t"></a> <a id="hw__scale_8h_1a3c7b4a7bc919d5db4f323d4c0e36cc0e"></a> bk\_err\_t bk\_hw\_scale\_driver\_init([scale\_id\_t](#_CPPv410scale_id_t "scale_id_t") id)
:   hw scale API

    This API to init scale 0 or 1

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv425bk_hw_scale_driver_deinit10scale_id_t"></a>

<a id="_CPPv325bk_hw_scale_driver_deinit10scale_id_t"></a> <a id="_CPPv225bk_hw_scale_driver_deinit10scale_id_t"></a> <a id="bk_hw_scale_driver_deinit__scale_id_t"></a> <a id="hw__scale_8h_1a92fc8ee81d78b6e5d1ea48dec04e83bf"></a> bk\_err\_t bk\_hw\_scale\_driver\_deinit([scale\_id\_t](#_CPPv410scale_id_t "scale_id_t") id)
:   This API use to deinit scale0/scale1.

    参数
    :   **scale0/scale1** –

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_hw_scale_isr_register10scale_id_t14hw_scale_isr_tPv"></a>

<a id="_CPPv324bk_hw_scale_isr_register10scale_id_t14hw_scale_isr_tPv"></a> <a id="_CPPv224bk_hw_scale_isr_register10scale_id_t14hw_scale_isr_tPv"></a> <a id="bk_hw_scale_isr_register__scale_id_t.hw_scale_isr_t.voidP"></a> <a id="hw__scale_8h_1a6535b7003373fb6cef83d16ace52c558"></a> bk\_err\_t bk\_hw\_scale\_isr\_register([scale\_id\_t](#_CPPv410scale_id_t "scale_id_t") id, [hw\_scale\_isr\_t](#_CPPv414hw_scale_isr_t "hw_scale_isr_t") isr, void \*param)
:   This API use to register scale isr.

    参数
    :   - **isr** – isr\_func
        - **scale** – params, must config by [scale\_drv\_config\_t](#structscale__drv__config__t)

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv426bk_hw_scale_isr_unregister10scale_id_t"></a>

<a id="_CPPv326bk_hw_scale_isr_unregister10scale_id_t"></a> <a id="_CPPv226bk_hw_scale_isr_unregister10scale_id_t"></a> <a id="bk_hw_scale_isr_unregister__scale_id_t"></a> <a id="hw__scale_8h_1aaa4cc519fe934f6c93eb8cb9ce389f9b"></a> bk\_err\_t bk\_hw\_scale\_isr\_unregister([scale\_id\_t](#_CPPv410scale_id_t "scale_id_t") id)
:   This API use to unregister scale isr.

    参数
    :   **scale0/scale1** –

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv422bk_hw_scale_int_enable10scale_id_tb"></a>

<a id="_CPPv322bk_hw_scale_int_enable10scale_id_tb"></a> <a id="_CPPv222bk_hw_scale_int_enable10scale_id_tb"></a> <a id="bk_hw_scale_int_enable__scale_id_t.b"></a> <a id="hw__scale_8h_1a8c1b89014aa3042e3e53c62e6111fd81"></a> bk\_err\_t bk\_hw\_scale\_int\_enable([scale\_id\_t](#_CPPv410scale_id_t "scale_id_t") id, bool en)
:   This API use to enable or display scale interrupt.

    参数
    :   **scale0/scale1** – 0/1

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv414hw_scale_frame10scale_id_tP18scale_drv_config_t"></a>

<a id="_CPPv314hw_scale_frame10scale_id_tP18scale_drv_config_t"></a> <a id="_CPPv214hw_scale_frame10scale_id_tP18scale_drv_config_t"></a> <a id="hw_scale_frame__scale_id_t.scale_drv_config_tP"></a> <a id="hw__scale_8h_1aaabd6bca78cdcf7589d44986b295ded8"></a> bk\_err\_t hw\_scale\_frame([scale\_id\_t](#_CPPv410scale_id_t "scale_id_t") id, [scale\_drv\_config\_t](#_CPPv418scale_drv_config_t "scale_drv_config_t") \*scale\_drv\_config)
:   This API use to scale a complete frame not by line scale.

    param: scale0/scale1 param: [scale\_drv\_config\_t](#structscale__drv__config__t)

    Usage example:

    ```
    scale_param->drv_config.src_width = src->width;
    scale_param->drv_config.dst_width = dst->width;
    scale_param->drv_config.src_height = src->height;
    scale_param->drv_config.dst_height = dst->height;

    scale_param->drv_config.pixel_fmt = src->fmt;
    scale_param->drv_config.scale_mode = FRAME_SCALE;
    scale_param->drv_config.frame_complete = scale_frame_cb;

    scale_param->drv_config.line_cycle = BLOCK_LINE_COUNT;
    scale_param->drv_config.line_mask = 0x1F;
    scale_param->drv_config.src_addr = src->frame;
    scale_param->drv_config.dst_addr = dst->frame;

    hw_scale_frame(HW_SCALE0, &scale_param->drv_config);
    ```

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421hw_scale_block_config10scale_id_tP18scale_drv_config_t"></a>

<a id="_CPPv321hw_scale_block_config10scale_id_tP18scale_drv_config_t"></a> <a id="_CPPv221hw_scale_block_config10scale_id_tP18scale_drv_config_t"></a> <a id="hw_scale_block_config__scale_id_t.scale_drv_config_tP"></a> <a id="hw__scale_8h_1adab8a33f4b5417acce63f93777528d36"></a> bk\_err\_t hw\_scale\_block\_config([scale\_id\_t](#_CPPv410scale_id_t "scale_id_t") id, [scale\_drv\_config\_t](#_CPPv418scale_drv_config_t "scale_drv_config_t") \*scale\_drv\_config)
:   This API use to by line scale.

    param: scale0/scale1 param: [scale\_drv\_config\_t](#structscale__drv__config__t)

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420hw_scale_block_start10scale_id_tP13scale_block_tP13scale_block_t"></a>

<a id="_CPPv320hw_scale_block_start10scale_id_tP13scale_block_tP13scale_block_t"></a> <a id="_CPPv220hw_scale_block_start10scale_id_tP13scale_block_tP13scale_block_t"></a> <a id="hw_scale_block_start__scale_id_t.scale_block_tP.scale_block_tP"></a> <a id="hw__scale_8h_1ab43572d54dd8bd504e6a475bf3fad7eb"></a> bk\_err\_t hw\_scale\_block\_start([scale\_id\_t](#_CPPv410scale_id_t "scale_id_t") id, [scale\_block\_t](#_CPPv413scale_block_t "scale_block_t") \*src, [scale\_block\_t](#_CPPv413scale_block_t "scale_block_t") \*dst)
:   start scale, reference lcd\_scale\_pipeline.c

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424hw_scale_dest_block_fill10scale_id_tP13scale_block_t"></a>

<a id="_CPPv324hw_scale_dest_block_fill10scale_id_tP13scale_block_t"></a> <a id="_CPPv224hw_scale_dest_block_fill10scale_id_tP13scale_block_t"></a> <a id="hw_scale_dest_block_fill__scale_id_t.scale_block_tP"></a> <a id="hw__scale_8h_1aae79ecfa35a6ee90cfeb7439b4fd1d7d"></a> bk\_err\_t hw\_scale\_dest\_block\_fill([scale\_id\_t](#_CPPv410scale_id_t "scale_id_t") id, [scale\_block\_t](#_CPPv413scale_block_t "scale_block_t") \*scale\_block)
:   start scale, reference lcd\_scale\_pipeline.c

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv426hw_scale_source_block_fill10scale_id_tP13scale_block_t"></a>

<a id="_CPPv326hw_scale_source_block_fill10scale_id_tP13scale_block_t"></a> <a id="_CPPv226hw_scale_source_block_fill10scale_id_tP13scale_block_t"></a> <a id="hw_scale_source_block_fill__scale_id_t.scale_block_tP"></a> <a id="hw__scale_8h_1a839424d7b16458d524d36d67355f4f59"></a> bk\_err\_t hw\_scale\_source\_block\_fill([scale\_id\_t](#_CPPv410scale_id_t "scale_id_t") id, [scale\_block\_t](#_CPPv413scale_block_t "scale_block_t") \*scale\_block)
:   start scale, reference lcd\_scale\_pipeline.c

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv416bk_hw_scale_stop10scale_id_t"></a>

<a id="_CPPv316bk_hw_scale_stop10scale_id_t"></a> <a id="_CPPv216bk_hw_scale_stop10scale_id_t"></a> <a id="bk_hw_scale_stop__scale_id_t"></a> <a id="hw__scale_8h_1a69628a3cb7fd0e3bdc3c8479535c8150"></a> bk\_err\_t bk\_hw\_scale\_stop([scale\_id\_t](#_CPPv410scale_id_t "scale_id_t") id)
:   stop scale

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_hw_scale_mem_free10scale_id_t"></a>

<a id="_CPPv320bk_hw_scale_mem_free10scale_id_t"></a> <a id="_CPPv220bk_hw_scale_mem_free10scale_id_t"></a> <a id="bk_hw_scale_mem_free__scale_id_t"></a> <a id="hw__scale_8h_1a0702a552a21ad6e687c951d0ed602b40"></a> bk\_err\_t bk\_hw\_scale\_mem\_free([scale\_id\_t](#_CPPv410scale_id_t "scale_id_t") id)
:   free 7.5K memcory by API bk\_hw\_scale\_driver\_init malloc

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="api-typedefs"></a>

## API Typedefs

<a id="id1"></a>

### Header File

- [hw\_scale\_types.h](https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/_header_files/bk_idk/include/driver/hw_scale_types.h)

<a id="structures"></a>

### Structures

<a id="_CPPv413scale_block_t"></a>

<a id="_CPPv313scale_block_t"></a> <a id="_CPPv213scale_block_t"></a> <a id="scale_block_t"></a> <a id="structscale__block__t"></a> struct scale\_block\_t

<a id="_CPPv414scale_result_t"></a>

<a id="_CPPv314scale_result_t"></a> <a id="_CPPv214scale_result_t"></a> <a id="scale_result_t"></a> <a id="structscale__result__t"></a> struct scale\_result\_t

<a id="_CPPv418scale_drv_config_t"></a>

<a id="_CPPv318scale_drv_config_t"></a> <a id="_CPPv218scale_drv_config_t"></a> <a id="scale_drv_config_t"></a> <a id="structscale__drv__config__t"></a> struct scale\_drv\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18scale_drv_config_t9src_widthE"></a>

    <a id="_CPPv3N18scale_drv_config_t9src_widthE"></a> <a id="_CPPv2N18scale_drv_config_t9src_widthE"></a> <a id="scale_drv_config_t::src_width__uint16_t"></a> <a id="structscale__drv__config__t_1a423154b46c4fe9614ff48a4dfa691b67"></a> uint16\_t src\_width
    :   src image width

    <a id="_CPPv4N18scale_drv_config_t10src_heightE"></a>

    <a id="_CPPv3N18scale_drv_config_t10src_heightE"></a> <a id="_CPPv2N18scale_drv_config_t10src_heightE"></a> <a id="scale_drv_config_t::src_height__uint16_t"></a> <a id="structscale__drv__config__t_1a492df808999c85e667792fd95b35b7ee"></a> uint16\_t src\_height
    :   src image height

    <a id="_CPPv4N18scale_drv_config_t9dst_widthE"></a>

    <a id="_CPPv3N18scale_drv_config_t9dst_widthE"></a> <a id="_CPPv2N18scale_drv_config_t9dst_widthE"></a> <a id="scale_drv_config_t::dst_width__uint16_t"></a> <a id="structscale__drv__config__t_1abaa2b36a7163c89c817455290d05cb5e"></a> uint16\_t dst\_width
    :   dst image width

    <a id="_CPPv4N18scale_drv_config_t10dst_heightE"></a>

    <a id="_CPPv3N18scale_drv_config_t10dst_heightE"></a> <a id="_CPPv2N18scale_drv_config_t10dst_heightE"></a> <a id="scale_drv_config_t::dst_height__uint16_t"></a> <a id="structscale__drv__config__t_1a3b23decb070bf15f8369a2aea8c1c917"></a> uint16\_t dst\_height
    :   dst image height

    <a id="_CPPv4N18scale_drv_config_t9pixel_fmtE"></a>

    <a id="_CPPv3N18scale_drv_config_t9pixel_fmtE"></a> <a id="_CPPv2N18scale_drv_config_t9pixel_fmtE"></a> <a id="scale_drv_config_t::pixel_fmt__pixel_format_t"></a> <a id="structscale__drv__config__t_1a10a1f96444d48eb7f74a6592500e1e54"></a> pixel\_format\_t pixel\_fmt
    :   scale module input data format , only select YUYV/RGB888/RGB565

    <a id="_CPPv4N18scale_drv_config_t8src_addrE"></a>

    <a id="_CPPv3N18scale_drv_config_t8src_addrE"></a> <a id="_CPPv2N18scale_drv_config_t8src_addrE"></a> <a id="scale_drv_config_t::src_addr__uint8_tP"></a> <a id="structscale__drv__config__t_1aafe0573b24b9aa4e413825be7df18b44"></a> uint8\_t \*src\_addr
    :   image src addr

    <a id="_CPPv4N18scale_drv_config_t8dst_addrE"></a>

    <a id="_CPPv3N18scale_drv_config_t8dst_addrE"></a> <a id="_CPPv2N18scale_drv_config_t8dst_addrE"></a> <a id="scale_drv_config_t::dst_addr__uint8_tP"></a> <a id="structscale__drv__config__t_1a82ab1335efb035fe4dd2cf57d150e5d8"></a> uint8\_t \*dst\_addr
    :   image dst addr

<a id="_CPPv418scale_drv_record_t"></a>

<a id="_CPPv318scale_drv_record_t"></a> <a id="_CPPv218scale_drv_record_t"></a> <a id="scale_drv_record_t"></a> <a id="structscale__drv__record__t"></a> struct scale\_drv\_record\_t

<a id="_CPPv418scale_drv_handle_t"></a>

<a id="_CPPv318scale_drv_handle_t"></a> <a id="_CPPv218scale_drv_handle_t"></a> <a id="scale_drv_handle_t"></a> <a id="structscale__drv__handle__t"></a> struct scale\_drv\_handle\_t

<a id="macros"></a>

### Macros

<a id="c.BK_ERR_HW_SCALE_NOT_INIT"></a>

<a id="hw__scale__types_8h_1ae64cae534c35000a90ae4bd442a09913"></a> BK\_ERR\_HW\_SCALE\_NOT\_INIT
:   hw scale init err

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv414hw_scale_isr_t"></a>

<a id="_CPPv314hw_scale_isr_t"></a> <a id="_CPPv214hw_scale_isr_t"></a> <a id="hw_scale_isr_t"></a> <a id="hw__scale__types_8h_1a9ba53f5c569dce96e9dfddb48f272b67"></a> typedef void (\*hw\_scale\_isr\_t)(void \*param)
:   jpeg isr callback relay jpeg driver

    Param id
    :   only 0 useful, set 0 default

    Param param
    :   NULL default

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv410scale_id_t"></a>

<a id="_CPPv310scale_id_t"></a> <a id="_CPPv210scale_id_t"></a> <a id="hw__scale__types_8h_1a6e34cf3efd5ffd41f706c8b668083cd1"></a> enum scale\_id\_t
:   *Values:*

    <a id="_CPPv4N10scale_id_t9HW_SCALE0E"></a>

    <a id="_CPPv3N10scale_id_t9HW_SCALE0E"></a> <a id="_CPPv2N10scale_id_t9HW_SCALE0E"></a> <a id="hw__scale__types_8h_1a6e34cf3efd5ffd41f706c8b668083cd1aaa5aff50768fdce41a43cd00b712b613"></a> enumerator HW\_SCALE0

    <a id="_CPPv4N10scale_id_t9HW_SCALE1E"></a>

    <a id="_CPPv3N10scale_id_t9HW_SCALE1E"></a> <a id="_CPPv2N10scale_id_t9HW_SCALE1E"></a> <a id="hw__scale__types_8h_1a6e34cf3efd5ffd41f706c8b668083cd1aeca47aaa820b76278cbe0a0e1d9081b8"></a> enumerator HW\_SCALE1

    <a id="_CPPv4N10scale_id_t12HW_SCALE_MAXE"></a>

    <a id="_CPPv3N10scale_id_t12HW_SCALE_MAXE"></a> <a id="_CPPv2N10scale_id_t12HW_SCALE_MAXE"></a> <a id="hw__scale__types_8h_1a6e34cf3efd5ffd41f706c8b668083cd1ac1c4627bb16911ae7cb52497d69faf09"></a> enumerator HW\_SCALE\_MAX

<a id="_CPPv412scale_mode_t"></a>

<a id="_CPPv312scale_mode_t"></a> <a id="_CPPv212scale_mode_t"></a> <a id="hw__scale__types_8h_1ae05450757671b1b5b0809bda2edaef1d"></a> enum scale\_mode\_t
:   *Values:*

    <a id="_CPPv4N12scale_mode_t11FRAME_SCALEE"></a>

    <a id="_CPPv3N12scale_mode_t11FRAME_SCALEE"></a> <a id="_CPPv2N12scale_mode_t11FRAME_SCALEE"></a> <a id="hw__scale__types_8h_1ae05450757671b1b5b0809bda2edaef1da83d5fcc8e69d709e78c0be72d30b024a"></a> enumerator FRAME\_SCALE

    <a id="_CPPv4N12scale_mode_t11BLOCK_SCALEE"></a>

    <a id="_CPPv3N12scale_mode_t11BLOCK_SCALEE"></a> <a id="_CPPv2N12scale_mode_t11BLOCK_SCALEE"></a> <a id="hw__scale__types_8h_1ae05450757671b1b5b0809bda2edaef1da159179bbdab2b24d711ffd1acf3fd399"></a> enumerator BLOCK\_SCALE

    <a id="_CPPv4N12scale_mode_t20DVP_DIRECT_YUV_SCALEE"></a>

    <a id="_CPPv3N12scale_mode_t20DVP_DIRECT_YUV_SCALEE"></a> <a id="_CPPv2N12scale_mode_t20DVP_DIRECT_YUV_SCALEE"></a> <a id="hw__scale__types_8h_1ae05450757671b1b5b0809bda2edaef1dafc840f3f3493c7ac21d707f9874f479b"></a> enumerator DVP\_DIRECT\_YUV\_SCALE

    <a id="_CPPv4N12scale_mode_t14DVP_H264_SCALEE"></a>

    <a id="_CPPv3N12scale_mode_t14DVP_H264_SCALEE"></a> <a id="_CPPv2N12scale_mode_t14DVP_H264_SCALEE"></a> <a id="hw__scale__types_8h_1ae05450757671b1b5b0809bda2edaef1dae6029d41f9e5c0698e27aa222ed8accd"></a> enumerator DVP\_H264\_SCALE

    <a id="_CPPv4N12scale_mode_t17JPEGDEC_YUV_SCALEE"></a>

    <a id="_CPPv3N12scale_mode_t17JPEGDEC_YUV_SCALEE"></a> <a id="_CPPv2N12scale_mode_t17JPEGDEC_YUV_SCALEE"></a> <a id="hw__scale__types_8h_1ae05450757671b1b5b0809bda2edaef1da5baf74d808eec671f5565048fbf69382"></a> enumerator JPEGDEC\_YUV\_SCALE
