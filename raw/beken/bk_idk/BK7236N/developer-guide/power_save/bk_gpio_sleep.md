---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7236n/zh_CN/v2.2.1/developer-guide/power_save/bk_gpio_sleep.html
sdk_family: bk_idk
chip: BK7236N
processor: ''
sdk_version: v2.2.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="gpio"></a>

# 设置GPIO作为唤醒源，系统进入深度睡眠和低压睡眠说明

<a id="id1"></a>

## 设置GPIO作为唤醒源，系统进入深度睡眠调用函数和调用顺序说明

- 1. bk\_gpio\_register\_wakeup\_source(GPIO\_18,GPIO\_INT\_TYPE\_FALLING\_EDGE);
  1. 设置唤醒的GPIO id : GPIO18
  2. 设置GPIO唤醒模式:

::
:   GPIO\_INT\_TYPE\_LOW\_LEVEL: 低电平唤醒;
    GPIO\_INT\_TYPE\_HIGH\_LEVEL: 高电平唤醒;
    GPIO\_INT\_TYPE\_RISING\_EDGE: 上升沿唤醒;
    GPIO\_INT\_TYPE\_FALLING\_EDGE: 下降沿唤醒;

- 2. bk\_pm\_wakeup\_source\_set(PM\_WAKEUP\_SOURCE\_INT\_GPIO, NULL);
  > 向系统中设置GPIO方式作为唤醒源；
- 3. bk\_pm\_sleep\_mode\_set(PM\_MODE\_DEEP\_SLEEP);
  > 设置睡眠模式，进入深度睡眠
  >
  > (系统从深度睡眠唤醒后，可以通过调用 \- bk\_gpio\_get\_wakeup\_gpio\_id() \- 函数接口获取当前时哪个GPIO ID唤醒系统)

<a id="id2"></a>

## 设置GPIO作为唤醒源，系统进入低压睡眠调用函数和调用顺序说明

- 1. bk\_gpio\_register\_wakeup\_source(GPIO\_18,GPIO\_INT\_TYPE\_FALLING\_EDGE);

  a.设置唤醒的GPIO id:GPIO18;

  b.设置GPIO唤醒模式:

  > GPIO\_INT\_TYPE\_LOW\_LEVEL: 低电平唤醒;
  > GPIO\_INT\_TYPE\_HIGH\_LEVEL: 高电平唤醒;
  > GPIO\_INT\_TYPE\_RISING\_EDGE: 上升沿唤醒;
  > GPIO\_INT\_TYPE\_FALLING\_EDGE: 下降沿唤醒;
  >
  > GPIO\_INT\_TYPE\_RISING\_EDGE: 上升延唤醒;
- 2. bk\_pm\_wakeup\_source\_set(PM\_WAKEUP\_SOURCE\_INT\_GPIO, NULL);
  > 向系统中设置GPIO方式作为唤醒源；
- 3. bk\_pm\_sleep\_mode\_set(PM\_MODE\_LOW\_VOLTAGE);
  > 设置睡眠模式，进入低压睡眠。(备注：当前系统默认设置为低压睡眠，只需要满足投的票，就可以进入低压睡眠)
- 4. bk\_pm\_module\_vote\_sleep\_ctrl(PM\_SLEEP\_MODULE\_NAME\_APP,0x1,0x0);
  > 向系统中投应用程序的票。

备注：

> - 1. BLE和WIFI的票，BLE和WIFI模块内部进入睡眠后自己投上，SDK内部做好，应用程序不用关注；
> - 2. 当系统中BLE或WIFI模块没有上电时，系统会自动给这两个模块投上sleep的票；
