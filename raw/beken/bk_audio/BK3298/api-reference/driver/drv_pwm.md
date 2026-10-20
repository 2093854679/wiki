---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_pwm.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-pwm"></a>

# DRV\_PWM

<a id="drv-pwm-api-status"></a>

## DRV\_PWM API Status

| API |
| --- |
| [`drv_pwm_init()`](#_CPPv412drv_pwm_init8uint32_t17drv_pwm_src_clk_e "drv_pwm_init") |
| [`drv_pwm_deinit()`](#_CPPv414drv_pwm_deinit8uint32_t "drv_pwm_deinit") |
| [`drv_pwm_sel_channel_mode()`](#_CPPv424drv_pwm_sel_channel_mode8uint32_t8uint32_t14drv_pwm_mode_e7uint8_t "drv_pwm_sel_channel_mode") |
| [`drv_pwm_breath_config()`](#_CPPv421drv_pwm_breath_config8uint32_t8uint32_tP22drv_pwm_breath_param_t "drv_pwm_breath_config") |
| [`drv_pwm_breath_sel_output()`](#_CPPv425drv_pwm_breath_sel_output8uint32_t8uint32_t20drv_pwm_breath_out_eb "drv_pwm_breath_sel_output") |
| [`drv_pwm_breath_reg_callback()`](#_CPPv427drv_pwm_breath_reg_callback8uint32_t8uint32_t20drv_pwm_breath_irq_e8uint16_tb21pfunc_pwm_breath_cb_tPv "drv_pwm_breath_reg_callback") |
| [`drv_pwm_out_pwm_config()`](#_CPPv422drv_pwm_out_pwm_config8uint32_t8uint32_tP22drv_pwm_output_param_t "drv_pwm_out_pwm_config") |
| [`drv_pwm_capture_config()`](#_CPPv422drv_pwm_capture_config8uint32_t8uint32_tP23drv_pwm_capture_param_t "drv_pwm_capture_config") |
| [`drv_pwm_capture_get_value()`](#_CPPv425drv_pwm_capture_get_value8uint32_t8uint32_t "drv_pwm_capture_get_value") |
| [`drv_pwm_reg_irq_callback()`](#_CPPv424drv_pwm_reg_irq_callback8uint32_t8uint32_t14pfunc_pwm_cb_tPv "drv_pwm_reg_irq_callback") |
| [`drv_pwm_enable_channel()`](#_CPPv422drv_pwm_enable_channel8uint32_t8uint32_tb "drv_pwm_enable_channel") |

<a id="drv-i2c-unit-number"></a>

## DRV\_I2C UNIT Number

| Capability | Number |
| --- | --- |
| UNIT Number | 11 |

<a id="drv-pwm-pin-and-gpio-map"></a>

## DRV\_PWM Pin and GPIO Map

| SPI Pin | Number |
| --- | --- |
| PWM0 | 13 |

<a id="drv-pwm-api-reference"></a>

## DRV\_PWM API Reference

<a id="header-file"></a>

### Header File

- [driver/pwm/drv\_pwm.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/pwm/drv_pwm.h)

<a id="functions"></a>

### Functions

<a id="_CPPv412drv_pwm_init8uint32_t17drv_pwm_src_clk_e"></a>

<a id="_CPPv312drv_pwm_init8uint32_t17drv_pwm_src_clk_e"></a> <a id="_CPPv212drv_pwm_init8uint32_t17drv_pwm_src_clk_e"></a> <a id="drv_pwm_init__uint32_t.drv_pwm_src_clk_e"></a> <a id="drv__pwm_8h_1aa08aa726c7ed671fa095495da137c977"></a> uint32\_t drv\_pwm\_init(uint32\_t dev\_index, [drv\_pwm\_src\_clk\_e](#_CPPv417drv_pwm_src_clk_e "drv_pwm_src_clk_e") e\_clk\_src)
:   init a PWM device.

    初始化PWM设备. 调用其他pwm函数前需要初始化设备并获取device instance

    参数:
    :   - **dev\_index** – **\[in\]** device index, from 0(the first device), \< [PWM\_DEVICE\_NUM](#drv__pwm_8h_1aacb9be334d25767ce787ff2d41e3da17)
        - **e\_clk\_src** – **\[in\]** pwm device source clock (32k or 26M)

    返回值:
    :   - **0** – fail
        - **other** – success

    返回:
    :   device instance

<a id="_CPPv414drv_pwm_deinit8uint32_t"></a>

<a id="_CPPv314drv_pwm_deinit8uint32_t"></a> <a id="_CPPv214drv_pwm_deinit8uint32_t"></a> <a id="drv_pwm_deinit__uint32_t"></a> <a id="drv__pwm_8h_1a065158d9a110320ed0f42b8f01ae57fb"></a> int32\_t drv\_pwm\_deinit(uint32\_t dev\_instance)
:   deinit a PWM device.

    反初始化PWM设备。是drv\_pwm\_init()的反向操作。所有channel都没有使用的时候该函数才会返回成功

    参数:
    :   **dev\_instance** – **\[in\]** return value of [drv\_pwm\_init()](#drv__pwm_8h_1aa08aa726c7ed671fa095495da137c977)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424drv_pwm_sel_channel_mode8uint32_t8uint32_t14drv_pwm_mode_e7uint8_t"></a>

<a id="_CPPv324drv_pwm_sel_channel_mode8uint32_t8uint32_t14drv_pwm_mode_e7uint8_t"></a> <a id="_CPPv224drv_pwm_sel_channel_mode8uint32_t8uint32_t14drv_pwm_mode_e7uint8_t"></a> <a id="drv_pwm_sel_channel_mode__uint32_t.uint32_t.drv_pwm_mode_e.uint8_t"></a> <a id="drv__pwm_8h_1a59410420374d3bc1695499addc934b39"></a> int32\_t drv\_pwm\_sel\_channel\_mode(uint32\_t dev\_instance, uint32\_t chn\_index, [drv\_pwm\_mode\_e](#_CPPv414drv_pwm_mode_e "drv_pwm_mode_e") e\_mode, uint8\_t pre\_div\_val)
:   config channel work mode.

    每个channel都有3种工作模式: 呼吸灯、 pwm输出、 输入捕获模式 PWM 呼吸灯模式会有最高的优先级，即它工作的时候，pwm输出模式和输入捕获模式都不会生效 PWM 呼吸灯使用第1个timer(分频会生效)，channel是第2个channel （其他channel无此功能） timer0 channel\_1 PWM输出模式时： 配置 channel 0时会把channel 1的输出和它同时（反向）输出 配置 channel 2时会把channel 3的输出和它同时（反向）输出 配置 channel 4时会把channel 5的输出和它同时（反向）输出 但是，用户也可以单独配置 channel 1 3 5，不过它的限制是只有1个比较值

    输入捕获模式时： 3个 timer 对应 3个channel timer0 –\> channel 0 timer1 –\> channel 2 timer2 –\> channel 4

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_pwm\_init()](#drv__pwm_8h_1aa08aa726c7ed671fa095495da137c977)
        - **chn\_index** – **\[in\]** channel index (0 \~ 5\)
        - **e\_mode** – **\[in\]** work mode for this channel (e\_mode \= DRV\_PWM\_MODE\_RESET\_NULL时会复位该值到默认)
        - **pre\_div\_val** – **\[in\]** 该channel对应的timer的预分频值 0 \~ 255

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421drv_pwm_breath_config8uint32_t8uint32_tP22drv_pwm_breath_param_t"></a>

<a id="_CPPv321drv_pwm_breath_config8uint32_t8uint32_tP22drv_pwm_breath_param_t"></a> <a id="_CPPv221drv_pwm_breath_config8uint32_t8uint32_tP22drv_pwm_breath_param_t"></a> <a id="drv_pwm_breath_config__uint32_t.uint32_t.drv_pwm_breath_param_tP"></a> <a id="drv__pwm_8h_1ab19e7a9d66e92c55a12c43f5e4097c60"></a> int32\_t drv\_pwm\_breath\_config(uint32\_t dev\_instance, uint32\_t chn\_index, [drv\_pwm\_breath\_param\_t](#_CPPv422drv_pwm_breath_param_t "drv_pwm_breath_param_t") \*pt\_breath\_param)
:   config paramter in breath light mode.

    呼吸灯模式时用来配置channel的参数的

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_pwm\_init()](#drv__pwm_8h_1aa08aa726c7ed671fa095495da137c977)
        - **chn\_index** – **\[in\]** channel index (0 \~ 5\)
        - **pt\_breath\_param** – **\[in\]** 指向呼吸灯模式的参数的结构体指针

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425drv_pwm_breath_sel_output8uint32_t8uint32_t20drv_pwm_breath_out_eb"></a>

<a id="_CPPv325drv_pwm_breath_sel_output8uint32_t8uint32_t20drv_pwm_breath_out_eb"></a> <a id="_CPPv225drv_pwm_breath_sel_output8uint32_t8uint32_t20drv_pwm_breath_out_eb"></a> <a id="drv_pwm_breath_sel_output__uint32_t.uint32_t.drv_pwm_breath_out_e.b"></a> <a id="drv__pwm_8h_1a4c1692b35a6bd4d53fed332a9a8e8fb8"></a> int32\_t drv\_pwm\_breath\_sel\_output(uint32\_t dev\_instance, uint32\_t chn\_index, [drv\_pwm\_breath\_out\_e](#_CPPv420drv_pwm_breath_out_e "drv_pwm_breath_out_e") e\_output, bool output\_reverse)
:   output control in breath light mode.

    呼吸灯模式时的输出控制

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_pwm\_init()](#drv__pwm_8h_1aa08aa726c7ed671fa095495da137c977)
        - **chn\_index** – **\[in\]** channel index (0 \~ 5\)
        - **e\_output** – **\[in\]** see drv\_pwm\_breath\_out\_e
        - **output\_reverse** – **\[in\]** 输出反向控制

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427drv_pwm_breath_reg_callback8uint32_t8uint32_t20drv_pwm_breath_irq_e8uint16_tb21pfunc_pwm_breath_cb_tPv"></a>

<a id="_CPPv327drv_pwm_breath_reg_callback8uint32_t8uint32_t20drv_pwm_breath_irq_e8uint16_tb21pfunc_pwm_breath_cb_tPv"></a> <a id="_CPPv227drv_pwm_breath_reg_callback8uint32_t8uint32_t20drv_pwm_breath_irq_e8uint16_tb21pfunc_pwm_breath_cb_tPv"></a> <a id="drv_pwm_breath_reg_callback__uint32_t.uint32_t.drv_pwm_breath_irq_e.uint16_t.b.pfunc_pwm_breath_cb_t.voidP"></a> <a id="drv__pwm_8h_1a5e4306e053522f0b5fe5aa1fee3ea339"></a> int32\_t drv\_pwm\_breath\_reg\_callback(uint32\_t dev\_instance, uint32\_t chn\_index, [drv\_pwm\_breath\_irq\_e](#_CPPv420drv_pwm_breath_irq_e "drv_pwm_breath_irq_e") e\_irq, uint16\_t irq\_pos, bool enable, [pfunc\_pwm\_breath\_cb\_t](#_CPPv421pfunc_pwm_breath_cb_t "pfunc_pwm_breath_cb_t") pfn\_cb, void \*pv\_cb\_arg)
:   注册呼吸灯的长亮/长灭时的中断

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_pwm\_init()](#drv__pwm_8h_1aa08aa726c7ed671fa095495da137c977)
        - **chn\_index** – **\[in\]** 1 is the breath channel
        - **e\_irq** – **\[in\]** see drv\_pwm\_breath\_irq\_e
        - **irq\_pos** – **\[in\]** 在第几个步进时产生中断
        - **enable** – **\[in\]** true: enable false: disable
        - **pfn\_cb** – **\[in\]** 对应的callback
        - **pv\_cb\_arg** – **\[in\]** 对应的callback 参数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422drv_pwm_out_pwm_config8uint32_t8uint32_tP22drv_pwm_output_param_t"></a>

<a id="_CPPv322drv_pwm_out_pwm_config8uint32_t8uint32_tP22drv_pwm_output_param_t"></a> <a id="_CPPv222drv_pwm_out_pwm_config8uint32_t8uint32_tP22drv_pwm_output_param_t"></a> <a id="drv_pwm_out_pwm_config__uint32_t.uint32_t.drv_pwm_output_param_tP"></a> <a id="drv__pwm_8h_1a14d243aac3d03489eec13bd95594022d"></a> int32\_t drv\_pwm\_out\_pwm\_config(uint32\_t dev\_instance, uint32\_t chn\_index, [drv\_pwm\_output\_param\_t](#_CPPv422drv_pwm_output_param_t "drv_pwm_output_param_t") \*pt\_out\_param)
:   config paramter in PWM output mode.

    PWM输出模式时用来配置channel的参数的 配置 channel 0时会把channel 1的输出和它同时（反向）输出 配置 channel 2时会把channel 3的输出和它同时（反向）输出 配置 channel 4时会把channel 5的输出和它同时（反向）输出 但是，用户也可以单独配置 channel 1 3 5，不过它的限制是只有1个比较值 即只有 cmp1\_value 这个值是有效的，其他两个比较值无效

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_pwm\_init()](#drv__pwm_8h_1aa08aa726c7ed671fa095495da137c977)
        - **chn\_index** – **\[in\]** channel index (0 \~ 5\)
        - **pt\_out\_param** – **\[in\]** 指向PWM输出模式的参数的结构体指针

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422drv_pwm_capture_config8uint32_t8uint32_tP23drv_pwm_capture_param_t"></a>

<a id="_CPPv322drv_pwm_capture_config8uint32_t8uint32_tP23drv_pwm_capture_param_t"></a> <a id="_CPPv222drv_pwm_capture_config8uint32_t8uint32_tP23drv_pwm_capture_param_t"></a> <a id="drv_pwm_capture_config__uint32_t.uint32_t.drv_pwm_capture_param_tP"></a> <a id="drv__pwm_8h_1ad4f8fa74c878258a129f5945446c59ac"></a> int32\_t drv\_pwm\_capture\_config(uint32\_t dev\_instance, uint32\_t chn\_index, [drv\_pwm\_capture\_param\_t](#_CPPv423drv_pwm_capture_param_t "drv_pwm_capture_param_t") \*pt\_capture\_param)
:   config paramter in input capture mode.

    输入捕获模式时用来配置channel的参数的, 注意，只有0/2/4 channel可以拿来做capture

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_pwm\_init()](#drv__pwm_8h_1aa08aa726c7ed671fa095495da137c977)
        - **chn\_index** – **\[in\]** channel index (0 2 4\)
        - **pt\_capture\_param** – **\[in\]** 指向输入捕获模式的参数的结构体指针

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425drv_pwm_capture_get_value8uint32_t8uint32_t"></a>

<a id="_CPPv325drv_pwm_capture_get_value8uint32_t8uint32_t"></a> <a id="_CPPv225drv_pwm_capture_get_value8uint32_t8uint32_t"></a> <a id="drv_pwm_capture_get_value__uint32_t.uint32_t"></a> <a id="drv__pwm_8h_1a273a1101d42866384a93a6eb6b156d4e"></a> uint32\_t drv\_pwm\_capture\_get\_value(uint32\_t dev\_instance, uint32\_t chn\_index)
:   get capture value.

    用在中断里面获取对应channel捕获的值

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_pwm\_init()](#drv__pwm_8h_1aa08aa726c7ed671fa095495da137c977)
        - **chn\_index** – **\[in\]** channel index (0 2 4\)

    返回:
    :   capture value

<a id="_CPPv424drv_pwm_reg_irq_callback8uint32_t8uint32_t14pfunc_pwm_cb_tPv"></a>

<a id="_CPPv324drv_pwm_reg_irq_callback8uint32_t8uint32_t14pfunc_pwm_cb_tPv"></a> <a id="_CPPv224drv_pwm_reg_irq_callback8uint32_t8uint32_t14pfunc_pwm_cb_tPv"></a> <a id="drv_pwm_reg_irq_callback__uint32_t.uint32_t.pfunc_pwm_cb_t.voidP"></a> <a id="drv__pwm_8h_1a54c04f90074d258de2c2376d10084779"></a> int32\_t drv\_pwm\_reg\_irq\_callback(uint32\_t dev\_instance, uint32\_t chn\_index, [pfunc\_pwm\_cb\_t](#_CPPv414pfunc_pwm_cb_t "pfunc_pwm_cb_t") pfn\_cb, void \*pv\_cb\_arg)
:   register callback for a channel.

    公共函数，3种模式都需要用到. pfn\_cb\=NULL 会禁用中断

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_pwm\_init()](#drv__pwm_8h_1aa08aa726c7ed671fa095495da137c977)
        - **chn\_index** – **\[in\]** channel index (0 \~ 5\)
        - **pfn\_cb** – **\[in\]** callback for this channel, diable interrupt if pfn\_cb\=NULL
        - **pv\_cb\_arg** – **\[in\]** callback argument

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422drv_pwm_enable_channel8uint32_t8uint32_tb"></a>

<a id="_CPPv322drv_pwm_enable_channel8uint32_t8uint32_tb"></a> <a id="_CPPv222drv_pwm_enable_channel8uint32_t8uint32_tb"></a> <a id="drv_pwm_enable_channel__uint32_t.uint32_t.b"></a> <a id="drv__pwm_8h_1af7ce78474b84f35ebaca0bde14b41d85"></a> int32\_t drv\_pwm\_enable\_channel(uint32\_t dev\_instance, uint32\_t chn\_index, bool enable)
:   enable or disable channel.

    公共函数，3种模式都需要用到

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_pwm\_init()](#drv__pwm_8h_1aa08aa726c7ed671fa095495da137c977)
        - **chn\_index** – **\[in\]** channel index (0 \~ 5\)
        - **enable** – **\[in\]** true:enable false:disable

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv423_drv_pwm_breath_param_t"></a>

<a id="_CPPv323_drv_pwm_breath_param_t"></a> <a id="_CPPv223_drv_pwm_breath_param_t"></a> <a id="_drv_pwm_breath_param_t"></a> <a id="struct__drv__pwm__breath__param__t"></a> struct \_drv\_pwm\_breath\_param\_t

<a id="_CPPv423_drv_pwm_output_param_t"></a>

<a id="_CPPv323_drv_pwm_output_param_t"></a> <a id="_CPPv223_drv_pwm_output_param_t"></a> <a id="_drv_pwm_output_param_t"></a> <a id="struct__drv__pwm__output__param__t"></a> struct \_drv\_pwm\_output\_param\_t

<a id="_CPPv424_drv_pwm_capture_param_t"></a>

<a id="_CPPv324_drv_pwm_capture_param_t"></a> <a id="_CPPv224_drv_pwm_capture_param_t"></a> <a id="_drv_pwm_capture_param_t"></a> <a id="struct__drv__pwm__capture__param__t"></a> struct \_drv\_pwm\_capture\_param\_t

<a id="macros"></a>

### Macros

<a id="c.PWM_DEVICE_NUM"></a>

<a id="drv__pwm_8h_1aacb9be334d25767ce787ff2d41e3da17"></a> PWM\_DEVICE\_NUM
:   PWM device number.

<a id="c.PWM_CHANNEL_NUM"></a>

<a id="drv__pwm_8h_1aa8de5932e202da33005841edc021a2e4"></a> PWM\_CHANNEL\_NUM

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv417drv_pwm_src_clk_e"></a>

<a id="_CPPv317drv_pwm_src_clk_e"></a> <a id="_CPPv217drv_pwm_src_clk_e"></a> <a id="drv_pwm_src_clk_e"></a> <a id="drv__pwm_8h_1a3c96efdac6dd837148207140a523b07f"></a> typedef enum [\_drv\_pwm\_src\_clk\_e](#_CPPv418_drv_pwm_src_clk_e "_drv_pwm_src_clk_e") drv\_pwm\_src\_clk\_e
:   PWM source clock.

<a id="_CPPv414drv_pwm_mode_e"></a>

<a id="_CPPv314drv_pwm_mode_e"></a> <a id="_CPPv214drv_pwm_mode_e"></a> <a id="drv_pwm_mode_e"></a> <a id="drv__pwm_8h_1a785b72f605cb8cddc78bcebb9c64c560"></a> typedef enum [\_drv\_pwm\_mode\_e](#_CPPv415_drv_pwm_mode_e "_drv_pwm_mode_e") drv\_pwm\_mode\_e
:   PWM work mode channel\_0\~5 support DRV\_PWM\_MODE\_OUT\_PWM \& DRV\_PWM\_MODE\_IN\_CAPTURE channel\_1 support DRV\_PWM\_MODE\_BREATH too.

<a id="_CPPv420drv_pwm_breath_irq_e"></a>

<a id="_CPPv320drv_pwm_breath_irq_e"></a> <a id="_CPPv220drv_pwm_breath_irq_e"></a> <a id="drv_pwm_breath_irq_e"></a> <a id="drv__pwm_8h_1a491bdf505406144ef2559b114c19279f"></a> typedef enum [\_drv\_pwm\_breath\_irq\_e](#_CPPv421_drv_pwm_breath_irq_e "_drv_pwm_breath_irq_e") drv\_pwm\_breath\_irq\_e

<a id="_CPPv422drv_pwm_breath_param_t"></a>

<a id="_CPPv322drv_pwm_breath_param_t"></a> <a id="_CPPv222drv_pwm_breath_param_t"></a> <a id="drv_pwm_breath_param_t"></a> <a id="drv__pwm_8h_1aaeec7277de7f7d29fc0aaba32c5db04a"></a> typedef struct [\_drv\_pwm\_breath\_param\_t](#_CPPv423_drv_pwm_breath_param_t "_drv_pwm_breath_param_t") drv\_pwm\_breath\_param\_t

<a id="_CPPv420drv_pwm_breath_out_e"></a>

<a id="_CPPv320drv_pwm_breath_out_e"></a> <a id="_CPPv220drv_pwm_breath_out_e"></a> <a id="drv_pwm_breath_out_e"></a> <a id="drv__pwm_8h_1a2c60d20d91dae2068659354b983a3c95"></a> typedef enum [\_drv\_pwm\_breath\_out\_e](#_CPPv421_drv_pwm_breath_out_e "_drv_pwm_breath_out_e") drv\_pwm\_breath\_out\_e

<a id="_CPPv421drv_pwm_output_mode_e"></a>

<a id="_CPPv321drv_pwm_output_mode_e"></a> <a id="_CPPv221drv_pwm_output_mode_e"></a> <a id="drv_pwm_output_mode_e"></a> <a id="drv__pwm_8h_1a02196a5bbd790818634c8b00de994cd9"></a> typedef enum [\_drv\_pwm\_output\_mode\_e](#_CPPv422_drv_pwm_output_mode_e "_drv_pwm_output_mode_e") drv\_pwm\_output\_mode\_e

<a id="_CPPv422drv_pwm_output_count_e"></a>

<a id="_CPPv322drv_pwm_output_count_e"></a> <a id="_CPPv222drv_pwm_output_count_e"></a> <a id="drv_pwm_output_count_e"></a> <a id="drv__pwm_8h_1aa2eae42db59f799f7073eb668f1a0d9d"></a> typedef enum [\_drv\_pwm\_output\_count\_e](#_CPPv423_drv_pwm_output_count_e "_drv_pwm_output_count_e") drv\_pwm\_output\_count\_e

<a id="_CPPv422drv_pwm_output_param_t"></a>

<a id="_CPPv322drv_pwm_output_param_t"></a> <a id="_CPPv222drv_pwm_output_param_t"></a> <a id="drv_pwm_output_param_t"></a> <a id="drv__pwm_8h_1a1468ef1e38e20d13bd0485a4afe331e4"></a> typedef struct [\_drv\_pwm\_output\_param\_t](#_CPPv423_drv_pwm_output_param_t "_drv_pwm_output_param_t") drv\_pwm\_output\_param\_t

<a id="_CPPv420drv_pwm_slave_mode_e"></a>

<a id="_CPPv320drv_pwm_slave_mode_e"></a> <a id="_CPPv220drv_pwm_slave_mode_e"></a> <a id="drv_pwm_slave_mode_e"></a> <a id="drv__pwm_8h_1afa3434fce1f0208dae6ac9e2f6fd8cc6"></a> typedef enum [\_drv\_pwm\_slave\_mode\_e](#_CPPv421_drv_pwm_slave_mode_e "_drv_pwm_slave_mode_e") drv\_pwm\_slave\_mode\_e

<a id="_CPPv420drv_pwm_trig_input_e"></a>

<a id="_CPPv320drv_pwm_trig_input_e"></a> <a id="_CPPv220drv_pwm_trig_input_e"></a> <a id="drv_pwm_trig_input_e"></a> <a id="drv__pwm_8h_1a0c2482b49dcb9ac72af1e39149192f00"></a> typedef enum [\_drv\_pwm\_trig\_input\_e](#_CPPv421_drv_pwm_trig_input_e "_drv_pwm_trig_input_e") drv\_pwm\_trig\_input\_e

<a id="_CPPv422drv_pwm_input_parity_e"></a>

<a id="_CPPv322drv_pwm_input_parity_e"></a> <a id="_CPPv222drv_pwm_input_parity_e"></a> <a id="drv_pwm_input_parity_e"></a> <a id="drv__pwm_8h_1a26ec8f2dc25ced2f7f0c417b559ebf8a"></a> typedef enum [\_drv\_pwm\_input\_parity\_e](#_CPPv423_drv_pwm_input_parity_e "_drv_pwm_input_parity_e") drv\_pwm\_input\_parity\_e

<a id="_CPPv423drv_pwm_capture_param_t"></a>

<a id="_CPPv323drv_pwm_capture_param_t"></a> <a id="_CPPv223drv_pwm_capture_param_t"></a> <a id="drv_pwm_capture_param_t"></a> <a id="drv__pwm_8h_1a29ec0596b9faeb17cad62ad95c41f81e"></a> typedef struct [\_drv\_pwm\_capture\_param\_t](#_CPPv424_drv_pwm_capture_param_t "_drv_pwm_capture_param_t") drv\_pwm\_capture\_param\_t

<a id="_CPPv414pfunc_pwm_cb_t"></a>

<a id="_CPPv314pfunc_pwm_cb_t"></a> <a id="_CPPv214pfunc_pwm_cb_t"></a> <a id="pfunc_pwm_cb_t"></a> <a id="drv__pwm_8h_1af9046923829449161c495900568065f9"></a> typedef void (\*pfunc\_pwm\_cb\_t)(uint32\_t chn\_index, [drv\_pwm\_mode\_e](#_CPPv414drv_pwm_mode_e "drv_pwm_mode_e") e\_irq\_mode, void \*pv\_arg)

<a id="_CPPv421pfunc_pwm_breath_cb_t"></a>

<a id="_CPPv321pfunc_pwm_breath_cb_t"></a> <a id="_CPPv221pfunc_pwm_breath_cb_t"></a> <a id="pfunc_pwm_breath_cb_t"></a> <a id="drv__pwm_8h_1af4108187783c20aba5698d169f976230"></a> typedef void (\*pfunc\_pwm\_breath\_cb\_t)(uint32\_t chn\_index, [drv\_pwm\_breath\_irq\_e](#_CPPv420drv_pwm_breath_irq_e "drv_pwm_breath_irq_e") e\_irq\_mode, void \*pv\_arg)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv418_drv_pwm_src_clk_e"></a>

<a id="_CPPv318_drv_pwm_src_clk_e"></a> <a id="_CPPv218_drv_pwm_src_clk_e"></a> <a id="drv__pwm_8h_1a5aabf09e621e17264f48454cc844964c"></a> enum \_drv\_pwm\_src\_clk\_e
:   PWM source clock.

    *Values:*

    <a id="_CPPv4N18_drv_pwm_src_clk_e19DRV_PWM_SRC_CLK_32KE"></a>

    <a id="_CPPv3N18_drv_pwm_src_clk_e19DRV_PWM_SRC_CLK_32KE"></a> <a id="_CPPv2N18_drv_pwm_src_clk_e19DRV_PWM_SRC_CLK_32KE"></a> <a id="drv__pwm_8h_1a5aabf09e621e17264f48454cc844964ca0581b60a6071ad8b8756622a2f346be9"></a> enumerator DRV\_PWM\_SRC\_CLK\_32K

    <a id="_CPPv4N18_drv_pwm_src_clk_e19DRV_PWM_SRC_CLK_26ME"></a>

    <a id="_CPPv3N18_drv_pwm_src_clk_e19DRV_PWM_SRC_CLK_26ME"></a> <a id="_CPPv2N18_drv_pwm_src_clk_e19DRV_PWM_SRC_CLK_26ME"></a> <a id="drv__pwm_8h_1a5aabf09e621e17264f48454cc844964ca0848c30ebf1802990bb6eb8b70a78540"></a> enumerator DRV\_PWM\_SRC\_CLK\_26M

<a id="_CPPv415_drv_pwm_mode_e"></a>

<a id="_CPPv315_drv_pwm_mode_e"></a> <a id="_CPPv215_drv_pwm_mode_e"></a> <a id="drv__pwm_8h_1a42a14ca25733987d16b838c2eb56c9f4"></a> enum \_drv\_pwm\_mode\_e
:   PWM work mode channel\_0\~5 support DRV\_PWM\_MODE\_OUT\_PWM \& DRV\_PWM\_MODE\_IN\_CAPTURE channel\_1 support DRV\_PWM\_MODE\_BREATH too.

    *Values:*

    <a id="_CPPv4N15_drv_pwm_mode_e23DRV_PWM_MODE_RESET_NULLE"></a>

    <a id="_CPPv3N15_drv_pwm_mode_e23DRV_PWM_MODE_RESET_NULLE"></a> <a id="_CPPv2N15_drv_pwm_mode_e23DRV_PWM_MODE_RESET_NULLE"></a> <a id="drv__pwm_8h_1a42a14ca25733987d16b838c2eb56c9f4a58d26ced6254cf94a6077c5824e8d856"></a> enumerator DRV\_PWM\_MODE\_RESET\_NULL

    <a id="_CPPv4N15_drv_pwm_mode_e19DRV_PWM_MODE_BREATHE"></a>

    <a id="_CPPv3N15_drv_pwm_mode_e19DRV_PWM_MODE_BREATHE"></a> <a id="_CPPv2N15_drv_pwm_mode_e19DRV_PWM_MODE_BREATHE"></a> <a id="drv__pwm_8h_1a42a14ca25733987d16b838c2eb56c9f4a9f653692bec88611b539950f03ee9506"></a> enumerator DRV\_PWM\_MODE\_BREATH

    <a id="_CPPv4N15_drv_pwm_mode_e20DRV_PWM_MODE_OUT_PWME"></a>

    <a id="_CPPv3N15_drv_pwm_mode_e20DRV_PWM_MODE_OUT_PWME"></a> <a id="_CPPv2N15_drv_pwm_mode_e20DRV_PWM_MODE_OUT_PWME"></a> <a id="drv__pwm_8h_1a42a14ca25733987d16b838c2eb56c9f4a362b931b1cd8e4b6d349e08acfb8e737"></a> enumerator DRV\_PWM\_MODE\_OUT\_PWM

    <a id="_CPPv4N15_drv_pwm_mode_e23DRV_PWM_MODE_IN_CAPTUREE"></a>

    <a id="_CPPv3N15_drv_pwm_mode_e23DRV_PWM_MODE_IN_CAPTUREE"></a> <a id="_CPPv2N15_drv_pwm_mode_e23DRV_PWM_MODE_IN_CAPTUREE"></a> <a id="drv__pwm_8h_1a42a14ca25733987d16b838c2eb56c9f4a22dd2f66ebf9006c3da0b064ee6d06e9"></a> enumerator DRV\_PWM\_MODE\_IN\_CAPTURE

<a id="_CPPv421_drv_pwm_breath_irq_e"></a>

<a id="_CPPv321_drv_pwm_breath_irq_e"></a> <a id="_CPPv221_drv_pwm_breath_irq_e"></a> <a id="drv__pwm_8h_1a0e07b8a05658d2eef5d9e6afe5acc180"></a> enum \_drv\_pwm\_breath\_irq\_e
:   *Values:*

    <a id="_CPPv4N21_drv_pwm_breath_irq_e21DRV_PWM_BREATH_IRQ_ONE"></a>

    <a id="_CPPv3N21_drv_pwm_breath_irq_e21DRV_PWM_BREATH_IRQ_ONE"></a> <a id="_CPPv2N21_drv_pwm_breath_irq_e21DRV_PWM_BREATH_IRQ_ONE"></a> <a id="drv__pwm_8h_1a0e07b8a05658d2eef5d9e6afe5acc180abca3584b03626ec0f6734faca94d7260"></a> enumerator DRV\_PWM\_BREATH\_IRQ\_ON

    <a id="_CPPv4N21_drv_pwm_breath_irq_e22DRV_PWM_BREATH_IRQ_OFFE"></a>

    <a id="_CPPv3N21_drv_pwm_breath_irq_e22DRV_PWM_BREATH_IRQ_OFFE"></a> <a id="_CPPv2N21_drv_pwm_breath_irq_e22DRV_PWM_BREATH_IRQ_OFFE"></a> <a id="drv__pwm_8h_1a0e07b8a05658d2eef5d9e6afe5acc180a06df4e6c9cac0f8504e7320ee7e7da7d"></a> enumerator DRV\_PWM\_BREATH\_IRQ\_OFF

<a id="_CPPv421_drv_pwm_breath_out_e"></a>

<a id="_CPPv321_drv_pwm_breath_out_e"></a> <a id="_CPPv221_drv_pwm_breath_out_e"></a> <a id="drv__pwm_8h_1a0d343e3b92804f11a383b6cc7787429e"></a> enum \_drv\_pwm\_breath\_out\_e
:   *Values:*

    <a id="_CPPv4N21_drv_pwm_breath_out_e18DRV_PWM_BREATH_OUTE"></a>

    <a id="_CPPv3N21_drv_pwm_breath_out_e18DRV_PWM_BREATH_OUTE"></a> <a id="_CPPv2N21_drv_pwm_breath_out_e18DRV_PWM_BREATH_OUTE"></a> <a id="drv__pwm_8h_1a0d343e3b92804f11a383b6cc7787429ea983e55292adcb22401a11de5f35d0b87"></a> enumerator DRV\_PWM\_BREATH\_OUT

    <a id="_CPPv4N21_drv_pwm_breath_out_e16DRV_PWM_LIGHT_ONE"></a>

    <a id="_CPPv3N21_drv_pwm_breath_out_e16DRV_PWM_LIGHT_ONE"></a> <a id="_CPPv2N21_drv_pwm_breath_out_e16DRV_PWM_LIGHT_ONE"></a> <a id="drv__pwm_8h_1a0d343e3b92804f11a383b6cc7787429eaea191c11ba2a580544d802a6b3a70207"></a> enumerator DRV\_PWM\_LIGHT\_ON

    <a id="_CPPv4N21_drv_pwm_breath_out_e17DRV_PWM_LIGHT_OFFE"></a>

    <a id="_CPPv3N21_drv_pwm_breath_out_e17DRV_PWM_LIGHT_OFFE"></a> <a id="_CPPv2N21_drv_pwm_breath_out_e17DRV_PWM_LIGHT_OFFE"></a> <a id="drv__pwm_8h_1a0d343e3b92804f11a383b6cc7787429ea9d79c97d8a444d91a050d2b2075dc5f4"></a> enumerator DRV\_PWM\_LIGHT\_OFF

<a id="_CPPv422_drv_pwm_output_mode_e"></a>

<a id="_CPPv322_drv_pwm_output_mode_e"></a> <a id="_CPPv222_drv_pwm_output_mode_e"></a> <a id="drv__pwm_8h_1a0b3e700b28c3469cee87f39c94e68011"></a> enum \_drv\_pwm\_output\_mode\_e
:   *Values:*

    <a id="_CPPv4N22_drv_pwm_output_mode_e24DRV_PWM_OUTPUT_MODE_KEEPE"></a>

    <a id="_CPPv3N22_drv_pwm_output_mode_e24DRV_PWM_OUTPUT_MODE_KEEPE"></a> <a id="_CPPv2N22_drv_pwm_output_mode_e24DRV_PWM_OUTPUT_MODE_KEEPE"></a> <a id="drv__pwm_8h_1a0b3e700b28c3469cee87f39c94e68011ac476f4ae2f4825fee3dc2103e20f2f5f"></a> enumerator DRV\_PWM\_OUTPUT\_MODE\_KEEP

    <a id="_CPPv4N22_drv_pwm_output_mode_e30DRV_PWM_OUTPUT_MODE_CMP_INVERTE"></a>

    <a id="_CPPv3N22_drv_pwm_output_mode_e30DRV_PWM_OUTPUT_MODE_CMP_INVERTE"></a> <a id="_CPPv2N22_drv_pwm_output_mode_e30DRV_PWM_OUTPUT_MODE_CMP_INVERTE"></a> <a id="drv__pwm_8h_1a0b3e700b28c3469cee87f39c94e68011a0fe19b84eb088295d0bd131d7a96efd6"></a> enumerator DRV\_PWM\_OUTPUT\_MODE\_CMP\_INVERT

    <a id="_CPPv4N22_drv_pwm_output_mode_e28DRV_PWM_OUTPUT_MODE_ALWAYS_1E"></a>

    <a id="_CPPv3N22_drv_pwm_output_mode_e28DRV_PWM_OUTPUT_MODE_ALWAYS_1E"></a> <a id="_CPPv2N22_drv_pwm_output_mode_e28DRV_PWM_OUTPUT_MODE_ALWAYS_1E"></a> <a id="drv__pwm_8h_1a0b3e700b28c3469cee87f39c94e68011ac929b1443e869d45641ae22083f89379"></a> enumerator DRV\_PWM\_OUTPUT\_MODE\_ALWAYS\_1

    <a id="_CPPv4N22_drv_pwm_output_mode_e38DRV_PWM_OUTPUT_MODE_CMP_AND_END_INVERTE"></a>

    <a id="_CPPv3N22_drv_pwm_output_mode_e38DRV_PWM_OUTPUT_MODE_CMP_AND_END_INVERTE"></a> <a id="_CPPv2N22_drv_pwm_output_mode_e38DRV_PWM_OUTPUT_MODE_CMP_AND_END_INVERTE"></a> <a id="drv__pwm_8h_1a0b3e700b28c3469cee87f39c94e68011a1198cc26f55dfc14463af984abb96f99"></a> enumerator DRV\_PWM\_OUTPUT\_MODE\_CMP\_AND\_END\_INVERT

    <a id="_CPPv4N22_drv_pwm_output_mode_e28DRV_PWM_OUTPUT_MODE_ALWAYS_0E"></a>

    <a id="_CPPv3N22_drv_pwm_output_mode_e28DRV_PWM_OUTPUT_MODE_ALWAYS_0E"></a> <a id="_CPPv2N22_drv_pwm_output_mode_e28DRV_PWM_OUTPUT_MODE_ALWAYS_0E"></a> <a id="drv__pwm_8h_1a0b3e700b28c3469cee87f39c94e68011a000a8542014e61c68a4861df82267036"></a> enumerator DRV\_PWM\_OUTPUT\_MODE\_ALWAYS\_0

<a id="_CPPv423_drv_pwm_output_count_e"></a>

<a id="_CPPv323_drv_pwm_output_count_e"></a> <a id="_CPPv223_drv_pwm_output_count_e"></a> <a id="drv__pwm_8h_1ad1237833c4ba88826614eb267ef9d9f3"></a> enum \_drv\_pwm\_output\_count\_e
:   *Values:*

    <a id="_CPPv4N23_drv_pwm_output_count_e27DRV_PWM_OUTPUT_DIR_INCREASEE"></a>

    <a id="_CPPv3N23_drv_pwm_output_count_e27DRV_PWM_OUTPUT_DIR_INCREASEE"></a> <a id="_CPPv2N23_drv_pwm_output_count_e27DRV_PWM_OUTPUT_DIR_INCREASEE"></a> <a id="drv__pwm_8h_1ad1237833c4ba88826614eb267ef9d9f3a544ed7e99059a32e02de3577de09b1ae"></a> enumerator DRV\_PWM\_OUTPUT\_DIR\_INCREASE

    <a id="_CPPv4N23_drv_pwm_output_count_e27DRV_PWM_OUTPUT_BIDIR_UP_CMPE"></a>

    <a id="_CPPv3N23_drv_pwm_output_count_e27DRV_PWM_OUTPUT_BIDIR_UP_CMPE"></a> <a id="_CPPv2N23_drv_pwm_output_count_e27DRV_PWM_OUTPUT_BIDIR_UP_CMPE"></a> <a id="drv__pwm_8h_1ad1237833c4ba88826614eb267ef9d9f3ae7bab5181863bafb6d9e1a3418e4c934"></a> enumerator DRV\_PWM\_OUTPUT\_BIDIR\_UP\_CMP

    <a id="_CPPv4N23_drv_pwm_output_count_e29DRV_PWM_OUTPUT_BIDIR_DOWN_CMPE"></a>

    <a id="_CPPv3N23_drv_pwm_output_count_e29DRV_PWM_OUTPUT_BIDIR_DOWN_CMPE"></a> <a id="_CPPv2N23_drv_pwm_output_count_e29DRV_PWM_OUTPUT_BIDIR_DOWN_CMPE"></a> <a id="drv__pwm_8h_1ad1237833c4ba88826614eb267ef9d9f3a86b51404309a1e284664e5505ec2ba77"></a> enumerator DRV\_PWM\_OUTPUT\_BIDIR\_DOWN\_CMP

    <a id="_CPPv4N23_drv_pwm_output_count_e32DRV_PWM_OUTPUT_BIDIR_UP_DOWN_CMPE"></a>

    <a id="_CPPv3N23_drv_pwm_output_count_e32DRV_PWM_OUTPUT_BIDIR_UP_DOWN_CMPE"></a> <a id="_CPPv2N23_drv_pwm_output_count_e32DRV_PWM_OUTPUT_BIDIR_UP_DOWN_CMPE"></a> <a id="drv__pwm_8h_1ad1237833c4ba88826614eb267ef9d9f3a1a6d65cf51358c7f3182ac623078187e"></a> enumerator DRV\_PWM\_OUTPUT\_BIDIR\_UP\_DOWN\_CMP

    <a id="_CPPv4N23_drv_pwm_output_count_e27DRV_PWM_OUTPUT_DIR_DECREASEE"></a>

    <a id="_CPPv3N23_drv_pwm_output_count_e27DRV_PWM_OUTPUT_DIR_DECREASEE"></a> <a id="_CPPv2N23_drv_pwm_output_count_e27DRV_PWM_OUTPUT_DIR_DECREASEE"></a> <a id="drv__pwm_8h_1ad1237833c4ba88826614eb267ef9d9f3ac58655bab67eb853c65fb6ae024a7545"></a> enumerator DRV\_PWM\_OUTPUT\_DIR\_DECREASE

<a id="_CPPv421_drv_pwm_slave_mode_e"></a>

<a id="_CPPv321_drv_pwm_slave_mode_e"></a> <a id="_CPPv221_drv_pwm_slave_mode_e"></a> <a id="drv__pwm_8h_1a8a4ab3770866c6b398d6512c668edf4b"></a> enum \_drv\_pwm\_slave\_mode\_e
:   *Values:*

    <a id="_CPPv4N21_drv_pwm_slave_mode_e17DRV_PWM_SLAVE_OFFE"></a>

    <a id="_CPPv3N21_drv_pwm_slave_mode_e17DRV_PWM_SLAVE_OFFE"></a> <a id="_CPPv2N21_drv_pwm_slave_mode_e17DRV_PWM_SLAVE_OFFE"></a> <a id="drv__pwm_8h_1a8a4ab3770866c6b398d6512c668edf4baaf6b7651f7ceb4874dd6dcda44c2e6b4"></a> enumerator DRV\_PWM\_SLAVE\_OFF

    <a id="_CPPv4N21_drv_pwm_slave_mode_e17DRV_PWM_SLAVE_LEDE"></a>

    <a id="_CPPv3N21_drv_pwm_slave_mode_e17DRV_PWM_SLAVE_LEDE"></a> <a id="_CPPv2N21_drv_pwm_slave_mode_e17DRV_PWM_SLAVE_LEDE"></a> <a id="drv__pwm_8h_1a8a4ab3770866c6b398d6512c668edf4ba9566ae1f3424522479584e771add1efb"></a> enumerator DRV\_PWM\_SLAVE\_LED

    <a id="_CPPv4N21_drv_pwm_slave_mode_e23DRV_PWM_SLAVE_ENCODER_1E"></a>

    <a id="_CPPv3N21_drv_pwm_slave_mode_e23DRV_PWM_SLAVE_ENCODER_1E"></a> <a id="_CPPv2N21_drv_pwm_slave_mode_e23DRV_PWM_SLAVE_ENCODER_1E"></a> <a id="drv__pwm_8h_1a8a4ab3770866c6b398d6512c668edf4bad899513c962fb21f57f63f499d8f6a09"></a> enumerator DRV\_PWM\_SLAVE\_ENCODER\_1

    <a id="_CPPv4N21_drv_pwm_slave_mode_e23DRV_PWM_SLAVE_ENCODER_2E"></a>

    <a id="_CPPv3N21_drv_pwm_slave_mode_e23DRV_PWM_SLAVE_ENCODER_2E"></a> <a id="_CPPv2N21_drv_pwm_slave_mode_e23DRV_PWM_SLAVE_ENCODER_2E"></a> <a id="drv__pwm_8h_1a8a4ab3770866c6b398d6512c668edf4ba041154c6a88b6d0b338168993c80cc4a"></a> enumerator DRV\_PWM\_SLAVE\_ENCODER\_2

    <a id="_CPPv4N21_drv_pwm_slave_mode_e23DRV_PWM_SLAVE_ENCODER_3E"></a>

    <a id="_CPPv3N21_drv_pwm_slave_mode_e23DRV_PWM_SLAVE_ENCODER_3E"></a> <a id="_CPPv2N21_drv_pwm_slave_mode_e23DRV_PWM_SLAVE_ENCODER_3E"></a> <a id="drv__pwm_8h_1a8a4ab3770866c6b398d6512c668edf4baee5bfa84ea2f27d63616cd75481de11c"></a> enumerator DRV\_PWM\_SLAVE\_ENCODER\_3

    <a id="_CPPv4N21_drv_pwm_slave_mode_e19DRV_PWM_SLAVE_RESETE"></a>

    <a id="_CPPv3N21_drv_pwm_slave_mode_e19DRV_PWM_SLAVE_RESETE"></a> <a id="_CPPv2N21_drv_pwm_slave_mode_e19DRV_PWM_SLAVE_RESETE"></a> <a id="drv__pwm_8h_1a8a4ab3770866c6b398d6512c668edf4badf9706d76695420f4288b6dae00323e3"></a> enumerator DRV\_PWM\_SLAVE\_RESET

    <a id="_CPPv4N21_drv_pwm_slave_mode_e18DRV_PWM_SLAVE_GATEE"></a>

    <a id="_CPPv3N21_drv_pwm_slave_mode_e18DRV_PWM_SLAVE_GATEE"></a> <a id="_CPPv2N21_drv_pwm_slave_mode_e18DRV_PWM_SLAVE_GATEE"></a> <a id="drv__pwm_8h_1a8a4ab3770866c6b398d6512c668edf4ba94617de099d313e8e14094ea3b5c8c2b"></a> enumerator DRV\_PWM\_SLAVE\_GATE

    <a id="_CPPv4N21_drv_pwm_slave_mode_e21DRV_PWM_SLAVE_TRIGGERE"></a>

    <a id="_CPPv3N21_drv_pwm_slave_mode_e21DRV_PWM_SLAVE_TRIGGERE"></a> <a id="_CPPv2N21_drv_pwm_slave_mode_e21DRV_PWM_SLAVE_TRIGGERE"></a> <a id="drv__pwm_8h_1a8a4ab3770866c6b398d6512c668edf4badc7c375d83b2ff094d2525862927139c"></a> enumerator DRV\_PWM\_SLAVE\_TRIGGER

    <a id="_CPPv4N21_drv_pwm_slave_mode_e22DRV_PWM_SLAVE_HALL_1INE"></a>

    <a id="_CPPv3N21_drv_pwm_slave_mode_e22DRV_PWM_SLAVE_HALL_1INE"></a> <a id="_CPPv2N21_drv_pwm_slave_mode_e22DRV_PWM_SLAVE_HALL_1INE"></a> <a id="drv__pwm_8h_1a8a4ab3770866c6b398d6512c668edf4baa21362ac976a368e46419b620e1f0190"></a> enumerator DRV\_PWM\_SLAVE\_HALL\_1IN

    <a id="_CPPv4N21_drv_pwm_slave_mode_e25DRV_PWM_SLAVE_HALL_3xorINE"></a>

    <a id="_CPPv3N21_drv_pwm_slave_mode_e25DRV_PWM_SLAVE_HALL_3xorINE"></a> <a id="_CPPv2N21_drv_pwm_slave_mode_e25DRV_PWM_SLAVE_HALL_3xorINE"></a> <a id="drv__pwm_8h_1a8a4ab3770866c6b398d6512c668edf4baacb6cacfb792f129d7306dd11c5dcd50"></a> enumerator DRV\_PWM\_SLAVE\_HALL\_3xorIN

<a id="_CPPv421_drv_pwm_trig_input_e"></a>

<a id="_CPPv321_drv_pwm_trig_input_e"></a> <a id="_CPPv221_drv_pwm_trig_input_e"></a> <a id="drv__pwm_8h_1a580971fbf75ae89de460457ad58802e5"></a> enum \_drv\_pwm\_trig\_input\_e
:   *Values:*

    <a id="_CPPv4N21_drv_pwm_trig_input_e25DRV_PWM_INPUT_CH1st_EDGE1E"></a>

    <a id="_CPPv3N21_drv_pwm_trig_input_e25DRV_PWM_INPUT_CH1st_EDGE1E"></a> <a id="_CPPv2N21_drv_pwm_trig_input_e25DRV_PWM_INPUT_CH1st_EDGE1E"></a> <a id="drv__pwm_8h_1a580971fbf75ae89de460457ad58802e5ae2f1b6265f96cebdd3d67303ba6af6f4"></a> enumerator DRV\_PWM\_INPUT\_CH1st\_EDGE1

    <a id="_CPPv4N21_drv_pwm_trig_input_e25DRV_PWM_INPUT_CH2nd_EDGE1E"></a>

    <a id="_CPPv3N21_drv_pwm_trig_input_e25DRV_PWM_INPUT_CH2nd_EDGE1E"></a> <a id="_CPPv2N21_drv_pwm_trig_input_e25DRV_PWM_INPUT_CH2nd_EDGE1E"></a> <a id="drv__pwm_8h_1a580971fbf75ae89de460457ad58802e5a7327fbebbc86fd9981282718ef25ed27"></a> enumerator DRV\_PWM\_INPUT\_CH2nd\_EDGE1

    <a id="_CPPv4N21_drv_pwm_trig_input_e25DRV_PWM_INPUT_CH1st_EDGE2E"></a>

    <a id="_CPPv3N21_drv_pwm_trig_input_e25DRV_PWM_INPUT_CH1st_EDGE2E"></a> <a id="_CPPv2N21_drv_pwm_trig_input_e25DRV_PWM_INPUT_CH1st_EDGE2E"></a> <a id="drv__pwm_8h_1a580971fbf75ae89de460457ad58802e5a4ba1910bd7ff80b27e5f4ce36555a728"></a> enumerator DRV\_PWM\_INPUT\_CH1st\_EDGE2

    <a id="_CPPv4N21_drv_pwm_trig_input_e25DRV_PWM_INPUT_CH2nd_EDGE2E"></a>

    <a id="_CPPv3N21_drv_pwm_trig_input_e25DRV_PWM_INPUT_CH2nd_EDGE2E"></a> <a id="_CPPv2N21_drv_pwm_trig_input_e25DRV_PWM_INPUT_CH2nd_EDGE2E"></a> <a id="drv__pwm_8h_1a580971fbf75ae89de460457ad58802e5aca587f1a0c8b88acc962247a12dc5f9b"></a> enumerator DRV\_PWM\_INPUT\_CH2nd\_EDGE2

    <a id="_CPPv4N21_drv_pwm_trig_input_e18DRV_PWM_INPUT_TRI2E"></a>

    <a id="_CPPv3N21_drv_pwm_trig_input_e18DRV_PWM_INPUT_TRI2E"></a> <a id="_CPPv2N21_drv_pwm_trig_input_e18DRV_PWM_INPUT_TRI2E"></a> <a id="drv__pwm_8h_1a580971fbf75ae89de460457ad58802e5adf2c7a60acdc4348c9b1e83c01ec8b06"></a> enumerator DRV\_PWM\_INPUT\_TRI2

    <a id="_CPPv4N21_drv_pwm_trig_input_e18DRV_PWM_INPUT_TRI1E"></a>

    <a id="_CPPv3N21_drv_pwm_trig_input_e18DRV_PWM_INPUT_TRI1E"></a> <a id="_CPPv2N21_drv_pwm_trig_input_e18DRV_PWM_INPUT_TRI1E"></a> <a id="drv__pwm_8h_1a580971fbf75ae89de460457ad58802e5a2cf8ff70fddf77b16bf5c381a4f4ba46"></a> enumerator DRV\_PWM\_INPUT\_TRI1

    <a id="_CPPv4N21_drv_pwm_trig_input_e18DRV_PWM_INPUT_TRI0E"></a>

    <a id="_CPPv3N21_drv_pwm_trig_input_e18DRV_PWM_INPUT_TRI0E"></a> <a id="_CPPv2N21_drv_pwm_trig_input_e18DRV_PWM_INPUT_TRI0E"></a> <a id="drv__pwm_8h_1a580971fbf75ae89de460457ad58802e5aa7dc20b73fdff706ac577aa67f901adb"></a> enumerator DRV\_PWM\_INPUT\_TRI0

<a id="_CPPv423_drv_pwm_input_parity_e"></a>

<a id="_CPPv323_drv_pwm_input_parity_e"></a> <a id="_CPPv223_drv_pwm_input_parity_e"></a> <a id="drv__pwm_8h_1a3d588a59abe6063a43e8bdc46ddfe9cc"></a> enum \_drv\_pwm\_input\_parity\_e
:   *Values:*

    <a id="_CPPv4N23_drv_pwm_input_parity_e30DRV_PWM_INPUT_PARITY_POSE_EDGEE"></a>

    <a id="_CPPv3N23_drv_pwm_input_parity_e30DRV_PWM_INPUT_PARITY_POSE_EDGEE"></a> <a id="_CPPv2N23_drv_pwm_input_parity_e30DRV_PWM_INPUT_PARITY_POSE_EDGEE"></a> <a id="drv__pwm_8h_1a3d588a59abe6063a43e8bdc46ddfe9cca1f3f2679d7024a1c381aad122f998c40"></a> enumerator DRV\_PWM\_INPUT\_PARITY\_POSE\_EDGE

    <a id="_CPPv4N23_drv_pwm_input_parity_e29DRV_PWM_INPUT_PARITY_NEG_EDGEE"></a>

    <a id="_CPPv3N23_drv_pwm_input_parity_e29DRV_PWM_INPUT_PARITY_NEG_EDGEE"></a> <a id="_CPPv2N23_drv_pwm_input_parity_e29DRV_PWM_INPUT_PARITY_NEG_EDGEE"></a> <a id="drv__pwm_8h_1a3d588a59abe6063a43e8bdc46ddfe9cca16f731a97878939e9c6e6678bc51e03a"></a> enumerator DRV\_PWM\_INPUT\_PARITY\_NEG\_EDGE

    <a id="_CPPv4N23_drv_pwm_input_parity_e26DRV_PWM_INPUT_PARITY_2EDGEE"></a>

    <a id="_CPPv3N23_drv_pwm_input_parity_e26DRV_PWM_INPUT_PARITY_2EDGEE"></a> <a id="_CPPv2N23_drv_pwm_input_parity_e26DRV_PWM_INPUT_PARITY_2EDGEE"></a> <a id="drv__pwm_8h_1a3d588a59abe6063a43e8bdc46ddfe9cca1f84ac5faa4b37f45b4ea6bfd2a35e02"></a> enumerator DRV\_PWM\_INPUT\_PARITY\_2EDGE
