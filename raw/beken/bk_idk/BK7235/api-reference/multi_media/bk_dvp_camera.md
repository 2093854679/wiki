---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7235/zh_CN/v1.5/api-reference/multi_media/bk_dvp_camera.html
sdk_family: bk_idk
chip: BK7235
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="dvp-camera-apis"></a>

# DVP\_CAMERA APIs

重要

The DVP\_CAMERA API v1.0 is the lastest stable DVP\_CAMERA APIs. All new applications should use DVP\_CAMERA API v1.0.

<a id="dvp-camera-interface"></a>

## DVP\_CAMERA Interface

> Current software version support two types dvp sensor: gc0328c and hm1055, they are comunicate by i2c with chip.
> gc0328c have 20pins interface, hm1055 have 24pins interface.
>
> gc0328c support different image resolution and frame rate:
> 1\. WQVGA(480\*272)
> 2\. QVGA(320\*240)
> 3\. VGA(640\*480)
> frame rate: 5fps/10fps/20fps/25fps
>
> hm1055 only support 720p(1280\*720) image resolution, and different frame rates: 5fps/15fps/20fps

<a id="dvp-camera-api-categories"></a>

## DVP\_CAMERA API Categories

Most of DVP\_CAMERA APIs can be categoried as:

> - DVP\_CAMERA APIs
>
>   The common APIs are prefixed with bk\_camera, e.g. bk\_camera\_init() etc.

DVP\_CAMERA APIs:
:   - `bk_camera_init()` \- init dvp camera(power on sensor)
    - `bk_camera_deinit()` \- deinit dvp camera(power off sensor)
    - `bk_camera_sensor_config()` \- set sensor register value(inorder to work at fix pps and fps that user wanted)
    - `bk_camera_set_ppi_fps()` \- set dvp camera pps(image resolution) and fps(frame rate)

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [dvp\_camera.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dvp_camera.h)

<a id="functions"></a>

### Functions

<a id="_CPPv425bk_dvp_camera_driver_initP19dvp_camera_config_t"></a>

<a id="_CPPv325bk_dvp_camera_driver_initP19dvp_camera_config_t"></a> <a id="_CPPv225bk_dvp_camera_driver_initP19dvp_camera_config_t"></a> <a id="bk_dvp_camera_driver_init__dvp_camera_config_tP"></a> <a id="dvp__camera_8h_1a1cd85bc809131d7d40be015e932b9025"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dvp\_camera\_driver\_init([dvp\_camera\_config\_t](#_CPPv419dvp_camera_config_t "dvp_camera_config_t") \*config)
:   Init the camera.

    This API will auto detect dvp sensor, and init sensor, jpeg module, i2c module, psram, dma, ect.

    1\. you need make sure upper module exist.

    参数
    :   **config** – process for sensor data

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv427bk_dvp_camera_driver_deinitv"></a>

<a id="_CPPv327bk_dvp_camera_driver_deinitv"></a> <a id="_CPPv227bk_dvp_camera_driver_deinitv"></a> <a id="bk_dvp_camera_driver_deinit__void"></a> <a id="dvp__camera_8h_1a1174994f036322674e7140e2cad9c139"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dvp\_camera\_driver\_deinit(void)
:   Deinit the camera.

    This API will deinit sensor, jpeg module, i2c module, psram, dma, ect.

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv424bk_dvp_camera_get_devicev"></a>

<a id="_CPPv324bk_dvp_camera_get_devicev"></a> <a id="_CPPv224bk_dvp_camera_get_devicev"></a> <a id="bk_dvp_camera_get_device__void"></a> <a id="dvp__camera_8h_1a09ef6ec12d418612eff12ed09c34b623"></a> [dvp\_camera\_device\_t](#_CPPv419dvp_camera_device_t "dvp_camera_device_t") \*bk\_dvp\_camera\_get\_device(void)
:   Get current use camera.

    This API will called after bk\_dvp\_camera\_driver\_init

    返回
    :   - [dvp\_camera\_device\_t](#structdvp__camera__device__t) \*: succeed
        - NULL: current no sensor work.

<a id="_CPPv426bk_dvp_camera_power_enable7uint8_t"></a>

<a id="_CPPv326bk_dvp_camera_power_enable7uint8_t"></a> <a id="_CPPv226bk_dvp_camera_power_enable7uint8_t"></a> <a id="bk_dvp_camera_power_enable__uint8_t"></a> <a id="dvp__camera_8h_1ad3f74d92b99ef5607028a35e9feab506"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_dvp\_camera\_power\_enable(uint8\_t enable)
:   dvp power on

    This API called by user, before calling bk\_dvp\_driver\_init, you should power on dvp

    1\. This api config ctrl by marco VIDEO\_GPIO\_CTRL\_LDO\_ENABLE

    参数
    :   **enable** – power up/down:1/0

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv429bk_dvp_get_sensor_auto_detectv"></a>

<a id="_CPPv329bk_dvp_get_sensor_auto_detectv"></a> <a id="_CPPv229bk_dvp_get_sensor_auto_detectv"></a> <a id="bk_dvp_get_sensor_auto_detect__void"></a> <a id="dvp__camera_8h_1adb852036e5596755bcddee5c928c9374"></a> const [dvp\_sensor\_config\_t](#_CPPv419dvp_sensor_config_t "dvp_sensor_config_t") \*bk\_dvp\_get\_sensor\_auto\_detect(void)
:   auto detect dvp camera

    This API called by user, before use dvp camera

    1\. This api return a pointer for dvp camera sensor config

    返回
    :   - get current dvp config(type)
        - return NULL

<a id="api-typedefs"></a>

## API Typedefs

<a id="id1"></a>

### Header File

- [dvp\_camera\_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dvp_camera_types.h)

<a id="structures"></a>

### Structures

<a id="_CPPv419dvp_camera_config_t"></a>

<a id="_CPPv319dvp_camera_config_t"></a> <a id="_CPPv219dvp_camera_config_t"></a> <a id="dvp_camera_config_t"></a> <a id="structdvp__camera__config__t"></a> struct dvp\_camera\_config\_t
:   dvp\_camera config

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19dvp_camera_config_t3ppiE"></a>

    <a id="_CPPv3N19dvp_camera_config_t3ppiE"></a> <a id="_CPPv2N19dvp_camera_config_t3ppiE"></a> <a id="dvp_camera_config_t::ppi__media_ppi_t"></a> <a id="structdvp__camera__config__t_1ab42ad2dc78a2e7d2d47b9f17bb5641d5"></a> media\_ppi\_t ppi
    :   sensor image resolution

    <a id="_CPPv4N19dvp_camera_config_t4typeE"></a>

    <a id="_CPPv3N19dvp_camera_config_t4typeE"></a> <a id="_CPPv2N19dvp_camera_config_t4typeE"></a> <a id="dvp_camera_config_t::type__media_camera_type_t"></a> <a id="structdvp__camera__config__t_1a996864341642698edc557063b5e0e5b1"></a> media\_camera\_type\_t type
    :   sensor output mode yuv/jpeg

    <a id="_CPPv4N19dvp_camera_config_t12fb_jpeg_initE"></a>

    <a id="_CPPv3N19dvp_camera_config_t12fb_jpeg_initE"></a> <a id="_CPPv2N19dvp_camera_config_t12fb_jpeg_initE"></a> <a id="structdvp__camera__config__t_1a5c3b46f8e54ae0c350dd47cfe0d244ee"></a> int (\*fb\_jpeg\_init)(media\_ppi\_t max\_ppi)
    :   init jpeg psram buffer

    <a id="_CPPv4N19dvp_camera_config_t14fb_jpeg_deinitE"></a>

    <a id="_CPPv3N19dvp_camera_config_t14fb_jpeg_deinitE"></a> <a id="_CPPv2N19dvp_camera_config_t14fb_jpeg_deinitE"></a> <a id="structdvp__camera__config__t_1a273d1cb585bb8c1717a4d860cf6a8b3c"></a> int (\*fb\_jpeg\_deinit)(void)
    :   deinit jpeg psram buffer

    <a id="_CPPv4N19dvp_camera_config_t15fb_display_initE"></a>

    <a id="_CPPv3N19dvp_camera_config_t15fb_display_initE"></a> <a id="_CPPv2N19dvp_camera_config_t15fb_display_initE"></a> <a id="structdvp__camera__config__t_1aa1808645f82769c04ba1dfd974e5bb10"></a> int (\*fb\_display\_init)(media\_ppi\_t max\_ppi)
    :   init yuv psram buffer

    <a id="_CPPv4N19dvp_camera_config_t17fb_display_deinitE"></a>

    <a id="_CPPv3N19dvp_camera_config_t17fb_display_deinitE"></a> <a id="_CPPv2N19dvp_camera_config_t17fb_display_deinitE"></a> <a id="structdvp__camera__config__t_1a12c2e31148d4d79856f6c5c39cbb2d7a"></a> int (\*fb\_display\_deinit)(void)
    :   deinit yuv psram buffer

    <a id="_CPPv4N19dvp_camera_config_t16fb_jpeg_completeE"></a>

    <a id="_CPPv3N19dvp_camera_config_t16fb_jpeg_completeE"></a> <a id="_CPPv2N19dvp_camera_config_t16fb_jpeg_completeE"></a> <a id="structdvp__camera__config__t_1a900ce3691da6968614aff89c60c43086"></a> void (\*fb\_jpeg\_complete)(frame\_buffer\_t \*buffer)
    :   dvp notify upper layer a complete frame ready

    <a id="_CPPv4N19dvp_camera_config_t14fb_jpeg_mallocE"></a>

    <a id="_CPPv3N19dvp_camera_config_t14fb_jpeg_mallocE"></a> <a id="_CPPv2N19dvp_camera_config_t14fb_jpeg_mallocE"></a> <a id="structdvp__camera__config__t_1aead9994519f40e57c0628f39d8be80a8"></a> frame\_buffer\_t \*(\*fb\_jpeg\_malloc)(void)
    :   malloc jpeg psram buffer

    <a id="_CPPv4N19dvp_camera_config_t17fb_display_mallocE"></a>

    <a id="_CPPv3N19dvp_camera_config_t17fb_display_mallocE"></a> <a id="_CPPv2N19dvp_camera_config_t17fb_display_mallocE"></a> <a id="structdvp__camera__config__t_1aa5623e6875e764b230b91a20d7a8caed"></a> frame\_buffer\_t \*(\*fb\_display\_malloc)(void)
    :   malloc yuv psram buffer

    <a id="_CPPv4N19dvp_camera_config_t10drop_frameE"></a>

    <a id="_CPPv3N19dvp_camera_config_t10drop_frameE"></a> <a id="_CPPv2N19dvp_camera_config_t10drop_frameE"></a> <a id="structdvp__camera__config__t_1a07d40f3b70cbbe495a16eda115a84b56"></a> void (\*drop\_frame)(uint8\_t index)
    :   jpeg module drop dvp source frame according to index

<a id="_CPPv419dvp_sensor_config_t"></a>

<a id="_CPPv319dvp_sensor_config_t"></a> <a id="_CPPv219dvp_sensor_config_t"></a> <a id="dvp_sensor_config_t"></a> <a id="structdvp__sensor__config__t"></a> struct dvp\_sensor\_config\_t
:   dvp sensor configure

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19dvp_sensor_config_t4nameE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t4nameE"></a> <a id="_CPPv2N19dvp_sensor_config_t4nameE"></a> <a id="dvp_sensor_config_t::name__cP"></a> <a id="structdvp__sensor__config__t_1ab7b2b20c53aa87375e3495562f7ee647"></a> char \*name
    :   sensor name

    <a id="_CPPv4N19dvp_sensor_config_t7def_ppiE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t7def_ppiE"></a> <a id="_CPPv2N19dvp_sensor_config_t7def_ppiE"></a> <a id="dvp_sensor_config_t::def_ppi__media_ppi_t"></a> <a id="structdvp__sensor__config__t_1a54a5669482eb1d3cdaebaf1097736df2"></a> media\_ppi\_t def\_ppi
    :   sensor default resolution

    <a id="_CPPv4N19dvp_sensor_config_t7def_fpsE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t7def_fpsE"></a> <a id="_CPPv2N19dvp_sensor_config_t7def_fpsE"></a> <a id="dvp_sensor_config_t::def_fps__sensor_fps_t"></a> <a id="structdvp__sensor__config__t_1aeaafd20e59e9f78e37ef145a57326be2"></a> sensor\_fps\_t def\_fps
    :   sensor default fps

    <a id="_CPPv4N19dvp_sensor_config_t3clkE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t3clkE"></a> <a id="_CPPv2N19dvp_sensor_config_t3clkE"></a> <a id="dvp_sensor_config_t::clk__jpeg_clk_t"></a> <a id="structdvp__sensor__config__t_1a4fb757ca18a8e703e2255edb9b42d8b6"></a> jpeg\_clk\_t clk
    :   sensor work clk in config fps and ppi

    <a id="_CPPv4N19dvp_sensor_config_t3fmtE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t3fmtE"></a> <a id="_CPPv2N19dvp_sensor_config_t3fmtE"></a> <a id="dvp_sensor_config_t::fmt__pixel_format_t"></a> <a id="structdvp__sensor__config__t_1a65ff8277a9ec25ac485ff358abd8fe8d"></a> pixel\_format\_t fmt
    :   sensor input data format

    <a id="_CPPv4N19dvp_sensor_config_t5vsyncE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t5vsyncE"></a> <a id="_CPPv2N19dvp_sensor_config_t5vsyncE"></a> <a id="dvp_sensor_config_t::vsync__jpeg_sync_level_t"></a> <a id="structdvp__sensor__config__t_1a1bb60cc5489e815b37ed876b2b209388"></a> jpeg\_sync\_level\_t vsync
    :   sensor vsync active level

    <a id="_CPPv4N19dvp_sensor_config_t5hsyncE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t5hsyncE"></a> <a id="_CPPv2N19dvp_sensor_config_t5hsyncE"></a> <a id="dvp_sensor_config_t::hsync__jpeg_sync_level_t"></a> <a id="structdvp__sensor__config__t_1aa989017d447933cef6287544aebaf39b"></a> jpeg\_sync\_level\_t hsync
    :   sensor hsync active level

    <a id="_CPPv4N19dvp_sensor_config_t2idE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t2idE"></a> <a id="_CPPv2N19dvp_sensor_config_t2idE"></a> <a id="dvp_sensor_config_t::id__uint16_t"></a> <a id="structdvp__sensor__config__t_1a54479b78007648b61b3c87e8172e7f49"></a> uint16\_t id
    :   sensor type, sensor\_id\_t

    <a id="_CPPv4N19dvp_sensor_config_t7addressE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t7addressE"></a> <a id="_CPPv2N19dvp_sensor_config_t7addressE"></a> <a id="dvp_sensor_config_t::address__uint16_t"></a> <a id="structdvp__sensor__config__t_1af605f3525eae060dc9559b75c49a07f6"></a> uint16\_t address
    :   sensor write register address by i2c

    <a id="_CPPv4N19dvp_sensor_config_t7fps_capE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t7fps_capE"></a> <a id="_CPPv2N19dvp_sensor_config_t7fps_capE"></a> <a id="dvp_sensor_config_t::fps_cap__uint16_t"></a> <a id="structdvp__sensor__config__t_1a031ad0f5bdd0cd7af41cf2a5054103a8"></a> uint16\_t fps\_cap
    :   sensor support fps

    <a id="_CPPv4N19dvp_sensor_config_t7ppi_capE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t7ppi_capE"></a> <a id="_CPPv2N19dvp_sensor_config_t7ppi_capE"></a> <a id="dvp_sensor_config_t::ppi_cap__uint16_t"></a> <a id="structdvp__sensor__config__t_1a1f3132bf13682e13e1138adb139fdeba"></a> uint16\_t ppi\_cap
    :   sensor support resoultions

    <a id="_CPPv4N19dvp_sensor_config_t6detectE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t6detectE"></a> <a id="_CPPv2N19dvp_sensor_config_t6detectE"></a> <a id="structdvp__sensor__config__t_1a1b64e4a9c7797281bcb9de08a02f5852"></a> bool (\*detect)(void)
    :   auto detect used dvp sensor

    <a id="_CPPv4N19dvp_sensor_config_t4initE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t4initE"></a> <a id="_CPPv2N19dvp_sensor_config_t4initE"></a> <a id="structdvp__sensor__config__t_1a7629893b4bb1a4b20337b36e8a144ea7"></a> int (\*init)(void)
    :   init dvp sensor

    <a id="_CPPv4N19dvp_sensor_config_t7set_ppiE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t7set_ppiE"></a> <a id="_CPPv2N19dvp_sensor_config_t7set_ppiE"></a> <a id="structdvp__sensor__config__t_1a623996bcd9781573f5087625d791f3ee"></a> int (\*set\_ppi)(media\_ppi\_t ppi)
    :   set resolution of sensor

    <a id="_CPPv4N19dvp_sensor_config_t7set_fpsE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t7set_fpsE"></a> <a id="_CPPv2N19dvp_sensor_config_t7set_fpsE"></a> <a id="structdvp__sensor__config__t_1ac3744fb53769cc4a293242b69b8497e5"></a> int (\*set\_fps)(sensor\_fps\_t fps)
    :   set fps of sensor

    <a id="_CPPv4N19dvp_sensor_config_t10power_downE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t10power_downE"></a> <a id="_CPPv2N19dvp_sensor_config_t10power_downE"></a> <a id="structdvp__sensor__config__t_1ae163574dd988458862dae284338b2d30"></a> int (\*power\_down)(void)
    :   power down or reset of sensor

    <a id="_CPPv4N19dvp_sensor_config_t13dump_registerE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t13dump_registerE"></a> <a id="_CPPv2N19dvp_sensor_config_t13dump_registerE"></a> <a id="structdvp__sensor__config__t_1aa6f4778e6f1de501f078f166a16bbede"></a> int (\*dump\_register)(media\_ppi\_t ppi)
    :   dump sensor register

    <a id="_CPPv4N19dvp_sensor_config_t13read_registerE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t13read_registerE"></a> <a id="_CPPv2N19dvp_sensor_config_t13read_registerE"></a> <a id="structdvp__sensor__config__t_1ad21e9eb56c6ea944c9d37d85591cbd31"></a> void (\*read\_register)(bool enable)
    :   read sensor register when write

<a id="_CPPv419dvp_camera_device_t"></a>

<a id="_CPPv319dvp_camera_device_t"></a> <a id="_CPPv219dvp_camera_device_t"></a> <a id="dvp_camera_device_t"></a> <a id="structdvp__camera__device__t"></a> struct dvp\_camera\_device\_t
:   current used camera config

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19dvp_camera_device_t3ppiE"></a>

    <a id="_CPPv3N19dvp_camera_device_t3ppiE"></a> <a id="_CPPv2N19dvp_camera_device_t3ppiE"></a> <a id="dvp_camera_device_t::ppi__media_ppi_t"></a> <a id="structdvp__camera__device__t_1a5bd309f58008a962458d85abf115842b"></a> media\_ppi\_t ppi
    :   sensor image resolution

    <a id="_CPPv4N19dvp_camera_device_t3fpsE"></a>

    <a id="_CPPv3N19dvp_camera_device_t3fpsE"></a> <a id="_CPPv2N19dvp_camera_device_t3fpsE"></a> <a id="dvp_camera_device_t::fps__sensor_fps_t"></a> <a id="structdvp__camera__device__t_1ab7ad92d21c956fb8f2f934961f97e2dd"></a> sensor\_fps\_t fps
    :   sensor fps

    <a id="_CPPv4N19dvp_camera_device_t4nameE"></a>

    <a id="_CPPv3N19dvp_camera_device_t4nameE"></a> <a id="_CPPv2N19dvp_camera_device_t4nameE"></a> <a id="dvp_camera_device_t::name__cP"></a> <a id="structdvp__camera__device__t_1a749253ecfec8374a3236f4b9fda35f4d"></a> char \*name
    :   sensor name

    <a id="_CPPv4N19dvp_camera_device_t2idE"></a>

    <a id="_CPPv3N19dvp_camera_device_t2idE"></a> <a id="_CPPv2N19dvp_camera_device_t2idE"></a> <a id="dvp_camera_device_t::id__uint16_t"></a> <a id="structdvp__camera__device__t_1aa12049648d49450927866b7b6ff80b03"></a> uint16\_t id
    :   sensor type, sensor\_id\_t

    <a id="_CPPv4N19dvp_camera_device_t7fps_capE"></a>

    <a id="_CPPv3N19dvp_camera_device_t7fps_capE"></a> <a id="_CPPv2N19dvp_camera_device_t7fps_capE"></a> <a id="dvp_camera_device_t::fps_cap__uint16_t"></a> <a id="structdvp__camera__device__t_1a127864dcb865ed121b5617fdd27dc2e6"></a> uint16\_t fps\_cap
    :   sensor support fps

    <a id="_CPPv4N19dvp_camera_device_t7ppi_capE"></a>

    <a id="_CPPv3N19dvp_camera_device_t7ppi_capE"></a> <a id="_CPPv2N19dvp_camera_device_t7ppi_capE"></a> <a id="dvp_camera_device_t::ppi_cap__uint16_t"></a> <a id="structdvp__camera__device__t_1aeba075932861dd9132bb874033c1caf9"></a> uint16\_t ppi\_cap
    :   sensor support resoultions

    <a id="_CPPv4N19dvp_camera_device_t10pixel_sizeE"></a>

    <a id="_CPPv3N19dvp_camera_device_t10pixel_sizeE"></a> <a id="_CPPv2N19dvp_camera_device_t10pixel_sizeE"></a> <a id="dvp_camera_device_t::pixel_size__uint32_t"></a> <a id="structdvp__camera__device__t_1af6e11e78b65d38f5c2808d0b63b55809"></a> uint32\_t pixel\_size
    :   sensor output image width

    <a id="_CPPv4N19dvp_camera_device_t4typeE"></a>

    <a id="_CPPv3N19dvp_camera_device_t4typeE"></a> <a id="_CPPv2N19dvp_camera_device_t4typeE"></a> <a id="dvp_camera_device_t::type__media_camera_type_t"></a> <a id="structdvp__camera__device__t_1a364d9d4b3a623541f33c71afdc10abc6"></a> media\_camera\_type\_t type
    :   dvp camera work type

<a id="macros"></a>

### Macros

<a id="c.GC_QVGA_USE_SUBSAMPLE"></a>

<a id="dvp__camera__types_8h_1a66644ee9010a9ef92e185f533bc53add"></a> GC\_QVGA\_USE\_SUBSAMPLE

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv411sensor_id_t"></a>

<a id="_CPPv311sensor_id_t"></a> <a id="_CPPv211sensor_id_t"></a> <a id="dvp__camera__types_8h_1a1e2efa0d9103cfa0fa5e77f4b65701f6"></a> enum sensor\_id\_t
:   dvp sensor id type

    *Values:*

    <a id="_CPPv4N11sensor_id_t9ID_UNKNOWE"></a>

    <a id="_CPPv3N11sensor_id_t9ID_UNKNOWE"></a> <a id="_CPPv2N11sensor_id_t9ID_UNKNOWE"></a> <a id="dvp__camera__types_8h_1a1e2efa0d9103cfa0fa5e77f4b65701f6aa522e5582aa8f0d9c6e142840443a523"></a> enumerator ID\_UNKNOW

    <a id="_CPPv4N11sensor_id_t10ID_PAS6329E"></a>

    <a id="_CPPv3N11sensor_id_t10ID_PAS6329E"></a> <a id="_CPPv2N11sensor_id_t10ID_PAS6329E"></a> <a id="dvp__camera__types_8h_1a1e2efa0d9103cfa0fa5e77f4b65701f6a9bee58f985939f499c9d6cd3fe368d8e"></a> enumerator ID\_PAS6329

    <a id="_CPPv4N11sensor_id_t9ID_OV7670E"></a>

    <a id="_CPPv3N11sensor_id_t9ID_OV7670E"></a> <a id="_CPPv2N11sensor_id_t9ID_OV7670E"></a> <a id="dvp__camera__types_8h_1a1e2efa0d9103cfa0fa5e77f4b65701f6a4bff123c4ea8676da98770abdcb36c78"></a> enumerator ID\_OV7670

    <a id="_CPPv4N11sensor_id_t10ID_PAS6375E"></a>

    <a id="_CPPv3N11sensor_id_t10ID_PAS6375E"></a> <a id="_CPPv2N11sensor_id_t10ID_PAS6375E"></a> <a id="dvp__camera__types_8h_1a1e2efa0d9103cfa0fa5e77f4b65701f6acfa56a6897a4e4a0313c06658a5da75c"></a> enumerator ID\_PAS6375

    <a id="_CPPv4N11sensor_id_t10ID_GC0328CE"></a>

    <a id="_CPPv3N11sensor_id_t10ID_GC0328CE"></a> <a id="_CPPv2N11sensor_id_t10ID_GC0328CE"></a> <a id="dvp__camera__types_8h_1a1e2efa0d9103cfa0fa5e77f4b65701f6a467d8e3d0b85197644f4e57f2e9bfd97"></a> enumerator ID\_GC0328C

    <a id="_CPPv4N11sensor_id_t9ID_BF2013E"></a>

    <a id="_CPPv3N11sensor_id_t9ID_BF2013E"></a> <a id="_CPPv2N11sensor_id_t9ID_BF2013E"></a> <a id="dvp__camera__types_8h_1a1e2efa0d9103cfa0fa5e77f4b65701f6a828081741d1e90ce4a84ed13e28a111d"></a> enumerator ID\_BF2013

    <a id="_CPPv4N11sensor_id_t10ID_GC0308CE"></a>

    <a id="_CPPv3N11sensor_id_t10ID_GC0308CE"></a> <a id="_CPPv2N11sensor_id_t10ID_GC0308CE"></a> <a id="dvp__camera__types_8h_1a1e2efa0d9103cfa0fa5e77f4b65701f6a1f60ec9fc31cf2140d8267273df0eef5"></a> enumerator ID\_GC0308C

    <a id="_CPPv4N11sensor_id_t9ID_HM1055E"></a>

    <a id="_CPPv3N11sensor_id_t9ID_HM1055E"></a> <a id="_CPPv2N11sensor_id_t9ID_HM1055E"></a> <a id="dvp__camera__types_8h_1a1e2efa0d9103cfa0fa5e77f4b65701f6a310b28e1516bcc5d04869f1a85d32751"></a> enumerator ID\_HM1055

    <a id="_CPPv4N11sensor_id_t9ID_GC2145E"></a>

    <a id="_CPPv3N11sensor_id_t9ID_GC2145E"></a> <a id="_CPPv2N11sensor_id_t9ID_GC2145E"></a> <a id="dvp__camera__types_8h_1a1e2efa0d9103cfa0fa5e77f4b65701f6a3fc0969905257087061c006548ad7b31"></a> enumerator ID\_GC2145

    <a id="_CPPv4N11sensor_id_t9ID_OV2640E"></a>

    <a id="_CPPv3N11sensor_id_t9ID_OV2640E"></a> <a id="_CPPv2N11sensor_id_t9ID_OV2640E"></a> <a id="dvp__camera__types_8h_1a1e2efa0d9103cfa0fa5e77f4b65701f6aa1f46e481e0e295c2a116c83e74a8275"></a> enumerator ID\_OV2640

    <a id="_CPPv4N11sensor_id_t9ID_GC0308E"></a>

    <a id="_CPPv3N11sensor_id_t9ID_GC0308E"></a> <a id="_CPPv2N11sensor_id_t9ID_GC0308E"></a> <a id="dvp__camera__types_8h_1a1e2efa0d9103cfa0fa5e77f4b65701f6a59ebd0e84e50168cccc19ad6a2b808b3"></a> enumerator ID\_GC0308

    <a id="_CPPv4N11sensor_id_t10ID_TVP5150E"></a>

    <a id="_CPPv3N11sensor_id_t10ID_TVP5150E"></a> <a id="_CPPv2N11sensor_id_t10ID_TVP5150E"></a> <a id="dvp__camera__types_8h_1a1e2efa0d9103cfa0fa5e77f4b65701f6afd325c5527ebb4b555f61ef252ce4ae8"></a> enumerator ID\_TVP5150
