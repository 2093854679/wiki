---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_arduino/bk7239n/zh_CN/chapters/hardware-timer.html
sdk_family: bk_arduino
chip: BK7239N
processor: ''
sdk_version: not-declared
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="hardwaretimer"></a>

# HardwareTimer

HardwareTimer类用于配置和控制硬件定时器，支持毫秒和微秒精度的中断回调。BK7239N内置6个32位通用定时器。

<a id="hardwaretimer-api"></a>

## HardwareTimer API 参考

<a id="id1"></a>

### HardwareTimer()

构造函数，用于创建HardwareTimer实例。

```
HardwareTimer(uint8_t timer_id = 4);
```

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| timer\_id | uint8\_t | 硬件定时器ID（0-5，默认为4） |

<a id="id2"></a>

### \~HardwareTimer()

析构函数，清理HardwareTimer实例。

```
~HardwareTimer();
```

<a id="begin"></a>

### begin

初始化定时器硬件。初始化成功后定时器将自动启动。

```
bool begin();
```

**返回：** 成功返回 `true`，否则返回 `false`。

<a id="attachinterrupt"></a>

### attachInterrupt

设置定时器中断回调函数。

```
void attachInterrupt(hardware_timer_callback_t callback);
```

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| callback | hardware\_timer\_callback\_t | 中断回调函数，签名为 `void callback(void)` |

<a id="start"></a>

### start

以毫秒为周期启动定时器。

```
bool start(uint32_t period_ms);
```

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| period\_ms | uint32\_t | 定时器周期（单位：毫秒） |

**返回：** 成功返回 `true`，否则返回 `false`。

<a id="startmicroseconds"></a>

### startMicroseconds

以微秒为周期启动定时器。

```
bool startMicroseconds(uint64_t period_us);
```

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| period\_us | uint64\_t | 定时器周期（单位：微秒） |

**返回：** 成功返回 `true`，否则返回 `false`。

<a id="stop"></a>

### stop

停止定时器计数。

```
void stop();
```

<a id="read"></a>

### read

获取当前定时器计数值。

```
uint32_t read() const;
```

**返回：** 当前计数值。

<a id="period"></a>

### period

获取配置的定时器周期（毫秒）。

```
uint32_t period() const;
```

**返回：** 毫秒为单位的定时器周期。

<a id="running"></a>

### running

检查定时器是否正在运行。

```
bool running() const;
```

**返回：** 如果定时器正在运行返回 `true`，否则返回 `false`。

<a id="id"></a>

### id

获取定时器ID。

```
uint8_t id() const;
```

**返回：** 定时器ID。

<a id="invoke"></a>

### invoke

手动触发定时器回调函数。

```
void invoke() const;
```

<a id="id3"></a>

## HardwareTimer 示例

<a id="id4"></a>

### 硬件定时器示例

此示例演示如何使用硬件定时器通过中断回调控制LED：

```
#include <Arduino.h>
static HardwareTimer g_timer(4);
static constexpr uint32_t kTimerPeriodMs = 250;

volatile uint32_t g_tick_count = 0;

void onHardwareTimer() {
    ++g_tick_count;
    digitalWrite(LED_BUILTIN, (g_tick_count & 1U) ? HIGH : LOW);
}

void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, LOW);

    Serial.begin(115200);
    delay(200);

    Serial.println();
    Serial.println("arduino-beken hardware timer");
    Serial.print("Starting timer ");
    Serial.print(g_timer.id());
    Serial.print(" with period ");
    Serial.print(kTimerPeriodMs);
    Serial.println(" ms.");

    if (!g_timer.begin()) {
        Serial.println("HardwareTimer.begin() failed");
        return;
    }

    g_timer.attachInterrupt(onHardwareTimer);
    if (!g_timer.start(kTimerPeriodMs)) {
        Serial.println("HardwareTimer.start() failed");
        return;
    }
}

void loop() {
    static unsigned long last_report = 0;
    if (millis() - last_report < 1000) {
        delay(10);
        return;
    }

    last_report = millis();

    Serial.print("ticks=");
    Serial.print(g_tick_count);
    Serial.print(" counter=");
    Serial.print(g_timer.read());
    Serial.print(" running=");
    Serial.println(g_timer.running() ? "yes" : "no");
}
```
