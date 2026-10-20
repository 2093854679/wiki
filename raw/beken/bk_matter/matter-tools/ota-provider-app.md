---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_matter/matter/zh_CN/v2.0.1/matter-tools/ota-provider-app/index.html
sdk_family: bk_matter
chip: BK7235,BK7236,BK7256,BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="matter-ota"></a>

# Matter OTA 测试工具

这里介绍使用 **chip-ota-provider-app** 进行Matter OTA测试的过程。
**chip-ota-provider-app** 会模拟Matter OTA 的 **provider** ，向设备发送OTA数据。
**Beken设备** 作为Matter OTA 的 **requestor** ，会接收OTA数据。

OTA基本过程是：在树莓派中使用 **chip-ota-provider-app** 模拟出一个 **provider**。
之后再开启一个新的树莓派终端来作为 **commissioner**，在这个新的 **commissioner终端** 中，
即要和前一个终端模拟出的 **provider** 配网，又要和 **Beken设备** 进行配网，使二者都在同一个Fabric网络中。
**provider** 配网完毕后, **commissioner终端** 需要配置provider的ACL访问权限，随后通知Beken设备有一个provider已经存在，从而开始OTA过程。

**1\. 制作OTA升级包**

使用由编译打包的时候自动化生成的RBL文件来生成Matter OTA文件。
编译生成的RBL文件一般存在于类似 build/matter/bk7236/encrypt/app\_pack.rbl 路径下，需根据具体项目而定。
执行如下命令生成OTA文件。

**其中设置的 -vn 版本号一定要比Beken设备中的版本号大，否则不会升级软件** 。

```
cd components/matter/connectedhomeip
./src/app/ota_image_tool.py create -v 0xDEAD -p 0xBEEF -vn 2 -vs "2.0" -da sha256 app_pack.rbl app_pack.ota
```

-v : vid

-p : pid

-vn : 软件版本号

-vs ：软件版本号，字符串格式

app\_pack.ota : 生成的Matter OTA文件

**2\. 启动provider**

在provider终端中执行如下命令。这里的 provider 也相当与一个Matter设备，它的作用是为其它设备提供OTA镜像下载。

```
./chip-ota-provider-app --discriminator 3855 --secured-device-port 5551 --KVS ./prokvs --filepath app_pack.ota -q updateAvailable
```

–KVS ./prokvs: 设置KVS存储路径， **每次要开启新的provider前，必须删除此文件**

–filepath app\_pack.ota : 将要升级的OTA文件

**3\. 将provider 配网加入 Matter fabric**

commissioner终端中执行如下指令，provider的 node id 为 3。

```
./chip-tool pairing onnetwork-long 3 20202021 3855
```

**4\. 赋予provider 权限**

commissioner终端中执行如下指令。

```
./chip-tool accesscontrol write acl '[{"fabricIndex": 1, "privilege": 5, "authMode": 2, "subjects": [112233], "targets": null}, {"fabricIndex": 1, "privilege": 3, "authMode": 2, "subjects": null, "targets": [{"cluster": 41, "endpoint": null, "deviceType": null}]}]' 3 0
```

**5\. 启动设备并配网**

commissioner终端中执行如下指令，Beken设备的 node id 为 1。

Beken设备的配网信息需要根据实际情况填写。

```
./chip-tool pairing ble-wifi 1 wifi_ssid wifi_pw 20202021 3840
```

**6\. 开始OTA升级**

commissioner终端中执行如下指令，发起OTA通知。

```
./chip-tool otasoftwareupdaterequestor announce-ota-provider 3 0 0 0 1 0
```

**7\. 确认OTA后的版本号**

显示OTA结束之后，commissioner终端中执行如下指令，查看Beken设备中的版本号是否已经更新。

```
./chip-tool basic read software-version 1  0
```

并在Beken设备的串口终端中，输入类似 ‘version get’ 命令，来确认是否是新的固件程序。
