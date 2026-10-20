---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_matter/matter/zh_CN/v2.0.1/matter-tools/chip-tool/index.html
sdk_family: bk_matter
chip: BK7235,BK7236,BK7256,BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="chip-tool"></a>

# 测试工具 chip-tool

chip-tool 是一个linux工具，可用于配对测试matter设备，详细使用方式可以参考 [这里](https://project-chip.github.io/connectedhomeip-doc/guides/chip_tool_guide.html#commissioning-into-a-wi-fi-network-over-bluetooth-le) 。

<a id="id2"></a>

## 配对命令

```
./chip-tool pairing ble-wifi <node_id> <ssid> <password> <pin_code> <discriminator>
```

在这个命令中：

- \<node\_id\> 用户自定义的被配对设备的ID
- \<ssid\> 和 \<password\> 给被配对设备设置的wifi和密码
- \<pin\_cod\> 和 \<discriminator\> 是针对被配对设备的密钥

<a id="onoff"></a>

## 控制 onoff

```
./chip-tool onoff toggle <node_id> <endpoint_id>
```

在这个命令中：

- \<node\_id\> 是被控制设备的ID
- \<endpoint\_id\> 是实现了onoff cluster 的endpoint 的 ID

## 模块导航

- [快速入门](../get-started.md)
- [Matter 简介](../matter-basic.md)
- [Beken 的Matter 应用开发](../matter-examples.md)
- [从零开发Matter 新的设备类型产品](../matter-develop.md)
- [Matter 产品认证及量产流程](../matter-production.md)
- [Matter 工具](../matter-tools.md)
- [配置工具 ZAP](zap.md)
- [证书工具 chip-cert](chip-cert.md)
- [factory-data打包工具](factory-data.md)
- [Matter ota 测试](ota-provider-app.md)
- [Matter 生态配网测试](work-with-apple.md)
