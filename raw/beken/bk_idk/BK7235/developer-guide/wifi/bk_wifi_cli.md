---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7235/zh_CN/v1.5/developer-guide/wifi/bk_wifi_cli.html
sdk_family: bk_idk
chip: BK7235
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="wi-fi-cli"></a>

# Wi-Fi Cli命令指南

为方便客户快速了解SDK以及开发调试，SDK集成了一些Wi-Fi基本操作指令

<a id="id1"></a>

## 代码路径

`components\bk_cli\cli_wifi.c & cli_netif.c`

<a id="cli"></a>

## cli命令简介

SDK支持的Wi-Fi相关的cli命令如下表：

| Command | Param | Description |
| --- | --- | --- |
| sta: sta \[ssid\] \[password\] | param1: ssid | 目标路由器 |
| param2: password | 目标路由器密码 |
| ap: ap ssid \[password\] \[channel\] | param1: ssid | 自定义热点名称 |
| param2: password | 自定义热点密码 |
| param2: channel | 自定义热点信道\[1-14\] |
| scan: scan \[ssid\] | 无 | 扫描附近所有热点 |
| ping: ping \[ip\] \[count\] | param1: ip | 目标主机IP地址 |
| param2: count | Ping包数量 |
| state: state \- show STA/AP state | 无 | 显示当前Station/SoftAP状态 |
| ip: ip \[sta\|ap\]\[{ip}{mask}{gate}{dns}\] | 无 | 显示当前Station网络连接参数 |
| stop: stop {sta\|ap} | sta/ap | 停止当前Station/SoftAP |
| iperf: iperf \[-s\|-c\|-stop\] | -s | DUT作为Server |
| -c -u | DUT作为Client, -u表示UDP |
| -stop | 停止 |

## 模块导航

- [简介](../../introduction.md)
- [快速入门](../../get-started.md)
- [H/W 参考手册](../../hw-reference.md)
- [API 参考手册](../../api-reference.md)
- [开发者指南](../../developer-guide.md)
- [软件架构与分层](../architecture.md)
- [构建与配置](../build_config.md)
- [系统安全](../security.md)
- [低功耗与电源管理](../power_save.md)
- [内存与性能](../memory_perf.md)
- [设备管理框架](../driver_model.md)
- [外设与驱动](../peripheral.md)
- [事件机制](../event.md)
- [出错与日志](../error_log.md)
- [系统调试](../debug_trace.md)
- [Wi-Fi](../wifi.md)
- [Armino Wi-Fi说明](bk_wifi.md)
- [Wi-Fi Quick Get-Started](bk_wifi_get_started.md)
- [Wi-Fi AP/STA/P2P模式示例说明](bk_wifi_mode.md)
- [Wi-Fi iPerf示例说明](bk_wifi_iperf.md)
- [Wi-Fi 扫描示例工程说明](bk_wifi_scan.md)
- [Wi-Fi 抓包使用说明](bk_wifi_capture.md)
- [Wi-Fi STA低功耗指南](bk_wifi_pm.md)
- [Bluetooth](../bluetooth.md)
- [HTTP](../http.md)
- [OS 抽象层](../os_abstraction.md)
- [OS 移植指南](../porting.md)
- [Bootloader和OTA](../bootloader.md)
- [特定芯片相关指南](../boards.md)
- [特定 CPU 相关指南](../cpu.md)
- [用例编写](../examples.md)
- [文档系统](../documentation.md)
- [分区规范](../partition_specification.md)
- [OS 相关参考](../../os.md)
- [样例演示](../../examples.md)
- [应用开发](../../application.md)
- [产品解决方案](../../projects.md)
- [开发与贡献代码流程](../../process.md)
- [云平台](../../clounds.md)
- [版本](../../release-notes.md)
