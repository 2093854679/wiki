---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7236n/zh_CN/v2.2.1/security/bk_security_fih.html
sdk_family: bk_idk
chip: BK7236N
processor: ''
sdk_version: v2.2.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="fault-injection-attack"></a>

<a id="id1"></a>

# 防故障注入攻击

<a id="id2"></a>

## 概述

故障注入攻击为一种主动侧信道攻击方式。常见的故障注入手段包括电压或时钟毛刺，电磁辐射，
物理探测，使用激光束对设备进行故障注入等。通过故障注入，攻击者能够干扰内存中位翻转，
从而破坏程序执行，如跳过相关指令，更改判断结果等等。

BK7236N 对核心安全组件提供了软/硬两方面的防范。

<a id="id3"></a>

## 软件防故障注入攻击

BK7236N 软件防故障注入攻击主要是通过在 BL1/BL2/TFM-S 中关注分支语句是增加随机时延，
使用复杂的 bool 变量，使用随机的 memcpy/memcmp 等机制来实现。

<a id="id4"></a>

## 硬件防故障注入攻击

BK7236N 硬件防注入攻击，主要是在 BL1 关键判断语句处使用硬件比较的方式来实现。例如，
将安全启动公钥 HASH 值的前 16bits 写入硬件比较寄存器 DST，在 BL1 的启动过程将实际
计算出的公钥 HASH 前 16bits 写入硬件比较寄存器 SRC，在 BL1 跳转到 BL2 前，硬件会
比较 SRC/DST，如果不一致就会中止启动。这样，如果攻击者通过故障注入方式将 ”公钥 HASH
验证结果为 false” 改成了 “true”，则在跳转到 BL2 前，硬件依然能够捕捉到这个错误，从而
中止安全启动。

## 模块导航

- [简介](../introduction.md)
- [快速入门](../get-started.md)
- [H/W 参考手册](../hw-reference.md)
- [API 参考手册](../api-reference.md)
- [开发者指南](../developer-guide.md)
- [安全](../security.md)
- [安全术语](bk_security_glossary.md)
- [PSA-L3/SESIP-L3 认证](bk_security_cert.md)
- [安全概述](bk_security_overview.md)
- [安全引擎](bk_security_enginee.md)
- [安全启动](bk_security_boot.md)
- [安全调试](bk_security_debug.md)
- [安全标识](bk_security_uid.md)
- [OTP](bk_security_otp.md)
- [EFUSE](bk_security_efuse.md)
- [FLASH 加密](bk_flash_aes.md)
- [漏洞披露](bk_security_bug_report.md)
- [OS 相关参考](../os.md)
- [购买 BK7236N 开发板](../boards.md)
- [用例指南](../examples.md)
- [开发与贡献代码流程](../process.md)
