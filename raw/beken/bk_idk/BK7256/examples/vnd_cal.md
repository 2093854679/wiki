# VND_CAL[](#vnd-cal "永久链接至标题")



## 1、概述[](#id1 "永久链接至标题")

> 为了方便客户理解vnd_cal.c里的参数，这里对vnd_cal.c里参数进行说明。


## 2、代码路径[](#id2 "永久链接至标题")

> 路径: `\middleware\boards\bk7256(bk7235\bk7235m\bk7236\bk7258)\vnd_cal\vnd_cal.c`


## 3、参数简介[](#id3 "永久链接至标题")

参数如下:

> 1.校准数据的来源
> #define CMTAG_FROM_FLASH 1
> #define CMTAG_FROM_CALI 0
> - 功能说明：用来配置DC，IQ校准值从flash读取，还是每次上电，校准获取（bk7236与bk7258未支持）。从flash获取校准数据是为了优化开机上电时间。
>
> 2.默认晶体值
> #define DEFAULT_TXID_XTAL (0x10)
> - 功能说明：用来配置晶体默认值，为了优化频偏。
>
> 3.外部PA开关
> #define EPA_ENABLE_FLAG 0
> - 功能说明：使用外置PA功能，0关闭，1打开(bk7236与bk7258未支持)。
>
> 4.gain基值
> #define PWR_GAIN_BASE_B (0x5494B400)
> #define PWR_GAIN_BASE_G (0x60B09800)
> #define PWR_GAIN_BASE_BLE (0x63E05800)
> const UINT32 g_pwr_gain_base_ble = PWR_GAIN_BASE_BLE;
> const UINT32 pwr_gain_base_gain_b = PWR_GAIN_BASE_B;
> const UINT32 pwr_gain_base_gain_g = PWR_GAIN_BASE_G;
> - 功能说明：发包功率基值，11B，11G与BLE使用不同的基值。bk7236与bk7258未使用宏。
>
> 5.BLE发包功率范围选择
> 宏 CONFIG_BLE_USE_HIGH_POWER_LEVEL
> - 功能说明：选择BLE发包功率支持的范围，打开宏BLE支持高功率。bk7236与bk7258无该配置
>
> 6.功率gain表
> const PWR_REGS cfg_tab_b[TCP_PAMAP_TAB_B_LEN]
> const PWR_REGS cfg_tab_g[TCP_PAMAP_TAB_G_LEN]
> const PWR_REGS cfg_tab_ble[TCP_PAMAP_TAB_BLE_LEN]
> - 功能说明：11B,11G与BLE发包使用的gain表，与第4条的gain基值组合后为发包的具体功率值。11B为0.5dB一个step，11G为0.25dB一个step，BLE为0.25dB一个step。
>
> 7.发包功率表
> const TXPWR_ST gtxpwr_tab_def_b[WLAN_2_4_G_CHANNEL_NUM]
> const TXPWR_ST gtxpwr_tab_def_g[WLAN_2_4_G_CHANNEL_NUM]
> const TXPWR_ST gtxpwr_tab_def_n_40[WLAN_2_4_G_CHANNEL_NUM]
> const TXPWR_ST gtxpwr_tab_def_ble[BLE_2_4_G_CHANNEL_NUM]
> - 功能说明：11B，11G，11N 40M带宽与BLE默认发包功率表。开发板按照指定的发包功率校准后，会得出以上4张表。表中的值，为第6条gain表中值的下标。
>
> 8.温补表
> const TMP_PWR_ST tmp_pwr_tab[TMP_PWR_TAB_LEN]
> - 功能说明：温补表，根据温度调节发包功率与频偏。表的第2列为11B发包功率随温度变化的偏移值，第3列为11G、11N与11AX发包功率随温度变化的偏移值。第5列为频偏随温度变化的偏移值。
>
> 9.自动功率校准配置
> const static AUTO_PWR_CALI_CONTEXT auto_pwr
> - 功能说明：自动功率校准配置参数。第一个参数为打开与关闭自动功率校准的开关，0是打开，1是关闭。第2-4个参数为11B 1信道，7信道，13信道，自动功率校准的阈值。第5-7个参数为11G 1信道，7信道，13信道，自动功率校准的阈值。11N与11AX基于11G自动功率校准结果偏移而来。
>
> 10.不同rate发包功率偏移表
> const INT16 shift_tab_b[4]
> const INT16 shift_tab_g[8]
> const INT16 shift_tab_n20[10]
> const INT16 shift_tab_n40[10]
> - 功能说明：不同rate发包功率偏移表。功率校准是以11B 11M，11G 54M，11N 40M NCS7进行校准，其他rate发包功率是在校准使用的rate功率进行偏移得出。
>
> 11.配置自动功率校准参数到代码
> vnd_cal_set_auto_pwr_thred(auto_pwr);
> - 功能说明：将第9条的参数配置到代码，并使用。
>
> 12.配置外部PA使用的GPIO
> vnd_cal_set_epa_config(1, GPIO_28, GPIO_26, pwr_gain_base_gain_b, pwr_gain_base_gain_g);
> vnd_cal_set_epa_config(0, GPIO_28, GPIO_26, pwr_gain_base_gain_b, pwr_gain_base_gain_g);
> - 功能说明：配置GPIO打开或关闭外PA功能。
