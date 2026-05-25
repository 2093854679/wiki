# BK Matter 开发框架概述

> **TLDR:** BK Matter 是博通集成基于 CSA Matter 协议的应用层框架，运行于 BK7235/BK7236/BK7256/BK7258 之上，提供统一的 Matter 设备类型开发、配网、安全通信和多生态接入能力。

> **Source:** [matter-basic.md](../../../raw/beken/bk_matter/matter-basic.md)

## Matter 是什么

Matter 由 CSA（连接标准联盟）制定，是一个**统一的开源应用层连接标准**，运行于 IP (WiFi/Thread/Ethernet) 之上，旨在解决智能家居碎片化问题。核心原则：**简单、可靠、互操作**。

## 协议栈分层

```
Application        ← 业务逻辑（开关灯、锁门）
Data Model         ← 属性/命令/事件的抽象定义
Interaction Model  ← Read / Write / Invoke / Subscribe
Action Framing     ← 二进制序列化
Security           ← AES 加密 + MAC 验证
Message            ← 包头 + 路由信息
UDP/TCP            ← IP 传输
```

## 核心概念

| 概念 | 说明 |
|------|------|
| **Node** | 逻辑独立的设备实例，拥有唯一 Node ID |
| **Endpoint** | 设备内的功能模块（Endpoint 0 预留） |
| **Cluster** | 基本功能集 = Attributes + Commands + Events，分 Server/Client |
| **Fabric** | 设备群的虚拟网络，共享根证书，跨 WiFi/Thread/Ethernet |
| **Commissioner** | 配网者，将设备引入 Fabric |
| **Controller** | 控制器（如 HomePod、Home App） |
| **Bridge** | 桥接非 Matter 设备（ZigBee/蓝牙）到 Matter 生态 |
| **DCL** | CSA 分布式数据库，存认证信息、证书、固件 URL |

## 配网流程

1. Commissioner 扫描设备二维码/手动码
2. PASE 建立初始安全通道（passcode 认证）
3. 分配网络凭证 + 操作证书 (NOC)
4. CASE 建立操作安全通道
5. 设备加入 Fabric，获得 Node ID

## 交互模型

- **Read** — 读取属性/事件
- **Write** — 修改属性
- **Invoke** — 触发命令
- **Subscribe** — 订阅数据推送（替代轮询）

## BK Matter 支持

- **芯片**: BK7235 / BK7236 / BK7256 / BK7258
- **SDK**: `git clone git@gitlab.bekencorp.com:armino/bk_matter.git`
- **构建**: `make bk7236 PROJECT=matter`（需 gn + ninja）
- **工具链**: ZAP (ZCL 配置工具) · chip-tool · chip-cert · ota-provider-app

## Related

- [[../concepts/bk-armino-framework|BK ARMINO 开发框架]]
- [[../concepts/iot-communication-protocols|物联网通信协议全景]]
- [[../../categories/bk-doc/matter|BK Matter 芯片 Hub]]
