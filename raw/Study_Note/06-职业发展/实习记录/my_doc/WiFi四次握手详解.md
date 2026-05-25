# WiFi四次握手详解

## 📖 概述

WiFi四次握手（4-Way Handshake）是WPA/WPA2安全协议中最重要的密钥交换过程。它确保AP（接入点）和STA（工作站）之间建立安全的通信信道。

---

## 🔑 核心概念解释

### 什么是Nonce？
**Nonce** = **N**umber used **once**（一次性数字）
- 这是一个随机生成的数字，每次连接都不同
- 就像"验证码"一样，用来防止重放攻击
- 确保每次握手过程都是唯一的

#### ANonce（Authenticator Nonce）
- **A**uthenticator **Nonce** = 认证者随机数
- 由**AP（接入点）**生成的随机数
- 相当于AP说："这是我的随机挑战码"

#### SNonce（Supplicant Nonce）
- **S**upplicant **Nonce** = 请求者随机数
- 由**STA（工作站）**生成的随机数
- 相当于STA说："这是我的随机响应码"

### 什么是MIC？
**MIC** = **M**essage **I**ntegrity **C**heck（消息完整性检查）
- 类似于"数字签名"或"校验码"
- 确保消息在传输过程中没有被篡改
- 接收方可以验证消息的真实性和完整性

### 什么是GTK？
**GTK** = **G**roup **T**emporal **K**ey（组临时密钥）
- 用于加密**广播和组播**数据的密钥
- 网络中所有设备共享同一个GTK
- 定期更换以提高安全性

---

## 🔄 四次握手详细过程

### 握手前的准备工作
在四次握手之前，STA和AP已经完成了：
1. **扫描**: STA发现AP
2. **认证**: 身份验证（Open或Shared Key）
3. **关联**: 建立基本连接
4. **PMK生成**: 根据密码生成主密钥

```
密码 "12345678"
    ↓ (通过PBKDF2算法)
PMK (Pairwise Master Key) - 主密钥
```

---

### 第一次握手 📤
**方向**: AP → STA
**内容**: AP发送ANonce给STA

```
AP: "你好，我是路由器，这是我的随机挑战码：ANonce = 0x1a2b3c..."
    "请用这个码和你的随机码一起生成通信密钥"
```

**技术细节**:
- AP生成32字节的随机数ANonce
- 将ANonce封装在EAPOL-Key消息中发送给STA
- 此时还没有加密，因为通信密钥尚未建立

---

### 第二次握手 📤
**方向**: STA → AP
**内容**: STA发送SNonce和MIC给AP

```
STA: "收到你的挑战码，这是我的随机响应码：SNonce = 0x4d5e6f..."
     "我已经生成了通信密钥，这是我的签名证明：MIC = 0x789abc..."
```

**技术细节**:
1. **STA生成SNonce**: 32字节随机数
2. **计算PTK**: 使用PMK + ANonce + SNonce + AP MAC + STA MAC生成PTK
3. **生成MIC**: 使用PTK中的KCK对消息进行签名
4. **发送响应**: 将SNonce和MIC发送给AP

**PTK生成公式**:
```
PTK = PRF-512(PMK, "Pairwise key expansion",
              Min(AP_MAC, STA_MAC) || Max(AP_MAC, STA_MAC) ||
              Min(ANonce, SNonce) || Max(ANonce, SNonce))
```

**PTK组成部分**:
- **KCK** (Key Confirmation Key): 用于MIC计算
- **KEK** (Key Encryption Key): 用于加密其他密钥
- **TK** (Temporal Key): 用于数据加密

---

### 第三次握手 📤
**方向**: AP → STA
**内容**: AP发送GTK和MIC给STA

```
AP: "很好，我验证了你的签名，证明你知道正确的密码"
    "这是组播密钥：GTK = 0xabcdef...（已加密）"
    "这是我的签名证明：MIC = 0x123456..."
```

**技术细节**:
1. **验证STA的MIC**: AP使用计算出的PTK验证STA发送的MIC
2. **生成GTK**: AP生成用于组播通信的密钥
3. **加密GTK**: 使用PTK中的KEK加密GTK
4. **生成MIC**: 使用KCK对整个消息签名
5. **发送GTK**: 将加密的GTK和MIC发送给STA

---

### 第四次握手 📤
**方向**: STA → AP
**内容**: STA发送确认给AP

```
STA: "收到组播密钥，验证签名正确"
     "四次握手完成，开始安全通信！"
     "这是我的最终确认：MIC = 0xfedcba..."
```

**技术细节**:
1. **验证AP的MIC**: STA验证AP发送的MIC
2. **解密GTK**: 使用KEK解密获得GTK
3. **安装密钥**: 将PTK和GTK安装到硬件加密引擎
4. **发送确认**: 发送最终确认消息给AP

---

## 🔐 密钥层次结构

```
用户密码 "12345678"
    ↓ PBKDF2算法
PMK (Pairwise Master Key) - 主密钥
    ↓ PRF算法 + Nonces + MAC地址
PTK (Pairwise Transient Key) - 成对临时密钥
    ├── KCK (Key Confirmation Key) - 用于MIC计算
    ├── KEK (Key Encryption Key) - 用于加密其他密钥
    └── TK (Temporal Key) - 用于数据加密

GTK (Group Temporal Key) - 组临时密钥
    └── 用于广播/组播数据加密
```

---

## 🛡️ 安全机制说明

### 为什么需要四次握手？

#### 1. **双向认证**
- AP需要证明它知道正确的密码
- STA也需要证明它知道正确的密码
- 防止恶意AP或STA的攻击

#### 2. **密钥新鲜性**
- 每次连接都生成新的临时密钥
- 即使密码相同，通信密钥也不同
- 防止重放攻击和密钥重用

#### 3. **完整性保护**
- MIC确保消息没有被篡改
- 防止中间人攻击
- 保证密钥交换的可靠性

---

## 🔍 实际抓包分析

### Wireshark中的四次握手

#### Message 1 (AP → STA)
```
EAPOL Key (1 of 4)
├── Key Information: 0x008a
├── Key Length: 0
├── Replay Counter: 1
├── WPA Key Nonce: ANonce (32 bytes)
├── WPA Key IV: 00000000000000000000000000000000
├── WPA Key RSC: 0000000000000000
├── WPA Key ID: 0000000000000000
├── WPA Key MIC: 空 (16 bytes)
└── WPA Key Data Length: 0
```

#### Message 2 (STA → AP)
```
EAPOL Key (2 of 4)
├── Key Information: 0x010a
├── Key Length: 0
├── Replay Counter: 1
├── WPA Key Nonce: SNonce (32 bytes)
├── WPA Key IV: 00000000000000000000000000000000
├── WPA Key RSC: 0000000000000000
├── WPA Key ID: 0000000000000000
├── WPA Key MIC: 有效MIC (16 bytes) ✓
└── WPA Key Data: RSN IE信息
```

#### Message 3 (AP → STA)
```
EAPOL Key (3 of 4)
├── Key Information: 0x13ca
├── Key Length: 16
├── Replay Counter: 2
├── WPA Key Nonce: ANonce (32 bytes)
├── WPA Key IV: 随机IV
├── WPA Key RSC: 0000000000000000
├── WPA Key ID: 0000000000000000
├── WPA Key MIC: 有效MIC (16 bytes) ✓
└── WPA Key Data: 加密的GTK + RSN IE
```

#### Message 4 (STA → AP)
```
EAPOL Key (4 of 4)
├── Key Information: 0x030a
├── Key Length: 0
├── Replay Counter: 2
├── WPA Key Nonce: 全零
├── WPA Key IV: 00000000000000000000000000000000
├── WPA Key RSC: 0000000000000000
├── WPA Key ID: 0000000000000000
├── WPA Key MIC: 有效MIC (16 bytes) ✓
└── WPA Key Data Length: 0
```

---

## 💻 SDK代码实现

在ARMINO SDK中，四次握手的实现主要在WPA Supplicant组件中：

### 发送第二次握手
```c
// @/components/wpa_supplicant_2_9/src/common/wpa.c
int wpa_supplicant_send_2_of_4(struct wpa_sm *sm,
                              const unsigned char *dst,
                              const struct wpa_eapol_key *key,
                              int ver, const u8 *nonce,
                              const u8 *wpa_ie, size_t wpa_ie_len,
                              struct wpa_ptk *ptk)
{
    struct wpa_eapol_key *reply;
    u8 *rbuf, *key_mic;
    size_t rlen;

    // 1. 分配消息缓冲区
    rbuf = wpa_sm_alloc_eapol(sm, IEEE802_1X_TYPE_EAPOL_KEY,
                             NULL, sizeof(*reply) + wpa_ie_len,
                             &rlen, (void *) &reply);

    // 2. 设置消息参数
    reply->type = EAPOL_KEY_TYPE_WPA;
    WPA_PUT_BE16(reply->key_info, ver | WPA_KEY_INFO_KEY_TYPE |
                 WPA_KEY_INFO_MIC);

    // 3. 复制SNonce
    os_memcpy(reply->key_nonce, nonce, WPA_NONCE_LEN);

    // 4. 添加RSN IE
    if (wpa_ie_len) {
        os_memcpy((u8 *)(reply + 1), wpa_ie, wpa_ie_len);
        WPA_PUT_BE16(reply->key_data_length, wpa_ie_len);
    }

    // 5. 计算并设置MIC
    key_mic = reply->key_mic;
    wpa_eapol_key_mic(ptk->kck, ptk->kck_len, ver, (u8 *) reply,
                     rlen, key_mic);

    // 6. 发送消息
    return wpa_sm_ether_send(sm, dst, ETH_P_EAPOL, rbuf, rlen);
}
```

### PTK密钥派生
```c
// PTK生成函数
void wpa_pmk_to_ptk(const u8 *pmk, size_t pmk_len, const char *label,
                   const u8 *addr1, const u8 *addr2,
                   const u8 *nonce1, const u8 *nonce2,
                   struct wpa_ptk *ptk, int akmp, int cipher)
{
    u8 data[2 * ETH_ALEN + 2 * WPA_NONCE_LEN];

    // 1. 组织输入数据：地址和随机数
    // 按字典序排列确保AP和STA计算结果相同
    if (os_memcmp(addr1, addr2, ETH_ALEN) < 0) {
        os_memcpy(data, addr1, ETH_ALEN);
        os_memcpy(data + ETH_ALEN, addr2, ETH_ALEN);
    } else {
        os_memcpy(data, addr2, ETH_ALEN);
        os_memcpy(data + ETH_ALEN, addr1, ETH_ALEN);
    }

    if (os_memcmp(nonce1, nonce2, WPA_NONCE_LEN) < 0) {
        os_memcpy(data + 2 * ETH_ALEN, nonce1, WPA_NONCE_LEN);
        os_memcpy(data + 2 * ETH_ALEN + WPA_NONCE_LEN, nonce2, WPA_NONCE_LEN);
    } else {
        os_memcpy(data + 2 * ETH_ALEN, nonce2, WPA_NONCE_LEN);
        os_memcpy(data + 2 * ETH_ALEN + WPA_NONCE_LEN, nonce1, WPA_NONCE_LEN);
    }

    // 2. 使用PRF函数派生PTK
    sha1_prf(pmk, pmk_len, label, data, sizeof(data),
             (u8 *) ptk, ptk_len);
}
```

---

## 🔢 详细握手流程

### 第一次握手：AP的挑战 📤

```
AP → STA: "开始密钥交换！"
┌─────────────────────────────────┐
│ EAPOL-Key Message 1 of 4        │
├─────────────────────────────────┤
│ Key Info: 0x008a                │
│ ├─ Key Type: Pairwise (成对密钥) │
│ ├─ Install: 0 (暂不安装)        │
│ ├─ Key Ack: 1 (需要确认)        │
│ ├─ Key MIC: 0 (无MIC)           │
│ └─ Secure: 0 (未加密)           │
│                                 │
│ Replay Counter: 递增计数器       │
│ Key Nonce: ANonce (32字节随机数) │
│ Key IV: 全零                    │
│ Key RSC: 全零                   │
│ Key MIC: 全零 (无签名)          │
│ Key Data: 空                    │
└─────────────────────────────────┘
```

**AP的操作**:
1. 生成32字节的随机数ANonce
2. 构造EAPOL-Key消息
3. 发送给STA，等待响应

---

### 第二次握手：STA的响应 📤

```
STA → AP: "我也准备好了，这是我的证明！"
┌─────────────────────────────────┐
│ EAPOL-Key Message 2 of 4        │
├─────────────────────────────────┤
│ Key Info: 0x010a                │
│ ├─ Key Type: Pairwise           │
│ ├─ Key MIC: 1 (有MIC签名) ✓     │
│ └─ Secure: 0 (仍未加密)         │
│                                 │
│ Replay Counter: 与Message 1相同  │
│ Key Nonce: SNonce (32字节随机数) │
│ Key MIC: 有效签名 ✓              │
│ Key Data: RSN IE (STA的能力信息) │
└─────────────────────────────────┘
```

**STA的操作**:
1. 生成32字节的随机数SNonce
2. 使用PMK + ANonce + SNonce + 地址信息计算PTK
3. 从PTK中提取KCK用于MIC计算
4. 对整个消息计算MIC签名
5. 发送SNonce、RSN IE和MIC给AP

**关键计算**:
```c
// PTK = PRF-512(PMK, "Pairwise key expansion", 地址和随机数)
// MIC = HMAC-SHA1(KCK, EAPOL-Key消息内容)
```

---

### 第三次握手：AP的确认和GTK分发 📤

```
AP → STA: "验证通过！这是组播密钥，开始安全通信！"
┌─────────────────────────────────┐
│ EAPOL-Key Message 3 of 4        │
├─────────────────────────────────┤
│ Key Info: 0x13ca                │
│ ├─ Key Type: Pairwise           │
│ ├─ Install: 1 (安装密钥) ✓      │
│ ├─ Key Ack: 1 (需要确认)        │
│ ├─ Key MIC: 1 (有MIC签名) ✓     │
│ ├─ Secure: 1 (已加密) ✓         │
│ └─ Encrypted: 1 (Key Data加密)  │
│                                 │
│ Replay Counter: 递增             │
│ Key Nonce: ANonce (重复)        │
│ Key MIC: 有效签名 ✓              │
│ Key Data: 加密的GTK + RSN IE 🔒 │
└─────────────────────────────────┘
```

**AP的操作**:
1. 验证STA发送的MIC签名
2. 生成GTK（组临时密钥）
3. 使用KEK加密GTK
4. 计算新的MIC签名
5. 设置Install位，指示STA安装密钥
6. 发送加密的GTK给STA

**GTK加密过程**:
```c
// 使用KEK加密GTK
aes_wrap(ptk->kek, gtk_len/8, gtk, encrypted_gtk);
```

---

### 第四次握手：STA的最终确认 📤

```
STA → AP: "收到组播密钥，四次握手完成！"
┌─────────────────────────────────┐
│ EAPOL-Key Message 4 of 4        │
├─────────────────────────────────┤
│ Key Info: 0x030a                │
│ ├─ Key Type: Pairwise           │
│ ├─ Key MIC: 1 (有MIC签名) ✓     │
│ └─ Secure: 1 (已加密) ✓         │
│                                 │
│ Replay Counter: 与Message 3相同  │
│ Key Nonce: 全零                 │
│ Key MIC: 有效签名 ✓              │
│ Key Data: 空                    │
└─────────────────────────────────┘
```

**STA的操作**:
1. 验证AP发送的MIC签名
2. 使用KEK解密GTK
3. 将PTK和GTK安装到硬件
4. 发送最终确认给AP
5. 开始使用新密钥进行安全通信

---

## 🎭 通俗比喻理解

### 银行开户比喻

想象你要在银行开户，需要建立安全的通信：

#### 第一次握手 - 银行的挑战
```
银行: "你好，我是XX银行，这是我的挑战码：12345"
      "请用这个码和你的信息生成验证密码"
```

#### 第二次握手 - 你的响应
```
你: "收到挑战码，这是我的响应码：67890"
    "我已经生成了通信密码，这是我的签名：ABCDE"
```

#### 第三次握手 - 银行的确认
```
银行: "验证通过！这是我们的共享密码本：XYZ（已加密）"
      "这是我的签名证明：FGHIJ"
```

#### 第四次握手 - 最终确认
```
你: "收到密码本，验证无误，开始安全通信！"
    "最终确认签名：KLMNO"
```

---

## 🚨 常见问题和故障

### 握手失败的原因

#### 1. **密码错误**
- 现象：第二次握手MIC验证失败
- 原因：STA使用了错误的密码计算PTK
- 解决：检查WiFi密码是否正确

#### 2. **时间同步问题**
- 现象：Replay Counter不匹配
- 原因：设备时间不同步
- 解决：重新连接或重启设备

#### 3. **硬件加密问题**
- 现象：第四次握手后无法通信
- 原因：密钥安装到硬件失败
- 解决：检查硬件加密引擎状态

### 调试方法

#### 1. **抓包分析**
```bash
# 使用Wireshark过滤四次握手
eapol and (wlan.fc.type_subtype == 0x08 or wlan.fc.type_subtype == 0x00)
```

#### 2. **日志分析**
```c
// 在SDK中启用WPA调试日志
#define WPA_MSG_DEBUG 1
wpa_printf(MSG_DEBUG, "4-way handshake step %d", step);
```

#### 3. **状态检查**
```bash
# CLI命令检查WiFi状态
wifi_status
wifi_state
```

---

## 📚 深入学习资源

### 相关文档
- `wifi基础介绍.md` - 第3章 WiFi安全机制
- IEEE 802.11i标准文档
- RFC 3748 - EAP协议

### 实践建议
1. 使用Wireshark捕获真实的四次握手过程
2. 分析不同安全模式下的握手差异
3. 实验密码错误时的握手失败过程
4. 研究WPA3 SAE认证的改进

---

## 🎯 学习检查点

完成以下任务，确保你真正理解了四次握手：

- [ ] 能够解释每个术语的含义（ANonce、SNonce、MIC、GTK）
- [ ] 理解四次握手的完整流程
- [ ] 知道每次握手中传输的具体内容
- [ ] 能够分析Wireshark抓包结果
- [ ] 理解握手失败的常见原因
- [ ] 能够在SDK代码中找到相关实现

---

*通过理解这些概念，你将对WiFi安全机制有更深入的认识，这对于开发安全可靠的IoT产品非常重要。*
