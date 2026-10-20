---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/api-reference/multi_media/bk_jpegenc.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="jpegenc-apis"></a>

# JPEGENC APIs

重要

The JPEGENC API v1.0 is the lastest stable JPEGENC APIs. All new applications should use JPEGENC API v1.0.

<a id="jpegenc-interface"></a>

## JPEGENC Interface

The JPEGENC module can work two different mode
:   - 0: JPEG ENCODER mode, output jpeg data
    - 1: YUV mode, output camera sample data, yuv data

<a id="jpegenc-api-categories"></a>

## JPEGENC API Categories

Most of JPEGENC APIs can be categoried as:

> - JPEGENC APIs
>
>   The common APIs are prefixed with bk\_jpeg\_enc, e.g. bk\_jpeg\_enc\_driver\_init() etc.

JPEGENC APIs:
:   - [`bk_jpeg_enc_driver_init()`](#_CPPv423bk_jpeg_enc_driver_initv "bk_jpeg_enc_driver_init") \- init jpeg encode module driver
    - [`bk_jpeg_enc_driver_deinit()`](#_CPPv425bk_jpeg_enc_driver_deinitv "bk_jpeg_enc_driver_deinit") \- deinit jpeg encode module driver
    - [`bk_jpeg_enc_init()`](#_CPPv416bk_jpeg_enc_initPK13jpeg_config_t "bk_jpeg_enc_init") \- init jpeg encode module
    - [`bk_jpeg_enc_deinit()`](#_CPPv418bk_jpeg_enc_deinitv "bk_jpeg_enc_deinit") \- deinit jpeg encode module
    - `bk_jpeg_enc_dvp_init()` \- init jpeg encode module
    - `bk_jpeg_enc_dvp_deinit()` \- deinit jpeg encode module
    - `bk_jpeg_enc_set_yuv_mode()` \- set jpeg encode module work mode
    - [`bk_jpeg_enc_set_enable()`](#_CPPv422bk_jpeg_enc_set_enable7uint8_t7uint8_t "bk_jpeg_enc_set_enable") \- set encode enable/disable
    - [`bk_jpeg_enc_get_frame_size()`](#_CPPv426bk_jpeg_enc_get_frame_sizev "bk_jpeg_enc_get_frame_size") \- get a frame size output from jpeg encode module
    - `bk_jpeg_enc_register_frame_start_isr()` \- register sof callback function
    - `bk_jpeg_enc_register_frame_end_isr()` \- register eof callback function
    - `bk_jpeg_enc_register_end_yuv_isr()` \- register yof callback function
    - `bk_jpeg_enc_dvp_gpio_enable()` \- enable jpeg encode module data gpio

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [jpeg\_enc.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/jpeg_enc.h)

<a id="functions"></a>

### Functions

<a id="_CPPv423bk_jpeg_enc_driver_initv"></a>

<a id="_CPPv323bk_jpeg_enc_driver_initv"></a> <a id="_CPPv223bk_jpeg_enc_driver_initv"></a> <a id="bk_jpeg_enc_driver_init__void"></a> <a id="jpeg__enc_8h_1aa627d0d3312f723f3a348dd53f05a63a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_enc\_driver\_init(void)
:   Init the jpeg encode driver.

    This API init the resoure common:

    - Init jpegenc driver control memory
    - register jpegenc isr

    **Attention**
    :   1\. This API should be called before any other jpeg APIs.

        2\. This API will power up video when soc is bk7256XX

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv425bk_jpeg_enc_driver_deinitv"></a>

<a id="_CPPv325bk_jpeg_enc_driver_deinitv"></a> <a id="_CPPv225bk_jpeg_enc_driver_deinitv"></a> <a id="bk_jpeg_enc_driver_deinit__void"></a> <a id="jpeg__enc_8h_1a8a6e76226601221ff4b3f6f02e272929"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_enc\_driver\_deinit(void)
:   Deinit the jpegenc driver.

    This API free all resource related to jpegenc and disable jpegenc.

    **Attention**
    :   1\. This API will power down video when soc is bk7256XX

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv416bk_jpeg_enc_initPK13jpeg_config_t"></a>

<a id="_CPPv316bk_jpeg_enc_initPK13jpeg_config_t"></a> <a id="_CPPv216bk_jpeg_enc_initPK13jpeg_config_t"></a> <a id="bk_jpeg_enc_init__jpeg_config_tCP"></a> <a id="jpeg__enc_8h_1a20ba8dee0b17571ec977683d0911185e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_enc\_init(const jpeg\_config\_t \*config)
:   Init the jpeg encode.

    This API init the jpegenc

    - Configure clock and Power up the jpegenc
    - Enable Jpegenc interrupt
    - Map the jpegenc to dedicated GPIO port(MCLK and PCLK)
    - Set the jpegenc parameters
    - Enable jpeg encode module

    Usage example:

    ```
     jpeg_config_t init_config = {
                         .rx_buf = xxx, // the address point to mem for receiving jpeg data
                         .yuv_mode = 0,
                         .sys_clk_div = 3, // jpeg_clk = 480 / (1+3) =120MHz
                         .mclk_div = 0, // MCLK=jpeg_clk/4 = 30MHz
                         .rx_buf_len = xxx, // the length of receive jpeg data
                         .node_len = xxx, // dma transfer length
                         .x_pixel = 80, // jpeg image resolution of width: 80 * 8 = 640
                         .y_pixel = 60, // jpeg image resolution of height: 60 * 8 = 480
                         .dma_rx_finish_handler = cb, // dma transfer finish callback
                     };
     BK_LOG_ON_ERR(bk_jpeg_init(&init_config);
    ```

    **Attention**
    :   1\. only work for imaging transfer

    参数
    :   **config** – jpeg encode parameter settings

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: jpegenc config paramter is NULL
        - BK\_ERR\_JPEG\_NOT\_INIT: jpegenc driver not init
        - others: other errors.

<a id="_CPPv418bk_jpeg_enc_deinitv"></a>

<a id="_CPPv318bk_jpeg_enc_deinitv"></a> <a id="_CPPv218bk_jpeg_enc_deinitv"></a> <a id="bk_jpeg_enc_deinit__void"></a> <a id="jpeg__enc_8h_1ab6a0d8537992e1373514cc3363b6c249"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_enc\_deinit(void)
:   Deinit the jpeg.

    This API stop jpeg encode, close jpeg gpio, power off jpeg module at last.

    **Attention**
    :   1\. only work for imaging transfer

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv422bk_jpeg_enc_set_enable7uint8_t7uint8_t"></a>

<a id="_CPPv322bk_jpeg_enc_set_enable7uint8_t7uint8_t"></a> <a id="_CPPv222bk_jpeg_enc_set_enable7uint8_t7uint8_t"></a> <a id="bk_jpeg_enc_set_enable__uint8_t.uint8_t"></a> <a id="jpeg__enc_8h_1ad2405dfa52d98fef670ec70e473a313f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_enc\_set\_enable(uint8\_t enable, uint8\_t mode)
:   set jpegenc enable

    This API will set jpegenc work enable/disable.

    **Attention**
    :   1\. if work in jpegenc mode, this api can enable/disable jpegenc mode

        2\. if work in yuv mode, this api only can disable yuv\_mode. The bk\_jpeg\_set\_yuv\_mode api also can set yuv mode enable/disable.

    参数
    :   - **enable** – 0/1:jpegenc work disable/enable
        - **mode** – 0/1:jpeg encode mode/yuv mode

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv423bk_jpeg_enc_yuv_fmt_sel8uint32_t"></a>

<a id="_CPPv323bk_jpeg_enc_yuv_fmt_sel8uint32_t"></a> <a id="_CPPv223bk_jpeg_enc_yuv_fmt_sel8uint32_t"></a> <a id="bk_jpeg_enc_yuv_fmt_sel__uint32_t"></a> <a id="jpeg__enc_8h_1a0dc0ff91f4ad6426235e7ddf0cc47de7"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_enc\_yuv\_fmt\_sel(uint32\_t value)
:   yuv format select

    This API will set yuv output format.

    **Attention**
    :   1\. this function only used when jpeg at yuv mode

    参数
    :   **value** – 0:yuyv, 1:uyvy, 2:yyuv, 3:uvyy

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv426bk_jpeg_enc_get_frame_sizev"></a>

<a id="_CPPv326bk_jpeg_enc_get_frame_sizev"></a> <a id="_CPPv226bk_jpeg_enc_get_frame_sizev"></a> <a id="bk_jpeg_enc_get_frame_size__void"></a> <a id="jpeg__enc_8h_1ac47ca42ba05cf3a44ecb2cf9e3d6c29d"></a> uint32\_t bk\_jpeg\_enc\_get\_frame\_size(void)
:   get a frame size output from jpegenc module, uint byte

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_jpeg_enc_register_isr15jpeg_isr_type_t10jpeg_isr_tPv"></a>

<a id="_CPPv324bk_jpeg_enc_register_isr15jpeg_isr_type_t10jpeg_isr_tPv"></a> <a id="_CPPv224bk_jpeg_enc_register_isr15jpeg_isr_type_t10jpeg_isr_tPv"></a> <a id="bk_jpeg_enc_register_isr__jpeg_isr_type_t.jpeg_isr_t.voidP"></a> <a id="jpeg__enc_8h_1af39149f90bba9122e2ca890ab0c71891"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_enc\_register\_isr(jpeg\_isr\_type\_t type\_id, [jpeg\_isr\_t](#_CPPv410jpeg_isr_t "jpeg_isr_t") isr, void \*param)
:   register frame end isr

    This API will register jpeg encode isr function, need user defined.The isr function will execute when the isr be triggered.

    .\*

    **Attention**
    :   1\. This API only effect when work yuv mode

    参数
    :   - **type\_id** – the type of the isr

          - JPEG\_EOY: (eoy)when jpeg encode work in yuv mode, once a complete frame have been transfer by jpeg encode module, the isr will trigger.
          - JPEG\_HEAD\_OUTPUT: jpeg encode output head the isrt will be triggered, work in jpeg encode mode.
          - START\_OFFRAME: (sof) when jpeg encode module start reveice a frame the isr will be triggered.
          - JPEG\_EOF: (eof) when jpeg encode module receive a complete frame the isr will be triggered, this only effect in jpeg encode mode.
          - JPEG\_VSYNC\_NEGEDGE: (vng) when jpeg encode module receive a vsync negedge the isr will be triggered.
        - **isr** – isr\_func
        - **param** – other value(default set NULL)

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv427bk_jpeg_enc_set_gpio_enable7uint8_t16jpeg_gpio_mode_t"></a>

<a id="_CPPv327bk_jpeg_enc_set_gpio_enable7uint8_t16jpeg_gpio_mode_t"></a> <a id="_CPPv227bk_jpeg_enc_set_gpio_enable7uint8_t16jpeg_gpio_mode_t"></a> <a id="bk_jpeg_enc_set_gpio_enable__uint8_t.jpeg_gpio_mode_t"></a> <a id="jpeg__enc_8h_1afef89ba28e608571ce79d5922f2d4c50"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_enc\_set\_gpio\_enable(uint8\_t enable, [jpeg\_gpio\_mode\_t](#_CPPv416jpeg_gpio_mode_t "jpeg_gpio_mode_t") mode)
:   set jpeg gpio function

    This API will operate jpeg gpio

    参数
    :   - **enable** – 0/1:unmap/map
        - **mode, :** – reference jpeg\_gpio\_mode\_t

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv425bk_jpeg_enc_get_fifo_addrP8uint32_t"></a>

<a id="_CPPv325bk_jpeg_enc_get_fifo_addrP8uint32_t"></a> <a id="_CPPv225bk_jpeg_enc_get_fifo_addrP8uint32_t"></a> <a id="bk_jpeg_enc_get_fifo_addr__uint32_tP"></a> <a id="jpeg__enc_8h_1accbcc8d4eb52e62607fef7369887e9c4"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_enc\_get\_fifo\_addr(uint32\_t \*fifo\_addr)
:   get jpeg enc fifo addr

    This API will get jpeg encode fifo addr in param

    **Attention**
    :   1\. only work in jpeg encode mode is effective

    参数
    :   **fifo\_addr** – fifo addr

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_jpeg_enc_set_auxs8uint32_t8uint32_t"></a>

<a id="_CPPv320bk_jpeg_enc_set_auxs8uint32_t8uint32_t"></a> <a id="_CPPv220bk_jpeg_enc_set_auxs8uint32_t8uint32_t"></a> <a id="bk_jpeg_enc_set_auxs__uint32_t.uint32_t"></a> <a id="jpeg__enc_8h_1ae273638b25edd14a671fd92d744c814f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_enc\_set\_auxs(uint32\_t cksel, uint32\_t ckdiv)
:   set mclk output

    This API will use for camera config

    1\. this api only used for bk7256xx\_mp chip, and when use this api, this api ‘bk\_jpeg\_enc\_mclk\_enable’ will not useful

    参数
    :   - **cksel** – 0-3:0:DCO/1:APLL/2:320M/3:480M,use 2 or 3
        - **ckdiv** – 0-15, div \= 1/(ckdiv\+1)

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv423bk_jpeg_enc_mclk_enablev"></a>

<a id="_CPPv323bk_jpeg_enc_mclk_enablev"></a> <a id="_CPPv223bk_jpeg_enc_mclk_enablev"></a> <a id="bk_jpeg_enc_mclk_enable__void"></a> <a id="jpeg__enc_8h_1adbd1adbdbff9ace476d9fbea8438b2ff"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_enc\_mclk\_enable(void)
:   set jpeg module mclk enable

    This API will set jpeg mclk output for sensor

    1\. this api must call after bk\_jpeg\_enc\_driver\_init, and output 24MHz.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv432bk_jpeg_enc_partial_display_initPK28jpeg_partial_offset_config_t"></a>

<a id="_CPPv332bk_jpeg_enc_partial_display_initPK28jpeg_partial_offset_config_t"></a> <a id="_CPPv232bk_jpeg_enc_partial_display_initPK28jpeg_partial_offset_config_t"></a> <a id="bk_jpeg_enc_partial_display_init__jpeg_partial_offset_config_tCP"></a> <a id="jpeg__enc_8h_1a3dc1fdd103c565e86468eb070809339b"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_enc\_partial\_display\_init(const jpeg\_partial\_offset\_config\_t \*offset\_config)
:   partial display init

    This API will use for partial display configure of jpeg encode

    参数
    :   **offset\_config** – x\_pixel left/right offset and y\_pixel left/right offset configure

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv434bk_jpeg_enc_partial_display_deinitv"></a>

<a id="_CPPv334bk_jpeg_enc_partial_display_deinitv"></a> <a id="_CPPv234bk_jpeg_enc_partial_display_deinitv"></a> <a id="bk_jpeg_enc_partial_display_deinit__void"></a> <a id="jpeg__enc_8h_1a89041c6211b312d6fb412476e0e8aa99"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_enc\_partial\_display\_deinit(void)
:   partial display deinit

    This API will use for partial display deinit

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_jpeg_set_em_base_addrP7uint8_t"></a>

<a id="_CPPv324bk_jpeg_set_em_base_addrP7uint8_t"></a> <a id="_CPPv224bk_jpeg_set_em_base_addrP7uint8_t"></a> <a id="bk_jpeg_set_em_base_addr__uint8_tP"></a> <a id="jpeg__enc_8h_1a5bd17d8d578305434d40bf2b5522d1d8"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_set\_em\_base\_addr(uint8\_t \*address)
:   jpeg em base set

    This API will use for jpeg em base address, 64KB memory align.

    参数
    :   **address** – set a mem used for jpeg encode

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv425bk_jpeg_enc_encode_config7uint8_t8uint16_t8uint16_t"></a>

<a id="_CPPv325bk_jpeg_enc_encode_config7uint8_t8uint16_t8uint16_t"></a> <a id="_CPPv225bk_jpeg_enc_encode_config7uint8_t8uint16_t8uint16_t"></a> <a id="bk_jpeg_enc_encode_config__uint8_t.uint16_t.uint16_t"></a> <a id="jpeg__enc_8h_1a42de4234dab8505c6cd5b85b4d14df39"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_enc\_encode\_config(uint8\_t enable, uint16\_t up\_size, uint16\_t low\_size)
:   jpeg encode enable encode auto contrl

    This API will use for enable/disable for auto encode size. only valid in jpeh encode mode

    1\. this api only called in jpeg\_eof\_isr function, and only bk\_jpeg\_enc\_enable\_encode\_auto\_ctrl have been set enable

    参数
    :   - **up\_size** – the jpeg image upper limit, unit byte
        - **low\_size** – the jpeg image lower limit, unit byte

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv423bk_jpeg_enc_mode_switchP13jpeg_config_t"></a>

<a id="_CPPv323bk_jpeg_enc_mode_switchP13jpeg_config_t"></a> <a id="_CPPv223bk_jpeg_enc_mode_switchP13jpeg_config_t"></a> <a id="bk_jpeg_enc_mode_switch__jpeg_config_tP"></a> <a id="jpeg__enc_8h_1a4b839f6fd75aebdac1358cea7eadcac6"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_jpeg\_enc\_mode\_switch(jpeg\_config\_t \*config)
:   jpeg encode mode and yuv mode switch

    This API will use for switch jpeg mode

    1\. this api must called in jpeg\_eof isr or yuv\_eof isr

    参数
    :   **config** – jpeg encode config or jpeg yuv config

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="api-typedefs"></a>

## API Typedefs

<a id="id1"></a>

### Header File

- [jpeg\_enc\_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/jpeg_enc_types.h)

<a id="macros"></a>

### Macros

<a id="c.Y_PIXEL_272"></a>

<a id="jpeg__enc__types_8h_1a522404482babcb4eaf5194f358da79ff"></a> Y\_PIXEL\_272
:   JPEGENC APIs Version 1.0.

    image resolution for hight: Y \* 8 \= 272

<a id="c.Y_PIXEL_320"></a>

<a id="jpeg__enc__types_8h_1ab0d71e31f0a16373ed2a009f2ffba484"></a> Y\_PIXEL\_320
:   image resolution for hight: Y \* 8 \= 320

<a id="c.X_PIXEL_480"></a>

<a id="jpeg__enc__types_8h_1a6d819fd957585002ae577656335ceb4d"></a> X\_PIXEL\_480
:   image resolution for width: X \* 8 \= 480

<a id="c.Y_PIXEL_480"></a>

<a id="jpeg__enc__types_8h_1ab3f397fb7ef0d4146c3eb8969be9fe97"></a> Y\_PIXEL\_480
:   image resolution for hight: Y \* 8 \= 480

<a id="c.X_PIXEL_640"></a>

<a id="jpeg__enc__types_8h_1a4f02881b00a2a0e8c216cb1eaec25f28"></a> X\_PIXEL\_640
:   image resolution for hight: X \* 8 \= 640

<a id="c.Y_PIXEL_240"></a>

<a id="jpeg__enc__types_8h_1ab4d9548ba28b2774a13e9c469f1f0f73"></a> Y\_PIXEL\_240
:   image resolution for hight: Y \* 8 \= 240

<a id="c.X_PIXEL_320"></a>

<a id="jpeg__enc__types_8h_1a949fd6364e8ce0227ce8f42217aefb03"></a> X\_PIXEL\_320
:   image resolution for hight: X \* 8 \= 320

<a id="c.Y_PIXEL_600"></a>

<a id="jpeg__enc__types_8h_1a3821b9a80a3f1fac681b46f53fc3398e"></a> Y\_PIXEL\_600
:   image resolution for hight: Y \* 8 \= 600

<a id="c.X_PIXEL_800"></a>

<a id="jpeg__enc__types_8h_1a9d01a40e7e75283f258fda84bda80130"></a> X\_PIXEL\_800
:   image resolution for hight: X \* 8 \= 800

<a id="c.Y_PIXEL_720"></a>

<a id="jpeg__enc__types_8h_1aea7342a2701602b4c2b8cb72a830dccc"></a> Y\_PIXEL\_720
:   image resolution for hight: Y \* 8 \= 720

<a id="c.X_PIXEL_1280"></a>

<a id="jpeg__enc__types_8h_1ad26437aad7c4d19fab25865b65e8a635"></a> X\_PIXEL\_1280
:   image resolution for hight: X \* 8 \= 1280

<a id="c.X_PIXEL_1600"></a>

<a id="jpeg__enc__types_8h_1a1bdb08449f697917a8b4877a1aaee026"></a> X\_PIXEL\_1600
:   image resolution for hight: X \* 8 \= 1600

<a id="c.Y_PIXEL_1200"></a>

<a id="jpeg__enc__types_8h_1a12ea013e007311ec2fff1afebd3d79a4"></a> Y\_PIXEL\_1200
:   image resolution for hight: Y \* 8 \= 1200

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv410jpeg_isr_t"></a>

<a id="_CPPv310jpeg_isr_t"></a> <a id="_CPPv210jpeg_isr_t"></a> <a id="jpeg_isr_t"></a> <a id="jpeg__enc__types_8h_1a763d0f2ab1836e988d6e2cafa1a73245"></a> typedef void (\*jpeg\_isr\_t)(jpeg\_unit\_t id, void \*param)
:   jpeg isr callback relay jpeg driver

    Param id, :
    :   only 0 useful, set 0 default

    Param param, :
    :   NULL default

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv416jpeg_gpio_mode_t"></a>

<a id="_CPPv316jpeg_gpio_mode_t"></a> <a id="_CPPv216jpeg_gpio_mode_t"></a> <a id="jpeg__enc__types_8h_1acccffedb45dfc8c6865ff1809616eda7"></a> enum jpeg\_gpio\_mode\_t
:   *Values:*

    <a id="_CPPv4N16jpeg_gpio_mode_t13JPEG_GPIO_CLKE"></a>

    <a id="_CPPv3N16jpeg_gpio_mode_t13JPEG_GPIO_CLKE"></a> <a id="_CPPv2N16jpeg_gpio_mode_t13JPEG_GPIO_CLKE"></a> <a id="jpeg__enc__types_8h_1acccffedb45dfc8c6865ff1809616eda7a287f962f72b7cfb60f9f7faf48609cfe"></a> enumerator JPEG\_GPIO\_CLK
    :   enable jpeg mclk and pclk gpio function

    <a id="_CPPv4N16jpeg_gpio_mode_t14JPEG_GPIO_DATAE"></a>

    <a id="_CPPv3N16jpeg_gpio_mode_t14JPEG_GPIO_DATAE"></a> <a id="_CPPv2N16jpeg_gpio_mode_t14JPEG_GPIO_DATAE"></a> <a id="jpeg__enc__types_8h_1acccffedb45dfc8c6865ff1809616eda7aa80837e9d5498c3c1266b8845beb9d37"></a> enumerator JPEG\_GPIO\_DATA
    :   enable jpeg vsync/hsync/D0-D7 gpio function

    <a id="_CPPv4N16jpeg_gpio_mode_t20JPEG_GPIO_HSYNC_DATAE"></a>

    <a id="_CPPv3N16jpeg_gpio_mode_t20JPEG_GPIO_HSYNC_DATAE"></a> <a id="_CPPv2N16jpeg_gpio_mode_t20JPEG_GPIO_HSYNC_DATAE"></a> <a id="jpeg__enc__types_8h_1acccffedb45dfc8c6865ff1809616eda7a1625754f73f49cce06d325a34639cf97"></a> enumerator JPEG\_GPIO\_HSYNC\_DATA
    :   enable jpeg hsync/D0-D7 gpio function

    <a id="_CPPv4N16jpeg_gpio_mode_t13JPEG_GPIO_ALLE"></a>

    <a id="_CPPv3N16jpeg_gpio_mode_t13JPEG_GPIO_ALLE"></a> <a id="_CPPv2N16jpeg_gpio_mode_t13JPEG_GPIO_ALLE"></a> <a id="jpeg__enc__types_8h_1acccffedb45dfc8c6865ff1809616eda7a63d2172138736418157814334e0ddf43"></a> enumerator JPEG\_GPIO\_ALL
    :   enable all jpeg gpio function
