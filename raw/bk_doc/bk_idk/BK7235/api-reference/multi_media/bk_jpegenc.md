# JPEGENC APIs[](#jpegenc-apis "永久链接至标题")

[[English]](../../../../en/v1.5/api-reference/multi_media/bk_jpegenc.html "../../../../en/v1.5/api-reference/multi_media/bk_jpegenc.html")

重要

The JPEGENC API v1.0 is the lastest stable JPEGENC APIs. All new applications should use JPEGENC API v1.0.


## JPEGENC Interface[](#jpegenc-interface "永久链接至标题")

The JPEGENC module can work two different mode
:   - 0: JPEG ENCODER mode, output jpeg data

    - 1: YUV mode, output camera sample data, yuv data


## JPEGENC API Categories[](#jpegenc-api-categories "永久链接至标题")

Most of JPEGENC APIs can be categoried as:

> - JPEGENC APIs
>
>   The common APIs are prefixed with bk_jpeg_enc, e.g. bk_jpeg_enc_driver_init() etc.

JPEGENC APIs:
:   - [`bk_jpeg_enc_driver_init()`](#_CPPv423bk_jpeg_enc_driver_initv "bk_jpeg_enc_driver_init") - init jpeg encode module driver

    - [`bk_jpeg_enc_driver_deinit()`](#_CPPv425bk_jpeg_enc_driver_deinitv "bk_jpeg_enc_driver_deinit") - deinit jpeg encode module driver

    - [`bk_jpeg_enc_init()`](#_CPPv416bk_jpeg_enc_initPK13jpeg_config_t "bk_jpeg_enc_init") - init jpeg encode module

    - [`bk_jpeg_enc_deinit()`](#_CPPv418bk_jpeg_enc_deinitv "bk_jpeg_enc_deinit") - deinit jpeg encode module

    - `bk_jpeg_enc_dvp_init()` - init jpeg encode module

    - `bk_jpeg_enc_dvp_deinit()` - deinit jpeg encode module

    - `bk_jpeg_enc_set_yuv_mode()` - set jpeg encode module work mode

    - [`bk_jpeg_enc_set_enable()`](#_CPPv422bk_jpeg_enc_set_enable7uint8_t7uint8_t "bk_jpeg_enc_set_enable") - set encode enable/disable

    - [`bk_jpeg_enc_get_frame_size()`](#_CPPv426bk_jpeg_enc_get_frame_sizev "bk_jpeg_enc_get_frame_size") - get a frame size output from jpeg encode module

    - `bk_jpeg_enc_register_frame_start_isr()` - register sof callback function

    - `bk_jpeg_enc_register_frame_end_isr()` - register eof callback function

    - `bk_jpeg_enc_register_end_yuv_isr()` - register yof callback function

    - `bk_jpeg_enc_dvp_gpio_enable()` - enable jpeg encode module data gpio


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [jpeg_enc.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/jpeg_enc.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/jpeg_enc.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_jpeg_enc_driver_init(void)[](#_CPPv423bk_jpeg_enc_driver_initv "永久链接至目标")
:   Init the jpeg encode driver.

    This API init the resoure common:


    - Init jpegenc driver control memory

    - register jpegenc isr


    **Attention**
    :   1. This API should be called before any other jpeg APIs.

        2. This API will power up video when soc is bk7256XX

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_jpeg_enc_driver_deinit(void)[](#_CPPv425bk_jpeg_enc_driver_deinitv "永久链接至目标")
:   Deinit the jpegenc driver.

    This API free all resource related to jpegenc and disable jpegenc.


    **Attention**
    :   1. This API will power down video when soc is bk7256XX

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_jpeg_enc_init(const jpeg_config_t *config)[](#_CPPv416bk_jpeg_enc_initPK13jpeg_config_t "永久链接至目标")
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
    :   1. only work for imaging transfer

    参数
    :   **config** – jpeg encode parameter settings

    返回
    :   - BK_OK: succeed

        - BK_ERR_NULL_PARAM: jpegenc config paramter is NULL

        - BK_ERR_JPEG_NOT_INIT: jpegenc driver not init

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_jpeg_enc_deinit(void)[](#_CPPv418bk_jpeg_enc_deinitv "永久链接至目标")
:   Deinit the jpeg.

    This API stop jpeg encode, close jpeg gpio, power off jpeg module at last.


    **Attention**
    :   1. only work for imaging transfer

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_jpeg_enc_set_enable(uint8_t enable, uint8_t mode)[](#_CPPv422bk_jpeg_enc_set_enable7uint8_t7uint8_t "永久链接至目标")
:   set jpegenc enable

    This API will set jpegenc work enable/disable.


    **Attention**
    :   1. if work in jpegenc mode, this api can enable/disable jpegenc mode

        2. if work in yuv mode, this api only can disable yuv_mode. The bk_jpeg_set_yuv_mode api also can set yuv mode enable/disable.

    参数
    :   - **enable** – 0/1:jpegenc work disable/enable

        - **mode** – 0/1:jpeg encode mode/yuv mode

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_jpeg_enc_yuv_fmt_sel(uint32_t value)[](#_CPPv423bk_jpeg_enc_yuv_fmt_sel8uint32_t "永久链接至目标")
:   yuv format select

    This API will set yuv output format.


    **Attention**
    :   1. this function only used when jpeg at yuv mode

    参数
    :   **value** – 0:yuyv, 1:uyvy, 2:yyuv, 3:uvyy

    返回
    :   - BK_OK: succeed

        - others: other errors.

uint32_t bk_jpeg_enc_get_frame_size(void)[](#_CPPv426bk_jpeg_enc_get_frame_sizev "永久链接至目标")
:   get a frame size output from jpegenc module, uint byte

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_jpeg_enc_register_isr(jpeg_isr_type_t type_id, [jpeg_isr_t](#_CPPv410jpeg_isr_t "jpeg_isr_t") isr, void *param)[](#_CPPv424bk_jpeg_enc_register_isr15jpeg_isr_type_t10jpeg_isr_tPv "永久链接至目标")
:   register frame end isr

    This API will register jpeg encode isr function, need user defined.The isr function will execute when the isr be triggered.

    .*


    **Attention**
    :   1. This API only effect when work yuv mode

    参数
    :   - **type_id** – the type of the isr

          - JPEG_EOY: (eoy)when jpeg encode work in yuv mode, once a complete frame have been transfer by jpeg encode module, the isr will trigger.

          - JPEG_HEAD_OUTPUT: jpeg encode output head the isrt will be triggered, work in jpeg encode mode.

          - START_OFFRAME: (sof) when jpeg encode module start reveice a frame the isr will be triggered.

          - JPEG_EOF: (eof) when jpeg encode module receive a complete frame the isr will be triggered, this only effect in jpeg encode mode.

          - JPEG_VSYNC_NEGEDGE: (vng) when jpeg encode module receive a vsync negedge the isr will be triggered.

        - **isr** – isr_func

        - **param** – other value(default set NULL)

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_jpeg_enc_set_gpio_enable(uint8_t enable, [jpeg_gpio_mode_t](#_CPPv416jpeg_gpio_mode_t "jpeg_gpio_mode_t") mode)[](#_CPPv427bk_jpeg_enc_set_gpio_enable7uint8_t16jpeg_gpio_mode_t "永久链接至目标")
:   set jpeg gpio function

    This API will operate jpeg gpio

    参数
    :   - **enable** – 0/1:unmap/map

        - **mode, :** – reference jpeg_gpio_mode_t

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_jpeg_enc_get_fifo_addr(uint32_t *fifo_addr)[](#_CPPv425bk_jpeg_enc_get_fifo_addrP8uint32_t "永久链接至目标")
:   get jpeg enc fifo addr

    This API will get jpeg encode fifo addr in param


    **Attention**
    :   1. only work in jpeg encode mode is effective

    参数
    :   **fifo_addr** – fifo addr

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_jpeg_enc_set_auxs(uint32_t cksel, uint32_t ckdiv)[](#_CPPv420bk_jpeg_enc_set_auxs8uint32_t8uint32_t "永久链接至目标")
:   set mclk output

    This API will use for camera config

    1. this api only used for bk7256xx_mp chip, and when use this api, this api ‘bk_jpeg_enc_mclk_enable’ will not useful

    参数
    :   - **cksel** – 0-3:0:DCO/1:APLL/2:320M/3:480M,use 2 or 3

        - **ckdiv** – 0-15, div = 1/(ckdiv+1)

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_jpeg_enc_mclk_enable(void)[](#_CPPv423bk_jpeg_enc_mclk_enablev "永久链接至目标")
:   set jpeg module mclk enable

    This API will set jpeg mclk output for sensor

    1. this api must call after bk_jpeg_enc_driver_init, and output 24MHz.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_jpeg_enc_partial_display_init(const jpeg_partial_offset_config_t *offset_config)[](#_CPPv432bk_jpeg_enc_partial_display_initPK28jpeg_partial_offset_config_t "永久链接至目标")
:   partial display init

    This API will use for partial display configure of jpeg encode

    参数
    :   **offset_config** – x_pixel left/right offset and y_pixel left/right offset configure

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_jpeg_enc_partial_display_deinit(void)[](#_CPPv434bk_jpeg_enc_partial_display_deinitv "永久链接至目标")
:   partial display deinit

    This API will use for partial display deinit

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_jpeg_set_em_base_addr(uint8_t *address)[](#_CPPv424bk_jpeg_set_em_base_addrP7uint8_t "永久链接至目标")
:   jpeg em base set

    This API will use for jpeg em base address, 64KB memory align.

    参数
    :   **address** – set a mem used for jpeg encode

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_jpeg_enc_encode_config(uint8_t enable, uint16_t up_size, uint16_t low_size)[](#_CPPv425bk_jpeg_enc_encode_config7uint8_t8uint16_t8uint16_t "永久链接至目标")
:   jpeg encode enable encode auto contrl

    This API will use for enable/disable for auto encode size. only valid in jpeh encode mode

    1. this api only called in jpeg_eof_isr function, and only bk_jpeg_enc_enable_encode_auto_ctrl have been set enable

    参数
    :   - **up_size** – the jpeg image upper limit, unit byte

        - **low_size** – the jpeg image lower limit, unit byte

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_jpeg_enc_mode_switch(jpeg_config_t *config)[](#_CPPv423bk_jpeg_enc_mode_switchP13jpeg_config_t "永久链接至目标")
:   jpeg encode mode and yuv mode switch

    This API will use for switch jpeg mode

    1. this api must called in jpeg_eof isr or yuv_eof isr

    参数
    :   **config** – jpeg encode config or jpeg yuv config

    返回
    :   - BK_OK: succeed

        - others: other errors.


## API Typedefs[](#api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [jpeg_enc_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/jpeg_enc_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/jpeg_enc_types.h")


### Macros[](#macros "永久链接至标题")

Y_PIXEL_272[](#c.Y_PIXEL_272 "永久链接至目标")
:   JPEGENC APIs Version 1.0.

    image resolution for hight: Y * 8 = 272

Y_PIXEL_320[](#c.Y_PIXEL_320 "永久链接至目标")
:   image resolution for hight: Y * 8 = 320

X_PIXEL_480[](#c.X_PIXEL_480 "永久链接至目标")
:   image resolution for width: X * 8 = 480

Y_PIXEL_480[](#c.Y_PIXEL_480 "永久链接至目标")
:   image resolution for hight: Y * 8 = 480

X_PIXEL_640[](#c.X_PIXEL_640 "永久链接至目标")
:   image resolution for hight: X * 8 = 640

Y_PIXEL_240[](#c.Y_PIXEL_240 "永久链接至目标")
:   image resolution for hight: Y * 8 = 240

X_PIXEL_320[](#c.X_PIXEL_320 "永久链接至目标")
:   image resolution for hight: X * 8 = 320

Y_PIXEL_600[](#c.Y_PIXEL_600 "永久链接至目标")
:   image resolution for hight: Y * 8 = 600

X_PIXEL_800[](#c.X_PIXEL_800 "永久链接至目标")
:   image resolution for hight: X * 8 = 800

Y_PIXEL_720[](#c.Y_PIXEL_720 "永久链接至目标")
:   image resolution for hight: Y * 8 = 720

X_PIXEL_1280[](#c.X_PIXEL_1280 "永久链接至目标")
:   image resolution for hight: X * 8 = 1280

X_PIXEL_1600[](#c.X_PIXEL_1600 "永久链接至目标")
:   image resolution for hight: X * 8 = 1600

Y_PIXEL_1200[](#c.Y_PIXEL_1200 "永久链接至目标")
:   image resolution for hight: Y * 8 = 1200


### Type Definitions[](#type-definitions "永久链接至标题")

typedef void (*jpeg_isr_t)(jpeg_unit_t id, void *param)[](#_CPPv410jpeg_isr_t "永久链接至目标")
:   jpeg isr callback relay jpeg driver

    Param id, :
    :   only 0 useful, set 0 default

    Param param, :
    :   NULL default


### Enumerations[](#enumerations "永久链接至标题")

enum jpeg_gpio_mode_t[](#_CPPv416jpeg_gpio_mode_t "永久链接至目标")
:   *Values:*

    enumerator JPEG_GPIO_CLK[](#_CPPv4N16jpeg_gpio_mode_t13JPEG_GPIO_CLKE "永久链接至目标")
    :   enable jpeg mclk and pclk gpio function

    enumerator JPEG_GPIO_DATA[](#_CPPv4N16jpeg_gpio_mode_t14JPEG_GPIO_DATAE "永久链接至目标")
    :   enable jpeg vsync/hsync/D0-D7 gpio function

    enumerator JPEG_GPIO_HSYNC_DATA[](#_CPPv4N16jpeg_gpio_mode_t20JPEG_GPIO_HSYNC_DATAE "永久链接至目标")
    :   enable jpeg hsync/D0-D7 gpio function

    enumerator JPEG_GPIO_ALL[](#_CPPv4N16jpeg_gpio_mode_t13JPEG_GPIO_ALLE "永久链接至目标")
    :   enable all jpeg gpio function
