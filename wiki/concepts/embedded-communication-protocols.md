# 嵌入式外设通信协议全景对比

> **TLDR:** I2C、SPI、UART三大基础串行总线各有适用场景：I2C适合多设备低速（2线、有地址、带应答）、SPI适合高速全双工（4线、无地址、主控全权）、UART适合点对点异步（2线、无时钟、最简洁）。加上TCP形成从板级到网络的完整通信栈。

## 协议对比表

| 特性 | I2C | SPI | UART | TCP |
|------|-----|-----|------|-----|
| 线数 | 2（SCL+SDA） | 4（SCLK+MOSI+MISO+CS） | 2（TX+RX） | 网络层协议 |
| 通信方式 | 同步、半双工 | 同步、全双工 | 异步、全双工 | 可靠字节流 |
| 速率 | 100kHz-3.4MHz | 可达50MHz+ | 9600-921600bps | 受限于物理层 |
| 地址机制 | 7/10位硬件地址 | CS片选（无地址） | 无地址 | IP+端口 |
| 应答/确认 | ACK/NACK每字节 | 无 | 无（应用层校验） | 序列号+ACK |
| 多设备 | 多主多从 | 单主多从（CS数量=从机数） | 点对点 | C/S模型 |
| 电气特性 | 开漏+上拉 | 推挽 | 推挽/RS232/RS485 | — |

## 选型指南

**选I2C的情况**：
- 板上有多个低速传感器/外设（温度、湿度、RTC、EEPROM）
- 引脚紧张（只需2根线，可接127个设备）
- 需要硬件应答保证数据可靠性
- 场景：传感器阵列、PMIC配置、小数据量寄存器读写

**选SPI的情况**：
- 高速数据传输需求（Flash、LCD、SD卡）
- 全双工通信需求
- 不在乎多用几根引脚
- 场景：SPI Flash（W25Qxx）、LCD/OLED屏幕、高速ADC/DAC

**选UART的情况**：
- 点对点通信
- 长距离（RS232/RS485）
- 与模块通信（WiFi/蓝牙/4G/GPS/串口屏）
- 调试日志输出
- 场景：AT指令模块、GPS NMEA、固件升级、printf调试

**选TCP的情况**：
- 需要可靠网络传输
- 跨设备/跨网络通信
- Wi-Fi/以太网承载
- 场景：WiFi数据上报、HTTP/MQTT上层、远程控制

## 层次关系

```
应用层：    HTTP / MQTT / AT Commands
传输层：    TCP / UDP
网络层：    IP (lwIP in embedded)
链路层：    Wi-Fi MAC (802.11) / Ethernet MAC
物理层：    I2C / SPI / UART (板级) + Wi-Fi PHY (无线)
```

板级总线（I2C/SPI/UART）负责MCU与外设/模块的物理连接，TCP/IP在其上构建网络通信能力。在嵌入式WiFi开发中，SPI连接WiFi模块然后跑lwIP TCP/IP栈是常见架构。

## Related

- [[i2c-protocol]] — I2C协议详解
- [[spi-protocol]] — SPI协议详解
- [[uart-protocol]] — UART协议详解
- [[tcp-protocol-basics]] — TCP协议基础
- [[wifi-basics]] — WiFi 802.11基础
