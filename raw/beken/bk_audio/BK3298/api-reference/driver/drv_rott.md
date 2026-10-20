---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_rott.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-rott"></a>

# DRV\_ROTT

<a id="drv-rott-api-status"></a>

## DRV\_ROTT API Status

| API |
| --- |
| [`drv_rott_init()`](#_CPPv413drv_rott_initv "drv_rott_init") |
| [`drv_rott_deinit()`](#_CPPv415drv_rott_deinitv "drv_rott_deinit") |
| [`drv_rott_config()`](#_CPPv415drv_rott_configP13rott_config_t "drv_rott_config") |
| [`drv_rott_start()`](#_CPPv414drv_rott_startv "drv_rott_start") |
| [`drv_rott_int_enable()`](#_CPPv419drv_rott_int_enable15rott_int_type_eb "drv_rott_int_enable") |
| [`drv_rott_int_cbk_register()`](#_CPPv425drv_rott_int_cbk_register15rott_int_type_e19pfunc_drv_rott_cb_t "drv_rott_int_cbk_register") |

<a id="drv-rott-api-reference"></a>

## DRV\_ROTT API Reference

<a id="header-file"></a>

### Header File

- [driver/rott/drv\_rott.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/rott/drv_rott.h)

<a id="functions"></a>

### Functions

<a id="_CPPv413drv_rott_initv"></a>

<a id="_CPPv313drv_rott_initv"></a> <a id="_CPPv213drv_rott_initv"></a> <a id="drv_rott_init__void"></a> <a id="drv__rott_8h_1a314378d0fed86dcf734bd7dde2d0e618"></a> int32\_t drv\_rott\_init(void)
:   init a rotate device.

    rotate硬件加速器初始化，在使用rotate功能前需要调用

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv415drv_rott_deinitv"></a>

<a id="_CPPv315drv_rott_deinitv"></a> <a id="_CPPv215drv_rott_deinitv"></a> <a id="drv_rott_deinit__void"></a> <a id="drv__rott_8h_1a8e376fd69e315467a8b2e1d513204158"></a> int32\_t drv\_rott\_deinit(void)
:   deinit a rotate device.

    反初始化rotate硬件加速器，对drv\_rott\_init()进行反向操作

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv415drv_rott_configP13rott_config_t"></a>

<a id="_CPPv315drv_rott_configP13rott_config_t"></a> <a id="_CPPv215drv_rott_configP13rott_config_t"></a> <a id="drv_rott_config__rott_config_tP"></a> <a id="drv__rott_8h_1a0f2b7ce9b55898e2dd25ad4c8865e05c"></a> int32\_t drv\_rott\_config([rott\_config\_t](#_CPPv413rott_config_t "rott_config_t") \*p\_config)
:   config rotate parameter

    - ROTT\_ONLY\_YUV2RGB565, only use yuv data pixel convert to rgb565 pixel, no rotate

      - ROTT\_ROTATE90, if rot\_input\_fmt \= RGB565, just rotate; if rot\_input\_fmt \= yuv, not only rotate but convert to rgb565.
      - ROTT\_ROTATE170,if rot\_input\_fmt \= RGB565, just rotate; if rot\_input\_fmt \= yuv, not only rotate but convert to rgb565.

    参数:
    :   **p\_config** – **\[in\]** 参考rott\_config\_t结构体

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv414drv_rott_startv"></a>

<a id="_CPPv314drv_rott_startv"></a> <a id="_CPPv214drv_rott_startv"></a> <a id="drv_rott_start__void"></a> <a id="drv__rott_8h_1a5b39e0c6ee9f5b50b70aaa3fa13749a1"></a> int32\_t drv\_rott\_start(void)
:   start rotate work

    开始硬件加速

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419drv_rott_int_enable15rott_int_type_eb"></a>

<a id="_CPPv319drv_rott_int_enable15rott_int_type_eb"></a> <a id="_CPPv219drv_rott_int_enable15rott_int_type_eb"></a> <a id="drv_rott_int_enable__rott_int_type_e.b"></a> <a id="drv__rott_8h_1ae2a7ab0c1adc277af0eeb182a316d6cb"></a> int32\_t drv\_rott\_int\_enable([rott\_int\_type\_e](#_CPPv415rott_int_type_e "rott_int_type_e") int\_type, bool en)
:   This API used to config rotate int type and int enable.

    参数:
    :   - **int\_type** – **\[in\]** int\_type include:

          ```
                 - ROTATE_COMPLETE_INT: rotate complete int
                 - ROTATE_WARTERMARK_INT: if enable, wtmk_block need config, and not set 0, you can set wtmk_block by api bk_rott_wartermark_block_config config or rott_config
                 - ROTATE_CFG_ERR_INT, the following will trigger cfg err int,like:
                                  - picture_xpixel & picture_ypixel be zero while working.
                                  - ROTATE_WARTERMARK_INT=1, but wtmk_block=0
                                  - block_cnt=0
                                  - block_xpixel > picture_xpixel,  block_ypixel > picture_ypixel
          ```
        - **en** – **\[in\]** en enable or disable

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425drv_rott_int_cbk_register15rott_int_type_e19pfunc_drv_rott_cb_t"></a>

<a id="_CPPv325drv_rott_int_cbk_register15rott_int_type_e19pfunc_drv_rott_cb_t"></a> <a id="_CPPv225drv_rott_int_cbk_register15rott_int_type_e19pfunc_drv_rott_cb_t"></a> <a id="drv_rott_int_cbk_register__rott_int_type_e.pfunc_drv_rott_cb_t"></a> <a id="drv__rott_8h_1a1e92c8cb272e93ba594a61967dd6c738"></a> int32\_t drv\_rott\_int\_cbk\_register([rott\_int\_type\_e](#_CPPv415rott_int_type_e "rott_int_type_e") int\_type, [pfunc\_drv\_rott\_cb\_t](#_CPPv419pfunc_drv_rott_cb_t "pfunc_drv_rott_cb_t") pfn\_cb)
:   register intrrupt callback function

    注册中断回调函数

    参数:
    :   - **int\_type** – **\[in\]** \- ROTATE\_COMPLETE\_INT \= 1 \<\< 0, rotate finish int enable

          - ROTATE\_WARTERMARK\_INT \= 1 \<\< 1, rotate watermark int enable
          - ROTATE\_CFG\_ERR\_INT \= 1 \<\< 2, rotate config error int enable
        - **pfn\_cb** – **\[in\]** 回调函数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv413rott_config_t"></a>

<a id="_CPPv313rott_config_t"></a> <a id="_CPPv213rott_config_t"></a> <a id="rott_config_t"></a> <a id="structrott__config__t"></a> struct rott\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N13rott_config_t8rot_modeE"></a>

    <a id="_CPPv3N13rott_config_t8rot_modeE"></a> <a id="_CPPv2N13rott_config_t8rot_modeE"></a> <a id="rott_config_t::rot_mode__rott_mode_e"></a> <a id="structrott__config__t_1ad951107ab9b1d3c8e1413f34938d9ff6"></a> [rott\_mode\_e](#_CPPv411rott_mode_e "rott_mode_e") rot\_mode
    :   bypass rotating, only use yuv2rgb565 pixel formart convert function

    <a id="_CPPv4N13rott_config_t10input_addrE"></a>

    <a id="_CPPv3N13rott_config_t10input_addrE"></a> <a id="_CPPv2N13rott_config_t10input_addrE"></a> <a id="rott_config_t::input_addr__voidP"></a> <a id="structrott__config__t_1aa1a99f790ad326e381c71778cfec0fd5"></a> void \*input\_addr
    :   input data addr

    <a id="_CPPv4N13rott_config_t11output_addrE"></a>

    <a id="_CPPv3N13rott_config_t11output_addrE"></a> <a id="_CPPv2N13rott_config_t11output_addrE"></a> <a id="rott_config_t::output_addr__voidP"></a> <a id="structrott__config__t_1a5de204524256bb41092a81a467b221a8"></a> void \*output\_addr
    :   output data addr

    <a id="_CPPv4N13rott_config_t9input_fmtE"></a>

    <a id="_CPPv3N13rott_config_t9input_fmtE"></a> <a id="_CPPv2N13rott_config_t9input_fmtE"></a> <a id="rott_config_t::input_fmt__rott_pixel_format_e"></a> <a id="structrott__config__t_1a8ed6eb892e8bbc087a0f96f35d2021da"></a> [rott\_pixel\_format\_e](#_CPPv419rott_pixel_format_e "rott_pixel_format_e") input\_fmt
    :   pixel format, output rgb565 always

    <a id="_CPPv4N13rott_config_t10input_flowE"></a>

    <a id="_CPPv3N13rott_config_t10input_flowE"></a> <a id="_CPPv2N13rott_config_t10input_flowE"></a> <a id="rott_config_t::input_flow__rott_input_data_flow_e"></a> <a id="structrott__config__t_1a0a9ae36af5555292df287e50a80d9f04"></a> [rott\_input\_data\_flow\_e](#_CPPv422rott_input_data_flow_e "rott_input_data_flow_e") input\_flow
    :   input data convert or not

    <a id="_CPPv4N13rott_config_t11output_flowE"></a>

    <a id="_CPPv3N13rott_config_t11output_flowE"></a> <a id="_CPPv2N13rott_config_t11output_flowE"></a> <a id="rott_config_t::output_flow__rott_output_data_flow_e"></a> <a id="structrott__config__t_1a3d47715006d98afa32119fe689f05be0"></a> [rott\_output\_data\_flow\_e](#_CPPv423rott_output_data_flow_e "rott_output_data_flow_e") output\_flow
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

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv419pfunc_drv_rott_cb_t"></a>

<a id="_CPPv319pfunc_drv_rott_cb_t"></a> <a id="_CPPv219pfunc_drv_rott_cb_t"></a> <a id="pfunc_drv_rott_cb_t"></a> <a id="drv__rott_8h_1a3b0a50f266af1ed797abd595ef2a8047"></a> typedef void (\*pfunc\_drv\_rott\_cb\_t)(void)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv415rott_int_type_e"></a>

<a id="_CPPv315rott_int_type_e"></a> <a id="_CPPv215rott_int_type_e"></a> <a id="drv__rott_8h_1adad0cede3b9fc366ba61c22da5e75cdd"></a> enum rott\_int\_type\_e
:   *Values:*

    <a id="_CPPv4N15rott_int_type_e19ROTATE_COMPLETE_INTE"></a>

    <a id="_CPPv3N15rott_int_type_e19ROTATE_COMPLETE_INTE"></a> <a id="_CPPv2N15rott_int_type_e19ROTATE_COMPLETE_INTE"></a> <a id="drv__rott_8h_1adad0cede3b9fc366ba61c22da5e75cdda2dc05bc066e634af4a1c4787432f94de"></a> enumerator ROTATE\_COMPLETE\_INT
    :   rotate finish int enable

    <a id="_CPPv4N15rott_int_type_e21ROTATE_WARTERMARK_INTE"></a>

    <a id="_CPPv3N15rott_int_type_e21ROTATE_WARTERMARK_INTE"></a> <a id="_CPPv2N15rott_int_type_e21ROTATE_WARTERMARK_INTE"></a> <a id="drv__rott_8h_1adad0cede3b9fc366ba61c22da5e75cdda0418381a5946702f8cabca3b306835ae"></a> enumerator ROTATE\_WARTERMARK\_INT
    :   rotate watermark int enable.

    <a id="_CPPv4N15rott_int_type_e18ROTATE_CFG_ERR_INTE"></a>

    <a id="_CPPv3N15rott_int_type_e18ROTATE_CFG_ERR_INTE"></a> <a id="_CPPv2N15rott_int_type_e18ROTATE_CFG_ERR_INTE"></a> <a id="drv__rott_8h_1adad0cede3b9fc366ba61c22da5e75cdda8c2e2aed4fb75d5d8664d5aa33b10d87"></a> enumerator ROTATE\_CFG\_ERR\_INT
    :   rotate config error int enable

<a id="_CPPv411rott_mode_e"></a>

<a id="_CPPv311rott_mode_e"></a> <a id="_CPPv211rott_mode_e"></a> <a id="drv__rott_8h_1a63918f093db5bb11cfcecfd964d0fa5a"></a> enum rott\_mode\_e
:   *Values:*

    <a id="_CPPv4N11rott_mode_e16ROTT_MODE_UNKNOWE"></a>

    <a id="_CPPv3N11rott_mode_e16ROTT_MODE_UNKNOWE"></a> <a id="_CPPv2N11rott_mode_e16ROTT_MODE_UNKNOWE"></a> <a id="drv__rott_8h_1a63918f093db5bb11cfcecfd964d0fa5aa6fc104391e9eb09b243089576bfe8f62"></a> enumerator ROTT\_MODE\_UNKNOW

    <a id="_CPPv4N11rott_mode_e20ROTT_ONLY_YUV2RGB565E"></a>

    <a id="_CPPv3N11rott_mode_e20ROTT_ONLY_YUV2RGB565E"></a> <a id="_CPPv2N11rott_mode_e20ROTT_ONLY_YUV2RGB565E"></a> <a id="drv__rott_8h_1a63918f093db5bb11cfcecfd964d0fa5aa5bbf49555e00bd85c6a490bc685fe78a"></a> enumerator ROTT\_ONLY\_YUV2RGB565
    :   bypass rotating, only use yuv2rgb565 pixel formart convert function

    <a id="_CPPv4N11rott_mode_e13ROTT_ROTATE90E"></a>

    <a id="_CPPv3N11rott_mode_e13ROTT_ROTATE90E"></a> <a id="_CPPv2N11rott_mode_e13ROTT_ROTATE90E"></a> <a id="drv__rott_8h_1a63918f093db5bb11cfcecfd964d0fa5aad3fe7664553d8c662ac0fd0751ae0601"></a> enumerator ROTT\_ROTATE90

    <a id="_CPPv4N11rott_mode_e14ROTT_ROTATE270E"></a>

    <a id="_CPPv3N11rott_mode_e14ROTT_ROTATE270E"></a> <a id="_CPPv2N11rott_mode_e14ROTT_ROTATE270E"></a> <a id="drv__rott_8h_1a63918f093db5bb11cfcecfd964d0fa5aa834c5c43daf2a5080dd876b1b6eea907"></a> enumerator ROTT\_ROTATE270

<a id="_CPPv422rott_input_data_flow_e"></a>

<a id="_CPPv322rott_input_data_flow_e"></a> <a id="_CPPv222rott_input_data_flow_e"></a> <a id="drv__rott_8h_1af803bb2be3237dfdf5b1715d480eb543"></a> enum rott\_input\_data\_flow\_e
:   *Values:*

    <a id="_CPPv4N22rott_input_data_flow_e17ROTT_INPUT_NORMALE"></a>

    <a id="_CPPv3N22rott_input_data_flow_e17ROTT_INPUT_NORMALE"></a> <a id="_CPPv2N22rott_input_data_flow_e17ROTT_INPUT_NORMALE"></a> <a id="drv__rott_8h_1af803bb2be3237dfdf5b1715d480eb543a2b690b87d281c6ee6adfd0c7de0bce97"></a> enumerator ROTT\_INPUT\_NORMAL
    :   input data not flip

    <a id="_CPPv4N22rott_input_data_flow_e30ROTT_INPUT_REVESE_BYTE_BY_BYTEE"></a>

    <a id="_CPPv3N22rott_input_data_flow_e30ROTT_INPUT_REVESE_BYTE_BY_BYTEE"></a> <a id="_CPPv2N22rott_input_data_flow_e30ROTT_INPUT_REVESE_BYTE_BY_BYTEE"></a> <a id="drv__rott_8h_1af803bb2be3237dfdf5b1715d480eb543a8e9b829515d4104802095191c325a820"></a> enumerator ROTT\_INPUT\_REVESE\_BYTE\_BY\_BYTE
    :   convert input data revese byte by byte.

    <a id="_CPPv4N22rott_input_data_flow_e38ROTT_INPUT_REVESE_HALFWORD_BY_HALFWORDE"></a>

    <a id="_CPPv3N22rott_input_data_flow_e38ROTT_INPUT_REVESE_HALFWORD_BY_HALFWORDE"></a> <a id="_CPPv2N22rott_input_data_flow_e38ROTT_INPUT_REVESE_HALFWORD_BY_HALFWORDE"></a> <a id="drv__rott_8h_1af803bb2be3237dfdf5b1715d480eb543a9a521e32a167e5ab7621722281ba9ffc"></a> enumerator ROTT\_INPUT\_REVESE\_HALFWORD\_BY\_HALFWORD
    :   convert input data revese halfword by halfword

<a id="_CPPv423rott_output_data_flow_e"></a>

<a id="_CPPv323rott_output_data_flow_e"></a> <a id="_CPPv223rott_output_data_flow_e"></a> <a id="drv__rott_8h_1aa245582a35ae281c70973456b0f928f0"></a> enum rott\_output\_data\_flow\_e
:   *Values:*

    <a id="_CPPv4N23rott_output_data_flow_e18ROTT_OUTPUT_NORMALE"></a>

    <a id="_CPPv3N23rott_output_data_flow_e18ROTT_OUTPUT_NORMALE"></a> <a id="_CPPv2N23rott_output_data_flow_e18ROTT_OUTPUT_NORMALE"></a> <a id="drv__rott_8h_1aa245582a35ae281c70973456b0f928f0a9ab0214ffdd65c6e60c4d9fc39fb7906"></a> enumerator ROTT\_OUTPUT\_NORMAL
    :   output data not flip

    <a id="_CPPv4N23rott_output_data_flow_e39ROTT_OUTPUT_REVESE_HALFWORD_BY_HALFWORDE"></a>

    <a id="_CPPv3N23rott_output_data_flow_e39ROTT_OUTPUT_REVESE_HALFWORD_BY_HALFWORDE"></a> <a id="_CPPv2N23rott_output_data_flow_e39ROTT_OUTPUT_REVESE_HALFWORD_BY_HALFWORDE"></a> <a id="drv__rott_8h_1aa245582a35ae281c70973456b0f928f0acc1f41aa018f809afdc918a325b6ff0c"></a> enumerator ROTT\_OUTPUT\_REVESE\_HALFWORD\_BY\_HALFWORD
    :   convert output data reverse halfword by halfword

<a id="_CPPv419rott_pixel_format_e"></a>

<a id="_CPPv319rott_pixel_format_e"></a> <a id="_CPPv219rott_pixel_format_e"></a> <a id="drv__rott_8h_1a17282f34721613bf258bd5a3baaa2bfd"></a> enum rott\_pixel\_format\_e
:   rgb lcd input data format, data save in mem is little endian, like VUYY format is \[bit31-bit0\] is \[V U Y Y\]

    *Values:*

    <a id="_CPPv4N19rott_pixel_format_e16PIXEL_FMT_UNKNOWE"></a>

    <a id="_CPPv3N19rott_pixel_format_e16PIXEL_FMT_UNKNOWE"></a> <a id="_CPPv2N19rott_pixel_format_e16PIXEL_FMT_UNKNOWE"></a> <a id="drv__rott_8h_1a17282f34721613bf258bd5a3baaa2bfda1c34bec144e3424d13cf2e7e5fa56207"></a> enumerator PIXEL\_FMT\_UNKNOW

    <a id="_CPPv4N19rott_pixel_format_e18PIXEL_FMT_DVP_JPEGE"></a>

    <a id="_CPPv3N19rott_pixel_format_e18PIXEL_FMT_DVP_JPEGE"></a> <a id="_CPPv2N19rott_pixel_format_e18PIXEL_FMT_DVP_JPEGE"></a> <a id="drv__rott_8h_1a17282f34721613bf258bd5a3baaa2bfda54eadc8fbc728888d97483d73fd02f57"></a> enumerator PIXEL\_FMT\_DVP\_JPEG

    <a id="_CPPv4N19rott_pixel_format_e18PIXEL_FMT_DVP_H264E"></a>

    <a id="_CPPv3N19rott_pixel_format_e18PIXEL_FMT_DVP_H264E"></a> <a id="_CPPv2N19rott_pixel_format_e18PIXEL_FMT_DVP_H264E"></a> <a id="drv__rott_8h_1a17282f34721613bf258bd5a3baaa2bfda1ba14b5dcca73524d46edb3739a8cf93"></a> enumerator PIXEL\_FMT\_DVP\_H264

    <a id="_CPPv4N19rott_pixel_format_e18PIXEL_FMT_UVC_JPEGE"></a>

    <a id="_CPPv3N19rott_pixel_format_e18PIXEL_FMT_UVC_JPEGE"></a> <a id="_CPPv2N19rott_pixel_format_e18PIXEL_FMT_UVC_JPEGE"></a> <a id="drv__rott_8h_1a17282f34721613bf258bd5a3baaa2bfdadb9189098f318f1cb2f31cfdf1e206cd"></a> enumerator PIXEL\_FMT\_UVC\_JPEG

    <a id="_CPPv4N19rott_pixel_format_e18PIXEL_FMT_UVC_H264E"></a>

    <a id="_CPPv3N19rott_pixel_format_e18PIXEL_FMT_UVC_H264E"></a> <a id="_CPPv2N19rott_pixel_format_e18PIXEL_FMT_UVC_H264E"></a> <a id="drv__rott_8h_1a17282f34721613bf258bd5a3baaa2bfda8a8daaf6d224e7ed3341787291e056b1"></a> enumerator PIXEL\_FMT\_UVC\_H264

    <a id="_CPPv4N19rott_pixel_format_e16PIXEL_FMT_RGB565E"></a>

    <a id="_CPPv3N19rott_pixel_format_e16PIXEL_FMT_RGB565E"></a> <a id="_CPPv2N19rott_pixel_format_e16PIXEL_FMT_RGB565E"></a> <a id="drv__rott_8h_1a17282f34721613bf258bd5a3baaa2bfdabddc53097f0b2541d7bca3bb25c49780"></a> enumerator PIXEL\_FMT\_RGB565
    :   input data format is rgb565(big endian), high pixel is bit\[31-16\], low pixel is bit\[15-0\] (PIXEL BIG ENDIAN)

    <a id="_CPPv4N19rott_pixel_format_e19PIXEL_FMT_RGB565_LEE"></a>

    <a id="_CPPv3N19rott_pixel_format_e19PIXEL_FMT_RGB565_LEE"></a> <a id="_CPPv2N19rott_pixel_format_e19PIXEL_FMT_RGB565_LEE"></a> <a id="drv__rott_8h_1a17282f34721613bf258bd5a3baaa2bfda5aa19e0043f24403c8d6bc4738a52f45"></a> enumerator PIXEL\_FMT\_RGB565\_LE
    :   input data format is rgb565(big endian), high pixel is bit\[15-0\], low pixel is bit\[31-16\] (PIXEL little ENDIAN)

    <a id="_CPPv4N19rott_pixel_format_e14PIXEL_FMT_YUYVE"></a>

    <a id="_CPPv3N19rott_pixel_format_e14PIXEL_FMT_YUYVE"></a> <a id="_CPPv2N19rott_pixel_format_e14PIXEL_FMT_YUYVE"></a> <a id="drv__rott_8h_1a17282f34721613bf258bd5a3baaa2bfda1d73f52d66545b585115ff73e9576c1b"></a> enumerator PIXEL\_FMT\_YUYV
    :   input data is yuyv format, diaplay module internal may convert to rgb565 data

    <a id="_CPPv4N19rott_pixel_format_e14PIXEL_FMT_UYVYE"></a>

    <a id="_CPPv3N19rott_pixel_format_e14PIXEL_FMT_UYVYE"></a> <a id="_CPPv2N19rott_pixel_format_e14PIXEL_FMT_UYVYE"></a> <a id="drv__rott_8h_1a17282f34721613bf258bd5a3baaa2bfda9bdd82804fcd0f1cbd242bf0c4477a6d"></a> enumerator PIXEL\_FMT\_UYVY

    <a id="_CPPv4N19rott_pixel_format_e14PIXEL_FMT_YYUVE"></a>

    <a id="_CPPv3N19rott_pixel_format_e14PIXEL_FMT_YYUVE"></a> <a id="_CPPv2N19rott_pixel_format_e14PIXEL_FMT_YYUVE"></a> <a id="drv__rott_8h_1a17282f34721613bf258bd5a3baaa2bfda7de255a8fded3122553b2b1d7ef6e147"></a> enumerator PIXEL\_FMT\_YYUV
    :   input data is yyuv format

    <a id="_CPPv4N19rott_pixel_format_e14PIXEL_FMT_UVYYE"></a>

    <a id="_CPPv3N19rott_pixel_format_e14PIXEL_FMT_UVYYE"></a> <a id="_CPPv2N19rott_pixel_format_e14PIXEL_FMT_UVYYE"></a> <a id="drv__rott_8h_1a17282f34721613bf258bd5a3baaa2bfdafffe94e23848297cf242128a0b142364"></a> enumerator PIXEL\_FMT\_UVYY
    :   input data is uvyy format

    <a id="_CPPv4N19rott_pixel_format_e14PIXEL_FMT_VUYYE"></a>

    <a id="_CPPv3N19rott_pixel_format_e14PIXEL_FMT_VUYYE"></a> <a id="_CPPv2N19rott_pixel_format_e14PIXEL_FMT_VUYYE"></a> <a id="drv__rott_8h_1a17282f34721613bf258bd5a3baaa2bfda0e5ac6d6002e58b1d65201778987b262"></a> enumerator PIXEL\_FMT\_VUYY
    :   input data is vuyy format
