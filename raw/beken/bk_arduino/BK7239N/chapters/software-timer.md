---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_arduino/bk7239n/zh_CN/chapters/software-timer.html
sdk_family: bk_arduino
chip: BK7239N
processor: ''
sdk_version: not-declared
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="ticker"></a>

# Ticker

软件定时器(Ticker)提供轻量级的软件定时功能，基于RTOS软件定时器实现，支持周期性和一次性回调。

<a id="ticker-api"></a>

## Ticker API 参考

<a id="attach"></a>

### attach

附加一个回调函数，以秒为单位定期调用。

```
void attach(float seconds, ticker_callback_t callback);
```

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| seconds | float | 周期时间（单位：秒，支持小数） |
| callback | ticker\_callback\_t | 回调函数，签名为 `void callback(void)` |

<a id="attach-ms"></a>

### attach\_ms

附加一个回调函数，以毫秒为单位定期调用。

```
void attach_ms(uint32_t milliseconds, ticker_callback_t callback);
```

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| milliseconds | uint32\_t | 周期时间（单位：毫秒） |
| callback | ticker\_callback\_t | 回调函数，签名为 `void callback(void)` |

<a id="once-ms"></a>

### once\_ms

附加一个回调函数，只调用一次（一次性定时器）。

```
void once_ms(uint32_t milliseconds, ticker_callback_t callback);
```

| 参数 | 类型 | 描述 |
| --- | --- | --- |
| milliseconds | uint32\_t | 延迟时间（单位：毫秒） |
| callback | ticker\_callback\_t | 回调函数，签名为 `void callback(void)` |

<a id="detach"></a>

### detach

分离定时器，停止定时器并清除回调函数。

```
void detach();
```

<a id="active"></a>

### active

检查定时器是否处于活动状态。

```
bool active() const;
```

**返回：** 如果定时器处于活动状态返回 `true`，否则返回 `false`。

<a id="id1"></a>

## Ticker 示例

<a id="id2"></a>

### Ticker 示例

此示例演示如何使用Ticker通过周期性回调控制LED：

```
#include <Ticker.h>

Ticker ledTicker;
volatile bool led_state = false;

void toggleLed() {
    led_state = !led_state;
    digitalWrite(LED_BUILTIN, led_state ? HIGH : LOW);
}

void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, LOW);

    Serial.begin(115200);
    Serial.println("arduino-beken ticker blink");

    ledTicker.attach(0.5f, toggleLed);
}

void loop() {
    static unsigned long last_report = 0;
    if (millis() - last_report >= 2000) {
        last_report = millis();
        Serial.print("Ticker active: ");
        Serial.println(ledTicker.active() ? "yes" : "no");
    }
}
```
