---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_pmu.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-pmu"></a>

# DRV\_PMU

<a id="drv-pmu-api-status"></a>

## DRV\_PMU API Status

| API |
| --- |
| [`drv_pmu_initialise()`](#_CPPv418drv_pmu_initialisev "drv_pmu_initialise") |
| [`drv_pmu_reg_vusb_callback()`](#_CPPv425drv_pmu_reg_vusb_callback15pfunc_vusb_cb_tb "drv_pmu_reg_vusb_callback") |
| [`drv_pmu_reg_ana_callback()`](#_CPPv424drv_pmu_reg_ana_callback15pfunc_wkup_cb_tb "drv_pmu_reg_ana_callback") |
| [`drv_pmu_enable_mbist_check_bypass()`](#_CPPv433drv_pmu_enable_mbist_check_bypassb "drv_pmu_enable_mbist_check_bypass") |
| [`drv_pmu_select_aon_32k_source()`](#_CPPv429drv_pmu_select_aon_32k_source17drv_pmu_32k_src_e "drv_pmu_select_aon_32k_source") |
| [`drv_pmu_select_watchdog_dest()`](#_CPPv428drv_pmu_select_watchdog_dest17drv_pmu_wdt_dst_eb "drv_pmu_select_watchdog_dest") |
| [`drv_pmu_enable_usb_interrput()`](#_CPPv428drv_pmu_enable_usb_interrput21drv_pmu_usb_voltage_ebb "drv_pmu_enable_usb_interrput") |
| [`drv_pmu_enable_dlp_reset_chip()`](#_CPPv429drv_pmu_enable_dlp_reset_chipb "drv_pmu_enable_dlp_reset_chip") |
| [`drv_pmu_get_usb_level_active_state()`](#_CPPv434drv_pmu_get_usb_level_active_statev "drv_pmu_get_usb_level_active_state") |
| [`drv_pmu_cfg_wakeup_source()`](#_CPPv425drv_pmu_cfg_wakeup_source20drv_pmu_wakeup_src_eb "drv_pmu_cfg_wakeup_source") |
| [`drv_pmu_enable_ana_interrput()`](#_CPPv428drv_pmu_enable_ana_interrput8uint32_tbb "drv_pmu_enable_ana_interrput") |
| [`drv_pmu_cfg_dlp_pull()`](#_CPPv420drv_pmu_cfg_dlp_pullbb "drv_pmu_cfg_dlp_pull") |
| [`drv_pmu_cfg_dlp_driver_strength()`](#_CPPv431drv_pmu_cfg_dlp_driver_strength8uint32_t "drv_pmu_cfg_dlp_driver_strength") |
| [`drv_pmu_cfg_flash_sck_driver_strength()`](#_CPPv437drv_pmu_cfg_flash_sck_driver_strength8uint32_t "drv_pmu_cfg_flash_sck_driver_strength") |
| [`drv_pmu_halt_config()`](#_CPPv419drv_pmu_halt_configP14pmu_halt_cfg_t "drv_pmu_halt_config") |
| [`drv_pmu_enable_aon_timer_clk()`](#_CPPv428drv_pmu_enable_aon_timer_clkb "drv_pmu_enable_aon_timer_clk") |
| [`drv_pmu_set_retention_regbit()`](#_CPPv428drv_pmu_set_retention_regbit8uint32_t8uint32_t8uint32_t "drv_pmu_set_retention_regbit") |
| [`drv_pmu_get_retention_regbit()`](#_CPPv428drv_pmu_get_retention_regbit8uint32_t8uint32_t "drv_pmu_get_retention_regbit") |
| [`drv_pmu_set_retention_reg()`](#_CPPv425drv_pmu_set_retention_reg8uint32_t8uint32_t "drv_pmu_set_retention_reg") |
| [`drv_pmu_get_retention_reg()`](#_CPPv425drv_pmu_get_retention_reg8uint32_t "drv_pmu_get_retention_reg") |
| [`drv_pmu_set_rw_wakeup_req()`](#_CPPv425drv_pmu_set_rw_wakeup_reqb "drv_pmu_set_rw_wakeup_req") |
| [`drv_pmu_set_bt_iso_en()`](#_CPPv421drv_pmu_set_bt_iso_enb "drv_pmu_set_bt_iso_en") |
| [`drv_pmu_get_wakeup_deepsleep_source()`](#_CPPv435drv_pmu_get_wakeup_deepsleep_sourcev "drv_pmu_get_wakeup_deepsleep_source") |

<a id="drv-pmu-api-reference"></a>

## DRV\_PMU API Reference

<a id="header-file"></a>

### Header File

- [driver/pmu/drv\_pmu.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/pmu/drv_pmu.h)

<a id="functions"></a>

### Functions

<a id="_CPPv418drv_pmu_initialisev"></a>

<a id="_CPPv318drv_pmu_initialisev"></a> <a id="_CPPv218drv_pmu_initialisev"></a> <a id="drv_pmu_initialise__void"></a> <a id="group__PMU_1ga47b76d72c2ae7d57172677aec3985747"></a> int32\_t drv\_pmu\_initialise(void)
:   pmu driver initialise.

    pmu driver的初始化，主要是中断的注册，开机的时候调用一次

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425drv_pmu_reg_vusb_callback15pfunc_vusb_cb_tb"></a>

<a id="_CPPv325drv_pmu_reg_vusb_callback15pfunc_vusb_cb_tb"></a> <a id="_CPPv225drv_pmu_reg_vusb_callback15pfunc_vusb_cb_tb"></a> <a id="drv_pmu_reg_vusb_callback__pfunc_vusb_cb_t.b"></a> <a id="group__PMU_1ga5f7fb3c54d132cadc8ff25367caeea6f"></a> int32\_t drv\_pmu\_reg\_vusb\_callback([pfunc\_vusb\_cb\_t](#_CPPv415pfunc_vusb_cb_t "pfunc_vusb_cb_t") pfn\_cb, bool enable)
:   注册充电口的vusb中断.

    如果多个用户注册，只有最后一个是生效的

    参数:
    :   - **pfn\_cb** – **\[in\]** 注册的callback中断函数
        - **enable** – **\[in\]** true: 注册 false: 反注册

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424drv_pmu_reg_ana_callback15pfunc_wkup_cb_tb"></a>

<a id="_CPPv324drv_pmu_reg_ana_callback15pfunc_wkup_cb_tb"></a> <a id="_CPPv224drv_pmu_reg_ana_callback15pfunc_wkup_cb_tb"></a> <a id="drv_pmu_reg_ana_callback__pfunc_wkup_cb_t.b"></a> <a id="group__PMU_1ga3946a466facf6de35cbd659d24d214de"></a> int32\_t drv\_pmu\_reg\_ana\_callback([pfunc\_wkup\_cb\_t](#_CPPv415pfunc_wkup_cb_t "pfunc_wkup_cb_t") pfn\_cb, bool enable)
:   注册模拟部分的其他中断callback.

    如果多个用户注册，只有最后一个是生效的

    参数:
    :   - **pfn\_cb** – **\[in\]** 注册的callback中断函数
        - **enable** – **\[in\]** true: 注册 false: 反注册

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv433drv_pmu_enable_mbist_check_bypassb"></a>

<a id="_CPPv333drv_pmu_enable_mbist_check_bypassb"></a> <a id="_CPPv233drv_pmu_enable_mbist_check_bypassb"></a> <a id="drv_pmu_enable_mbist_check_bypass__b"></a> <a id="group__PMU_1ga91feae9ec53d4308a7da1f60e44e342b"></a> int32\_t drv\_pmu\_enable\_mbist\_check\_bypass(bool bypass)
:   enable Mbist memory check bypass or not.

    参数:
    :   **bypass** – **\[in\]** true: bypass false: not bypass(default)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv429drv_pmu_select_aon_32k_source17drv_pmu_32k_src_e"></a>

<a id="_CPPv329drv_pmu_select_aon_32k_source17drv_pmu_32k_src_e"></a> <a id="_CPPv229drv_pmu_select_aon_32k_source17drv_pmu_32k_src_e"></a> <a id="drv_pmu_select_aon_32k_source__drv_pmu_32k_src_e"></a> <a id="group__PMU_1gabf42b820435df1c44bcf509ba3d68ce0"></a> int32\_t drv\_pmu\_select\_aon\_32k\_source([drv\_pmu\_32k\_src\_e](#_CPPv417drv_pmu_32k_src_e "drv_pmu_32k_src_e") e\_src)
:   select aon 32k source.

    参数:
    :   **e\_src** – **\[in\]** see [drv\_pmu\_32k\_src\_e](#group__PMU_1ga2e084e0132308107f4229a9a249c4bc6)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv428drv_pmu_select_watchdog_dest17drv_pmu_wdt_dst_eb"></a>

<a id="_CPPv328drv_pmu_select_watchdog_dest17drv_pmu_wdt_dst_eb"></a> <a id="_CPPv228drv_pmu_select_watchdog_dest17drv_pmu_wdt_dst_eb"></a> <a id="drv_pmu_select_watchdog_dest__drv_pmu_wdt_dst_e.b"></a> <a id="group__PMU_1ga2c7cd25c4ae12acb0d0a6970e1d3a154"></a> int32\_t drv\_pmu\_select\_watchdog\_dest([drv\_pmu\_wdt\_dst\_e](#_CPPv417drv_pmu_wdt_dst_e "drv_pmu_wdt_dst_e") e\_wdt\_rst\_dst, bool permit)
:   select watch dog reset destionation.

    配置watchdog reset的时候reset哪些部分

    参数:
    :   - **e\_wdt\_rst\_dst** – **\[in\]** see drv\_pmu\_wdt\_dst\_e，枚举类型可以或起来一起传入
        - **permit** – **\[in\]** true: permit false: not permit

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv428drv_pmu_enable_usb_interrput21drv_pmu_usb_voltage_ebb"></a>

<a id="_CPPv328drv_pmu_enable_usb_interrput21drv_pmu_usb_voltage_ebb"></a> <a id="_CPPv228drv_pmu_enable_usb_interrput21drv_pmu_usb_voltage_ebb"></a> <a id="drv_pmu_enable_usb_interrput__drv_pmu_usb_voltage_e.b.b"></a> <a id="group__PMU_1ga07b45b580935bdaa1ce84198c4c9b03f"></a> int32\_t drv\_pmu\_enable\_usb\_interrput([drv\_pmu\_usb\_voltage\_e](#_CPPv421drv_pmu_usb_voltage_e "drv_pmu_usb_voltage_e") e\_vol, bool enable\_irq, bool irq\_lvl\_low)
:   config usb interrupt.

    配置充电口的中断电压选择

    参数:
    :   - **e\_vol** – **\[in\]** 选择的中断电压 see [drv\_pmu\_usb\_voltage\_e](#group__PMU_1gad78866aa534014b28133b3330736c2b4)
        - **enable\_irq** – **\[in\]** true: enable interrutp false: disable interrupt
        - **irq\_lvl\_low** – **\[in\]** true: generate interrrupt in low level false: generate interrrupt in high level

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv429drv_pmu_enable_dlp_reset_chipb"></a>

<a id="_CPPv329drv_pmu_enable_dlp_reset_chipb"></a> <a id="_CPPv229drv_pmu_enable_dlp_reset_chipb"></a> <a id="drv_pmu_enable_dlp_reset_chip__b"></a> <a id="group__PMU_1ga644db5c2497de88a54cdc290ce68d2bb"></a> int32\_t drv\_pmu\_enable\_dlp\_reset\_chip(bool en\_reset)
:   enable DLP reset chip or not.

    参数:
    :   **en\_reset** – **\[in\]** true: enable reset chip false: disable reset chip

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv434drv_pmu_get_usb_level_active_statev"></a>

<a id="_CPPv334drv_pmu_get_usb_level_active_statev"></a> <a id="_CPPv234drv_pmu_get_usb_level_active_statev"></a> <a id="drv_pmu_get_usb_level_active_state__void"></a> <a id="group__PMU_1gac8e7e44e383cced69a8beacd44be138c"></a> [drv\_pmu\_usb\_voltage\_e](#_CPPv421drv_pmu_usb_voltage_e "drv_pmu_usb_voltage_e") drv\_pmu\_get\_usb\_level\_active\_state(void)
:   get current usb voltage state

    返回:
    :   voltage state see [drv\_pmu\_usb\_voltage\_e](#group__PMU_1gad78866aa534014b28133b3330736c2b4)

<a id="_CPPv425drv_pmu_cfg_wakeup_source20drv_pmu_wakeup_src_eb"></a>

<a id="_CPPv325drv_pmu_cfg_wakeup_source20drv_pmu_wakeup_src_eb"></a> <a id="_CPPv225drv_pmu_cfg_wakeup_source20drv_pmu_wakeup_src_eb"></a> <a id="drv_pmu_cfg_wakeup_source__drv_pmu_wakeup_src_e.b"></a> <a id="group__PMU_1gad2d55e275ffcdc495b71f3f46f0ab333"></a> int32\_t drv\_pmu\_cfg\_wakeup\_source([drv\_pmu\_wakeup\_src\_e](#_CPPv420drv_pmu_wakeup_src_e "drv_pmu_wakeup_src_e") e\_src, bool enable\_wakeup)
:   config deep wakeup enable source.

    参数:
    :   - **e\_src** – **\[in\]** see [drv\_pmu\_wakeup\_src\_e](#group__PMU_1ga8a9610d9bebf1281c8051971a7a2f78a)
        - **enable\_wakeup** – **\[in\]** true: enable false: disable

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv428drv_pmu_enable_ana_interrput8uint32_tbb"></a>

<a id="_CPPv328drv_pmu_enable_ana_interrput8uint32_tbb"></a> <a id="_CPPv228drv_pmu_enable_ana_interrput8uint32_tbb"></a> <a id="drv_pmu_enable_ana_interrput__uint32_t.b.b"></a> <a id="group__PMU_1ga680941ac466fbc1b89a20d7da838b8ea"></a> int32\_t drv\_pmu\_enable\_ana\_interrput(uint32\_t ana\_idx, bool enable\_irq, bool irq\_lvl\_low)
:   config analog wakeup.

    模拟wakeup的中断配置

    参数:
    :   - **ana\_idx** – **\[in\]** analog wakeup index, 0 \~ 7, see @drv\_pmu\_ana\_src\_e
        - **enable\_irq** – **\[in\]** true: enable interrupt false: disable interrupt
        - **irq\_lvl\_low** – **\[in\]** true: generate interrrupt in low level false: generate interrrupt in high level

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420drv_pmu_cfg_dlp_pullbb"></a>

<a id="_CPPv320drv_pmu_cfg_dlp_pullbb"></a> <a id="_CPPv220drv_pmu_cfg_dlp_pullbb"></a> <a id="drv_pmu_cfg_dlp_pull__b.b"></a> <a id="group__PMU_1ga19810d9532bdef4e4387eb9002cc972f"></a> int32\_t drv\_pmu\_cfg\_dlp\_pull(bool pull\_en, bool pull\_down)
:   DLP pull config.

    参数:
    :   - **pull\_en** – **\[in\]** true: enable pull false: disable pull
        - **pull\_down** – **\[in\]** true: pull down false: pull up

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv431drv_pmu_cfg_dlp_driver_strength8uint32_t"></a>

<a id="_CPPv331drv_pmu_cfg_dlp_driver_strength8uint32_t"></a> <a id="_CPPv231drv_pmu_cfg_dlp_driver_strength8uint32_t"></a> <a id="drv_pmu_cfg_dlp_driver_strength__uint32_t"></a> <a id="group__PMU_1ga8e3e704895fcd2035e30eac946976c41"></a> int32\_t drv\_pmu\_cfg\_dlp\_driver\_strength(uint32\_t strenth)
:   配置DLP的驱动强度

    参数:
    :   **strenth** – **\[in\]** 驱动强度 0\~3 ,default\=0

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv437drv_pmu_cfg_flash_sck_driver_strength8uint32_t"></a>

<a id="_CPPv337drv_pmu_cfg_flash_sck_driver_strength8uint32_t"></a> <a id="_CPPv237drv_pmu_cfg_flash_sck_driver_strength8uint32_t"></a> <a id="drv_pmu_cfg_flash_sck_driver_strength__uint32_t"></a> <a id="group__PMU_1ga8c88816ddf9ac687a4f1dff4361f9b76"></a> int32\_t drv\_pmu\_cfg\_flash\_sck\_driver\_strength(uint32\_t strenth)
:   配置flash sck的驱动强度

    参数:
    :   **strenth** – **\[in\]** 驱动强度 0\~3 ,default\=0

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419drv_pmu_halt_configP14pmu_halt_cfg_t"></a>

<a id="_CPPv319drv_pmu_halt_configP14pmu_halt_cfg_t"></a> <a id="_CPPv219drv_pmu_halt_configP14pmu_halt_cfg_t"></a> <a id="drv_pmu_halt_config__pmu_halt_cfg_tP"></a> <a id="group__PMU_1gaf6c805f68241d0c6bf103eb77b1a920d"></a> int32\_t drv\_pmu\_halt\_config([pmu\_halt\_cfg\_t](#_CPPv414pmu_halt_cfg_t "pmu_halt_cfg_t") \*cfg)
:   drv\_pmu\_halt\_config brief description

    参数:
    :   **cfg** – **\[in\]** 指向halt config的指针，默认不配置时，该config对应的register默认为0

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv428drv_pmu_enable_aon_timer_clkb"></a>

<a id="_CPPv328drv_pmu_enable_aon_timer_clkb"></a> <a id="_CPPv228drv_pmu_enable_aon_timer_clkb"></a> <a id="drv_pmu_enable_aon_timer_clk__b"></a> <a id="group__PMU_1ga008f01249f66d516be0a7a09e5a0ab91"></a> int32\_t drv\_pmu\_enable\_aon\_timer\_clk(bool enable)
:   enable or disable aon timer clock.

    控制AON timer的clock是否打开

    参数:
    :   **enable** – **\[in\]** true: 打开clock false: 关闭clock

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv428drv_pmu_set_retention_regbit8uint32_t8uint32_t8uint32_t"></a>

<a id="_CPPv328drv_pmu_set_retention_regbit8uint32_t8uint32_t8uint32_t"></a> <a id="_CPPv228drv_pmu_set_retention_regbit8uint32_t8uint32_t8uint32_t"></a> <a id="drv_pmu_set_retention_regbit__uint32_t.uint32_t.uint32_t"></a> <a id="group__PMU_1gaae8c281cc2f4e2d8eae34200fa4d5876"></a> int32\_t drv\_pmu\_set\_retention\_regbit(uint32\_t reg\_index, uint32\_t bit, uint32\_t val)
:   set retention register bit value.

    配置retention register的值，一个有4个retention register，需要指定

    参数:
    :   - **reg\_index** – **\[in\]** 0\~3, 指定是哪个retention register
        - **bit** – **\[in\]** 0\~31, 指定retention register的哪个bit
        - **val** – **\[in\]** 0 or 1, 该bit对应的值

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv428drv_pmu_get_retention_regbit8uint32_t8uint32_t"></a>

<a id="_CPPv328drv_pmu_get_retention_regbit8uint32_t8uint32_t"></a> <a id="_CPPv228drv_pmu_get_retention_regbit8uint32_t8uint32_t"></a> <a id="drv_pmu_get_retention_regbit__uint32_t.uint32_t"></a> <a id="group__PMU_1ga5c836e27e2a320c418de24edf13f4bff"></a> uint32\_t drv\_pmu\_get\_retention\_regbit(uint32\_t reg\_index, uint32\_t bit)
:   get retention register bit value.

    获取某个retention register的某个bit对应的值

    参数:
    :   - **reg\_index** – **\[in\]** 0\~3, 指定是哪个retention register
        - **bit** – **\[in\]** 0\~31, 指定retention register的哪个bit

    返回:
    :   bit value, 0 or 1

<a id="_CPPv425drv_pmu_set_retention_reg8uint32_t8uint32_t"></a>

<a id="_CPPv325drv_pmu_set_retention_reg8uint32_t8uint32_t"></a> <a id="_CPPv225drv_pmu_set_retention_reg8uint32_t8uint32_t"></a> <a id="drv_pmu_set_retention_reg__uint32_t.uint32_t"></a> <a id="group__PMU_1ga09908c9433c1c532bd58ce8f54ff3a65"></a> int32\_t drv\_pmu\_set\_retention\_reg(uint32\_t reg\_index, uint32\_t reg\_val)
:   set retention register value.

    配置retention register的值，一个有4个retention register，需要指定

    参数:
    :   - **reg\_index** – **\[in\]** 0\~3, 指定是哪个retention register
        - **reg\_val** – **\[in\]** register 对应的值

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425drv_pmu_get_retention_reg8uint32_t"></a>

<a id="_CPPv325drv_pmu_get_retention_reg8uint32_t"></a> <a id="_CPPv225drv_pmu_get_retention_reg8uint32_t"></a> <a id="drv_pmu_get_retention_reg__uint32_t"></a> <a id="group__PMU_1gab24d6eff5c8159f24733d6b1b259b347"></a> uint32\_t drv\_pmu\_get\_retention\_reg(uint32\_t reg\_index)
:   get retention register value.

    获取某个retention register的值

    参数:
    :   **reg\_index** – **\[in\]** 0\~3, 指定是哪个retention register

    返回:
    :   register value

<a id="_CPPv425drv_pmu_set_rw_wakeup_reqb"></a>

<a id="_CPPv325drv_pmu_set_rw_wakeup_reqb"></a> <a id="_CPPv225drv_pmu_set_rw_wakeup_reqb"></a> <a id="drv_pmu_set_rw_wakeup_req__b"></a> <a id="group__PMU_1gaec43218014066bb484310bfbb6dc977e"></a> int32\_t drv\_pmu\_set\_rw\_wakeup\_req(bool value)
:   drv\_pmu\_set\_rw\_wakeup\_req.

    设置rw唤醒请求

    参数:
    :   **void** – **\[in\]**

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv421drv_pmu_set_bt_iso_enb"></a>

<a id="_CPPv321drv_pmu_set_bt_iso_enb"></a> <a id="_CPPv221drv_pmu_set_bt_iso_enb"></a> <a id="drv_pmu_set_bt_iso_en__b"></a> <a id="group__PMU_1ga73abb0b883f9de3440dc03f72a7a7988"></a> int32\_t drv\_pmu\_set\_bt\_iso\_en(bool value)
:   drv\_pmu\_set\_bt\_iso\_en.

    设置bt休眠锁存信号

    参数:
    :   **void** – **\[in\]**

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv435drv_pmu_get_wakeup_deepsleep_sourcev"></a>

<a id="_CPPv335drv_pmu_get_wakeup_deepsleep_sourcev"></a> <a id="_CPPv235drv_pmu_get_wakeup_deepsleep_sourcev"></a> <a id="drv_pmu_get_wakeup_deepsleep_source__void"></a> <a id="group__PMU_1ga11951bccd395a0474b8c6b8e7ff5e52d"></a> uint32\_t drv\_pmu\_get\_wakeup\_deepsleep\_source(void)
:   get wakeup deepsleep source (register 0x14) bit0: rw bit1: int\_TD bit2: touch\_wkup bit3: GPIO\_DET compare bit4: chg\_trc bit5: chg\_cv bit6: chg\_ccfast bit7: wake\_touch bit8: usb4v bit9: usb2v bit10: usb1v bit11: re\_chg bit12: chg\_finish bit13: rtc bit14: gpio bit15: aon timer

    返回:
    :   wakeup source

<a id="structures"></a>

### Structures

<a id="_CPPv414pmu_halt_cfg_t"></a>

<a id="_CPPv314pmu_halt_cfg_t"></a> <a id="_CPPv214pmu_halt_cfg_t"></a> <a id="pmu_halt_cfg_t"></a> <a id="structpmu__halt__cfg__t"></a> struct pmu\_halt\_cfg\_t

<a id="macros"></a>

### Macros

<a id="c.PMU_RETENTION_0_0__FAST_JUMP2FLASH"></a>

<a id="group__PMU_1gadbbe891777d47a26a28dde6fddaa0f53"></a> PMU\_RETENTION\_0\_0\_\_FAST\_JUMP2FLASH

<a id="c.PMU_RETENTION_0_1__4Line_FASTBOOT"></a>

<a id="group__PMU_1ga4f1485dc4ce71d8befb03c25596c9e52"></a> PMU\_RETENTION\_0\_1\_\_4Line\_FASTBOOT

<a id="c.PMU_RETENTION_0_2__reset_flash"></a>

<a id="group__PMU_1ga07eb173ff08abd029f2b3654e0afec62"></a> PMU\_RETENTION\_0\_2\_\_reset\_flash

<a id="c.PMU_RETENTION_0_3__reset_wait_2times"></a>

<a id="group__PMU_1ga6dd4ac148f4a8759298f67bd65e9db82"></a> PMU\_RETENTION\_0\_3\_\_reset\_wait\_2times

<a id="c.PMU_RETENTION_0_4__charger_in_deepsleep"></a>

<a id="group__PMU_1ga5f1849c5ca4bcba1b221cab110ea8bc5"></a> PMU\_RETENTION\_0\_4\_\_charger\_in\_deepsleep

<a id="c.PMU_RETENTION_0_5__charger_first_active"></a>

<a id="group__PMU_1ga9feec0abac416fbac6c3f28f4704d9fc"></a> PMU\_RETENTION\_0\_5\_\_charger\_first\_active

<a id="c.PMU_RETENTION_0_6__ota_reboot"></a>

<a id="group__PMU_1gae65e4795d7dc06ffe84f38f23423ce41"></a> PMU\_RETENTION\_0\_6\_\_ota\_reboot

<a id="c.PMU_RETENTION_0_7__froce_reboot"></a>

<a id="group__PMU_1gaa667f02725b40de042bb4ec34a3a629b"></a> PMU\_RETENTION\_0\_7\_\_froce\_reboot

<a id="c.PMU_RETENTION_3_14__keep_rom"></a>

<a id="group__PMU_1gafbc78e0357fde3ca15fcf922ba5bce31"></a> PMU\_RETENTION\_3\_14\_\_keep\_rom

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv417drv_pmu_wdt_dst_e"></a>

<a id="_CPPv317drv_pmu_wdt_dst_e"></a> <a id="_CPPv217drv_pmu_wdt_dst_e"></a> <a id="drv_pmu_wdt_dst_e"></a> <a id="group__PMU_1gaff0aba78d3302829ad4ea83ebb60de7f"></a> typedef enum [\_drv\_pmu\_wdt\_dst\_e](#_CPPv418_drv_pmu_wdt_dst_e "_drv_pmu_wdt_dst_e") drv\_pmu\_wdt\_dst\_e
:   watchdog reset destination select

<a id="_CPPv417drv_pmu_32k_src_e"></a>

<a id="_CPPv317drv_pmu_32k_src_e"></a> <a id="_CPPv217drv_pmu_32k_src_e"></a> <a id="drv_pmu_32k_src_e"></a> <a id="group__PMU_1ga2e084e0132308107f4229a9a249c4bc6"></a> typedef enum [\_drv\_pmu\_32k\_src\_e](#_CPPv418_drv_pmu_32k_src_e "_drv_pmu_32k_src_e") drv\_pmu\_32k\_src\_e
:   aon 32k source

<a id="_CPPv421drv_pmu_usb_voltage_e"></a>

<a id="_CPPv321drv_pmu_usb_voltage_e"></a> <a id="_CPPv221drv_pmu_usb_voltage_e"></a> <a id="drv_pmu_usb_voltage_e"></a> <a id="group__PMU_1gad78866aa534014b28133b3330736c2b4"></a> typedef enum [\_drv\_pmu\_usb\_voltage\_e](#_CPPv422_drv_pmu_usb_voltage_e "_drv_pmu_usb_voltage_e") drv\_pmu\_usb\_voltage\_e
:   usb电压

<a id="_CPPv415pfunc_vusb_cb_t"></a>

<a id="_CPPv315pfunc_vusb_cb_t"></a> <a id="_CPPv215pfunc_vusb_cb_t"></a> <a id="pfunc_vusb_cb_t"></a> <a id="group__PMU_1gabfded7af341231910fdcf8ffc48aa160"></a> typedef void (\*pfunc\_vusb\_cb\_t)([drv\_pmu\_usb\_voltage\_e](#_CPPv421drv_pmu_usb_voltage_e "drv_pmu_usb_voltage_e") e\_from, [drv\_pmu\_usb\_voltage\_e](#_CPPv421drv_pmu_usb_voltage_e "drv_pmu_usb_voltage_e") e\_to)
:   vusb interrupt callback

<a id="_CPPv417drv_pmu_ana_src_e"></a>

<a id="_CPPv317drv_pmu_ana_src_e"></a> <a id="_CPPv217drv_pmu_ana_src_e"></a> <a id="drv_pmu_ana_src_e"></a> <a id="group__PMU_1ga67c75378c8bc98556a37f52c3b75a9d0"></a> typedef enum [\_drv\_pmu\_ana\_src\_e](#_CPPv418_drv_pmu_ana_src_e "_drv_pmu_ana_src_e") drv\_pmu\_ana\_src\_e
:   analog source define

<a id="_CPPv420drv_pmu_wakeup_src_e"></a>

<a id="_CPPv320drv_pmu_wakeup_src_e"></a> <a id="_CPPv220drv_pmu_wakeup_src_e"></a> <a id="drv_pmu_wakeup_src_e"></a> <a id="group__PMU_1ga8a9610d9bebf1281c8051971a7a2f78a"></a> typedef enum [\_drv\_pmu\_wakeup\_src\_e](#_CPPv421_drv_pmu_wakeup_src_e "_drv_pmu_wakeup_src_e") drv\_pmu\_wakeup\_src\_e
:   wakeup source

<a id="_CPPv415pfunc_wkup_cb_t"></a>

<a id="_CPPv315pfunc_wkup_cb_t"></a> <a id="_CPPv215pfunc_wkup_cb_t"></a> <a id="pfunc_wkup_cb_t"></a> <a id="group__PMU_1ga20f8c72837fccccf98b0ef58b51f10cd"></a> typedef void (\*pfunc\_wkup\_cb\_t)([drv\_pmu\_wakeup\_src\_e](#_CPPv420drv_pmu_wakeup_src_e "drv_pmu_wakeup_src_e") e\_src)
:   wakeup interrupt callback

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv418_drv_pmu_wdt_dst_e"></a>

<a id="_CPPv318_drv_pmu_wdt_dst_e"></a> <a id="_CPPv218_drv_pmu_wdt_dst_e"></a> <a id="group__PMU_1ga70ff96032b0255c091d9294f19989a14"></a> enum \_drv\_pmu\_wdt\_dst\_e
:   watchdog reset destination select

    *Values:*

    <a id="_CPPv4N18_drv_pmu_wdt_dst_e21DRV_PMU_WDT_RESET_AONE"></a>

    <a id="_CPPv3N18_drv_pmu_wdt_dst_e21DRV_PMU_WDT_RESET_AONE"></a> <a id="_CPPv2N18_drv_pmu_wdt_dst_e21DRV_PMU_WDT_RESET_AONE"></a> <a id="group__PMU_1gga70ff96032b0255c091d9294f19989a14a9991c8f0dc15bf41673254961bf6c42a"></a> enumerator DRV\_PMU\_WDT\_RESET\_AON

    <a id="_CPPv4N18_drv_pmu_wdt_dst_e21DRV_PMU_WDT_RESET_DIGE"></a>

    <a id="_CPPv3N18_drv_pmu_wdt_dst_e21DRV_PMU_WDT_RESET_DIGE"></a> <a id="_CPPv2N18_drv_pmu_wdt_dst_e21DRV_PMU_WDT_RESET_DIGE"></a> <a id="group__PMU_1gga70ff96032b0255c091d9294f19989a14a539ba5d3a8f67f85ffbd3b04377aa04a"></a> enumerator DRV\_PMU\_WDT\_RESET\_DIG

    <a id="_CPPv4N18_drv_pmu_wdt_dst_e21DRV_PMU_WDT_RESET_ANAE"></a>

    <a id="_CPPv3N18_drv_pmu_wdt_dst_e21DRV_PMU_WDT_RESET_ANAE"></a> <a id="_CPPv2N18_drv_pmu_wdt_dst_e21DRV_PMU_WDT_RESET_ANAE"></a> <a id="group__PMU_1gga70ff96032b0255c091d9294f19989a14ac3afebe965b102b84d7afd18c2c4b6d3"></a> enumerator DRV\_PMU\_WDT\_RESET\_ANA

    <a id="_CPPv4N18_drv_pmu_wdt_dst_e21DRV_PMU_WDT_RESET_PMUE"></a>

    <a id="_CPPv3N18_drv_pmu_wdt_dst_e21DRV_PMU_WDT_RESET_PMUE"></a> <a id="_CPPv2N18_drv_pmu_wdt_dst_e21DRV_PMU_WDT_RESET_PMUE"></a> <a id="group__PMU_1gga70ff96032b0255c091d9294f19989a14a3fecb2461d6b3e4c736902b30482c883"></a> enumerator DRV\_PMU\_WDT\_RESET\_PMU

<a id="_CPPv418_drv_pmu_32k_src_e"></a>

<a id="_CPPv318_drv_pmu_32k_src_e"></a> <a id="_CPPv218_drv_pmu_32k_src_e"></a> <a id="group__PMU_1ga7eb1d407bc94504364b76f61fbb4e970"></a> enum \_drv\_pmu\_32k\_src\_e
:   aon 32k source

    *Values:*

    <a id="_CPPv4N18_drv_pmu_32k_src_e24DRV_PMU_32K_FROM_26M_DIVE"></a>

    <a id="_CPPv3N18_drv_pmu_32k_src_e24DRV_PMU_32K_FROM_26M_DIVE"></a> <a id="_CPPv2N18_drv_pmu_32k_src_e24DRV_PMU_32K_FROM_26M_DIVE"></a> <a id="group__PMU_1gga7eb1d407bc94504364b76f61fbb4e970a0e4b82486c292ed813f7d2a757d4f3ec"></a> enumerator DRV\_PMU\_32K\_FROM\_26M\_DIV

    <a id="_CPPv4N18_drv_pmu_32k_src_e22DRV_PMU_32K_FROM_RC32KE"></a>

    <a id="_CPPv3N18_drv_pmu_32k_src_e22DRV_PMU_32K_FROM_RC32KE"></a> <a id="_CPPv2N18_drv_pmu_32k_src_e22DRV_PMU_32K_FROM_RC32KE"></a> <a id="group__PMU_1gga7eb1d407bc94504364b76f61fbb4e970ac44f3726ee021112dd459f22a6157c9d"></a> enumerator DRV\_PMU\_32K\_FROM\_RC32K

<a id="_CPPv422_drv_pmu_usb_voltage_e"></a>

<a id="_CPPv322_drv_pmu_usb_voltage_e"></a> <a id="_CPPv222_drv_pmu_usb_voltage_e"></a> <a id="group__PMU_1gaf927d19dd5018f0a8124be964d591497"></a> enum \_drv\_pmu\_usb\_voltage\_e
:   usb电压

    *Values:*

    <a id="_CPPv4N22_drv_pmu_usb_voltage_e19DRV_PMU_USB_0V_MOREE"></a>

    <a id="_CPPv3N22_drv_pmu_usb_voltage_e19DRV_PMU_USB_0V_MOREE"></a> <a id="_CPPv2N22_drv_pmu_usb_voltage_e19DRV_PMU_USB_0V_MOREE"></a> <a id="group__PMU_1ggaf927d19dd5018f0a8124be964d591497a28fe1476a0652ce39b6e55baa5cff53c"></a> enumerator DRV\_PMU\_USB\_0V\_MORE

    <a id="_CPPv4N22_drv_pmu_usb_voltage_e19DRV_PMU_USB_1V_MOREE"></a>

    <a id="_CPPv3N22_drv_pmu_usb_voltage_e19DRV_PMU_USB_1V_MOREE"></a> <a id="_CPPv2N22_drv_pmu_usb_voltage_e19DRV_PMU_USB_1V_MOREE"></a> <a id="group__PMU_1ggaf927d19dd5018f0a8124be964d591497a77ced6a044b92e67e26bcaf2499b7023"></a> enumerator DRV\_PMU\_USB\_1V\_MORE

    <a id="_CPPv4N22_drv_pmu_usb_voltage_e19DRV_PMU_USB_2V_MOREE"></a>

    <a id="_CPPv3N22_drv_pmu_usb_voltage_e19DRV_PMU_USB_2V_MOREE"></a> <a id="_CPPv2N22_drv_pmu_usb_voltage_e19DRV_PMU_USB_2V_MOREE"></a> <a id="group__PMU_1ggaf927d19dd5018f0a8124be964d591497a0698896b76e0785b41db305aa2f4872c"></a> enumerator DRV\_PMU\_USB\_2V\_MORE

    <a id="_CPPv4N22_drv_pmu_usb_voltage_e19DRV_PMU_USB_4V_MOREE"></a>

    <a id="_CPPv3N22_drv_pmu_usb_voltage_e19DRV_PMU_USB_4V_MOREE"></a> <a id="_CPPv2N22_drv_pmu_usb_voltage_e19DRV_PMU_USB_4V_MOREE"></a> <a id="group__PMU_1ggaf927d19dd5018f0a8124be964d591497a32bee9db38b586ca3943f5913f47694a"></a> enumerator DRV\_PMU\_USB\_4V\_MORE

<a id="_CPPv418_drv_pmu_ana_src_e"></a>

<a id="_CPPv318_drv_pmu_ana_src_e"></a> <a id="_CPPv218_drv_pmu_ana_src_e"></a> <a id="group__PMU_1ga173a387361b8e5f5dc186678d9334730"></a> enum \_drv\_pmu\_ana\_src\_e
:   analog source define

    *Values:*

    <a id="_CPPv4N18_drv_pmu_ana_src_e20DRV_PMU_ANA_chg_termE"></a>

    <a id="_CPPv3N18_drv_pmu_ana_src_e20DRV_PMU_ANA_chg_termE"></a> <a id="_CPPv2N18_drv_pmu_ana_src_e20DRV_PMU_ANA_chg_termE"></a> <a id="group__PMU_1gga173a387361b8e5f5dc186678d9334730ade5964bf32aa77c1eed06d7a74172208"></a> enumerator DRV\_PMU\_ANA\_chg\_term

    <a id="_CPPv4N18_drv_pmu_ana_src_e18DRV_PMU_ANA_re_chgE"></a>

    <a id="_CPPv3N18_drv_pmu_ana_src_e18DRV_PMU_ANA_re_chgE"></a> <a id="_CPPv2N18_drv_pmu_ana_src_e18DRV_PMU_ANA_re_chgE"></a> <a id="group__PMU_1gga173a387361b8e5f5dc186678d9334730aae07e9880a17c096bbc193a170821791"></a> enumerator DRV\_PMU\_ANA\_re\_chg

    <a id="_CPPv4N18_drv_pmu_ana_src_e22DRV_PMU_ANA_chg_ccfastE"></a>

    <a id="_CPPv3N18_drv_pmu_ana_src_e22DRV_PMU_ANA_chg_ccfastE"></a> <a id="_CPPv2N18_drv_pmu_ana_src_e22DRV_PMU_ANA_chg_ccfastE"></a> <a id="group__PMU_1gga173a387361b8e5f5dc186678d9334730a20835226d9d9337e33b12ca34706106b"></a> enumerator DRV\_PMU\_ANA\_chg\_ccfast

    <a id="_CPPv4N18_drv_pmu_ana_src_e18DRV_PMU_ANA_chg_cvE"></a>

    <a id="_CPPv3N18_drv_pmu_ana_src_e18DRV_PMU_ANA_chg_cvE"></a> <a id="_CPPv2N18_drv_pmu_ana_src_e18DRV_PMU_ANA_chg_cvE"></a> <a id="group__PMU_1gga173a387361b8e5f5dc186678d9334730a4671d99ad971901429d118ff9c284fd9"></a> enumerator DRV\_PMU\_ANA\_chg\_cv

    <a id="_CPPv4N18_drv_pmu_ana_src_e19DRV_PMU_ANA_chg_trcE"></a>

    <a id="_CPPv3N18_drv_pmu_ana_src_e19DRV_PMU_ANA_chg_trcE"></a> <a id="_CPPv2N18_drv_pmu_ana_src_e19DRV_PMU_ANA_chg_trcE"></a> <a id="group__PMU_1gga173a387361b8e5f5dc186678d9334730a817bf27d4d42b1368c0f94f1a9b61cb9"></a> enumerator DRV\_PMU\_ANA\_chg\_trc

    <a id="_CPPv4N18_drv_pmu_ana_src_e20DRV_PMU_ANA_gpio_detE"></a>

    <a id="_CPPv3N18_drv_pmu_ana_src_e20DRV_PMU_ANA_gpio_detE"></a> <a id="_CPPv2N18_drv_pmu_ana_src_e20DRV_PMU_ANA_gpio_detE"></a> <a id="group__PMU_1gga173a387361b8e5f5dc186678d9334730a0b77b239af3c46e4d0de7c5553405393"></a> enumerator DRV\_PMU\_ANA\_gpio\_det

    <a id="_CPPv4N18_drv_pmu_ana_src_e22DRV_PMU_ANA_touch_wkupE"></a>

    <a id="_CPPv3N18_drv_pmu_ana_src_e22DRV_PMU_ANA_touch_wkupE"></a> <a id="_CPPv2N18_drv_pmu_ana_src_e22DRV_PMU_ANA_touch_wkupE"></a> <a id="group__PMU_1gga173a387361b8e5f5dc186678d9334730a2e144090b6812ada9551dda454cc10d2"></a> enumerator DRV\_PMU\_ANA\_touch\_wkup

    <a id="_CPPv4N18_drv_pmu_ana_src_e21DRV_PMU_ANA_int_touchE"></a>

    <a id="_CPPv3N18_drv_pmu_ana_src_e21DRV_PMU_ANA_int_touchE"></a> <a id="_CPPv2N18_drv_pmu_ana_src_e21DRV_PMU_ANA_int_touchE"></a> <a id="group__PMU_1gga173a387361b8e5f5dc186678d9334730a4a9f0f64e053ad3fed314cb2480b2ed8"></a> enumerator DRV\_PMU\_ANA\_int\_touch

    <a id="_CPPv4N18_drv_pmu_ana_src_e19DRV_PMU_ANA_SRC_MAXE"></a>

    <a id="_CPPv3N18_drv_pmu_ana_src_e19DRV_PMU_ANA_SRC_MAXE"></a> <a id="_CPPv2N18_drv_pmu_ana_src_e19DRV_PMU_ANA_SRC_MAXE"></a> <a id="group__PMU_1gga173a387361b8e5f5dc186678d9334730a84c742fbf2f42b1e47da67b144bbdac3"></a> enumerator DRV\_PMU\_ANA\_SRC\_MAX

<a id="_CPPv421_drv_pmu_wakeup_src_e"></a>

<a id="_CPPv321_drv_pmu_wakeup_src_e"></a> <a id="_CPPv221_drv_pmu_wakeup_src_e"></a> <a id="group__PMU_1ga6db1142fc87d704d98d3afa9a43c303d"></a> enum \_drv\_pmu\_wakeup\_src\_e
:   wakeup source

    *Values:*

    <a id="_CPPv4N21_drv_pmu_wakeup_src_e23DRV_PMU_WAKEUP_SRC_gpioE"></a>

    <a id="_CPPv3N21_drv_pmu_wakeup_src_e23DRV_PMU_WAKEUP_SRC_gpioE"></a> <a id="_CPPv2N21_drv_pmu_wakeup_src_e23DRV_PMU_WAKEUP_SRC_gpioE"></a> <a id="group__PMU_1gga6db1142fc87d704d98d3afa9a43c303da792ca0650b6a7248532c98b0583caf25"></a> enumerator DRV\_PMU\_WAKEUP\_SRC\_gpio

    <a id="_CPPv4N21_drv_pmu_wakeup_src_e22DRV_PMU_WAKEUP_SRC_rtcE"></a>

    <a id="_CPPv3N21_drv_pmu_wakeup_src_e22DRV_PMU_WAKEUP_SRC_rtcE"></a> <a id="_CPPv2N21_drv_pmu_wakeup_src_e22DRV_PMU_WAKEUP_SRC_rtcE"></a> <a id="group__PMU_1gga6db1142fc87d704d98d3afa9a43c303daee4237b3a652c7b783c4970b1a69e5aa"></a> enumerator DRV\_PMU\_WAKEUP\_SRC\_rtc

    <a id="_CPPv4N21_drv_pmu_wakeup_src_e32DRV_PMU_WAKEUP_SRC_ana0_chg_termE"></a>

    <a id="_CPPv3N21_drv_pmu_wakeup_src_e32DRV_PMU_WAKEUP_SRC_ana0_chg_termE"></a> <a id="_CPPv2N21_drv_pmu_wakeup_src_e32DRV_PMU_WAKEUP_SRC_ana0_chg_termE"></a> <a id="group__PMU_1gga6db1142fc87d704d98d3afa9a43c303da415fc1ed22c78fd784f69df78b6c74b5"></a> enumerator DRV\_PMU\_WAKEUP\_SRC\_ana0\_chg\_term

    <a id="_CPPv4N21_drv_pmu_wakeup_src_e29DRV_PMU_WAKEUP_SRC_ana1_rechgE"></a>

    <a id="_CPPv3N21_drv_pmu_wakeup_src_e29DRV_PMU_WAKEUP_SRC_ana1_rechgE"></a> <a id="_CPPv2N21_drv_pmu_wakeup_src_e29DRV_PMU_WAKEUP_SRC_ana1_rechgE"></a> <a id="group__PMU_1gga6db1142fc87d704d98d3afa9a43c303da4c359e5b59d53d33718343ff5b76a35b"></a> enumerator DRV\_PMU\_WAKEUP\_SRC\_ana1\_rechg

    <a id="_CPPv4N21_drv_pmu_wakeup_src_e24DRV_PMU_WAKEUP_SRC_usb1vE"></a>

    <a id="_CPPv3N21_drv_pmu_wakeup_src_e24DRV_PMU_WAKEUP_SRC_usb1vE"></a> <a id="_CPPv2N21_drv_pmu_wakeup_src_e24DRV_PMU_WAKEUP_SRC_usb1vE"></a> <a id="group__PMU_1gga6db1142fc87d704d98d3afa9a43c303da293480d17fd6f77c519370c224d5f734"></a> enumerator DRV\_PMU\_WAKEUP\_SRC\_usb1v

    <a id="_CPPv4N21_drv_pmu_wakeup_src_e24DRV_PMU_WAKEUP_SRC_usb2vE"></a>

    <a id="_CPPv3N21_drv_pmu_wakeup_src_e24DRV_PMU_WAKEUP_SRC_usb2vE"></a> <a id="_CPPv2N21_drv_pmu_wakeup_src_e24DRV_PMU_WAKEUP_SRC_usb2vE"></a> <a id="group__PMU_1gga6db1142fc87d704d98d3afa9a43c303dabad5c05c1b428394630b9da73b01a9bc"></a> enumerator DRV\_PMU\_WAKEUP\_SRC\_usb2v

    <a id="_CPPv4N21_drv_pmu_wakeup_src_e24DRV_PMU_WAKEUP_SRC_usb4vE"></a>

    <a id="_CPPv3N21_drv_pmu_wakeup_src_e24DRV_PMU_WAKEUP_SRC_usb4vE"></a> <a id="_CPPv2N21_drv_pmu_wakeup_src_e24DRV_PMU_WAKEUP_SRC_usb4vE"></a> <a id="group__PMU_1gga6db1142fc87d704d98d3afa9a43c303da56027f97a84a7bb354f36e16a67dfa5f"></a> enumerator DRV\_PMU\_WAKEUP\_SRC\_usb4v

    <a id="_CPPv4N21_drv_pmu_wakeup_src_e24DRV_PMU_WAKEUP_SRC_touchE"></a>

    <a id="_CPPv3N21_drv_pmu_wakeup_src_e24DRV_PMU_WAKEUP_SRC_touchE"></a> <a id="_CPPv2N21_drv_pmu_wakeup_src_e24DRV_PMU_WAKEUP_SRC_touchE"></a> <a id="group__PMU_1gga6db1142fc87d704d98d3afa9a43c303da9dc1129827460da2ca3368c26459471c"></a> enumerator DRV\_PMU\_WAKEUP\_SRC\_touch

    <a id="_CPPv4N21_drv_pmu_wakeup_src_e34DRV_PMU_WAKEUP_SRC_ana2_chg_ccfastE"></a>

    <a id="_CPPv3N21_drv_pmu_wakeup_src_e34DRV_PMU_WAKEUP_SRC_ana2_chg_ccfastE"></a> <a id="_CPPv2N21_drv_pmu_wakeup_src_e34DRV_PMU_WAKEUP_SRC_ana2_chg_ccfastE"></a> <a id="group__PMU_1gga6db1142fc87d704d98d3afa9a43c303da8979b9fb1dbd50dde5cf21b088a9481f"></a> enumerator DRV\_PMU\_WAKEUP\_SRC\_ana2\_chg\_ccfast

    <a id="_CPPv4N21_drv_pmu_wakeup_src_e30DRV_PMU_WAKEUP_SRC_ana3_chg_cvE"></a>

    <a id="_CPPv3N21_drv_pmu_wakeup_src_e30DRV_PMU_WAKEUP_SRC_ana3_chg_cvE"></a> <a id="_CPPv2N21_drv_pmu_wakeup_src_e30DRV_PMU_WAKEUP_SRC_ana3_chg_cvE"></a> <a id="group__PMU_1gga6db1142fc87d704d98d3afa9a43c303daad250e3751d6648f74cbbc520c9a76d9"></a> enumerator DRV\_PMU\_WAKEUP\_SRC\_ana3\_chg\_cv

    <a id="_CPPv4N21_drv_pmu_wakeup_src_e31DRV_PMU_WAKEUP_SRC_ana4_chg_trcE"></a>

    <a id="_CPPv3N21_drv_pmu_wakeup_src_e31DRV_PMU_WAKEUP_SRC_ana4_chg_trcE"></a> <a id="_CPPv2N21_drv_pmu_wakeup_src_e31DRV_PMU_WAKEUP_SRC_ana4_chg_trcE"></a> <a id="group__PMU_1gga6db1142fc87d704d98d3afa9a43c303dae7eaa47518de323d148e1ab4e074f0b6"></a> enumerator DRV\_PMU\_WAKEUP\_SRC\_ana4\_chg\_trc

    <a id="_CPPv4N21_drv_pmu_wakeup_src_e32DRV_PMU_WAKEUP_SRC_ana5_gpio_detE"></a>

    <a id="_CPPv3N21_drv_pmu_wakeup_src_e32DRV_PMU_WAKEUP_SRC_ana5_gpio_detE"></a> <a id="_CPPv2N21_drv_pmu_wakeup_src_e32DRV_PMU_WAKEUP_SRC_ana5_gpio_detE"></a> <a id="group__PMU_1gga6db1142fc87d704d98d3afa9a43c303daa1fab90ed38ccb216c6bd5964b327e70"></a> enumerator DRV\_PMU\_WAKEUP\_SRC\_ana5\_gpio\_det

    <a id="_CPPv4N21_drv_pmu_wakeup_src_e34DRV_PMU_WAKEUP_SRC_ana6_touch_wkupE"></a>

    <a id="_CPPv3N21_drv_pmu_wakeup_src_e34DRV_PMU_WAKEUP_SRC_ana6_touch_wkupE"></a> <a id="_CPPv2N21_drv_pmu_wakeup_src_e34DRV_PMU_WAKEUP_SRC_ana6_touch_wkupE"></a> <a id="group__PMU_1gga6db1142fc87d704d98d3afa9a43c303da8c172e705ee0623de517567372daf052"></a> enumerator DRV\_PMU\_WAKEUP\_SRC\_ana6\_touch\_wkup

    <a id="_CPPv4N21_drv_pmu_wakeup_src_e33DRV_PMU_WAKEUP_SRC_ana7_int_touchE"></a>

    <a id="_CPPv3N21_drv_pmu_wakeup_src_e33DRV_PMU_WAKEUP_SRC_ana7_int_touchE"></a> <a id="_CPPv2N21_drv_pmu_wakeup_src_e33DRV_PMU_WAKEUP_SRC_ana7_int_touchE"></a> <a id="group__PMU_1gga6db1142fc87d704d98d3afa9a43c303dac9a28a5adfe58f55edabb1045036ddda"></a> enumerator DRV\_PMU\_WAKEUP\_SRC\_ana7\_int\_touch

    <a id="_CPPv4N21_drv_pmu_wakeup_src_e23DRV_PMU_WAKEUP_SRC_rwipE"></a>

    <a id="_CPPv3N21_drv_pmu_wakeup_src_e23DRV_PMU_WAKEUP_SRC_rwipE"></a> <a id="_CPPv2N21_drv_pmu_wakeup_src_e23DRV_PMU_WAKEUP_SRC_rwipE"></a> <a id="group__PMU_1gga6db1142fc87d704d98d3afa9a43c303da0997417ba455e0702feb42a7373ead5d"></a> enumerator DRV\_PMU\_WAKEUP\_SRC\_rwip

    <a id="_CPPv4N21_drv_pmu_wakeup_src_e28DRV_PMU_WAKEUP_SRC_aon_timerE"></a>

    <a id="_CPPv3N21_drv_pmu_wakeup_src_e28DRV_PMU_WAKEUP_SRC_aon_timerE"></a> <a id="_CPPv2N21_drv_pmu_wakeup_src_e28DRV_PMU_WAKEUP_SRC_aon_timerE"></a> <a id="group__PMU_1gga6db1142fc87d704d98d3afa9a43c303daf5dadc8e269bea4cd2c9ac5fc5f03bd3"></a> enumerator DRV\_PMU\_WAKEUP\_SRC\_aon\_timer

    <a id="_CPPv4N21_drv_pmu_wakeup_src_e22DRV_PMU_WAKEUP_SRC_ALLE"></a>

    <a id="_CPPv3N21_drv_pmu_wakeup_src_e22DRV_PMU_WAKEUP_SRC_ALLE"></a> <a id="_CPPv2N21_drv_pmu_wakeup_src_e22DRV_PMU_WAKEUP_SRC_ALLE"></a> <a id="group__PMU_1gga6db1142fc87d704d98d3afa9a43c303da6aeca1a37e7e92af076f279313e83698"></a> enumerator DRV\_PMU\_WAKEUP\_SRC\_ALL
