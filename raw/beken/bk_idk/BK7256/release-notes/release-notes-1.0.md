---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/release-notes/release-notes-1.0.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="armino-1-2-0"></a>

<a id="armino-1-0"></a>

# Armino 1.2.0

We are pleased to announce the release of Armino version 1.2.0.

备注

Armino is not designed from scratch, the baseline of Armino 1.2.0 is Beken Wi-Fi SDK v3.0,
which has been used by many customers around the world. A lot of enhancements and changes
have been made in Armino 1.2.0 compares to it’s baseline, that’s what we annouced in this
release notes.

Major enhancements with this release include:

- Support new software architecture, such as components and middleware etc
- Support boot for RISC-V
- Support new APIs for following drivers:

  - ADC
  - GPIO
  - DMA
  - UART
  - SPI
  - QSPI
  - Timer
  - TRNG
  - MailBox
  - Interrupt
  - Watchdog
  - Efusea
  - PWM
  - Vault
- Support Wi-Fi 6 stack
- Support new APIs for Wi-Fi
- Support new APIs for BLE
- Support BLE 5.x stack
- Support POSIX for FreeRTOS
- Upgrade FreeRTOS to v10.0
- Upgrade LWIP to v2.1.2
- Support CMake build
- Support Kconfig and per-soc and per-project configuration
- Support new documentation

The following sections provide detailed lists of changes by component.

<a id="software-architecture"></a>

## Software Architecture

The software architecture has been redesigned:

> - A dedicated layer `components` has been added, it’s used to contain the reusable or service related modules.
> - A dedicated layer `middleware` has been added, it works as the adapter between hardware and other components.
> - A dedicated layer `projects` has been added to contains all applications, projects or examples.
> - The FreeRTOS have been moved to Armino, Armino supports FreeRTOS by default.

<a id="freertos"></a>

## FreeRTOS

The FreeRTOS has been upgrade from v9.0 to v10.0.

<a id="posix-apis"></a>

## Posix APIs

The POSIX APIs has been supported.

<a id="wi-fi"></a>

## Wi-Fi

> - Support Wi-Fi 6 stack
> - Support new Wi-Fi APIs
>
> > - [`bk_wifi_init()`](../api-reference/wifi/bk_wifi.md#_CPPv412bk_wifi_initPK18wifi_init_config_t "bk_wifi_init") \- init WiFi
> > - [`bk_wifi_deinit()`](../api-reference/wifi/bk_wifi.md#_CPPv414bk_wifi_deinitv "bk_wifi_deinit") \- deinit WiFi
> > - [`bk_wifi_set_country()`](../api-reference/wifi/bk_wifi.md#_CPPv419bk_wifi_set_countryPK14wifi_country_t "bk_wifi_set_country") \- set country code
> > - [`bk_wifi_get_country()`](../api-reference/wifi/bk_wifi.md#_CPPv419bk_wifi_get_countryP14wifi_country_t "bk_wifi_get_country") \- get country code
> > - [`bk_wifi_send_raw()`](../api-reference/wifi/bk_wifi.md#_CPPv416bk_wifi_send_rawP7uint8_ti "bk_wifi_send_raw") \- send raw 802.11 frame
> > - [`bk_wifi_sta_start()`](../api-reference/wifi/bk_wifi.md#_CPPv417bk_wifi_sta_startv "bk_wifi_sta_start") \- start BK STA
> > - [`bk_wifi_sta_stop()`](../api-reference/wifi/bk_wifi.md#_CPPv416bk_wifi_sta_stopv "bk_wifi_sta_stop") \- stop BK STA
> > - [`bk_wifi_sta_set_config()`](../api-reference/wifi/bk_wifi.md#_CPPv422bk_wifi_sta_set_configPK17wifi_sta_config_t "bk_wifi_sta_set_config") \- set **basic** configurations BK STA, such as SSID etc
> > - [`bk_wifi_sta_get_config()`](../api-reference/wifi/bk_wifi.md#_CPPv422bk_wifi_sta_get_configP17wifi_sta_config_t "bk_wifi_sta_get_config") \- get basic configuration of BK STA
> > - [`bk_wifi_sta_get_link_status()`](../api-reference/wifi/bk_wifi.md#_CPPv427bk_wifi_sta_get_link_statusP18wifi_link_status_t "bk_wifi_sta_get_link_status") \- get link status of BK STA
> > - [`bk_wifi_sta_get_mac()`](../api-reference/wifi/bk_wifi.md#_CPPv419bk_wifi_sta_get_macP7uint8_t "bk_wifi_sta_get_mac") \- get STA MAC address
> > - [`bk_wifi_ap_start()`](../api-reference/wifi/bk_wifi.md#_CPPv416bk_wifi_ap_startv "bk_wifi_ap_start") \- start BK AP
> > - [`bk_wifi_ap_stop()`](../api-reference/wifi/bk_wifi.md#_CPPv415bk_wifi_ap_stopv "bk_wifi_ap_stop") \- stop BK AP
> > - [`bk_wifi_ap_set_config()`](../api-reference/wifi/bk_wifi.md#_CPPv421bk_wifi_ap_set_configPK16wifi_ap_config_t "bk_wifi_ap_set_config") \- set the **basic** configuration of BK AP, such as SSID etc
> > - [`bk_wifi_ap_get_config()`](../api-reference/wifi/bk_wifi.md#_CPPv421bk_wifi_ap_get_configP16wifi_ap_config_t "bk_wifi_ap_get_config") \- get the basic configuration of BK AP
> > - [`bk_wifi_ap_get_mac()`](../api-reference/wifi/bk_wifi.md#_CPPv418bk_wifi_ap_get_macP7uint8_t "bk_wifi_ap_get_mac") \- get AP MAC address
> > - [`bk_wifi_monitor_start()`](../api-reference/wifi/bk_wifi.md#_CPPv421bk_wifi_monitor_startv "bk_wifi_monitor_start") \- start the monitor
> > - [`bk_wifi_monitor_stop()`](../api-reference/wifi/bk_wifi.md#_CPPv420bk_wifi_monitor_stopv "bk_wifi_monitor_stop") \- stop the monitor
> > - [`bk_wifi_monitor_set_config()`](../api-reference/wifi/bk_wifi.md#_CPPv426bk_wifi_monitor_set_configPK21wifi_monitor_config_t "bk_wifi_monitor_set_config") \- set **basic** configuration of the monitor
> > - [`bk_wifi_monitor_get_config()`](../api-reference/wifi/bk_wifi.md#_CPPv426bk_wifi_monitor_get_configP21wifi_monitor_config_t "bk_wifi_monitor_get_config") \- get basic configuration of the monitor
> > - [`bk_wifi_monitor_register_cb()`](../api-reference/wifi/bk_wifi.md#_CPPv427bk_wifi_monitor_register_cbK17wifi_monitor_cb_t "bk_wifi_monitor_register_cb") \- register monitor callback function
> > - [`bk_wifi_monitor_set_channel()`](../api-reference/wifi/bk_wifi.md#_CPPv427bk_wifi_monitor_set_channelPK14wifi_channel_t "bk_wifi_monitor_set_channel") \- set the channel of monitor
> > - `bk_wifi_scan_register_cb()` \- register scan callback function
> > - [`bk_wifi_scan_start()`](../api-reference/wifi/bk_wifi.md#_CPPv418bk_wifi_scan_startPK18wifi_scan_config_t "bk_wifi_scan_start") \- start the scan
> > - [`bk_wifi_scan_stop()`](../api-reference/wifi/bk_wifi.md#_CPPv417bk_wifi_scan_stopv "bk_wifi_scan_stop") \- stop the scan
> > - [`bk_wifi_scan_get_result()`](../api-reference/wifi/bk_wifi.md#_CPPv423bk_wifi_scan_get_resultP18wifi_scan_result_t "bk_wifi_scan_get_result") \- get the scan result
> > - [`bk_wifi_scan_dump_result()`](../api-reference/wifi/bk_wifi.md#_CPPv424bk_wifi_scan_dump_resultPK18wifi_scan_result_t "bk_wifi_scan_dump_result") \- dump the scan result
> > - [`bk_wifi_scan_free_result()`](../api-reference/wifi/bk_wifi.md#_CPPv424bk_wifi_scan_free_resultP18wifi_scan_result_t "bk_wifi_scan_free_result") \- dump the scan result
> > - [`bk_wifi_filter_set_config()`](../api-reference/wifi/bk_wifi.md#_CPPv425bk_wifi_filter_set_configPK20wifi_filter_config_t "bk_wifi_filter_set_config") \- set filter configuration
> > - [`bk_wifi_filter_register_cb()`](../api-reference/wifi/bk_wifi.md#_CPPv426bk_wifi_filter_register_cbK16wifi_filter_cb_t "bk_wifi_filter_register_cb") \- register the filter callback function

<a id="ble"></a>

## BLE

<a id="driver"></a>

## Driver

The driver architecture has been redesigned:

> - The driver has been divided to 3 layers, the Driver layer, HAL layer and SoC Layer.
> - Some driver of the peripherals are re-implemented based on the new driver architecture, such as ADC etc.

<a id="adc"></a>

### ADC

ADC are re-designed in this release, here are the new ADC APIs:

> - [`bk_adc_driver_init()`](../api-reference/peripheral/bk_adc.md#_CPPv418bk_adc_driver_initv "bk_adc_driver_init")
> - `bk_adc_aquire()`
> - [`bk_adc_release()`](../api-reference/peripheral/bk_adc.md#_CPPv414bk_adc_releasev "bk_adc_release")
> - [`bk_adc_driver_deinit()`](../api-reference/peripheral/bk_adc.md#_CPPv420bk_adc_driver_deinitv "bk_adc_driver_deinit")
> - [`bk_adc_init()`](../api-reference/peripheral/bk_adc.md#_CPPv411bk_adc_init10adc_chan_t "bk_adc_init")
> - [`bk_adc_deinit()`](../api-reference/peripheral/bk_adc.md#_CPPv413bk_adc_deinit10adc_chan_t "bk_adc_deinit")
> - [`bk_adc_start()`](../api-reference/peripheral/bk_adc.md#_CPPv412bk_adc_startv "bk_adc_start")
> - [`bk_adc_stop()`](../api-reference/peripheral/bk_adc.md#_CPPv411bk_adc_stopv "bk_adc_stop")
> - [`bk_adc_read_raw()`](../api-reference/peripheral/bk_adc.md#_CPPv415bk_adc_read_rawP8uint16_t8uint32_t8uint32_t "bk_adc_read_raw")
> - [`bk_adc_read()`](../api-reference/peripheral/bk_adc.md#_CPPv411bk_adc_readP8uint16_t8uint32_t "bk_adc_read")
> - [`bk_adc_register_isr()`](../api-reference/peripheral/bk_adc.md#_CPPv419bk_adc_register_isr9adc_isr_t8uint32_t "bk_adc_register_isr")
> - [`bk_adc_set_clk()`](../api-reference/peripheral/bk_adc.md#_CPPv414bk_adc_set_clk13adc_src_clk_t8uint32_t "bk_adc_set_clk")
> - [`bk_adc_set_channel()`](../api-reference/peripheral/bk_adc.md#_CPPv418bk_adc_set_channel10adc_chan_t "bk_adc_set_channel")
> - [`bk_adc_set_sample_rate()`](../api-reference/peripheral/bk_adc.md#_CPPv422bk_adc_set_sample_rate8uint32_t "bk_adc_set_sample_rate")
> - [`bk_adc_set_filter()`](../api-reference/peripheral/bk_adc.md#_CPPv417bk_adc_set_filter8uint32_t "bk_adc_set_filter")
> - [`bk_adc_set_steady_time()`](../api-reference/peripheral/bk_adc.md#_CPPv422bk_adc_set_steady_time8uint32_t "bk_adc_set_steady_time")
> - [`bk_adc_set_sample_cnt()`](../api-reference/peripheral/bk_adc.md#_CPPv421bk_adc_set_sample_cnt8uint32_t "bk_adc_set_sample_cnt")
> - `bk_adc_enable_saturate()`
> - `bk_adc_disable_saturate()`
> - `bk_adc_set_saturate()`
> - [`bk_adc_get_saturate()`](../api-reference/peripheral/bk_adc.md#_CPPv419bk_adc_get_saturateP19adc_saturate_mode_t "bk_adc_get_saturate")
> - [`bk_adc_set_config()`](../api-reference/peripheral/bk_adc.md#_CPPv417bk_adc_set_configP12adc_config_t "bk_adc_set_config")
> - [`bk_adc_set_mode()`](../api-reference/peripheral/bk_adc.md#_CPPv415bk_adc_set_mode10adc_mode_t "bk_adc_set_mode")
> - [`bk_adc_get_mode()`](../api-reference/peripheral/bk_adc.md#_CPPv415bk_adc_get_modev "bk_adc_get_mode")

<a id="gpio"></a>

### GPIO

GPIO are re-designed in this release, here are the new GPIO APIs:

> - [`bk_gpio_driver_init()`](../api-reference/peripheral/bk_gpio.md#_CPPv419bk_gpio_driver_initv "bk_gpio_driver_init")
> - [`bk_gpio_driver_deinit()`](../api-reference/peripheral/bk_gpio.md#_CPPv421bk_gpio_driver_deinitv "bk_gpio_driver_deinit")
> - [`bk_gpio_enable_output()`](../api-reference/peripheral/bk_gpio.md#_CPPv421bk_gpio_enable_output9gpio_id_t "bk_gpio_enable_output")
> - [`bk_gpio_disable_output()`](../api-reference/peripheral/bk_gpio.md#_CPPv422bk_gpio_disable_output9gpio_id_t "bk_gpio_disable_output")
> - [`bk_gpio_enable_input()`](../api-reference/peripheral/bk_gpio.md#_CPPv420bk_gpio_enable_input9gpio_id_t "bk_gpio_enable_input")
> - [`bk_gpio_disable_input()`](../api-reference/peripheral/bk_gpio.md#_CPPv421bk_gpio_disable_input9gpio_id_t "bk_gpio_disable_input")
> - [`bk_gpio_enable_pull()`](../api-reference/peripheral/bk_gpio.md#_CPPv419bk_gpio_enable_pull9gpio_id_t "bk_gpio_enable_pull")
> - [`bk_gpio_disable_pull()`](../api-reference/peripheral/bk_gpio.md#_CPPv420bk_gpio_disable_pull9gpio_id_t "bk_gpio_disable_pull")
> - [`bk_gpio_pull_up()`](../api-reference/peripheral/bk_gpio.md#_CPPv415bk_gpio_pull_up9gpio_id_t "bk_gpio_pull_up")
> - [`bk_gpio_pull_down()`](../api-reference/peripheral/bk_gpio.md#_CPPv417bk_gpio_pull_down9gpio_id_t "bk_gpio_pull_down")
> - [`bk_gpio_set_output_high()`](../api-reference/peripheral/bk_gpio.md#_CPPv423bk_gpio_set_output_high9gpio_id_t "bk_gpio_set_output_high")
> - [`bk_gpio_set_output_low()`](../api-reference/peripheral/bk_gpio.md#_CPPv422bk_gpio_set_output_low9gpio_id_t "bk_gpio_set_output_low")
> - [`bk_gpio_get_input()`](../api-reference/peripheral/bk_gpio.md#_CPPv417bk_gpio_get_input9gpio_id_t "bk_gpio_get_input")
> - [`bk_gpio_set_config()`](../api-reference/peripheral/bk_gpio.md#_CPPv418bk_gpio_set_config9gpio_id_tPK13gpio_config_t "bk_gpio_set_config")
> - [`bk_gpio_register_isr()`](../api-reference/peripheral/bk_gpio.md#_CPPv420bk_gpio_register_isr9gpio_id_t10gpio_isr_t "bk_gpio_register_isr")
> - [`bk_gpio_enable_interrupt()`](../api-reference/peripheral/bk_gpio.md#_CPPv424bk_gpio_enable_interrupt9gpio_id_t "bk_gpio_enable_interrupt")
> - [`bk_gpio_disable_interrupt()`](../api-reference/peripheral/bk_gpio.md#_CPPv425bk_gpio_disable_interrupt9gpio_id_t "bk_gpio_disable_interrupt")
> - [`bk_gpio_set_interrupt_type()`](../api-reference/peripheral/bk_gpio.md#_CPPv426bk_gpio_set_interrupt_type9gpio_id_t15gpio_int_type_t "bk_gpio_set_interrupt_type")

<a id="pwm"></a>

### PWM

PWM are re-designed in this release, here are the new PWM APIs:

> - [`bk_pwm_driver_init()`](../api-reference/peripheral/bk_pwm.md#_CPPv418bk_pwm_driver_initv "bk_pwm_driver_init")
> - [`bk_pwm_driver_deinit()`](../api-reference/peripheral/bk_pwm.md#_CPPv420bk_pwm_driver_deinitv "bk_pwm_driver_deinit")
> - [`bk_pwm_init()`](../api-reference/peripheral/bk_pwm.md#_CPPv411bk_pwm_init10pwm_chan_tPK17pwm_init_config_t "bk_pwm_init")
> - [`bk_pwm_deinit()`](../api-reference/peripheral/bk_pwm.md#_CPPv413bk_pwm_deinit10pwm_chan_t "bk_pwm_deinit")
> - `bk_pwm_set_duty_period()`
> - [`bk_pwm_start()`](../api-reference/peripheral/bk_pwm.md#_CPPv412bk_pwm_start10pwm_chan_t "bk_pwm_start")
> - [`bk_pwm_stop()`](../api-reference/peripheral/bk_pwm.md#_CPPv411bk_pwm_stop10pwm_chan_t "bk_pwm_stop")
> - [`bk_pwm_set_init_signal_low()`](../api-reference/peripheral/bk_pwm.md#_CPPv426bk_pwm_set_init_signal_low10pwm_chan_t "bk_pwm_set_init_signal_low")
> - [`bk_pwm_set_init_signal_high()`](../api-reference/peripheral/bk_pwm.md#_CPPv427bk_pwm_set_init_signal_high10pwm_chan_t "bk_pwm_set_init_signal_high")
> - [`bk_pwm_register_isr()`](../api-reference/peripheral/bk_pwm.md#_CPPv419bk_pwm_register_isr10pwm_chan_t9pwm_isr_t "bk_pwm_register_isr")
> - [`bk_pwm_enable_interrupt()`](../api-reference/peripheral/bk_pwm.md#_CPPv423bk_pwm_enable_interrupt10pwm_chan_t "bk_pwm_enable_interrupt")
> - [`bk_pwm_disable_interrupt()`](../api-reference/peripheral/bk_pwm.md#_CPPv424bk_pwm_disable_interrupt10pwm_chan_t "bk_pwm_disable_interrupt")
> - [`bk_pwm_group_init()`](../api-reference/peripheral/bk_pwm.md#_CPPv417bk_pwm_group_initPK23pwm_group_init_config_tP11pwm_group_t "bk_pwm_group_init")
> - [`bk_pwm_group_deinit()`](../api-reference/peripheral/bk_pwm.md#_CPPv419bk_pwm_group_deinit11pwm_group_t "bk_pwm_group_deinit")
> - [`bk_pwm_group_start()`](../api-reference/peripheral/bk_pwm.md#_CPPv418bk_pwm_group_start11pwm_group_t "bk_pwm_group_start")
> - [`bk_pwm_group_stop()`](../api-reference/peripheral/bk_pwm.md#_CPPv417bk_pwm_group_stop11pwm_group_t "bk_pwm_group_stop")
> - [`bk_pwm_capture_init()`](../api-reference/peripheral/bk_pwm.md#_CPPv419bk_pwm_capture_init10pwm_chan_tPK25pwm_capture_init_config_t "bk_pwm_capture_init")
> - [`bk_pwm_capture_deinit()`](../api-reference/peripheral/bk_pwm.md#_CPPv421bk_pwm_capture_deinit10pwm_chan_t "bk_pwm_capture_deinit")
> - [`bk_pwm_capture_start()`](../api-reference/peripheral/bk_pwm.md#_CPPv420bk_pwm_capture_start10pwm_chan_t "bk_pwm_capture_start")
> - [`bk_pwm_capture_stop()`](../api-reference/peripheral/bk_pwm.md#_CPPv419bk_pwm_capture_stop10pwm_chan_t "bk_pwm_capture_stop")
> - [`bk_pwm_capture_get_value()`](../api-reference/peripheral/bk_pwm.md#_CPPv424bk_pwm_capture_get_value10pwm_chan_t "bk_pwm_capture_get_value")

<a id="dma"></a>

### DMA

DMA are re-designed in this release, here are the new DMA APIs:

> - [`bk_dma_driver_init()`](../api-reference/peripheral/bk_dma.md#_CPPv418bk_dma_driver_initv "bk_dma_driver_init")
> - [`bk_dma_driver_deinit()`](../api-reference/peripheral/bk_dma.md#_CPPv420bk_dma_driver_deinitv "bk_dma_driver_deinit")
> - [`bk_dma_init()`](../api-reference/peripheral/bk_dma.md#_CPPv411bk_dma_init8dma_id_tPK12dma_config_t "bk_dma_init")
> - [`bk_dma_deinit()`](../api-reference/peripheral/bk_dma.md#_CPPv413bk_dma_deinit8dma_id_t "bk_dma_deinit")
> - [`bk_dma_start()`](../api-reference/peripheral/bk_dma.md#_CPPv412bk_dma_start8dma_id_t "bk_dma_start")
> - [`bk_dma_stop()`](../api-reference/peripheral/bk_dma.md#_CPPv411bk_dma_stop8dma_id_t "bk_dma_stop")
> - [`bk_dma_write()`](../api-reference/peripheral/bk_dma.md#_CPPv412bk_dma_write8dma_id_tPK7uint8_t8uint32_t "bk_dma_write")
> - [`bk_dma_read()`](../api-reference/peripheral/bk_dma.md#_CPPv411bk_dma_read8dma_id_tP7uint8_t8uint32_t "bk_dma_read")
> - [`bk_dma_enable_finish_interrupt()`](../api-reference/peripheral/bk_dma.md#_CPPv430bk_dma_enable_finish_interrupt8dma_id_t "bk_dma_enable_finish_interrupt")
> - [`bk_dma_disable_finish_interrupt()`](../api-reference/peripheral/bk_dma.md#_CPPv431bk_dma_disable_finish_interrupt8dma_id_t "bk_dma_disable_finish_interrupt")
> - [`bk_dma_enable_half_finish_interrupt()`](../api-reference/peripheral/bk_dma.md#_CPPv435bk_dma_enable_half_finish_interrupt8dma_id_t "bk_dma_enable_half_finish_interrupt")
> - [`bk_dma_disable_half_finish_interrupt()`](../api-reference/peripheral/bk_dma.md#_CPPv436bk_dma_disable_half_finish_interrupt8dma_id_t "bk_dma_disable_half_finish_interrupt")
> - [`bk_dma_register_isr()`](../api-reference/peripheral/bk_dma.md#_CPPv419bk_dma_register_isr8dma_id_t9dma_isr_t9dma_isr_t "bk_dma_register_isr")
> - [`bk_dma_set_transfer_len()`](../api-reference/peripheral/bk_dma.md#_CPPv423bk_dma_set_transfer_len8dma_id_t8uint32_t "bk_dma_set_transfer_len")
> - [`bk_dma_set_src_addr()`](../api-reference/peripheral/bk_dma.md#_CPPv419bk_dma_set_src_addr8dma_id_t8uint32_t8uint32_t "bk_dma_set_src_addr")
> - [`bk_dma_set_dest_addr()`](../api-reference/peripheral/bk_dma.md#_CPPv420bk_dma_set_dest_addr8dma_id_t8uint32_t8uint32_t "bk_dma_set_dest_addr")
> - [`bk_dma_get_remain_len()`](../api-reference/peripheral/bk_dma.md#_CPPv421bk_dma_get_remain_len8dma_id_t "bk_dma_get_remain_len")

<a id="uart"></a>

### UART

UART are re-designed in this release, here are the new UART APIs:

> - [`bk_uart_driver_init()`](../api-reference/peripheral/bk_uart.md#_CPPv419bk_uart_driver_initv "bk_uart_driver_init")
> - [`bk_uart_driver_deinit()`](../api-reference/peripheral/bk_uart.md#_CPPv421bk_uart_driver_deinitv "bk_uart_driver_deinit")
> - [`bk_uart_init()`](../api-reference/peripheral/bk_uart.md#_CPPv412bk_uart_init9uart_id_tPK13uart_config_t "bk_uart_init")
> - [`bk_uart_deinit()`](../api-reference/peripheral/bk_uart.md#_CPPv414bk_uart_deinit9uart_id_t "bk_uart_deinit")
> - [`bk_uart_set_baud_rate()`](../api-reference/peripheral/bk_uart.md#_CPPv421bk_uart_set_baud_rate9uart_id_t8uint32_t "bk_uart_set_baud_rate")
> - [`bk_uart_set_data_bits()`](../api-reference/peripheral/bk_uart.md#_CPPv421bk_uart_set_data_bits9uart_id_t16uart_data_bits_t "bk_uart_set_data_bits")
> - [`bk_uart_set_stop_bits()`](../api-reference/peripheral/bk_uart.md#_CPPv421bk_uart_set_stop_bits9uart_id_t16uart_stop_bits_t "bk_uart_set_stop_bits")
> - [`bk_uart_set_parity()`](../api-reference/peripheral/bk_uart.md#_CPPv418bk_uart_set_parity9uart_id_t13uart_parity_t "bk_uart_set_parity")
> - [`bk_uart_set_hw_flow_ctrl()`](../api-reference/peripheral/bk_uart.md#_CPPv424bk_uart_set_hw_flow_ctrl9uart_id_t7uint8_t "bk_uart_set_hw_flow_ctrl")
> - [`bk_uart_set_rx_full_threshold()`](../api-reference/peripheral/bk_uart.md#_CPPv429bk_uart_set_rx_full_threshold9uart_id_t7uint8_t "bk_uart_set_rx_full_threshold")
> - [`bk_uart_set_tx_empty_threshold()`](../api-reference/peripheral/bk_uart.md#_CPPv430bk_uart_set_tx_empty_threshold9uart_id_t7uint8_t "bk_uart_set_tx_empty_threshold")
> - [`bk_uart_set_rx_timeout()`](../api-reference/peripheral/bk_uart.md#_CPPv422bk_uart_set_rx_timeout9uart_id_t26uart_rx_stop_detect_time_t "bk_uart_set_rx_timeout")
> - [`bk_uart_disable_hw_flow_ctrl()`](../api-reference/peripheral/bk_uart.md#_CPPv428bk_uart_disable_hw_flow_ctrl9uart_id_t "bk_uart_disable_hw_flow_ctrl")
> - [`bk_uart_enable_tx_interrupt()`](../api-reference/peripheral/bk_uart.md#_CPPv427bk_uart_enable_tx_interrupt9uart_id_t "bk_uart_enable_tx_interrupt")
> - [`bk_uart_disable_tx_interrupt()`](../api-reference/peripheral/bk_uart.md#_CPPv428bk_uart_disable_tx_interrupt9uart_id_t "bk_uart_disable_tx_interrupt")
> - [`bk_uart_enable_rx_interrupt()`](../api-reference/peripheral/bk_uart.md#_CPPv427bk_uart_enable_rx_interrupt9uart_id_t "bk_uart_enable_rx_interrupt")
> - [`bk_uart_disable_rx_interrupt()`](../api-reference/peripheral/bk_uart.md#_CPPv428bk_uart_disable_rx_interrupt9uart_id_t "bk_uart_disable_rx_interrupt")
> - [`bk_uart_register_rx_isr()`](../api-reference/peripheral/bk_uart.md#_CPPv423bk_uart_register_rx_isr9uart_id_t10uart_isr_tPv "bk_uart_register_rx_isr")
> - [`bk_uart_register_tx_isr()`](../api-reference/peripheral/bk_uart.md#_CPPv423bk_uart_register_tx_isr9uart_id_t10uart_isr_tPv "bk_uart_register_tx_isr")
> - [`bk_uart_write_bytes()`](../api-reference/peripheral/bk_uart.md#_CPPv419bk_uart_write_bytes9uart_id_tPKv8uint32_t "bk_uart_write_bytes")
> - [`bk_uart_read_bytes()`](../api-reference/peripheral/bk_uart.md#_CPPv418bk_uart_read_bytes9uart_id_tPv8uint32_t8uint32_t "bk_uart_read_bytes")
> - [`bk_uart_disable_rx()`](../api-reference/peripheral/bk_uart.md#_CPPv418bk_uart_disable_rx9uart_id_t "bk_uart_disable_rx")
> - [`bk_uart_disable_tx()`](../api-reference/peripheral/bk_uart.md#_CPPv418bk_uart_disable_tx9uart_id_t "bk_uart_disable_tx")
> - [`bk_uart_enable_sw_fifo()`](../api-reference/peripheral/bk_uart.md#_CPPv422bk_uart_enable_sw_fifo9uart_id_t "bk_uart_enable_sw_fifo")
> - [`bk_uart_disable_sw_fifo()`](../api-reference/peripheral/bk_uart.md#_CPPv423bk_uart_disable_sw_fifo9uart_id_t "bk_uart_disable_sw_fifo")

<a id="spi"></a>

### SPI

SPI are re-designed in this release, here are the new SPI APIs:

> - [`bk_spi_driver_init()`](../api-reference/peripheral/bk_spi.md#_CPPv418bk_spi_driver_initv "bk_spi_driver_init")
> - [`bk_spi_driver_deinit()`](../api-reference/peripheral/bk_spi.md#_CPPv420bk_spi_driver_deinitv "bk_spi_driver_deinit")
> - [`bk_spi_init()`](../api-reference/peripheral/bk_spi.md#_CPPv411bk_spi_init8spi_id_tPK12spi_config_t "bk_spi_init")
> - [`bk_spi_deinit()`](../api-reference/peripheral/bk_spi.md#_CPPv413bk_spi_deinit8spi_id_t "bk_spi_deinit")
> - [`bk_spi_set_mode()`](../api-reference/peripheral/bk_spi.md#_CPPv415bk_spi_set_mode8spi_id_t10spi_mode_t "bk_spi_set_mode")
> - [`bk_spi_set_bit_width()`](../api-reference/peripheral/bk_spi.md#_CPPv420bk_spi_set_bit_width8spi_id_t15spi_bit_width_t "bk_spi_set_bit_width")
> - [`bk_spi_set_wire_mode()`](../api-reference/peripheral/bk_spi.md#_CPPv420bk_spi_set_wire_mode8spi_id_t15spi_wire_mode_t "bk_spi_set_wire_mode")
> - [`bk_spi_set_baud_rate()`](../api-reference/peripheral/bk_spi.md#_CPPv420bk_spi_set_baud_rate8spi_id_t8uint32_t "bk_spi_set_baud_rate")
> - [`bk_spi_set_bit_order()`](../api-reference/peripheral/bk_spi.md#_CPPv420bk_spi_set_bit_order8spi_id_t15spi_bit_order_t "bk_spi_set_bit_order")
> - [`bk_spi_register_rx_isr()`](../api-reference/peripheral/bk_spi.md#_CPPv422bk_spi_register_rx_isr8spi_id_t9spi_isr_tPv "bk_spi_register_rx_isr")
> - [`bk_spi_register_tx_finish_isr()`](../api-reference/peripheral/bk_spi.md#_CPPv429bk_spi_register_tx_finish_isr8spi_id_t9spi_isr_tPv "bk_spi_register_tx_finish_isr")
> - [`bk_spi_write_bytes()`](../api-reference/peripheral/bk_spi.md#_CPPv418bk_spi_write_bytes8spi_id_tPKv8uint32_t "bk_spi_write_bytes")
> - [`bk_spi_read_bytes()`](../api-reference/peripheral/bk_spi.md#_CPPv417bk_spi_read_bytes8spi_id_tPv8uint32_t "bk_spi_read_bytes")
> - [`bk_spi_transmit()`](../api-reference/peripheral/bk_spi.md#_CPPv415bk_spi_transmit8spi_id_tPKv8uint32_tPv8uint32_t "bk_spi_transmit")
> - `bk_spi_dma_write_bytes()`
> - `bk_spi_dma_read_bytes()`
> - `bk_spi_dma_transmit()`

<a id="qspi"></a>

### QSPI

QSPI driver are re-designed in this release, here are the new QSPI APIs:

> - [`bk_qspi_driver_init()`](../api-reference/peripheral/bk_qspi.md#_CPPv419bk_qspi_driver_initv "bk_qspi_driver_init")
> - [`bk_qspi_driver_deinit()`](../api-reference/peripheral/bk_qspi.md#_CPPv421bk_qspi_driver_deinitv "bk_qspi_driver_deinit")
> - [`bk_qspi_init()`](../api-reference/peripheral/bk_qspi.md#_CPPv412bk_qspi_initPK13qspi_config_t "bk_qspi_init")
> - [`bk_qspi_deinit()`](../api-reference/peripheral/bk_qspi.md#_CPPv414bk_qspi_deinitv "bk_qspi_deinit")
> - [`bk_qspi_command()`](../api-reference/peripheral/bk_qspi.md#_CPPv415bk_qspi_commandPK10qspi_cmd_t "bk_qspi_command")
> - [`bk_qspi_write()`](../api-reference/peripheral/bk_qspi.md#_CPPv413bk_qspi_writePKv8uint32_t "bk_qspi_write")
> - [`bk_qspi_read()`](../api-reference/peripheral/bk_qspi.md#_CPPv412bk_qspi_readPv8uint32_t "bk_qspi_read")
> - [`bk_qspi_register_tx_isr()`](../api-reference/peripheral/bk_qspi.md#_CPPv423bk_qspi_register_tx_isr10qspi_isr_tPv "bk_qspi_register_tx_isr")
> - [`bk_qspi_register_rx_isr()`](../api-reference/peripheral/bk_qspi.md#_CPPv423bk_qspi_register_rx_isr10qspi_isr_tPv "bk_qspi_register_rx_isr")
> - [`bk_qspi_psram_init()`](../api-reference/peripheral/bk_qspi.md#_CPPv418bk_qspi_psram_initv "bk_qspi_psram_init")
> - [`bk_qspi_psram_deinit()`](../api-reference/peripheral/bk_qspi.md#_CPPv420bk_qspi_psram_deinitv "bk_qspi_psram_deinit")
> - [`bk_qspi_psram_enter_quad_mode()`](../api-reference/peripheral/bk_qspi.md#_CPPv429bk_qspi_psram_enter_quad_modev "bk_qspi_psram_enter_quad_mode")
> - [`bk_qspi_psram_exit_quad_mode()`](../api-reference/peripheral/bk_qspi.md#_CPPv428bk_qspi_psram_exit_quad_modev "bk_qspi_psram_exit_quad_mode")
> - [`bk_qspi_psram_quad_write()`](../api-reference/peripheral/bk_qspi.md#_CPPv424bk_qspi_psram_quad_writev "bk_qspi_psram_quad_write")
> - [`bk_qspi_psram_single_write()`](../api-reference/peripheral/bk_qspi.md#_CPPv426bk_qspi_psram_single_writev "bk_qspi_psram_single_write")
> - [`bk_qspi_psram_quad_read()`](../api-reference/peripheral/bk_qspi.md#_CPPv423bk_qspi_psram_quad_readv "bk_qspi_psram_quad_read")
> - [`bk_qspi_psram_single_read()`](../api-reference/peripheral/bk_qspi.md#_CPPv425bk_qspi_psram_single_readv "bk_qspi_psram_single_read")
> - [`bk_qspi_psram_write()`](../api-reference/peripheral/bk_qspi.md#_CPPv419bk_qspi_psram_write8uint32_tPKv8uint32_t "bk_qspi_psram_write")
> - [`bk_qspi_psram_read()`](../api-reference/peripheral/bk_qspi.md#_CPPv418bk_qspi_psram_read8uint32_tPv8uint32_t "bk_qspi_psram_read")

<a id="timer"></a>

### Timer

Timer driver are re-designed in this release, here are the new Timer APIs:

> - [`bk_timer_driver_init()`](../api-reference/peripheral/bk_timer.md#_CPPv420bk_timer_driver_initv "bk_timer_driver_init")
> - [`bk_timer_driver_deinit()`](../api-reference/peripheral/bk_timer.md#_CPPv422bk_timer_driver_deinitv "bk_timer_driver_deinit")
> - [`bk_timer_start()`](../api-reference/peripheral/bk_timer.md#_CPPv414bk_timer_start10timer_id_t8uint32_t11timer_isr_t "bk_timer_start")
> - [`bk_timer_stop()`](../api-reference/peripheral/bk_timer.md#_CPPv413bk_timer_stop10timer_id_t "bk_timer_stop")
> - [`bk_timer_get_cnt()`](../api-reference/peripheral/bk_timer.md#_CPPv416bk_timer_get_cnt10timer_id_t "bk_timer_get_cnt")
> - [`bk_timer_enable()`](../api-reference/peripheral/bk_timer.md#_CPPv415bk_timer_enable10timer_id_t "bk_timer_enable")
> - [`bk_timer_disable()`](../api-reference/peripheral/bk_timer.md#_CPPv416bk_timer_disable10timer_id_t "bk_timer_disable")
> - [`bk_timer_get_period()`](../api-reference/peripheral/bk_timer.md#_CPPv419bk_timer_get_period10timer_id_t "bk_timer_get_period")

<a id="trng"></a>

### TRNG

TRNG driver are re-designed in this release, here are the new TRNG APIs:

> - [`bk_trng_driver_init()`](../api-reference/peripheral/bk_trng.md#_CPPv419bk_trng_driver_initv "bk_trng_driver_init")
> - [`bk_trng_driver_deinit()`](../api-reference/peripheral/bk_trng.md#_CPPv421bk_trng_driver_deinitv "bk_trng_driver_deinit")
> - [`bk_trng_start()`](../api-reference/peripheral/bk_trng.md#_CPPv413bk_trng_startv "bk_trng_start")
> - [`bk_trng_stop()`](../api-reference/peripheral/bk_trng.md#_CPPv412bk_trng_stopv "bk_trng_stop")
> - [`bk_rand()`](../api-reference/peripheral/bk_trng.md#_CPPv47bk_randv "bk_rand")

<a id="efuse"></a>

### EFUSE

Efuse driver are re-designed in this release, here are the new Efuse APIs:

> - [`bk_efuse_driver_init()`](../api-reference/peripheral/bk_efuse.md#_CPPv420bk_efuse_driver_initv "bk_efuse_driver_init")
> - [`bk_efuse_driver_deinit()`](../api-reference/peripheral/bk_efuse.md#_CPPv422bk_efuse_driver_deinitv "bk_efuse_driver_deinit")
> - `bk_efuse_write()`
> - `bk_efuse_read()`

<a id="mailbox"></a>

### MailBox

Mailbox driver are re-designed in this release, here are the new Mailbox APIs:

> - `mailbox_init()`
> - `mailbox_deinit()`
> - `mailbox_set_param()`
> - `mailbox_recv_callback_register()`
> - `mailbox_recv_callback_unregister()`
> - `mailbox_send()`

<a id="interrupt"></a>

### Interrupt

Interrupt control are re-designed in this release, here are the new Interrupt APIs:

> - [`bk_int_isr_register()`](../api-reference/peripheral/bk_interrupt.md#_CPPv419bk_int_isr_register13icu_int_src_t15int_group_isr_tPv "bk_int_isr_register")
> - [`bk_int_isr_unregister()`](../api-reference/peripheral/bk_interrupt.md#_CPPv421bk_int_isr_unregister13icu_int_src_t "bk_int_isr_unregister")
> - [`bk_int_set_priority()`](../api-reference/peripheral/bk_interrupt.md#_CPPv419bk_int_set_priority13icu_int_src_t8uint32_t "bk_int_set_priority")
> - [`bk_int_set_group()`](../api-reference/peripheral/bk_interrupt.md#_CPPv416bk_int_set_groupv "bk_int_set_group")
> - `bk_get_int_statis()`
> - `bk_dump_int_statis()`

<a id="watchdog"></a>

### Watchdog

Watchdog are re-designed in this release, here are the new Watchdog APIs:

> - [`bk_wdt_driver_init()`](../api-reference/peripheral/bk_wdt.md#_CPPv418bk_wdt_driver_initv "bk_wdt_driver_init")
> - [`bk_wdt_driver_deinit()`](../api-reference/peripheral/bk_wdt.md#_CPPv420bk_wdt_driver_deinitv "bk_wdt_driver_deinit")
> - [`bk_wdt_start()`](../api-reference/peripheral/bk_wdt.md#_CPPv412bk_wdt_start8uint32_t "bk_wdt_start")
> - [`bk_wdt_stop()`](../api-reference/peripheral/bk_wdt.md#_CPPv411bk_wdt_stopv "bk_wdt_stop")
> - [`bk_wdt_feed()`](../api-reference/peripheral/bk_wdt.md#_CPPv411bk_wdt_feedv "bk_wdt_feed")

<a id="build-system"></a>

## Build System

The legacy GNU Makefile build system has been removed and the CMake build system has been supported.

<a id="log"></a>

## Log

Following log APIs have been added:

> - BK\_LOGI
> - BK\_LOGD
> - BK\_LOGV

<a id="event"></a>

## Event

Following Event APIs have been added:

> - [`bk_event_register_cb()`](../api-reference/system/bk_event.md#_CPPv420bk_event_register_cb14event_module_ti10event_cb_tPv "bk_event_register_cb")
> - [`bk_event_unregister_cb()`](../api-reference/system/bk_event.md#_CPPv422bk_event_unregister_cb14event_module_ti10event_cb_t "bk_event_unregister_cb")
> - [`bk_event_post()`](../api-reference/system/bk_event.md#_CPPv413bk_event_post14event_module_tiPv6size_t8uint32_t "bk_event_post")

<a id="netif"></a>

## Netif

Following Netif APIs have been added:

> - [`bk_netif_init()`](../api-reference/tcpip/bk_netif.md#_CPPv413bk_netif_initv "bk_netif_init")
> - [`bk_netif_set_ip4_config()`](../api-reference/tcpip/bk_netif.md#_CPPv423bk_netif_set_ip4_config10netif_if_tPK18netif_ip4_config_t "bk_netif_set_ip4_config")
> - [`bk_netif_get_ip4_config()`](../api-reference/tcpip/bk_netif.md#_CPPv423bk_netif_get_ip4_config10netif_if_tP18netif_ip4_config_t "bk_netif_get_ip4_config")

<a id="documentation"></a>

## Documentation

New documentation framework has been added to this release.

<a id="examples"></a>

## Examples

Following examples has been added:

> - [hello world](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/get-started/hello_world)
> - [ADC](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/peripherals/adc)
> - [DMA](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/peripherals/dma)
> - [GPIO](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/peripherals/gpio)
> - [Interrupt](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/peripherals/icu)
> - [PWM](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/peripherals/pwm)
> - [SPI](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/peripherals/spi)
> - [Timer](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/peripherals/timer)
> - [Uart](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/peripherals/uart)
> - [Soft-AP](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/wifi/ap)
> - [Wi-Fi Scan](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/wifi/scan)
> - [Station](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/wifi/sta)
> - [Build System](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/build_system)
