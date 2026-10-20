---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_sys/app_sys_comm.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="system-common-layer-application-functions"></a>

# System Common Layer Application Functions

<a id="app-sys-comm-api-brief"></a>

## APP\_SYS\_COMM API Brief

| Application | Brief |
| --- | --- |
| [`app_sys_power_init()`](#_CPPv418app_sys_power_initv "app_sys_power_init") | device module power initialize |
| [`app_sys_preinit()`](#_CPPv415app_sys_preinitv "app_sys_preinit") | preinitialize include low level initialize and memheap initialize |
| [`app_sys_cpu_init()`](#_CPPv416app_sys_cpu_initv "app_sys_cpu_init") | cpu setting initialize |
| [`app_sys_driver_init()`](#_CPPv419app_sys_driver_initv "app_sys_driver_init") | system driver initialize |
| [`app_sys_service_init()`](#_CPPv420app_sys_service_initv "app_sys_service_init") | system service initialize |
| [`app_sys_shutdown()`](#_CPPv416app_sys_shutdownv "app_sys_shutdown") | execute system shutdown |
| [`app_sys_shutdown_condition()`](#_CPPv426app_sys_shutdown_condition7int32_t "app_sys_shutdown_condition") | execute system shutdown with condition |
| [`app_sys_env_stored()`](#_CPPv418app_sys_env_storedv "app_sys_env_stored") | save environment data |
| [`app_sys_start_button_check()`](#_CPPv426app_sys_start_button_checkv "app_sys_start_button_check") | system need to power on or not |
| [`app_sys_force_reboot()`](#_CPPv420app_sys_force_reboot7uint8_t "app_sys_force_reboot") | execute force reboot |

<a id="app-sys-comm-api-reference"></a>

## APP\_SYS\_COMM API Reference

<a id="header-file"></a>

### Header File

- [common/app\_sys/app\_sys\_comm.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_sys/app_sys_comm.h)

<a id="functions"></a>

### Functions

<a id="_CPPv418app_sys_power_initv"></a>

<a id="_CPPv318app_sys_power_initv"></a> <a id="_CPPv218app_sys_power_initv"></a> <a id="app_sys_power_init__void"></a> <a id="app__sys__comm_8h_1ae8ddb6c50409098747c72b52f05826fd"></a> int32\_t app\_sys\_power\_init(void)
:   device module power initialize.

    系统模块上电初始化

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv415app_sys_preinitv"></a>

<a id="_CPPv315app_sys_preinitv"></a> <a id="_CPPv215app_sys_preinitv"></a> <a id="app_sys_preinit__void"></a> <a id="app__sys__comm_8h_1ac0eefe36053f56de71d2b6f713dd1fc2"></a> int32\_t app\_sys\_preinit(void)
:   low level initialize.

    最初需要的初始化动作

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416app_sys_cpu_initv"></a>

<a id="_CPPv316app_sys_cpu_initv"></a> <a id="_CPPv216app_sys_cpu_initv"></a> <a id="app_sys_cpu_init__void"></a> <a id="app__sys__comm_8h_1a4203139f25aab97a429a61b761f530b1"></a> int32\_t app\_sys\_cpu\_init(void)
:   cpu setting initialize

    init cpu environment and set interrupt priority

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419app_sys_driver_initv"></a>

<a id="_CPPv319app_sys_driver_initv"></a> <a id="_CPPv219app_sys_driver_initv"></a> <a id="app_sys_driver_init__void"></a> <a id="app__sys__comm_8h_1aba0b171becd919801ff932283e6806c5"></a> int32\_t app\_sys\_driver\_init(void)
:   system driver initialize

    init system driver and clear all pending interrupt

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420app_sys_service_initv"></a>

<a id="_CPPv320app_sys_service_initv"></a> <a id="_CPPv220app_sys_service_initv"></a> <a id="app_sys_service_init__void"></a> <a id="app__sys__comm_8h_1a4873cd53be2a436a6512a1a412de5636"></a> int32\_t app\_sys\_service\_init(void)
:   system service initialize

    init BEKEN log service and rtos service

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416app_sys_shutdownv"></a>

<a id="_CPPv316app_sys_shutdownv"></a> <a id="_CPPv216app_sys_shutdownv"></a> <a id="app_sys_shutdown__void"></a> <a id="app__sys__comm_8h_1a298c8310ecd34d8fc7b439360aaaa632"></a> int32\_t app\_sys\_shutdown(void)
:   execute system shutdown

    disable interrupt, save environment data and execut shutdown process

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv425app_sys_power_calibrationv"></a>

<a id="_CPPv325app_sys_power_calibrationv"></a> <a id="_CPPv225app_sys_power_calibrationv"></a> <a id="app_sys_power_calibration__void"></a> <a id="app__sys__comm_8h_1a9e9bc79a1e70af93d0ee83fde8da749d"></a> int32\_t app\_sys\_power\_calibration(void)
:   system power voltage calibration

    voltage calibration

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426app_sys_shutdown_condition7int32_t"></a>

<a id="_CPPv326app_sys_shutdown_condition7int32_t"></a> <a id="_CPPv226app_sys_shutdown_condition7int32_t"></a> <a id="app_sys_shutdown_condition__int32_t"></a> <a id="app__sys__comm_8h_1a758627a19d3b9188a24b14ac4be184d3"></a> int32\_t app\_sys\_shutdown\_condition(int32\_t cond)
:   execute system shutdown with condition

    参数:
    :   **cond** – **\[in\]** 匹配的条件

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv418app_sys_env_storedv"></a>

<a id="_CPPv318app_sys_env_storedv"></a> <a id="_CPPv218app_sys_env_storedv"></a> <a id="app_sys_env_stored__void"></a> <a id="app__sys__comm_8h_1a05ae34653774ec0ea735f871e02af121"></a> int32\_t app\_sys\_env\_stored(void)
:   save environment data

    flash log data, un-initialize led setting and save environment data into flash

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426app_sys_start_button_checkv"></a>

<a id="_CPPv326app_sys_start_button_checkv"></a> <a id="_CPPv226app_sys_start_button_checkv"></a> <a id="app_sys_start_button_check__void"></a> <a id="app__sys__comm_8h_1af28b0081868241688e1e78da16641a24"></a> int32\_t app\_sys\_start\_button\_check(void)
:   system need to power on or not

    check system power setting and execute power-on process if necessary

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420app_sys_force_reboot7uint8_t"></a>

<a id="_CPPv320app_sys_force_reboot7uint8_t"></a> <a id="_CPPv220app_sys_force_reboot7uint8_t"></a> <a id="app_sys_force_reboot__uint8_t"></a> <a id="app__sys__comm_8h_1a4be563ae1a2803b795fd93d8bc70ca52"></a> void app\_sys\_force\_reboot(uint8\_t reboot\_method)
:   execute force reboot

    enable watch dog and wait for reset

    参数:
    :   **reboot\_method** – **\[in\]** reboot method(watch dog or rtc)

    返回:
    :   N/A

<a id="macros"></a>

### Macros

<a id="c.REBOOT_USE_WDT"></a>

<a id="app__sys__comm_8h_1aed0a13f1e0c9e4ffd45eeee353fa0e6c"></a> REBOOT\_USE\_WDT

<a id="c.REBOOT_USE_RTC"></a>

<a id="app__sys__comm_8h_1a48fd73f99ca33c0b39f52d8f44c0d1a7"></a> REBOOT\_USE\_RTC
