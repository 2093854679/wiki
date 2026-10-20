---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/api-reference/multi_media/bk_dvp_camera.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
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

> Current software version support peripherals, please refer to [Support Peripherals](https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/support_peripherals/index.html)

<a id="dvp-camera-api-categories"></a>

## DVP\_CAMERA API Categories

Most of DVP\_CAMERA APIs can be categoried as:

> - DVP\_CAMERA APIs
>
>   The common APIs are prefixed with bk\_camera, e.g. bk\_dvp\_camera\_driver\_init() etc.

DVP\_CAMERA APIs:
:   - [`bk_dvp_camera_driver_init()`](#_CPPv425bk_dvp_camera_driver_initP19dvp_camera_config_t "bk_dvp_camera_driver_init") \- init dvp camera(power on sensor, begin to sample image)
    - [`bk_dvp_camera_driver_deinit()`](#_CPPv427bk_dvp_camera_driver_deinitv "bk_dvp_camera_driver_deinit") \- deinit dvp camera(power off sensor)
    - [`bk_dvp_camera_get_device()`](#_CPPv424bk_dvp_camera_get_devicev "bk_dvp_camera_get_device") \- get current dvp dendor config
    - `bk_dvp_camera_encode_config()` \- change encode image upper and lower size or close auto encode
    - `dvp_camera_i2c_read_uint8()` \- master read dvp senor register value by byte
    - `dvp_camera_i2c_read_uint16()` \- master read dvp senor register value by double byte
    - `dvp_camera_i2c_read_uint8()` \- master write dvp senor register value by byte
    - `dvp_camera_i2c_write_uint16()` \- master write dvp senor register value by double byte

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [dvp\_camera.h](https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/_header_files/bk_idk/include/driver/dvp_camera.h)

<a id="functions"></a>

### Functions

<a id="_CPPv430get_sensor_config_devices_listv"></a>

<a id="_CPPv330get_sensor_config_devices_listv"></a> <a id="_CPPv230get_sensor_config_devices_listv"></a> <a id="get_sensor_config_devices_list__void"></a> <a id="dvp__camera_8h_1ae2dea9f1a486424d8d913dc719599c73"></a> const [dvp\_sensor\_config\_t](#_CPPv419dvp_sensor_config_t "dvp_sensor_config_t") \*\*get\_sensor\_config\_devices\_list(void)

<a id="_CPPv429get_sensor_config_devices_numv"></a>

<a id="_CPPv329get_sensor_config_devices_numv"></a> <a id="_CPPv229get_sensor_config_devices_numv"></a> <a id="get_sensor_config_devices_num__void"></a> <a id="dvp__camera_8h_1ac6c754a6e17e14609f9cae59ebbf99c0"></a> int get\_sensor\_config\_devices\_num(void)

<a id="_CPPv433get_sensor_config_interface_by_id11sensor_id_t"></a>

<a id="_CPPv333get_sensor_config_interface_by_id11sensor_id_t"></a> <a id="_CPPv233get_sensor_config_interface_by_id11sensor_id_t"></a> <a id="get_sensor_config_interface_by_id__sensor_id_t"></a> <a id="dvp__camera_8h_1a33428d6a6d266dd4d8b999912a0aa746"></a> const [dvp\_sensor\_config\_t](#_CPPv419dvp_sensor_config_t "dvp_sensor_config_t") \*get\_sensor\_config\_interface\_by\_id([sensor\_id\_t](#_CPPv411sensor_id_t "sensor_id_t") id)

<a id="_CPPv430bk_dvp_camera_set_devices_listPPK19dvp_sensor_config_t8uint16_t"></a>

<a id="_CPPv330bk_dvp_camera_set_devices_listPPK19dvp_sensor_config_t8uint16_t"></a> <a id="_CPPv230bk_dvp_camera_set_devices_listPPK19dvp_sensor_config_t8uint16_t"></a> <a id="bk_dvp_camera_set_devices_list__dvp_sensor_config_tCPP.uint16_t"></a> <a id="dvp__camera_8h_1abcaa6485d9f2d8a1f05a3c7624574711"></a> void bk\_dvp\_camera\_set\_devices\_list(const [dvp\_sensor\_config\_t](#_CPPv419dvp_sensor_config_t "dvp_sensor_config_t") \*\*list, uint16\_t size)
:   This API set dvp camera device list.

    返回
    :   - void

<a id="_CPPv423bk_dvp_camera_enumeratev"></a>

<a id="_CPPv323bk_dvp_camera_enumeratev"></a> <a id="_CPPv223bk_dvp_camera_enumeratev"></a> <a id="bk_dvp_camera_enumerate__void"></a> <a id="dvp__camera_8h_1a6a72504e096e57917b7ec961285a4303"></a> const [dvp\_sensor\_config\_t](#_CPPv419dvp_sensor_config_t "dvp_sensor_config_t") \*bk\_dvp\_camera\_enumerate(void)
:   enumerate dvp camera

    This API will auto detect dvp sensor, and init sensor, i2c module, psram, dma, ect.

    @attation 1\. bk\_dvp\_camera\_driver\_init api include bk\_dvp\_camera\_enumerate function

    参数
    :   **config** – process for sensor data

    返回
    :   - dvp\_sensor\_config: sensor ptr
        - NULL: not found

<a id="_CPPv425bk_dvp_camera_driver_initP19dvp_camera_config_t"></a>

<a id="_CPPv325bk_dvp_camera_driver_initP19dvp_camera_config_t"></a> <a id="_CPPv225bk_dvp_camera_driver_initP19dvp_camera_config_t"></a> <a id="bk_dvp_camera_driver_init__dvp_camera_config_tP"></a> <a id="dvp__camera_8h_1a1cd85bc809131d7d40be015e932b9025"></a> bk\_err\_t bk\_dvp\_camera\_driver\_init([dvp\_camera\_config\_t](#_CPPv419dvp_camera_config_t "dvp_camera_config_t") \*config)
:   Init the camera.

    This API will auto detect dvp sensor, and init sensor, jpeg module, i2c module, psram, dma, ect.

    @attation 1\. you need make sure upper module exist.

    参数
    :   **config** – process for sensor data

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv427bk_dvp_camera_driver_deinitv"></a>

<a id="_CPPv327bk_dvp_camera_driver_deinitv"></a> <a id="_CPPv227bk_dvp_camera_driver_deinitv"></a> <a id="bk_dvp_camera_driver_deinit__void"></a> <a id="dvp__camera_8h_1a1174994f036322674e7140e2cad9c139"></a> bk\_err\_t bk\_dvp\_camera\_driver\_deinit(void)
:   Deinit the camera.

    This API will deinit sensor, jpeg module, i2c module, psram, dma, ect.

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv424bk_dvp_camera_get_devicev"></a>

<a id="_CPPv324bk_dvp_camera_get_devicev"></a> <a id="_CPPv224bk_dvp_camera_get_devicev"></a> <a id="bk_dvp_camera_get_device__void"></a> <a id="dvp__camera_8h_1a4a9bae6a23efd18005f88f4f8aced4df"></a> media\_camera\_device\_t \*bk\_dvp\_camera\_get\_device(void)
:   Get current use camera.

    This API will called after bk\_dvp\_camera\_driver\_init

    返回
    :   - dvp\_camera\_device\_t \*: succeed
        - NULL: current no sensor work.

<a id="_CPPv426bk_dvp_camera_power_enable7uint8_t"></a>

<a id="_CPPv326bk_dvp_camera_power_enable7uint8_t"></a> <a id="_CPPv226bk_dvp_camera_power_enable7uint8_t"></a> <a id="bk_dvp_camera_power_enable__uint8_t"></a> <a id="dvp__camera_8h_1ad3f74d92b99ef5607028a35e9feab506"></a> bk\_err\_t bk\_dvp\_camera\_power\_enable(uint8\_t enable)
:   dvp power on

    This API called by user, before calling bk\_dvp\_driver\_init, you should power on dvp

    @attation 1\. This api config ctrl by marco VIDEO\_GPIO\_CTRL\_LDO\_ENABLE

    参数
    :   **enable** – power up/down:1/0

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv429bk_dvp_get_sensor_auto_detectv"></a>

<a id="_CPPv329bk_dvp_get_sensor_auto_detectv"></a> <a id="_CPPv229bk_dvp_get_sensor_auto_detectv"></a> <a id="bk_dvp_get_sensor_auto_detect__void"></a> <a id="dvp__camera_8h_1adb852036e5596755bcddee5c928c9374"></a> const [dvp\_sensor\_config\_t](#_CPPv419dvp_sensor_config_t "dvp_sensor_config_t") \*bk\_dvp\_get\_sensor\_auto\_detect(void)
:   auto detect dvp camera

    This API called by user, before use dvp camera

    @attation 1\. This api return a pointer for dvp camera sensor config

    返回
    :   - get current dvp config(type)
        - return NULL

<a id="_CPPv429bk_dvp_camera_free_encode_memv"></a>

<a id="_CPPv329bk_dvp_camera_free_encode_memv"></a> <a id="_CPPv229bk_dvp_camera_free_encode_memv"></a> <a id="bk_dvp_camera_free_encode_mem__void"></a> <a id="dvp__camera_8h_1a1ca93a5384e3075075bd51ed7441855e"></a> bk\_err\_t bk\_dvp\_camera\_free\_encode\_mem(void)
:   free encode mem

    This API called by user, once call this api, will free malloc sram for jpeg enc or h264 encode

    @attation 1\. This api only effect in camera is not working, and call this api when you do not use dvp again, if you want use again, you maybe malloc encode mem success.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv439bk_dvp_camera_h264_regenerate_idr_framev"></a>

<a id="_CPPv339bk_dvp_camera_h264_regenerate_idr_framev"></a> <a id="_CPPv239bk_dvp_camera_h264_regenerate_idr_framev"></a> <a id="bk_dvp_camera_h264_regenerate_idr_frame__void"></a> <a id="dvp__camera_8h_1ae2cd348649fb7622ee37ffe95ced112e"></a> bk\_err\_t bk\_dvp\_camera\_h264\_regenerate\_idr\_frame(void)
:   regenerate idr frame

    This API called by user, once call this api, will regenerate idr frame

    @attation 1\. This api only effect in camera is working, and work in h264 mode or h264\&yuv mode,

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="api-typedefs"></a>

## API Typedefs

<a id="id1"></a>

### Header File

- [dvp\_camera\_types.h](https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/_header_files/bk_idk/include/driver/dvp_camera_types.h)

<a id="structures"></a>

### Structures

<a id="_CPPv419dvp_camera_config_t"></a>

<a id="_CPPv319dvp_camera_config_t"></a> <a id="_CPPv219dvp_camera_config_t"></a> <a id="dvp_camera_config_t"></a> <a id="structdvp__camera__config__t"></a> struct dvp\_camera\_config\_t
:   dvp\_camera config

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19dvp_camera_config_t7fb_initE"></a>

    <a id="_CPPv3N19dvp_camera_config_t7fb_initE"></a> <a id="_CPPv2N19dvp_camera_config_t7fb_initE"></a> <a id="structdvp__camera__config__t_1ad93e7ca7c172fd763fa026368650c099"></a> int (\*fb\_init)(fb\_type\_t type)
    :   init frame buffer

    <a id="_CPPv4N19dvp_camera_config_t9fb_deinitE"></a>

    <a id="_CPPv3N19dvp_camera_config_t9fb_deinitE"></a> <a id="_CPPv2N19dvp_camera_config_t9fb_deinitE"></a> <a id="structdvp__camera__config__t_1a827eaf1d61047bd5886d6ef22d82f019"></a> int (\*fb\_deinit)(fb\_type\_t type)
    :   deinit frame buffer

    <a id="_CPPv4N19dvp_camera_config_t8fb_clearE"></a>

    <a id="_CPPv3N19dvp_camera_config_t8fb_clearE"></a> <a id="_CPPv2N19dvp_camera_config_t8fb_clearE"></a> <a id="structdvp__camera__config__t_1a90f3b816db7bf1b08d042037eac4784e"></a> void (\*fb\_clear)(fb\_type\_t type)
    :   clear frame buffer

    <a id="_CPPv4N19dvp_camera_config_t11fb_completeE"></a>

    <a id="_CPPv3N19dvp_camera_config_t11fb_completeE"></a> <a id="_CPPv2N19dvp_camera_config_t11fb_completeE"></a> <a id="structdvp__camera__config__t_1a0510a02f110694e479b8db9b00b88199"></a> void (\*fb\_complete)(frame\_buffer\_t \*buffer)
    :   dvp notify upper layer a complete frame ready

    <a id="_CPPv4N19dvp_camera_config_t9fb_mallocE"></a>

    <a id="_CPPv3N19dvp_camera_config_t9fb_mallocE"></a> <a id="_CPPv2N19dvp_camera_config_t9fb_mallocE"></a> <a id="structdvp__camera__config__t_1aa4e16ce5b2c15908d2d0daa025eefc25"></a> frame\_buffer\_t \*(\*fb\_malloc)(fb\_type\_t type, uint32\_t size)
    :   malloc jpeg psram buffer

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

    <a id="_CPPv3N19dvp_sensor_config_t7def_fpsE"></a> <a id="_CPPv2N19dvp_sensor_config_t7def_fpsE"></a> <a id="dvp_sensor_config_t::def_fps__frame_fps_t"></a> <a id="structdvp__sensor__config__t_1a72c34312c76b198a36efa2f3b9eb5f7f"></a> frame\_fps\_t def\_fps
    :   sensor default fps

    <a id="_CPPv4N19dvp_sensor_config_t3clkE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t3clkE"></a> <a id="_CPPv2N19dvp_sensor_config_t3clkE"></a> <a id="dvp_sensor_config_t::clk__mclk_freq_t"></a> <a id="structdvp__sensor__config__t_1acc75e0d6e90b402ebb4c2efd2953f7a6"></a> mclk\_freq\_t clk
    :   sensor work clk in config fps and ppi

    <a id="_CPPv4N19dvp_sensor_config_t3fmtE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t3fmtE"></a> <a id="_CPPv2N19dvp_sensor_config_t3fmtE"></a> <a id="dvp_sensor_config_t::fmt__pixel_format_t"></a> <a id="structdvp__sensor__config__t_1a65ff8277a9ec25ac485ff358abd8fe8d"></a> pixel\_format\_t fmt
    :   sensor input data format

    <a id="_CPPv4N19dvp_sensor_config_t5vsyncE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t5vsyncE"></a> <a id="_CPPv2N19dvp_sensor_config_t5vsyncE"></a> <a id="dvp_sensor_config_t::vsync__sync_level_t"></a> <a id="structdvp__sensor__config__t_1a362a51d84e5c4a755e1744181bdd041c"></a> sync\_level\_t vsync
    :   sensor vsync active level

    <a id="_CPPv4N19dvp_sensor_config_t5hsyncE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t5hsyncE"></a> <a id="_CPPv2N19dvp_sensor_config_t5hsyncE"></a> <a id="dvp_sensor_config_t::hsync__sync_level_t"></a> <a id="structdvp__sensor__config__t_1af62377e7f34b990ea6d6a0a7a35b7358"></a> sync\_level\_t hsync
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

    <a id="_CPPv3N19dvp_sensor_config_t6detectE"></a> <a id="_CPPv2N19dvp_sensor_config_t6detectE"></a> <a id="structdvp__sensor__config__t_1aebd73324267e31f955404ec1f5afa0f7"></a> bool (\*detect)(void)
    :   auto detect used dvp sensor

    <a id="_CPPv4N19dvp_sensor_config_t4initE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t4initE"></a> <a id="_CPPv2N19dvp_sensor_config_t4initE"></a> <a id="structdvp__sensor__config__t_1ad3ffee59ad42f2f49c95bc5ca266ec3a"></a> int (\*init)(void)
    :   init dvp sensor

    <a id="_CPPv4N19dvp_sensor_config_t7set_ppiE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t7set_ppiE"></a> <a id="_CPPv2N19dvp_sensor_config_t7set_ppiE"></a> <a id="structdvp__sensor__config__t_1a95009b91ad5fec8fd7818b3ba778a201"></a> int (\*set\_ppi)(media\_ppi\_t ppi)
    :   set resolution of sensor

    <a id="_CPPv4N19dvp_sensor_config_t7set_fpsE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t7set_fpsE"></a> <a id="_CPPv2N19dvp_sensor_config_t7set_fpsE"></a> <a id="structdvp__sensor__config__t_1a47812c1d994d7a2952f9c3de71c4f932"></a> int (\*set\_fps)(frame\_fps\_t fps)
    :   set fps of sensor

    <a id="_CPPv4N19dvp_sensor_config_t10power_downE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t10power_downE"></a> <a id="_CPPv2N19dvp_sensor_config_t10power_downE"></a> <a id="structdvp__sensor__config__t_1af8bcb71c496ecda44014603cf429d4c7"></a> int (\*power\_down)(void)
    :   power down or reset of sensor

    <a id="_CPPv4N19dvp_sensor_config_t13dump_registerE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t13dump_registerE"></a> <a id="_CPPv2N19dvp_sensor_config_t13dump_registerE"></a> <a id="structdvp__sensor__config__t_1aaef7bf2c34cc87f166eef650b7307628"></a> int (\*dump\_register)(media\_ppi\_t ppi)
    :   dump sensor register

    <a id="_CPPv4N19dvp_sensor_config_t13read_registerE"></a>

    <a id="_CPPv3N19dvp_sensor_config_t13read_registerE"></a> <a id="_CPPv2N19dvp_sensor_config_t13read_registerE"></a> <a id="structdvp__sensor__config__t_1ae41d31f8a123db9b763bf54405744a89"></a> void (\*read\_register)(bool enable)
    :   read sensor register when write

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

    <a id="_CPPv4N11sensor_id_t8ID_SC101E"></a>

    <a id="_CPPv3N11sensor_id_t8ID_SC101E"></a> <a id="_CPPv2N11sensor_id_t8ID_SC101E"></a> <a id="dvp__camera__types_8h_1a1e2efa0d9103cfa0fa5e77f4b65701f6a309ebd04930981b6a2fd3461a74367dc"></a> enumerator ID\_SC101
