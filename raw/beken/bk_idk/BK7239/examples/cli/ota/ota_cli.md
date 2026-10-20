---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7239/zh_CN/v2.2.1/examples/cli/ota/ota_cli.html
sdk_family: bk_idk
chip: BK7239
processor: ''
sdk_version: v2.2.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="ota-cli"></a>

<a id="id1"></a>

# **OTA cli命令**

重要

*用于ota升级测试使用*

- [http\_ota](#ota-otacli) :OTA升级命令

<a id="http-ota-ota"></a>

<a id="ota-otacli"></a>

## [http\_ota](#ota-cli) **:执行OTA升级命令**

**命令**

```
http_ota url
```

**参数**

```
url:想要升级的rbl文件位置（通常位于HTTP服务器上）
```

**使用场景**

```
1）通过编译生成想要升级版本的rbl文件

2）rbl文件所在路径---build/app/bk7239n/encrypt/app_pack.rbl

3）在windows电脑上使用Everything创建HTTP服务器,拷贝url

4）使用命令进行升级：

        http_ota http://192.168.21.101/D%3A/E/build/app_pack.rbl
```

**响应**

```
CMDRSP:OK

CMDRSP:ERROR
```

备注

*本命令在CONFIG\_OTA\_HTTP开启且CONFIG\_SECURITY\_OTA不开启下生效!*

## 模块导航

- [简介](../../../introduction.md)
- [快速入门](../../../get-started.md)
- [H/W 参考手册](../../../hw-reference.md)
- [API 参考手册](../../../api-reference.md)
- [开发者指南](../../../developer-guide.md)
- [安全](../../../security.md)
- [OS 相关参考](../../../os.md)
- [购买 BK7239 开发板](../../../boards.md)
- [样例 CLI 演示](../../../examples.md)
- [命令](../../cli.md)
- [蓝牙](../bluetooth.md)
- [触摸](../touch.md)
- [wifi](../wifi/wifi_cli.md)
- [phy](../phy/phy_cli.md)
- [power manager](../pm/pm_cli.md)
- [platform](../platform/plt_cli.md)
- [gpio](../gpio/gpio_cli.md)
- [sd_card](../sd_card/sd_cli.md)
- [外设](../../peripheral.md)
- [平台](../../platform.md)
- [VND_CAL](../../vnd_cal/vnd_cal.md)
- [saradc](../../saradc/saradc.md)
- [开发与贡献代码流程](../../../process.md)
