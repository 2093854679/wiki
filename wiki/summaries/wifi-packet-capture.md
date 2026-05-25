# Wi-Fi抓包方法总结

> **Source:** [Wi-Fi抓包方法总结.md](../../raw/Study_Note/06-职业发展/实习记录/资料/wifi 抓包/Wi-Fi抓包方法总结.md)
> **TLDR:** Wi-Fi抓包两种方案——空中抓包用Omnipeek+专用无线网卡捕获802.11帧，有线端抓包用交换机端口镜像+Wireshark捕获WLAN口数据；含信道配置、解密密钥设置和分析技巧。

## Key Points

- **空中抓包（Omnipeek）**：需要支持Monitor模式的无线网卡（如MTK/EDIMAX EW-7822UAC）；配置抓包信道与目标AP一致；输入WPA密钥实时解密或抓包后解密
- **有线抓包（Wireshark）**：通过交换机端口镜像将WLAN口流量复制到抓包口；适用于分析AP上行数据
- **信道配置**：2.4G（1-14信道）和5G信道不同，抓包前确认AP工作信道
- **解密条件**：必须捕获到完整的4次EAPOL握手帧才能解密加密数据帧；抓包前输入密码可实时解密，抓包后补充密码也可解密
- **Wireshark过滤**：MAC地址过滤（`wlan.addr == xx:xx:xx:xx:xx:xx`）、握手帧过滤（`eapol`）、正则过滤定位特定数据
- **中文SSID解密**：中文SSID需特殊处理（编码问题可能导致解密失败）
- **分析技巧**：按帧类型（Management/Control/Data）分类查看；关注信号强度（RSSI）判断距离；时序分析定位响应延迟

## Related Concepts

- [[wifi-four-way-handshake]] — EAPOL四次握手
- [[wifi-basics]] — 802.11帧结构理解
