# BK 安全框架

> **TLDR:** BK 芯片五层安全体系——Secure Boot(启动链校验)、Flash AES(固件加密)、eFuse/OTP(硬件密钥)、LCS(生命周期管理)、FIH(抗故障注入)；支持安全 OTA 升级和完整的证书管理流程。

> **Source:** [security/index.md](../../raw/bk_doc/bk_idk/BK7236/security/index.md)

## 五层安全体系

```
┌─────────────────────────────────┐
│ 5. FIH (故障注入加固)            │ ← 运行时抗攻击
├─────────────────────────────────┤
│ 4. LCS (生命周期状态)            │ ← 芯片状态机管理
├─────────────────────────────────┤
│ 3. eFuse / OTP                  │ ← 硬件唯一 ID + 密钥存储
├─────────────────────────────────┤
│ 2. Flash AES                    │ ← 静态数据加密
├─────────────────────────────────┤
│ 1. Secure Boot                  │ ← 启动链可信验证
└─────────────────────────────────┘
```

### 1. Secure Boot (安全启动)
- ROM → Bootloader → Application 逐级校验
- 支持 XIP (eXecute In Place) 和 Overwrite 两种模式
- 镜像签名 + Hash 校验防止篡改

### 2. Flash AES
- 固件以 AES 密文存储于 Flash
- 运行时硬件解密，不影响性能
- 密钥由 eFuse 提供，不可软件读取

### 3. eFuse / OTP
- **eFuse**: 一次性可编程存储（不可擦除）
  - UID (唯一设备标识)
  - Security Boot 密钥
  - Flash AES 密钥
- **OTP**: 类似 eFuse，容量更大
- 通过 `bkfil` 工具烧录

### 4. LCS (Life Cycle State)
芯片生命周期状态机：
```
Raw → Test → Provisioning → Secure → RMA (Return Merchandise Authorization)
```
- **Raw**: 出厂默认
- **Secure**: 量产发货状态，所有安全功能启用
- **RMA**: 返修模式，允许重新编程

### 5. FIH (Fault Injection Hardening)
- 抗电压毛刺、时钟毛刺、激光注入等物理攻击
- 关键逻辑冗余 + 随机化执行
- 安全 Bug Report 机制（非公开披露）

## 安全 OTA

- 固件包签名验证
- A/B 分区回滚保护
- 版本防降级

## 关键工具

- **bkfil** — OTP/eFuse 烧录工具
- **BK_SignTool** — 固件签名工具
- **安全调试** — 需认证后才能开启 JTAG/SWD

## Related

- [[../concepts/bk-armino-framework|BK ARMINO 开发框架]]
- [[../categories/bk-doc|BK Docs 分类页面]]
