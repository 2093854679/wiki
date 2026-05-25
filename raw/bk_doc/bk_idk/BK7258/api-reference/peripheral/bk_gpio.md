# GPIO 使用指南[](#gpio "永久链接至标题")

[[English]](../../../../en/v2.0.1/api-reference/peripheral/bk_gpio.html "../../../../en/v2.0.1/api-reference/peripheral/bk_gpio.html")

博通芯片支持丰富的 GPIO 引脚，不过有些GPIO引脚不能被应用程序所使用：

> - 在大多数博通芯片中，UART0 默认处于启用状态，GPIO 10 和GPIO 11 复用为UART0。
> - 一些 GPIO 引脚可能会被特定的外设所使用。如果某个设备通过软件被启用了，那么应用程序就不能使用该设备所使用的GPIO。例如，在 BK7258 芯片中，SPI-1 可以使用GPIO 2、GPIO 3、GPIO 4 和GPIO 5。如果SPI-1通过软件被启用了，应用程序就不能使用GPIO 2、GPIO 3、GPIO 4和GPIO 5；但如果SPI-1通过软件被禁用了，应用程序仍然可以使用GPIO 2、GPIO 3、GPIO 4和GPIO 5。

如果GPIO引脚已经被外设使用，那么像 bk_gpio_set_config（）这样的API将返回 GPIO_ERR_INTERNAL_USED 错误码。

一般来说，GPIO 用户可以按照以下步骤来使用 GPIO：

> - 阅读芯片硬件数据手册，以全面了解外设是如何使用GPIO引脚的。
> - 检查应用程序中已启用的外设，并找出这些设备所使用的GPIO。
> - 始终检查GPIO API的返回值，确保返回值不是 GPIO_ERR_INTERNAL_USED。

备注

GPIO 实行分时复用，同一时刻仅可充当普通 GPIO 或使用其第二功能。


## GPIO MAP Config[](#gpio-map-config "永久链接至标题")

> gpio_map.h
>
> BK7258是多核AMP架构，在每个 CPU 核心驱动初始化过程中，GPIO会根据映射表（**GPIO_DEFAULT_DEV_CONFIG**）进行配置。该映射表中的每一行包含九个元素。
> 这9个元素含义如下:
>
> > - gpio_id：从 0 开始编号的对应GPIO引脚号。
> > - second_func_en：是否启用第二功能。
> > - second_func_dev:选择引脚的第二功能。（目前，单个GPIO引脚最多可复用八种第二功能，同一时间只能复用一个第二功能，详见 **GPIO_DEV_MAP**。该表格用户不可修改。）
> > - io_mode：选择输入输出（IO）操作模式，包括输入模式、输出模式或高阻态。（输出模式下为开漏输出）
> > - pull_mode：选择GPIO的上拉或下拉模式。
> > - int_en：是否开启中断。
> > - int_type：选择触发中断的条件，包括高电平触发、低电平触发、上升沿触发、下降沿触发。
> > - low_power_io_ctrl：低功耗模式下是否保持GPIO的输出状态或设置为唤醒源。（配置GPIO_LOW_POWER_KEEP_INPUT_STATUS可以将GPIO设置为唤醒源，若设为唤醒源，需要开启中断，配置中断类型。若未对该位进行设置，GPIO 在进入低功耗模式时GPIO将处于高阻状态）
> > - driver_capacity：驱动能力选择，共有四个等级。


## GPIO 部分使用介绍:[](#id1 "永久链接至标题")

> 1. 客户需要根据其开发板的配置需求来配置 **GPIO_DEFAULT_DEV_CONFIG** 表。您可以依据 **GPIO_DEV_MAP** 表中定义的每个 GPIO 的功能，自由地配置 **GPIO_DEFAULT_DEV_CONFIG** 表。
>    如果您想在程序运行期间更改某个 GPIO 的功能，可以使用 gpio_dev_unmap() 函数取消原有的映射，然后使用 gpio_dev_map() 函数进行新的映射。 GPIO外设初始化时会在gpio_hal.c的
>    gpio_hal_default_map_init（）函数里按照 **GPIO_DEFAULT_DEV_CONFIG** 表初始化GPIO（需要打开宏CONFIG_GPIO_DEFAULT_SET_SUPPORT，平台只会操作一次，后面以用户配置为准,如果没有开启该宏，则平台不会操作GPIO，GPIO默认值为高组态）
> 2. 目前，BK7258 基于非对称多处理（AMP）架构，这会导致 GPIO 中断由多个 CPU 核心处理，影响程序的预期运行表现（CPU1 的时钟速度高于 CPU0，CPU1清除了GPIO的中断状态位，CPU0无法检测到该中断，会导致中断丢失）。为解决该问题，提出以下解决办法：
>
> > - 通过采用第3点，为每个 CPU 核心定义 **GPIO_DEFAULT_DEV_CONFIG** 表，将不同的 GPIO 分配给不同的核心。这样每个 CPU 核心将仅响应其对应映射表中的中断，从而避免多个核心处理同一个中断，确保程序按预期运行。
> >
> > （**note**: 新建工程之后，每个CPU必须配置自己需要控制的GPIO,确保每个CPU管理自己的GPIO，注册相应的中断回调函数，确保程序按预期运行）
>
> 3. 以自定义方式覆盖默认的 **GPIO_DEFAULT_DEV_CONFIG** 时，可按以下步骤操作：
>
> > - 打开宏定义：在项目配置文件中开启 CONFIG_USR_GPIO_CFG_EN 宏，以启用自定义 GPIO 配置功能。
> > - 创建 usr_gpio_cfg.h 文件：在项目的合适位置创建 usr_gpio_cfg.h 头文件，并在该文件中定义你自定义的 GPIO_DEFAULT_DEV_CONFIG。此配置应包含你所需的所有 GPIO 的初始化设置和映射关系。如 bk_avdk_release\projects\lvgl\86box\config\bk7258 所示。
> >
> > > 需要注意的是，新映射的功能必须已在 **GPIO_DEV_MAP** 表中定义。在初始化过程中，芯片会根据 **GPIO_DEFAULT_DEV_CONFIG** 表来配置 GPIO 的状态。（注意：确保在代码中包含 usr_gpio_cfg.h 文件，这样在编译时就会使用你自定义的 GPIO 配置。）
>
> 4. 低功耗状态：在低功耗状态下，GPIO 可配置为输入模式（唤醒源）和输出模式。如果在低功耗期间不使用相应的 GPIO（GPIO_LOW_POWER_DISCARD_IO_STATUS），低功耗模式程序会将GPIO 设置为高阻状态，以防止在低功耗模式下出现漏电现象。
> 5. 当你需要在低功耗模式下保持 GPIO 的输出状态时，有两种办法设置：
>
> > - 按照说明配置 **GPIO_DEFAULT_DEV_CONFIG** 表。
> > - 使用 bk_gpio_register_lowpower_keep_status() 函数注册。目前默认数量为4，可使用CONFIG_GPIO_DYNAMIC_KEEP_STATUS_MAX_CNT修改数量）
> > - 使用 bk_gpio_unregister_lowpower_keep_status（）函数可以取消之前注册需要保持的GPIO。
>
> 6. 当进入低功耗模式时，可以将多个外部 GPIO 设置为唤醒源。如果任何一个 GPIO 产生中断信号，芯片就能从低功耗模式中唤醒。目前有三种办法设置为唤醒源：
>
> > - 按照说明配置 **GPIO_DEFAULT_DEV_CONFIG** 表。
> > - **GPIO_STATIC_WAKEUP_SOURCE_MAP** 中设置多个唤醒源。
> > - 使用 bk_gpio_register_wakeup_source（）函数注册。（目前默认数量为4，可使用CONFIG_GPIO_DYNAMIC_WAKEUP_SOURCE_MAX_CNT修改数量）
> > - 使用 bk_gpio_unregister_wakeup_source（）函数可以取消注册的唤醒源。
>
> 7. 当进入低功耗模式（仅适用于低压情况）时，GPIO 的状态将被备份。退出低功耗模式后，GPIO 会自动恢复到进入该模式之前的状态。
>    （**note**：从深度睡眠模式退出后，相当于进行了一次软重启，GPIO状态不会自动恢复，会重新走初始化流程，如果需要从深度睡眠模式退出保持GPIO的状态，见第8点）
> 8. GPIO在OTA或者软件重启过程中保持状态
>
> > - 3. 初始化GPIO驱动也不掉电，增加跳过保持输出的GPIO 代码，修改文件 gpio_hal.c 约Line：335。例如 GPIO20 保持输出：if(default_map[i].gpio_id == GPIO_20) continue;
>
> 9. 设置输入中断检测时，需要确保开启中断前，电平状态稳定，处理逻辑如下：先将电平钳位在高电平或者低电平（根据中断触发方式决定），即如果是上升沿触发中断，则一开始就需要
>    将GPIO设置到拉低状态，防止抖动或高阻态随机值引起误触发。
> 10. GPIO复用为第二功能有两种方式：静态和动态。
>
>     - 静态方式是在gpio_map.h中的GPIO_DEFAULT_DEV_CONFIG结构体数组中设置second_func_en和second_func_dev成员。启用second_func_en并选择所需的第二功能后，GPIO将在芯片上电初始化时自动复用为相应的第二功能。
>     - 动态方式则通过调用 gpio_dev_map()或 gpio_dev_unprotect_map()函数实现。 gpio_dev_unprotect_map()函数不会检查当前GPIO是否被别的CPU核心使用。而 gpio_dev_map()函数会在GPIO复用过程中加锁，保证原子操作。
>
>     （**note**: 为防止同一个管脚被多个业务使用发生冲突，建议所有的GPIO引脚通过 **GPIO_DEFAULT_DEV_CONFIG** 进行配置，只有特殊情况，比如分时复用等场景，才使用动态方式配置GPIO）。
> 11. 同一外设的复用功能不能同时映射到多组引脚上，这会导致硬件资源冲突。（比如 GPIO_30 和 GPIO_40 同时复用为UART2的RX，这会导致UART2无法正常工作）

备注


- usr_gpio_cfg.h 必须被配置。

- GPIO 的驱动能力如下表所示。REG 表示 GPIO 寄存器的设置值，驱动能力共有四个等级。
  :   |  | REG=2 | REG=102 | REG=202 | REG=302 |
      | --- | --- | --- | --- | --- |
      | P14 | 10.49 | 19.95 | 33.72 | 40.8 |
      | P15 | 10.48 | 19.9 | 33.28 | 40.03 |
      | P16 | 10.41 | 19.65 | 32.76 | 39.35 |
      | P17 | 10.36 | 19.45 | 32.26 | 38.6 |

      > - 高电平拉电流(mA)

      |  | REG=0 | REG=100 | REG=200 | REG=300 |
      | --- | --- | --- | --- | --- |
      | P14 | 8.54 | 16.09 | 26.05 | 32 |
      | P15 | 8.56 | 16.19 | 26.47 | 32.6 |
      | P16 | 8.56 | 16.35 | 26.87 | 33.24 |
      | P17 | 8.62 | 16.5 | 27.24 | 33.85 |

      > - 低电平灌电流(mA)

Example:

GPIO_0 配置为 [GPIO_DEV_I2C1_SCL] 功能，将 GPIO_1 配置为 [GPIO_DEV_I2C1_SDA] 功能：
:   | gpio_id | second_func_en | second_func_dev | io_mode | pull_mode | int_en | int_type | low_power_io_ctrl | driver_capacity |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | GPIO_0 | GPIO_SECOND_FUNC_ENABLE | GPIO_DEV_I2C1_SCL | GPIO_IO_DISABLE | GPIO_PULL_UP_EN | GPIO_INT_DISABLE | GPIO_INT_TYPE_LOW_LEVEL | GPIO_LOW_POWER_DISCARD_IO_STATUS | GPIO_DRIVER_CAPACITY_3 |
    | GPIO_1 | GPIO_SECOND_FUNC_ENABLE | GPIO_DEV_I2C1_SDA | GPIO_IO_DISABLE | GPIO_PULL_UP_EN | GPIO_INT_DISABLE | GPIO_INT_TYPE_LOW_LEVEL | GPIO_LOW_POWER_DISCARD_IO_STATUS | GPIO_DRIVER_CAPACITY_3 |

    > - PS：当使用 GPIO 的第二功能时，GPIO 默认处于关闭状态（输入输出模式 io_mode 为 [GPIO_IO_DISABLE]）。I2C 需要更强的驱动能力（驱动能力 driver_capacity 设为 [GPIO_DRIVER_CAPACITY_3]）

GPIO_0 被设置为高阻态（默认状态）：
:   | gpio_id | second_func_en | second_func_dev | io_mode | pull_mode | int_en | int_type | low_power_io_ctrl | driver_capacity |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | GPIO_0 | GPIO_SECOND_FUNC_DISABLE | GPIO_DEV_INVALID | GPIO_IO_DISABLE | GPIO_PULL_DISABLE | GPIO_INT_DISABLE | GPIO_INT_TYPE_LOW_LEVEL | GPIO_LOW_POWER_DISCARD_IO_STATUS | GPIO_DRIVER_CAPACITY_0 |

    > - PS：禁用所有配置

GPIO_0 设置为输入模式，并配置为下降沿触发中断：
:   | gpio_id | second_func_en | second_func_dev | io_mode | pull_mode | int_en | int_type | low_power_io_ctrl | driver_capacity |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | GPIO_0 | GPIO_SECOND_FUNC_DISABLE | GPIO_DEV_INVALID | GPIO_INPUT_ENABLE | GPIO_PULL_UP_EN | GPIO_INT_ENABLE | GPIO_INT_TYPE_FALLING_EDGE | GPIO_LOW_POWER_DISCARD_IO_STATUS | GPIO_DRIVER_CAPACITY_0 |

    > - PS：关闭第二功能。有 4 种中断触发条件：低电平触发、高电平触发、上升沿触发、下降沿触发

GPIO_0 作为低功耗唤醒源，下降沿唤醒：
:   | gpio_id | second_func_en | second_func_dev | io_mode | pull_mode | int_en | int_type | low_power_io_ctrl | driver_capacity |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | GPIO_0 | GPIO_SECOND_FUNC_DISABLE | GPIO_DEV_INVALID | GPIO_INPUT_ENABLE | GPIO_PULL_UP_EN | GPIO_INT_ENABLE | GPIO_INT_TYPE_FALLING_EDGE | GPIO_LOW_POWER_KEEP_INPUT_STATUS | GPIO_DRIVER_CAPACITY_0 |

    > - PS：low_power_io_ctrl 设置为 [GPIO_LOW_POWER_KEEP_INPUT_STATUS]


## Q&A[](#q-a "永久链接至标题")

1. 低压模式设置了RTC和GPIO中断，RTC触发后GPIO则失效了。

   该问题原因为在进入低压模式之前，MCU会备份GPIO的状态。为了防止未使能唤醒GPIO引脚的中断，导致MCU无法被唤醒，在低压模式下，唤醒GPIO的引脚中断会被使能。
   退出中断后，该引脚的状态会恢复到进入低压之前的状态。如果在进入低压模式之前未使能唤醒引脚的中断，那么在退出低压后，该引脚的中断仍然未被使能，因此在正
   常工作模式下唤醒GPIO的中断无法被触发。
2. 进入深度休眠后，敲一下串口，设备会唤醒。
   因为一些场景需求，默认支持在low voltage、 deepsleep时使用uart来唤醒设备。如果不需要该功能，可以在gpio_map.h中将GPIO_STATIC_WAKEUP_SOURCE_MAP中GPIO_10注释掉。
3. 多核操作同一个GPIO之间的协同问题，某客户在多核AMP系统中未采用CPU独立配置GPIO方案，导致以下典型问题，表象如下：

> - 使用dvp摄像头打开后，按键中断偶现丢失。
> - 单独打开lcd或uvc时，按键gpio中断50%概率左右不会触发
>
> BK7258是AMP架构，多个CPU共享硬件资源。所有的GPIO引脚共享GPIO中断线。如果每个CPU没有配置自己需要控制的GPIO，在GPIO发生中断时，多个CPU核心都会接到中断通知，执行中断处理函数。
> 开dvp和lcd等操作都会开启CPU1，CPU1的主频比CPU0快，可能会清掉中断标志位，造成CPU0的GPIO中断丢失，导致程序为按照预期执行。为避免这种情况，每个CPU必须配置各自的GPIO_MAP表。


## GPIO API Status[](#gpio-api-status "永久链接至标题")

| API | BK7258 | BK7258_cp1 |
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


## Application Example[](#application-example "永久链接至标题")

DEMO1:
:   GPIO_0 as wake-up source for DeepSleep or LowPower, pseudo code description and interpretation.

![GPIO](../../_images/GPIO_Lowpower_Deepsleep.png)

Figure 1. GPIO as wake-up source for DeepSleep or LowPower[](#id3 "永久链接至图片")


## GPIO API Reference[](#gpio-api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [gpio.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/gpio.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/gpio.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_driver_init(void)[](#_CPPv419bk_gpio_driver_initv "永久链接至目标")
:   Init the GPIO driver.

    This API init the resoure common to all GPIO channels:


    - Init GPIO driver control memory

    This API should be called before any other GPIO APIs.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_driver_deinit(void)[](#_CPPv421bk_gpio_driver_deinitv "永久链接至目标")
:   Deinit the GPIO driver.

    This API free all resource related to GPIO and power down all GPIO channels.

    返回
    :   - BK_OK: succeed

        - others: other errors.

void bk_gpio_set_value(gpio_id_t id, uint32_t v)[](#_CPPv417bk_gpio_set_value9gpio_id_t8uint32_t "永久链接至目标")
:   Direct set GPIO config value.

    @NOTES Please be care to use this API,unless you know the detail mean, because it will set the GPIO config value. Sometimes the special GPIO needs to re-used by one more owner, after the second owner re-used it, it should restore the config value. Before re-use a GPIO, the owner can call bk_gpio_get_value and bakup it, after re-used finish, it call bk_gpio_set_value to restore the prevous value.

uint32_t bk_gpio_get_value(gpio_id_t id)[](#_CPPv417bk_gpio_get_value9gpio_id_t "永久链接至目标")
:   get GPIO config value.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_enable_output(gpio_id_t gpio_id)[](#_CPPv421bk_gpio_enable_output9gpio_id_t "永久链接至目标")
:   enable GPIO output mode

    返回
    :   - BK_OK: succeed

        - BK_ERR_GPIO_CHAN_ID: invalid GPIO channel

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_disable_output(gpio_id_t gpio_id)[](#_CPPv422bk_gpio_disable_output9gpio_id_t "永久链接至目标")
:   disable GPIO output mode

    返回
    :   - BK_OK: succeed

        - BK_ERR_GPIO_CHAN_ID: invalid GPIO channel

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_enable_input(gpio_id_t gpio_id)[](#_CPPv420bk_gpio_enable_input9gpio_id_t "永久链接至目标")
:   enable GPIO input mode

    返回
    :   - BK_OK: succeed

        - BK_ERR_GPIO_CHAN_ID: invalid GPIO channel

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_disable_input(gpio_id_t gpio_id)[](#_CPPv421bk_gpio_disable_input9gpio_id_t "永久链接至目标")
:   disable GPIO input mode

    返回
    :   - BK_OK: succeed

        - BK_ERR_GPIO_CHAN_ID: invalid GPIO channel

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_enable_pull(gpio_id_t gpio_id)[](#_CPPv419bk_gpio_enable_pull9gpio_id_t "永久链接至目标")
:   enable GPIO pull mode

    返回
    :   - BK_OK: succeed

        - BK_ERR_GPIO_CHAN_ID: invalid GPIO channel

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_disable_pull(gpio_id_t gpio_id)[](#_CPPv420bk_gpio_disable_pull9gpio_id_t "永久链接至目标")
:   disable gpio pull mode

    返回
    :   - BK_OK: succeed

        - BK_ERR_GPIO_CHAN_ID: invalid GPIO channel

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_pull_up(gpio_id_t gpio_id)[](#_CPPv415bk_gpio_pull_up9gpio_id_t "永久链接至目标")
:   set GPIO as pull up mode

    返回
    :   - BK_OK: succeed

        - BK_ERR_GPIO_CHAN_ID: invalid GPIO channel

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_pull_down(gpio_id_t gpio_id)[](#_CPPv417bk_gpio_pull_down9gpio_id_t "永久链接至目标")
:   set GPIO as pull down mode

    返回
    :   - BK_OK: succeed

        - BK_ERR_GPIO_CHAN_ID: invalid GPIO channel

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_set_config(gpio_id_t gpio_id, const gpio_config_t *config)[](#_CPPv418bk_gpio_set_config9gpio_id_tPK13gpio_config_t "永久链接至目标")
:   Config the GPIO mode.

    This API config GPIO’s mode


    - BK_OK: succeed

    - BK_ERR_GPIO_CHAN_ID: invalid GPIO channel

    - BK_ERR_GPIO_INVALID_MODE: invalid GPIO’s io_mode/pull_mode

    - BK_ERR_GPIO_INTERNAL_USED:GPIO was map to another device

    - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_set_output_high(gpio_id_t gpio_id)[](#_CPPv423bk_gpio_set_output_high9gpio_id_t "永久链接至目标")
:   Set the GPIO output high,.

    返回
    :   - BK_OK: succeed

        - BK_ERR_GPIO_CHAN_ID: invalid GPIO channel

        - BK_ERR_GPIO_NOT_OUTPUT_MODE:GPIO not in output mode

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_set_output_low(gpio_id_t gpio_id)[](#_CPPv422bk_gpio_set_output_low9gpio_id_t "永久链接至目标")
:   Set the GPIO output low,.

    返回
    :   - BK_OK: succeed

        - BK_ERR_GPIO_CHAN_ID: invalid GPIO channel

        - BK_ERR_GPIO_NOT_OUTPUT_MODE:GPIO not in output mode

        - others: other errors.

bool bk_gpio_get_input(gpio_id_t gpio_id)[](#_CPPv417bk_gpio_get_input9gpio_id_t "永久链接至目标")
:   Get the GPIO input value,.

    This API get GPIO’s input level: 0 :low_level 1:high_level.

    返回
    :   - input value

        - BK_ERR_GPIO_CHAN_ID: invalid GPIO channel

        - BK_ERR_GPIO_NOT_INPUT_MODE : GPIO is not input mode

        - others: other errors.

bool bk_gpio_set_capacity(gpio_id_t gpio_id, uint32 capacity)[](#_CPPv420bk_gpio_set_capacity9gpio_id_t6uint32 "永久链接至目标")
:   Set the GPIO driver capacity.

    This API Set GPIO’s output driver capacity which range is 0~3.

    返回
    :   - input value

        - BK_ERR_GPIO_CHAN_ID: invalid GPIO channel

        - BK_ERR_GPIO_NOT_INPUT_MODE : GPIO is not input mode

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_set_interrupt_type(gpio_id_t gpio_id, gpio_int_type_t type)[](#_CPPv426bk_gpio_set_interrupt_type9gpio_id_t15gpio_int_type_t "永久链接至目标")
:   Config the GPIO intterrupt type mode when use gpio intterrupt mode,.

    This API config all GPIO channels’ intterrupt mode, the mode included in gpio_int_type_t.

    返回
    :   - BK_OK: succeed

        - BK_ERR_GPIO_CHAN_ID: invalid GPIO channel

        - BK_ERR_GPIO_INVALID_INT_TYPE: invalid GPIO int type

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_enable_interrupt(gpio_id_t id)[](#_CPPv424bk_gpio_enable_interrupt9gpio_id_t "永久链接至目标")
:   Enable GPIO intterrupt.

    返回
    :   - BK_OK: succeed

        - BK_ERR_GPIO_CHAN_ID: invalid GPIO channel

        - BK_ERR_GPIO_NOT_INPUT_MODE : GPIO is not input mode

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_disable_interrupt(gpio_id_t id)[](#_CPPv425bk_gpio_disable_interrupt9gpio_id_t "永久链接至目标")
:   Disable GPIO intterrupt.

    返回
    :   - BK_OK: succeed

        - BK_ERR_GPIO_CHAN_ID: invalid GPIO channel

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_clear_interrupt(gpio_id_t gpio_id)[](#_CPPv423bk_gpio_clear_interrupt9gpio_id_t "永久链接至目标")
:   Clear GPIO intterrupt.

    返回
    :   - BK_OK: succeed

        - BK_ERR_GPIO_CHAN_ID: invalid gpio channel

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_register_isr(gpio_id_t id, [gpio_isr_t](#_CPPv410gpio_isr_t "gpio_isr_t") isr)[](#_CPPv420bk_gpio_register_isr9gpio_id_t10gpio_isr_t "永久链接至目标")
:   Register the interrupt service routine for GPIO channel.

    This API regist gpio isr callback function.

    返回
    :   - BK_OK: succeed

        - BK_ERR_GPIO_CHAN_ID: invalid gpio channel

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_unregister_isr(gpio_id_t id)[](#_CPPv422bk_gpio_unregister_isr9gpio_id_t "永久链接至目标")
:   Unregister the interrupt service routine for GPIO channel.

    This API deregist gpio isr callback function.

    返回
    :   - BK_OK: succeed

        - BK_ERR_GPIO_CHAN_ID: invalid gpio channel

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_reg_save(uint32_t *gpio_cfg)[](#_CPPv416bk_gpio_reg_saveP8uint32_t "永久链接至目标")
:   Register save all gpio reg value.

    This API save all gpio reg value function.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_reg_restore(uint32_t *gpio_cfg)[](#_CPPv419bk_gpio_reg_restoreP8uint32_t "永久链接至目标")
:   Register restore all gpio reg value.

    This API restore all gpio reg value function.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_wakeup_enable(int64_t index, uint64_t type_l, uint64_t type_h)[](#_CPPv421bk_gpio_wakeup_enable7int64_t8uint64_t8uint64_t "永久链接至目标")
:   Register configue the gpio wakeup value.

    This API configue the gpio wakeup value function.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_gpio_wakeup_interrupt_clear()[](#_CPPv430bk_gpio_wakeup_interrupt_clearv "永久链接至目标")
:   Register clear wake up interrupt.

    This API clear wake up interrupt function.

    返回
    :   - BK_OK: succeed

        - others: other errors.


## GPIO API Typedefs[](#gpio-api-typedefs "永久链接至标题")


### Header File[](#id2 "永久链接至标题")


- [gpio_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/gpio_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/gpio_types.h")


### Structures[](#structures "永久链接至标题")

struct gpio_wakeup_config_t[](#_CPPv420gpio_wakeup_config_t "永久链接至目标")


### Macros[](#macros "永久链接至标题")

BK_ERR_GPIO_CHAN_ID[](#c.BK_ERR_GPIO_CHAN_ID "永久链接至目标")
:   gpio channel number is invalid

BK_ERR_GPIO_INVALID_MODE[](#c.BK_ERR_GPIO_INVALID_MODE "永久链接至目标")
:   gpio mode is invalid

BK_ERR_GPIO_NOT_INPUT_MODE[](#c.BK_ERR_GPIO_NOT_INPUT_MODE "永久链接至目标")
:   gpio is not in input mode

BK_ERR_GPIO_SET_INVALID_FUNC_MODE[](#c.BK_ERR_GPIO_SET_INVALID_FUNC_MODE "永久链接至目标")
:   gpio perial mode is invalid or was be set as 2nd func

BK_ERR_GPIO_INVALID_INT_TYPE[](#c.BK_ERR_GPIO_INVALID_INT_TYPE "永久链接至目标")
:   gpio int type is invalid

BK_ERR_GPIOS_MAP_NONE[](#c.BK_ERR_GPIOS_MAP_NONE "永久链接至目标")
:   gpio map device is none

BK_ERR_GPIO_NOT_OUTPUT_MODE[](#c.BK_ERR_GPIO_NOT_OUTPUT_MODE "永久链接至目标")
:   gpio is not in output mode

BK_ERR_GPIO_BITS_NUM[](#c.BK_ERR_GPIO_BITS_NUM "永久链接至目标")
:   gpio map bit num is error

BK_ERR_GPIO_INTERNAL_USED[](#c.BK_ERR_GPIO_INTERNAL_USED "永久链接至目标")
:   gpio map was be map to a device

BK_ERR_GPIO_MAP_PWMS_CHAN[](#c.BK_ERR_GPIO_MAP_PWMS_CHAN "永久链接至目标")
:   gpio map to pwm pwms’ channel is invalid

BK_ERR_GPIO_INVALID_ID[](#c.BK_ERR_GPIO_INVALID_ID "永久链接至目标")
:   gpio id is invalid

BK_ERR_GPIO_WAKESOURCE_OVER_MAX_CNT[](#c.BK_ERR_GPIO_WAKESOURCE_OVER_MAX_CNT "永久链接至目标")
:   too much GPIO is register to wakeup source

BK_ERR_ANA_GPIO_TYPE_NOT_SUPPORT[](#c.BK_ERR_ANA_GPIO_TYPE_NOT_SUPPORT "永久链接至目标")
:   analog gpio wake source pin config is invalid>


### Type Definitions[](#type-definitions "永久链接至标题")

typedef void (*gpio_isr_t)(gpio_id_t gpio_id)[](#_CPPv410gpio_isr_t "永久链接至目标")
:   GPIO interrupt service routine.
