# hardware scale APIs[](#hardware-scale-apis "永久链接至标题")



## SCALE Interface[](#scale-interface "永久链接至标题")


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [hw_scale.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hw_scale.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hw_scale.h")


### Functions[](#functions "永久链接至标题")

bk_err_t bk_hw_scale_driver_init([scale_id_t](#_CPPv410scale_id_t "scale_id_t") id)[](#_CPPv423bk_hw_scale_driver_init10scale_id_t "永久链接至目标")
:   hw scale API

    This API to init scale 0 or 1

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t bk_hw_scale_driver_deinit([scale_id_t](#_CPPv410scale_id_t "scale_id_t") id)[](#_CPPv425bk_hw_scale_driver_deinit10scale_id_t "永久链接至目标")
:   This API use to deinit scale0/scale1.

    参数
    :   **scale0/scale1** –

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t bk_hw_scale_isr_register([scale_id_t](#_CPPv410scale_id_t "scale_id_t") id, [hw_scale_isr_t](#_CPPv414hw_scale_isr_t "hw_scale_isr_t") isr, void *param)[](#_CPPv424bk_hw_scale_isr_register10scale_id_t14hw_scale_isr_tPv "永久链接至目标")
:   This API use to register scale isr.

    参数
    :   - **isr** – isr_func

        - **scale** – params, must config by [scale_drv_config_t](#structscale__drv__config__t "#structscale__drv__config__t")

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t bk_hw_scale_isr_unregister([scale_id_t](#_CPPv410scale_id_t "scale_id_t") id)[](#_CPPv426bk_hw_scale_isr_unregister10scale_id_t "永久链接至目标")
:   This API use to unregister scale isr.

    参数
    :   **scale0/scale1** –

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t bk_hw_scale_int_enable([scale_id_t](#_CPPv410scale_id_t "scale_id_t") id, bool en)[](#_CPPv422bk_hw_scale_int_enable10scale_id_tb "永久链接至目标")
:   This API use to enable or display scale interrupt.

    参数
    :   **scale0/scale1** – 0/1

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t hw_scale_frame([scale_id_t](#_CPPv410scale_id_t "scale_id_t") id, [scale_drv_config_t](#_CPPv418scale_drv_config_t "scale_drv_config_t") *scale_drv_config)[](#_CPPv414hw_scale_frame10scale_id_tP18scale_drv_config_t "永久链接至目标")
:   This API use to scale a complete frame not by line scale.

    param: scale0/scale1 param: [scale_drv_config_t](#structscale__drv__config__t "#structscale__drv__config__t")

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
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t hw_scale_block_config([scale_id_t](#_CPPv410scale_id_t "scale_id_t") id, [scale_drv_config_t](#_CPPv418scale_drv_config_t "scale_drv_config_t") *scale_drv_config)[](#_CPPv421hw_scale_block_config10scale_id_tP18scale_drv_config_t "永久链接至目标")
:   This API use to by line scale.

    param: scale0/scale1 param: [scale_drv_config_t](#structscale__drv__config__t "#structscale__drv__config__t")

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t hw_scale_block_start([scale_id_t](#_CPPv410scale_id_t "scale_id_t") id, [scale_block_t](#_CPPv413scale_block_t "scale_block_t") *src, [scale_block_t](#_CPPv413scale_block_t "scale_block_t") *dst)[](#_CPPv420hw_scale_block_start10scale_id_tP13scale_block_tP13scale_block_t "永久链接至目标")
:   start scale, reference lcd_scale_pipeline.c

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t hw_scale_dest_block_fill([scale_id_t](#_CPPv410scale_id_t "scale_id_t") id, [scale_block_t](#_CPPv413scale_block_t "scale_block_t") *scale_block)[](#_CPPv424hw_scale_dest_block_fill10scale_id_tP13scale_block_t "永久链接至目标")
:   start scale, reference lcd_scale_pipeline.c

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t hw_scale_source_block_fill([scale_id_t](#_CPPv410scale_id_t "scale_id_t") id, [scale_block_t](#_CPPv413scale_block_t "scale_block_t") *scale_block)[](#_CPPv426hw_scale_source_block_fill10scale_id_tP13scale_block_t "永久链接至目标")
:   start scale, reference lcd_scale_pipeline.c

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t bk_hw_scale_stop([scale_id_t](#_CPPv410scale_id_t "scale_id_t") id)[](#_CPPv416bk_hw_scale_stop10scale_id_t "永久链接至目标")
:   stop scale

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t bk_hw_scale_mem_free([scale_id_t](#_CPPv410scale_id_t "scale_id_t") id)[](#_CPPv420bk_hw_scale_mem_free10scale_id_t "永久链接至目标")
:   free 7.5K memcory by API bk_hw_scale_driver_init malloc

    返回
    :   - BK_OK: succeed

        - others: other errors.


## API Typedefs[](#api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [hw_scale_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hw_scale_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hw_scale_types.h")


### Structures[](#structures "永久链接至标题")

struct scale_block_t[](#_CPPv413scale_block_t "永久链接至目标")

struct scale_result_t[](#_CPPv414scale_result_t "永久链接至目标")

struct scale_drv_config_t[](#_CPPv418scale_drv_config_t "永久链接至目标")
:   Public Members

    uint16_t src_width[](#_CPPv4N18scale_drv_config_t9src_widthE "永久链接至目标")
    :   src image width

    uint16_t src_height[](#_CPPv4N18scale_drv_config_t10src_heightE "永久链接至目标")
    :   src image height

    uint16_t dst_width[](#_CPPv4N18scale_drv_config_t9dst_widthE "永久链接至目标")
    :   dst image width

    uint16_t dst_height[](#_CPPv4N18scale_drv_config_t10dst_heightE "永久链接至目标")
    :   dst image height

    pixel_format_t pixel_fmt[](#_CPPv4N18scale_drv_config_t9pixel_fmtE "永久链接至目标")
    :   scale module input data format , only select YUYV/RGB888/RGB565

    uint8_t *src_addr[](#_CPPv4N18scale_drv_config_t8src_addrE "永久链接至目标")
    :   image src addr

    uint8_t *dst_addr[](#_CPPv4N18scale_drv_config_t8dst_addrE "永久链接至目标")
    :   image dst addr

struct scale_drv_record_t[](#_CPPv418scale_drv_record_t "永久链接至目标")

struct scale_drv_handle_t[](#_CPPv418scale_drv_handle_t "永久链接至目标")


### Macros[](#macros "永久链接至标题")

BK_ERR_HW_SCALE_NOT_INIT[](#c.BK_ERR_HW_SCALE_NOT_INIT "永久链接至目标")
:   hw scale init err


### Type Definitions[](#type-definitions "永久链接至标题")

typedef void (*hw_scale_isr_t)(void *param)[](#_CPPv414hw_scale_isr_t "永久链接至目标")
:   jpeg isr callback relay jpeg driver

    Param id
    :   only 0 useful, set 0 default

    Param param
    :   NULL default


### Enumerations[](#enumerations "永久链接至标题")

enum scale_id_t[](#_CPPv410scale_id_t "永久链接至目标")
:   *Values:*

    enumerator HW_SCALE0[](#_CPPv4N10scale_id_t9HW_SCALE0E "永久链接至目标")

    enumerator HW_SCALE1[](#_CPPv4N10scale_id_t9HW_SCALE1E "永久链接至目标")

    enumerator HW_SCALE_MAX[](#_CPPv4N10scale_id_t12HW_SCALE_MAXE "永久链接至目标")

enum scale_mode_t[](#_CPPv412scale_mode_t "永久链接至目标")
:   *Values:*

    enumerator FRAME_SCALE[](#_CPPv4N12scale_mode_t11FRAME_SCALEE "永久链接至目标")

    enumerator BLOCK_SCALE[](#_CPPv4N12scale_mode_t11BLOCK_SCALEE "永久链接至目标")

    enumerator DVP_DIRECT_YUV_SCALE[](#_CPPv4N12scale_mode_t20DVP_DIRECT_YUV_SCALEE "永久链接至目标")

    enumerator DVP_H264_SCALE[](#_CPPv4N12scale_mode_t14DVP_H264_SCALEE "永久链接至目标")

    enumerator JPEGDEC_YUV_SCALE[](#_CPPv4N12scale_mode_t17JPEGDEC_YUV_SCALEE "永久链接至目标")
