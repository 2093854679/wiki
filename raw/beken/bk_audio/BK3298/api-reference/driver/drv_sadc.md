---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_sadc.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-sadc"></a>

# DRV\_SADC

<a id="drv-sadc-api-status"></a>

## DRV\_SADC API Status

| API |
| --- |
| [`drv_sadc_init()`](#_CPPv413drv_sadc_init8uint32_t "drv_sadc_init") |
| [`drv_sadc_deinit()`](#_CPPv415drv_sadc_deinit8uint32_t "drv_sadc_deinit") |
| [`drv_sadc_reg_callback()`](#_CPPv421drv_sadc_reg_callback8uint32_t15pfunc_sadc_cb_t "drv_sadc_reg_callback") |
| [`drv_sadc_cfg_channel_div()`](#_CPPv424drv_sadc_cfg_channel_div8uint32_t7uint8_t8uint32_t7uint8_t "drv_sadc_cfg_channel_div") |
| [`drv_sadc_cfg_samp_param()`](#_CPPv423drv_sadc_cfg_samp_param8uint32_t7uint8_t7uint8_t7uint8_t "drv_sadc_cfg_samp_param") |
| [`drv_sadc_cfg_samp_param2()`](#_CPPv424drv_sadc_cfg_samp_param28uint32_t7uint8_t7uint8_t "drv_sadc_cfg_samp_param2") |
| [`drv_sadc_start()`](#_CPPv414drv_sadc_start8uint32_t8uint32_t "drv_sadc_start") |
| [`drv_sadc_get_data()`](#_CPPv417drv_sadc_get_data8uint32_t "drv_sadc_get_data") |
| [`drv_sadc_stop()`](#_CPPv413drv_sadc_stop8uint32_t "drv_sadc_stop") |

<a id="drv-sadc-pin-and-gpio-map"></a>

## DRV\_SADC Pin and GPIO Map

<a id="drv-sadc-api-reference"></a>

## DRV\_SADC API Reference

<a id="header-file"></a>

### Header File

- [driver/sadc/drv\_sadc.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/sadc/drv_sadc.h)

<a id="functions"></a>

### Functions

<a id="_CPPv413drv_sadc_init8uint32_t"></a>

<a id="_CPPv313drv_sadc_init8uint32_t"></a> <a id="_CPPv213drv_sadc_init8uint32_t"></a> <a id="drv_sadc_init__uint32_t"></a> <a id="drv__sadc_8h_1adf9ffedbe892479e5476057c0acf2acc"></a> uint32\_t drv\_sadc\_init(uint32\_t dev\_index)
:   init a sadc device.

    初始化sadc设备，在使用sadc功能前需要调用它获取device instance

    参数:
    :   **dev\_index** – **\[in\]** device index, start with 0

    返回值:
    :   - **0** – fail
        - **other** – success

    返回:
    :   device instance

<a id="_CPPv415drv_sadc_deinit8uint32_t"></a>

<a id="_CPPv315drv_sadc_deinit8uint32_t"></a> <a id="_CPPv215drv_sadc_deinit8uint32_t"></a> <a id="drv_sadc_deinit__uint32_t"></a> <a id="drv__sadc_8h_1a11be695e07f2fb479d89bfb2d64f9a42"></a> int32\_t drv\_sadc\_deinit(uint32\_t dev\_instance)
:   deinit a sadc device.

    反初始化sadc设备，对drv\_sadc\_device\_init()进行反向操作

    参数:
    :   **dev\_instance** – **\[in\]** return value of drv\_sadc\_device\_init()

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421drv_sadc_reg_callback8uint32_t15pfunc_sadc_cb_t"></a>

<a id="_CPPv321drv_sadc_reg_callback8uint32_t15pfunc_sadc_cb_t"></a> <a id="_CPPv221drv_sadc_reg_callback8uint32_t15pfunc_sadc_cb_t"></a> <a id="drv_sadc_reg_callback__uint32_t.pfunc_sadc_cb_t"></a> <a id="drv__sadc_8h_1a11d58cc05131ed0e13e5c6de83eaf19d"></a> int32\_t drv\_sadc\_reg\_callback(uint32\_t dev\_instance, [pfunc\_sadc\_cb\_t](#_CPPv415pfunc_sadc_cb_t "pfunc_sadc_cb_t") pfn\_cb)
:   register user callback.

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_sadc\_device\_init()
        - **pfn\_cb** – **\[in\]** user callback

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424drv_sadc_cfg_channel_div8uint32_t7uint8_t8uint32_t7uint8_t"></a>

<a id="_CPPv324drv_sadc_cfg_channel_div8uint32_t7uint8_t8uint32_t7uint8_t"></a> <a id="_CPPv224drv_sadc_cfg_channel_div8uint32_t7uint8_t8uint32_t7uint8_t"></a> <a id="drv_sadc_cfg_channel_div__uint32_t.uint8_t.uint32_t.uint8_t"></a> <a id="drv__sadc_8h_1a357da788e8a5210160a01f4d9421ded3"></a> int32\_t drv\_sadc\_cfg\_channel\_div(uint32\_t dev\_instance, uint8\_t channel, uint32\_t div, uint8\_t sample\_interval\_plus\_12)
:   config sadc channel \& clock.

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_sadc\_device\_init()
        - **channel** – **\[in\]** 具体从哪个通道进行数据采样, 0\~12
        - **div** – **\[in\]** 分频参数，最大256
        - **sample\_interval\_plus\_12** – **\[in\]** 采样间隔，0:12个clock采样一次 1:13个clock采样一次 。。。

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv423drv_sadc_cfg_samp_param8uint32_t7uint8_t7uint8_t7uint8_t"></a>

<a id="_CPPv323drv_sadc_cfg_samp_param8uint32_t7uint8_t7uint8_t7uint8_t"></a> <a id="_CPPv223drv_sadc_cfg_samp_param8uint32_t7uint8_t7uint8_t7uint8_t"></a> <a id="drv_sadc_cfg_samp_param__uint32_t.uint8_t.uint8_t.uint8_t"></a> <a id="drv__sadc_8h_1ab0a339c35769c4ec24f9d722895687e8"></a> int32\_t drv\_sadc\_cfg\_samp\_param(uint32\_t dev\_instance, uint8\_t drop\_cnt, uint8\_t sum\_cnt, uint8\_t out\_cnt)
:   配置sadc channel的其他参数，平均后再写入fifo.

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_sadc\_device\_init()
        - **drop\_cnt** – **\[in\]** 采样后先丢掉drop个数据，最大15个
        - **sum\_cnt** – **\[in\]** 平均多少个数据,求平均出一个数据(1/2/4/8/16)
        - **out\_cnt** – **\[in\]** 多少个数据触发中断由用户callback读取, \< 32\=fifo depth

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424drv_sadc_cfg_samp_param28uint32_t7uint8_t7uint8_t"></a>

<a id="_CPPv324drv_sadc_cfg_samp_param28uint32_t7uint8_t7uint8_t"></a> <a id="_CPPv224drv_sadc_cfg_samp_param28uint32_t7uint8_t7uint8_t"></a> <a id="drv_sadc_cfg_samp_param2__uint32_t.uint8_t.uint8_t"></a> <a id="drv__sadc_8h_1a6699a8594572aa185349fb3960fd46c7"></a> int32\_t drv\_sadc\_cfg\_samp\_param2(uint32\_t dev\_instance, uint8\_t drop\_cnt, uint8\_t fifo\_level)
:   配置sadc channel的其他参数，使用fifo的中断.

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_sadc\_device\_init()
        - **drop\_cnt** – **\[in\]** 采样后先丢掉drop个数据，最大15个
        - **fifo\_level** – **\[in\]** fifo 中断的level配置 0 \~ 31

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv414drv_sadc_start8uint32_t8uint32_t"></a>

<a id="_CPPv314drv_sadc_start8uint32_t8uint32_t"></a> <a id="_CPPv214drv_sadc_start8uint32_t8uint32_t"></a> <a id="drv_sadc_start__uint32_t.uint32_t"></a> <a id="drv__sadc_8h_1a9d556938484322e43f040eb4f26cd1cf"></a> int32\_t drv\_sadc\_start(uint32\_t dev\_instance, uint32\_t vref\_sel)
:   start sadc, start to sample.

    参数:
    :   - **dev\_instance** – **\[in\]** return value of drv\_sadc\_device\_init()
        - **vref\_sel** – **\[in\]** 0: 绝对电压 1:gpio测试相对电压(0\~Vsys)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv417drv_sadc_get_data8uint32_t"></a>

<a id="_CPPv317drv_sadc_get_data8uint32_t"></a> <a id="_CPPv217drv_sadc_get_data8uint32_t"></a> <a id="drv_sadc_get_data__uint32_t"></a> <a id="drv__sadc_8h_1afe509ac711ac2625282942344e4c5d77"></a> uint16\_t drv\_sadc\_get\_data(uint32\_t dev\_instance)
:   get sample data from sadc FIFO.

    参数:
    :   **dev\_instance** – **\[in\]** return value of drv\_sadc\_device\_init()

    返回:
    :   sample data(16bit)

<a id="_CPPv413drv_sadc_stop8uint32_t"></a>

<a id="_CPPv313drv_sadc_stop8uint32_t"></a> <a id="_CPPv213drv_sadc_stop8uint32_t"></a> <a id="drv_sadc_stop__uint32_t"></a> <a id="drv__sadc_8h_1a94716fb0787720ab508c1d5326e3c671"></a> int32\_t drv\_sadc\_stop(uint32\_t dev\_instance)
:   force stop sadc.

    一般情况下不会调用到该接口

    参数:
    :   **dev\_instance** – **\[in\]** return value of drv\_sadc\_device\_init()

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv415pfunc_sadc_cb_t"></a>

<a id="_CPPv315pfunc_sadc_cb_t"></a> <a id="_CPPv215pfunc_sadc_cb_t"></a> <a id="pfunc_sadc_cb_t"></a> <a id="drv__sadc_8h_1a4d03baddc859d87ca5c69193aafc9e20"></a> typedef void (\*pfunc\_sadc\_cb\_t)(uint32\_t dev\_instance, uint8\_t channel, uint8\_t data\_cnt)
