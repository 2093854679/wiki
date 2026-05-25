# BLE协议概述

> **Source:** [BLE.md](../../../raw/Study_Note/06-职业发展/实习记录/my_doc/八股文/协议/BLE/BLE.md)
> **TLDR:** BLE（蓝牙低功耗）协议栈分层架构——PHY/LL/HCI/GAP/L2CAP/SMP/ATT/GATT；核心概念包括GAP角色（Peripheral/Central）和GATT数据模型（Service/Characteristic/UUID）。

## Key Points

- **协议栈分层**：Controller（PHY+LL+HCI，硬件） + Host（GAP+L2CAP+SMP+ATT+GATT，软件）；HCI是Controller与Host间的标准接口
- **GAP（通用访问协议）**：定义设备角色——Broadcaster/Observer/Peripheral/Central；连接参数（Interval/Latency/Timeout）
- **GATT（通用属性协议）**：数据组织模型——Profile→Service→Characteristic→Value+Descriptor；UUID标识每个元素
- **ATT**：属性协议，GATT的传输层，定义Attribute PDU格式和数据读写操作
- **SMP**：安全管理协议——配对方法（Just Works/Passkey/OOB）、密钥分发、加密链路建立
- **连接参数**：Connection Interval（7.5ms-4s）、Slave Latency（跳过n个间隔）、Supervision Timeout（链路监控超时）
- **开发实战**：SDK提供GATT Server/Client API；ble_gatts（GATT服务端）、ble_gattc（GATT客户端）、SPP（串口透传）、Mesh
- **性能优化**：MTU协商（增大单次传输数据量）、PHY升级（1M→2M→Coded PHY→LE Audio）

## Related Concepts

- [[wifi-basics]] — WiFi与BLE对比
- [[i2c-protocol]] — 嵌入式总线协议对比
- [[embedded-interview-prep]] — 面试中的BLE问题
