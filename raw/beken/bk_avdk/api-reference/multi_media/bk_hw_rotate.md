# Rotate APIs[](#rotate-apis "永久链接至标题")



## Rotate Interface[](#rotate-interface "永久链接至标题")

旋转模块（Rotate module）主要功能是将储存在memory的yuv422图像，旋转成rgb565格式的图像，完成后储存在另一块memory中

模块共有三种工作模式：
:   1.顺时针旋转模式
    2.逆时针旋转模式
    3.不旋转只进行格式转换


    - 针对旋转，如果输入的数据时RGB565数据，那么就只执行旋转

demo运行依赖的宏配置:

| Name | Description | File | value |
| --- | --- | --- | --- |
| CONFIG_HW_ROTATE_PFC | 配置Rotate功能 | `\middleware\soc\bk7236\bk7236.defconfig` | y |


## Rotate Categories[](#rotate-categories "永久链接至标题")


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [rott_driver.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/rott_driver.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/rott_driver.h")


### Functions[](#functions "永久链接至标题")

bk_err_t bk_rott_driver_init(void)[](#_CPPv419bk_rott_driver_initv "永久链接至目标")
:   This API used config sysclk.

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t bk_rott_soft_reset(void)[](#_CPPv418bk_rott_soft_resetv "永久链接至目标")
:   This API used reset rotate.

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t bk_rott_driver_deinit(void)[](#_CPPv421bk_rott_driver_deinitv "永久链接至目标")
:   This API used disable rotate cpu int.

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t bk_rott_int_enable([rott_int_type_t](#_CPPv415rott_int_type_t "rott_int_type_t") int_type, bool en)[](#_CPPv418bk_rott_int_enable15rott_int_type_tb "永久链接至目标")
:   This API used to config rotate int type and int enable.

    参数
    :   **1:int_type** – include:

        ```

               - ROTATE_COMPLETE_INT: rotate complete int

               - ROTATE_WARTERMARK_INT: if enable, wtmk_block need config, and not set 0, you can set wtmk_block by api bk_rott_wartermark_block_config config or rott_config

               - ROTATE_CFG_ERR_INT, the following will trigger cfg err int,like:

                                - picture_xpixel & picture_ypixel be zero while working.

                                - ROTATE_WARTERMARK_INT=1, but wtmk_block=0

                                - block_cnt=0

                                - block_xpixel > picture_xpixel,  block_ypixel > picture_ypixel
        2: en enable or disable
        ```

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t bk_rott_block_delay_config(bool en, uint16_t delay_hclk_count1, uint16_t delay_hclk_count2)[](#_CPPv426bk_rott_block_delay_configb8uint16_t8uint16_t "永久链接至目标")
:   This API used config rotate delay cycle in block and block interval.

    参数
    :   **-** – en,enable the delay function


        - delay_hclk_count1 (range 0 ~ 0x7fff), the delay pclk cycle is calculate by (delay_hclk_count1 * delay_hclk_count2)

        - delay_hclk_count2 (range 0 ~ 0xffff), the delay pclk cycle is calculate by (delay_hclk_count1 * delay_hclk_count2)

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t bk_rott_mode_config(media_rotate_t rot_mode)[](#_CPPv419bk_rott_mode_config14media_rotate_t "永久链接至目标")
:   This API used config rotate mode.

    参数
    :   **struct** – rott_mode_t


        - ROTT_ONLY_YUV2RGB565, only use yuv data pixel convert to rgb565 pixel, no rotate

        - ROTT_ROTATE90, if rot_input_fmt = RGB565, just rotate; if rot_input_fmt = yuv, not only rotate but convert to rgb565.

        - ROTT_ROTATE170,if rot_input_fmt = RGB565, just rotate; if rot_input_fmt = yuv, not only rotate but convert to rgb565.

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t bk_rott_input_data_format(pixel_format_t rot_input_fmt)[](#_CPPv425bk_rott_input_data_format14pixel_format_t "永久链接至目标")
:   This API used config input data format, output data format is default rgb565.


    **Attention**
    :   if your data rotate or pixel convert not display normally,you can use api bk_rott_data_reverse modify input/output data flow to see see

    参数
    :   **struct** – rott_input_fmt_t


        - RGB565, input format is rgb565 be

        - RGB565le, input format is rgb565 le

        - ROTT_FMT_YUYV

        - ROTT_FMT_VUYY

        - others

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t bk_rott_data_reverse([rott_input_data_flow_t](#_CPPv422rott_input_data_flow_t "rott_input_data_flow_t") input_flow, [rott_output_data_flow_t](#_CPPv423rott_output_data_flow_t "rott_output_data_flow_t") output_flow)[](#_CPPv420bk_rott_data_reverse22rott_input_data_flow_t23rott_output_data_flow_t "永久链接至目标")
:   This API used config input data or output data flip(reverse)


    **Attention**
    :   if your data rotate or pixel convert not display normally,you can use api bk_rott_data_reverse modify input/output data flow to see see

    参数
    :   - **struct** – rott_input_data_flow_t

          - ROTT_INPUT_NORMAL just input data, no flip

          - ROTT_INPUT_REVESE_BYTE_BY_BYTE, input data input convert or flip byte by byte

          - ROTT_INPUT_REVESE_HALFWORD_BY_HALFWORD, the input convert or flip halfword by halfword

        - **struct** – rott_output_data_flow_t

          - ROTT_OUTPUT_NORMAL just output data, no flip outpuy

          - ROTT_OUTPUT_REVESE_HALFWORD_BY_HALFWORD, convert output data reversed(flip) halfword by halfword

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t bk_rott_block_rotate_config(uint16_t picture_xpixel, uint16_t picture_ypixel, uint16_t block_xpixel, uint16_t block_ypixel, uint16_t block_cnt)[](#_CPPv427bk_rott_block_rotate_config8uint16_t8uint16_t8uint16_t8uint16_t8uint16_t "永久链接至目标")
:   This API used config rotate param, rotate is by block, a block is max 4800 pixel,so (block_xpixel * block_ypixel) not over then 4800.

    Param

bk_err_t bk_rott_wr_addr_config(uint32_t rd_base_addr, uint32_t wr_base_addr)[](#_CPPv422bk_rott_wr_addr_config8uint32_t8uint32_t "永久链接至目标")
:   This API used config rotate src/dst addr.

    Param

bk_err_t bk_rott_wartermark_block_config(uint16_t wtmk_block)[](#_CPPv431bk_rott_wartermark_block_config8uint16_t "永久链接至目标")
:   This API used config block threshold value,must make sure you enable ROTATE_WARTERMARK_INT int.

    Usage example:

    ```
         A 640X480 picture, the param can set [640,480,80,60,64], you can set wtmk_block 32 or 16 or 48 or other less then block_cnt value
    ```

    参数
    :   **wtmk_block** – when rotate block is wtmk_block, will trigger ROTATE_WARTERMARK_INT

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t bk_rott_enable(void)[](#_CPPv414bk_rott_enablev "永久链接至目标")
:   This API used enable rotate, when rotate complete once, you should enable again to rotate.

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t bk_rott_soft_rst(void)[](#_CPPv416bk_rott_soft_rstv "永久链接至目标")
:   This API used reset ROTATE hardware logic.

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t bk_rott_isr_register([rott_isr_t](#_CPPv410rott_isr_t "rott_isr_t") rott_isr)[](#_CPPv420bk_rott_isr_register10rott_isr_t "永久链接至目标")
:   This API register rotate isr.

    Param

bk_err_t bk_rott_int_status_clear([rott_int_type_t](#_CPPv415rott_int_type_t "rott_int_type_t") int_type)[](#_CPPv424bk_rott_int_status_clear15rott_int_type_t "永久链接至目标")
:   This API used to clear int status.

    Usage example:

    ```
      if ((bk_rott_int_status_get() & ROTATE_COMPLETE_INT))
       bk_rott_int_status_clear(ROTATE_COMPLETE_INT);
    ```

    参数
    :   **-** – int type: you should used with bk_rott_int_status_get() api

    返回
    :   - BK_OK: succeed

        - others: other errors.

uint32_t bk_rott_int_status_get(void)[](#_CPPv422bk_rott_int_status_getv "永久链接至目标")
:   This API get int status.

    返回
    :   - the int status value

bk_err_t rott_config([rott_config_t](#_CPPv413rott_config_t "rott_config_t") *rott)[](#_CPPv411rott_configP13rott_config_t "永久链接至目标")
:   This API is concentrate multiple api to realize rotate config.

    Usage example:

    ```

     - you can realize only yuv to  rgb565 no rotate mode like this:
         rott.rot_mode = ROTT_ONLY_YUV2RGB565
         rott.input_addr = (void*)&yuyv_640_480[0];
         rott.output_addr = (uint8_t *)0x60000000;
         rott.input_fmt = PIXEL_FMT_YUYV;
         rott.input_flow = ROTT_INPUT_NORMAL;
         rott.output_flow = ROTT_OUTPUT_REVESE_HALFWORD_BY_HALFWORD;
         rott.picture_xpixel = 640;
         rott.picture_ypixel = 480;
         rott.block_xpixel = 80;
         rott.block_ypixel = 60;
         rott.block_cnt = 64;
         rott.watermark_blk = 32;
         rott_config(&rott);


     - you can realize only yuyv to  rgb565 rotate 270 mode like this:
         rott.rot_mode = ROTT_ROTATE270;
         rott.input_addr = (void*)&yuyv_640_480[0];
         rott.output_addr = (uint8_t *)0x60000000;
         rott.input_fmt = PIXEL_FMT_YUYV;
         rott.input_flow = ROTT_INPUT_NORMAL;
         rott.output_flow = ROTT_OUTPUT_REVESE_HALFWORD_BY_HALFWORD;
         rott.picture_xpixel = ROTT_XPIXE;
         rott.picture_ypixel = ROTT_YPIXE;
         rott.block_xpixel = ROTT_XBLOCK;
         rott.block_ypixel = ROTT_YBLOCK;
         rott.block_cnt = ROTT_BLOCK_NUM;
         rott.watermark_blk = ROTT_BLOCK_NUM >> 1;
         rott_config(&rott);


     - you can realize only  rgb565 rotate 270 mode like this:
         rott.rot_mode = ROTT_ROTATE270;
         rott.input_fmt = PIXEL_FMT_RGB565;
         rott.input_addr = XXXX;
         .................
    ```

    参数
    :   **struct** – rott_input_data_flow_t


        - those params is the same as every solo api

    返回
    :   - BK_OK: succeed

        - others: other errors.

bk_err_t bk_rott_transfer_ability([rott_trans_ability_t](#_CPPv420rott_trans_ability_t "rott_trans_ability_t") ability)[](#_CPPv424bk_rott_transfer_ability20rott_trans_ability_t "永久链接至目标")
:   set ahb master busrt len.

    参数
    :   **0:64** – word per busrt; 1:32;2:16; 3:8; 4:4


## API Typedefs[](#api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [rott_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/rott_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/rott_types.h")


### Structures[](#structures "永久链接至标题")

struct rott_config_t[](#_CPPv413rott_config_t "永久链接至目标")
:   Public Members

    media_rotate_t rot_mode[](#_CPPv4N13rott_config_t8rot_modeE "永久链接至目标")
    :   bypass rotating, only use yuv2rgb565 pixel formart convert function

    void *input_addr[](#_CPPv4N13rott_config_t10input_addrE "永久链接至目标")
    :   input data addr

    void *output_addr[](#_CPPv4N13rott_config_t11output_addrE "永久链接至目标")
    :   output data addr

    pixel_format_t input_fmt[](#_CPPv4N13rott_config_t9input_fmtE "永久链接至目标")
    :   pixel format, output rgb565 always

    [rott_input_data_flow_t](#_CPPv422rott_input_data_flow_t "rott_input_data_flow_t") input_flow[](#_CPPv4N13rott_config_t10input_flowE "永久链接至目标")
    :   input data convert or not

    [rott_output_data_flow_t](#_CPPv423rott_output_data_flow_t "rott_output_data_flow_t") output_flow[](#_CPPv4N13rott_config_t11output_flowE "永久链接至目标")
    :   output data convert or not

    uint16_t picture_xpixel[](#_CPPv4N13rott_config_t14picture_xpixelE "永久链接至目标")
    :   image width

    uint16_t picture_ypixel[](#_CPPv4N13rott_config_t14picture_ypixelE "永久链接至目标")
    :   image height

    uint16_t block_xpixel[](#_CPPv4N13rott_config_t12block_xpixelE "永久链接至目标")
    :   the following is optional, but should make sure rott_driver.c’s TABLE_ROTT_BLOCK table is include used x/y pixel image width separated block width , must be devisible by picture_xpixel

    uint16_t block_ypixel[](#_CPPv4N13rott_config_t12block_ypixelE "永久链接至目标")
    :   image height separated block height, must be devisible by picture_ypixel

    uint16_t block_cnt[](#_CPPv4N13rott_config_t9block_cntE "永久链接至目标")
    :   block counts, must be (picture_xpixel/block_xpixel)*(picture_ypixel/block_ypixel) cnt

    uint16_t watermark_blk[](#_CPPv4N13rott_config_t13watermark_blkE "永久链接至目标")
    :   if enable watermark enable, you should config watermark_blk, normally defult one-half block cnt


### Macros[](#macros "永久链接至标题")

USE_ROTT_REGISTER_CALLBACKS[](#c.USE_ROTT_REGISTER_CALLBACKS "永久链接至目标")

BK_ERR_ROTT_NOT_INIT[](#c.BK_ERR_ROTT_NOT_INIT "永久链接至目标")
:   rotate driver not init


### Type Definitions[](#type-definitions "永久链接至标题")

typedef void (*rott_isr_t)(void)[](#_CPPv410rott_isr_t "永久链接至目标")


### Enumerations[](#enumerations "永久链接至标题")

enum rott_trans_ability_t[](#_CPPv420rott_trans_ability_t "永久链接至目标")
:   *Values:*

    enumerator ROTATE_BURST_64[](#_CPPv4N20rott_trans_ability_t15ROTATE_BURST_64E "永久链接至目标")

    enumerator ROTATE_BURST_32[](#_CPPv4N20rott_trans_ability_t15ROTATE_BURST_32E "永久链接至目标")

    enumerator ROTATE_BURST_16[](#_CPPv4N20rott_trans_ability_t15ROTATE_BURST_16E "永久链接至目标")

    enumerator ROTATE_BURST_8[](#_CPPv4N20rott_trans_ability_t14ROTATE_BURST_8E "永久链接至目标")

    enumerator ROTATE_BURST_4[](#_CPPv4N20rott_trans_ability_t14ROTATE_BURST_4E "永久链接至目标")

enum rott_int_type_t[](#_CPPv415rott_int_type_t "永久链接至目标")
:   *Values:*

    enumerator ROTATE_COMPLETE_INT[](#_CPPv4N15rott_int_type_t19ROTATE_COMPLETE_INTE "永久链接至目标")
    :   rotate finish int enable

    enumerator ROTATE_WARTERMARK_INT[](#_CPPv4N15rott_int_type_t21ROTATE_WARTERMARK_INTE "永久链接至目标")
    :   rotate watermark int enable.

    enumerator ROTATE_CFG_ERR_INT[](#_CPPv4N15rott_int_type_t18ROTATE_CFG_ERR_INTE "永久链接至目标")
    :   rotate config error int enable

enum rott_input_data_flow_t[](#_CPPv422rott_input_data_flow_t "永久链接至目标")
:   *Values:*

    enumerator ROTT_INPUT_NORMAL[](#_CPPv4N22rott_input_data_flow_t17ROTT_INPUT_NORMALE "永久链接至目标")
    :   input data not flip

    enumerator ROTT_INPUT_REVESE_BYTE_BY_BYTE[](#_CPPv4N22rott_input_data_flow_t30ROTT_INPUT_REVESE_BYTE_BY_BYTEE "永久链接至目标")
    :   convert input data revese byte by byte.

    enumerator ROTT_INPUT_REVESE_HALFWORD_BY_HALFWORD[](#_CPPv4N22rott_input_data_flow_t38ROTT_INPUT_REVESE_HALFWORD_BY_HALFWORDE "永久链接至目标")
    :   convert input data revese halfword by halfword

enum rott_output_data_flow_t[](#_CPPv423rott_output_data_flow_t "永久链接至目标")
:   *Values:*

    enumerator ROTT_OUTPUT_NORMAL[](#_CPPv4N23rott_output_data_flow_t18ROTT_OUTPUT_NORMALE "永久链接至目标")
    :   output data not flip

    enumerator ROTT_OUTPUT_REVESE_HALFWORD_BY_HALFWORD[](#_CPPv4N23rott_output_data_flow_t39ROTT_OUTPUT_REVESE_HALFWORD_BY_HALFWORDE "永久链接至目标")
    :   convert output data reverse halfword by halfword
