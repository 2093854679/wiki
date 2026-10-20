---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_arduino/bk7239n/zh_CN/chapters/peripherals/uart.html
sdk_family: bk_arduino
chip: BK7239N
processor: ''
sdk_version: not-declared
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="uart"></a>

# UART

UART（通用异步收发器）用于串行通信。
BK7239N芯片包含四个UART接口，支持全双工、异步串行通信，波特率最高可达10Mbps。
其中，2个UART支持硬件流控制，1个支持Flash下载功能。

<a id="uart-api"></a>

## UART API 参考

<a id="begin"></a>

### begin()

使用指定的波特率初始化串行端口。

```
void Serial.begin(unsigned long baud);
void Serial.begin(unsigned long baud, uint16_t config);
```

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| `baud` | `unsigned long` | 波特率（例如：9600, 115200） |
| `config` | `uint16_t` | 使用预定义常量的配置（SERIAL\_8N1, SERIAL\_7E1等） |

配置常量：

- `SERIAL_8N1`: 8个数据位，无奇偶校验，1个停止位
- `SERIAL_8N2`: 8个数据位，无奇偶校验，2个停止位
- `SERIAL_8E1`: 8个数据位，偶校验，1个停止位
- `SERIAL_8E2`: 8个数据位，偶校验，2个停止位
- `SERIAL_8O1`: 8个数据位，奇校验，1个停止位
- `SERIAL_8O2`: 8个数据位，奇校验，2个停止位
- 以及其他使用5、6或7个数据位的配置

<a id="end"></a>

### end()

禁用串行端口。

```
void Serial.end();
```

<a id="write"></a>

### write()

向串行端口写入原始数据。

```
size_t Serial.write(uint8_t data);
size_t Serial.write(const uint8_t *buf, size_t size);
```

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| `data` | `uint8_t` | 要写入的单个字节 |
| `buf` | `const uint8_t*` | 要写入的缓冲区 |
| `size` | `size_t` | 要写入的字节数 |

**返回：** 写入的字节数。

<a id="print"></a>

### print()

向串行端口打印数据，不包含换行符。

```
size_t Serial.print(any data);
size_t Serial.print(any data, int base);
```

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| `data` | 多种类型 | 要打印的数据（字符串、数字等） |
| `base` | `int` | 整数的进制（DEC, HEX, OCT, BIN） |

**返回：** 打印的字节数。

<a id="println"></a>

### println()

向串行端口打印数据并添加换行符。

```
size_t Serial.println(any data);
size_t Serial.println(any data, int base);
```

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| `data` | 多种类型 | 要打印的数据（字符串、数字等） |
| `base` | `int` | 整数的进制（DEC, HEX, OCT, BIN） |

**返回：** 打印的字节数。

<a id="available"></a>

### available()

获取串行端口可读取的字节数。

```
int Serial.available();
```

**返回：** 可读取的字节数。

<a id="read"></a>

### read()

从串行端口读取下一个字节。

```
int Serial.read();
```

**返回：** 串行缓冲区中的下一个字节，如果无数据则返回-1。

<a id="flush"></a>

### flush()

等待传出串行数据传输完成。

```
void Serial.flush();
```

<a id="availableforwrite"></a>

### availableForWrite()

获取可用于写入串行端口的字节数。

```
int Serial.availableForWrite();
```

**返回：** 可用于写入的字节数（如果已初始化则始终为1，否则为0）。

<a id="id1"></a>

## UART 示例

<a id="id2"></a>

### 串行回显示例

此示例演示通过串行接口回显接收到的字符：

```
static const unsigned long kBaudRate = 115200;

void setup() {
    Serial.begin(kBaudRate);
    Serial.println();
    Serial.println("arduino-beken serial echo");
    Serial.println("Type any character to echo it back.");
}

void loop() {
    if (Serial.available() > 0) {
        int value = Serial.read();
        Serial.print("RX: 0x");
        if (value < 16) {
            Serial.print("0");
        }
        Serial.print(value, HEX);
        Serial.print(" '");
        if (value >= 32 && value <= 126) {
            Serial.write((uint8_t)value);
        } else {
            Serial.print(".");
        }
        Serial.println("'");
    }
}
```
