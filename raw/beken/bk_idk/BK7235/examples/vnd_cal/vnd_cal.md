---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7235/zh_CN/v1.5/examples/vnd_cal/vnd_cal.html
sdk_family: bk_idk
chip: BK7235
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="vnd-cal"></a>

# VND\_CAL

<a id="id1"></a>

## 1、概述

> 为了方便客户理解vnd\_cal.c里的参数，这里对vnd\_cal.c里参数进行说明。

<a id="id2"></a>

## 2、代码路径

> 路径: `\middleware\boards\bk7256(bk7235\bk7235m\bk7236\bk7258)\vnd_cal\vnd_cal.c`

<a id="id3"></a>

## 3、参数简介

参数如下:

> 1.校准数据的来源
> #define CMTAG\_FROM\_FLASH 1
> #define CMTAG\_FROM\_CALI 0
> \- 功能说明：用来配置DC，IQ校准值从flash读取，还是每次上电，校准获取（bk7236与bk7258未支持）。从flash获取校准数据是为了优化开机上电时间。
>
> 2.默认晶体值
> #define DEFAULT\_TXID\_XTAL (0x10)
> \- 功能说明：用来配置晶体默认值，为了优化频偏。
>
> 3.外部PA开关
> #define EPA\_ENABLE\_FLAG 0
> \- 功能说明：使用外置PA功能，0关闭，1打开(bk7236与bk7258未支持)。
>
> 4.gain基值
> #define PWR\_GAIN\_BASE\_B (0x5494B400)
> #define PWR\_GAIN\_BASE\_G (0x60B09800)
> #define PWR\_GAIN\_BASE\_BLE (0x63E05800)
> const UINT32 g\_pwr\_gain\_base\_ble \= PWR\_GAIN\_BASE\_BLE;
> const UINT32 pwr\_gain\_base\_gain\_b \= PWR\_GAIN\_BASE\_B;
> const UINT32 pwr\_gain\_base\_gain\_g \= PWR\_GAIN\_BASE\_G;
> \- 功能说明：发包功率基值，11B，11G与BLE使用不同的基值。bk7236与bk7258未使用宏。
>
> 5.BLE发包功率范围选择
> 宏 CONFIG\_BLE\_USE\_HIGH\_POWER\_LEVEL
> \- 功能说明：选择BLE发包功率支持的范围，打开宏BLE支持高功率。bk7236与bk7258无该配置
>
> 6.功率gain表
> const PWR\_REGS cfg\_tab\_b\[TCP\_PAMAP\_TAB\_B\_LEN\]
> const PWR\_REGS cfg\_tab\_g\[TCP\_PAMAP\_TAB\_G\_LEN\]
> const PWR\_REGS cfg\_tab\_ble\[TCP\_PAMAP\_TAB\_BLE\_LEN\]
> \- 功能说明：11B,11G与BLE发包使用的gain表，与第4条的gain基值组合后为发包的具体功率值。11B为0.5dB一个step，11G为0.25dB一个step，BLE为0.25dB一个step。
>
> 7.发包功率表
> const TXPWR\_ST gtxpwr\_tab\_def\_b\[WLAN\_2\_4\_G\_CHANNEL\_NUM\]
> const TXPWR\_ST gtxpwr\_tab\_def\_g\[WLAN\_2\_4\_G\_CHANNEL\_NUM\]
> const TXPWR\_ST gtxpwr\_tab\_def\_n\_40\[WLAN\_2\_4\_G\_CHANNEL\_NUM\]
> const TXPWR\_ST gtxpwr\_tab\_def\_ble\[BLE\_2\_4\_G\_CHANNEL\_NUM\]
> \- 功能说明：11B，11G，11N 40M带宽与BLE默认发包功率表。开发板按照指定的发包功率校准后，会得出以上4张表。表中的值，为第6条gain表中值的下标。
>
> 8.温补表
> const TMP\_PWR\_ST tmp\_pwr\_tab\[TMP\_PWR\_TAB\_LEN\]
> \- 功能说明：温补表，根据温度调节发包功率与频偏。表的第2列为11B发包功率随温度变化的偏移值，第3列为11G、11N与11AX发包功率随温度变化的偏移值。第5列为频偏随温度变化的偏移值。
>
> 9.自动功率校准配置
> const static AUTO\_PWR\_CALI\_CONTEXT auto\_pwr
> \- 功能说明：自动功率校准配置参数。第一个参数为打开与关闭自动功率校准的开关，0是打开，1是关闭。第2-4个参数为11B 1信道，7信道，13信道，自动功率校准的阈值。第5-7个参数为11G 1信道，7信道，13信道，自动功率校准的阈值。11N与11AX基于11G自动功率校准结果偏移而来。
>
> 10.不同rate发包功率偏移表
> const INT16 shift\_tab\_b\[4\]
> const INT16 shift\_tab\_g\[8\]
> const INT16 shift\_tab\_n20\[10\]
> const INT16 shift\_tab\_n40\[10\]
> \- 功能说明：不同rate发包功率偏移表。功率校准是以11B 11M，11G 54M，11N 40M NCS7进行校准，其他rate发包功率是在校准使用的rate功率进行偏移得出。
>
> 11.配置自动功率校准参数到代码
> vnd\_cal\_set\_auto\_pwr\_thred(auto\_pwr);
> \- 功能说明：将第9条的参数配置到代码，并使用。
>
> 12.配置外部PA使用的GPIO
> vnd\_cal\_set\_epa\_config(1, GPIO\_28, GPIO\_26, pwr\_gain\_base\_gain\_b, pwr\_gain\_base\_gain\_g);
> vnd\_cal\_set\_epa\_config(0, GPIO\_28, GPIO\_26, pwr\_gain\_base\_gain\_b, pwr\_gain\_base\_gain\_g);
> \- 功能说明：配置GPIO打开或关闭外PA功能。
