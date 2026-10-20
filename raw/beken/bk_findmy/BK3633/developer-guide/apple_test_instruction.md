---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_findmy/bk3633/zh_CN/v2.0.1/developer-guide/apple_test_instruction/index.html
sdk_family: bk_findmy
chip: BK3633
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 测试说明

<a id="id2"></a>

## 1.开发板上电

<a id="id11"></a>
[![test instruction](../../../_assets/6576b1bbaabdce732e48-fmna_0.png)](../../../_assets/6576b1bbaabdce732e48-fmna_0.png)


开发板

<a id="id3"></a>

## 2.手机蓝牙绑定追踪器

1）先打开iPhone的蓝牙功能，再打开iPhone的“查找”应用程序

<a id="id12"></a>
![test instruction 1](../../../_assets/f75020ce7062fd10295e-fmna_1.png)


查找应用程序

2）在APP中点击 添加物品-\>其他支持的物品

<a id="id13"></a>
![test instruction 2](../../../_assets/b053f7ba49a0a4f84571-fmna_3_1.png)


添加其他物品

3）搜索到后，为它取一个名字，并选取一个图标，以方便识别

<a id="id14"></a>
![test instruction 3](../../../_assets/deb2f7c773b55e3c14f1-fmna_6_1.png)


连接

4）阅读并同意设备使用定位协议后，即完成绑定

<a id="id15"></a>
![test instruction 4](../../../_assets/49f99e8fe6bf5941ecc5-fmna_8_1.png)


绑定完成

<a id="id4"></a>

## 3.查找物品功能

> 当你想寻找这个物品时，在物品列表中点击你要查找的物品，并点击“播放声音”，设备就会滴滴响5秒

<a id="id16"></a>
![play sound](../../../_assets/bcceb9c2bc0590753e9a-fmna_11_1.png)


播放声音

<a id="id5"></a>

## 4.物品遗落通知功能

> 在APP中开启“遗落时通知”功能，当用户离开某区域，不小心把放有追踪器的物品遗落在原地，iPhone将受到该设备被遗落的通知。

<a id="id17"></a>
![lost](../../../_assets/8d8fcfec5e12b974e0a9-fmna_12.png)


遗落通知

<a id="id6"></a>

## 5.发现通知

> 在APP中开启“找到时通知”功能，当追踪器已与配对的iPhone断开。当iPhone靠近追踪器时，手机会自动连接到追踪器上，用户将收到物品在附近的即时通知。

<a id="id18"></a>
![find lost](../../../_assets/3288b2b0d18d63c0d98f-fmna_13_1.png)


发现通知

<a id="id7"></a>

## 6.丢失模式——开启丢失模式

> 当物品丢失时，要打开丢失模式，在APP的物品列表里，点击你丢失的物品。找到“丢失模式”，点击“启用”。

<a id="id19"></a>
![lost 1](../../../_assets/4a7e1407a49469581b4d-fmna_13_2.png)


启用丢失模式

> 点击“继续”，输入你的电话号码，然后点击“下一步”。

<a id="id20"></a>
![lost 2](../../../_assets/13a4967f435c89f65151-fmna_14_1.png)


输入电话号码

> 打开“找到时通知”开关-\>”启用”。

<a id="id21"></a>
![lost 3](../../../_assets/07ba3b7f9be5ade154c3-fmna_17_1.png)


启用找到时通知

<a id="id8"></a>

## 7.丢失模式——拾物者查询失主信息

1）如果拾到别人的追踪器，打开iPhone的蓝牙功能，并打开APP在“物品”页面点击“识别找到的物品”。

<a id="id22"></a>
![lost 4](../../../_assets/17cc3e10dc7e793d730c-fmna_16.png)


识别找到的物品

2）点击搜索到的物品名称，然后点击“继续”。

<a id="id23"></a>
![lost 5](../../../_assets/10d8675e7e2b34174c3d-fmna_22.png)


搜索物品

3）按下按键，听到哔的一声后松开按键，等待约几分钟后，点击“在网站上继续”。

<a id="id24"></a>
![lost 6](../../../_assets/5e4cfef3326ad606c86f-fmna_24.png)


点击在网站上继续

4）查询到失主联系方式。

<a id="id25"></a>
![lost 7](../../../_assets/ed2942554db2a8645fcf-fmna_25.png)


查询到失主联系方式

<a id="id9"></a>

## 8.运动检测模式

> 在进入分离状态3天后自动开启。追踪器每隔6小时进入到“等待移动”状态，在“等待移动”状态检测到自身有运动就会发出5秒的报警声音。

<a id="id10"></a>

## 9.移除跟踪器绑定

> - 清除追踪器上的配对
>   :   长按追踪器上按键，当听到三声哔哔声时，继续按住，直到听到响亮的哔哔声。追踪器将恢复到出厂设置，这将清除追踪器配对信息。
> - 手机端移除
>   :   在Find My APP中移除时，需要与苹果设备连接的状态下移除，这样可以同步清除追踪器中的配对信息，如果在未连接的状态下移除，只能在苹果设备上移除，追踪器中的配对信息还在，并不会再发配对广播，所以就不会再被发现并添加。

<a id="id26"></a>
![remove](../../../_assets/16a22b1aadb1571ff3b7-fmna_20_1.png)


移除跟踪器绑定

备注

关于蜂鸣器的声音
:   - 开机 哔哔两声；
    - 连接成功 哔一声；
    - 移除成功 持续的哔\~\~声音；
    - 获取serial number，按2s, 哔一声；
    - 删除配对信息，长按，当听到哔哔哔三声时，继续按住，直到听到持续的哔\~\~声音，此时配对信息删除成功；
