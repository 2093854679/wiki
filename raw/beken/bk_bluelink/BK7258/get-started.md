---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_bluelink/bk7258/zh_CN/v2.0.1/get-started/index.html
sdk_family: bk_bluelink
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 快速入门

<a id="armino-blue-link-sdk"></a>

## Armino Blue\_Link SDK代码下载

您可从 gitlab 上下载 Armino Blue\_Link SDK:

```
mkdir -p ~/armino
cd ~/armino
git clone https://gitlab.bekencorp.com/armino/bk_blue_link/bk_blue_link.git -b blue_link_release/v2.0.1
cd bk_blue_link
git submodule update --init --recursive
```

备注

从官网的gitlab下载的为最近的SDK代码，相关账号找项目上审核申请。

<a id="id2"></a>

## 环境部署

> 请参考 [IDK环境部署](https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v2.0.2/get-started/index.html#id4) 。

<a id="id3"></a>

## 编译代码

以 `projects/bluetooth/wearable` 工程为例，编译命令如下:

```
cd ~/armino/bk_blue_link
make bk7258 PROJECT=bluetooth/wearable
```

<a id="id4"></a>

## 新建工程

> 可参考工程 `projects/bluetooth/wearable` 新建工程。

<a id="id5"></a>

## 烧录代码

> Armino 支持在 Windows/Linux 平台进行固件烧录, 烧录方法参考烧录工具中指导文档。
> 以Windows 平台为例， Armino 目前支持 UART 烧录。
>
> 请参考 [IDK烧录流程](https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v2.0.2/get-started/index.html#id8) 。

## 模块导航

- [H/W 参考](hw-reference.md)
- [API 参考](api-reference.md)
- [参考工程](projects.md)
