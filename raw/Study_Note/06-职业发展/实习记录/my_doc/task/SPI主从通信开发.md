# SPI主从通信开发

## 任务目标
- 测试主机、从机例程，验证不同时钟频率的数据交互和波形确认。

## 参考例程
- projects/examples/peripherals/spi（如有）

## 开发计划
- [ ] 方案设计与流程图
- [ ] SPI主机配置与测试
- [ ] SPI从机配置与测试
- [ ] 不同频率下数据交互与波形分析

## 问题记录
-

## 代码区
```c
// 代码片段可在此补充
```

---

## SPI主从通信实现细节

### 1. SPI主机配置与测试

```c
#include "driver/spi.h"

spi_config_t spi_cfg = {
    .mode = SPI_MODE_MASTER,
    .clk = 1000000, // 1MHz
    .bit_order = SPI_MSB_FIRST,
    // 其他参数...
};
bk_spi_init(SPI_ID_0, &spi_cfg);

// 发送数据
uint8_t tx_buf[] = {0x01, 0x02, 0x03};
bk_spi_write_bytes(SPI_ID_0, tx_buf, sizeof(tx_buf));
```

---

### 2. SPI从机配置与测试

```c
spi_config_t spi_cfg = {
    .mode = SPI_MODE_SLAVE,
    .clk = 1000000, // 1MHz
    .bit_order = SPI_MSB_FIRST,
    // 其他参数...
};
bk_spi_init(SPI_ID_1, &spi_cfg);

// 接收数据
uint8_t rx_buf[16] = {0};
bk_spi_read_bytes(SPI_ID_1, rx_buf, sizeof(rx_buf));
```

---

### 3. 不同频率下数据交互与波形分析
- 修改`.clk`参数测试不同频率（如1MHz、5MHz、10MHz等）。
- 用示波器/逻辑分析仪观察SCK、MOSI、MISO、CS波形，确认时序和数据正确。

---

### 4. 关键点说明
- **主从同步**：建议主机先拉低CS，再发送数据，确保从机同步。
- **数据完整性**：收发数据建议加校验。
- **硬件连线**：注意主从SCK、MOSI、MISO、CS正确连接。

---

### 5. 参考资料
- BK7236 SDK SPI驱动文档与例程
- [SPI协议基础](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface)
