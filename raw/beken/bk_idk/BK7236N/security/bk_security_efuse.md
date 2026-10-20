---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7236n/zh_CN/v2.2.1/security/bk_security_efuse.html
sdk_family: bk_idk
chip: BK7236N
processor: ''
sdk_version: v2.2.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="efuse"></a>

<a id="bk-securify-efuse"></a>

# EFUSE

<a id="id1"></a>

## 概述

EFUSE (Electrically Programming Efuse) 用于配置 BK7236N 中与安全相关的特性，只能由 0 配置成 1，无法由 1 配置成 0。

BK7236N EFUSE 共有 4x8 共 32 Bits, 在安全启动使能前，可以通过 [BKFIL](../developer-guide/config_tools/bk_tool_bkfil.md#bk-tool-bkfil) 配置，详情请参考 [EFUSE 配置](../developer-guide/config_tools/bk_config_otp_efuse.md#bk-config-otp-efuse)。

| 位 | 名字 | 描述 |
| --- | --- | --- |
| 0 | secure\_boot | 0: 安全启动未强制使能；1: 强制使能安全启动。 |
| 1 | secure\_boot\_debug\_disable | 0: 使能安全启动调试信息；1: 关闭安全启动调试信息。 |
| 2 | fast\_boot\_disable | 0: 使能快速启动；1: 关闭快速启动。 |
| 3 | download\_disable | 0: 下载模式使能；1: 下载模式禁用，使能安全启动模式。 |
| 4 | pll\_enable | 0: 安全启动使用 XTAL 时钟；1: 安全启动使能 PLL。 |
| 5 | fih\_delay\_enable | 0: 关闭随机延时；1: 使能随机延迟 (FIH delay)。 |
| 6 | power\_on\_fastboot\_disable | 0: power on 时跳过验签；1: power on 时不跳过验签。 |
| 7 | critical\_err\_disable | 0: 使能安全启动中严重错误打印；1: 关闭安全启动中严重错误打印。 |
| 8 | reserved | 保留位。 |
| 9 | flash\_ctrl\_access\_disable | 0: 允许通过 HCI 访问 flash 控制寄存器；1: 禁止通过 HCI 访问 flash 控制寄存器。 |
| 10 | deep\_lv\_fast\_boot\_disable | 0: Deep LV 快速启动到 RAM 使能；1: Deep LV 快速启动到 RAM 禁用。 |
| 11 | long\_version\_length | 0: BL1 security counter 占用 4 Bytes；1: BL1 security counter 占用 68 Bytes。 |
| 12 | secure\_download | 0: 安全下载关闭；1: 安全下载使能。 |
| 13 | bkfil\_channel\_ctrl\[0\] | bit 13/14/15 组合使用，1/7 \- BKFIL 通道关闭，0/2/3/4/5/6 \- BKFIL 通道使能。 |
| 14 | bkfil\_channel\_ctrl\[1\] | bit 13/14/15 组合使用，1/7 \- BKFIL 通道关闭，0/2/3/4/5/6 \- BKFIL 通道使能。 |
| 15 | bkfil\_channel\_ctrl\[2\] | bit 13/14/15 组合使用，1/7 \- BKFIL 通道关闭，0/2/3/4/5/6 \- BKFIL 通道使能。 |
| 16 | legacy\_boot\_high\_freq\_disable\| 0: 传统下载高频使能；1: 传统下载高频禁用。 | |
| 17 | cpu\_120m\_enable | 0: CPU 80M；1: CPU 120M。 |
| 18 | flash\_high\_freq\_enable | 0: flash XTAL 40M；1: flash 80M。 |
| 19 | cbus\_disable | 0: CBUS 端口使能；1: CBUS 端口禁用。 |
| 20 | attack\_nmi\_enable | 0: 检测到注入攻击时不产生 NMI；1: 检测到注入攻击时产生 NMI。 |
| 21 | spi\_to\_ahb\_disable | 0: SPI 到 AHB 通路不关闭；1: SPI 到 AHB 通路关闭。 |
| 22 | auto\_reset\_enable\[0\] | 温度电压异常复位控制位 0。 |
| 23 | auto\_reset\_enable\[1\] | 温度电压异常复位控制位 1。 |
| 24 | memchk\_bps\_enable | 0: 冷启动执行 memchk；1: 冷启动不做 memchk。 |
| 25 | debug\_hw\_disable | 0: 硬件调试 (JTAG) 未关闭；1: 硬件调试 (JTAG) 关闭。 |
| 26 | shanhai\_clk\_gating\_enable | 0: 硬件未使能 clk\_gating；1: 硬件使能 clk\_gating。 |
| 27 | flash\_no\_crc | 0: CRC mode；1: no CRC mode。 |
| 28 | flash\_aes\_mode | 0: FLASH AES-XTS-128 模式；1: FLASH AES-XTS-256 模式。 |
| 29 | flash\_aes\_enable | 0: FLASH AES 加密未使能；1: FLASH AES 加密使能。 |
| 30 | spi\_download\_disable | 0: SPI 下载使能；1: SPI 下载关闭。 |
| 31 | jtag\_disable | 0: 使能 CPU SWD；1: 关闭 CPU SWD。 |

<a id="bit-1-secure-boot-debug-disable"></a>

<a id="efuse-bit1"></a>

### BIT(1) \- secure\_boot\_debug\_disable

BL1 定义了两级调试信息来供用户定位问题：

> - [BIT(1)](#efuse-bit1) \- 控制普通调试信息。
> - [BIT(7)](#efuse-bit7) \- 控制严重错误。

普通调试信息除了错误之外，还包括一些流程性的日志打印。严重错误通常是指会导致 BL1 启动失败的错误，当前 BL1 支持下述严重错误:

| 错误码 | 含义 |
| --- | --- |
| 0x1 | 读 EFUSE 出错 1 |
| 0x2 | 读 EFUSE 出错 2 |
| 0x3 | 读 FLASH 出错 1 |
| 0x11 | CPU 异常 NMI |
| 0x12 | CPU 异常 MemMange |
| 0x13 | CPU 异常 HardFault |
| 0x14 | CPU 异常 BusFault |
| 0x15 | CPU 异常 UserFault |
| 0x16 | CPU 异常 SecurityFault |
| 0x21 | OTP 为空 |
| 0x22 | 公钥为空 |
| 0x23 | 跳转 BIN 校验失败 |
| 0x1xxx | OTP 读失败 |
| 0x8yyyyyyy | 验签失败 |

其中 xxx 指 OTP 的 OFFSET，yyyyyyy 指具体的验签失败点。

严重错误在打印时仅打出错误码，如 “E16” 表示CPU 异常 SecurityFault。

备注

当严重错误使能时，BL1 安全启动时并不会初始化 UART，仅当产生了不可回复的严重错误时才会初始化 UART，进行打印。
因此，严重错误并不会影响正常启动功能，也不会带来安全问题。

重要

一般在开发阶段，尤其是尚未在任何板子上成功配置过安全启动之前，建议开启普通日志，这样，可以看到更多调试信息；
在熟悉了安全启动配置之后，或者在量产阶段，应该关闭普通日志。严重错误则建议在量产版本中也不要关闭。

<a id="bit-2-fast-boot-disable"></a>

<a id="efuse-bit2"></a>

### BIT(2) \- fast boot disable

BIT(2) 置 0 时使能 Fast Boot 启动，置 1 时关闭 Fast Boot 启动。

Fast Boot 用于控制系统从 Deep Sleep 醒来的流程，当 Fast Boot 使能时，Deep Sleep 醒来后跳过安全启动，直接跳转到应用程序中；
当 Fast Boot 关闭时，则与上电重启类似，会做完整的安全启动。

重要

Fast Boot 使能时，启动速度更快，但不够安全；Fast Boot 关闭时，启动速度较慢，但安全可靠。
应用应该依据实际需求决定是否开关 Fast Boot。

<a id="bit-3-download-disable"></a>

<a id="efuse-bit3"></a>

### BIT(3) \- download\_disable

用于禁用下载模式，使能安全启动：

> - 0 \- 下载模式使能，支持传统下载。
> - 1 \- 下载模式禁用，使能安全启动模式。

<a id="bit-4-secure-boot-clock-select"></a>

<a id="efuse-bit4"></a>

### BIT(4) \- secure boot clock select

BIT(4) 用于使能/关闭安全启动高频模式。

> - 0 表示 CPU 与 FLASH 使用 XTAL 作为时钟，通常为 26Mhz。
> - 1 表示使能 PLL，CPU 与 FLASH 配置

在高频模式。在高频模式下，安全启动速度更快，对启动性能有要求的应用一般建议使能高频模式。

<a id="bit-5-random-delay-enable"></a>

<a id="efuse-bit5"></a>

### BIT(5) \- random delay enable

BIT(5) 用于控制 BootROM 中关闭判断语句的随机延迟:

> - 0 表示随机延时关闭。
> - 1 表示开启。当随机延时开启时，BL1 在调用关键函数前，都会做一个随机 delay，通过这种机制减缓 [故障注入攻击](bk_security_fih.md#fault-injection-attack) 带来的影响。

备注

随机延时使能会增加安全启动时间，除非对注入攻击防范特别高的应用，通常不建议打开随机延迟功能!

<a id="bit-6-power-on-fastboot-disable"></a>

<a id="efuse-bit6"></a>

### BIT(6) \- power\_on\_fastboot\_disable

BIT(6) 用于配置 BL1 是否跳过验签流程:

> - 0 表示每次power on启动时，都直接进入到快速验签过程。
> - 1 标志任何安全启动场景下，都需要进行完整的验签过程。

<a id="bit-7-critical-err-disable"></a>

<a id="efuse-bit7"></a>

### BIT(7) \- critical\_err\_disable

请参考 [BIT(1)](#efuse-bit1)。。

<a id="bit-20-attack-nmi"></a>

<a id="efuse-bit20"></a>

### BIT(20) \- attack NMI

BIT(20) 用于配置在检测到 [故障注入攻击](bk_security_fih.md#fault-injection-attack) 之后是否产生 NMI 异常：

> - 0 \- BL1 不会进行硬件层面的故障注入攻击检测。
> - 1 \- BL1 进行硬件层面的故障注入攻击检测，当检测到攻击时产生 NMI 异常。

备注

对故障注入攻击特别关注的应用，建议打开这个开关。

<a id="bit-21-spi-to-ahb-disable"></a>

<a id="efuse-bit21"></a>

### BIT(21) \- spi to ahb disable

BIT(21) 用于禁用 SPI 到 AHB 通道：

> - 0 \- SPI 到 AHB 通道使能。此时，通过 SPI 接口可直接操作 BK7236N 寄存器。
> - 1 \- SPI 到 AHB 通道关闭。此时，无法通过 SPI 接口操作 BK7236N 寄存器。

需要注意，BIT(21) 与 [BIT(30) spi flash download disable](#efuse-bit30) 相互独立，需要分别配置。

重要

在安全启动使能时，SPI to AHB 接必须关闭。

<a id="bit-29-flash-aes-enable"></a>

<a id="efuse-bit29"></a>

### BIT(29) \- flash\_aes\_enable

BIT(29) 用于使能 FLASH AES 加密：

> - 0 \- FLASH AES 加密不使能。
> - 1 \- FLASH AES 加密使能。此必需要配置 [FASH AES KEY](bk_security_otp.md#otp-flash-aes-key)。

<a id="bit-30-spi-download-disable"></a>

<a id="efuse-bit30"></a>

### BIT(30) \- spi\_download\_disable

关闭 SPI 下载功能:

> - 0 \- 内部 SPI FLASH 通道使能，支持 SPI 下载。
> - 1 \- 内部 SPI FLASH 通道关闭，不支持 SPI 下载。

需要注意，BIT(30) 与 [BIT(21) spi to ahb disable](#efuse-bit21) 相互独立，需要分别配置。

重要

为避免带来安全隐患，量产版本中应该禁用 SPI 下载。但在尚未成功部署安全启动之前，可先不要禁用 SPI 下载，
这样，当安全启动部署失败时，依然可通过 SPI 下载将版本下载到 FLASH。否则，一旦安全启动部署失败，就再
也无法下载版本，板子变砖。

<a id="bit-31-jtag-disable"></a>

<a id="efuse-bit31"></a>

### BIT(31) \- jtag\_disable

BIT(31) 用于控制 CPU 调试口的开关:

> - 0 \- CPU 调试开启，BK7236N 支持 SWD 调试。
> - 1 \- CPU 调试关闭。此时，必须通过 [安全调试](bk_security_debug.md#security-secure-debug) 才能使能 CPU 调试功能。

重要

安全启动使能时，需要关闭 SWD 调试。
