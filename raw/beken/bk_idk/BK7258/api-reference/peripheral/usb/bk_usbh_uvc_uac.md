---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v2.0.1/api-reference/peripheral/usb/bk_usbh_uvc_uac.html
sdk_family: bk_idk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="usb-host-uvc-uac"></a>

# USB Host UVC\+UAC

uvc\_uac\_api\_common是BK7258的 USB UVC \+ UAC 主机驱动程序，支持从 USB 设备读取/写入/控制多媒体流。当前最多同时支持 1 路摄像头 \+ 1 路麦克风 \+ 1 路播放器数据流。
具体的综合使用示例，请参考avdk多媒体代码，谢谢。

<a id="uvc"></a>

## UVC 主机驱动基本使用流程

<a id="id1"></a>
![uvc start stop](../../../../../_assets/64d16fa4e71155f03177-uvc_start_stop.png)


UVC start/stop

<a id="uvc-cli"></a>

## UVC 主机驱动CLI测试示例

注：BK7258 USB 默认运行在CPU2，使用默认avdk调试需要连接UART2协助输入命令测试。 测试目标：UVC 获得参数正常，设置参数正常，Buffer管理正常，启动传输正常，关闭传输正常。

作为HOST 运行Video设备为例，输入命令和LOG信息如下图所示：

<a id="id2"></a>
![uvc connect disconnect](../../../../../_assets/498b1aa6c0c4faa45483-cli_uvc_connect_disconnect.png)


UVC Connect/Disconnect

<a id="id3"></a>
![uvc get param](../../../../../_assets/4d11a21534073e52eee4-cli_uvc_get_param.png)


UVC Get Param

<a id="id4"></a>
![uvc set param](../../../../../_assets/bb035a58d137804262b7-cli_uvc_set_param.png)


UVC Set Param

注：根据获得参数来设置参数，设置最大包长1024字节，分辨率1280X720 索引1，帧率30fps，视频数据格式索引1(实例中1为MJPG)。

<a id="id5"></a>
![uvc reg buffer ops](../../../../../_assets/a12e2e71a33755194424-cli_uvc_register_buffer_ops.png)


UVC Register Buffer ops

注：代码参考视频多媒体，buffer管理部分。

<a id="id6"></a>
![uvc start](../../../../../_assets/091e78566fb5e74130f7-cli_uvc_start.png)


UVC Start

<a id="id7"></a>
![uvc stop](../../../../../_assets/32fd3bc647fcfdecad9b-cli_uvc_stop.png)


UVC Stop

<a id="uac"></a>

## UAC 主机驱动基本使用流程

<a id="id8"></a>
![usb open close](../../../../../_assets/a917884d1e8c1a7dd16b-uac_start_stop.png)


UAC start/stop

<a id="uac-cli"></a>

## UAC 主机驱动CLI测试示例

注：BK7258 USB 默认运行在CPU2，使用默认avdk调试需要连接UART2协助输入命令测试。 测试目标：UVC 获得参数正常，设置参数正常，Buffer管理正常，启动传输正常，关闭传输正常。

作为HOST 运行Video\+Audio融合设备为例，输入命令和LOG信息如下图所示：

<a id="id9"></a>
![uvc connect disconnect](../../../../../_assets/271c5c4b69df2c2196af-cli_uac_connect_disconnect.png)


UAC Connect/Disconnect

<a id="id10"></a>
![uvc get param](../../../../../_assets/16d3ccdcd6c0d8733ea2-cli_uac_get_param.png)


UAC Get Param

<a id="id11"></a>
![uvc set param](../../../../../_assets/76f9b4d7d4282ef2350d-cli_uac_set_param.png)


UAC Set Param

注：根据获得参数来设置参数，设置采样率，音频格式。

<a id="id12"></a>
![uvc reg buffer ops](../../../../../_assets/03c2d5fec73e9a727287-cli_uac_register_buffer_ops.png)


UAC Register Buffer ops

注：代码参考音频多媒体，buffer管理部分。

<a id="id13"></a>
![uvc mic start](../../../../../_assets/fcf59c211cf4f89a7a37-cli_uac_mic_start.png)


UAC MIC Start

<a id="id14"></a>
![uvc mic stop](../../../../../_assets/c0a7e997a0a7b2d86081-cli_uac_mic_stop.png)


UAC MIC Stop

<a id="id15"></a>
![uvc start](../../../../../_assets/5b9129dc85dd81a68c4f-cli_uac_speaker_start.png)


UAC SPK Start

<a id="id16"></a>
![uvc stop](../../../../../_assets/329efd7706e064c8ab7c-cli_uac_speaker_stop.png)


UAC SPK Stop

<a id="usb-uvc-uac-reference"></a>

## USB UVC UAC Reference

<a id="header-file"></a>

### Header File

- [uvc\_uac\_api\_common.h](https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v2.0.1/_header_files/include/components/uvc_uac_api_common.h)

<a id="functions"></a>

### Functions

<a id="_CPPv428bk_uvc_uac_register_callbackP23bk_uvc_uac_app_callback"></a>

<a id="_CPPv328bk_uvc_uac_register_callbackP23bk_uvc_uac_app_callback"></a> <a id="_CPPv228bk_uvc_uac_register_callbackP23bk_uvc_uac_app_callback"></a> <a id="bk_uvc_uac_register_callback__bk_uvc_uac_app_callbackP"></a> <a id="uvc__uac__api__common_8h_1ad89a944d9c23e1baf1d86e03fac99329"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uvc\_uac\_register\_callback([bk\_uvc\_uac\_app\_callback](../bk_usb.md#_CPPv423bk_uvc_uac_app_callback "bk_uvc_uac_app_callback") \*uvc\_uac\_all\_cb)
:   Registering the callback function for UVC and UAC fusion devices.

    Register the corresponding callback function based on the structure, and be sure to fill in the specific type to facilitate the management of the callback function parameter: uvc\_uac\_all\_cb E\_USB\_DEVICE\_T dev; FUNCPTR uvc\_uac\_connect\_cb; FUNCPTR uvc\_uac\_disconnect\_cb;

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv436bk_usb_uvc_register_connect_callbackPv"></a>

<a id="_CPPv336bk_usb_uvc_register_connect_callbackPv"></a> <a id="_CPPv236bk_usb_uvc_register_connect_callbackPv"></a> <a id="bk_usb_uvc_register_connect_callback__voidP"></a> <a id="uvc__uac__api__common_8h_1a1bcd375c67bea5e205d3884c5953a23c"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_usb\_uvc\_register\_connect\_callback(void \*param)
:   UVC connect the callback function registration function registration.

    This API connect the callback:

    - parameter is the registered callback function.
    - The callback function needs to be defined.

    Notify the registered callback function when the device is connected.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv439bk_usb_uvc_register_disconnect_callbackPv"></a>

<a id="_CPPv339bk_usb_uvc_register_disconnect_callbackPv"></a> <a id="_CPPv239bk_usb_uvc_register_disconnect_callbackPv"></a> <a id="bk_usb_uvc_register_disconnect_callback__voidP"></a> <a id="uvc__uac__api__common_8h_1a4bd89c30457221b3b4c32a228245765d"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_usb\_uvc\_register\_disconnect\_callback(void \*param)
:   UVC disconnect the callback function registration function registration.

    This API disconnect the callback:

    - parameter is the registered callback function.
    - The callback function needs to be defined.

    Notify the registered callback function when the device is disconnected.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_usb_uvc_get_paramP26bk_uvc_device_brief_info_t"></a>

<a id="_CPPv320bk_usb_uvc_get_paramP26bk_uvc_device_brief_info_t"></a> <a id="_CPPv220bk_usb_uvc_get_paramP26bk_uvc_device_brief_info_t"></a> <a id="bk_usb_uvc_get_param__bk_uvc_device_brief_info_tP"></a> <a id="uvc__uac__api__common_8h_1a00d2eab0579e1f86e26cad327cc19ffd"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_usb\_uvc\_get\_param([bk\_uvc\_device\_brief\_info\_t](../bk_usb.md#_CPPv426bk_uvc_device_brief_info_t "bk_uvc_device_brief_info_t") \*uvc\_device\_info)
:   Obtain UVC relate parameters.

    Including basic parameters,VID PID FORMAT FRAME EndPoint

    parameter: uvc\_device\_info uint16\_t vendor\_id; uint16\_t product\_id; [bk\_uvc\_format\_index](../bk_usb.md#structbk__uvc__format__index) format\_index; [bk\_uvc\_all\_frame](../bk_usb.md#structbk__uvc__all__frame) all\_frame; uint32\_t endpoints\_num; struct [s\_bk\_usb\_endpoint\_descriptor](../bk_usb.md#structs__bk__usb__endpoint__descriptor) \*ep\_desc;

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_usb_uvc_set_paramP15bk_uvc_config_t"></a>

<a id="_CPPv320bk_usb_uvc_set_paramP15bk_uvc_config_t"></a> <a id="_CPPv220bk_usb_uvc_set_paramP15bk_uvc_config_t"></a> <a id="bk_usb_uvc_set_param__bk_uvc_config_tP"></a> <a id="uvc__uac__api__common_8h_1aabc65b06a945c357495107e880019158"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_usb\_uvc\_set\_param([bk\_uvc\_config\_t](../bk_usb.md#_CPPv415bk_uvc_config_t "bk_uvc_config_t") \*uvc\_config)
:   Configure the basic parameters for starting UVC.

    Execute the command according to the configured parameters, please fill in the parameters correctly. Prevent parameter requirements that cannot be executed

    parameter: uvc\_config uint16\_t vendor\_id; uint16\_t product\_id; uint16\_t width; uint16\_t height; uint32\_t fps; uint16\_t frame\_index; uint16\_t format\_index; struct [s\_bk\_usb\_endpoint\_descriptor](../bk_usb.md#structs__bk__usb__endpoint__descriptor) \*ep\_desc;

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv439bk_usb_uvc_register_transfer_buffer_opsPv"></a>

<a id="_CPPv339bk_usb_uvc_register_transfer_buffer_opsPv"></a> <a id="_CPPv239bk_usb_uvc_register_transfer_buffer_opsPv"></a> <a id="bk_usb_uvc_register_transfer_buffer_ops__voidP"></a> <a id="uvc__uac__api__common_8h_1a8086f9309979f81dc8df85270c6332e6"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_usb\_uvc\_register\_transfer\_buffer\_ops(void \*ops)
:   Start UVC stream transmission.

    Execute the command according to the configured parameters, please fill in the parameters correctly. Prevent parameter requirements that cannot be executed

    This API means that the data needs to transfer and needs to be copied.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv412bk_uvc_startv"></a>

<a id="_CPPv312bk_uvc_startv"></a> <a id="_CPPv212bk_uvc_startv"></a> <a id="bk_uvc_start__void"></a> <a id="uvc__uac__api__common_8h_1a84fe3f0ca15f889270977ab9021ded0e"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uvc\_start(void)
:   Start UVC stream transmission.

    USB video camera data transfer starts:

    - configure the required configuration parameters
    - Send video stream data transfer instructions

    This API means that the data starts to transfer and needs to transfer and needs to be copied.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv417bk_uvc_dual_startv"></a>

<a id="_CPPv317bk_uvc_dual_startv"></a> <a id="_CPPv217bk_uvc_dual_startv"></a> <a id="bk_uvc_dual_start__void"></a> <a id="uvc__uac__api__common_8h_1afbd4b2749a8eb51da95a6d842b46b44e"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uvc\_dual\_start(void)

<a id="_CPPv411bk_uvc_stopv"></a>

<a id="_CPPv311bk_uvc_stopv"></a> <a id="_CPPv211bk_uvc_stopv"></a> <a id="bk_uvc_stop__void"></a> <a id="uvc__uac__api__common_8h_1a440843e8a51d700fe5567ab88e405b47"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uvc\_stop(void)
:   Stop UVC stream transmission.

    USB video camera data transfer stops:

    - Send the video stream data stop transmission command

    There will be no more data flow after execution.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv416bk_uvc_dual_stopv"></a>

<a id="_CPPv316bk_uvc_dual_stopv"></a> <a id="_CPPv216bk_uvc_dual_stopv"></a> <a id="bk_uvc_dual_stop__void"></a> <a id="uvc__uac__api__common_8h_1ad5d8126291356892be31b2335d598411"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uvc\_dual\_stop(void)

<a id="_CPPv434bk_usb_uvc_check_support_attribute8uint32_t"></a>

<a id="_CPPv334bk_usb_uvc_check_support_attribute8uint32_t"></a> <a id="_CPPv234bk_usb_uvc_check_support_attribute8uint32_t"></a> <a id="bk_usb_uvc_check_support_attribute__uint32_t"></a> <a id="uvc__uac__api__common_8h_1adea1a55cfcdcb4f959bc538823b5b658"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_usb\_uvc\_check\_support\_attribute(uint32\_t attribute)
:   Check whether the attribute configuration is supported.

    After connecting the UVC device, determine whether the attribute operation is supported by calling this API:

    - The Parameters has enumeration variable A planning, please fill in the attribute parameter correctly.
    - attribute: Processing Unit Control Selectors;

    Choose to call this API.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv423bk_usb_uvc_attribute_op18E_USB_ATTRIBUTE_OP8uint32_tP8uint32_t"></a>

<a id="_CPPv323bk_usb_uvc_attribute_op18E_USB_ATTRIBUTE_OP8uint32_tP8uint32_t"></a> <a id="_CPPv223bk_usb_uvc_attribute_op18E_USB_ATTRIBUTE_OP8uint32_tP8uint32_t"></a> <a id="bk_usb_uvc_attribute_op__E_USB_ATTRIBUTE_OP.uint32_t.uint32_tP"></a> <a id="uvc__uac__api__common_8h_1afcc5f60e653a93171e1fac1470d49243"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_usb\_uvc\_attribute\_op([E\_USB\_ATTRIBUTE\_OP](../bk_usb.md#_CPPv418E_USB_ATTRIBUTE_OP "E_USB_ATTRIBUTE_OP") ops, uint32\_t attribute, uint32\_t \*param)
:   Set camera attributes values.

    This API set/get camera attributes values:

    - Three parameters ops/attributes/values.
    - ops: E\_USB\_ATTRIBUTE\_OP
    - attributes: Processing Unit Control Selectors
    - param: Incoming parameter pointer

      example: Reference cli\_usb.c
    - Valid values needs to be viewed in camera.

    Choose to call this API.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv436bk_usb_uac_register_connect_callbackPv"></a>

<a id="_CPPv336bk_usb_uac_register_connect_callbackPv"></a> <a id="_CPPv236bk_usb_uac_register_connect_callbackPv"></a> <a id="bk_usb_uac_register_connect_callback__voidP"></a> <a id="uvc__uac__api__common_8h_1a28acc762aaac8635171526b4be4c8488"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_usb\_uac\_register\_connect\_callback(void \*param)
:   UAC connect the callback function registration function registration.

    This API disconnect the callback:

    - parameter is the registered callback function.
    - The callback function needs to be defined.

    Notify the registered callback function when the device is connected.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv439bk_usb_uac_register_disconnect_callbackPv"></a>

<a id="_CPPv339bk_usb_uac_register_disconnect_callbackPv"></a> <a id="_CPPv239bk_usb_uac_register_disconnect_callbackPv"></a> <a id="bk_usb_uac_register_disconnect_callback__voidP"></a> <a id="uvc__uac__api__common_8h_1ab85ad80a4e8d1522641ef3b5fa13a293"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_usb\_uac\_register\_disconnect\_callback(void \*param)
:   UAC disconnect the callback function registration function registration.

    This API disconnect the callback:

    - parameter is the registered callback function.
    - The callback function needs to be defined.

    Notify the registered callback function when the device is disconnected.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_usb_uac_get_paramP26bk_uac_device_brief_info_t"></a>

<a id="_CPPv320bk_usb_uac_get_paramP26bk_uac_device_brief_info_t"></a> <a id="_CPPv220bk_usb_uac_get_paramP26bk_uac_device_brief_info_t"></a> <a id="bk_usb_uac_get_param__bk_uac_device_brief_info_tP"></a> <a id="uvc__uac__api__common_8h_1a734e92573faea1756406895a2237cc5d"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_usb\_uac\_get\_param([bk\_uac\_device\_brief\_info\_t](../bk_usb.md#_CPPv426bk_uac_device_brief_info_t "bk_uac_device_brief_info_t") \*uac\_device\_info)
:   Obtain UAC relate parameters.

    Including basic parameters,VID PID mic\_samples\_frequence spk\_samples\_frequence

    parameter: uac\_device\_info uint16\_t vendor\_id; uint16\_t product\_id; uint16\_t mic\_format\_tag; uint8\_t mic\_samples\_frequence\_num; uint8\_t \*mic\_samples\_frequence; struct audio\_ep\_descriptor \*mic\_ep\_desc; uint16\_t spk\_format\_tag; uint8\_t spk\_samples\_frequence\_num; uint8\_t \*spk\_samples\_frequence; struct audio\_ep\_descriptor \*spk\_ep\_desc;

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_usb_uac_set_paramP15bk_uac_config_t"></a>

<a id="_CPPv320bk_usb_uac_set_paramP15bk_uac_config_t"></a> <a id="_CPPv220bk_usb_uac_set_paramP15bk_uac_config_t"></a> <a id="bk_usb_uac_set_param__bk_uac_config_tP"></a> <a id="uvc__uac__api__common_8h_1a55e7f891d32635a92cfbd8f703465795"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_usb\_uac\_set\_param([bk\_uac\_config\_t](../bk_usb.md#_CPPv415bk_uac_config_t "bk_uac_config_t") \*uac\_config)
:   Configure the basic parameters for starting UAC.

    Execute the command according to the configured parameters, please fill in the parameters correctly. Prevent parameter requirements that cannot be executed

    parameter: uac\_config uint16\_t vendor\_id; uint16\_t product\_id; uint16\_t mic\_format\_tag; uint32\_t mic\_samples\_frequence; struct audio\_ep\_descriptor \*mic\_ep\_desc; uint16\_t spk\_format\_tag; uint32\_t spk\_samples\_frequence; struct audio\_ep\_descriptor \*spk\_ep\_desc;

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_usb_uac_set_mic_paramP19bk_uac_mic_config_t"></a>

<a id="_CPPv324bk_usb_uac_set_mic_paramP19bk_uac_mic_config_t"></a> <a id="_CPPv224bk_usb_uac_set_mic_paramP19bk_uac_mic_config_t"></a> <a id="bk_usb_uac_set_mic_param__bk_uac_mic_config_tP"></a> <a id="uvc__uac__api__common_8h_1ad006c1f3429228ceb00760b9f0daa22d"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_usb\_uac\_set\_mic\_param([bk\_uac\_mic\_config\_t](../bk_usb.md#_CPPv419bk_uac_mic_config_t "bk_uac_mic_config_t") \*uac\_mic\_config)
:   Configure the basic parameters for starting Mic.

    Execute the command according to the configured parameters, please fill in the parameters correctly. Prevent parameter requirements that cannot be executed

    parameter: uac\_mic\_config uint16\_t mic\_format\_tag; uint32\_t mic\_samples\_frequence; struct audio\_ep\_descriptor \*mic\_ep\_desc;

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv424bk_usb_uac_set_spk_paramP19bk_uac_spk_config_t"></a>

<a id="_CPPv324bk_usb_uac_set_spk_paramP19bk_uac_spk_config_t"></a> <a id="_CPPv224bk_usb_uac_set_spk_paramP19bk_uac_spk_config_t"></a> <a id="bk_usb_uac_set_spk_param__bk_uac_spk_config_tP"></a> <a id="uvc__uac__api__common_8h_1addaffab59bc49c90bba04ab2bd3fcee8"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_usb\_uac\_set\_spk\_param([bk\_uac\_spk\_config\_t](../bk_usb.md#_CPPv419bk_uac_spk_config_t "bk_uac_spk_config_t") \*uac\_spk\_config)
:   Configure the basic parameters for starting Speaker.

    Execute the command according to the configured parameters, please fill in the parameters correctly. Prevent parameter requirements that cannot be executed

    parameter: uac\_spk\_config uint16\_t spk\_format\_tag; uint32\_t spk\_samples\_frequence; struct audio\_ep\_descriptor \*spk\_ep\_desc;

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv439bk_usb_uac_register_transfer_buffer_opsPv"></a>

<a id="_CPPv339bk_usb_uac_register_transfer_buffer_opsPv"></a> <a id="_CPPv239bk_usb_uac_register_transfer_buffer_opsPv"></a> <a id="bk_usb_uac_register_transfer_buffer_ops__voidP"></a> <a id="uvc__uac__api__common_8h_1aa6fa674aecacb786e182657f6bb01178"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_usb\_uac\_register\_transfer\_buffer\_ops(void \*ops)
:   Start UVC stream transmission.

    Execute the command according to the configured parameters, please fill in the parameters correctly. Prevent parameter requirements that cannot be executed

    This API means that the data needs to transfer and needs to be copied.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv416bk_uac_start_micv"></a>

<a id="_CPPv316bk_uac_start_micv"></a> <a id="_CPPv216bk_uac_start_micv"></a> <a id="bk_uac_start_mic__void"></a> <a id="uvc__uac__api__common_8h_1a6dac1e57d1d912da77c0f12c37973548"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uac\_start\_mic(void)
:   Start UAC mic stream transmission.

    USB audio data transfer starts:

    - configure the required configuration parameters
    - Send audio stream data transfer instructions

    This API means that the data starts to transfer and needs to transfer and needs to be copied.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv415bk_uac_stop_micv"></a>

<a id="_CPPv315bk_uac_stop_micv"></a> <a id="_CPPv215bk_uac_stop_micv"></a> <a id="bk_uac_stop_mic__void"></a> <a id="uvc__uac__api__common_8h_1ace4ce771362af2a02a37e7a40fac4fb5"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uac\_stop\_mic(void)
:   Stop UAC mic stream transmission.

    USB audio data transfer stops:

    - Send the video stream data stop transmission command

    There will be no more data flow after execution.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_uac_start_speakerv"></a>

<a id="_CPPv320bk_uac_start_speakerv"></a> <a id="_CPPv220bk_uac_start_speakerv"></a> <a id="bk_uac_start_speaker__void"></a> <a id="uvc__uac__api__common_8h_1aa8eb52ee1ca2a433760389237699089b"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uac\_start\_speaker(void)
:   Start UAC speaker stream transmission.

    USB audio data transfer starts:

    - configure the required configuration parameters
    - Send audio stream data transfer instructions

    This API means that the data starts to transfer and needs to transfer and needs to be copied.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv419bk_uac_stop_speakerv"></a>

<a id="_CPPv319bk_uac_stop_speakerv"></a> <a id="_CPPv219bk_uac_stop_speakerv"></a> <a id="bk_uac_stop_speaker__void"></a> <a id="uvc__uac__api__common_8h_1af3b50bb6a3d24f9709181f5c451b7bed"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_uac\_stop\_speaker(void)
:   Stop UAC speaker stream transmission.

    USB audio data transfer stops:

    - Send the video stream data stop transmission command

    There will be no more data flow after execution.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv434bk_usb_uac_check_support_attribute8uint32_t"></a>

<a id="_CPPv334bk_usb_uac_check_support_attribute8uint32_t"></a> <a id="_CPPv234bk_usb_uac_check_support_attribute8uint32_t"></a> <a id="bk_usb_uac_check_support_attribute__uint32_t"></a> <a id="uvc__uac__api__common_8h_1a3428f593872f903cf5204c7709c07bcc"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_usb\_uac\_check\_support\_attribute(uint32\_t attribute)
:   Check whether the attribute configuration is supported.

    After connecting the UAC device, determine whether the attribute operation is supported by calling this API:

    - The Parameters has enumeration variable A planning, please fill in the attribute parameter correctly.
    - attribute: Feature Unit Control Bits;

    Choose to call this API.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv423bk_usb_uac_attribute_op18E_USB_ATTRIBUTE_OP8uint32_tP8uint32_t"></a>

<a id="_CPPv323bk_usb_uac_attribute_op18E_USB_ATTRIBUTE_OP8uint32_tP8uint32_t"></a> <a id="_CPPv223bk_usb_uac_attribute_op18E_USB_ATTRIBUTE_OP8uint32_tP8uint32_t"></a> <a id="bk_usb_uac_attribute_op__E_USB_ATTRIBUTE_OP.uint32_t.uint32_tP"></a> <a id="uvc__uac__api__common_8h_1a1e2c4ecee3e9b5ccf714d27a33d0d3f5"></a> [bk\_err\_t](../../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_usb\_uac\_attribute\_op([E\_USB\_ATTRIBUTE\_OP](../bk_usb.md#_CPPv418E_USB_ATTRIBUTE_OP "E_USB_ATTRIBUTE_OP") ops, uint32\_t attribute, uint32\_t \*param)
:   Set camera attributes values.

    This API set/get camera attributes values:

    - Three parameters ops/attributes/values.
    - ops: E\_USB\_ATTRIBUTE\_OP
    - attributes: Feature Unit Control Bits
    - param: Incoming parameter pointer

      example: Reference cli\_usb.c
    - Valid values needs to be viewed in camera.

    Choose to call this API.

    返回
    :   - BK\_OK: succeed
        - others: other errors.
