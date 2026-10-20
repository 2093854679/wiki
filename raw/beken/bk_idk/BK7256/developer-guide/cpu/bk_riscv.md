---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/developer-guide/cpu/bk_riscv.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="risc-v-guide"></a>

# RISC-V Guide

<a id="id1"></a>

## 简介

BK7256使用的是Andes Technology(晶心科技)的双核CPU（D25F核），基于RISC-V指令集架构

<a id="andes"></a>

## Andes官网

> - Andes官网： <http://www.andestech.com>
> - AndeSight 工具下载路径： <https://github.com/andestech/Andes-Development-Kit/releases>
> - Andes CPU (D25F核)编译工具链开源代码: <https://github.com/andestech/nds-gnu-toolchain>

<a id="id2"></a>

## Andes相关文档

> > 软件安装之后，在安装目录下：以Windows为例，D:ToolsAndestechAndeSight\_STD\_v510doc
>
> - 《AMSI\_Drivers\_and\_Demos\_Application\_Note\_AN031\_V1.3.pdf》
>   :   —Andes MCU Software Interface (AMSI) Drivers and Demos Application Note
> - 《AndeSight\_STD\_v5.1\_IDE\_Quick\_Start\_Guide\_UM250\_V1.0.pdf》
>   :   —AndeSight IDE用户快速入门向导手册
> - 《AndeSight\_STD\_v5.0\_IDE\_User\_Manual\_UM230\_V1.1.pdf》
>   :   —AndeSight IDE用户手册
> - 《AndeSight\_STD\_v5.1\_Installation\_Guide\_UM251\_V1.0.pdf》
>   :   —AndeSight IDE安装手册
> - 《AndeSight\_STD\_v5.1\_Release\_Notes\_RN312\_V1.0.pdf》
>   :   —AndeSight IDE软件Release Note
> - 《AndeSight\_v5.1\_BSP\_User\_Manual\_UM255\_V1.0.pdf》
>   :   —AndeSight BSP用户手册
> - 《AndeStar\_V5\_CLIC\_Spec\_UM205\_V1.0.pdf》
>   :   —Andes CLIC架构介绍，Armino平台7256系列产品使用PLIC架构
> - 《AndeStar\_V5\_SPA\_UM164\_V1.5.pdf》
>   :   —AndeStar系统架构和CSR文档
> - 《AndeStar\_V5\_ISA\_Spec\_UM165\_V1.4.pdf》
>   :   —AndeStar V5 Instruction Extension Specification 扩展指令介绍
> - 《AndeStar\_V5\_PLIC\_UM166\_V1.3.pdf》
>   :   —Andes PLIC架构介绍，Armino平台7256系列产品使用PLIC架构
> - 《AndeStar\_V5\_SPA\_UM164\_V1.5.pdf》
>   :   —AndeStar系统架构和CSR文档
> - 《AndeStar\_V5\_Timer\_UM167\_V1.1.pdf》
>   :   —Andes CPU内部mtimer相关介绍
> - 《Andes\_AMP\_System\_for\_Bare\_Metal\_and\_RTOS\_Application\_Note\_AN060\_V1.0.pdf》
> - 《Andes\_DSP\_Library\_V5\_User\_Manual\_UM179\_V2.1.pdf》
> - 《Andes\_ICE\_Management\_Software\_UM067\_V3.3.pdf》
>   :   —Andes ICE Management软件介绍，类似JLink的GDBServer
> - 《Andes\_Neural\_Network\_Library\_User\_Manual\_UM232\_V2.1.pdf》
> - 《Andes\_Programming\_Guide\_for\_ISA\_V5\_PG012\_V2.6.pdf》
>   :   —Andes编程指南
> - 《The\_RISC-V\_Instruction\_Set\_Manual\_Volume\_II\_Privileged\_Architecture\_TD002\_V1.10.pdf》
>   :   —Andes RISCV指令集
> - 《The\_RISC-V\_Instruction\_Set\_Manual\_Volume\_I\_User-Level\_ISA\_TD001\_V2.2.pdf》
>   :   —Andes RISCV指令集(User-Level)

<a id="andes-sagld"></a>

## Andes sag转ld文件方法

> 1. 通过D:\\Tools\\Andestech\\AndeSight\_STD\_v510\\toolchains\\nds32le-elf-mculib-v5\\cygwin-andes.bat 进入cygwin
> 2. 进入D:\\Tools\\Andestech\\AndeSight\_STD\_v510\\utils目录，将sag文件放入该目录下

在cygwin环境执行如下命令:

```
nds_ldsag.exe --version=v5 -t ./nds32_template_v5.txt bk7256_bsp.sag -o bk7256_bsp.ld
```
