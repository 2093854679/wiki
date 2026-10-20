---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7235/zh_CN/v1.5/developer-guide/porting/index.html
sdk_family: bk_idk
chip: BK7235
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="os"></a>

# OS移植介绍

本章节以BK7256 RISC-V架构鸿蒙OS移植为例

> - 操作系统内核源码路径：components/os\_source/
> - 操作系统内核源码在components/os\_source/CMakeLists.txt中修改添加到Armino平台编译
> - 在components/bk\_rtos/Kconfig中定义操作系统相关的宏
>
>   ```
>   menu "LITEOS_M"
>
>       config LITEOS_M
>           bool "liteos_m"
>           default n
>
>       config LITEOS_M_V3
>           bool "liteos_m v3.0.1-LTS"
>           default n
>
>
>       config LITEOS_M_BK
>           depends on LITEOS_M_V3
>               bool "liteos_m bk adapter"
>               default n
>   endmenu
>   ```
> - 增加鸿蒙工程：projects/harmony
> - 配置操作系统相关的宏定义：projects/harmony/sdkconfig.defaults
>
>   ```
>   # LITEOS_M
>   CONFIG_LITEOS_M_V3=y
>   CONFIG_LITEOS_M_BK=y
>
>   # FreeRTOS
>   CONFIG_FREERTOS=n
>   CONFIG_FREERTOS_V9=n
>   CONFIG_FREERTOS_V10=n
>   ```
> - 实现OS抽象层接口：components/bk\_rtos/liteos\_m\_v3/rtos\_pub.c
> - 创建系统启动汇编代码：middleware/arch/riscv/boot\_vectors\_liteos\_m.S
> - RISC-V的关键寄存器：设置中断和异常入口：
>
>   ```
>   /* Initial machine trap-vector Base.*/
>   la t0, HalTrapVector
>   csrw mtvec, t0
>   ```
> - 适配异常处理函数：trap\_handler
>   在components/os\_source/liteos\_m\_v3/kernel/arch/risc-v/riscv32/gcc/los\_exc.S中修改HalTrapEntry
> - 中断入口：HalHwiInterruptDone
> - 注册Armino平台外部中断处理函数：vPortSetupMEXTInterrupt
> - 注册Armino平台MTIME中断处理函数：vPortSetupTimerInterrupt
> - 在调度之前注册外部中断和MTIME中断
>
>   ```
>   LITE_OS_SEC_TEXT_INIT UINT32 HalStartSchedule(VOID)
>   {
>       (VOID)LOS_IntLock();
>       OsSchedStart();
>
>   #if CONFIG_LITEOS_M_BK
>       vPortSetupTimerInterrupt();
>       vPortSetupMEXTInterrupt();
>   #endif
>
>       HalStartToRun();
>       return LOS_OK; /* never return */
>   }
>   ```
> - BK7256 RISC-V的mtime寄存器是64位，适配的时候需要注意最大值的定义类型。
