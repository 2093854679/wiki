---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7235/zh_CN/v1.5/developer-guide/power_save/bk_rtc_sleep.html
sdk_family: bk_idk
chip: BK7235
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="rtc"></a>

# 设置RTC作为唤醒源，系统进入深度睡眠和低压睡眠说明

<a id="id1"></a>

## 设置RTC作为唤醒源，系统进入深度睡眠调用函数和调用顺序说明

- 1. 配置RTC唤醒源的参数
  > alarm\_info\_t low\_valtage\_alarm \= {
  >
  > > “low\_vol”,
  > >
  > > 3000\*AON\_RTC\_MS\_TICK\_CNT,//设置为3000ms后唤醒，唤醒时间可以根据需求更改
  > >
  > > 1,
  > >
  > > cli\_pm\_rtc\_callback,
  > >
  > > NULL
  > >
  > > };
  >
  > bk\_alarm\_register(AON\_RTC\_ID\_1, \&low\_valtage\_alarm);
- 2. bk\_pm\_wakeup\_source\_set(PM\_WAKEUP\_SOURCE\_INT\_RTC, NULL);
  > 向系统中设置RTC方式作为唤醒源
- 3. bk\_pm\_sleep\_mode\_set(PM\_MODE\_DEEP\_SLEEP);
  > 设置睡眠模式，进入深度睡眠

备注:
:   - 1. 进入深度睡眠前，需要把多媒体（audio,video）关闭下电，下电后会自动把票投上。
    - 2. BT和WIFI的票，BT和WIFI模块内部进入睡眠后自己投上，SDK内部做好，应用程序不用关注

<a id="id2"></a>

## 设置RTC作为唤醒源，系统进入低压睡眠调用函数和调用顺序说明

- 1. 配置RTC唤醒源的参数;
  > alarm\_info\_t low\_valtage\_alarm \= {
  >
  > > “low\_vol”,
  > >
  > > 3000\*AON\_RTC\_MS\_TICK\_CNT,//设置为3000ms后唤醒，唤醒时间可以根据需求更改
  > >
  > > 1,
  > >
  > > cli\_pm\_rtc\_callback,
  > >
  > > NULL
  > >
  > > };
  >
  > bk\_alarm\_register(AON\_RTC\_ID\_1, \&low\_valtage\_alarm);
- 2. bk\_pm\_wakeup\_source\_set(PM\_WAKEUP\_SOURCE\_INT\_RTC, NULL);
  > 向系统中设置RTC方式作为唤醒源
- 3. bk\_pm\_sleep\_mode\_set(PM\_MODE\_LOW\_VOLTAGE);
  > 设置睡眠模式，进入低压睡眠
  > (备注：当前系统默认设置为低压睡眠，只需要满足投的票，就可以进入低压睡眠)
- 4. bk\_pm\_module\_vote\_sleep\_ctrl(PM\_POWER\_MODULE\_NAME\_APP,0x1,0x0);
  > 向系统中投应用程序的票

备注:

> - 1. BT和WIFI的票，BT和WIFI模块内部进入睡眠后自己投上，SDK内部做好，应用程序不用关注
> - 2. 当系统中BT或WIFI模块没有上电时，系统会自动给这两个模块投上sleep的票。
