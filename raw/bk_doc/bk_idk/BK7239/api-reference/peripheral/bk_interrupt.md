# Interrupt Control Unit[](#interrupt-control-unit "永久链接至标题")

Beken chip supports interrupt service function.


## Interrupt API Status[](#interrupt-api-status "永久链接至标题")

| API | BK7239 |
| --- | --- |
| [`bk_int_isr_register()`](#_CPPv419bk_int_isr_register13icu_int_src_t15int_group_isr_tPv "bk_int_isr_register") | Y |
| [`bk_int_isr_unregister()`](#_CPPv421bk_int_isr_unregister13icu_int_src_t "bk_int_isr_unregister") | Y |
| [`bk_int_set_priority()`](#_CPPv419bk_int_set_priority13icu_int_src_t8uint32_t "bk_int_set_priority") | Y |
| `bk_int_set_group()` | Y |
| `bk_get_int_statis()` | Y |
| `bk_dump_int_statis()` | Y |


## Interrupt API Reference[](#interrupt-api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [int.h](https://github.com/bekencorp/armino/blob/main/components/int.h "https://github.com/bekencorp/armino/blob/main/components/int.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_icu_driver_init(void)[](#_CPPv418bk_icu_driver_initv "永久链接至目标")
:   Init the ICU driver.

    This API init the icu modules :


    - Init ICU driver control memory, enable fiq and irq of system platform

    This API should be called before any other ICU APIs.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_icu_driver_deinit(void)[](#_CPPv420bk_icu_driver_deinitv "永久链接至目标")
:   deinit the ICU driver

    This API deinit the icu module

    This API disable all devices’ intterrupts

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_int_isr_register([icu_int_src_t](#_CPPv413icu_int_src_t "icu_int_src_t") dev, int_group_isr_t isr, void *arg)[](#_CPPv419bk_int_isr_register13icu_int_src_t15int_group_isr_tPv "永久链接至目标")
:   register interrupt service handler


    **Attention**
    :   1. If this is called, the default interrupt handler is replaced by the new handler, the caller is fully responsible for handling the interrupt, such as, read the interrupt status, clear the interrupt status and processing the interrupt etc.

    参数
    :   - **dev** – interrupt source device

        - **isr** – int service function

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_int_isr_unregister([icu_int_src_t](#_CPPv413icu_int_src_t "icu_int_src_t") src)[](#_CPPv421bk_int_isr_unregister13icu_int_src_t "永久链接至目标")
:   unregister interrupt service handler

    参数
    :   **dev** – interrupt source device

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_int_set_priority([icu_int_src_t](#_CPPv413icu_int_src_t "icu_int_src_t") src, uint32_t int_priority)[](#_CPPv419bk_int_set_priority13icu_int_src_t8uint32_t "永久链接至目标")
:   set/change interrupt priority

    Every interrupt source has a two-level priority, the group priority and the priority. The interrupt source has higher group priority will be schedule first. The interrupt sources has higher priority will be schedule first if they has the same group priority.

    This API is used to configure the pririty.

    参数
    :   - **dev** – interrupt source device

        - **isr** – int service function

    返回
    :   - BK_OK: succeed

        - BK_ERR_NOT_SUPPORT :not support

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_int_register_mac_ps_callback([int_mac_ps_callback_t](#_CPPv421int_mac_ps_callback_t "int_mac_ps_callback_t") mac_ps_cb)[](#_CPPv431bk_int_register_mac_ps_callback21int_mac_ps_callback_t "永久链接至目标")
:   Register callback for mac ps.

    参数
    :   **mac_ps_cb** – mac ps callback

    返回
    :   - BK_OK: succeed

        - others: other errors.


## Interrupt API Typedefs[](#interrupt-api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [int_types.h](https://github.com/bekencorp/armino/blob/main/components/int_types.h "https://github.com/bekencorp/armino/blob/main/components/int_types.h")


### Macros[](#macros "永久链接至标题")

BK_ERR_INT_DEVICE_NONE[](#c.BK_ERR_INT_DEVICE_NONE "永久链接至目标")
:   icu device number is invalid

BK_ERR_INT_NOT_EXIST[](#c.BK_ERR_INT_NOT_EXIST "永久链接至目标")
:   icu device number is invalid


### Type Definitions[](#type-definitions "永久链接至标题")

typedef void (*int_mac_ps_callback_t)(uint32_t status)[](#_CPPv421int_mac_ps_callback_t "永久链接至目标")


### Enumerations[](#enumerations "永久链接至标题")

enum icu_int_src_t[](#_CPPv413icu_int_src_t "永久链接至目标")
:   *Values:*

    enumerator INT_SRC_UART0[](#_CPPv4N13icu_int_src_t13INT_SRC_UART0E "永久链接至目标")

    enumerator INT_SRC_UART1[](#_CPPv4N13icu_int_src_t13INT_SRC_UART1E "永久链接至目标")

    enumerator INT_SRC_I2C0[](#_CPPv4N13icu_int_src_t12INT_SRC_I2C0E "永久链接至目标")

    enumerator INT_SRC_IRDA[](#_CPPv4N13icu_int_src_t12INT_SRC_IRDAE "永久链接至目标")

    enumerator INT_SRC_I2S[](#_CPPv4N13icu_int_src_t11INT_SRC_I2SE "永久链接至目标")

    enumerator INT_SRC_I2C1[](#_CPPv4N13icu_int_src_t12INT_SRC_I2C1E "永久链接至目标")

    enumerator INT_SRC_SPI[](#_CPPv4N13icu_int_src_t11INT_SRC_SPIE "永久链接至目标")

    enumerator INT_SRC_GPIO[](#_CPPv4N13icu_int_src_t12INT_SRC_GPIOE "永久链接至目标")

    enumerator INT_SRC_TIMER[](#_CPPv4N13icu_int_src_t13INT_SRC_TIMERE "永久链接至目标")

    enumerator INT_SRC_PWM[](#_CPPv4N13icu_int_src_t11INT_SRC_PWME "永久链接至目标")

    enumerator INT_SRC_AUDIO[](#_CPPv4N13icu_int_src_t13INT_SRC_AUDIOE "永久链接至目标")

    enumerator INT_SRC_SARADC[](#_CPPv4N13icu_int_src_t14INT_SRC_SARADCE "永久链接至目标")

    enumerator INT_SRC_SDIO[](#_CPPv4N13icu_int_src_t12INT_SRC_SDIOE "永久链接至目标")

    enumerator INT_SRC_USB[](#_CPPv4N13icu_int_src_t11INT_SRC_USBE "永久链接至目标")

    enumerator INT_SRC_FFT[](#_CPPv4N13icu_int_src_t11INT_SRC_FFTE "永久链接至目标")

    enumerator INT_SRC_GDMA[](#_CPPv4N13icu_int_src_t12INT_SRC_GDMAE "永久链接至目标")

    enumerator INT_SRC_MODEM[](#_CPPv4N13icu_int_src_t13INT_SRC_MODEME "永久链接至目标")

    enumerator INT_SRC_MAC_TXRX_TIMER[](#_CPPv4N13icu_int_src_t22INT_SRC_MAC_TXRX_TIMERE "永久链接至目标")

    enumerator INT_SRC_MAC_TXRX_MISC[](#_CPPv4N13icu_int_src_t21INT_SRC_MAC_TXRX_MISCE "永久链接至目标")

    enumerator INT_SRC_MAC_RX_TRIGGER[](#_CPPv4N13icu_int_src_t22INT_SRC_MAC_RX_TRIGGERE "永久链接至目标")

    enumerator INT_SRC_MAC_TX_TRIGGER[](#_CPPv4N13icu_int_src_t22INT_SRC_MAC_TX_TRIGGERE "永久链接至目标")

    enumerator INT_SRC_MAC_PROT_TRIGGER[](#_CPPv4N13icu_int_src_t24INT_SRC_MAC_PROT_TRIGGERE "永久链接至目标")

    enumerator INT_SRC_MAC_GENERAL[](#_CPPv4N13icu_int_src_t19INT_SRC_MAC_GENERALE "永久链接至目标")

    enumerator INT_SRC_SDIO_DMA[](#_CPPv4N13icu_int_src_t16INT_SRC_SDIO_DMAE "永久链接至目标")

    enumerator INT_SRC_USB_PLUG_INOUT[](#_CPPv4N13icu_int_src_t22INT_SRC_USB_PLUG_INOUTE "永久链接至目标")

    enumerator INT_SRC_SECURITY[](#_CPPv4N13icu_int_src_t16INT_SRC_SECURITYE "永久链接至目标")

    enumerator INT_SRC_MAC_WAKEUP[](#_CPPv4N13icu_int_src_t18INT_SRC_MAC_WAKEUPE "永久链接至目标")

    enumerator INT_SRC_HSSPI_SLAVE[](#_CPPv4N13icu_int_src_t19INT_SRC_HSSPI_SLAVEE "永久链接至目标")

    enumerator INT_SRC_PLL_UNLOCK[](#_CPPv4N13icu_int_src_t18INT_SRC_PLL_UNLOCKE "永久链接至目标")

    enumerator INT_SRC_JPEG[](#_CPPv4N13icu_int_src_t12INT_SRC_JPEGE "永久链接至目标")

    enumerator INT_SRC_BLE[](#_CPPv4N13icu_int_src_t11INT_SRC_BLEE "永久链接至目标")

    enumerator INT_SRC_PSRAM[](#_CPPv4N13icu_int_src_t13INT_SRC_PSRAME "永久链接至目标")

    enumerator INT_SRC_LA[](#_CPPv4N13icu_int_src_t10INT_SRC_LAE "永久链接至目标")

    enumerator INT_SRC_BTDM[](#_CPPv4N13icu_int_src_t12INT_SRC_BTDME "永久链接至目标")

    enumerator INT_SRC_BT[](#_CPPv4N13icu_int_src_t10INT_SRC_BTE "永久链接至目标")

    enumerator INT_SRC_UART2[](#_CPPv4N13icu_int_src_t13INT_SRC_UART2E "永久链接至目标")

    enumerator INT_SRC_I2C2[](#_CPPv4N13icu_int_src_t12INT_SRC_I2C2E "永久链接至目标")

    enumerator INT_SRC_SPI2[](#_CPPv4N13icu_int_src_t12INT_SRC_SPI2E "永久链接至目标")

    enumerator INT_SRC_SPI3[](#_CPPv4N13icu_int_src_t12INT_SRC_SPI3E "永久链接至目标")

    enumerator INT_SRC_PWM2[](#_CPPv4N13icu_int_src_t12INT_SRC_PWM2E "永久链接至目标")

    enumerator INT_SRC_USB2[](#_CPPv4N13icu_int_src_t12INT_SRC_USB2E "永久链接至目标")

    enumerator INT_SRC_MAILBOX0[](#_CPPv4N13icu_int_src_t16INT_SRC_MAILBOX0E "永久链接至目标")

    enumerator INT_SRC_MAILBOX1[](#_CPPv4N13icu_int_src_t16INT_SRC_MAILBOX1E "永久链接至目标")

    enumerator INT_SRC_BT_WDT[](#_CPPv4N13icu_int_src_t14INT_SRC_BT_WDTE "永久链接至目标")

    enumerator INT_SRC_DSP_WDT[](#_CPPv4N13icu_int_src_t15INT_SRC_DSP_WDTE "永久链接至目标")

    enumerator INT_SRC_RTC[](#_CPPv4N13icu_int_src_t11INT_SRC_RTCE "永久链接至目标")

    enumerator INT_SRC_TOUCH[](#_CPPv4N13icu_int_src_t13INT_SRC_TOUCHE "永久链接至目标")

    enumerator INT_SRC_CEC[](#_CPPv4N13icu_int_src_t11INT_SRC_CECE "永久链接至目标")

    enumerator INT_SRC_MODEM_RC[](#_CPPv4N13icu_int_src_t16INT_SRC_MODEM_RCE "永久链接至目标")

    enumerator INT_SRC_MAC_HSU[](#_CPPv4N13icu_int_src_t15INT_SRC_MAC_HSUE "永久链接至目标")

    enumerator INT_SRC_NONE[](#_CPPv4N13icu_int_src_t12INT_SRC_NONEE "永久链接至目标")
