---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/peripheral_guide/uart.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="uart"></a>

# UART 驱动

<a id="id1"></a>

## 概述

UART（Universal Asynchronous Receiver/Transmitter）通用异步收发器是一种串行通信接口，支持全双工异步数据传输。BK7239N 支持多个 UART 通道，提供灵活的串行通信解决方案。

<a id="id2"></a>

## 功能描述

- **多通道支持**：支持多个 UART 通道同时工作
- **波特率配置**：支持多种波特率设置，适应不同通信需求
- **数据格式**：支持 5-8 位数据位、1-2 位停止位、奇偶校验
- **流控制**：支持硬件流控制（RTS/CTS）和软件流控制
- **中断支持**：支持接收/发送中断，提高系统响应效率
- **DMA 支持**：支持 DMA 传输，减少 CPU 负载
- **软件 FIFO**：内置软件 FIFO 缓冲，提高数据传输效率
- **低功耗**：支持低功耗模式，节省功耗

<a id="id3"></a>

## 开发指引

1. **初始化流程**
   \- 调用 bk\_uart\_driver\_init() 初始化 UART 驱动
   \- 配置 UART 参数（波特率、数据位、停止位、校验位等）
   \- 调用 bk\_uart\_init() 初始化具体 UART 通道
   \- 根据需要配置中断和 DMA
2. **基本使用**
   \- 使用 bk\_uart\_write\_bytes() 发送数据
   \- 使用 bk\_uart\_read\_bytes() 接收数据
   \- 使用 bk\_uart\_write\_string() 发送字符串
3. **中断处理**
   \- 注册接收中断回调函数
   \- 在中断中处理接收到的数据
   \- 根据需要启用/禁用中断
4. **DMA 使用**
   \- 配置 DMA 通道
   \- 使用 DMA 进行大数据量传输
   \- 处理 DMA 传输完成中断

<a id="id4"></a>

## 注意事项

- 确保在调用其他 UART API 前先调用 bk\_uart\_driver\_init()
- 波特率设置需要与通信对方保持一致
- 使用中断模式时注意中断优先级设置
- DMA 传输时注意内存对齐和缓存一致性
- 低功耗模式下 UART 可能被关闭，需要重新初始化

<a id="api"></a>

## API 说明

主要 API 函数：

- bk\_uart\_driver\_init() \- 初始化 UART 驱动
- bk\_uart\_driver\_deinit() \- 反初始化 UART 驱动
- bk\_uart\_init() \- 初始化 UART 通道
- bk\_uart\_deinit() \- 反初始化 UART 通道
- bk\_uart\_write\_bytes() \- 发送字节数据
- bk\_uart\_read\_bytes() \- 接收字节数据
- bk\_uart\_write\_string() \- 发送字符串
- bk\_uart\_set\_baud\_rate() \- 设置波特率
- bk\_uart\_set\_data\_bits() \- 设置数据位
- bk\_uart\_set\_stop\_bits() \- 设置停止位
- bk\_uart\_set\_parity() \- 设置校验位
- bk\_uart\_set\_flow\_ctrl() \- 设置流控制
- bk\_uart\_enable\_rx\_interrupt() \- 启用接收中断
- bk\_uart\_disable\_rx\_interrupt() \- 禁用接收中断
- bk\_uart\_register\_rx\_isr() \- 注册接收中断服务函数
- bk\_uart\_set\_rx\_threshold() \- 设置接收阈值
- bk\_uart\_set\_rx\_timeout() \- 设置接收超时
- bk\_uart\_get\_tx\_over\_status() \- 获取发送溢出状态
- bk\_uart\_clear\_tx\_over\_status() \- 清除发送溢出状态
- bk\_uart\_power\_save\_backup() \- 低功耗备份
- bk\_uart\_power\_save\_restore() \- 低功耗恢复

<a id="id5"></a>

## 示例代码

基本使用示例：

```
#include <driver/uart.h>

void uart_example(void)
{
    uart_config_t config = {
        .baud_rate = 115200,
        .data_bits = UART_DATA_8BITS,
        .stop_bits = UART_STOP_1BITS,
        .parity = UART_PARITY_NONE,
        .flow_ctrl = UART_HW_FLOWCTRL_NONE,
        .source_clk = UART_SCLK_APB
    };

    // 初始化 UART 驱动
    bk_uart_driver_init();

    // 初始化 UART0
    bk_uart_init(UART_ID_0, &config);

    // 发送数据
    const char *msg = "Hello UART!\n";
    bk_uart_write_string(UART_ID_0, msg);

    // 接收数据
    uint8_t buffer[64];
    int len = bk_uart_read_bytes(UART_ID_0, buffer, sizeof(buffer), 1000);
    if (len > 0) {
        // 处理接收到的数据
    }
}
```

中断接收示例：

```
static void uart_rx_callback(uart_id_t id, void *param)
{
    uint8_t ch;
    while (bk_uart_read_bytes(id, &ch, 1, 0) > 0) {
        // 处理接收到的字符
        printf("Received: %c\n", ch);
    }
}

void uart_interrupt_example(void)
{
    // 注册接收中断回调
    bk_uart_register_rx_isr(UART_ID_0, uart_rx_callback, NULL);

    // 启用接收中断
    bk_uart_enable_rx_interrupt(UART_ID_0);
}
```

<a id="id6"></a>

## 常见问题

- **波特率不生效**：确认 bk\_uart\_driver\_init() 与 bk\_uart\_init() 调用顺序，检查时钟源与分频是否支持该波特率
- **接收丢数据**：检查 RX 满阈值、接收超时设置，必要时开启硬件流控或 DMA/软件 FIFO
- **回调未触发**：确认已启用对应中断，并核对 ISR 注册是否成功、优先级设置是否合理

<a id="id7"></a>

## 实战示例

1. 中断接收（注册 RX ISR）

```
static void uart_rx_cb(uart_id_t id, void *param) {
    uint8_t ch;
    while (bk_uart_read_bytes(id, &ch, 1, 0) > 0) {
        // 处理接收到的数据
    }
}
bk_uart_register_rx_isr(UART_ID_1, (uart_isr_t)uart_rx_cb, NULL);
bk_uart_enable_rx_interrupt(UART_ID_1);
```

<a id="id8"></a>

## 常见错误码说明

- BK\_ERR\_UART\_NOT\_INIT：未调用 bk\_uart\_driver\_init()
- BK\_ERR\_UART\_INVALID\_ID：传入的 uart\_id\_t 非法或不支持
- BK\_ERR\_UART\_BAUD\_RATE\_NOT\_SUPPORT：当前时钟配置下不支持该波特率
- BK\_ERR\_UART\_ID\_NOT\_INIT：未对具体通道调用 bk\_uart\_init()
