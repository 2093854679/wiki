---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/api-reference/multi_media/bk_hw_rotate.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="rotate-apis"></a>

# Rotate APIs

<a id="rotate-interface"></a>

## Rotate Interface

旋转模块（Rotate module）主要功能是将储存在memory的yuv422图像，旋转成rgb565格式的图像，完成后储存在另一块memory中

模块共有三种工作模式：
:   1.顺时针旋转模式
    2.逆时针旋转模式
    3.不旋转只进行格式转换

    - 针对旋转，如果输入的数据时RGB565数据，那么就只执行旋转

demo运行依赖的宏配置:

| Name | Description | File | value |
| --- | --- | --- | --- |
| CONFIG\_HW\_ROTATE\_PFC | 配置Rotate功能 | `\middleware\soc\bk7236\bk7236.defconfig` | y |

<a id="rotate-categories"></a>

## Rotate Categories

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [rott\_driver.h](https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/_header_files/bk_idk/include/driver/rott_driver.h)

<a id="functions"></a>

### Functions

<a id="_CPPv419bk_rott_driver_initv"></a>

<a id="_CPPv319bk_rott_driver_initv"></a> <a id="_CPPv219bk_rott_driver_initv"></a> <a id="bk_rott_driver_init__void"></a> <a id="rott__driver_8h_1a25fbccdaffcfd3c6b2cf6c30b477b9b6"></a> bk\_err\_t bk\_rott\_driver\_init(void)
:   This API used config sysclk.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv418bk_rott_soft_resetv"></a>

<a id="_CPPv318bk_rott_soft_resetv"></a> <a id="_CPPv218bk_rott_soft_resetv"></a> <a id="bk_rott_soft_reset__void"></a> <a id="rott__driver_8h_1a6140b932ff23568ddbff072fe49e2479"></a> bk\_err\_t bk\_rott\_soft\_reset(void)
:   This API used reset rotate.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_rott_driver_deinitv"></a>

<a id="_CPPv321bk_rott_driver_deinitv"></a> <a id="_CPPv221bk_rott_driver_deinitv"></a> <a id="bk_rott_driver_deinit__void"></a> <a id="rott__driver_8h_1a54e89fbe429ddafbd7acba49c8516ecf"></a> bk\_err\_t bk\_rott\_driver\_deinit(void)
:   This API used disable rotate cpu int.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv418bk_rott_int_enable15rott_int_type_tb"></a>

<a id="_CPPv318bk_rott_int_enable15rott_int_type_tb"></a> <a id="_CPPv218bk_rott_int_enable15rott_int_type_tb"></a> <a id="bk_rott_int_enable__rott_int_type_t.b"></a> <a id="rott__driver_8h_1ab27dc2112f51781cfde86222aa248d8c"></a> bk\_err\_t bk\_rott\_int\_enable([rott\_int\_type\_t](#_CPPv415rott_int_type_t "rott_int_type_t") int\_type, bool en)
:   This API used to config rotate int type and int enable.

    参数
    :   **1:int\_type** – include:

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
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv426bk_rott_block_delay_configb8uint16_t8uint16_t"></a>

<a id="_CPPv326bk_rott_block_delay_configb8uint16_t8uint16_t"></a> <a id="_CPPv226bk_rott_block_delay_configb8uint16_t8uint16_t"></a> <a id="bk_rott_block_delay_config__b.uint16_t.uint16_t"></a> <a id="rott__driver_8h_1a3c794378d18ef231a7eb89acf606be5b"></a> bk\_err\_t bk\_rott\_block\_delay\_config(bool en, uint16\_t delay\_hclk\_count1, uint16\_t delay\_hclk\_count2)
:   This API used config rotate delay cycle in block and block interval.

    参数
    :   **\-** – en,enable the delay function

        - delay\_hclk\_count1 (range 0 \~ 0x7fff), the delay pclk cycle is calculate by (delay\_hclk\_count1 \* delay\_hclk\_count2)
        - delay\_hclk\_count2 (range 0 \~ 0xffff), the delay pclk cycle is calculate by (delay\_hclk\_count1 \* delay\_hclk\_count2)

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv419bk_rott_mode_config14media_rotate_t"></a>

<a id="_CPPv319bk_rott_mode_config14media_rotate_t"></a> <a id="_CPPv219bk_rott_mode_config14media_rotate_t"></a> <a id="bk_rott_mode_config__media_rotate_t"></a> <a id="rott__driver_8h_1a0b9784cf116385cbad6bfbb1ef39d489"></a> bk\_err\_t bk\_rott\_mode\_config(media\_rotate\_t rot\_mode)
:   This API used config rotate mode.

    参数
    :   **struct** – rott\_mode\_t

        - ROTT\_ONLY\_YUV2RGB565, only use yuv data pixel convert to rgb565 pixel, no rotate
        - ROTT\_ROTATE90, if rot\_input\_fmt \= RGB565, just rotate; if rot\_input\_fmt \= yuv, not only rotate but convert to rgb565.
        - ROTT\_ROTATE170,if rot\_input\_fmt \= RGB565, just rotate; if rot\_input\_fmt \= yuv, not only rotate but convert to rgb565.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv425bk_rott_input_data_format14pixel_format_t"></a>

<a id="_CPPv325bk_rott_input_data_format14pixel_format_t"></a> <a id="_CPPv225bk_rott_input_data_format14pixel_format_t"></a> <a id="bk_rott_input_data_format__pixel_format_t"></a> <a id="rott__driver_8h_1a5675a576854c134bb6af363ce7274848"></a> bk\_err\_t bk\_rott\_input\_data\_format(pixel\_format\_t rot\_input\_fmt)
:   This API used config input data format, output data format is default rgb565.

    **Attention**
    :   if your data rotate or pixel convert not display normally,you can use api bk\_rott\_data\_reverse modify input/output data flow to see see

    参数
    :   **struct** – rott\_input\_fmt\_t

        - RGB565, input format is rgb565 be
        - RGB565le, input format is rgb565 le
        - ROTT\_FMT\_YUYV
        - ROTT\_FMT\_VUYY
        - others

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_rott_data_reverse22rott_input_data_flow_t23rott_output_data_flow_t"></a>

<a id="_CPPv320bk_rott_data_reverse22rott_input_data_flow_t23rott_output_data_flow_t"></a> <a id="_CPPv220bk_rott_data_reverse22rott_input_data_flow_t23rott_output_data_flow_t"></a> <a id="bk_rott_data_reverse__rott_input_data_flow_t.rott_output_data_flow_t"></a> <a id="rott__driver_8h_1a990d7b7e767a4c35d29edc3e45361f9b"></a> bk\_err\_t bk\_rott\_data\_reverse([rott\_input\_data\_flow\_t](#_CPPv422rott_input_data_flow_t "rott_input_data_flow_t") input\_flow, [rott\_output\_data\_flow\_t](#_CPPv423rott_output_data_flow_t "rott_output_data_flow_t") output\_flow)
:   This API used config input data or output data flip(reverse)

    **Attention**
    :   if your data rotate or pixel convert not display normally,you can use api bk\_rott\_data\_reverse modify input/output data flow to see see

    参数
    :   - **struct** – rott\_input\_data\_flow\_t

          - ROTT\_INPUT\_NORMAL just input data, no flip
          - ROTT\_INPUT\_REVESE\_BYTE\_BY\_BYTE, input data input convert or flip byte by byte
          - ROTT\_INPUT\_REVESE\_HALFWORD\_BY\_HALFWORD, the input convert or flip halfword by halfword
        - **struct** – rott\_output\_data\_flow\_t

          - ROTT\_OUTPUT\_NORMAL just output data, no flip outpuy
          - ROTT\_OUTPUT\_REVESE\_HALFWORD\_BY\_HALFWORD, convert output data reversed(flip) halfword by halfword

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv427bk_rott_block_rotate_config8uint16_t8uint16_t8uint16_t8uint16_t8uint16_t"></a>

<a id="_CPPv327bk_rott_block_rotate_config8uint16_t8uint16_t8uint16_t8uint16_t8uint16_t"></a> <a id="_CPPv227bk_rott_block_rotate_config8uint16_t8uint16_t8uint16_t8uint16_t8uint16_t"></a> <a id="bk_rott_block_rotate_config__uint16_t.uint16_t.uint16_t.uint16_t.uint16_t"></a> <a id="rott__driver_8h_1ac0bc9a227b2e226ade5f29abf38c365d"></a> bk\_err\_t bk\_rott\_block\_rotate\_config(uint16\_t picture\_xpixel, uint16\_t picture\_ypixel, uint16\_t block\_xpixel, uint16\_t block\_ypixel, uint16\_t block\_cnt)
:   This API used config rotate param, rotate is by block, a block is max 4800 pixel,so (block\_xpixel \* block\_ypixel) not over then 4800\.

    Param

<a id="_CPPv422bk_rott_wr_addr_config8uint32_t8uint32_t"></a>

<a id="_CPPv322bk_rott_wr_addr_config8uint32_t8uint32_t"></a> <a id="_CPPv222bk_rott_wr_addr_config8uint32_t8uint32_t"></a> <a id="bk_rott_wr_addr_config__uint32_t.uint32_t"></a> <a id="rott__driver_8h_1ab040a1cb39d35a19005d1abdfe967b01"></a> bk\_err\_t bk\_rott\_wr\_addr\_config(uint32\_t rd\_base\_addr, uint32\_t wr\_base\_addr)
:   This API used config rotate src/dst addr.

    Param

<a id="_CPPv431bk_rott_wartermark_block_config8uint16_t"></a>

<a id="_CPPv331bk_rott_wartermark_block_config8uint16_t"></a> <a id="_CPPv231bk_rott_wartermark_block_config8uint16_t"></a> <a id="bk_rott_wartermark_block_config__uint16_t"></a> <a id="rott__driver_8h_1ac54530e1d40aae99872aaf35154a3898"></a> bk\_err\_t bk\_rott\_wartermark\_block\_config(uint16\_t wtmk\_block)
:   This API used config block threshold value,must make sure you enable ROTATE\_WARTERMARK\_INT int.

    Usage example:

    ```
         A 640X480 picture, the param can set [640,480,80,60,64], you can set wtmk_block 32 or 16 or 48 or other less then block_cnt value
    ```

    参数
    :   **wtmk\_block** – when rotate block is wtmk\_block, will trigger ROTATE\_WARTERMARK\_INT

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv414bk_rott_enablev"></a>

<a id="_CPPv314bk_rott_enablev"></a> <a id="_CPPv214bk_rott_enablev"></a> <a id="bk_rott_enable__void"></a> <a id="rott__driver_8h_1aaf6e0dd947f999d0b6bedf1e0f18f85e"></a> bk\_err\_t bk\_rott\_enable(void)
:   This API used enable rotate, when rotate complete once, you should enable again to rotate.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv416bk_rott_soft_rstv"></a>

<a id="_CPPv316bk_rott_soft_rstv"></a> <a id="_CPPv216bk_rott_soft_rstv"></a> <a id="bk_rott_soft_rst__void"></a> <a id="rott__driver_8h_1acdea40908440aef4773f1151c747c2c2"></a> bk\_err\_t bk\_rott\_soft\_rst(void)
:   This API used reset ROTATE hardware logic.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_rott_isr_register10rott_isr_t"></a>

<a id="_CPPv320bk_rott_isr_register10rott_isr_t"></a> <a id="_CPPv220bk_rott_isr_register10rott_isr_t"></a> <a id="bk_rott_isr_register__rott_isr_t"></a> <a id="rott__driver_8h_1af6ca606a7b8f66a4c93e93cb6b96eab0"></a> bk\_err\_t bk\_rott\_isr\_register([rott\_isr\_t](#_CPPv410rott_isr_t "rott_isr_t") rott\_isr)
:   This API register rotate isr.

    Param

<a id="_CPPv424bk_rott_int_status_clear15rott_int_type_t"></a>

<a id="_CPPv324bk_rott_int_status_clear15rott_int_type_t"></a> <a id="_CPPv224bk_rott_int_status_clear15rott_int_type_t"></a> <a id="bk_rott_int_status_clear__rott_int_type_t"></a> <a id="rott__driver_8h_1ab3f3f18f666784799c16d5e07e7aa688"></a> bk\_err\_t bk\_rott\_int\_status\_clear([rott\_int\_type\_t](#_CPPv415rott_int_type_t "rott_int_type_t") int\_type)
:   This API used to clear int status.

    Usage example:

    ```
      if ((bk_rott_int_status_get() & ROTATE_COMPLETE_INT))
       bk_rott_int_status_clear(ROTATE_COMPLETE_INT);
    ```

    参数
    :   **\-** – int type: you should used with bk\_rott\_int\_status\_get() api

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv422bk_rott_int_status_getv"></a>

<a id="_CPPv322bk_rott_int_status_getv"></a> <a id="_CPPv222bk_rott_int_status_getv"></a> <a id="bk_rott_int_status_get__void"></a> <a id="rott__driver_8h_1a3dab7b623b28859e66b40add40412964"></a> uint32\_t bk\_rott\_int\_status\_get(void)
:   This API get int status.

    返回
    :   - the int status value

<a id="_CPPv411rott_configP13rott_config_t"></a>

<a id="_CPPv311rott_configP13rott_config_t"></a> <a id="_CPPv211rott_configP13rott_config_t"></a> <a id="rott_config__rott_config_tP"></a> <a id="rott__driver_8h_1acf4472edb176523ad96fff3bea3c9ace"></a> bk\_err\_t rott\_config([rott\_config\_t](#_CPPv413rott_config_t "rott_config_t") \*rott)
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
    :   **struct** – rott\_input\_data\_flow\_t

        - those params is the same as every solo api

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_rott_transfer_ability20rott_trans_ability_t"></a>

<a id="_CPPv324bk_rott_transfer_ability20rott_trans_ability_t"></a> <a id="_CPPv224bk_rott_transfer_ability20rott_trans_ability_t"></a> <a id="bk_rott_transfer_ability__rott_trans_ability_t"></a> <a id="rott__driver_8h_1a7b6e921e04adfb7f252a42213b5b09b4"></a> bk\_err\_t bk\_rott\_transfer\_ability([rott\_trans\_ability\_t](#_CPPv420rott_trans_ability_t "rott_trans_ability_t") ability)
:   set ahb master busrt len.

    参数
    :   **0:64** – word per busrt; 1:32;2:16; 3:8; 4:4

<a id="api-typedefs"></a>

## API Typedefs

<a id="id1"></a>

### Header File

- [rott\_types.h](https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/_header_files/bk_idk/include/driver/rott_types.h)

<a id="structures"></a>

### Structures

<a id="_CPPv413rott_config_t"></a>

<a id="_CPPv313rott_config_t"></a> <a id="_CPPv213rott_config_t"></a> <a id="rott_config_t"></a> <a id="structrott__config__t"></a> struct rott\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N13rott_config_t8rot_modeE"></a>

    <a id="_CPPv3N13rott_config_t8rot_modeE"></a> <a id="_CPPv2N13rott_config_t8rot_modeE"></a> <a id="rott_config_t::rot_mode__media_rotate_t"></a> <a id="structrott__config__t_1a6033aa0d8ac3efea14051412c208986d"></a> media\_rotate\_t rot\_mode
    :   bypass rotating, only use yuv2rgb565 pixel formart convert function

    <a id="_CPPv4N13rott_config_t10input_addrE"></a>

    <a id="_CPPv3N13rott_config_t10input_addrE"></a> <a id="_CPPv2N13rott_config_t10input_addrE"></a> <a id="rott_config_t::input_addr__voidP"></a> <a id="structrott__config__t_1aa1a99f790ad326e381c71778cfec0fd5"></a> void \*input\_addr
    :   input data addr

    <a id="_CPPv4N13rott_config_t11output_addrE"></a>

    <a id="_CPPv3N13rott_config_t11output_addrE"></a> <a id="_CPPv2N13rott_config_t11output_addrE"></a> <a id="rott_config_t::output_addr__voidP"></a> <a id="structrott__config__t_1a5de204524256bb41092a81a467b221a8"></a> void \*output\_addr
    :   output data addr

    <a id="_CPPv4N13rott_config_t9input_fmtE"></a>

    <a id="_CPPv3N13rott_config_t9input_fmtE"></a> <a id="_CPPv2N13rott_config_t9input_fmtE"></a> <a id="rott_config_t::input_fmt__pixel_format_t"></a> <a id="structrott__config__t_1a10c82432f4f5dafbcd0f86ab9d8297e8"></a> pixel\_format\_t input\_fmt
    :   pixel format, output rgb565 always

    <a id="_CPPv4N13rott_config_t10input_flowE"></a>

    <a id="_CPPv3N13rott_config_t10input_flowE"></a> <a id="_CPPv2N13rott_config_t10input_flowE"></a> <a id="rott_config_t::input_flow__rott_input_data_flow_t"></a> <a id="structrott__config__t_1a1c37f41d9e7ff89a15f3517d8f7af717"></a> [rott\_input\_data\_flow\_t](#_CPPv422rott_input_data_flow_t "rott_input_data_flow_t") input\_flow
    :   input data convert or not

    <a id="_CPPv4N13rott_config_t11output_flowE"></a>

    <a id="_CPPv3N13rott_config_t11output_flowE"></a> <a id="_CPPv2N13rott_config_t11output_flowE"></a> <a id="rott_config_t::output_flow__rott_output_data_flow_t"></a> <a id="structrott__config__t_1a80b048c2793a1f7b3d95f3b9b4fa93db"></a> [rott\_output\_data\_flow\_t](#_CPPv423rott_output_data_flow_t "rott_output_data_flow_t") output\_flow
    :   output data convert or not

    <a id="_CPPv4N13rott_config_t14picture_xpixelE"></a>

    <a id="_CPPv3N13rott_config_t14picture_xpixelE"></a> <a id="_CPPv2N13rott_config_t14picture_xpixelE"></a> <a id="rott_config_t::picture_xpixel__uint16_t"></a> <a id="structrott__config__t_1a5df6c5fdedf032119b47ee482c9bba5a"></a> uint16\_t picture\_xpixel
    :   image width

    <a id="_CPPv4N13rott_config_t14picture_ypixelE"></a>

    <a id="_CPPv3N13rott_config_t14picture_ypixelE"></a> <a id="_CPPv2N13rott_config_t14picture_ypixelE"></a> <a id="rott_config_t::picture_ypixel__uint16_t"></a> <a id="structrott__config__t_1a47123d1a9d8993c3b4709c1406afe009"></a> uint16\_t picture\_ypixel
    :   image height

    <a id="_CPPv4N13rott_config_t12block_xpixelE"></a>

    <a id="_CPPv3N13rott_config_t12block_xpixelE"></a> <a id="_CPPv2N13rott_config_t12block_xpixelE"></a> <a id="rott_config_t::block_xpixel__uint16_t"></a> <a id="structrott__config__t_1a4f6042d62d86697e04fffcf0a9c5d811"></a> uint16\_t block\_xpixel
    :   the following is optional, but should make sure rott\_driver.c’s TABLE\_ROTT\_BLOCK table is include used x/y pixel image width separated block width , must be devisible by picture\_xpixel

    <a id="_CPPv4N13rott_config_t12block_ypixelE"></a>

    <a id="_CPPv3N13rott_config_t12block_ypixelE"></a> <a id="_CPPv2N13rott_config_t12block_ypixelE"></a> <a id="rott_config_t::block_ypixel__uint16_t"></a> <a id="structrott__config__t_1a4719fca92edbbf377c9495271f09854a"></a> uint16\_t block\_ypixel
    :   image height separated block height, must be devisible by picture\_ypixel

    <a id="_CPPv4N13rott_config_t9block_cntE"></a>

    <a id="_CPPv3N13rott_config_t9block_cntE"></a> <a id="_CPPv2N13rott_config_t9block_cntE"></a> <a id="rott_config_t::block_cnt__uint16_t"></a> <a id="structrott__config__t_1ae5ff3d5a34682b7cd75dc4806db1ebdc"></a> uint16\_t block\_cnt
    :   block counts, must be (picture\_xpixel/block\_xpixel)\*(picture\_ypixel/block\_ypixel) cnt

    <a id="_CPPv4N13rott_config_t13watermark_blkE"></a>

    <a id="_CPPv3N13rott_config_t13watermark_blkE"></a> <a id="_CPPv2N13rott_config_t13watermark_blkE"></a> <a id="rott_config_t::watermark_blk__uint16_t"></a> <a id="structrott__config__t_1a9e981d9da930e69b1b1b3145341d05d0"></a> uint16\_t watermark\_blk
    :   if enable watermark enable, you should config watermark\_blk, normally defult one-half block cnt

<a id="macros"></a>

### Macros

<a id="c.USE_ROTT_REGISTER_CALLBACKS"></a>

<a id="rott__types_8h_1a22e91759f64ea51b9df79cfec92324f7"></a> USE\_ROTT\_REGISTER\_CALLBACKS

<a id="c.BK_ERR_ROTT_NOT_INIT"></a>

<a id="rott__types_8h_1a541f36033fee2a229e494d64035713e8"></a> BK\_ERR\_ROTT\_NOT\_INIT
:   rotate driver not init

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv410rott_isr_t"></a>

<a id="_CPPv310rott_isr_t"></a> <a id="_CPPv210rott_isr_t"></a> <a id="rott_isr_t"></a> <a id="rott__types_8h_1a76273d97dcd877148e1e52bcf4d7ce2f"></a> typedef void (\*rott\_isr\_t)(void)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv420rott_trans_ability_t"></a>

<a id="_CPPv320rott_trans_ability_t"></a> <a id="_CPPv220rott_trans_ability_t"></a> <a id="rott__types_8h_1a8cde02af1cf5a4d8f1ef4c3ca9709708"></a> enum rott\_trans\_ability\_t
:   *Values:*

    <a id="_CPPv4N20rott_trans_ability_t15ROTATE_BURST_64E"></a>

    <a id="_CPPv3N20rott_trans_ability_t15ROTATE_BURST_64E"></a> <a id="_CPPv2N20rott_trans_ability_t15ROTATE_BURST_64E"></a> <a id="rott__types_8h_1a8cde02af1cf5a4d8f1ef4c3ca9709708a56c7abfa3fe558760eaf791a9018bc3a"></a> enumerator ROTATE\_BURST\_64

    <a id="_CPPv4N20rott_trans_ability_t15ROTATE_BURST_32E"></a>

    <a id="_CPPv3N20rott_trans_ability_t15ROTATE_BURST_32E"></a> <a id="_CPPv2N20rott_trans_ability_t15ROTATE_BURST_32E"></a> <a id="rott__types_8h_1a8cde02af1cf5a4d8f1ef4c3ca9709708a9a87bb3c6dbda0e10fb7b06cf26c2f99"></a> enumerator ROTATE\_BURST\_32

    <a id="_CPPv4N20rott_trans_ability_t15ROTATE_BURST_16E"></a>

    <a id="_CPPv3N20rott_trans_ability_t15ROTATE_BURST_16E"></a> <a id="_CPPv2N20rott_trans_ability_t15ROTATE_BURST_16E"></a> <a id="rott__types_8h_1a8cde02af1cf5a4d8f1ef4c3ca9709708a0c5b1150a41c4d6a9948df3b8a7c2279"></a> enumerator ROTATE\_BURST\_16

    <a id="_CPPv4N20rott_trans_ability_t14ROTATE_BURST_8E"></a>

    <a id="_CPPv3N20rott_trans_ability_t14ROTATE_BURST_8E"></a> <a id="_CPPv2N20rott_trans_ability_t14ROTATE_BURST_8E"></a> <a id="rott__types_8h_1a8cde02af1cf5a4d8f1ef4c3ca9709708acf46fb2b51580229d2e47bc01e8e8780"></a> enumerator ROTATE\_BURST\_8

    <a id="_CPPv4N20rott_trans_ability_t14ROTATE_BURST_4E"></a>

    <a id="_CPPv3N20rott_trans_ability_t14ROTATE_BURST_4E"></a> <a id="_CPPv2N20rott_trans_ability_t14ROTATE_BURST_4E"></a> <a id="rott__types_8h_1a8cde02af1cf5a4d8f1ef4c3ca9709708a7ff991db89203d866cfad7da4207799c"></a> enumerator ROTATE\_BURST\_4

<a id="_CPPv415rott_int_type_t"></a>

<a id="_CPPv315rott_int_type_t"></a> <a id="_CPPv215rott_int_type_t"></a> <a id="rott__types_8h_1a6cd15260f5140b5c4f595e3bb051cea1"></a> enum rott\_int\_type\_t
:   *Values:*

    <a id="_CPPv4N15rott_int_type_t19ROTATE_COMPLETE_INTE"></a>

    <a id="_CPPv3N15rott_int_type_t19ROTATE_COMPLETE_INTE"></a> <a id="_CPPv2N15rott_int_type_t19ROTATE_COMPLETE_INTE"></a> <a id="rott__types_8h_1a6cd15260f5140b5c4f595e3bb051cea1a2dc05bc066e634af4a1c4787432f94de"></a> enumerator ROTATE\_COMPLETE\_INT
    :   rotate finish int enable

    <a id="_CPPv4N15rott_int_type_t21ROTATE_WARTERMARK_INTE"></a>

    <a id="_CPPv3N15rott_int_type_t21ROTATE_WARTERMARK_INTE"></a> <a id="_CPPv2N15rott_int_type_t21ROTATE_WARTERMARK_INTE"></a> <a id="rott__types_8h_1a6cd15260f5140b5c4f595e3bb051cea1a0418381a5946702f8cabca3b306835ae"></a> enumerator ROTATE\_WARTERMARK\_INT
    :   rotate watermark int enable.

    <a id="_CPPv4N15rott_int_type_t18ROTATE_CFG_ERR_INTE"></a>

    <a id="_CPPv3N15rott_int_type_t18ROTATE_CFG_ERR_INTE"></a> <a id="_CPPv2N15rott_int_type_t18ROTATE_CFG_ERR_INTE"></a> <a id="rott__types_8h_1a6cd15260f5140b5c4f595e3bb051cea1a8c2e2aed4fb75d5d8664d5aa33b10d87"></a> enumerator ROTATE\_CFG\_ERR\_INT
    :   rotate config error int enable

<a id="_CPPv422rott_input_data_flow_t"></a>

<a id="_CPPv322rott_input_data_flow_t"></a> <a id="_CPPv222rott_input_data_flow_t"></a> <a id="rott__types_8h_1a9cc4e06581e30f0933fc5bac6ee52d7b"></a> enum rott\_input\_data\_flow\_t
:   *Values:*

    <a id="_CPPv4N22rott_input_data_flow_t17ROTT_INPUT_NORMALE"></a>

    <a id="_CPPv3N22rott_input_data_flow_t17ROTT_INPUT_NORMALE"></a> <a id="_CPPv2N22rott_input_data_flow_t17ROTT_INPUT_NORMALE"></a> <a id="rott__types_8h_1a9cc4e06581e30f0933fc5bac6ee52d7ba2b690b87d281c6ee6adfd0c7de0bce97"></a> enumerator ROTT\_INPUT\_NORMAL
    :   input data not flip

    <a id="_CPPv4N22rott_input_data_flow_t30ROTT_INPUT_REVESE_BYTE_BY_BYTEE"></a>

    <a id="_CPPv3N22rott_input_data_flow_t30ROTT_INPUT_REVESE_BYTE_BY_BYTEE"></a> <a id="_CPPv2N22rott_input_data_flow_t30ROTT_INPUT_REVESE_BYTE_BY_BYTEE"></a> <a id="rott__types_8h_1a9cc4e06581e30f0933fc5bac6ee52d7ba8e9b829515d4104802095191c325a820"></a> enumerator ROTT\_INPUT\_REVESE\_BYTE\_BY\_BYTE
    :   convert input data revese byte by byte.

    <a id="_CPPv4N22rott_input_data_flow_t38ROTT_INPUT_REVESE_HALFWORD_BY_HALFWORDE"></a>

    <a id="_CPPv3N22rott_input_data_flow_t38ROTT_INPUT_REVESE_HALFWORD_BY_HALFWORDE"></a> <a id="_CPPv2N22rott_input_data_flow_t38ROTT_INPUT_REVESE_HALFWORD_BY_HALFWORDE"></a> <a id="rott__types_8h_1a9cc4e06581e30f0933fc5bac6ee52d7ba9a521e32a167e5ab7621722281ba9ffc"></a> enumerator ROTT\_INPUT\_REVESE\_HALFWORD\_BY\_HALFWORD
    :   convert input data revese halfword by halfword

<a id="_CPPv423rott_output_data_flow_t"></a>

<a id="_CPPv323rott_output_data_flow_t"></a> <a id="_CPPv223rott_output_data_flow_t"></a> <a id="rott__types_8h_1a9f416f5dad5df17a76df39b8dd4cd25c"></a> enum rott\_output\_data\_flow\_t
:   *Values:*

    <a id="_CPPv4N23rott_output_data_flow_t18ROTT_OUTPUT_NORMALE"></a>

    <a id="_CPPv3N23rott_output_data_flow_t18ROTT_OUTPUT_NORMALE"></a> <a id="_CPPv2N23rott_output_data_flow_t18ROTT_OUTPUT_NORMALE"></a> <a id="rott__types_8h_1a9f416f5dad5df17a76df39b8dd4cd25ca9ab0214ffdd65c6e60c4d9fc39fb7906"></a> enumerator ROTT\_OUTPUT\_NORMAL
    :   output data not flip

    <a id="_CPPv4N23rott_output_data_flow_t39ROTT_OUTPUT_REVESE_HALFWORD_BY_HALFWORDE"></a>

    <a id="_CPPv3N23rott_output_data_flow_t39ROTT_OUTPUT_REVESE_HALFWORD_BY_HALFWORDE"></a> <a id="_CPPv2N23rott_output_data_flow_t39ROTT_OUTPUT_REVESE_HALFWORD_BY_HALFWORDE"></a> <a id="rott__types_8h_1a9f416f5dad5df17a76df39b8dd4cd25cacc1f41aa018f809afdc918a325b6ff0c"></a> enumerator ROTT\_OUTPUT\_REVESE\_HALFWORD\_BY\_HALFWORD
    :   convert output data reverse halfword by halfword
