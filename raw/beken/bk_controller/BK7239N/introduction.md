---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/introduction/index.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 简介

<a id="controller"></a>

## **Controller产品介绍**

Controller产品需要配合主控平台一起工作，主控平台需要开发相应的软件以完成对Controller的控制（比如WLAN扫描/连接）。
Controller产品通常有两种实现方式，分别是标准方案和私有方案。低功耗产品通常使用私有方案，本文档主要介绍BK私有Controller方案(BK Controller)。

<a id="bk-controller"></a>

## **BK Controller方案简介**

BK7239N Wi-Fi Controller可应用在低功耗IPC/门铃/门锁等产品，主控和Controller之间通过SDIO接口通信。
与标准的Controller产品相比，这类产品更关注功耗，要求Controller能够独立完成与服务器之间的保活，保活期间主控可能处于深度休眠甚至下电状态。

![BK7239N Wi-Fi Controller示意图](../../_assets/d38c3d8ed6c73b33deff-bk_controller.png)

## 模块导航

- [快速入门](get-started.md)
- [硬件开发指南](hw-reference.md)
- [Controller软件开发指南](controller-guide.md)
- [主控平台软件开发指南](host-guide.md)
- [工程与示例](project-example.md)
- [开发工具介绍](dev-tool.md)
- [调测指导](debug-guide.md)
- [产测指导](production-test-guide.md)
- [常见问题解答](faq.md)
