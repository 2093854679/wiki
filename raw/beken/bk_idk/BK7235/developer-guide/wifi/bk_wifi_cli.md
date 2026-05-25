# Wi-Fi Cli命令指南[](#wi-fi-cli "永久链接至标题")


为方便客户快速了解SDK以及开发调试，SDK集成了一些Wi-Fi基本操作指令


## 代码路径[](#id1 "永久链接至标题")

`components\bk_cli\cli_wifi.c & cli_netif.c`


## cli命令简介[](#cli "永久链接至标题")

SDK支持的Wi-Fi相关的cli命令如下表：

| Command | Param | Description |
| --- | --- | --- |
| sta: sta [ssid] [password] | param1: ssid | 目标路由器 |
| param2: password | 目标路由器密码 |
| ap: ap ssid [password] [channel] | param1: ssid | 自定义热点名称 |
| param2: password | 自定义热点密码 |
| param2: channel | 自定义热点信道[1-14] |
| scan: scan [ssid] | 无 | 扫描附近所有热点 |
| ping: ping [ip] [count] | param1: ip | 目标主机IP地址 |
| param2: count | Ping包数量 |
| state: state - show STA/AP state | 无 | 显示当前Station/SoftAP状态 |
| ip: ip [sta|ap][{ip}{mask}{gate}{dns}] | 无 | 显示当前Station网络连接参数 |
| stop: stop {sta|ap} | sta/ap | 停止当前Station/SoftAP |
| iperf: iperf [-s|-c|-stop] | -s | DUT作为Server |
| -c -u | DUT作为Client, -u表示UDP |
| -stop | 停止 |

