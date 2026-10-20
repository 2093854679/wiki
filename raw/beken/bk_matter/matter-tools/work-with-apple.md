---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_matter/matter/zh_CN/v2.0.1/matter-tools/work-with-apple/index.html
sdk_family: bk_matter
chip: BK7235,BK7236,BK7256,BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="matter"></a>

# Matter 生态配网测试

<a id="apple-home"></a>

## Apple home

apple生态在配对时会进行两次配对过程：第一次由home app进行配对；第二次由home app分享，homepod音响配对。

**配对**

参考 [配对和管理 Matter 配件](https://support.apple.com/zh-cn/HT213441) ，在iPhone上添加Matter设备。

在 iPhone 或 iPad 上打开“家庭”App，然后轻点“添加”按钮 。
轻点“添加配件”。如果 Matter 配件之前已与另一个 App 配对，请轻点“更多选项”，然后选择你的 Matter 配件。
按照屏幕上的说明完成设置。

警告

你必须设置 [家居中枢](https://support.apple.com/zh-cn/HT213441) ，才能向“家庭”App 添加受支持的 Matter 配件。

**删除设备**

1. 在“Matter 配件”屏幕上，轻点某个配件。
2. 轻点“编辑”。
3. 轻点要移除的配件旁边的“删除”按钮 。
4. 轻扫或轻点“移除”，以确认要移除相应配件。
5. 轻点“从 \[已连接的服务\] 移除”以确认移除。

目前apple生态移除时，可能仅仅删除已一个fabric，需要在设备端执行matter\_factory\_reset进行进行重置才能再次进入配网模式。

<a id="amazon-alexa"></a>

## Amazon Alexa

Alexa app在ios端和android端都可以添加管理Matter设备。

**配对**

1. 打开Alexa app。
2. 点击屏幕下方的Devices按键。
3. 点击屏幕右上方的”\+”按键。
4. 点击”Add Device”按键。
5. 向下滚动屏幕，点击”Other”，点击”Matter”。
6. 按照屏幕提示扫描二维码开始配对。

**删除设备**

1. 点击屏幕下方的Devices按键。
2. 点击”All Device”，选择要删除的设备。
3. 点击右上角的设置图标。
4. 点击右上角的删除图标。
5. 点击”DELETE”，删除设备。

警告

你必须设置家居中枢Amazon Echo，才能配对控制Matter设备。

<a id="google-home"></a>

## Google home

**配对**

1. 打开GHA(Google Home App)。
2. 点击”\+”图标。
3. 点击”Set up device”，点击”New device”。
4. 选择家点击”Next”
5. GHA将扫描你的设备。 一旦它提示你是否想设置你的设备，请点击”Set up a different device”。
6. 点击”Matter device”。
7. 扫描二维码完成配对。

警告

Google 生态无法配对未认证设备，需要使用经过认证的证书和cd

警告

Google 生态需要 [中控](https://support.google.com/googlenest/answer/12391458) ，才能控制Matter设备

**删除设备**

1. 点击设备。
2. 点击设置。
3. 点击删除设备。
