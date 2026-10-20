---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/component/cpu_freq.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="cpu-freq"></a>

# CPU\_FREQ

<a id="cpu-freq-api-status"></a>

## CPU\_FREQ API Status

| API |
| --- |
| [`bk_cpu_freq_acquire()`](#_CPPv419bk_cpu_freq_acquire8uint32_t "bk_cpu_freq_acquire") |
| [`bk_cpu_freq_release()`](#_CPPv419bk_cpu_freq_release8uint32_t "bk_cpu_freq_release") |
| [`bk_cpu_freq_get_current_sys_clock()`](#_CPPv433bk_cpu_freq_get_current_sys_clockv "bk_cpu_freq_get_current_sys_clock") |

<a id="cpu-freq-api-reference"></a>

## CPU\_FREQ API Reference

<a id="header-file"></a>

### Header File

- [component/cpu\_freq/cpu\_freq.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/component/cpu_freq/cpu_freq.h)

<a id="functions"></a>

### Functions

<a id="_CPPv419bk_cpu_freq_acquire8uint32_t"></a>

<a id="_CPPv319bk_cpu_freq_acquire8uint32_t"></a> <a id="_CPPv219bk_cpu_freq_acquire8uint32_t"></a> <a id="bk_cpu_freq_acquire__uint32_t"></a> <a id="cpu__freq_8h_1ad9d86fd6277f888d6300a593dca4c98b"></a> int32\_t bk\_cpu\_freq\_acquire(uint32\_t clk\_hz)
:   request the default cpu work on the desired clock:clk\_hz

    用户期望调整cpu到一个工作频率时调用

    参数:
    :   **clk\_hz** – **\[in\]** desired cpu clock in hz, see the define CPU\_FREQ\_xxM

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419bk_cpu_freq_release8uint32_t"></a>

<a id="_CPPv319bk_cpu_freq_release8uint32_t"></a> <a id="_CPPv219bk_cpu_freq_release8uint32_t"></a> <a id="bk_cpu_freq_release__uint32_t"></a> <a id="cpu__freq_8h_1ac71f81997e20f31c68d493448b400f6b"></a> int32\_t bk\_cpu\_freq\_release(uint32\_t clk\_hz)
:   tell the default cpu do not need to work on the desired clock:clk\_hz

    用户不再期望cpu工作在该频率时调用，一般是和 [bk\_cpu\_freq\_acquire()](#cpu__freq_8h_1ad9d86fd6277f888d6300a593dca4c98b) 配套调用

    参数:
    :   **clk\_hz** – **\[in\]** desired cpu clock in hz, see the define CPU\_FREQ\_xxM

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv433bk_cpu_freq_get_current_sys_clockv"></a>

<a id="_CPPv333bk_cpu_freq_get_current_sys_clockv"></a> <a id="_CPPv233bk_cpu_freq_get_current_sys_clockv"></a> <a id="bk_cpu_freq_get_current_sys_clock__void"></a> <a id="cpu__freq_8h_1a72638e65c99adab611e36f0f3a050d6b"></a> uint16\_t bk\_cpu\_freq\_get\_current\_sys\_clock(void)
:   get current system clock (cpu/bus clock)

    返回:
    :   current system clock

<a id="macros"></a>

### Macros

<a id="c.CPU_FREQ_26M"></a>

<a id="cpu__freq_8h_1aab0d79dbfbc306f93236097bdc2dd11d"></a> CPU\_FREQ\_26M

<a id="c.CPU_FREQ_32M"></a>

<a id="cpu__freq_8h_1a7749b26d0dd3fbd177c0025e4eff061d"></a> CPU\_FREQ\_32M

<a id="c.CPU_FREQ_40M"></a>

<a id="cpu__freq_8h_1a141461736a5d5b72d4ea45cb53a36e94"></a> CPU\_FREQ\_40M

<a id="c.CPU_FREQ_48M"></a>

<a id="cpu__freq_8h_1a5859399e4e3058cfb8040d9014aade91"></a> CPU\_FREQ\_48M

<a id="c.CPU_FREQ_52M"></a>

<a id="cpu__freq_8h_1ae7d1f2e762dc92c37b30c423364cca0c"></a> CPU\_FREQ\_52M

<a id="c.CPU_FREQ_78M"></a>

<a id="cpu__freq_8h_1a76c9db18b88609ad59407f3196f45a9d"></a> CPU\_FREQ\_78M

<a id="c.CPU_FREQ_96M"></a>

<a id="cpu__freq_8h_1a358e76e6606613f88d6e42f16fec4145"></a> CPU\_FREQ\_96M

<a id="c.CPU_FREQ_104M"></a>

<a id="cpu__freq_8h_1a8b29668d4f32ce8f193dd258fdd531f8"></a> CPU\_FREQ\_104M

<a id="c.CPU_FREQ_120M"></a>

<a id="cpu__freq_8h_1afd8ad05f2917a10960fa7a7908e5125b"></a> CPU\_FREQ\_120M

<a id="c.CPU_FREQ_156M"></a>

<a id="cpu__freq_8h_1aee4e94859e03442831995f184660e386"></a> CPU\_FREQ\_156M

<a id="c.CPU_FREQ_312M"></a>

<a id="cpu__freq_8h_1aea33ed2de902e72e3eb48af8f4dd78c5"></a> CPU\_FREQ\_312M

<a id="c.CPU_FREQ_ON_XTAL"></a>

<a id="cpu__freq_8h_1ad76dc09d8d19f79050cb98d50aae81ab"></a> CPU\_FREQ\_ON\_XTAL

<a id="c.CPU_FREQ_MAX_CLK"></a>

<a id="cpu__freq_8h_1ac17dde29bcf1966f6efcedf91955ec32"></a> CPU\_FREQ\_MAX\_CLK

<a id="c.CPU_FREQ_MAX_CLK_UP_VOL_LVL1"></a>

<a id="cpu__freq_8h_1aeab88e45d0db7cc6fdd363a1c68f4720"></a> CPU\_FREQ\_MAX\_CLK\_UP\_VOL\_LVL1

<a id="c.CPU_FREQ_MAX_CLK_UP_VOL_LVL2"></a>

<a id="cpu__freq_8h_1abd78e88ca9298385453e6d61c1095650"></a> CPU\_FREQ\_MAX\_CLK\_UP\_VOL\_LVL2

<a id="c.CPU_FREQ_MAX_CLK_UP_VOL_LVL3"></a>

<a id="cpu__freq_8h_1a4395b48375a2199946a86b86f52a5d90"></a> CPU\_FREQ\_MAX\_CLK\_UP\_VOL\_LVL3

<a id="c.SYS_VDDDIG_VOL_LVL1"></a>

<a id="cpu__freq_8h_1aa175555d50ac6e21d392f1fd7193f680"></a> SYS\_VDDDIG\_VOL\_LVL1

<a id="c.SYS_VDDDIG_VOL_LVL2"></a>

<a id="cpu__freq_8h_1a46d891508e1d3c1cd0661df4ec852450"></a> SYS\_VDDDIG\_VOL\_LVL2

<a id="c.SYS_VDDDIG_VOL_LVL3"></a>

<a id="cpu__freq_8h_1a81044ca0e93f8b2a6ef6bbb95dd9423d"></a> SYS\_VDDDIG\_VOL\_LVL3

<a id="c.SYS_VDDDIG_VOL_LVL4"></a>

<a id="cpu__freq_8h_1ab76fad4dc330ce432805a6a1b7fae549"></a> SYS\_VDDDIG\_VOL\_LVL4

<a id="c.BK_CPU_FREQ_ACQUIRE"></a>

<a id="cpu__freq_8h_1a7947f88aa05c7be4ea9b8bfe0af6ab9f"></a> BK\_CPU\_FREQ\_ACQUIRE(x)

<a id="c.BK_CPU_FREQ_RELEASE"></a>

<a id="cpu__freq_8h_1aa3efe89004ad1dcf5d0fd32ae665eb2e"></a> BK\_CPU\_FREQ\_RELEASE(x)
