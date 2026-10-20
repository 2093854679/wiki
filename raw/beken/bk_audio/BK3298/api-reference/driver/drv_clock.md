---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_clock.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-clock"></a>

# DRV\_CLOCK

<a id="drv-clock-api-status"></a>

## DRV\_CLOCK API Status

| API |
| --- |
| [`drv_clk_dpll_enable()`](#_CPPv419drv_clk_dpll_enable8uint32_t "drv_clk_dpll_enable") |
| [`drv_clk_dpll_disable()`](#_CPPv420drv_clk_dpll_disablev "drv_clk_dpll_disable") |
| [`drv_clk_dpll_calibration()`](#_CPPv424drv_clk_dpll_calibrationv "drv_clk_dpll_calibration") |
| [`drv_clk_rc32k_calibration()`](#_CPPv425drv_clk_rc32k_calibrationb "drv_clk_rc32k_calibration") |
| [`drv_clk_rc32k_fine_tuning()`](#_CPPv425drv_clk_rc32k_fine_tuning7int32_t8uint32_t "drv_clk_rc32k_fine_tuning") |
| [`drv_clk_xtal26M_lowpower_en()`](#_CPPv427drv_clk_xtal26M_lowpower_enb "drv_clk_xtal26M_lowpower_en") |
| [`drv_clk_xtal26M_fine_tuning()`](#_CPPv427drv_clk_xtal26M_fine_tuning7int32_t "drv_clk_xtal26M_fine_tuning") |
| [`drv_clk_test_buf_for_dpll()`](#_CPPv425drv_clk_test_buf_for_dpllv "drv_clk_test_buf_for_dpll") |
| [`drv_clk_apll_enable()`](#_CPPv419drv_clk_apll_enablef "drv_clk_apll_enable") |
| [`drv_clk_apll_disable()`](#_CPPv420drv_clk_apll_disablev "drv_clk_apll_disable") |
| [`drv_clk_apll_calibration()`](#_CPPv424drv_clk_apll_calibrationf "drv_clk_apll_calibration") |
| [`drv_clk_apll_unlock_det_en()`](#_CPPv426drv_clk_apll_unlock_det_enb "drv_clk_apll_unlock_det_en") |
| [`drv_clk_apll_fine_tuning()`](#_CPPv424drv_clk_apll_fine_tuning7int32_t "drv_clk_apll_fine_tuning") |

<a id="drv-clock-api-reference"></a>

## DRV\_CLOCK API Reference

<a id="header-file"></a>

### Header File

- [driver/clock/drv\_clk.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/clock/drv_clk.h)

<a id="functions"></a>

### Functions

<a id="_CPPv419drv_clk_dpll_enable8uint32_t"></a>

<a id="_CPPv319drv_clk_dpll_enable8uint32_t"></a> <a id="_CPPv219drv_clk_dpll_enable8uint32_t"></a> <a id="drv_clk_dpll_enable__uint32_t"></a> <a id="drv__clk_8h_1a6b4d14dde12f5bee865536c3a5487398"></a> int32\_t drv\_clk\_dpll\_enable(uint32\_t req\_freq\_Mhz)
:   打开DPLL，并提供对应的频率输出.

    这里只是打开DPLL，对应的模块是否使用该clock还需要手动切换

    参数:
    :   **req\_freq\_Mhz** – **\[in\]** 期望的PLL输出的频率，单位是Mhz

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420drv_clk_dpll_disablev"></a>

<a id="_CPPv320drv_clk_dpll_disablev"></a> <a id="_CPPv220drv_clk_dpll_disablev"></a> <a id="drv_clk_dpll_disable__void"></a> <a id="drv__clk_8h_1ad53eeb4acb19784f63d4d4105fb33a88"></a> int32\_t drv\_clk\_dpll\_disable(void)
:   关闭DPLL

    关闭前使用到DPLL的模块需要先进行切换，否则会挂掉

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424drv_clk_dpll_calibrationv"></a>

<a id="_CPPv324drv_clk_dpll_calibrationv"></a> <a id="_CPPv224drv_clk_dpll_calibrationv"></a> <a id="drv_clk_dpll_calibration__void"></a> <a id="drv__clk_8h_1a4f067f2f7def934dea6dd7b4b641de0a"></a> int32\_t drv\_clk\_dpll\_calibration(void)
:   对DPLL进行校准.

    先要打开DPLL才调用该函数进行校准，在以下几种情况需要校准 第一次开机或者从下电后的唤醒启动 改变频率或者温度改变太大

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419drv_clk_apll_enablef"></a>

<a id="_CPPv319drv_clk_apll_enablef"></a> <a id="_CPPv219drv_clk_apll_enablef"></a> <a id="drv_clk_apll_enable__float"></a> <a id="drv__clk_8h_1a03219669538b2a82256b1f4a9de8308e"></a> int32\_t drv\_clk\_apll\_enable(float req\_freq\_Mhz)
:   打开APLL，并提供对应的频率输出.

    这里只是打开APLL，对应的模块是否使用该clock还需要手动切换

    参数:
    :   **req\_freq\_Mhz** – **\[in\]** 期望的PLL输出的频率，单位是Mhz

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420drv_clk_apll_disablev"></a>

<a id="_CPPv320drv_clk_apll_disablev"></a> <a id="_CPPv220drv_clk_apll_disablev"></a> <a id="drv_clk_apll_disable__void"></a> <a id="drv__clk_8h_1ab06f96acc01c5429b3745d654d7b8444"></a> int32\_t drv\_clk\_apll\_disable(void)
:   关闭APLL

    关闭前使用到APLL的模块需要先进行切换，否则会挂掉

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422drv_clk_apll_is_activev"></a>

<a id="_CPPv322drv_clk_apll_is_activev"></a> <a id="_CPPv222drv_clk_apll_is_activev"></a> <a id="drv_clk_apll_is_active__void"></a> <a id="drv__clk_8h_1aaad0ab984a2766aa8fa68737874d876c"></a> bool drv\_clk\_apll\_is\_active(void)
:   check if APLL is active or not.

    返回值:
    :   - **true** – active
        - **false** – inactive

    返回:
    :   active status

<a id="_CPPv424drv_clk_apll_calibrationf"></a>

<a id="_CPPv324drv_clk_apll_calibrationf"></a> <a id="_CPPv224drv_clk_apll_calibrationf"></a> <a id="drv_clk_apll_calibration__float"></a> <a id="drv__clk_8h_1a80f62706b71bfa553ffde0a70008b322"></a> int32\_t drv\_clk\_apll\_calibration(float req\_freq\_Mhz)
:   对APLL进行校准.

    先要打开APLL才调用该函数进行校准

    参数:
    :   **req\_freq\_Mhz** – **\[in\]** 期望的PLL输出的频率，单位是Mhz

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426drv_clk_apll_unlock_det_enb"></a>

<a id="_CPPv326drv_clk_apll_unlock_det_enb"></a> <a id="_CPPv226drv_clk_apll_unlock_det_enb"></a> <a id="drv_clk_apll_unlock_det_en__b"></a> <a id="drv__clk_8h_1ab2e15b1be3c8d870f70948e39b6e50e0"></a> int32\_t drv\_clk\_apll\_unlock\_det\_en(bool enable)
:   打开APLL的失锁检测功能

    参数:
    :   **enable** – **\[in\]** true:打开检测功能 false:关闭检测

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424drv_clk_apll_fine_tuning7int32_t"></a>

<a id="_CPPv324drv_clk_apll_fine_tuning7int32_t"></a> <a id="_CPPv224drv_clk_apll_fine_tuning7int32_t"></a> <a id="drv_clk_apll_fine_tuning__int32_t"></a> <a id="drv__clk_8h_1a1b23a159bd2df85ef81ccf01097b5bb7"></a> int32\_t drv\_clk\_apll\_fine\_tuning(int32\_t adjust\_val)
:   APLL 微调

    微调APLL的clock

    参数:
    :   **adjust\_val** – **\[in\]** \>0 频率升高 \<0 频率降低

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425drv_clk_rc32k_calibrationb"></a>

<a id="_CPPv325drv_clk_rc32k_calibrationb"></a> <a id="_CPPv225drv_clk_rc32k_calibrationb"></a> <a id="drv_clk_rc32k_calibration__b"></a> <a id="drv__clk_8h_1a29b5de4457fb221f7c026c1146d95c27"></a> int32\_t drv\_clk\_rc32k\_calibration(bool first\_cal)
:   RC32K calibration,.

    手动触发32K的校准，校准完成时间需要25ms

    参数:
    :   **first\_cal** – **\[in\]** true: first calibration

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425drv_clk_rc32k_fine_tuning7int32_t8uint32_t"></a>

<a id="_CPPv325drv_clk_rc32k_fine_tuning7int32_t8uint32_t"></a> <a id="_CPPv225drv_clk_rc32k_fine_tuning7int32_t8uint32_t"></a> <a id="drv_clk_rc32k_fine_tuning__int32_t.uint32_t"></a> <a id="drv__clk_8h_1aee0f762b9dbc11871c05306619646f17"></a> int32\_t drv\_clk\_rc32k\_fine\_tuning(int32\_t fine\_val, uint32\_t coarse\_val)
:   RC32K 微调

    手动控制或者微调32K

    参数:
    :   - **fine\_val** – **\[in\]** 变大频率升高 变小频率降低
        - **coarse\_val** – **\[in\]** 默认粗调值

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv432drv_clk_rc32k_manual_fine_tuning7int32_t"></a>

<a id="_CPPv332drv_clk_rc32k_manual_fine_tuning7int32_t"></a> <a id="_CPPv232drv_clk_rc32k_manual_fine_tuning7int32_t"></a> <a id="drv_clk_rc32k_manual_fine_tuning__int32_t"></a> <a id="drv__clk_8h_1acffd1b589890b58f0284f4a84df02dca"></a> int32\_t drv\_clk\_rc32k\_manual\_fine\_tuning(int32\_t adjust\_val)
:   RC32K 手动微调

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv434drv_clk_rc32k_manual_coarse_tuning7int32_t"></a>

<a id="_CPPv334drv_clk_rc32k_manual_coarse_tuning7int32_t"></a> <a id="_CPPv234drv_clk_rc32k_manual_coarse_tuning7int32_t"></a> <a id="drv_clk_rc32k_manual_coarse_tuning__int32_t"></a> <a id="drv__clk_8h_1a82d79790d4b05b2c29b36d75b656e588"></a> int32\_t drv\_clk\_rc32k\_manual\_coarse\_tuning(int32\_t adjust\_val)
:   RC32K 手动粗调

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv428drv_clk_get_rc32k_fine_valuev"></a>

<a id="_CPPv328drv_clk_get_rc32k_fine_valuev"></a> <a id="_CPPv228drv_clk_get_rc32k_fine_valuev"></a> <a id="drv_clk_get_rc32k_fine_value__void"></a> <a id="drv__clk_8h_1a25556a3bbfc62088ba4aac17983b69d5"></a> int32\_t drv\_clk\_get\_rc32k\_fine\_value(void)

<a id="_CPPv428drv_clk_set_rc32k_fine_value7int32_t"></a>

<a id="_CPPv328drv_clk_set_rc32k_fine_value7int32_t"></a> <a id="_CPPv228drv_clk_set_rc32k_fine_value7int32_t"></a> <a id="drv_clk_set_rc32k_fine_value__int32_t"></a> <a id="drv__clk_8h_1a9402f94ebbec6c9bf1c6446b8d856b90"></a> int32\_t drv\_clk\_set\_rc32k\_fine\_value(int32\_t fine\_val)

<a id="_CPPv426drv_clk_rc32k_tuning_force7int32_t8uint32_t"></a>

<a id="_CPPv326drv_clk_rc32k_tuning_force7int32_t8uint32_t"></a> <a id="_CPPv226drv_clk_rc32k_tuning_force7int32_t8uint32_t"></a> <a id="drv_clk_rc32k_tuning_force__int32_t.uint32_t"></a> <a id="drv__clk_8h_1ad718574aef9c7c223abc333404934c6c"></a> int32\_t drv\_clk\_rc32k\_tuning\_force(int32\_t fine\_val, uint32\_t coarse\_val)
:   直接控制rc32k调整参数，用于校准时使用

    参数:
    :   - **fine\_val** – **\[in\]** 细调参数
        - **coarse\_val** – **\[in\]** 粗调参数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427drv_clk_xtal26M_lowpower_enb"></a>

<a id="_CPPv327drv_clk_xtal26M_lowpower_enb"></a> <a id="_CPPv227drv_clk_xtal26M_lowpower_enb"></a> <a id="drv_clk_xtal26M_lowpower_en__b"></a> <a id="drv__clk_8h_1aec5a5ebd4ac0e8980392135690c330da"></a> int32\_t drv\_clk\_xtal26M\_lowpower\_en(bool enable)
:   26M low power设定

    在RF没有工作的时候可以设置26M进低功耗

    参数:
    :   **enable** – **\[in\]** true: 进low power false: 退出low power

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv427drv_clk_xtal26M_fine_tuning7int32_t"></a>

<a id="_CPPv327drv_clk_xtal26M_fine_tuning7int32_t"></a> <a id="_CPPv227drv_clk_xtal26M_fine_tuning7int32_t"></a> <a id="drv_clk_xtal26M_fine_tuning__int32_t"></a> <a id="drv__clk_8h_1a3408a901e9b8273926f8d416fbb9d415"></a> int32\_t drv\_clk\_xtal26M\_fine\_tuning(int32\_t adjust\_val)
:   26M 微调

    参数:
    :   **adjust\_val** – **\[in\]** \>0 频率升高 \<0 频率降低

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425drv_clk_test_buf_for_dpllv"></a>

<a id="_CPPv325drv_clk_test_buf_for_dpllv"></a> <a id="_CPPv225drv_clk_test_buf_for_dpllv"></a> <a id="drv_clk_test_buf_for_dpll__void"></a> <a id="drv__clk_8h_1ab49deac2443972a1d3e6c9eecb9ceaa3"></a> void drv\_clk\_test\_buf\_for\_dpll(void)

<a id="_CPPv425drv_clk_test_buf_for_apllv"></a>

<a id="_CPPv325drv_clk_test_buf_for_apllv"></a> <a id="_CPPv225drv_clk_test_buf_for_apllv"></a> <a id="drv_clk_test_buf_for_apll__void"></a> <a id="drv__clk_8h_1ac392c03d70c41b3faaca47a4fc56bc69"></a> void drv\_clk\_test\_buf\_for\_apll(void)

<a id="macros"></a>

### Macros

<a id="c.COARSE_DEFAULT_VALUE"></a>

<a id="drv__clk_8h_1aaba58790b3b0a27b69679dfd904198c8"></a> COARSE\_DEFAULT\_VALUE

<a id="c.FINE_DEFAULT_VALUE"></a>

<a id="drv__clk_8h_1afe6b3291e45fda482ca1790cc69729ec"></a> FINE\_DEFAULT\_VALUE
