# WiFi 802.11基础知识介绍

## 目录
1. [WiFi 802.11协议概述](#1-wifi-80211协议概述)
2. [WiFi连接过程](#2-wifi连接过程)
3. [WiFi安全机制](#3-wifi安全机制)
4. [WiFi帧间间距](#4-wifi帧间间距)
5. [QoS服务质量](#5-qos服务质量)
6. [TBTT机制](#6-tbtt机制)
7. [帧聚合技术](#7-帧聚合技术)
8. [RW架构学习](#8-rw架构学习)
9. [KE/IP代码学习](#9-keip代码学习)
10. [VIF和STA管理](#10-vif和sta管理)
11. [速率控制](#11-速率控制)
12. [WPA3安全](#12-wpa3安全)
13. [WLAN漫游](#13-wlan漫游)
14. [IPv6支持](#14-ipv6支持)
15. [WiFi抓包及分析](#15-wifi抓包及分析)
16. [SDK代码实现分析](#16-sdk代码实现分析)

---

## 1. WiFi 802.11协议概述

### 1.1 什么是网络协议（五层模型）

WiFi通信基于网络五层模型：

```
应用层    | http/https, mqtt, websocket, coap
传输层    | tcp, udp
网络层    | IP (ICMP等), ARP, RARP
数据链路层 | MAC层
物理层    | PHY层, 射频层
```

在ARMINO SDK中，网络接口的实现可以在 `@/components/bk_netif/bk_netif.c` 中找到：

```c
// 网络接口事件回调处理
bk_err_t netif_wifi_event_cb(void *arg, event_module_t event_module,
                int event_id, void *event_data)
{
    if (event_module != EVENT_MOD_WIFI) {
        return BK_OK;
    }

    switch (event_id) {
    case EVENT_WIFI_STA_CONNECTED:
        // WiFi连接成功后启动IP配置
        if (sta_static_ip_flag !=0) {
            sta_ip_mode_set(0);
            BK_LOG_ON_ERR(bk_netif_set_ip4_config(NETIF_IF_STA, &static_ip));
        }
        sta_ip_start();
        break;
    case EVENT_WIFI_STA_DISCONNECTED:
        // WiFi断开连接时停止IP服务
        sta_ip_down();
        sta_static_ip_flag = 0;
        sta_ip_mode_set(1);
        break;
    }
    return BK_OK;
}
```

### 1.2. 802.11协议知识介绍

#### 802.11帧结构
802.11帧的最大长度2346个字节，基本结构包含：
- **Frame Control**: 2字节的帧控制字段，包含协议版本、帧类型、子类型、DS位等
- **Duration/ID**: 2字节，用于设置NAV或关联标识符
- **Address 1-4**: 地址字段，包含源地址、目的地址、BSSID等（最多4个地址）
- **Sequence Control**: 2字节序列控制字段，用于重组帧片段和丢弃重复帧
- **Frame Body**: 可变长度的帧体数据
- **FCS**: 4字节帧校验序列

#### Frame Control字段详解
Frame Control字段包含以下重要信息：
- **Protocol**: 协议版本（当前为0）
- **Type**: 帧类型（00=管理帧，01=控制帧，10=数据帧）
- **Subtype**: 帧子类型，与Type字段结合确定具体帧类型
- **To DS/From DS**: 指示帧的目的地是否位于分布式系统
- **More Fragments**: 类似IP数据报的更多分片位
- **Retry**: 表示重传帧
- **Power Management**: 指出发送端完成当前帧交换后是否进入省电模式
- **More Data**: 设定为1表示至少有一个帧待传给休眠中的工作站
- **Protected Frame**: 设定为1表示帧受链路层安全协议保护
- **Order**: 设定为1表示帧与帧片段进行严格依次传送

在SDK中，帧处理的相关定义可以在 `@/components/bk_wifi/include/bk_private/bk_wifi_types.h` 中找到：

```c
typedef struct probe_rsp {
    #ifdef CONFIG_MINIMUM_SCAN_RESULTS
    UINT64 timestamp;
    #else
    UINT8 timestamp[8];
    #endif
    UINT16 beacon_int;      // 信标间隔
    UINT16 capab_info;      // 能力信息

    /* followed by some of SSID, Supported rates,
     * FH Params, DS Params, CF Params, IBSS Params */
    UINT8 variable[1];
} __attribute__ ((packed)) PROBE_RSP_T;
```

### 1.3 帧类型分类

#### 管理帧 (Type=00 Management frames)
- **0000 Association request** (关联请求)
- **0001 Association response** (关联响应)
- **0010 Reassociation request** (重新关联请求)
- **0011 Reassociation response** (重新关联响应)
- **0100 Probe request** (探测请求)
- **0101 Probe response** (探测响应)
- **1000 Beacon** (信标帧)
- **1001 ATIM** (宣布流量指示消息)
- **1010 Disassociation** (解除关联)
- **1011 Authentication** (身份验证)
- **1100 Deauthentication** (解除身份验证)

#### 控制帧 (Type=01 Control frames)
- **1010 PS-Poll** (省电轮询)
- **1011 RTS** (请求发送)
- **1100 CTS** (清除发送)
- **1101 ACK** (确认)

#### 数据帧 (Type=10 Data frames)
- **0000 Data** (数据)
- **0001 Data + CF-Ack** (数据+无竞争确认)
- **0100 Null function** (空功能)
- **1000 QoS Data** (QoS数据)

#### 控制帧详解

**RTS（请求发送）帧**
- 用于取得媒介控制权，传送"大型"帧
- 只用于单播帧，广播和组播帧直接传送
- Duration字段预订整个RTS-CTS-frame-ACK交换过程的媒介使用时间

**CTS（清除发送）帧**
- 回复RTS帧，也用于802.11g保护机制
- Duration字段从RTS的duration值减去传送CTS帧及短帧间间隔所需时间

**ACK（确认）帧**
- 提供MAC层可靠性的肯定确认
- Duration设定取决于是否为最后一个帧片段

**PS-Poll（省电轮询）帧**
- 移动工作站从省电模式苏醒后用于取得缓存帧
- 包含关联标识符（AID）以识别缓存帧的目标工作站

### 1.4 地址字段与DS位

地址字段的用法取决于To DS和From DS位的设置：

| To DS | From DS | Address 1 | Address 2 | Address 3 | Address 4 |
|-------|---------|-----------|-----------|-----------|-----------|
| 0     | 0       | DA        | SA        | BSSID     | N/A       |
| 0     | 1       | DA        | BSSID     | SA        | N/A       |
| 1     | 0       | BSSID     | SA        | DA        | N/A       |
| 1     | 1       | RA        | TA        | DA        | SA        |

- **DA**: 目的地地址（Destination Address）
- **SA**: 来源地址（Source Address）
- **RA**: 接收端地址（Receiver Address）
- **TA**: 发送端地址（Transmitter Address）
- **BSSID**: 基本服务集标识符

## 2. WiFi连接过程

WiFi连接包含三个主要阶段：**扫描、认证和关联**。

### 2.1 扫描阶段

#### 被动扫描
- 工作站在各信道间切换，静候Beacon帧
- 节省电池电力，不需要传送任何信号
- 收集传送Beacon帧的BSS相关数据

#### 主动扫描
- 工作站发送Probe Request帧请求网络响应
- 扫描过程：
  1. 跳至某信道，等候帧指示或Probe Delay定时器超时
  2. 使用DCF访问过程取得媒介使用权，发送Probe Request帧
  3. 等候MinChannelTime，如媒介不忙碌则跳至下个信道
  4. 如媒介忙碌，继续等候至MaxChannelTime，处理Probe Response帧

#### Probe Request帧结构
包含两个主要信息元素：
- **SSID**: 服务集标识符（0-32字节），可为特定网络SSID或广播SSID
- **Supported Rates**: 支持的数据速率，每字节7位表示速率，最高位表示是否强制

### 2.2 身份认证阶段

#### 开放系统认证（Open System）
- 最简单的认证方式，实际上是"不认证"
- AP接受任何发送认证请求的STA
- 两帧交换：Authentication Request → Authentication Response

#### 共享密钥认证（Shared Key）
- 需要使用WEP加密
- 四帧交换过程：
  1. STA发送Authentication Request
  2. AP发送Authentication Response（包含质询文本）
  3. STA发送加密的质询文本响应
  4. AP验证后发送最终Authentication Response

### 2.3 关联阶段

#### 关联过程
1. STA发送Association Request帧
2. AP处理关联请求，考虑帧缓存空间等因素
3. AP返回Association Response，包含状态码和AID（关联标识符）
4. AP开始为STA处理帧

#### 重新关联过程
- 用于在不同接入点间移动时维持连接
- 包含旧接入点地址信息
- 新旧接入点间会转移缓存帧

#### Association Request帧结构
包含以下字段：
- **Capability Information**: 通告网络具备的性能
- **Listen Interval**: 以Beacon interval为单位的休眠时间
- **SSID**: 服务集标识符
- **Supported Rates**: 支持的数据速率

## 3. WiFi安全机制

### 3.1 AKM（Authentication and Key Management）

AKM定义了认证和密钥管理的方法，包括：
- 身份验证机制
- 密钥派生和管理
- 加密算法选择

### 3.2 密钥类型

#### 成对密钥（Pairwise Key）
- 用于单播通信的加密
- 每个STA与AP之间有独立的成对密钥
- 包含PTK（Pairwise Transient Key）的组成部分

#### 组密钥（Group Key）
- 用于广播和组播通信
- 网络中所有设备共享同一组密钥
- 包含GTK（Group Transient Key）

### 3.3 四次握手过程

四次握手用于更新成对密钥：

1. **第一次握手**: AP发送ANonce给STA
2. **第二次握手**: STA发送SNonce和MIC给AP
3. **第三次握手**: AP发送GTK和MIC给STA
4. **第四次握手**: STA发送确认给AP

在SDK中，WPA相关的实现可以在以下文件中找到：

```c
// @/components/wpa_supplicant_2_9/src/common/wpa_common.h
// 定义了WPA/WPA2的基本常量和结构

// PTK（Pairwise Transient Key）派生
void wpa_pmk_to_ptk(const u8 *pmk, size_t pmk_len, const char *label,
                   const u8 *addr1, const u8 *addr2,
                   const u8 *nonce1, const u8 *nonce2,
                   struct wpa_ptk *ptk, int akmp, int cipher)
```

### 3.4 加密算法

#### WEP（Wired Equivalent Privacy）
- 使用RC4流加密算法
- 密钥长度40位或104位
- 存在安全漏洞，已不推荐使用

#### TKIP（Temporal Key Integrity Protocol）
- WPA使用的加密协议
- 基于RC4，但增加了密钥混合和MIC
- 解决了WEP的安全问题

#### CCMP（Counter Mode with CBC-MAC Protocol）
- WPA2使用的加密协议
- 基于AES算法
- 提供更强的安全性

## 4. WiFi帧间间距

### 4.1 SIFS（Short Interframe Space）
- 最短的帧间间隔
- 用于高优先级的帧交换
- 典型值：10μs（2.4GHz），16μs（5GHz）

### 4.2 PIFS（PCF Interframe Space）
- PCF帧间间隔
- PIFS = SIFS + Slot Time
- 用于无竞争周期的访问

### 4.3 DIFS（DCF Interframe Space）
- DCF帧间间隔
- DIFS = SIFS + 2 × Slot Time
- 用于基于竞争的媒介访问

### 4.4 EIFS（Extended Interframe Space）
- 扩展帧间间隔
- 当检测到错误帧时使用
- 提供额外的恢复时间

## 5. QoS服务质量

### 5.1 QoS的必要性
- 不同应用对网络性能要求不同
- 语音、视频需要低延迟和抖动
- 数据传输更关注吞吐量
- 802.11e引入QoS机制解决这些问题

### 5.2 QoS优势
- **优先级管理**: 为不同类型流量分配优先级
- **带宽保证**: 为重要应用保证最小带宽
- **延迟控制**: 减少实时应用的传输延迟
- **抖动减少**: 提供更稳定的传输性能

### 5.3 访问类别（Access Categories）
- **AC_VO（Voice）**: 语音，最高优先级
- **AC_VI（Video）**: 视频，高优先级
- **AC_BE（Best Effort）**: 尽力而为，普通优先级
- **AC_BK（Background）**: 背景，最低优先级

## 6. TBTT机制

### 6.1 TBTT概念
TBTT（Target Beacon Transmission Time）是目标信标传输时间，定义了AP发送Beacon帧的时间点。

### 6.2 TBTT中完成的任务
- **信标帧传输**: 在TBTT时刻发送Beacon帧
- **功率管理**: 处理休眠STA的缓存帧
- **TIM更新**: 更新流量指示映射
- **信道切换**: 执行信道切换操作
- **节能处理**: 管理DTIM周期内的组播帧

### 6.3 TBTT切换管理
- 支持多VIF环境下的TBTT协调
- 处理不同VIF间的信道冲突
- 优化功耗和性能平衡

## 7. 帧聚合技术

### 7.1 帧聚合概述
802.11n引入帧聚合技术以减少开销，提高MAC层吞吐量。主要包括：
- **A-MSDU**: MAC服务数据单元聚合
- **A-MPDU**: MAC协议数据单元聚合

### 7.2 A-MSDU聚合

#### A-MSDU结构
- 多个A-MSDU子帧组成
- 每个子帧包含：DA、SA、Length、MSDU数据、Padding
- 除最后一个子帧外，都填充为4字节整数倍

#### A-MSDU限制
- 聚合的帧必须有相同的SA/DA映射
- 只能有一种QoS属性
- 适合较小MSDU的聚合
- 传输可靠性较差（一个FCS）

### 7.3 A-MPDU聚合

#### A-MPDU结构
- 每个子帧都有完整的802.11 MAC帧头
- 包含MPDU分界符和MPDU实体
- 支持更大的聚合长度（最大64KB）

#### A-MPDU优势
- 每个MPDU有独立的序列号
- 支持选择性重传
- 配合Block Ack机制提高效率

### 7.4 Block Ack机制

#### Block Ack建立流程
1. 通过ADDBA Request/Response协商建立Block ACK协定
2. 发送方发送多个QoS数据帧
3. 接收方保留接收状态
4. 收到BlockAckReq后，回应BlockAck帧
5. 通过DELBA Request撤销协定

#### Block Ack类型
- **即时确认**: 由硬件完成，映射到确认位图
- **延时确认**: 由协议栈完成，可进行进一步数据检查

## 8. RW架构学习

### 8.1 硬件帧传输接收

#### TX路径（发送路径）
- UMAC处理上层协议数据
- LMAC处理MAC层协议
- 硬件完成物理层传输

#### RX路径（接收路径）
- 硬件接收物理层信号
- LMAC处理MAC层协议
- UMAC向上层传递数据

### 8.2 SoftAP和STA工作过程

#### SoftAP模式
- 设备作为接入点工作
- 管理连接的STA
- 处理认证、关联和数据转发

#### STA模式
- 设备作为工作站连接到AP
- 执行扫描、认证、关联流程
- 接收AP的管理和控制

### 8.3 扫描过程详解

#### 扫描流程
1. 接收SCANU_START_REQ消息
2. 进入SCANU_SCANNING状态
3. 在每个信道上执行扫描
4. 收集Beacon和Probe Response
5. 完成后返回扫描结果

### 8.4 Monitor模式
- 用于数据包捕获和分析
- 接收所有802.11帧
- 不参与网络通信

## 9. KE/IP代码学习

### 9.1 KE消息机制

#### KE_MSG_SAVED vs KE_MSG_CONSUMED
- **KE_MSG_SAVED**: 消息被保存，稍后处理
- **KE_MSG_CONSUMED**: 消息被消费，立即处理

#### 消息队列函数
- 消息分配、发送、接收机制
- 支持不同任务间的通信
- 提供可靠的消息传递

### 9.2 内核环境

#### 功能列表
- 消息管理
- 定时器服务
- 任务调度
- 事件处理

#### 消息对象
- 消息标识符
- 参数管理
- 状态跟踪

### 9.3 调度器
- 调度算法实现
- 保存服务机制
- 任务优先级管理

### 9.4 内核定时器
- 定时器函数接口
- ke_timer和mm_timer使用
- 超时处理机制

## 10. VIF和STA管理

### 10.1 VIF（Virtual Interface）管理

#### VIF数据结构
```c
struct vif_mgmt_env_tag {
    struct vif_info_tag vif_info[NX_VIRT_DEV_MAX];
    uint32_t used_vif_for_ch_ctxt[PHY_BAND_MAX];
    uint8_t vif_sta_cnt[NX_VIRT_DEV_MAX];
    uint8_t low_bcn_int_idx;
};
```

#### VIF操作
- VIF注册和注销
- 信道上下文管理
- 多VIF协调

### 10.2 STA管理

#### STA数据结构
```c
struct sta_info_tag {
    struct mac_addr mac_addr;
    uint8_t inst_nbr;
    uint8_t staid;
    uint32_t bcn_int;
    struct sta_mgmt_sec_info sta_sec_info;
    // ... 其他字段
};
```

#### STA操作
- STA添加和删除
- 密钥管理
- 状态跟踪

### 10.3 密钥管理

#### 添加密钥
```c
void sta_mgmt_add_key(struct mm_key_add_req const *param, uint8_t hw_key_idx)
{
    struct sta_info_tag *sta = &sta_info_tab[param->sta_idx];
    struct sta_mgmt_sec_info *sec = &sta->sta_sec_info;
    struct key_info_tag *key;

    // 根据加密类型配置密钥
    switch(key->cipher) {
        case MAC_RSNIE_CIPHER_WEP40:
        case MAC_RSNIE_CIPHER_WEP104:
            key->tx_pn = co_rand_word() & 0xFFFFFF;
            break;
        case MAC_RSNIE_CIPHER_TKIP:
            // TKIP密钥配置
            break;
        default:
            key->tx_pn = 0;
            break;
    }
    key->valid = true;
}
```

## 11. 速率控制

### 11.1 速率控制概述
速率控制算法设计目标是使代码和内存大小较小，基于从MAC执行的A-MPDU和单例MPDU传输中检索的统计信息。

### 11.2 数据结构

#### 缓冲区控制结构
```c
struct txl_buffer_control {
    struct tx_policy_tbl policy_tbl;
    uint32_t mac_control_info;
    uint32_t phy_control_info;
    uint32_t status;
};
```

#### 统计与控制结构
```c
struct sta_pol_tbl_cntl {
    struct txl_buffer_control *buf_ctrl[2];
    struct rc_sta_stats *sta_stats;
    uint16_t prot_cfg;
    uint16_t ppdu_tx_cfg;
    uint8_t upd_field;
    uint8_t buf_ctrl_idx;
};
```

### 11.3 速率控制步骤

#### 算法概述
- 使用100毫秒固定时间段的统计信息
- 计算吞吐量和成功概率
- 填充重试链表
- 十分之一的传输用于试探其他速率

#### 初始化过程
- 样本表初始化：最低速率到最高速率
- 重试链设置：前3步使用最高速率，第4步使用最低速率
- 统计信息重置

#### 帧传输准备
检查是否需要修改重试链：
- RC间隔到期（100ms）
- 试用期结束
- 达到最大SW重试次数

## 12. WPA3安全

### 12.1 WPA3认证
- **SAE（Simultaneous Authentication of Equals）**: 同等身份验证
- **Enhanced Open**: 增强开放网络
- **更强的密码保护**: 抵御离线字典攻击

### 12.2 WPA3加密
- 使用更强的加密算法
- 支持192位安全套件
- 改进的密钥派生

### 12.3 WPA3转换模式
- 支持WPA2/WPA3混合模式
- 向后兼容性
- 渐进式部署

### 12.4 设备配置协议（DPP）
- 简化设备配置过程
- 基于公钥加密
- 支持二维码配置

### 12.5 机会无线加密（OWE）
- 为开放网络提供加密
- 不需要预共享密钥
- 防止被动窃听

## 13. WLAN漫游

### 13.1 漫游简介
WLAN漫游是指移动设备在不同接入点间切换时保持连接的能力。

### 13.2 漫游触发条件
- 信号强度下降
- 连接质量恶化
- 负载均衡需求

### 13.3 漫游基本原理
1. **信号监测**: 持续监测当前和邻近AP信号
2. **切换决策**: 根据算法决定是否切换
3. **重新关联**: 与新AP建立连接
4. **状态同步**: 更新网络状态信息

### 13.4 802.11k/v/r协议

#### 802.11k（Radio Resource Measurement）
- 提供射频资源测量
- 邻居AP信息报告
- 信道负载统计

#### 802.11v（Wireless Network Management）
- 网络管理功能
- BSS过渡管理
- 睡眠模式管理

#### 802.11r（Fast BSS Transition）
- 快速BSS过渡
- 减少切换时间
- 保持QoS状态

## 14. IPv6支持

### 14.1 IPv6地址表示方法
- 128位地址长度
- 十六进制表示法
- 地址压缩规则

### 14.2 IPv6基本首部
- **Version**: 版本字段（6）
- **Traffic Class**: 流量类别
- **Flow Label**: 流标签
- **Payload Length**: 有效载荷长度
- **Next Header**: 下一个首部
- **Hop Limit**: 跳数限制
- **Source Address**: 源地址（128位）
- **Destination Address**: 目的地址（128位）

### 14.3 IPv6地址类型

#### 单播地址
- **全球单播地址**: 全球唯一标识
- **链路本地地址**: 仅在本地链路有效
- **唯一本地地址**: 本地网络内唯一

#### 组播地址
- 一对多通信
- 特定的组播地址范围
- 支持不同作用域

#### 任播地址
- 一对最近通信
- 与单播地址格式相同
- 路由到最近的接口

### 14.4 IPv6协议

#### 地址配置协议
- **SLAAC**: 无状态地址自动配置
- **DHCPv6**: 有状态地址配置
- **邻居发现协议**: ND协议

#### 路由协议
- **ICMPv6**: 错误报告和诊断
- **路由器通告**: RA消息
- **邻居请求/通告**: NS/NA消息

### 14.5 过渡技术
- **双栈技术**: 同时运行IPv4和IPv6
- **隧道技术**: 在IPv4网络上传输IPv6
- **转换技术**: IPv4/IPv6协议转换

## 15. WiFi抓包及分析

### 15.1 抓包工具
常用的WiFi抓包工具包括：
- **Wireshark**: 最流行的网络协议分析器
- **tcpdump**: 命令行抓包工具
- **OmniPeek**: 商业级无线分析工具

### 15.2 抓包分析要点

#### 连接过程分析
1. **Probe Request/Response**: 查看扫描过程
2. **Authentication**: 分析认证类型和结果
3. **Association Request/Response**: 检查关联参数
4. **4-Way Handshake**: 验证密钥交换过程
5. **DHCP过程**: 确认IP地址分配

#### 性能分析
- **重传率**: 检查网络质量
- **信号强度**: RSSI值分析
- **信道利用率**: 查看信道忙碌程度
- **吞吐量**: 实际数据传输速率

### 15.3 常见问题诊断

#### 连接失败
- 认证失败：检查密码和安全配置
- 关联失败：查看AP容量和兼容性
- DHCP失败：检查网络配置

#### 性能问题
- 高重传率：信号干扰或距离问题
- 低吞吐量：信道拥塞或设备能力限制
- 高延迟：网络负载或路由问题

在SDK中，监控和分析功能的实现可以参考：

```c
// @/components/bk_wifi/src/rwnx_rx.c
// WiFi接收处理逻辑

static u8 rwnx_rx_data_skb(struct rwnx_hw *rwnx_hw,
                          struct rwnx_vif *rwnx_vif,
                          struct sk_buff *skb,
                          struct hw_rxhdr *hw_rxhdr)
{
    // 处理接收到的数据帧
    // 包含信号强度、速率等信息的提取
}
```

## 16. SDK代码实现分析

### 16.1 ARMINO SDK架构

ARMINO SDK采用分层架构设计：

```
应用层 (Application)
    ↓
中间件层 (Middleware)
    ↓
组件层 (Components)
    ↓
驱动层 (Driver)
    ↓
硬件抽象层 (HAL)
```

### 16.2 WiFi相关组件

#### 主要组件目录结构
- `components/bk_wifi/`: WiFi驱动和协议栈
- `components/wpa_supplicant_2_9/`: WPA认证组件
- `components/lwip_2_1_2/`: TCP/IP协议栈
- `components/bk_netif/`: 网络接口管理

#### WiFi API接口
主要的WiFi API在 `@/components/bk_wifi/src/wifi_v2.c` 中实现：

```c
// WiFi初始化
bk_err_t bk_wifi_init(void)
{
    // 初始化WiFi硬件和软件组件
    // 注册事件回调
    // 启动相关任务
}

// WiFi扫描
bk_err_t bk_wifi_scan_start(wifi_scan_config_t *scan_config)
{
    // 配置扫描参数
    // 启动扫描过程
    // 返回扫描结果
}

// WiFi连接
bk_err_t bk_wifi_sta_connect(wifi_sta_config_t *sta_config)
{
    // 配置STA参数
    // 启动连接过程
    // 处理连接结果
}
```

### 16.3 事件处理机制

WiFi事件处理通过事件回调机制实现，主要事件包括：
- `EVENT_WIFI_STA_CONNECTED`: STA连接成功
- `EVENT_WIFI_STA_DISCONNECTED`: STA断开连接
- `EVENT_WIFI_SCAN_DONE`: 扫描完成
- `EVENT_WIFI_AP_CONNECTED`: AP模式下有STA连接

### 16.4 安全实现

#### WPA/WPA2实现
WPA相关的安全实现主要在 `@/components/wpa_supplicant_2_9/` 目录下：

```c
// @/components/wpa_supplicant_2_9/src/common/wpa.c
// 四次握手实现
int wpa_supplicant_send_2_of_4(struct wpa_sm *sm,
                              const unsigned char *dst,
                              const struct wpa_eapol_key *key,
                              int ver, const u8 *nonce,
                              const u8 *wpa_ie, size_t wpa_ie_len,
                              struct wpa_ptk *ptk)
{
    // 实现四次握手的第二步
    // 发送SNonce和MIC
}
```

### 16.5 DHCP服务实现

DHCP服务器实现在 `@/components/lwip_2_1_2/src/apps/dhcp-server.c`：

```c
// DHCP服务器主要处理函数
static void dhcp_server_recv(void *arg, struct udp_pcb *pcb,
                           struct pbuf *p, const ip_addr_t *addr, u16_t port)
{
    // 处理DHCP请求
    // 分配IP地址
    // 发送DHCP响应
}
```

### 16.6 CLI命令系统

WiFi相关的CLI命令实现提供了丰富的调试和配置接口：

```bash
# WiFi基本操作
wifi_scan                    # 扫描WiFi网络
wifi_connect <ssid> <password>  # 连接WiFi网络
wifi_disconnect             # 断开WiFi连接
wifi_status                 # 查看WiFi状态

# 高级功能
wifi_monitor_start          # 启动监控模式
wifi_ap_start              # 启动AP模式
wifi_powersave             # 配置省电模式
```

### 16.7 低功耗实现

#### DTIM机制
- **DTIM Count**: DTIM计数
- **DTIM Period**: DTIM周期
- **组播缓存**: 在DTIM信标后发送组播帧

在 `@/components/bk_wifi/src/lsig_monitor.c` 中可以找到相关实现：

```c
// DTIM相关的低功耗处理
static void lsig_dtim_handler(void)
{
    // 处理DTIM信标
    // 管理组播帧传输
    // 控制STA睡眠/唤醒
}
```

### 16.8 性能优化

#### 快速连接机制
- **PMK缓存**: 避免重复的密钥派生
- **快速重连**: 利用之前的认证信息
- **信道记忆**: 优先扫描之前使用的信道

#### 吞吐量优化
- **帧聚合**: A-MSDU和A-MPDU
- **Block Ack**: 批量确认机制
- **速率自适应**: 根据信道条件调整传输速率

---

## 802.11常见缩写

| 缩写 | 英文全称 | 中文含义 |
|------|----------|----------|
| AP | Access Point | 接入点 |
| STA | Station | 工作站 |
| BSS | Basic Service Set | 基本服务集 |
| ESS | Extended Service Set | 扩展服务集 |
| BSSID | Basic Service Set Identifier | 基本服务集标识符 |
| SSID | Service Set Identifier | 服务集标识符 |
| TBTT | Target Beacon Transmission Time | 目标信标传输时间 |
| DTIM | Delivery Traffic Indication Message | 传送流量指示消息 |
| TIM | Traffic Indication Map | 流量指示映射 |
| NAV | Network Allocation Vector | 网络分配矢量 |
| RTS | Request To Send | 请求发送 |
| CTS | Clear To Send | 清除发送 |
| ACK | Acknowledgment | 确认 |
| SIFS | Short Interframe Space | 短帧间间隔 |
| DIFS | DCF Interframe Space | DCF帧间间隔 |
| PIFS | PCF Interframe Space | PCF帧间间隔 |
| EIFS | Extended Interframe Space | 扩展帧间间隔 |
| DCF | Distributed Coordination Function | 分布式协调功能 |
| PCF | Point Coordination Function | 点协调功能 |
| QoS | Quality of Service | 服务质量 |
| WMM | Wi-Fi Multimedia | WiFi多媒体 |
| EDCA | Enhanced Distributed Channel Access | 增强分布式信道访问 |
| TXOP | Transmission Opportunity | 传输机会 |
| MSDU | MAC Service Data Unit | MAC服务数据单元 |
| MPDU | MAC Protocol Data Unit | MAC协议数据单元 |
| A-MSDU | Aggregated MSDU | 聚合MSDU |
| A-MPDU | Aggregated MPDU | 聚合MPDU |
| BA | Block Acknowledgment | 块确认 |
| PMF | Protected Management Frames | 受保护管理帧 |
| MFP | Management Frame Protection | 管理帧保护 |
| BIP | Broadcast/Multicast Integrity Protocol | 广播/组播完整性协议 |
| SAE | Simultaneous Authentication of Equals | 同等身份验证 |
| OWE | Opportunistic Wireless Encryption | 机会无线加密 |
| DPP | Device Provisioning Protocol | 设备配置协议 |
| PMK | Pairwise Master Key | 成对主密钥 |
| PTK | Pairwise Transient Key | 成对瞬时密钥 |
| GTK | Group Transient Key | 组瞬时密钥 |
| KCK | Key Confirmation Key | 密钥确认密钥 |
| KEK | Key Encryption Key | 密钥加密密钥 |
| TK | Temporal Key | 临时密钥 |
| MIC | Message Integrity Check | 消息完整性检查 |
| CCMP | Counter Mode with CBC-MAC Protocol | 计数器模式及密码块链消息认证码协议 |
| TKIP | Temporal Key Integrity Protocol | 临时密钥完整性协议 |
| RSSI | Received Signal Strength Indicator | 接收信号强度指示 |
| SNR | Signal-to-Noise Ratio | 信噪比 |
| RSNIE | Robust Security Network Information Element | 健壮安全网络信息元素 |
| VIF | Virtual Interface | 虚拟接口 |
| UMAC | Upper MAC | 上层MAC |
| LMAC | Lower MAC | 下层MAC |
| KE | Kernel Environment | 内核环境 |
| RC | Rate Control | 速率控制 |

---

## 总结

本文档详细介绍了WiFi 802.11协议的基础知识，涵盖了从基本的帧结构到高级的安全机制、性能优化等各个方面。通过结合ARMINO SDK的具体实现，展示了理论知识在实际产品中的应用。

主要内容包括：
1. **协议基础**: 帧结构、帧类型、地址机制
2. **连接过程**: 扫描、认证、关联的详细流程
3. **安全机制**: 从WEP到WPA3的演进
4. **性能优化**: 帧聚合、QoS、速率控制
5. **高级特性**: 漫游、IPv6、低功耗
6. **实现细节**: SDK架构和关键代码分析

这些知识对于WiFi产品的开发、调试和优化都具有重要的指导意义。

