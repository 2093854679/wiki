---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/peripheral_guide/spi.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="spi"></a>

# SPI 驱动

<a id="id1"></a>

## 概述

SPI（Serial Peripheral Interface）串行外设接口是一种同步串行通信协议，广泛用于微控制器与各种外设之间的高速数据传输。BK7239N 支持多个 SPI 通道，提供灵活的串行通信解决方案。

<a id="id2"></a>

## 功能描述

- **多通道支持**：支持多个 SPI 通道同时工作
- **多种模式**：支持 SPI 模式 0-3，适应不同外设需求
- **位宽配置**：支持 8-32 位数据位宽
- **线制支持**：支持标准 4 线制和 3 线制 SPI
- **时钟配置**：支持多种时钟频率设置
- **位序配置**：支持 MSB 和 LSB 位序
- **中断支持**：支持接收/发送完成中断
- **DMA 支持**：支持 DMA 传输，减少 CPU 负载
- **同步/异步**：支持同步和异步数据传输
- **全双工传输**：支持全双工数据传输

<a id="id3"></a>

## 开发指引

1. **初始化流程**
   \- 调用 bk\_spi\_driver\_init() 初始化 SPI 驱动
   \- 配置 SPI 参数（模式、位宽、线制、时钟频率等）
   \- 调用 bk\_spi\_init() 初始化具体 SPI 通道
   \- 根据需要配置中断和 DMA
2. **基本使用**
   \- 使用 bk\_spi\_transmit() 进行同步收发
   \- 使用 bk\_spi\_write() 和 bk\_spi\_read() 进行异步传输
   \- 使用 bk\_spi\_duplex\_transfer() 进行全双工传输
3. **DMA 使用**
   \- 配置 DMA 通道
   \- 使用 DMA 进行大数据量传输
   \- 处理 DMA 传输完成中断
4. **中断处理**
   \- 注册接收/发送完成中断回调
   \- 在中断中处理传输状态
   \- 根据需要启用/禁用中断

<a id="id4"></a>

## 注意事项

- 确保在调用其他 SPI API 前先调用 bk\_spi\_driver\_init()
- SPI 模式设置需要与从设备保持一致
- 时钟频率设置需要考虑信号完整性
- 使用中断模式时注意中断优先级设置
- DMA 传输时注意内存对齐和缓存一致性
- 注意 SPI 信号线的电气特性和时序要求

<a id="api"></a>

## API 说明

主要 API 函数：

- bk\_spi\_driver\_init() \- 初始化 SPI 驱动
- bk\_spi\_driver\_deinit() \- 反初始化 SPI 驱动
- bk\_spi\_init() \- 初始化 SPI 通道
- bk\_spi\_deinit() \- 反初始化 SPI 通道
- bk\_spi\_set\_mode() \- 设置 SPI 模式
- bk\_spi\_set\_bit\_width() \- 设置位宽
- bk\_spi\_set\_wire\_mode() \- 设置线制
- bk\_spi\_set\_baud\_rate() \- 设置波特率
- bk\_spi\_set\_bit\_order() \- 设置位序
- bk\_spi\_enable\_rx\_interrupt() \- 启用接收中断
- bk\_spi\_disable\_rx\_interrupt() \- 禁用接收中断
- bk\_spi\_enable\_tx\_interrupt() \- 启用发送中断
- bk\_spi\_disable\_tx\_interrupt() \- 禁用发送中断
- bk\_spi\_register\_rx\_isr() \- 注册接收中断服务函数
- bk\_spi\_register\_tx\_isr() \- 注册发送中断服务函数
- bk\_spi\_transmit() \- 同步传输
- bk\_spi\_write() \- 异步写入
- bk\_spi\_read() \- 异步读取
- bk\_spi\_duplex\_transfer() \- 全双工传输
- bk\_spi\_dma\_read() \- DMA 读取
- bk\_spi\_dma\_write() \- DMA 写入
- bk\_spi\_dma\_transmit() \- DMA 传输

<a id="id5"></a>

## 示例代码

基本使用示例：

```
#include <driver/spi.h>

void spi_example(void)
{
    spi_config_t config = {
        .mode = SPI_MODE_0,
        .bit_width = SPI_BIT_WIDTH_8,
        .wire_mode = SPI_4WIRE_MODE,
        .baud_rate = 1000000,
        .bit_order = SPI_MSB_FIRST
    };

    // 初始化 SPI 驱动
    bk_spi_driver_init();

    // 初始化 SPI0
    bk_spi_init(SPI_ID_0, &config);

    // 同步传输
    uint8_t tx_data[] = {0x9F, 0x00};
    uint8_t rx_data[2];
    bk_spi_transmit(SPI_ID_0, tx_data, sizeof(tx_data), rx_data, sizeof(rx_data));

    printf("SPI Response: 0x%02X 0x%02X\n", rx_data[0], rx_data[1]);
}
```

异步传输示例：

```
static void spi_rx_callback(spi_id_t id, void *param)
{
    printf("SPI RX Complete\n");
}

static void spi_tx_callback(spi_id_t id, void *param)
{
    printf("SPI TX Complete\n");
}

void spi_async_example(void)
{
    // 注册中断回调
    bk_spi_register_rx_isr(SPI_ID_0, spi_rx_callback, NULL);
    bk_spi_register_tx_isr(SPI_ID_0, spi_tx_callback, NULL);

    // 启用中断
    bk_spi_enable_rx_interrupt(SPI_ID_0);
    bk_spi_enable_tx_interrupt(SPI_ID_0);

    // 异步写入
    uint8_t tx_data[] = {0x9F, 0x00};
    bk_spi_write(SPI_ID_0, tx_data, sizeof(tx_data));

    // 异步读取
    uint8_t rx_data[2];
    bk_spi_read(SPI_ID_0, rx_data, sizeof(rx_data));
}
```

DMA 传输示例：

```
void spi_dma_example(void)
{
    uint8_t tx_buffer[1024];
    uint8_t rx_buffer[1024];

    // 准备发送数据
    for (int i = 0; i < 1024; i++) {
        tx_buffer[i] = i & 0xFF;
    }

    // DMA 传输
    bk_spi_dma_transmit(SPI_ID_0, tx_buffer, rx_buffer, 1024);

    // 处理接收到的数据
    printf("DMA Transfer Complete\n");
}
```

全双工传输示例：

```
void spi_duplex_example(void)
{
    uint8_t tx_data[] = {0x9F, 0x00, 0x00, 0x00};
    uint8_t rx_data[4];

    // 全双工传输
    bk_spi_duplex_transfer(SPI_ID_0, tx_data, rx_data, 4);

    printf("Duplex Transfer: ");
    for (int i = 0; i < 4; i++) {
        printf("0x%02X ", rx_data[i]);
    }
    printf("\n");
}
```

<a id="id6"></a>

## 常见问题

- **收发错位**：校验 CPOL/CPHA 是否与外设一致
- **读不到数据**：确认片选时序、线制配置与外设规格匹配，必要时降低波特率测试
- **DMA 传输失败**：检查内存对齐、缓存一致性、DMA 通道配置
- **中断未触发**：确认中断注册和启用，检查中断优先级设置

<a id="id7"></a>

## 实战示例

1. 同步收发一体

```
spi_config_t cfg = { /* 填充模式/线制/位序/波特率 */ };
bk_spi_init(SPI_ID_0, &cfg);
uint8_t tx[2] = {0x9F, 0x00}, rx[2] = {0};
bk_spi_transmit(SPI_ID_0, tx, sizeof(tx), rx, sizeof(rx)); // 读取器件ID
```

<a id="id8"></a>

## 常见错误码说明

- BK\_ERR\_SPI\_NOT\_INIT：未调用 bk\_spi\_driver\_init()
- BK\_ERR\_SPI\_INVALID\_ID：SPI 通道 ID 非法或不支持
- BK\_ERR\_SPI\_ID\_NOT\_INIT：未对通道调用 bk\_spi\_init()
