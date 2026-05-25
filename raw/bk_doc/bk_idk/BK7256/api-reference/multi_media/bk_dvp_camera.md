# DVP_CAMERA APIs[](#dvp-camera-apis "永久链接至标题")

[[English]](../../../../en/v1.5/api-reference/multi_media/bk_dvp_camera.html "../../../../en/v1.5/api-reference/multi_media/bk_dvp_camera.html")

重要

The DVP_CAMERA API v1.0 is the lastest stable DVP_CAMERA APIs. All new applications should use DVP_CAMERA API v1.0.


## DVP_CAMERA Interface[](#dvp-camera-interface "永久链接至标题")

> Current software version support two types dvp sensor: gc0328c and hm1055. they are comunicate by i2c with chip.
> gc0328c have 20pins interface, hm1055 have 24pins interface.
>
> gc0328c support different image resolution and frame rate:
> 1. WQVGA(480*272)
> 2. QVGA(320*240)
> 3. VGA(640*480)
> frame rate: 5fps/10fps/20fps/25fps
>
> hm1055 only support 720p(1280*720) image resolution, and different frame rates: 5fps/15fps/20fps


## DVP_CAMERA API Categories[](#dvp-camera-api-categories "永久链接至标题")

Most of DVP_CAMERA APIs can be categoried as:

> - DVP_CAMERA APIs
>
>   The common APIs are prefixed with bk_camera, e.g. bk_camera_driver_init() etc.

DVP_CAMERA APIs:
:   - [`bk_dvp_camera_driver_init()`](#_CPPv425bk_dvp_camera_driver_initP19dvp_camera_config_t "bk_dvp_camera_driver_init") - init dvp camera(power on sensor, begin to sample image)

    - [`bk_dvp_camera_driver_deinit()`](#_CPPv427bk_dvp_camera_driver_deinitv "bk_dvp_camera_driver_deinit") - deinit dvp camera(power off sensor)

    - [`bk_dvp_camera_get_device()`](#_CPPv424bk_dvp_camera_get_devicev "bk_dvp_camera_get_device") - get current dvp dendor config

    - `bk_dvp_camera_encode_config()` - change encode image upper and lower size or close auto encode

    - `dvp_camera_i2c_read_uint8()` - master read dvp senor register value by byte

    - `dvp_camera_i2c_read_uint16()` - master read dvp senor register value by double byte

    - `dvp_camera_i2c_read_uint8()` - master write dvp senor register value by byte

    - `dvp_camera_i2c_write_uint16()` - master write dvp senor register value by double byte


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [dvp_camera.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dvp_camera.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dvp_camera.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dvp_camera_driver_init([dvp_camera_config_t](#_CPPv419dvp_camera_config_t "dvp_camera_config_t") *config)[](#_CPPv425bk_dvp_camera_driver_initP19dvp_camera_config_t "永久链接至目标")
:   Init the camera.

    This API will auto detect dvp sensor, and init sensor, jpeg module, i2c module, psram, dma, ect.

    1. you need make sure upper module exist.

    参数
    :   **config** – process for sensor data

    返回
    :   - kNoErr: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dvp_camera_driver_deinit(void)[](#_CPPv427bk_dvp_camera_driver_deinitv "永久链接至目标")
:   Deinit the camera.

    This API will deinit sensor, jpeg module, i2c module, psram, dma, ect.

    返回
    :   - kNoErr: succeed

        - others: other errors.

[dvp_camera_device_t](#_CPPv419dvp_camera_device_t "dvp_camera_device_t") *bk_dvp_camera_get_device(void)[](#_CPPv424bk_dvp_camera_get_devicev "永久链接至目标")
:   Get current use camera.

    This API will called after bk_dvp_camera_driver_init

    返回
    :   - [dvp_camera_device_t](#structdvp__camera__device__t "#structdvp__camera__device__t") *: succeed

        - NULL: current no sensor work.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_dvp_camera_power_enable(uint8_t enable)[](#_CPPv426bk_dvp_camera_power_enable7uint8_t "永久链接至目标")
:   dvp power on

    This API called by user, before calling bk_dvp_driver_init, you should power on dvp

    1. This api config ctrl by marco VIDEO_GPIO_CTRL_LDO_ENABLE

    参数
    :   **enable** – power up/down:1/0

    返回
    :   - BK_OK: succeed

        - others: other errors.

const [dvp_sensor_config_t](#_CPPv419dvp_sensor_config_t "dvp_sensor_config_t") *bk_dvp_get_sensor_auto_detect(void)[](#_CPPv429bk_dvp_get_sensor_auto_detectv "永久链接至目标")
:   auto detect dvp camera

    This API called by user, before use dvp camera

    1. This api return a pointer for dvp camera sensor config

    返回
    :   - get current dvp config(type)

        - return NULL


## API Typedefs[](#api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [dvp_camera_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dvp_camera_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dvp_camera_types.h")


### Structures[](#structures "永久链接至标题")

struct dvp_camera_config_t[](#_CPPv419dvp_camera_config_t "永久链接至目标")
:   dvp_camera config

    Public Members

    media_ppi_t ppi[](#_CPPv4N19dvp_camera_config_t3ppiE "永久链接至目标")
    :   sensor image resolution

    media_camera_type_t type[](#_CPPv4N19dvp_camera_config_t4typeE "永久链接至目标")
    :   sensor output mode yuv/jpeg

    int (*fb_jpeg_init)(media_ppi_t max_ppi)[](#_CPPv4N19dvp_camera_config_t12fb_jpeg_initE "永久链接至目标")
    :   init jpeg psram buffer

    int (*fb_jpeg_deinit)(void)[](#_CPPv4N19dvp_camera_config_t14fb_jpeg_deinitE "永久链接至目标")
    :   deinit jpeg psram buffer

    int (*fb_display_init)(media_ppi_t max_ppi)[](#_CPPv4N19dvp_camera_config_t15fb_display_initE "永久链接至目标")
    :   init yuv psram buffer

    int (*fb_display_deinit)(void)[](#_CPPv4N19dvp_camera_config_t17fb_display_deinitE "永久链接至目标")
    :   deinit yuv psram buffer

    void (*fb_jpeg_complete)(frame_buffer_t *buffer)[](#_CPPv4N19dvp_camera_config_t16fb_jpeg_completeE "永久链接至目标")
    :   dvp notify upper layer a complete frame ready

    frame_buffer_t *(*fb_jpeg_malloc)(void)[](#_CPPv4N19dvp_camera_config_t14fb_jpeg_mallocE "永久链接至目标")
    :   malloc jpeg psram buffer

    frame_buffer_t *(*fb_display_malloc)(void)[](#_CPPv4N19dvp_camera_config_t17fb_display_mallocE "永久链接至目标")
    :   malloc yuv psram buffer

    void (*drop_frame)(uint8_t index)[](#_CPPv4N19dvp_camera_config_t10drop_frameE "永久链接至目标")
    :   jpeg module drop dvp source frame according to index

struct dvp_sensor_config_t[](#_CPPv419dvp_sensor_config_t "永久链接至目标")
:   dvp sensor configure

    Public Members

    char *name[](#_CPPv4N19dvp_sensor_config_t4nameE "永久链接至目标")
    :   sensor name

    media_ppi_t def_ppi[](#_CPPv4N19dvp_sensor_config_t7def_ppiE "永久链接至目标")
    :   sensor default resolution

    sensor_fps_t def_fps[](#_CPPv4N19dvp_sensor_config_t7def_fpsE "永久链接至目标")
    :   sensor default fps

    jpeg_clk_t clk[](#_CPPv4N19dvp_sensor_config_t3clkE "永久链接至目标")
    :   sensor work clk in config fps and ppi

    pixel_format_t fmt[](#_CPPv4N19dvp_sensor_config_t3fmtE "永久链接至目标")
    :   sensor input data format

    jpeg_sync_level_t vsync[](#_CPPv4N19dvp_sensor_config_t5vsyncE "永久链接至目标")
    :   sensor vsync active level

    jpeg_sync_level_t hsync[](#_CPPv4N19dvp_sensor_config_t5hsyncE "永久链接至目标")
    :   sensor hsync active level

    uint16_t id[](#_CPPv4N19dvp_sensor_config_t2idE "永久链接至目标")
    :   sensor type, sensor_id_t

    uint16_t address[](#_CPPv4N19dvp_sensor_config_t7addressE "永久链接至目标")
    :   sensor write register address by i2c

    uint16_t fps_cap[](#_CPPv4N19dvp_sensor_config_t7fps_capE "永久链接至目标")
    :   sensor support fps

    uint16_t ppi_cap[](#_CPPv4N19dvp_sensor_config_t7ppi_capE "永久链接至目标")
    :   sensor support resoultions

    bool (*detect)(void)[](#_CPPv4N19dvp_sensor_config_t6detectE "永久链接至目标")
    :   auto detect used dvp sensor

    int (*init)(void)[](#_CPPv4N19dvp_sensor_config_t4initE "永久链接至目标")
    :   init dvp sensor

    int (*set_ppi)(media_ppi_t ppi)[](#_CPPv4N19dvp_sensor_config_t7set_ppiE "永久链接至目标")
    :   set resolution of sensor

    int (*set_fps)(sensor_fps_t fps)[](#_CPPv4N19dvp_sensor_config_t7set_fpsE "永久链接至目标")
    :   set fps of sensor

    int (*power_down)(void)[](#_CPPv4N19dvp_sensor_config_t10power_downE "永久链接至目标")
    :   power down or reset of sensor

    int (*dump_register)(media_ppi_t ppi)[](#_CPPv4N19dvp_sensor_config_t13dump_registerE "永久链接至目标")
    :   dump sensor register

    void (*read_register)(bool enable)[](#_CPPv4N19dvp_sensor_config_t13read_registerE "永久链接至目标")
    :   read sensor register when write

struct dvp_camera_device_t[](#_CPPv419dvp_camera_device_t "永久链接至目标")
:   current used camera config

    Public Members

    media_ppi_t ppi[](#_CPPv4N19dvp_camera_device_t3ppiE "永久链接至目标")
    :   sensor image resolution

    sensor_fps_t fps[](#_CPPv4N19dvp_camera_device_t3fpsE "永久链接至目标")
    :   sensor fps

    char *name[](#_CPPv4N19dvp_camera_device_t4nameE "永久链接至目标")
    :   sensor name

    uint16_t id[](#_CPPv4N19dvp_camera_device_t2idE "永久链接至目标")
    :   sensor type, sensor_id_t

    uint16_t fps_cap[](#_CPPv4N19dvp_camera_device_t7fps_capE "永久链接至目标")
    :   sensor support fps

    uint16_t ppi_cap[](#_CPPv4N19dvp_camera_device_t7ppi_capE "永久链接至目标")
    :   sensor support resoultions

    uint32_t pixel_size[](#_CPPv4N19dvp_camera_device_t10pixel_sizeE "永久链接至目标")
    :   sensor output image width

    media_camera_type_t type[](#_CPPv4N19dvp_camera_device_t4typeE "永久链接至目标")
    :   dvp camera work type


### Macros[](#macros "永久链接至标题")

GC_QVGA_USE_SUBSAMPLE[](#c.GC_QVGA_USE_SUBSAMPLE "永久链接至目标")


### Enumerations[](#enumerations "永久链接至标题")

enum sensor_id_t[](#_CPPv411sensor_id_t "永久链接至目标")
:   dvp sensor id type


    *Values:*

    enumerator ID_UNKNOW[](#_CPPv4N11sensor_id_t9ID_UNKNOWE "永久链接至目标")

    enumerator ID_PAS6329[](#_CPPv4N11sensor_id_t10ID_PAS6329E "永久链接至目标")

    enumerator ID_OV7670[](#_CPPv4N11sensor_id_t9ID_OV7670E "永久链接至目标")

    enumerator ID_PAS6375[](#_CPPv4N11sensor_id_t10ID_PAS6375E "永久链接至目标")

    enumerator ID_GC0328C[](#_CPPv4N11sensor_id_t10ID_GC0328CE "永久链接至目标")

    enumerator ID_BF2013[](#_CPPv4N11sensor_id_t9ID_BF2013E "永久链接至目标")

    enumerator ID_GC0308C[](#_CPPv4N11sensor_id_t10ID_GC0308CE "永久链接至目标")

    enumerator ID_HM1055[](#_CPPv4N11sensor_id_t9ID_HM1055E "永久链接至目标")

    enumerator ID_GC2145[](#_CPPv4N11sensor_id_t9ID_GC2145E "永久链接至目标")

    enumerator ID_OV2640[](#_CPPv4N11sensor_id_t9ID_OV2640E "永久链接至目标")

    enumerator ID_GC0308[](#_CPPv4N11sensor_id_t9ID_GC0308E "永久链接至目标")

    enumerator ID_TVP5150[](#_CPPv4N11sensor_id_t10ID_TVP5150E "永久链接至目标")
