---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7236n/zh_CN/v2.2.1/developer-guide/peripheral/bk_wdt.html
sdk_family: bk_idk
chip: BK7236N
processor: ''
sdk_version: v2.2.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="wdt"></a>

# WDT 使用指南

<a id="id1"></a>

## 概述

watchdog 实际上是一个硬件定时器，定时器超时会触发系统 watchdog 重启。

bk\_wdt\_start(timeout\_ms) 可以设置 watchdog 定时器时间，目前时间配置范围为(1\~0xFFFF)， bk\_wdt\_feed() 可重置 watchdog 定时器。

<a id="watchdog"></a>

## watchdog 使用方法

watchdog 有两种常见的使用方式：

> - 在周期性中断中喂狗，如在 OS tick 中断中喂狗，当因为软件问题，如关中断过长，tick 中断未能及时喂狗，导致 watchdog 超时，最终触发 watchdog 重启。通过这种方式，能及时发现软件中断异常问题。这类 watchdog 使用通常称为 interrupt watchdog。
> - 在周期性任务中喂狗，如在 idle task 中喂狗，通常 idle task 为整个系统中优先级最低的 task, 当软件出现问题，如某个任务出现死循环长期占用 CPU，使 idle task 无法调度，导致未能及时喂狗，最终触发 watchdog 重启。通过这种方式，能及时发现软件任务调度上的问题。这类 watchdog 使用通常称为 task watchdog。

<a id="armino-interrupt-watchdog"></a>

## ARMINO Interrupt Watchdog

在 ARMINO 中，默认情况下，Interrupt Watchdog 是使能的，可通过 menuconfig 中 INT\_WDT\_PERIOD\_MS 来设置超时时间，或者关闭 interrupt watchdog。通常，应用不应该关闭 interrupt watchdog。

备注

当应用需要完全自己实现 interrupt watchdog 时，请通过 menuconfig 中 INT\_WDT 来关闭系统默认的 interrupt watchdog。

<a id="armino-task-watchdog"></a>

## ARMINO Task Watchdog

ARMINO 中也实现了 Task Watchdog, 但并不是基于真正硬件 Watchdog，即不是基于 bk\_wdt\_start()/bk\_wdt\_feed() 实现， 具体实现方式如下：

全局变量 s\_last\_task\_wdg\_feed\_tick 表示上次喂狗时间，在 idle task 中更新 s\_last\_task\_wdg\_feed\_tick，在 tick 中断中判断距离上次喂狗时间是否超出 task watchdog 超时时间，如果超时，则打出 task watchdog 超时的警告信息，但不重启系统。

备注

通常应用应该使能 task watchdog，除非应用实现自己的 task watchdog，可通过 menuconfig 中 TASK\_WDT 来关闭系统默认的 task watchdog。
