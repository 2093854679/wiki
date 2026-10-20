---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/api-reference/multi_media/bk_uvc_camera.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
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
    - [`bk_uvc_camera_set_config()`](#_CPPv424bk_uvc_camera_set_configP15bk_uvc_config_t "bk_uvc_camera_set_config") \- set uvc camera pps(image resolution) and fps(frame rate)
    - `bk_uvc_camera_driver_start()` \- start uvc, start simple image information
    - `bk_uvc_camera_driver_stop()` \- stop uvc, stop simple image information
    - [`bk_uvc_camera_get_device()`](#_CPPv424bk_uvc_camera_get_devicev "bk_uvc_camera_get_device") \- get current working uvc device

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [uvc\_camera.h](https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/_header_files/bk_idk/include/driver/uvc_camera.h)

<a id="functions"></a>

### Functions

<a id="_CPPv425bk_uvc_camera_driver_initP19uvc_camera_config_t"></a>

<a id="_CPPv325bk_uvc_camera_driver_initP19uvc_camera_config_t"></a> <a id="_CPPv225bk_uvc_camera_driver_initP19uvc_camera_config_t"></a> <a id="bk_uvc_camera_driver_init__uvc_camera_config_tP"></a> <a id="uvc__camera_8h_1a318c95553a5c8e0b918bb62ca4b91009"></a> bk\_err\_t bk\_uvc\_camera\_driver\_init(uvc\_camera\_config\_t \*config)
:   Init the uvc.

    This API init psram, dma, uvc param, and open uvc

    参数
    :   **data** – configure for camera

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv427bk_uvc_camera_driver_deinitv"></a>

<a id="_CPPv327bk_uvc_camera_driver_deinitv"></a> <a id="_CPPv227bk_uvc_camera_driver_deinitv"></a> <a id="bk_uvc_camera_driver_deinit__void"></a> <a id="uvc__camera_8h_1a999108d7cb85f81e1f7af2f9b05d8472"></a> bk\_err\_t bk\_uvc\_camera\_driver\_deinit(void)
:   Deinit the uvc.

    This API deinit dma and close uvc

    @attation: called after bk\_uvc\_camera\_driver\_init

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv426bk_uvc_camera_power_enable7uint8_t7uint8_t"></a>

<a id="_CPPv326bk_uvc_camera_power_enable7uint8_t7uint8_t"></a> <a id="_CPPv226bk_uvc_camera_power_enable7uint8_t7uint8_t"></a> <a id="bk_uvc_camera_power_enable__uint8_t.uint8_t"></a> <a id="uvc__camera_8h_1a094df383a692371d5bda1ad05264ab2b"></a> bk\_err\_t bk\_uvc\_camera\_power\_enable(uint8\_t enable, uint8\_t active\_level)
:   uvc power on

    This API called by user, before calling bk\_uvc\_camera\_driver\_init, you should power on uvc

    @attation 1\. This api config different gpio and different active level

    参数
    :   - **enable** – power up/down:1/0
        - **enable** – 1:high power leve for power up; 0 low power lever for power up

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv424bk_uvc_camera_get_configP19uvc_camera_device_t8uint16_t"></a>

<a id="_CPPv324bk_uvc_camera_get_configP19uvc_camera_device_t8uint16_t"></a> <a id="_CPPv224bk_uvc_camera_get_configP19uvc_camera_device_t8uint16_t"></a> <a id="bk_uvc_camera_get_config__uvc_camera_device_tP.uint16_t"></a> <a id="uvc__camera_8h_1a80c195669458438dc180a3874fbf41c1"></a> bk\_err\_t bk\_uvc\_camera\_get\_config(uvc\_camera\_device\_t \*param, uint16\_t count)
:   Get uvc config.

    This API called by user, get uvc support fps and resolutions

    参数
    :   - **param** – the memory user malloc for save uvc support config
        - **count** – the param1 malloc size, the count config of uvc support

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv419bk_uvc_camera_startv"></a>

<a id="_CPPv319bk_uvc_camera_startv"></a> <a id="_CPPv219bk_uvc_camera_startv"></a> <a id="bk_uvc_camera_start__void"></a> <a id="uvc__camera_8h_1a1ed6f44470b969e3b1afb859aab388a8"></a> bk\_err\_t bk\_uvc\_camera\_start(void)
:   Set uvc config.

    This API called by user, Set uvc support fps and resolutions

    Set uvc start

    This API called by user, Set uvc start transfer

    @attation 1\. this api called must after uvc have been init and have stopped

    参数
    :   - **mode** – the uvc work type, reference `media_camera_type_t`
        - **config** – the uvc need support param the user set

    返回
    :   - kNoErr: succeed
        - others: other errors.

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv418bk_uvc_camera_stopv"></a>

<a id="_CPPv318bk_uvc_camera_stopv"></a> <a id="_CPPv218bk_uvc_camera_stopv"></a> <a id="bk_uvc_camera_stop__void"></a> <a id="uvc__camera_8h_1a1fe8638e248eb59a2a63df126aa0b4d7"></a> bk\_err\_t bk\_uvc\_camera\_stop(void)
:   Stop uvc start.

    This API called by user, Set uvc stop transfer

    @attation 1\. this api called must after uvc have been init and have start

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv424bk_uvc_camera_get_devicev"></a>

<a id="_CPPv324bk_uvc_camera_get_devicev"></a> <a id="_CPPv224bk_uvc_camera_get_devicev"></a> <a id="bk_uvc_camera_get_device__void"></a> <a id="uvc__camera_8h_1adbc4cc5d003ac776f78deeae0312abe9"></a> media\_camera\_device\_t \*bk\_uvc\_camera\_get\_device(void)
:   Get current uvc device.

    This API called by user, get currnet uvc device in working

    @attation 1\. if no uvc work, the return will be NULL

    返回
    :   - uvc\_camera\_device\_t \*: current working uvc device ptr
        - NULL: no uvc device working

<a id="_CPPv436bk_uvc_camera_register_info_callback17uvc_device_info_t"></a>

<a id="_CPPv336bk_uvc_camera_register_info_callback17uvc_device_info_t"></a> <a id="_CPPv236bk_uvc_camera_register_info_callback17uvc_device_info_t"></a> <a id="bk_uvc_camera_register_info_callback__uvc_device_info_t"></a> <a id="uvc__camera_8h_1a1655072ada8c3dcfb5df1f3c8b86f762"></a> bk\_err\_t bk\_uvc\_camera\_register\_info\_callback(uvc\_device\_info\_t cb)
:   register callback notify uvc device info

    This API called by user, before uvc start work

    @attation 1\. this function will be called when uvc connect success, if you register

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_uvc_camera_set_configP15bk_uvc_config_t"></a>

<a id="_CPPv324bk_uvc_camera_set_configP15bk_uvc_config_t"></a> <a id="_CPPv224bk_uvc_camera_set_configP15bk_uvc_config_t"></a> <a id="bk_uvc_camera_set_config__bk_uvc_config_tP"></a> <a id="uvc__camera_8h_1a0c2a7383232da6abaa3f579a102dff31"></a> bk\_err\_t bk\_uvc\_camera\_set\_config(bk\_uvc\_config\_t \*config)
:   set uvc params

    This API called by user, after uvc bk\_uvc\_camera\_driver\_init, if you called bk\_uvc\_camera\_register\_info\_callback

    @attation 1\. this function need user to call, when register info callback, need set config reference struct bk\_uvc\_config\_t

    @attation 2\. this function will use config param to start uvc

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv434bk_uvc_camera_jpeg_frame_check_eofP7uint8_t8uint32_t"></a>

<a id="_CPPv334bk_uvc_camera_jpeg_frame_check_eofP7uint8_t8uint32_t"></a> <a id="_CPPv234bk_uvc_camera_jpeg_frame_check_eofP7uint8_t8uint32_t"></a> <a id="bk_uvc_camera_jpeg_frame_check_eof__uint8_tP.uint32_t"></a> <a id="uvc__camera_8h_1a7434bbad9dceb79969b5b233fbb83bcf"></a> int bk\_uvc\_camera\_jpeg\_frame\_check\_eof(uint8\_t \*data, uint32\_t length)
:   check input frame length

    This API called by user, check frame valied length, check eof(0xffd9), some frame after ffd9 have invailed data

    @attation, the check length control by marco CONFIG\_JPEG\_FRAME\_CHECK\_LENGTH, default value 1024

    参数
    :   - **1\.** – The frame start address
        - **2\.** – the frame total length

    返回
    :   - length: actual data length
        - others: cannot find 0xffd9, this frame have error

<a id="api-typedefs"></a>

## API Typedefs
