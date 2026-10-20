---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_bluelink/bk7258/zh_CN/v2.0.1/projects/wearable/index.html
sdk_family: bk_bluelink
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="wearable"></a>

# wearable 工程

<a id="id1"></a>

## 1\. 简介

> 本工程是wearable工程，集成了A2DP\_SINK、HFP、GATT、配网等蓝牙相关profile的应用。

- [A2DP\_SINK](wearable/a2dp_sink.md)
- [DOORBELL](wearable/doorbell.md)
- [GATT](wearable/gatt.md)
- [HFP](wearable/hfp.md)
- [HOGPD](wearable/hhogpd.md)
- [SPP\_VDN](wearable/spp_vnd.md)
- [STORAGE](wearable/storage.md)
- [BT\_MANAGER](wearable/manager.md)

<a id="id2"></a>

## 2\. 项目配置

> wearable 工程设置了以下项目宏选项，可以在工程的config文件中配置是否开启相关功能。

```
CONFIG_A2DP_SINK_DEMO 配置是否开启A2DP_SINK
CONFIG_HFP_HF_DEMO 配置是否开启HFP
CONFIG_INTEGRATION_DOORBELL 配置是否开启DOORBELL
```

<a id="id3"></a>

## 3\. 代码编译

> 编译命令: `make bk7258 PROJECT=bluetooth/wearable` 。
>
> 编译完成后输出的bin文件为 `./build/wearable/bk7258/all-app.bin` 。

<a id="bin"></a>

## 4\. bin文件烧录

> 请参考 [IDK烧录流程](https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v2.0.2/get-started/index.html#id8) 。

## 模块导航

- [快速入门](../get-started.md)
- [H/W 参考](../hw-reference.md)
- [API 参考](../api-reference.md)
- [参考工程](../projects.md)
- [A2DP_SINK](wearable/a2dp_sink.md)
- [DOORBELL](wearable/doorbell.md)
- [GATT](wearable/gatt.md)
- [HFP](wearable/hfp.md)
- [HOGPD](wearable/hhogpd.md)
- [SPP_VDN](wearable/spp_vnd.md)
- [STORAGE](wearable/storage.md)
- [BT_MANAGER](wearable/manager.md)
