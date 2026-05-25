# 从零开发Matter 新的设备类型产品[](#matter "永久链接至标题")

[[English]](../../../en/v2.0.1/matter-develop/index.html "../../../en/v2.0.1/matter-develop/index.html")

这一小节通过在bk_matter基础上，新建一个 **On/Off Plug** 的Matter应用，用于详细说明bk_matter创建Matter新设备类型的过程。


## zap文件配置[](#zap "永久链接至标题")

zap文件是Matter的一个配置文件，可以通过参照 [matter协议](https://csa-iot.org/developer-resource/specifications-download-request/ "https://csa-iot.org/developer-resource/specifications-download-request/") `Device Library Specification` 对要实现的设备类型进行配置，关于zap工具的使用可以参考 [Matter 配置工具 ZAP](../matter-tools/zap/index.html "../matter-tools/zap/index.html") 。

关于Matter的一些基本概念的介绍可以参考 [Matter 简介](../matter-basic/index.html "../matter-basic/index.html") 。

zap工具会根据Matter的开发有多个版本，因此在目录 `components/matter/connectedhomeip/zap` 中包含了两个可执行文件：


- zap: 用于对zap文件进行可视化的编辑。修改配置zap文件时需要用到这个工具。

- zap-cli: 用于解析zap文件，在编译过程中会用到。

On/Off Plug设备将会包括两个endpoint。

endpoint 0 设备类型为 0x0016(Matter Root Node)，包含了Matter所有基础的cluster，基础信息配置（Basic Information cluster）、wifi（Network Commissioning，WiFi Network Diagnostics）、OTA（OTA Software Update Provider，OTA Software Update Requestor）等，对于所有类型的设备，这部分基本都一样。因此比较方便的做法是，直接在 `examples/lighting-app/lighting-common/lighting-app.zap` 文件的基础上进行修改，只保留endpoint 0 即可，按需添加新的endpoint即可。

endpoint 1 设备类型为 0x010A(On/Off Plug-in Unit)，对于具体cluster的配置，需要参考 `Device Library Specification` 文档。

On/Off Plug-in Unit Cluster Requirements[](#id5 "永久链接至表格")

| ID | Cluster | Client/Server | Quality | Conformance |
| --- | --- | --- | --- | --- |
| 0x0003 | Identify | Server |  | M |
| 0x0004 | Groups | Server |  | M |
| 0x0005 | Scenes | Server |  | P,M |
| 0x0006 | On/Off | Server |  | M |
| 0x0008 | Level Control | Server |  | O |

将文件保存为 `on-off-plug.zap` ，在下一小节中将会用到。


## 创建gn项目[](#gn "永久链接至标题")

1. 首先创建一个文件夹 `components/matter/connectedhomeip/examples/on-off-plug/beken` ，用于存放新设备的代码和配置。


```
mkdir -p components/matter/connectedhomeip/examples/on-off-plug/beken

```

2. 创建一些软链接，引入需要的一些依赖。


```
cd components/matter/connectedhomeip/examples/on-off-plug/beken
mkdir third_party
ln -s ../../build_overrides build_overrides
ln -s ../../../.. connectedhomeip

```

3. 创建文件 `.gn` ，gn项目的配置文件


```
 1# Copyright (c) 2022 Project CHIP Authors
 2#
 3# Licensed under the Apache License, Version 2.0 (the "License");
 4# you may not use this file except in compliance with the License.
 5# You may obtain a copy of the License at
 6#
 7# http://www.apache.org/licenses/LICENSE-2.0
 8#
 9# Unless required by applicable law or agreed to in writing, software
10# distributed under the License is distributed on an "AS IS" BASIS,
11# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
12# See the License for the specific language governing permissions and
13# limitations under the License.
14
15import("//build_overrides/build.gni")
16import("//build_overrides/chip.gni")
17
18# The location of the build configuration file.
19buildconfig = "${build_root}/config/BUILDCONFIG.gn"
20
21# CHIP uses angle bracket includes.
22check_system_includes = true
23
24default_args = {
25  target_cpu = "risc-v"
26  target_os = "freertos"
27
28  import("//args.gni")
29}

```

4. 创建文件 `args.gn` 对项目进行一些默认配置。


```
 1# Copyright (c) 2022 Project CHIP Authors
 2#
 3# Licensed under the Apache License, Version 2.0 (the "License");
 4# you may not use this file except in compliance with the License.
 5# You may obtain a copy of the License at
 6#
 7# http://www.apache.org/licenses/LICENSE-2.0
 8#
 9# Unless required by applicable law or agreed to in writing, software
10# distributed under the License is distributed on an "AS IS" BASIS,
11# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
12# See the License for the specific language governing permissions and
13# limitations under the License.
14
15# Options from standalone-chip.mk that differ from configure defaults. These
16# options are used from examples/.
17
18import("//build_overrides/chip.gni")
19
20chip_device_platform = "beken"
21
22chip_project_config_include = ""
23chip_system_project_config_include = ""
24chip_ble_project_config_include = ""
25
26mbedtls_target = "${chip_root}/config/beken/mbedtls:mbedtls"
27lwip_platform = "external"
28
29chip_build_tests = false
30
31chip_inet_config_enable_tcp_endpoint = false
32chip_inet_config_enable_udp_endpoint = true
33
34chip_config_network_layer_ble = true
35chip_config_memory_management = "platform"
36chip_enable_additional_data_advertising = false
37chip_enable_rotating_device_id = true
38chip_enable_ota_requestor = false
39chip_inet_config_enable_ipv4 = true
40
41chip_detail_logging = false
42chip_automation_logging = false
43chip_use_transitional_device_instance_info_provider = false
44chip_use_transitional_commissionable_data_provider = false
45
46custom_toolchain = "${chip_root}/config/beken/toolchain:beken"

```

其中第20行通过 `chip_device_platform = "beken"` 制定了Matter的编译平台，编译时将会使用 `src/platform/beken` 下的源码。

5. 创建 `BUILD.gn` 用于设置项目源码等。


```
 1# Copyright (c) 2020 Project CHIP Authors
 2#
 3# Licensed under the Apache License, Version 2.0 (the "License");
 4# you may not use this file except in compliance with the License.
 5# You may obtain a copy of the License at
 6#
 7# http://www.apache.org/licenses/LICENSE-2.0
 8#
 9# Unless required by applicable law or agreed to in writing, software
10# distributed under the License is distributed on an "AS IS" BASIS,
11# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
12# See the License for the specific language governing permissions and
13# limitations under the License.
14
15import("//build_overrides/build.gni")
16import("//build_overrides/chip.gni")
17import("${chip_root}/examples/common/pigweed/pigweed_rpcs.gni")
18import("${chip_root}/src/app/chip_data_model.gni")
19import("${chip_root}/examples/on-off-plug/beken/args.gni")
20
21examples_plat_dir = "${chip_root}/examples/platform/beken"
22
23chip_data_model("on-off-plug") {
24  zap_file = "on-off-plug.zap"
25
26  is_server = true
27}
28
29static_library("MatterApp") {
30  public_deps = [
31    ":on-off-plug",
32    "${chip_root}/examples/providers:device_info_provider",
33    "${chip_root}/src/platform/logging:default",
34  ]
35
36  include_dirs = [
37    "${chip_root}/examples/on-off-plug/beken/main/include",
38    "${examples_plat_dir}",
39  ]
40
41  if (chip_enable_ota_requestor) {
42    sources = [
43      "${examples_plat_dir}/common/BekenAppServer.cpp",
44      "${examples_plat_dir}/common/CHIPDeviceManager.cpp",
45      "${examples_plat_dir}/common/CommonDeviceCallbacks.cpp",
46      "${examples_plat_dir}/ota/OTAHelper.cpp",
47      "main/DeviceCallbacks.cpp",
48      "main/DsoHack.cpp",
49      "main/chipinterface.cpp",
50      "main/Plug.cpp",
51    ]
52  } else {
53    sources = [
54      "${examples_plat_dir}/common/BekenAppServer.cpp",
55      "${examples_plat_dir}/common/CHIPDeviceManager.cpp",
56      "${examples_plat_dir}/common/CommonDeviceCallbacks.cpp",
57      "main/DeviceCallbacks.cpp",
58      "main/DsoHack.cpp",
59      "main/chipinterface.cpp",
60      "main/Plug.cpp",
61    ]
62  }
63
64  output_name = "libMatterApp"
65  output_dir = "${root_out_dir}/lib"
66  complete_static_lib = true
67}
68
69group("default") {
70  deps = [ ":MatterApp" ]
71}
72
73config("config") {
74  include_dirs = [ "include" ]
75}

```

第40-49行主要包括了此Matter device的应用层代码。

第22-27行通过函数 `chip_data_model` 传入了zap配置文件。
因此需要将上一小节中创建的zap文件 `on-off-plug.zap` ，复制到改改目录下。
另外，需要目录 `components/matter/connectedhomeip` 中执行


```
./scripts/tools/zap/generate.py examples/on-off-plug/beken/on-off-plug.zap

```

这将会生成 `on-off-plug.matter` 文件。

编译过程中将会根据这个两个文件选择需要的cluster加入源码，并生成一些代码。关于这部分的原理，可以参考Matter 的文档 [code_generation](https://project-chip.github.io/connectedhomeip-doc/code_generation.html "https://project-chip.github.io/connectedhomeip-doc/code_generation.html") 。


## 实现相关代码[](#id3 "永久链接至标题")

1. 实现plug设备的基本操作，主要实现对插座设备的初始化开关等操作

Plug.cpp[](#id6 "永久链接至代码")


```
 1#define KEY_GPIO        GPIO_24
 2#define CONTROL_GPIO    GPIO_26
 3#define LED_GPIO        GPIO_9
 4
 5void Plug::Init()
 6{
 7    ChipLogDetail(DeviceLayer,"Plug Init");
 8    gpio_config_t cfg;
 9	gpio_int_type_t int_type = GPIO_INT_TYPE_MAX;
10
11    bk_gpio_disable_input(CONTROL_GPIO);
12    bk_gpio_enable_output(CONTROL_GPIO);
13
14    bk_gpio_disable_input(LED_GPIO);
15    bk_gpio_enable_output(LED_GPIO);
16
17    cfg.io_mode =GPIO_INPUT_ENABLE;
18	int_type = GPIO_INT_TYPE_FALLING_EDGE;
19	cfg.pull_mode = GPIO_PULL_UP_EN;
20	bk_gpio_set_config(KEY_GPIO, &cfg);
21	bk_gpio_register_isr(KEY_GPIO ,key_callback);
22    bk_gpio_enable_interrupt(KEY_GPIO);
23
24    bk_gpio_set_output_high(CONTROL_GPIO);
25    bk_gpio_set_output_high(LED_GPIO);
26    isOn = false;
27    mFlashingFreq = 0;
28    initOver = false;
29}
30
31void Plug::StartUpInit()
32{
33    ChipLogDetail(DeviceLayer,"Plug StartUpInit");
34    if (Server::GetInstance().GetFabricTable().FabricCount() == 0)
35    {
36        LedStartFlashing(false);
37    }
38    initOver = true;
39}
40
41void Plug::SetOnOff(bool on)
42{
43    ChipLogDetail(DeviceLayer,"Plug SetOnOff");
44    if(!initOver || mFlashingFreq != 0 || on == isOn)
45    {
46        return;
47    }

```

2. 实现Matter的回调，Matter协议接收到控制端相关属性的更改后，会调用对应的回调

DeviceCallbacks.cpp[](#id7 "永久链接至代码")


```
 1void AppDeviceCallbacks::PostAttributeChangeCallback(EndpointId endpointId, ClusterId clusterId, AttributeId attributeId,
 2                                                     uint8_t type, uint16_t size, uint8_t * value)
 3{
 4    switch (clusterId)
 5    {
 6    case Clusters::OnOff::Id:
 7        OnOnOffPostAttributeChangeCallback(endpointId, attributeId, value);
 8        break;
 9    default:
10        ChipLogProgress(Zcl, "Unknown cluster ID: " ChipLogFormatMEI, ChipLogValueMEI(clusterId));
11        break;
12    }
13}
14void AppDeviceCallbacks::OnOnOffPostAttributeChangeCallback(EndpointId endpointId, AttributeId attributeId, uint8_t * value)
15{
16    VerifyOrExit(attributeId == Clusters::OnOff::Attributes::OnOff::Id,
17                 ChipLogError(DeviceLayer, "[%s] Unhandled Attribute ID: '0x%04lx", TAG, attributeId));
18    VerifyOrExit(endpointId == 1 || endpointId == 2,
19                 ChipLogError(DeviceLayer, "[%s] Unexpected EndPoint ID: `0x%02x'", TAG, endpointId));
20    PlugMgr().SetOnOff(*value);
21
22exit:
23    return;
24}

```

3. 启动Matter进程，初始化并启动Matter CHIP进程

chipinterface.cpp[](#id8 "永久链接至代码")


```
 1static AppDeviceCallbacks EchoCallbacks;
 2static void InitServer(intptr_t context)
 3{
 4    chip::BekenAppServer::Init();
 5    gExampleDeviceInfoProvider.SetStorageDelegate(&Server::GetInstance().GetPersistentStorage());
 6    chip::DeviceLayer::SetDeviceInfoProvider(&gExampleDeviceInfoProvider);
 7#if CHIP_DEVICE_CONFIG_ENABLE_OTA_REQUESTOR
 8    OTAHelpers::Instance().InitOTARequestor();
 9#endif
10    PlugMgr().StartUpInit();
11}
12
13{
14    ChipLogProgress(DeviceLayer, "on-off-plug!");
15    chip::Inet::UDPEndPointImplLwIP::SetQueueFilter((chip::Inet::EndpointQueueFilter *)&filter);
16
17    CHIPDeviceManager & deviceMgr = CHIPDeviceManager::GetInstance();
18    err                           = deviceMgr.Init(&EchoCallbacks); // start the CHIP task
19    if (err != CHIP_NO_ERROR)
20    {
21        ChipLogError(DeviceLayer, "DeviceManagerInit() - ERROR!\r\n");
22    }
23    else
24    {
25        ChipLogProgress(DeviceLayer, "DeviceManagerInit() - OK\r\n");
26        vTaskDelay(pdMS_TO_TICKS(50)); // Just server the application event handler
27    ChipLogProgress(SoftwareUpdate, "Exited");

```


## 编译[](#id4 "永久链接至标题")

修改对应的配置文件 `projects/matter/config/bk7258/config` 中的配置 `CONFIG_MATTER_EXAMPLE="on-off-plug"`

即可编译新建的Matter 应用


```
make bk7258 PROJECT=matter

```
