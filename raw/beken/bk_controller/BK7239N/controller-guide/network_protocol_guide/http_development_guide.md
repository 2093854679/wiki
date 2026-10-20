---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/network_protocol_guide/http_development_guide.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk-controller-http"></a>

# BK Controller HTTP 开发指南

<a id="id1"></a>

## 前言

<a id="id2"></a>

### 概述

> 本文档主要介绍BEKEN Controller HTTP Client功能开发实现示例。

<a id="id3"></a>

### 产品版本

> 与本文档相对应的产品版本如下：
>
> | 产品名称 | 产品版本 |
> | --- | --- |
> | BK7239N | V1.0 |

<a id="id4"></a>

### 读者对象

> 本文档主要适用于以下对象：
>
> - 技术支持工程师
> - 软件开发工程师

<a id="id5"></a>

### 符号约定

> 在本文中可能出现下列标志，它们所代表的含义如下：
>
> | 符号 | 说明 |
> | --- | --- |
> | ![高等级风险](../../../../_assets/484f5b7e6ab95d4d1e8b-warning_high.png) | 表示如不避免则将会导致死亡或严重伤害的具有高等级风险的危害。 |
> | ![中等级风险](../../../../_assets/1a44a557aa66eeb27571-warning_medium.png) | 表示如不避免则可能导致死亡或严重伤害的具有中等级风险的危害。 |
> | ![低等级风险](../../../../_assets/73c6d395db7cc5df903d-warning_low.png) | 表示如不避免则可能导致轻微或中度伤害的具有低等级风险的危害。 |
> | ![注意](../../../../_assets/cc7a942057f838d114a7-caution.png) | 用于传递设备或环境安全警示信息。如不避免则可能会导致设备损坏、数据丢失、设备性能降低或其它不可预知的结果。”须知”不涉及人身伤害。 |
> | ![说明](../../../../_assets/1cf101865ae7e8bec4b2-note.png) | 对正文中重点信息的补充说明。”说明”不是安全警示信息，不涉及人身、设备及环境伤害信息。 |

<a id="id6"></a>

### 修改记录

> | 文档版本 | 发布日期 | 修改说明 |
> | --- | --- | --- |
> | 01 | 2025-10-17 | 第一次正式版本发布。 |

<a id="id7"></a>

## 1 开发指南

<a id="id8"></a>

### 1.1 概述

> lwIP HTTP Client在BEKEN Controller中被命名为 **webclient**，组件位于components/webclient目录下，代码由功能宏 `CONFIG_WEBCLIENT` 控制，默认关闭。

<a id="id9"></a>

### 1.2 示例代码

> ```
> #include <components/webclient.h>
> int bk_webclient_get(bk_webclient_input_t *input);  //get请求
> int bk_webclient_post(bk_webclient_input_t *input); //post请求
> int demo_webclient_get(char *url)  //get请求示例
> {
>   int err;
>   if(!url)
>   {
>     err = BK_FAIL;
>     CLI_LOGD( "url is NULL\r\n");
>     return err;
>   }
>   bk_webclient_input_t config = {
>       .url = url,
>       .header_size = 1024*2,
>       .rx_buffer_size = 1024*4
>   };
>   err = bk_webclient_get(&config);
>   if(err == BK_OK)
>     CLI_LOGD("bk_webclient_get ok\r\n");
>   else
>     CLI_LOGD("bk_webclient_get fail, err:%x\r\n", err);
>   return err;
> }
> int demo_webclient_post(char *url, char *post_data) //post请求示例
> {
>   int err;
>   if(!url)
>   {
>     err = BK_FAIL;
>     CLI_LOGD( "url is NULL\r\n");
>     return err;
>   }
>   if (post_data==NULL)
>   {
>     err = BK_FAIL;
>     CLI_LOGD( "post_data is NULL\r\n");
>     return err;
>   }
>   bk_webclient_input_t config = {
>       .url = url,
>       .header_size = 1024*2,
>       .rx_buffer_size = 1024*4,
>       .post_data = post_data
>   };
>   err = bk_webclient_post(&config);
>   if(err == BK_OK)
>     CLI_LOGD("bk_webclient_post ok\r\n");
>   else
>     CLI_LOGD("bk_webclient_post fail, err:%x\r\n", err);
>   return err;
> }
> void cli_webclient_cmd(char *pcWriteBuffer, int xWriteBufferLen, int argc, char **argv) //webclient命令实现
> {
>   int ret = 0;
>   char *msg = NULL;
>   if (argc == 3) {
>     if (strncmp(argv[1], "get", 3) == 0) {
>       CLI_LOGD("starting http(s) get url:%s\n", argv[2]);
>       demo_webclient_get(argv[2]);
>     } else {
>       CLI_LOGE("usage: webclient [get/post].\n");
>       goto error;
>     }
>   }
>   else if ((argc == 4) && (strncmp(argv[1], "post", 4) == 0)) {
>     CLI_LOGD("starting http(s) post url:%s\n", argv[2]);
>     demo_webclient_post(argv[2], argv[3]);
>   }
>   else {
>     CLI_LOGE("usage: webclient [url].\n");
>     goto error;
>   }
>   if (!ret) {
>     msg = WIFI_CMD_RSP_SUCCEED;
>     os_memcpy(pcWriteBuffer, msg, os_strlen(msg));
>     return;
>   }
> error:
>   msg = WIFI_CMD_RSP_ERROR;
>   os_memcpy(pcWriteBuffer, msg, os_strlen(msg));
>   return;
> }
> ```

<a id="id10"></a>

### 1.3 使用示例

> webclient \[ota\|get\|post\] \[url\] \[postdata\]
>
> ```
> webclient get http://www.baidu.com
> starting http(s) get url:http://www.baidu.com
> request header:
> GET / HTTP/1.1
> Host: www.baidu.com
> User-Agent: BEKEN HTTP Agent
> response header:
> HTTP/1.1 200 OK
> Accept-Ranges: bytes
> Cache-Control: no-cache
> Connection: keep-alive
> Content-Length: 29506
> Content-Type: text/html
> Date: Tue, 21 Oct 2025 07:06:46 GMT
> P3p: CP=" OTI DSP COR IVA OUR IND COM "
> P3p: CP=" OTI DSP COR IVA OUR IND COM "
> Pragma: no-cache
> Server: BWS/1.1
> Set-Cookie: BAIDUID=A9F4CAE2C24210E1742501480B71218D:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
> Set-Cookie: BIDUPSID=A9F4CAE2C24210E1742501480B71218D; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
> Set-Cookie: PSTM=1761030406; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
> Set-Cookie: BAIDUID=A9F4CAE2C24210E1DA8F773A71F84E68:FG=1; max-age=31536000; expires=Wed, 21-Oct-26 07:06:46 GMT; domain=.baidu.com; path=/; version=1; comment=bd
> Tr_id: pr_0x9afe527f011f1b6d
> Traceid: 176103040606074982506854824042807921914
> Vary: Accept-Encoding
> X-Ua-Compatible: IE=Edge,chrome=1
> X-Xss-Protection: 1;mode=block
> get position handle response(200).
> webclient get response data:
> bk_webclient_get bytes_read:4096 content_pos:4096
> bk_webclient_get bytes_read:4096 content_pos:8192
> bk_webclient_get bytes_read:4096 content_pos:12288
>
> bk_webclient_get bytes_read:4096 content_pos:16384
> bk_webclient_get bytes_read:4096 content_pos:20480
> bk_webclient_get bytes_read:4096 content_pos:24576
>
> bk_webclient_get bytes_read:4096 content_pos:28672
> bk_webclient_get bytes_read:834 content_pos:29506
> k_webclient_get ok
>
> $CMDRSP:OK
> ```
>
> ![说明](../../../../_assets/1cf101865ae7e8bec4b2-note.png)
>
> - 使用webclient命令需要确保cli\_netif.c模块参与编译
> - 使用webclient命令前需要确保模块连接到网络

<a id="id11"></a>

## 2 术语

> | **缩写** | **术语** | **描述** |
> | --- | --- | --- |
> | lwIP | 轻量级TCP/IP协议栈 | lwIP是一款广泛应用于嵌入式系统的轻量级开源TCP/IP协议栈。 |
> | RTOS | Real-Time Operating System | Real-Time Operating System是一种实时操作系统，用于为嵌入式系统提供实时性。 |
> | HTTP | Hyper Text Transfer Protocol | 超文本传输协议，是互联网上应用最广泛的客户端和服务器之间的通信协议。 |

文档版本 01 (2025-10-17) 版权所有 © 博通集成电路（上海）有限公司
