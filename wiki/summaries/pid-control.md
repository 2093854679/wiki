# PID控制原理

> **Source:** [PID.md](../../raw/Study_Note/02-嵌入式开发/PID/PID.md)
> **TLDR:** PID是最经典的控制算法——比例(P)响应当前误差、积分(I)消除稳态误差、微分(D)预判趋势抑制超调；核心是三个参数的整定和离散化实现。

## Key Points

- **P（比例）**：输出与误差成正比；Kp越大响应越快但可能震荡；单独使用有稳态误差
- **I（积分）**：累积历史误差消除稳态误差；Ki太大会引起积分饱和和震荡；需积分限幅（anti-windup）
- **D（微分）**：预测误差变化趋势提供阻尼；对噪声敏感常需滤波；Kd太大会放大高频噪声
- **位置式 vs 增量式**：位置式PID输出绝对控制量；增量式输出变化量（Δu），天然无积分饱和
- **参数整定**：手动试凑法（先P后I最后D）、Ziegler-Nichols法（临界比例度）、Cohen-Coon法；工程上常只用PI
- **嵌入式实现**：定时中断中周期性调用PID计算；`u(k) = u(k-1) + Kp*(e(k)-e(k-1)) + Ki*e(k) + Kd*(e(k)-2*e(k-1)+e(k-2))`

## Related Concepts

- [[tim-timer-overview]] — 定时器提供PID计算节拍
- [[embedded-registration-patterns]] — 控制模块的注册模式
