# UVC_CAMERA APIs[](#uvc-camera-apis "永久链接至标题")

[[English]](../../../../en/v1.5/api-reference/multi_media/bk_uvc_camera.html "../../../../en/v1.5/api-reference/multi_media/bk_uvc_camera.html")

重要

The UVC_CAMERA API v1.0 is the lastest stable UVC_CAMERA APIs. All new applications should use UVC_CAMERA API v1.0.


## UVC_CAMERA Interface[](#uvc-camera-interface "永久链接至标题")

> UVC camera only support full speed type


## UVC_CAMERA API Categories[](#uvc-camera-api-categories "永久链接至标题")

Most of UVC_CAMERA APIs can be categoried as:

> - UVC_CAMERA APIs
>
>   The common APIs are prefixed with bk_uvc, e.g. bk_uvc_init() etc.

UVC_CAMERA APIs:
:   - [`bk_uvc_camera_driver_init()`](#_CPPv425bk_uvc_camera_driver_initP19uvc_camera_config_t "bk_uvc_camera_driver_init") - init uvc camera(open uvc device)

    - [`bk_uvc_camera_driver_deinit()`](#_CPPv427bk_uvc_camera_driver_deinitv "bk_uvc_camera_driver_deinit") - deinit uvc camera(close uvc device)

    - `bk_uvc_camera_power_on()` - power on uvc

    - [`bk_uvc_camera_get_config()`](#_CPPv424bk_uvc_camera_get_configP19uvc_camera_device_t8uint16_t "bk_uvc_camera_get_config") - set uvc camera pps(image resolution) and fps(frame rate)

    - [`bk_uvc_camera_set_config()`](#_CPPv424bk_uvc_camera_set_config19media_camera_type_tP19uvc_camera_device_t "bk_uvc_camera_set_config") - set uvc camera pps(image resolution) and fps(frame rate)

    - `bk_uvc_camera_driver_start()` - start uvc, start simple image information

    - `bk_uvc_camera_driver_stop()` - stop uvc, stop simple image information

    - [`bk_uvc_camera_get_device()`](#_CPPv424bk_uvc_camera_get_devicev "bk_uvc_camera_get_device") - get current working uvc device


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [uvc_camera.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/uvc_camera.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/uvc_camera.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uvc_camera_driver_init(uvc_camera_config_t *config)[](#_CPPv425bk_uvc_camera_driver_initP19uvc_camera_config_t "永久链接至目标")
:   Init the uvc.

    This API init psram, dma, uvc param, and open uvc

    参数
    :   **data** – configure for camera

    返回
    :   - kNoErr: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uvc_camera_driver_deinit(void)[](#_CPPv427bk_uvc_camera_driver_deinitv "永久链接至目标")
:   Deinit the uvc.

    This API deinit dma and close uvc

    : called after bk_uvc_camera_driver_init

    返回
    :   - kNoErr: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uvc_camera_power_enable(uint8_t enable)[](#_CPPv426bk_uvc_camera_power_enable7uint8_t "永久链接至目标")
:   uvc power on

    This API called by user, before calling bk_uvc_camera_driver_init, you should power on uvc

    1. This api config different gpio and different active level

    参数
    :   **enable** – power up/down:1/0

    返回
    :   - kNoErr: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uvc_camera_get_config(uvc_camera_device_t *param, uint16_t count)[](#_CPPv424bk_uvc_camera_get_configP19uvc_camera_device_t8uint16_t "永久链接至目标")
:   Get uvc config.

    This API called by user, get uvc support fps and resolutions

    参数
    :   - **param** – the memory user malloc for save uvc support config

        - **count** – the param1 malloc size, the count config of uvc support

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uvc_camera_set_config(media_camera_type_t type, uvc_camera_device_t *config)[](#_CPPv424bk_uvc_camera_set_config19media_camera_type_tP19uvc_camera_device_t "永久链接至目标")
:   Set uvc config.

    This API called by user, Set uvc support fps and resolutions

    参数
    :   - **mode** – the uvc work type, reference `media_camera_type_t`

        - **config** – the uvc need support param the user set

    返回
    :   - kNoErr: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uvc_camera_start(void)[](#_CPPv419bk_uvc_camera_startv "永久链接至目标")
:   Set uvc start.

    This API called by user, Set uvc start transfer

    1. this api called must after uvc have been init and have stopped

    返回
    :   - kNoErr: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uvc_camera_stop(void)[](#_CPPv418bk_uvc_camera_stopv "永久链接至目标")
:   Stop uvc start.

    This API called by user, Set uvc stop transfer

    1. this api called must after uvc have been init and have start

    返回
    :   - kNoErr: succeed

        - others: other errors.

uvc_camera_device_t *bk_uvc_camera_get_device(void)[](#_CPPv424bk_uvc_camera_get_devicev "永久链接至目标")
:   Get current uvc device.

    This API called by user, get currnet uvc device in working

    1. if no uvc work, the return will be NULL

    返回
    :   - uvc_camera_device_t *: current working uvc device ptr

        - NULL: no uvc device working

void bk_uvc_camera_drop_frame(uint8_t number)[](#_CPPv424bk_uvc_camera_drop_frame7uint8_t "永久链接至目标")
:   drop first number frame

    This API called by user, before uvc start work

    1. this function must called before bk_uvc_camera_driver_init

    返回
    :   - NULL

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uvc_camera_set_type(media_camera_type_t type)[](#_CPPv422bk_uvc_camera_set_type19media_camera_type_t "永久链接至目标")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uvc_camera_init(uvc_config_t *config)[](#_CPPv418bk_uvc_camera_initP12uvc_config_t "永久链接至目标")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_uvc_camera_deinit()[](#_CPPv420bk_uvc_camera_deinitv "永久链接至目标")


## API Typedefs[](#api-typedefs "永久链接至标题")
