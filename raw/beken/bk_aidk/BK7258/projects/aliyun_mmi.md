---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_aidk/bk7258/zh_CN/v2.0.1/projects/aliyun_mmi/index.html
sdk_family: bk_aidk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="aliyun-mmi"></a>

# 阿里云百炼（Aliyun MMI）工程

<a id="id1"></a>

## 1\. 简介

> 本工程基于 `beken_genie`，对接\*\*阿里云百炼多模态智能体（Bailian Multimodal Agent / MMI）\*\*。
>
> 工程目录名是 `aliyun_mmi`，不是 `bailian`。云端主机为 `bailian.multimodalagent.aliyuncs.com`。
>
> 配网、按键、灯效、双屏 AVI、唤醒词与 `beken_genie` 一致。硬件仍是 AIDK AI 玩具开发板。
>
> 详细硬件、按键、灯效、App 配网请参考：[博通集成精灵AI（Beken\_Genie）工程](beken_genie.md)
>
> 工程目录：`<source code>/projects/aliyun_mmi`
>
> 与 ``` lingxin``（阿里灵芯）不是同一个工程：灵芯走 ``LingXin_AI_IoT_VoiceChatEngine ```；本工程走阿里云 `aliyun_sdk` \+ 百炼 MMI 的 register / getToken / WSS。

<a id="beken-genie"></a>

## 2\. 与 beken\_genie 的差异

> - 打开 `CONFIG_ALIYUN_MMI_EN=y`，显示仍为双屏 AVI（`CONFIG_DUAL_SCREEN_AVI_PLAY=y`）。
> - 配网成功后走 `bk_smart_config` 的阿里云 adapter：设备注册、拉 Token，再由 `ali_wss` 按 SDK 给出的 host/api/port 建 WSS。
> - 对话模式默认双工（`C_MMI_MODE_DUPLEX`），文本上下行都开（`C_MMI_TEXT_MODE_BOTH`），默认音色 `longxiaochun_v2`。
> - 不使用声网 / 火山 RTC，也不走 `CONFIG_LINGXIN_AI_EN`。

<a id="id2"></a>

## 3\. 主要配置

> |  |  |  |  |
> | --- | --- | --- | --- |
> | Kconfig | CPU | Format | Value |
> | CONFIG\_ALIYUN\_MMI\_EN | CPU0 | bool | y |
> | CONFIG\_BK\_SMART\_CONFIG | CPU0 | bool | y |
> | CONFIG\_DUAL\_SCREEN\_AVI\_PLAY | CPU0 \& CPU1 | bool | y |
>
> 关键代码：
>
> - 注册 / Token：`projects/common_components/bk_smart_config/src/adapter/aliyun/bk_smart_config_ali_adapter.c`
> - WSS 传输：`projects/common_components/network_transfer/aliyun_wss/`
> - 事件回调与工作模式：`ali_wss_main.c` 中 `_mmi_event_callback`

<a id="id3"></a>

## 4\. 鉴权与连接

> adapter 里需要填百炼应用凭证（源码默认是占位符 `xxx`，不改无法连云）：
>
> - `C_APP_ID` / ``` C_APP_SECRET``（``bk_smart_config_ali_adapter.c ```）
> - 设备名用 Wi-Fi MAC 字符串写入 `c_storage`
>
> 联网后流程：
>
> 1. `c_mmi_sdk_init()`。
> 2. 未注册则 HTTPS POST `/api/device/v1/register` 到 `bailian.multimodalagent.aliyuncs.com`。
> 3. HTTPS POST `/api/token/v1/getToken` 取会话 Token。
> 4. `c_mmi_get_wss_host/api/port/header` 拼 `wss://<host>:<port><api>`，`ali_auto_run()` 建连。
> 5. MIC 数据 `c_mmi_put_recorder_data`，下行播放 `c_mmi_get_player_data`。
>
> 凭证请到阿里云百炼控制台申请，不要把真实 Secret 提交进公开仓库。

<a id="id4"></a>

## 5\. 编译与烧录

> - 源码根目录：`make bk7258 PROJECT=aliyun_mmi`
> - 固件：`<source code>/build/aliyun_mmi/bk7258/all-app.bin`
> - SD-NAND 眼睛 AVI 等资源与 `beken_genie` 相同。

<a id="id5"></a>

## 6\. 问题\&回答

Q：和灵芯工程怎么区分？

A：灵芯是 ``` projects/lingxin``（``CONFIG_LINGXIN_AI_EN ```）。百炼是本工程 ``` aliyun_mmi``（``CONFIG_ALIYUN_MMI_EN ```），云端是 `bailian.multimodalagent.aliyuncs.com`。

Q：编译能过但连不上？

A：先把 `C_APP_ID` / `C_APP_SECRET` 换成控制台真实值，并确认设备能访问上述 HTTPS / WSS 域名。
