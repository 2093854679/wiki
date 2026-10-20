---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v2.0.1/api-reference/peripheral/bk_gpio.html
sdk_family: bk_idk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="gpio"></a>

# GPIO 使用指南

博通芯片支持丰富的 GPIO 引脚，不过有些GPIO引脚不能被应用程序所使用：

> - 在大多数博通芯片中，UART0 默认处于启用状态，GPIO 10 和GPIO 11 复用为UART0。
> - 一些 GPIO 引脚可能会被特定的外设所使用。如果某个设备通过软件被启用了，那么应用程序就不能使用该设备所使用的GPIO。例如，在 BK7258 芯片中，SPI-1 可以使用GPIO 2、GPIO 3、GPIO 4 和GPIO 5。如果SPI-1通过软件被启用了，应用程序就不能使用GPIO 2、GPIO 3、GPIO 4和GPIO 5；但如果SPI-1通过软件被禁用了，应用程序仍然可以使用GPIO 2、GPIO 3、GPIO 4和GPIO 5。

如果GPIO引脚已经被外设使用，那么像 bk\_gpio\_set\_config（）这样的API将返回 GPIO\_ERR\_INTERNAL\_USED 错误码。

一般来说，GPIO 用户可以按照以下步骤来使用 GPIO：

> - 阅读芯片硬件数据手册，以全面了解外设是如何使用GPIO引脚的。
> - 检查应用程序中已启用的外设，并找出这些设备所使用的GPIO。
> - 始终检查GPIO API的返回值，确保返回值不是 GPIO\_ERR\_INTERNAL\_USED。

备注

GPIO 实行分时复用，同一时刻仅可充当普通 GPIO 或使用其第二功能。

<a id="gpio-map-config"></a>

## GPIO MAP Config

> gpio\_map.h
>
> BK7258是多核AMP架构，在每个 CPU 核心驱动初始化过程中，GPIO会根据映射表（**GPIO\_DEFAULT\_DEV\_CONFIG**）进行配置。该映射表中的每一行包含九个元素。
> 这9个元素含义如下:
>
> > - gpio\_id：从 0 开始编号的对应GPIO引脚号。
> > - second\_func\_en：是否启用第二功能。
> > - second\_func\_dev:选择引脚的第二功能。（目前，单个GPIO引脚最多可复用八种第二功能，同一时间只能复用一个第二功能，详见 **GPIO\_DEV\_MAP**。该表格用户不可修改。）
> > - io\_mode：选择输入输出（IO）操作模式，包括输入模式、输出模式或高阻态。（输出模式下为开漏输出）
> > - pull\_mode：选择GPIO的上拉或下拉模式。
> > - int\_en：是否开启中断。
> > - int\_type：选择触发中断的条件，包括高电平触发、低电平触发、上升沿触发、下降沿触发。
> > - low\_power\_io\_ctrl：低功耗模式下是否保持GPIO的输出状态或设置为唤醒源。（配置GPIO\_LOW\_POWER\_KEEP\_INPUT\_STATUS可以将GPIO设置为唤醒源，若设为唤醒源，需要开启中断，配置中断类型。若未对该位进行设置，GPIO 在进入低功耗模式时GPIO将处于高阻状态）
> > - driver\_capacity：驱动能力选择，共有四个等级。

<a id="id1"></a>

## GPIO 部分使用介绍:

> 1. 客户需要根据其开发板的配置需求来配置 **GPIO\_DEFAULT\_DEV\_CONFIG** 表。您可以依据 **GPIO\_DEV\_MAP** 表中定义的每个 GPIO 的功能，自由地配置 **GPIO\_DEFAULT\_DEV\_CONFIG** 表。
>    如果您想在程序运行期间更改某个 GPIO 的功能，可以使用 gpio\_dev\_unmap() 函数取消原有的映射，然后使用 gpio\_dev\_map() 函数进行新的映射。 GPIO外设初始化时会在gpio\_hal.c的
>    gpio\_hal\_default\_map\_init（）函数里按照 **GPIO\_DEFAULT\_DEV\_CONFIG** 表初始化GPIO（需要打开宏CONFIG\_GPIO\_DEFAULT\_SET\_SUPPORT，平台只会操作一次，后面以用户配置为准,如果没有开启该宏，则平台不会操作GPIO，GPIO默认值为高组态）
> 2. 目前，BK7258 基于非对称多处理（AMP）架构，这会导致 GPIO 中断由多个 CPU 核心处理，影响程序的预期运行表现（CPU1 的时钟速度高于 CPU0，CPU1清除了GPIO的中断状态位，CPU0无法检测到该中断，会导致中断丢失）。为解决该问题，提出以下解决办法：
>
> > - 通过采用第3点，为每个 CPU 核心定义 **GPIO\_DEFAULT\_DEV\_CONFIG** 表，将不同的 GPIO 分配给不同的核心。这样每个 CPU 核心将仅响应其对应映射表中的中断，从而避免多个核心处理同一个中断，确保程序按预期运行。
> >
> > （**note**: 新建工程之后，每个CPU必须配置自己需要控制的GPIO,确保每个CPU管理自己的GPIO，注册相应的中断回调函数，确保程序按预期运行）
>
> 3. 以自定义方式覆盖默认的 **GPIO\_DEFAULT\_DEV\_CONFIG** 时，可按以下步骤操作：
>
> > - 打开宏定义：在项目配置文件中开启 CONFIG\_USR\_GPIO\_CFG\_EN 宏，以启用自定义 GPIO 配置功能。
> > - 创建 usr\_gpio\_cfg.h 文件：在项目的合适位置创建 usr\_gpio\_cfg.h 头文件，并在该文件中定义你自定义的 GPIO\_DEFAULT\_DEV\_CONFIG。此配置应包含你所需的所有 GPIO 的初始化设置和映射关系。如 bk\_avdk\_release\\projects\\lvgl\\86box\\config\\bk7258 所示。
> >
> > > 需要注意的是，新映射的功能必须已在 **GPIO\_DEV\_MAP** 表中定义。在初始化过程中，芯片会根据 **GPIO\_DEFAULT\_DEV\_CONFIG** 表来配置 GPIO 的状态。（注意：确保在代码中包含 usr\_gpio\_cfg.h 文件，这样在编译时就会使用你自定义的 GPIO 配置。）
>
> 4. 低功耗状态：在低功耗状态下，GPIO 可配置为输入模式（唤醒源）和输出模式。如果在低功耗期间不使用相应的 GPIO（GPIO\_LOW\_POWER\_DISCARD\_IO\_STATUS），低功耗模式程序会将GPIO 设置为高阻状态，以防止在低功耗模式下出现漏电现象。
> 5. 当你需要在低功耗模式下保持 GPIO 的输出状态时，有两种办法设置：
>
> > - 按照说明配置 **GPIO\_DEFAULT\_DEV\_CONFIG** 表。
> > - 使用 bk\_gpio\_register\_lowpower\_keep\_status() 函数注册。目前默认数量为4，可使用CONFIG\_GPIO\_DYNAMIC\_KEEP\_STATUS\_MAX\_CNT修改数量）
> > - 使用 bk\_gpio\_unregister\_lowpower\_keep\_status（）函数可以取消之前注册需要保持的GPIO。
>
> 6. 当进入低功耗模式时，可以将多个外部 GPIO 设置为唤醒源。如果任何一个 GPIO 产生中断信号，芯片就能从低功耗模式中唤醒。目前有三种办法设置为唤醒源：
>
> > - 按照说明配置 **GPIO\_DEFAULT\_DEV\_CONFIG** 表。
> > - **GPIO\_STATIC\_WAKEUP\_SOURCE\_MAP** 中设置多个唤醒源。
> > - 使用 bk\_gpio\_register\_wakeup\_source（）函数注册。（目前默认数量为4，可使用CONFIG\_GPIO\_DYNAMIC\_WAKEUP\_SOURCE\_MAX\_CNT修改数量）
> > - 使用 bk\_gpio\_unregister\_wakeup\_source（）函数可以取消注册的唤醒源。
>
> 7. 当进入低功耗模式（仅适用于低压情况）时，GPIO 的状态将被备份。退出低功耗模式后，GPIO 会自动恢复到进入该模式之前的状态。
>    （**note**：从深度睡眠模式退出后，相当于进行了一次软重启，GPIO状态不会自动恢复，会重新走初始化流程，如果需要从深度睡眠模式退出保持GPIO的状态，见第8点）
> 8. GPIO在OTA或者软件重启过程中保持状态
>
> > - 3. 初始化GPIO驱动也不掉电，增加跳过保持输出的GPIO 代码，修改文件 gpio\_hal.c 约Line：335。例如 GPIO20 保持输出：if(default\_map\[i\].gpio\_id \=\= GPIO\_20) continue;
>
> 9. 设置输入中断检测时，需要确保开启中断前，电平状态稳定，处理逻辑如下：先将电平钳位在高电平或者低电平（根据中断触发方式决定），即如果是上升沿触发中断，则一开始就需要
>    将GPIO设置到拉低状态，防止抖动或高阻态随机值引起误触发。
> 10. GPIO复用为第二功能有两种方式：静态和动态。
>
>     - 静态方式是在gpio\_map.h中的GPIO\_DEFAULT\_DEV\_CONFIG结构体数组中设置second\_func\_en和second\_func\_dev成员。启用second\_func\_en并选择所需的第二功能后，GPIO将在芯片上电初始化时自动复用为相应的第二功能。
>     - 动态方式则通过调用 gpio\_dev\_map()或 gpio\_dev\_unprotect\_map()函数实现。 gpio\_dev\_unprotect\_map()函数不会检查当前GPIO是否被别的CPU核心使用。而 gpio\_dev\_map()函数会在GPIO复用过程中加锁，保证原子操作。
>
>     （**note**: 为防止同一个管脚被多个业务使用发生冲突，建议所有的GPIO引脚通过 **GPIO\_DEFAULT\_DEV\_CONFIG** 进行配置，只有特殊情况，比如分时复用等场景，才使用动态方式配置GPIO）。
> 11. 同一外设的复用功能不能同时映射到多组引脚上，这会导致硬件资源冲突。（比如 GPIO\_30 和 GPIO\_40 同时复用为UART2的RX，这会导致UART2无法正常工作）

备注

- usr\_gpio\_cfg.h 必须被配置。
- GPIO 的驱动能力如下表所示。REG 表示 GPIO 寄存器的设置值，驱动能力共有四个等级。
  :   |  | REG\=2 | REG\=102 | REG\=202 | REG\=302 |
      | --- | --- | --- | --- | --- |
      | P14 | 10.49 | 19.95 | 33.72 | 40.8 |
      | P15 | 10.48 | 19.9 | 33.28 | 40.03 |
      | P16 | 10.41 | 19.65 | 32.76 | 39.35 |
      | P17 | 10.36 | 19.45 | 32.26 | 38.6 |

      > - 高电平拉电流(mA)

      |  | REG\=0 | REG\=100 | REG\=200 | REG\=300 |
      | --- | --- | --- | --- | --- |
      | P14 | 8.54 | 16.09 | 26.05 | 32 |
      | P15 | 8.56 | 16.19 | 26.47 | 32.6 |
      | P16 | 8.56 | 16.35 | 26.87 | 33.24 |
      | P17 | 8.62 | 16.5 | 27.24 | 33.85 |

      > - 低电平灌电流(mA)

Example:

GPIO\_0 配置为 \[GPIO\_DEV\_I2C1\_SCL\] 功能，将 GPIO\_1 配置为 \[GPIO\_DEV\_I2C1\_SDA\] 功能：
:   | gpio\_id | second\_func\_en | second\_func\_dev | io\_mode | pull\_mode | int\_en | int\_type | low\_power\_io\_ctrl | driver\_capacity |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | GPIO\_0 | GPIO\_SECOND\_FUNC\_ENABLE | GPIO\_DEV\_I2C1\_SCL | GPIO\_IO\_DISABLE | GPIO\_PULL\_UP\_EN | GPIO\_INT\_DISABLE | GPIO\_INT\_TYPE\_LOW\_LEVEL | GPIO\_LOW\_POWER\_DISCARD\_IO\_STATUS | GPIO\_DRIVER\_CAPACITY\_3 |
    | GPIO\_1 | GPIO\_SECOND\_FUNC\_ENABLE | GPIO\_DEV\_I2C1\_SDA | GPIO\_IO\_DISABLE | GPIO\_PULL\_UP\_EN | GPIO\_INT\_DISABLE | GPIO\_INT\_TYPE\_LOW\_LEVEL | GPIO\_LOW\_POWER\_DISCARD\_IO\_STATUS | GPIO\_DRIVER\_CAPACITY\_3 |

    > - PS：当使用 GPIO 的第二功能时，GPIO 默认处于关闭状态（输入输出模式 io\_mode 为 \[GPIO\_IO\_DISABLE\]）。I2C 需要更强的驱动能力（驱动能力 driver\_capacity 设为 \[GPIO\_DRIVER\_CAPACITY\_3\]）

GPIO\_0 被设置为高阻态（默认状态）：
:   | gpio\_id | second\_func\_en | second\_func\_dev | io\_mode | pull\_mode | int\_en | int\_type | low\_power\_io\_ctrl | driver\_capacity |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | GPIO\_0 | GPIO\_SECOND\_FUNC\_DISABLE | GPIO\_DEV\_INVALID | GPIO\_IO\_DISABLE | GPIO\_PULL\_DISABLE | GPIO\_INT\_DISABLE | GPIO\_INT\_TYPE\_LOW\_LEVEL | GPIO\_LOW\_POWER\_DISCARD\_IO\_STATUS | GPIO\_DRIVER\_CAPACITY\_0 |

    > - PS：禁用所有配置

GPIO\_0 设置为输入模式，并配置为下降沿触发中断：
:   | gpio\_id | second\_func\_en | second\_func\_dev | io\_mode | pull\_mode | int\_en | int\_type | low\_power\_io\_ctrl | driver\_capacity |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | GPIO\_0 | GPIO\_SECOND\_FUNC\_DISABLE | GPIO\_DEV\_INVALID | GPIO\_INPUT\_ENABLE | GPIO\_PULL\_UP\_EN | GPIO\_INT\_ENABLE | GPIO\_INT\_TYPE\_FALLING\_EDGE | GPIO\_LOW\_POWER\_DISCARD\_IO\_STATUS | GPIO\_DRIVER\_CAPACITY\_0 |

    > - PS：关闭第二功能。有 4 种中断触发条件：低电平触发、高电平触发、上升沿触发、下降沿触发

GPIO\_0 作为低功耗唤醒源，下降沿唤醒：
:   | gpio\_id | second\_func\_en | second\_func\_dev | io\_mode | pull\_mode | int\_en | int\_type | low\_power\_io\_ctrl | driver\_capacity |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | GPIO\_0 | GPIO\_SECOND\_FUNC\_DISABLE | GPIO\_DEV\_INVALID | GPIO\_INPUT\_ENABLE | GPIO\_PULL\_UP\_EN | GPIO\_INT\_ENABLE | GPIO\_INT\_TYPE\_FALLING\_EDGE | GPIO\_LOW\_POWER\_KEEP\_INPUT\_STATUS | GPIO\_DRIVER\_CAPACITY\_0 |

    > - PS：low\_power\_io\_ctrl 设置为 \[GPIO\_LOW\_POWER\_KEEP\_INPUT\_STATUS\]

<a id="q-a"></a>

## Q\&A

1. 低压模式设置了RTC和GPIO中断，RTC触发后GPIO则失效了。

   该问题原因为在进入低压模式之前，MCU会备份GPIO的状态。为了防止未使能唤醒GPIO引脚的中断，导致MCU无法被唤醒，在低压模式下，唤醒GPIO的引脚中断会被使能。
   退出中断后，该引脚的状态会恢复到进入低压之前的状态。如果在进入低压模式之前未使能唤醒引脚的中断，那么在退出低压后，该引脚的中断仍然未被使能，因此在正
   常工作模式下唤醒GPIO的中断无法被触发。
2. 进入深度休眠后，敲一下串口，设备会唤醒。
   因为一些场景需求，默认支持在low voltage、 deepsleep时使用uart来唤醒设备。如果不需要该功能，可以在gpio\_map.h中将GPIO\_STATIC\_WAKEUP\_SOURCE\_MAP中GPIO\_10注释掉。
3. 多核操作同一个GPIO之间的协同问题，某客户在多核AMP系统中未采用CPU独立配置GPIO方案，导致以下典型问题，表象如下：

> - 使用dvp摄像头打开后，按键中断偶现丢失。
> - 单独打开lcd或uvc时，按键gpio中断50%概率左右不会触发
>
> BK7258是AMP架构，多个CPU共享硬件资源。所有的GPIO引脚共享GPIO中断线。如果每个CPU没有配置自己需要控制的GPIO，在GPIO发生中断时，多个CPU核心都会接到中断通知，执行中断处理函数。
> 开dvp和lcd等操作都会开启CPU1，CPU1的主频比CPU0快，可能会清掉中断标志位，造成CPU0的GPIO中断丢失，导致程序为按照预期执行。为避免这种情况，每个CPU必须配置各自的GPIO\_MAP表。

<a id="gpio-api-status"></a>

## GPIO API Status

| API | BK7258 | BK7258\_cp1 |
| --- | --- | --- |
| [`bk_gpio_driver_init()`](#_CPPv419bk_gpio_driver_initv "bk_gpio_driver_init") | Y | Y |
| [`bk_gpio_driver_deinit()`](#_CPPv421bk_gpio_driver_deinitv "bk_gpio_driver_deinit") | Y | Y |
| [`bk_gpio_enable_output()`](#_CPPv421bk_gpio_enable_output9gpio_id_t "bk_gpio_enable_output") | Y | Y |
| [`bk_gpio_disable_output()`](#_CPPv422bk_gpio_disable_output9gpio_id_t "bk_gpio_disable_output") | Y | Y |
| [`bk_gpio_enable_input()`](#_CPPv420bk_gpio_enable_input9gpio_id_t "bk_gpio_enable_input") | Y | Y |
| [`bk_gpio_disable_input()`](#_CPPv421bk_gpio_disable_input9gpio_id_t "bk_gpio_disable_input") | Y | Y |
| [`bk_gpio_enable_pull()`](#_CPPv419bk_gpio_enable_pull9gpio_id_t "bk_gpio_enable_pull") | Y | Y |
| [`bk_gpio_disable_pull()`](#_CPPv420bk_gpio_disable_pull9gpio_id_t "bk_gpio_disable_pull") | Y | Y |
| [`bk_gpio_pull_up()`](#_CPPv415bk_gpio_pull_up9gpio_id_t "bk_gpio_pull_up") | Y | Y |
| [`bk_gpio_pull_down()`](#_CPPv417bk_gpio_pull_down9gpio_id_t "bk_gpio_pull_down") | Y | Y |
| [`bk_gpio_set_output_high()`](#_CPPv423bk_gpio_set_output_high9gpio_id_t "bk_gpio_set_output_high") | Y | Y |
| [`bk_gpio_set_output_low()`](#_CPPv422bk_gpio_set_output_low9gpio_id_t "bk_gpio_set_output_low") | Y | Y |
| [`bk_gpio_get_input()`](#_CPPv417bk_gpio_get_input9gpio_id_t "bk_gpio_get_input") | Y | Y |
| [`bk_gpio_set_config()`](#_CPPv418bk_gpio_set_config9gpio_id_tPK13gpio_config_t "bk_gpio_set_config") | Y | Y |
| [`bk_gpio_register_isr()`](#_CPPv420bk_gpio_register_isr9gpio_id_t10gpio_isr_t "bk_gpio_register_isr") | Y | Y |
| [`bk_gpio_enable_interrupt()`](#_CPPv424bk_gpio_enable_interrupt9gpio_id_t "bk_gpio_enable_interrupt") | Y | Y |
| [`bk_gpio_disable_interrupt()`](#_CPPv425bk_gpio_disable_interrupt9gpio_id_t "bk_gpio_disable_interrupt") | Y | Y |
| [`bk_gpio_set_interrupt_type()`](#_CPPv426bk_gpio_set_interrupt_type9gpio_id_t15gpio_int_type_t "bk_gpio_set_interrupt_type") | Y | Y |

<a id="application-example"></a>

## Application Example

DEMO1:
:   GPIO\_0 as wake-up source for DeepSleep or LowPower, pseudo code description and interpretation.

<a id="id3"></a>
![GPIO](../../../../_assets/e0c10b4e1f7148ca09ac-GPIO_Lowpower_Deepsleep.png)


Figure 1\. GPIO as wake-up source for DeepSleep or LowPower

<a id="gpio-api-reference"></a>

## GPIO API Reference

<a id="header-file"></a>

### Header File

- [gpio.h](https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v2.0.1/_header_files/include/driver/gpio.h)

<a id="functions"></a>

### Functions

<a id="_CPPv419bk_gpio_driver_initv"></a>

<a id="_CPPv319bk_gpio_driver_initv"></a> <a id="_CPPv219bk_gpio_driver_initv"></a> <a id="bk_gpio_driver_init__void"></a> <a id="group__bk__api__gpio_1gacae1346ccd48c98d892fe82d0473cfde"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_driver\_init(void)
:   Init the GPIO driver.

    This API init the resoure common to all GPIO channels:

    - Init GPIO driver control memory

    This API should be called before any other GPIO APIs.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_gpio_driver_deinitv"></a>

<a id="_CPPv321bk_gpio_driver_deinitv"></a> <a id="_CPPv221bk_gpio_driver_deinitv"></a> <a id="bk_gpio_driver_deinit__void"></a> <a id="group__bk__api__gpio_1ga1f1b3f85bc530c7bd4179fdcc3fb5868"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_driver\_deinit(void)
:   Deinit the GPIO driver.

    This API free all resource related to GPIO and power down all GPIO channels.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv417bk_gpio_set_value9gpio_id_t8uint32_t"></a>

<a id="_CPPv317bk_gpio_set_value9gpio_id_t8uint32_t"></a> <a id="_CPPv217bk_gpio_set_value9gpio_id_t8uint32_t"></a> <a id="bk_gpio_set_value__gpio_id_t.uint32_t"></a> <a id="group__bk__api__gpio_1gafca019ef63ca760b3764e97462c0585b"></a> void bk\_gpio\_set\_value(gpio\_id\_t id, uint32\_t v)
:   Direct set GPIO config value.

    @NOTES Please be care to use this API,unless you know the detail mean, because it will set the GPIO config value. Sometimes the special GPIO needs to re-used by one more owner, after the second owner re-used it, it should restore the config value. Before re-use a GPIO, the owner can call bk\_gpio\_get\_value and bakup it, after re-used finish, it call bk\_gpio\_set\_value to restore the prevous value.

<a id="_CPPv417bk_gpio_get_value9gpio_id_t"></a>

<a id="_CPPv317bk_gpio_get_value9gpio_id_t"></a> <a id="_CPPv217bk_gpio_get_value9gpio_id_t"></a> <a id="bk_gpio_get_value__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga21130dd4b1f24b16e8526226438f9b31"></a> uint32\_t bk\_gpio\_get\_value(gpio\_id\_t id)
:   get GPIO config value.

<a id="_CPPv421bk_gpio_enable_output9gpio_id_t"></a>

<a id="_CPPv321bk_gpio_enable_output9gpio_id_t"></a> <a id="_CPPv221bk_gpio_enable_output9gpio_id_t"></a> <a id="bk_gpio_enable_output__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga2973cb2479aaf6bbfe2efebd84d3985d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_enable\_output(gpio\_id\_t gpio\_id)
:   enable GPIO output mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - others: other errors.

<a id="_CPPv422bk_gpio_disable_output9gpio_id_t"></a>

<a id="_CPPv322bk_gpio_disable_output9gpio_id_t"></a> <a id="_CPPv222bk_gpio_disable_output9gpio_id_t"></a> <a id="bk_gpio_disable_output__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga2e177c4285dd8673b446bcd15db92126"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_disable\_output(gpio\_id\_t gpio\_id)
:   disable GPIO output mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - others: other errors.

<a id="_CPPv420bk_gpio_enable_input9gpio_id_t"></a>

<a id="_CPPv320bk_gpio_enable_input9gpio_id_t"></a> <a id="_CPPv220bk_gpio_enable_input9gpio_id_t"></a> <a id="bk_gpio_enable_input__gpio_id_t"></a> <a id="group__bk__api__gpio_1gaf9acdf13c743f920174bbb103f108ac7"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_enable\_input(gpio\_id\_t gpio\_id)
:   enable GPIO input mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - others: other errors.

<a id="_CPPv421bk_gpio_disable_input9gpio_id_t"></a>

<a id="_CPPv321bk_gpio_disable_input9gpio_id_t"></a> <a id="_CPPv221bk_gpio_disable_input9gpio_id_t"></a> <a id="bk_gpio_disable_input__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga200faf135f7d18061fc1c4057bd48b6f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_disable\_input(gpio\_id\_t gpio\_id)
:   disable GPIO input mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - others: other errors.

<a id="_CPPv419bk_gpio_enable_pull9gpio_id_t"></a>

<a id="_CPPv319bk_gpio_enable_pull9gpio_id_t"></a> <a id="_CPPv219bk_gpio_enable_pull9gpio_id_t"></a> <a id="bk_gpio_enable_pull__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga231a1940364f61c699d2d4fba643a743"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_enable\_pull(gpio\_id\_t gpio\_id)
:   enable GPIO pull mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - others: other errors.

<a id="_CPPv420bk_gpio_disable_pull9gpio_id_t"></a>

<a id="_CPPv320bk_gpio_disable_pull9gpio_id_t"></a> <a id="_CPPv220bk_gpio_disable_pull9gpio_id_t"></a> <a id="bk_gpio_disable_pull__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga044f2ca367852a0ae8f85f9440db08f8"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_disable\_pull(gpio\_id\_t gpio\_id)
:   disable gpio pull mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - others: other errors.

<a id="_CPPv415bk_gpio_pull_up9gpio_id_t"></a>

<a id="_CPPv315bk_gpio_pull_up9gpio_id_t"></a> <a id="_CPPv215bk_gpio_pull_up9gpio_id_t"></a> <a id="bk_gpio_pull_up__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga8d974991d0a7d561eda8bd14c9bfc3b5"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_pull\_up(gpio\_id\_t gpio\_id)
:   set GPIO as pull up mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - others: other errors.

<a id="_CPPv417bk_gpio_pull_down9gpio_id_t"></a>

<a id="_CPPv317bk_gpio_pull_down9gpio_id_t"></a> <a id="_CPPv217bk_gpio_pull_down9gpio_id_t"></a> <a id="bk_gpio_pull_down__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga206cf499bae8f2d5b7057f8d3f3f21fe"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_pull\_down(gpio\_id\_t gpio\_id)
:   set GPIO as pull down mode

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - others: other errors.

<a id="_CPPv418bk_gpio_set_config9gpio_id_tPK13gpio_config_t"></a>

<a id="_CPPv318bk_gpio_set_config9gpio_id_tPK13gpio_config_t"></a> <a id="_CPPv218bk_gpio_set_config9gpio_id_tPK13gpio_config_t"></a> <a id="bk_gpio_set_config__gpio_id_t.gpio_config_tCP"></a> <a id="group__bk__api__gpio_1gabc229ebbc3ae486f8538789a61491bc7"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_set\_config(gpio\_id\_t gpio\_id, const gpio\_config\_t \*config)
:   Config the GPIO mode.

    This API config GPIO’s mode

    - BK\_OK: succeed
    - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
    - BK\_ERR\_GPIO\_INVALID\_MODE: invalid GPIO’s io\_mode/pull\_mode
    - BK\_ERR\_GPIO\_INTERNAL\_USED:GPIO was map to another device
    - others: other errors.

<a id="_CPPv423bk_gpio_set_output_high9gpio_id_t"></a>

<a id="_CPPv323bk_gpio_set_output_high9gpio_id_t"></a> <a id="_CPPv223bk_gpio_set_output_high9gpio_id_t"></a> <a id="bk_gpio_set_output_high__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga6813699d36a76f6ed87e72c6f90a0592"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_set\_output\_high(gpio\_id\_t gpio\_id)
:   Set the GPIO output high,.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - BK\_ERR\_GPIO\_NOT\_OUTPUT\_MODE:GPIO not in output mode
        - others: other errors.

<a id="_CPPv422bk_gpio_set_output_low9gpio_id_t"></a>

<a id="_CPPv322bk_gpio_set_output_low9gpio_id_t"></a> <a id="_CPPv222bk_gpio_set_output_low9gpio_id_t"></a> <a id="bk_gpio_set_output_low__gpio_id_t"></a> <a id="group__bk__api__gpio_1gad53b1f39990fd6d6d051b75b0424dd9c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_set\_output\_low(gpio\_id\_t gpio\_id)
:   Set the GPIO output low,.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - BK\_ERR\_GPIO\_NOT\_OUTPUT\_MODE:GPIO not in output mode
        - others: other errors.

<a id="_CPPv417bk_gpio_get_input9gpio_id_t"></a>

<a id="_CPPv317bk_gpio_get_input9gpio_id_t"></a> <a id="_CPPv217bk_gpio_get_input9gpio_id_t"></a> <a id="bk_gpio_get_input__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga71b4f9272a2c8bc27d906f2de602bce2"></a> bool bk\_gpio\_get\_input(gpio\_id\_t gpio\_id)
:   Get the GPIO input value,.

    This API get GPIO’s input level: 0 :low\_level 1:high\_level.

    返回
    :   - input value
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - BK\_ERR\_GPIO\_NOT\_INPUT\_MODE : GPIO is not input mode
        - others: other errors.

<a id="_CPPv420bk_gpio_set_capacity9gpio_id_t6uint32"></a>

<a id="_CPPv320bk_gpio_set_capacity9gpio_id_t6uint32"></a> <a id="_CPPv220bk_gpio_set_capacity9gpio_id_t6uint32"></a> <a id="bk_gpio_set_capacity__gpio_id_t.uint32"></a> <a id="group__bk__api__gpio_1ga2e422b1299cf61773beedbddcdc15c47"></a> bool bk\_gpio\_set\_capacity(gpio\_id\_t gpio\_id, uint32 capacity)
:   Set the GPIO driver capacity.

    This API Set GPIO’s output driver capacity which range is 0\~3.

    返回
    :   - input value
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - BK\_ERR\_GPIO\_NOT\_INPUT\_MODE : GPIO is not input mode
        - others: other errors.

<a id="_CPPv426bk_gpio_set_interrupt_type9gpio_id_t15gpio_int_type_t"></a>

<a id="_CPPv326bk_gpio_set_interrupt_type9gpio_id_t15gpio_int_type_t"></a> <a id="_CPPv226bk_gpio_set_interrupt_type9gpio_id_t15gpio_int_type_t"></a> <a id="bk_gpio_set_interrupt_type__gpio_id_t.gpio_int_type_t"></a> <a id="group__bk__api__gpio_1ga33259d746c51989bbeb0d98956570235"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_set\_interrupt\_type(gpio\_id\_t gpio\_id, gpio\_int\_type\_t type)
:   Config the GPIO intterrupt type mode when use gpio intterrupt mode,.

    This API config all GPIO channels’ intterrupt mode, the mode included in gpio\_int\_type\_t.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - BK\_ERR\_GPIO\_INVALID\_INT\_TYPE: invalid GPIO int type
        - others: other errors.

<a id="_CPPv424bk_gpio_enable_interrupt9gpio_id_t"></a>

<a id="_CPPv324bk_gpio_enable_interrupt9gpio_id_t"></a> <a id="_CPPv224bk_gpio_enable_interrupt9gpio_id_t"></a> <a id="bk_gpio_enable_interrupt__gpio_id_t"></a> <a id="group__bk__api__gpio_1gacd7ff15a6390a73472c435411da6c660"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_enable\_interrupt(gpio\_id\_t id)
:   Enable GPIO intterrupt.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - BK\_ERR\_GPIO\_NOT\_INPUT\_MODE : GPIO is not input mode
        - others: other errors.

<a id="_CPPv425bk_gpio_disable_interrupt9gpio_id_t"></a>

<a id="_CPPv325bk_gpio_disable_interrupt9gpio_id_t"></a> <a id="_CPPv225bk_gpio_disable_interrupt9gpio_id_t"></a> <a id="bk_gpio_disable_interrupt__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga48e0eaf44663f68f2f2cea47e6476f95"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_disable\_interrupt(gpio\_id\_t id)
:   Disable GPIO intterrupt.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid GPIO channel
        - others: other errors.

<a id="_CPPv423bk_gpio_clear_interrupt9gpio_id_t"></a>

<a id="_CPPv323bk_gpio_clear_interrupt9gpio_id_t"></a> <a id="_CPPv223bk_gpio_clear_interrupt9gpio_id_t"></a> <a id="bk_gpio_clear_interrupt__gpio_id_t"></a> <a id="group__bk__api__gpio_1ga9309e183217de3b2dfadd4b3d35290cd"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_clear\_interrupt(gpio\_id\_t gpio\_id)
:   Clear GPIO intterrupt.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid gpio channel
        - others: other errors.

<a id="_CPPv420bk_gpio_register_isr9gpio_id_t10gpio_isr_t"></a>

<a id="_CPPv320bk_gpio_register_isr9gpio_id_t10gpio_isr_t"></a> <a id="_CPPv220bk_gpio_register_isr9gpio_id_t10gpio_isr_t"></a> <a id="bk_gpio_register_isr__gpio_id_t.gpio_isr_t"></a> <a id="group__bk__api__gpio_1gadf2d7a2aaf11b9140e9ee78de984ed2e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_register\_isr(gpio\_id\_t id, [gpio\_isr\_t](#_CPPv410gpio_isr_t "gpio_isr_t") isr)
:   Register the interrupt service routine for GPIO channel.

    This API regist gpio isr callback function.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid gpio channel
        - others: other errors.

<a id="_CPPv422bk_gpio_unregister_isr9gpio_id_t"></a>

<a id="_CPPv322bk_gpio_unregister_isr9gpio_id_t"></a> <a id="_CPPv222bk_gpio_unregister_isr9gpio_id_t"></a> <a id="bk_gpio_unregister_isr__gpio_id_t"></a> <a id="group__bk__api__gpio_1gac5d7e52d0c90e032dfa52089f6492f01"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_unregister\_isr(gpio\_id\_t id)
:   Unregister the interrupt service routine for GPIO channel.

    This API deregist gpio isr callback function.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_GPIO\_CHAN\_ID: invalid gpio channel
        - others: other errors.

<a id="_CPPv416bk_gpio_reg_saveP8uint32_t"></a>

<a id="_CPPv316bk_gpio_reg_saveP8uint32_t"></a> <a id="_CPPv216bk_gpio_reg_saveP8uint32_t"></a> <a id="bk_gpio_reg_save__uint32_tP"></a> <a id="group__bk__api__gpio_1gab087a8620f896615b5080fc7f5186b4d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_reg\_save(uint32\_t \*gpio\_cfg)
:   Register save all gpio reg value.

    This API save all gpio reg value function.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv419bk_gpio_reg_restoreP8uint32_t"></a>

<a id="_CPPv319bk_gpio_reg_restoreP8uint32_t"></a> <a id="_CPPv219bk_gpio_reg_restoreP8uint32_t"></a> <a id="bk_gpio_reg_restore__uint32_tP"></a> <a id="group__bk__api__gpio_1gac0f85bcc46f1f17f82d56d60720723ad"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_reg\_restore(uint32\_t \*gpio\_cfg)
:   Register restore all gpio reg value.

    This API restore all gpio reg value function.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv421bk_gpio_wakeup_enable7int64_t8uint64_t8uint64_t"></a>

<a id="_CPPv321bk_gpio_wakeup_enable7int64_t8uint64_t8uint64_t"></a> <a id="_CPPv221bk_gpio_wakeup_enable7int64_t8uint64_t8uint64_t"></a> <a id="bk_gpio_wakeup_enable__int64_t.uint64_t.uint64_t"></a> <a id="group__bk__api__gpio_1ga54bf46c728d9157572b533e225daf14c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_wakeup\_enable(int64\_t index, uint64\_t type\_l, uint64\_t type\_h)
:   Register configue the gpio wakeup value.

    This API configue the gpio wakeup value function.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv430bk_gpio_wakeup_interrupt_clearv"></a>

<a id="_CPPv330bk_gpio_wakeup_interrupt_clearv"></a> <a id="_CPPv230bk_gpio_wakeup_interrupt_clearv"></a> <a id="bk_gpio_wakeup_interrupt_clear"></a> <a id="group__bk__api__gpio_1gab8fe4b39f956d0151701327998bf044a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_gpio\_wakeup\_interrupt\_clear()
:   Register clear wake up interrupt.

    This API clear wake up interrupt function.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="gpio-api-typedefs"></a>

## GPIO API Typedefs

<a id="id2"></a>

### Header File

- [gpio\_types.h](https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v2.0.1/_header_files/include/driver/gpio_types.h)

<a id="structures"></a>

### Structures

<a id="_CPPv420gpio_wakeup_config_t"></a>

<a id="_CPPv320gpio_wakeup_config_t"></a> <a id="_CPPv220gpio_wakeup_config_t"></a> <a id="gpio_wakeup_config_t"></a> <a id="structgpio__wakeup__config__t"></a> struct gpio\_wakeup\_config\_t

<a id="macros"></a>

### Macros

<a id="c.BK_ERR_GPIO_CHAN_ID"></a>

<a id="group__bk__api__gpio__defs_1gaacc3e93706a93358d601c6ec04146261"></a> BK\_ERR\_GPIO\_CHAN\_ID
:   gpio channel number is invalid

<a id="c.BK_ERR_GPIO_INVALID_MODE"></a>

<a id="group__bk__api__gpio__defs_1gace5c41582937a21a27ae0820f313e9ee"></a> BK\_ERR\_GPIO\_INVALID\_MODE
:   gpio mode is invalid

<a id="c.BK_ERR_GPIO_NOT_INPUT_MODE"></a>

<a id="group__bk__api__gpio__defs_1ga0822231d653ff3a5b33526debcfddd1f"></a> BK\_ERR\_GPIO\_NOT\_INPUT\_MODE
:   gpio is not in input mode

<a id="c.BK_ERR_GPIO_SET_INVALID_FUNC_MODE"></a>

<a id="group__bk__api__gpio__defs_1ga8b45865d53d4c8b3a3f1132ec8ce05e3"></a> BK\_ERR\_GPIO\_SET\_INVALID\_FUNC\_MODE
:   gpio perial mode is invalid or was be set as 2nd func

<a id="c.BK_ERR_GPIO_INVALID_INT_TYPE"></a>

<a id="group__bk__api__gpio__defs_1ga97a713384ad81a53908f88b78bca5b13"></a> BK\_ERR\_GPIO\_INVALID\_INT\_TYPE
:   gpio int type is invalid

<a id="c.BK_ERR_GPIOS_MAP_NONE"></a>

<a id="group__bk__api__gpio__defs_1ga10f54a8b0a842f63d6a96af9b9f67a84"></a> BK\_ERR\_GPIOS\_MAP\_NONE
:   gpio map device is none

<a id="c.BK_ERR_GPIO_NOT_OUTPUT_MODE"></a>

<a id="group__bk__api__gpio__defs_1ga04b0272d3fc9708ce8f0ee7cfabdd77b"></a> BK\_ERR\_GPIO\_NOT\_OUTPUT\_MODE
:   gpio is not in output mode

<a id="c.BK_ERR_GPIO_BITS_NUM"></a>

<a id="group__bk__api__gpio__defs_1gaf9b248434af2ff4fd9cd48255cf0e176"></a> BK\_ERR\_GPIO\_BITS\_NUM
:   gpio map bit num is error

<a id="c.BK_ERR_GPIO_INTERNAL_USED"></a>

<a id="group__bk__api__gpio__defs_1ga7988719e8641431bff42a6dfe4f31631"></a> BK\_ERR\_GPIO\_INTERNAL\_USED
:   gpio map was be map to a device

<a id="c.BK_ERR_GPIO_MAP_PWMS_CHAN"></a>

<a id="group__bk__api__gpio__defs_1gabcf06b5e850fb98924efeb471d2aa539"></a> BK\_ERR\_GPIO\_MAP\_PWMS\_CHAN
:   gpio map to pwm pwms’ channel is invalid

<a id="c.BK_ERR_GPIO_INVALID_ID"></a>

<a id="group__bk__api__gpio__defs_1ga9621ce48723cd742c2e9f43667c94d1a"></a> BK\_ERR\_GPIO\_INVALID\_ID
:   gpio id is invalid

<a id="c.BK_ERR_GPIO_WAKESOURCE_OVER_MAX_CNT"></a>

<a id="group__bk__api__gpio__defs_1gafd653a6a90fb2b5e8145cf3b6c407ecd"></a> BK\_ERR\_GPIO\_WAKESOURCE\_OVER\_MAX\_CNT
:   too much GPIO is register to wakeup source

<a id="c.BK_ERR_ANA_GPIO_TYPE_NOT_SUPPORT"></a>

<a id="group__bk__api__gpio__defs_1gaa2b6eb440b415cab586e3a2cde07f5dc"></a> BK\_ERR\_ANA\_GPIO\_TYPE\_NOT\_SUPPORT
:   analog gpio wake source pin config is invalid\>

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv410gpio_isr_t"></a>

<a id="_CPPv310gpio_isr_t"></a> <a id="_CPPv210gpio_isr_t"></a> <a id="gpio_isr_t"></a> <a id="group__bk__api__gpio__defs_1ga35b08da8d5d3e07661468da1cf30eed3"></a> typedef void (\*gpio\_isr\_t)(gpio\_id\_t gpio\_id)
:   GPIO interrupt service routine.
