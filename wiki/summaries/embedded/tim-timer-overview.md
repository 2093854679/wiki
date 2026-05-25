# TIM定时器

> **Source:** [05-TIM定时器.md](../../../raw/Study_Note/02-嵌入式开发/外设通信/05-TIM定时器.md)
> **TLDR:** MCU定时器外设的全面介绍：基本定时、输入捕获（测频/测脉宽）、输出比较/PWM、编码器模式、定时器级联和中断/DMA配合。

## Key Points

- **定时器分类**：基本定时器（只有计数功能）、通用定时器（PWM/输入捕获/输出比较）、高级定时器（互补输出/死区/刹车）
- **时基单元**：PSC预分频器→CNT计数器→ARR自动重载寄存器；`f_CNT = f_CLK / (PSC+1)`，`T_overflow = (ARR+1) / f_CNT`
- **输入捕获**：捕获引脚跳变时刻的CNT值；两次捕获差值=脉宽/周期；配合DMA实现高速连续捕获
- **输出比较**：CNT与CCR匹配时翻转/置高/置低输出；可用于产生任意波形
- **PWM模式**：边沿对齐（CNT从0计到ARR→溢出）和中心对齐（CNT从0到ARR再回到0）；占空比=CCR/ARR
- **编码器模式**：连接正交编码器（A/B两相），硬件自动计数方向判断，无需软件中断
- **中断与DMA**：更新中断（溢出）、捕获/比较中断；DMA批量传输可减轻CPU负担

## Related Concepts

- [[pwm-overview]] — PWM应用
- [[embedded-registration-patterns]] — 定时器与模块注册配合
