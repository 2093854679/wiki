# SPI通信协议

> **Source:** [03-SPI.md](../../raw/Study_Note/02-嵌入式开发/外设通信/03-SPI.md)
> **TLDR:** SPI是四线制（SCLK/MISO/MOSI/CS）全双工同步串行总线，高速（可达数十MHz）、无应答、单主多从，通过时钟极性和相位（CPOL/CPHA）配置四种工作模式。

## Key Points

- **四线定义**：SCLK（时钟）、MOSI（Master Out Slave In）、MISO（Master In Slave Out）、CS/SS（片选，低有效）
- **CPOL/CPHA**：CPOL=0时钟空闲低，CPOL=1空闲高；CPHA=0第一边沿采样，CPHA=1第二边沿采样；主从必须一致
- **数据交换**：主从内部移位寄存器组成环形——主机发1字节的同时接收1字节（全双工）
- **多从机方案**：①每个从机独立CS引脚（星型，速度快但占引脚） ②菊花链（daisy chain，节省引脚但延迟大）
- **速度优势**：比I2C快得多（I2C通常≤400kHz，SPI可达50MHz+）；无地址和应答开销
- **缺点**：无标准协议层（需自定义命令格式）、无应答无流控错误检测、多从机需要多根CS线
- **应用场景**：Flash芯片（W25Qxx）、LCD/OLED显示、SD卡、ADC/DAC、传感器

## Related Concepts

- [[i2c-protocol]] — I2C对比
- [[uart-protocol]] — UART对比
- [[spi-task-dev]] — SPI主从通信开发
