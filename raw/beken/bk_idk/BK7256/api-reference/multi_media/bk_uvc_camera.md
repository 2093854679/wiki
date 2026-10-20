---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/api-reference/multi_media/bk_uvc_camera.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="uvc-camera-apis"></a>

# UVC\_CAMERA APIs

重要

The UVC\_CAMERA API v1.0 is the lastest stable UVC\_CAMERA APIs. All new applications should use UVC\_CAMERA API v1.0.

<a id="uvc-camera-interface"></a>

## UVC\_CAMERA Interface

> UVC camera only support full speed type

<a id="uvc-camera-api-categories"></a>

## UVC\_CAMERA API Categories

Most of UVC\_CAMERA APIs can be categoried as:

> - UVC\_CAMERA APIs
>
>   The common APIs are prefixed with bk\_uvc, e.g. bk\_uvc\_init() etc.

UVC\_CAMERA APIs:
:   - [`bk_uvc_camera_driver_init()`](#_CPPv425bk_uvc_camera_driver_initP19uvc_camera_config_t "bk_uvc_camera_driver_init") \- init uvc camera(open uvc device)
    - [`bk_uvc_camera_driver_deinit()`](#_CPPv427bk_uvc_camera_driver_deinitv "bk_uvc_camera_driver_deinit") \- deinit uvc camera(close uvc device)
    - `bk_uvc_camera_power_on()` \- power on uvc
    - [`bk_uvc_camera_get_config()`](#_CPPv424bk_uvc_camera_get_configP19uvc_camera_device_t8uint16_t "bk_uvc_camera_get_config") \- set uvc camera pps(image resolution) and fps(frame rate)
    - [`bk_uvc_camera_set_config()`](#_CPPv424bk_uvc_camera_set_config19media_camera_type_tP19uvc_camera_device_t "bk_uvc_camera_set_config") \- set uvc camera pps(image resolution) and fps(frame rate)
    - `bk_uvc_camera_driver_start()` \- start uvc, start simple image information
    - `bk_uvc_camera_driver_stop()` \- stop uvc, stop simple image information
    - [`bk_uvc_camera_get_device()`](#_CPPv424bk_uvc_camera_get_devicev "bk_uvc_camera_get_device") \- get current working uvc device

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [uvc\_camera.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/uvc_camera.h)

<a id="functions"></a>

### Functions

<a id="_CPPv425bk_uvc_camera_driver_initP19uvc_camera_config_t"></a>

<a id="_CPPv325bk_uvc_camera_driver_initP19uvc_camera_config_t"></a> <a id="_CPPv225bk_uvc_camera_driver_initP19uvc_camera_config_t"></a> <a id="bk_uvc_camera_driver_init__uvc_camera_config_tP"></a> <a id="uvc__camera_8h_1a318c95553a5c8e0b918bb62ca4b91009"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uvc\_camera\_driver\_init(uvc\_camera\_config\_t \*config)
:   Init the uvc.

    This API init psram, dma, uvc param, and open uvc

    参数
    :   **data** – configure for camera

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv427bk_uvc_camera_driver_deinitv"></a>

<a id="_CPPv327bk_uvc_camera_driver_deinitv"></a> <a id="_CPPv227bk_uvc_camera_driver_deinitv"></a> <a id="bk_uvc_camera_driver_deinit__void"></a> <a id="uvc__camera_8h_1a999108d7cb85f81e1f7af2f9b05d8472"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uvc\_camera\_driver\_deinit(void)
:   Deinit the uvc.

    This API deinit dma and close uvc

    : called after bk\_uvc\_camera\_driver\_init

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv426bk_uvc_camera_power_enable7uint8_t"></a>

<a id="_CPPv326bk_uvc_camera_power_enable7uint8_t"></a> <a id="_CPPv226bk_uvc_camera_power_enable7uint8_t"></a> <a id="bk_uvc_camera_power_enable__uint8_t"></a> <a id="uvc__camera_8h_1a6f7687469b9e7c238dd0186930248648"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uvc\_camera\_power\_enable(uint8\_t enable)
:   uvc power on

    This API called by user, before calling bk\_uvc\_camera\_driver\_init, you should power on uvc

    1\. This api config different gpio and different active level

    参数
    :   **enable** – power up/down:1/0

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv424bk_uvc_camera_get_configP19uvc_camera_device_t8uint16_t"></a>

<a id="_CPPv324bk_uvc_camera_get_configP19uvc_camera_device_t8uint16_t"></a> <a id="_CPPv224bk_uvc_camera_get_configP19uvc_camera_device_t8uint16_t"></a> <a id="bk_uvc_camera_get_config__uvc_camera_device_tP.uint16_t"></a> <a id="uvc__camera_8h_1a80c195669458438dc180a3874fbf41c1"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uvc\_camera\_get\_config(uvc\_camera\_device\_t \*param, uint16\_t count)
:   Get uvc config.

    This API called by user, get uvc support fps and resolutions

    参数
    :   - **param** – the memory user malloc for save uvc support config
        - **count** – the param1 malloc size, the count config of uvc support

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_uvc_camera_set_config19media_camera_type_tP19uvc_camera_device_t"></a>

<a id="_CPPv324bk_uvc_camera_set_config19media_camera_type_tP19uvc_camera_device_t"></a> <a id="_CPPv224bk_uvc_camera_set_config19media_camera_type_tP19uvc_camera_device_t"></a> <a id="bk_uvc_camera_set_config__media_camera_type_t.uvc_camera_device_tP"></a> <a id="uvc__camera_8h_1a476473e4f2d44940127694e1165d6cbe"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uvc\_camera\_set\_config(media\_camera\_type\_t type, uvc\_camera\_device\_t \*config)
:   Set uvc config.

    This API called by user, Set uvc support fps and resolutions

    参数
    :   - **mode** – the uvc work type, reference `media_camera_type_t`
        - **config** – the uvc need support param the user set

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv419bk_uvc_camera_startv"></a>

<a id="_CPPv319bk_uvc_camera_startv"></a> <a id="_CPPv219bk_uvc_camera_startv"></a> <a id="bk_uvc_camera_start__void"></a> <a id="uvc__camera_8h_1a1ed6f44470b969e3b1afb859aab388a8"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uvc\_camera\_start(void)
:   Set uvc start.

    This API called by user, Set uvc start transfer

    1\. this api called must after uvc have been init and have stopped

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv418bk_uvc_camera_stopv"></a>

<a id="_CPPv318bk_uvc_camera_stopv"></a> <a id="_CPPv218bk_uvc_camera_stopv"></a> <a id="bk_uvc_camera_stop__void"></a> <a id="uvc__camera_8h_1a1fe8638e248eb59a2a63df126aa0b4d7"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uvc\_camera\_stop(void)
:   Stop uvc start.

    This API called by user, Set uvc stop transfer

    1\. this api called must after uvc have been init and have start

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv424bk_uvc_camera_get_devicev"></a>

<a id="_CPPv324bk_uvc_camera_get_devicev"></a> <a id="_CPPv224bk_uvc_camera_get_devicev"></a> <a id="bk_uvc_camera_get_device__void"></a> <a id="uvc__camera_8h_1a898f87bf25b434b597c88d8fa85b0f7d"></a> uvc\_camera\_device\_t \*bk\_uvc\_camera\_get\_device(void)
:   Get current uvc device.

    This API called by user, get currnet uvc device in working

    1\. if no uvc work, the return will be NULL

    返回
    :   - uvc\_camera\_device\_t \*: current working uvc device ptr
        - NULL: no uvc device working

<a id="_CPPv424bk_uvc_camera_drop_frame7uint8_t"></a>

<a id="_CPPv324bk_uvc_camera_drop_frame7uint8_t"></a> <a id="_CPPv224bk_uvc_camera_drop_frame7uint8_t"></a> <a id="bk_uvc_camera_drop_frame__uint8_t"></a> <a id="uvc__camera_8h_1a64437d8d71756adba76d2a97ed579608"></a> void bk\_uvc\_camera\_drop\_frame(uint8\_t number)
:   drop first number frame

    This API called by user, before uvc start work

    1\. this function must called before bk\_uvc\_camera\_driver\_init

    返回
    :   - NULL

<a id="_CPPv422bk_uvc_camera_set_type19media_camera_type_t"></a>

<a id="_CPPv322bk_uvc_camera_set_type19media_camera_type_t"></a> <a id="_CPPv222bk_uvc_camera_set_type19media_camera_type_t"></a> <a id="bk_uvc_camera_set_type__media_camera_type_t"></a> <a id="uvc__camera_8h_1a986611cad88af6fc5b062a9212eac534"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uvc\_camera\_set\_type(media\_camera\_type\_t type)

<a id="_CPPv418bk_uvc_camera_initP12uvc_config_t"></a>

<a id="_CPPv318bk_uvc_camera_initP12uvc_config_t"></a> <a id="_CPPv218bk_uvc_camera_initP12uvc_config_t"></a> <a id="bk_uvc_camera_init__uvc_config_tP"></a> <a id="uvc__camera_8h_1a077c837752fa3cf186fb4eb022af75cd"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uvc\_camera\_init(uvc\_config\_t \*config)

<a id="_CPPv420bk_uvc_camera_deinitv"></a>

<a id="_CPPv320bk_uvc_camera_deinitv"></a> <a id="_CPPv220bk_uvc_camera_deinitv"></a> <a id="bk_uvc_camera_deinit"></a> <a id="uvc__camera_8h_1a11acc2989d6de5b103926f92c88a61d8"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uvc\_camera\_deinit()

<a id="api-typedefs"></a>

## API Typedefs
