# BK Bootloader & OTA 升级

> **TLDR:** BK7236/7236N/7239 支持 A/B 分区无位置依赖 OTA 升级方案——双固件分区轮流升级、Hash 完整性校验、回滚保护、安全 OTA 签名验证；同时支持传统单分区 Bootloader 方案。

> **Source:** [bootloader_ota/index.md](../../../raw/beken/bk_idk/BK7236/developer-guide/bootloader_ota/index.md)

## 两种方案对比

| | 传统 Bootloader | A/B 无位置依赖 OTA |
|---|---|---|
| 分区数 | 1 App | 2 App (A + B) |
| 升级方式 | 覆盖当前固件 | 写到备用分区 |
| 回滚 | 不支持 | 自动回滚 |
| 适用 | BK7235 | BK7236/7236N/7239 |
| Flash 占用 | 低 | 高 (双倍) |

## A/B OTA 核心流程

```
1. 下载新固件 → 写入 B 分区 (当前运行 A)
2. Hash 校验 B 分区完整性
3. 设置启动标志指向 B
4. 重启 → Bootloader 加载 B 分区
5. 如果 B 启动失败 → 自动回退到 A
```

## Bootloader 关键组件

### L-Bootloader (Light Bootloader)
- 精简启动管理，负责分区选择
- 支持安全启动链验证
- 通过 `bk_bootloader_imag_update` API 管理镜像更新

### 镜像生成
- 需生成含签名的固件包
- 使用 BK_SignTool 签名
- 支持 XIP 和 Overwrite 两种安全模式

## 安全 OTA 注意事项
- 固件包必须带有有效签名
- 版本号防降级检查
- OTA 分区也支持 AES 加密存储

## Related

- [[../concepts/bk-armino-framework|BK ARMINO 开发框架]]
- [[bk-security-framework|BK 安全框架]]
- [[../../categories/bk-doc|BK Docs 分类页面]]
