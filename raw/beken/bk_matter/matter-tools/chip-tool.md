# 测试工具 chip-tool[](#chip-tool "永久链接至标题")

[[English]](../../../../en/v2.0.1/matter-tools/chip-tool/index.html "../../../../en/v2.0.1/matter-tools/chip-tool/index.html")

chip-tool 是一个linux工具，可用于配对测试matter设备，详细使用方式可以参考 [这里](https://project-chip.github.io/connectedhomeip-doc/guides/chip_tool_guide.html#commissioning-into-a-wi-fi-network-over-bluetooth-le "https://project-chip.github.io/connectedhomeip-doc/guides/chip_tool_guide.html#commissioning-into-a-wi-fi-network-over-bluetooth-le") 。


## 配对命令[](#id2 "永久链接至标题")


```
./chip-tool pairing ble-wifi <node_id> <ssid> <password> <pin_code> <discriminator>

```

在这个命令中：


- <node_id> 用户自定义的被配对设备的ID

- <ssid> 和 <password> 给被配对设备设置的wifi和密码

- <pin_cod> 和 <discriminator> 是针对被配对设备的密钥


## 控制 onoff[](#onoff "永久链接至标题")


```
./chip-tool onoff toggle <node_id> <endpoint_id>

```

在这个命令中：


- <node_id> 是被控制设备的ID

- <endpoint_id> 是实现了onoff cluster 的endpoint 的 ID
