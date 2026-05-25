---
type: concept
aliases:
  - SPI 主从通信任务
  - SPI 任务开发
---

# SPI 主从通信任务

> **TLDR:** SPI 主从通信任务关注 CPOL/CPHA、片选、速率、收发缓冲和逻辑分析仪验证，是外设通信开发的典型入口。

## 关键链路

- 硬件连接：SCLK、MOSI、MISO、CS 和共地。
- 参数配置：时钟极性、时钟相位、位宽、速率、主从模式。
- 数据收发：主机驱动时钟，从机按时序响应。
- 验证：用逻辑分析仪确认波形、频率、片选和数据顺序。

## 易错点

- CPOL/CPHA 两端配置不一致。
- CS 时序不满足从设备要求。
- 速率过高导致边沿采样错误。
- 字节序、位序或缓冲长度不一致。

## Related

- [[spi-protocol]]
- [[embedded-communication-protocols]]
- [[task-development-records]]
- [[internship-plan]]
