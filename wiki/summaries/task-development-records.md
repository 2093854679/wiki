# 5个实习Task开发记录

> **Source:** 5 task/*.md files
> **TLDR:** BK7236平台5个实习任务的完整开发文档——SOFTAP配网、TCP UART AT指令、WiFi DTIM10 TCP保活、SPI主从通信、HTTP文件上传；每项包含需求分析、技术设计、代码实现和测试要点。

## Key Points

- **SOFTAP配网**：SoftAP模式启动→HTTP Server接收配网信息（SSID/Password通过POST）→切换STA模式连接→反馈结果；核心API：`bk_wifi_softap_start()`/`bk_wifi_sta_connect()`
- **TCP UART AT指令**：UART接收AT命令字符串→状态机解析（AT+TCPCONN/TCPSEND/TCPCLOSE）→调用lwIP Socket API→格式化AT响应→UART返回；AT解析用环形缓冲+超时分帧
- **WiFi DTIM10 TCP保活**：设置DTIM=10→每10个Beacon(≈1s)唤醒一次→TCP心跳60s发送→Server可主动唤醒；核心：`bk_wifi_sta_set_dtim()`配置省电参数
- **SPI主从通信**：BK_SPI_Init配置时钟极性和相位→`bk_spi_write_bytes()`/`bk_spi_read_bytes()`收发→逻辑分析仪验证波形和频率
- **HTTP文件上传**：Littlefs文件操作（mount/write/read）→lwIP httpd POST/CGI处理→multipart/form-data解析→文件存储到Flash

## Related Concepts

- [[huang-learning-log]] — 开发日志中的问题与解决
- [[freertos-deep-dive]] — RTOS支撑
- [[wifi-basics]] — WiFi功能基础
