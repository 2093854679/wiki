---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_gpio.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-gpio"></a>

# DRV\_GPIO

<a id="drv-gpio-api-status"></a>

## DRV\_GPIO API Status

| API |
| --- |
| [`drv_gpio_initialise()`](#_CPPv419drv_gpio_initialisev "drv_gpio_initialise") |
| [`drv_gpio_pin_config_pull()`](#_CPPv424drv_gpio_pin_config_pull8uint32_tbb "drv_gpio_pin_config_pull") |
| [`drv_gpio_pin_config_output()`](#_CPPv426drv_gpio_pin_config_output8uint32_tbb "drv_gpio_pin_config_output") |
| [`drv_gpio_pin_output_reverse()`](#_CPPv427drv_gpio_pin_output_reverse8uint32_t "drv_gpio_pin_output_reverse") |
| [`drv_gpio_pin_enable_input()`](#_CPPv425drv_gpio_pin_enable_input8uint32_tb "drv_gpio_pin_enable_input") |
| [`drv_gpio_pin_get_input()`](#_CPPv422drv_gpio_pin_get_input8uint32_t "drv_gpio_pin_get_input") |
| [`drv_gpio_pin_reg_intr_callback()`](#_CPPv430drv_gpio_pin_reg_intr_callback8uint32_t20drv_gpio_intr_cond_e15pfunc_gpio_cb_t "drv_gpio_pin_reg_intr_callback") |
| [`drv_gpio_pin_enable_function()`](#_CPPv428drv_gpio_pin_enable_function8uint32_tb11gpio_func_e "drv_gpio_pin_enable_function") |
| [`drv_gpio_pin_enter_highz()`](#_CPPv424drv_gpio_pin_enter_highz8uint32_t "drv_gpio_pin_enter_highz") |
| [`drv_gpio_pin_set_driver_capacity()`](#_CPPv432drv_gpio_pin_set_driver_capacity8uint32_t7uint8_t "drv_gpio_pin_set_driver_capacity") |

<a id="drv-gpio-api-reference"></a>

## DRV\_GPIO API Reference

<a id="header-file"></a>

### Header File

- [driver/gpio/drv\_gpio.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/gpio/drv_gpio.h)

<a id="functions"></a>

### Functions

<a id="_CPPv419drv_gpio_initialisev"></a>

<a id="_CPPv319drv_gpio_initialisev"></a> <a id="_CPPv219drv_gpio_initialisev"></a> <a id="drv_gpio_initialise__void"></a> <a id="drv__gpio_8h_1adb8eeb50d6d500fa531ae8250e379d58"></a> int32\_t drv\_gpio\_initialise(void)
:   gpio driver initialise.

    gpio driver的初始化，主要是中断的注册，开机的时候调用一次

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424drv_gpio_pin_config_pull8uint32_tbb"></a>

<a id="_CPPv324drv_gpio_pin_config_pull8uint32_tbb"></a> <a id="_CPPv224drv_gpio_pin_config_pull8uint32_tbb"></a> <a id="drv_gpio_pin_config_pull__uint32_t.b.b"></a> <a id="drv__gpio_8h_1a60fc55afebee1bcf1bef7b6634efdedf"></a> int32\_t drv\_gpio\_pin\_config\_pull(uint32\_t gpio\_pin\_id, bool pull\_en, bool pull\_down)
:   config gpio pull.

    设置gpio的上拉/下拉，或者不进行上下拉

    参数:
    :   - **gpio\_pin\_id** – **\[in\]** gpio pin index, from 0 to GPIO\_PIN\_NUM
        - **pull\_en** – **\[in\]** true: enable pull false: disable pull
        - **pull\_down** – **\[in\]** true: pull down false: pull up (it works only when pull\_en is true)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426drv_gpio_pin_config_output8uint32_tbb"></a>

<a id="_CPPv326drv_gpio_pin_config_output8uint32_tbb"></a> <a id="_CPPv226drv_gpio_pin_config_output8uint32_tbb"></a> <a id="drv_gpio_pin_config_output__uint32_t.b.b"></a> <a id="drv__gpio_8h_1aa67ccf3b386ed9a3b94aad69c5f44488"></a> int32\_t drv\_gpio\_pin\_config\_output(uint32\_t gpio\_pin\_id, bool output\_en, bool out\_high)
:   config gpio output.

    配置gpio的输出功能，是否输出，输出高还是低

    参数:
    :   - **gpio\_pin\_id** – **\[in\]** gpio pin index, from 0 to GPIO\_PIN\_NUM-1
        - **output\_en** – **\[in\]** output enable, true: enable false: disable output
        - **out\_high** – **\[in\]** true: output 1 false: output 0 (it works only when output\_en is true)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427drv_gpio_pin_output_reverse8uint32_t"></a>

<a id="_CPPv327drv_gpio_pin_output_reverse8uint32_t"></a> <a id="_CPPv227drv_gpio_pin_output_reverse8uint32_t"></a> <a id="drv_gpio_pin_output_reverse__uint32_t"></a> <a id="drv__gpio_8h_1a69052a084005029228ec5ade45489cf7"></a> int32\_t drv\_gpio\_pin\_output\_reverse(uint32\_t gpio\_pin\_id)
:   reverse gpio output value.

    reverse gpio output value

    参数:
    :   **gpio\_pin\_id** – **\[in\]** gpio pin index, from 0 to GPIO\_PIN\_NUM-1

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425drv_gpio_pin_enable_input8uint32_tb"></a>

<a id="_CPPv325drv_gpio_pin_enable_input8uint32_tb"></a> <a id="_CPPv225drv_gpio_pin_enable_input8uint32_tb"></a> <a id="drv_gpio_pin_enable_input__uint32_t.b"></a> <a id="drv__gpio_8h_1af527cbfb7153c0fccc9e1a2b89c58ab7"></a> int32\_t drv\_gpio\_pin\_enable\_input(uint32\_t gpio\_pin\_id, bool input\_en)
:   enable gpio input function or not.

    是否打开gpio的输入功能

    参数:
    :   - **gpio\_pin\_id** – **\[in\]** gpio pin index, from 0 to GPIO\_PIN\_NUM-1
        - **input\_en** – **\[in\]** true: enable input function false: disable input function

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422drv_gpio_pin_get_input8uint32_t"></a>

<a id="_CPPv322drv_gpio_pin_get_input8uint32_t"></a> <a id="_CPPv222drv_gpio_pin_get_input8uint32_t"></a> <a id="drv_gpio_pin_get_input__uint32_t"></a> <a id="drv__gpio_8h_1a808783977e7209ea3e9ab3f248266b6a"></a> uint32\_t drv\_gpio\_pin\_get\_input(uint32\_t gpio\_pin\_id)
:   get input value.

    获取当前gpio的输入值，0(低电平) 1(高电平)

    参数:
    :   **gpio\_pin\_id** – **\[in\]** gpio pin index, from 0 to GPIO\_PIN\_NUM-1

    返回:
    :   input value

<a id="_CPPv430drv_gpio_pin_reg_intr_callback8uint32_t20drv_gpio_intr_cond_e15pfunc_gpio_cb_t"></a>

<a id="_CPPv330drv_gpio_pin_reg_intr_callback8uint32_t20drv_gpio_intr_cond_e15pfunc_gpio_cb_t"></a> <a id="_CPPv230drv_gpio_pin_reg_intr_callback8uint32_t20drv_gpio_intr_cond_e15pfunc_gpio_cb_t"></a> <a id="drv_gpio_pin_reg_intr_callback__uint32_t.drv_gpio_intr_cond_e.pfunc_gpio_cb_t"></a> <a id="drv__gpio_8h_1a99c51456efd2c1010bdbbc3e3ac61f82"></a> int32\_t drv\_gpio\_pin\_reg\_intr\_callback(uint32\_t gpio\_pin\_id, [drv\_gpio\_intr\_cond\_e](#_CPPv420drv_gpio_intr_cond_e "drv_gpio_intr_cond_e") e\_type, [pfunc\_gpio\_cb\_t](#_CPPv415pfunc_gpio_cb_t "pfunc_gpio_cb_t") pfn\_cb)
:   register gpio callback.

    注册GPIO的中断处理函数，如果想关掉中断，将参数pfn\_cb赋为NULL即可

    参数:
    :   - **gpio\_pin\_id** – **\[in\]** gpio pin index, from 0 to GPIO\_PIN\_NUM-1
        - **e\_type** – **\[in\]** 产生中断的条件, see [drv\_gpio\_intr\_cond\_e](#drv__gpio_8h_1aa0c5bf93283d0c532df03e1827149614)
        - **pfn\_cb** – **\[in\]** interrupt callback, disable interrupt if it is NULL

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv428drv_gpio_pin_enable_function8uint32_tb11gpio_func_e"></a>

<a id="_CPPv328drv_gpio_pin_enable_function8uint32_tb11gpio_func_e"></a> <a id="_CPPv228drv_gpio_pin_enable_function8uint32_tb11gpio_func_e"></a> <a id="drv_gpio_pin_enable_function__uint32_t.b.gpio_func_e"></a> <a id="drv__gpio_8h_1a35c4c159a4ff929e67794a94805a4f4b"></a> int32\_t drv\_gpio\_pin\_enable\_function(uint32\_t gpio\_pin\_id, bool func\_en, gpio\_func\_e e\_func)
:   enable gpio peripheral function or not.

    打开或关闭GPIO的外设功能

    参数:
    :   - **gpio\_pin\_id** – **\[in\]** gpio pin index, from 0 to GPIO\_PIN\_NUM-1
        - **func\_en** – **\[in\]** true: enable function false: disable function
        - **e\_func** – **\[in\]** see gpio\_func\_e (it works only when func\_en is true)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424drv_gpio_pin_enter_highz8uint32_t"></a>

<a id="_CPPv324drv_gpio_pin_enter_highz8uint32_t"></a> <a id="_CPPv224drv_gpio_pin_enter_highz8uint32_t"></a> <a id="drv_gpio_pin_enter_highz__uint32_t"></a> <a id="drv__gpio_8h_1ad3d25ff8e57c3a5c5b3a8e061ca2df27"></a> int32\_t drv\_gpio\_pin\_enter\_highz(uint32\_t gpio\_pin\_id)
:   make the gpio enter high Z.

    参数:
    :   **gpio\_pin\_id** – **\[in\]** gpio pin index, from 0 to GPIO\_PIN\_NUM-1

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv432drv_gpio_pin_set_driver_capacity8uint32_t7uint8_t"></a>

<a id="_CPPv332drv_gpio_pin_set_driver_capacity8uint32_t7uint8_t"></a> <a id="_CPPv232drv_gpio_pin_set_driver_capacity8uint32_t7uint8_t"></a> <a id="drv_gpio_pin_set_driver_capacity__uint32_t.uint8_t"></a> <a id="drv__gpio_8h_1acb1747e8107b644839734df0468d9142"></a> int32\_t drv\_gpio\_pin\_set\_driver\_capacity(uint32\_t gpio\_pin\_id, uint8\_t value)
:   set gpio driver capacity.

    参数:
    :   - **gpio\_pin\_id** – **\[in\]** gpio pin index, from 0 to GPIO\_PIN\_NUM-1\]
        - **value** – **\[in\]** driver level, form 0 to 3

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="macros"></a>

### Macros

<a id="c.GPIO_PIN0"></a>

<a id="drv__gpio_8h_1a67f2e6c6f1966ab9a91d24145905feaf"></a> GPIO\_PIN0

<a id="c.GPIO_PIN1"></a>

<a id="drv__gpio_8h_1a2dc81f879c206e185859e16a1d183d20"></a> GPIO\_PIN1

<a id="c.GPIO_PIN2"></a>

<a id="drv__gpio_8h_1aebf3be1d7b203c33417509d429207294"></a> GPIO\_PIN2

<a id="c.GPIO_PIN3"></a>

<a id="drv__gpio_8h_1abcf7b7e5a9111274f0754ba30f2f8c1d"></a> GPIO\_PIN3

<a id="c.GPIO_PIN4"></a>

<a id="drv__gpio_8h_1ac495e8033fa04b85308efe349e7d82e6"></a> GPIO\_PIN4

<a id="c.GPIO_PIN5"></a>

<a id="drv__gpio_8h_1afb54cfe4db898aff180c3a187469e8cf"></a> GPIO\_PIN5

<a id="c.GPIO_PIN6"></a>

<a id="drv__gpio_8h_1a6dc2613b3902598dd9bedea1588547d0"></a> GPIO\_PIN6

<a id="c.GPIO_PIN7"></a>

<a id="drv__gpio_8h_1ad8c9677b2629cc4f2086e730df92208e"></a> GPIO\_PIN7

<a id="c.GPIO_PIN8"></a>

<a id="drv__gpio_8h_1a0a6a0329e3a1f4580abdba7ea88bde2e"></a> GPIO\_PIN8

<a id="c.GPIO_PIN9"></a>

<a id="drv__gpio_8h_1a36ea3f65f6d277c35ac3e164a98db1aa"></a> GPIO\_PIN9

<a id="c.GPIO_PIN10"></a>

<a id="drv__gpio_8h_1ad2801886720d62e87a3dcfc62e9bae95"></a> GPIO\_PIN10

<a id="c.GPIO_PIN11"></a>

<a id="drv__gpio_8h_1a7f093153e7358f4325de71c9d0309492"></a> GPIO\_PIN11

<a id="c.GPIO_PIN12"></a>

<a id="drv__gpio_8h_1a0b32a7c1889c071ee4634eefb9511ac2"></a> GPIO\_PIN12

<a id="c.GPIO_PIN13"></a>

<a id="drv__gpio_8h_1ab7d59c1ff20366d38f2597afedd75c19"></a> GPIO\_PIN13

<a id="c.GPIO_PIN14"></a>

<a id="drv__gpio_8h_1a04575bab91f31a10e29a9397b87b38f7"></a> GPIO\_PIN14

<a id="c.GPIO_PIN15"></a>

<a id="drv__gpio_8h_1a979c8b086aa708c5301f6d73c16d5b0b"></a> GPIO\_PIN15

<a id="c.GPIO_PIN16"></a>

<a id="drv__gpio_8h_1af34be8bedd867d52b85b7d4eb7b3b770"></a> GPIO\_PIN16

<a id="c.GPIO_PIN17"></a>

<a id="drv__gpio_8h_1a29a09c2adf4fafbe8798264af3256689"></a> GPIO\_PIN17

<a id="c.GPIO_PIN18"></a>

<a id="drv__gpio_8h_1a5be77a66b8fd363516d6bd6028f1958d"></a> GPIO\_PIN18

<a id="c.GPIO_PIN19"></a>

<a id="drv__gpio_8h_1aba4f7e4f864b03e6cbc751d0d085b965"></a> GPIO\_PIN19

<a id="c.GPIO_PIN20"></a>

<a id="drv__gpio_8h_1ac3f0f1478aef164fa9526cc5a68d013f"></a> GPIO\_PIN20

<a id="c.GPIO_PIN21"></a>

<a id="drv__gpio_8h_1a29a579535156a1521b103a91b816d725"></a> GPIO\_PIN21

<a id="c.GPIO_PIN22"></a>

<a id="drv__gpio_8h_1acae80e8e6a6fb035b31fef45479ca43a"></a> GPIO\_PIN22

<a id="c.GPIO_PIN23"></a>

<a id="drv__gpio_8h_1ac69ff378e693ca54e1841341e8f32991"></a> GPIO\_PIN23

<a id="c.GPIO_PIN24"></a>

<a id="drv__gpio_8h_1af30db8c61ef8100d3eb611951d94f0ce"></a> GPIO\_PIN24

<a id="c.GPIO_PIN25"></a>

<a id="drv__gpio_8h_1ac7348c4d7173aa6591e6f6223754b4b8"></a> GPIO\_PIN25

<a id="c.GPIO_PIN26"></a>

<a id="drv__gpio_8h_1a49ccbdcffed67af9806b02c7e5606b50"></a> GPIO\_PIN26

<a id="c.GPIO_PIN27"></a>

<a id="drv__gpio_8h_1aa34af5fb91ae73f2c3f2d30878b36799"></a> GPIO\_PIN27

<a id="c.GPIO_PIN28"></a>

<a id="drv__gpio_8h_1a3bf681f3a41509cc21953742d3308016"></a> GPIO\_PIN28

<a id="c.GPIO_PIN29"></a>

<a id="drv__gpio_8h_1a8ffa60693e7b5a44aeceae2a24b32863"></a> GPIO\_PIN29

<a id="c.GPIO_PIN30"></a>

<a id="drv__gpio_8h_1ab0fcbeb73ea81b78b9ee809e7cec9bfa"></a> GPIO\_PIN30

<a id="c.GPIO_PIN31"></a>

<a id="drv__gpio_8h_1a2995b5b8bd941dd4c94889ef73978cd1"></a> GPIO\_PIN31

<a id="c.GPIO_OUT_HIGH"></a>

<a id="drv__gpio_8h_1a8e0ab8287c9b08767e8c0f53c25628fe"></a> GPIO\_OUT\_HIGH(x)

<a id="c.GPIO_OUT_LOW"></a>

<a id="drv__gpio_8h_1acf7c70bc4d730701b5adb1d73ad74679"></a> GPIO\_OUT\_LOW(x)

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv420drv_gpio_intr_cond_e"></a>

<a id="_CPPv320drv_gpio_intr_cond_e"></a> <a id="_CPPv220drv_gpio_intr_cond_e"></a> <a id="drv_gpio_intr_cond_e"></a> <a id="drv__gpio_8h_1aa0c5bf93283d0c532df03e1827149614"></a> typedef enum [\_drv\_gpio\_intr\_cond\_e](#_CPPv421_drv_gpio_intr_cond_e "_drv_gpio_intr_cond_e") drv\_gpio\_intr\_cond\_e
:   gpio interrupt condition

<a id="_CPPv415pfunc_gpio_cb_t"></a>

<a id="_CPPv315pfunc_gpio_cb_t"></a> <a id="_CPPv215pfunc_gpio_cb_t"></a> <a id="pfunc_gpio_cb_t"></a> <a id="drv__gpio_8h_1a03962c6cabc0271cd7b8871b7f1f8201"></a> typedef void (\*pfunc\_gpio\_cb\_t)(uint32\_t gpio\_pin\_id)
:   GPIO interrupt callback.

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv421_drv_gpio_intr_cond_e"></a>

<a id="_CPPv321_drv_gpio_intr_cond_e"></a> <a id="_CPPv221_drv_gpio_intr_cond_e"></a> <a id="drv__gpio_8h_1ad5c26bc807827891da31689c4ee67815"></a> enum \_drv\_gpio\_intr\_cond\_e
:   gpio interrupt condition

    *Values:*

    <a id="_CPPv4N21_drv_gpio_intr_cond_e21DRV_GPIO_INTR_LOW_LVLE"></a>

    <a id="_CPPv3N21_drv_gpio_intr_cond_e21DRV_GPIO_INTR_LOW_LVLE"></a> <a id="_CPPv2N21_drv_gpio_intr_cond_e21DRV_GPIO_INTR_LOW_LVLE"></a> <a id="drv__gpio_8h_1ad5c26bc807827891da31689c4ee67815a6b9f1c9e167d1fade6fdb6bd191bd40f"></a> enumerator DRV\_GPIO\_INTR\_LOW\_LVL
    :   generate interrupt if gpio is low

    <a id="_CPPv4N21_drv_gpio_intr_cond_e22DRV_GPIO_INTR_HIGH_LVLE"></a>

    <a id="_CPPv3N21_drv_gpio_intr_cond_e22DRV_GPIO_INTR_HIGH_LVLE"></a> <a id="_CPPv2N21_drv_gpio_intr_cond_e22DRV_GPIO_INTR_HIGH_LVLE"></a> <a id="drv__gpio_8h_1ad5c26bc807827891da31689c4ee67815ad196a01c5878dc719143589c2158216c"></a> enumerator DRV\_GPIO\_INTR\_HIGH\_LVL
    :   generate interrupt if gpio is high

    <a id="_CPPv4N21_drv_gpio_intr_cond_e22DRV_GPIO_INTR_POS_EDGEE"></a>

    <a id="_CPPv3N21_drv_gpio_intr_cond_e22DRV_GPIO_INTR_POS_EDGEE"></a> <a id="_CPPv2N21_drv_gpio_intr_cond_e22DRV_GPIO_INTR_POS_EDGEE"></a> <a id="drv__gpio_8h_1ad5c26bc807827891da31689c4ee67815a205cc3a22f47533028994c5e3f961f74"></a> enumerator DRV\_GPIO\_INTR\_POS\_EDGE
    :   generate interrupt if gpio is on the rising edage

    <a id="_CPPv4N21_drv_gpio_intr_cond_e22DRV_GPIO_INTR_NEG_EDGEE"></a>

    <a id="_CPPv3N21_drv_gpio_intr_cond_e22DRV_GPIO_INTR_NEG_EDGEE"></a> <a id="_CPPv2N21_drv_gpio_intr_cond_e22DRV_GPIO_INTR_NEG_EDGEE"></a> <a id="drv__gpio_8h_1ad5c26bc807827891da31689c4ee67815ae702f8f063c90d3ae1d6d98596cea13d"></a> enumerator DRV\_GPIO\_INTR\_NEG\_EDGE
    :   generate interrupt if gpio is on the falling edage

    <a id="_CPPv4N21_drv_gpio_intr_cond_e22DRV_GPIO_INTR_TYPE_MAXE"></a>

    <a id="_CPPv3N21_drv_gpio_intr_cond_e22DRV_GPIO_INTR_TYPE_MAXE"></a> <a id="_CPPv2N21_drv_gpio_intr_cond_e22DRV_GPIO_INTR_TYPE_MAXE"></a> <a id="drv__gpio_8h_1ad5c26bc807827891da31689c4ee67815af91d43873aada822e13765a57ffd08f9"></a> enumerator DRV\_GPIO\_INTR\_TYPE\_MAX
    :   not used
