---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_app/bkfil_v4/zh_CN/latest/flash_config/flash_config_guide/flash_config_guide.html
sdk_family: bk_toolkit
chip: ''
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="flash"></a>

# 外置 Flash 配置说明

本文档说明如何在本项目中进行\*\*外置 Flash 配置\*\*，以扩展或定制工具支持的 Flash 芯片列表，而无需修改内置配置。

备注

外置 Flash 配置功能仅在工具版本 **4.1.1.260312087** 及以上提供。

<a id="id1"></a>

## 概述

项目支持两类 Flash 配置来源：

| 类型 | 路径 | 说明 |
| --- | --- | --- |
| **内置配置** | 工具内置 | 随工具发布，包含 BK、GD、TH、XTX、BY、PY、UC、GT、XM 等厂商的多种 Flash。 |
| **外置配置** | 由用户指定路径的 YAML 文件（如 `flash_config_out.yaml`） | 用于\*\*追加\*\*内置中不存在的 Flash 型号，不修改、不覆盖内置配置。 |

工具运行时会先加载内置配置，再根据是否传入外置配置路径决定是否加载并\*\*合并\*\*外置配置。合并规则：**仅将外置文件中 MID 在内置里不存在的条目追加到总列表**，同 MID 时以内置为准。

<a id="id2"></a>

## 如何指定外置配置文件

<a id="bk-loader"></a>

### 命令行（bk\_loader）

通过参数 `--flash_config_path_out` 传入外置配置文件的\*\*绝对路径或相对路径\*\*：

```
bk_loader --flash_config_path_out /path/to/flash_config_out.yaml download -p COM3 ...
```

未传该参数或路径指向的文件不存在时，仅使用内置配置，不会报错。

<a id="flutter-ui"></a>

### Flutter UI

UI 在发起下载、擦除、读 Flash 等操作时，会自动设置外置配置路径，默认取自：

| 平台 | 默认外置配置文件路径 |
| --- | --- |
| **Windows / Linux** | `<可执行文件所在目录>/data/flutter_assets/assets/config/flash_config_out.yaml` |
| **macOS** | `<用户缓存目录>/bkfil/config/flash_config_out.yaml` |

因此：

- **使用默认路径**：在对应目录下创建或放置 `flash_config_out.yaml`，按下一节格式填写内容即可，UI 会自动传入该路径。

<a id="id3"></a>

## 外置配置文件格式

外置文件格式与内置配置\*\*完全一致\*\*：一个 YAML 数组，每个元素为一条 Flash 配置（共 9 列）。以下为格式示例。

<a id="id4"></a>

### 单条配置字段说明

| 列序号 | 字段名（含义） | 类型 | 说明 |
| --- | --- | --- | --- |
| 1 | **MID** | hex | Flash 厂商/型号 ID，用于与芯片读出的 Flash ID 匹配。 |
| 2 | **IC Name** | string | Flash IC 型号名称。 |
| 3 | **Manufactor** | string | 制造商。 |
| 4 | **Size** | int | 容量，单位为 bit（如 4MB 写为 `4*1024*1024`）。 |
| 5 | **UNPROT\_BITS** | 数组 | 解保护时状态寄存器控制位（bit 数组），一般关心 CMP、BPx。不关心填 `null`。 |
| 6 | **PROT\_BITS** | 数组 | 加保护时状态寄存器控制位（bit 数组），一般关心 CMP、BPx。 |
| 7 | **LB\_PROT\_BITS** | 数组 | LB 保护相关位，无则填 `null`。 |
| 8 | **R\_SR\_CMD** | hex 或 list | 读状态寄存器命令，最多 4 字节；多字节可写为 `[0x05, 0x35]`。 |
| 9 | **W\_SR\_CMD** | hex 或 list | 写状态寄存器命令（加/解保护）；0x01 支持多 SR 时有的芯片可只填 `0x01`。 |

同一 MID 若已在内置中存在，则外置中该条会被忽略（以内置为准）。

<a id="id5"></a>

### 配置格式示例（节选）

以下为内置配置的格式示例（节选）。外置配置使用相同格式，仅需提供需要\*\*追加\*\*的条目（MID 不与内置重复）：

<a id="id10"></a>

配置格式示例（节选）

```
# 该配置文件用于配置flash信息，工具会根据配置信息做相应的flash操作

# 注意: 错误的配置信息会导致不可预知的错误，添加新的flash的时请认真核对信息


#############################################################
#################       参数说明      ########################
#############################################################
# MID: flash MID，类型: hex   
# IC Name: flash的IC名称  类型:string
# Manufactor: 制造商      类型:string
# Size: flash容量         类型:int 单位为bit
# UNPROT_CMD: flash寄存器解保护控制位内容 (bit数组) 一般只关心CMP、BPx bit位
# PROT_CMD: flash寄存器加保护命令控制位内容 (bit数组)  一般只关心CMP、BPx bit位
# R_SR_CMD（Read status register）: 状态寄存器读命令，最多支持4个字节
# W_SR_CMD（Write status register）: 状态寄存器写命令(用于Flash加保护和解保护操作)(0x01支持写入多个SR时，可以忽略0x31指令，只填写0x01即可)

#############################################################
#################       如何添加新的flash      ###############
#############################################################
# 
#  1. 获取flash的datasheet
#  2. 从datasheet中获取上述"参数说明"中所需的信息
#  3. 参考下面已有的flash配置，添加后保存 （修改前建议备份一下配置文件，以便出现错误后恢复）
#  4. 关闭工具后重新打开
# 

[
  #       MID       |      IC Name         |      manufactor        |         size(bit)         |                                      UNPROT_BITS                                 |                              PROT_BITS                                        |                              LB_PROT_BITS                                                       |          R_SR_CMD             |        W_SR_CMD         
  #BK
  [  0x00424b01      ,     BK              ,        BK              ,     4 * 1024 * 1024       ,  [null, null, null, null, null, null, null, null]                               , [null, null, null, null, null, null, null, null]                               , [null, null, null, null, null, null, null, null]                                                ,          0xff                   ,         0xff             ],
  #GD
  [  0x00134051      ,     MD25D40D        ,        GD              ,     4 * 1024 * 1024       ,  [null, 0, 0, 0, 0, 0, null, null]                                              , [null, 0, 0, 1, 1, 1, null, null]                                              , [null, null, null, null, null, null, null, null]                                                ,          0x05                   ,         0x01             ],
  [  0x001540c8      ,     GD25Q16C        ,        GD              ,     16 * 1024 * 1024      ,  [null, 0, null, null, null, null, null, null, null, 0, 0, 0, 0, 0, null, null] , [null, 0, null, null, null, null, null, null, null, 0, 0, 1, 1, 1, null, null] , [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null],          [0x05, 0x35]           ,         0x01             ],
]
```

外置配置时，可复制上述或内置配置中任意一条，修改 MID、型号名、容量和寄存器相关字段后，放入外置 YAML 作为起点，再按 datasheet 调整。

<a id="datasheet-flash"></a>

## 根据 Datasheet 添加一款新 Flash 的详细步骤

下面说明如何从 Flash 芯片的 **datasheet（数据手册）** 中逐项提取信息，填成一条可用的配置。

<a id="datasheet"></a>

### 在 Datasheet 中需要找什么

建议先看目录，重点查找以下内容（不同厂商章节名可能略有差异）：

| 配置项 | Datasheet 中常见章节/表名 | 说明 |
| --- | --- | --- |
| **MID** | “Read ID” / “JEDEC ID” / “Manufacturer and Device ID” | 读 ID 命令（多为 **0x9F**）返回的字节。 |
| **容量** | “Memory Size” / “Density” / 型号后缀（如 Q16 \= 16Mbit） | 单位可能是 Mbit 或 Mbyte，需换算成本工具用的 **bit**。 |
| **状态寄存器** | “Status Register” / “SR” / “Block Protection (BP)” / “Security Registers” | 用于写保护/解保护，一般有 SR1、有的还有 SR2/SR3。 |
| **读 SR 命令** | “Read Status Register” / 指令表 | 常见：SR1\=\*\*0x05\*\*，SR2\=\*\*0x35\*\*，SR3\=\*\*0x15\*\*。 |
| **写 SR 命令** | “Write Status Register” / 指令表 | 常见：写 SR1\=\*\*0x01\*\*，写 SR2\=\*\*0x31\*\*，写 SR3\=\*\*0x11\*\*。 |

<a id="mid-flash-id"></a>

### MID（Flash 型号 ID）

- 工具通过 **SPI 命令 0x9F（Read JEDEC ID）** 从 Flash 读出 3 个字节，并组合成一个 24 位的 MID。
- **Datasheet 查法**：在 “Read JEDEC ID” 或 “Manufacturer and Device ID” 表中看返回值，通常为：
  \- **Byte 1**：Manufacturer ID（如 0xC8 \= GigaDevice）
  \- **Byte 2**：Device ID 高字节
  \- **Byte 3**：Device ID 低字节
- **配置写法**：将上述 3 字节按 **高字节在前** 组成一个 hex 数，前面补 0 写成 4 位或更多 hex，例如：
  \- 若返回 `0xC8, 0x40, 0x15`，则 MID \= ``` 0x001540c8``（即 0x15 0x40 0xC8 拼成 24 位，或 datasheet 写为 15 40 C8 时对应 ``0x001540c8 ```）。
- 若 datasheet 只写 “JEDEC ID: 15 40 C8”，则 MID 填 `0x001540c8` 即可（具体字节顺序以工具实际读出的 3 字节为准，可与已有同厂型号对照）。

<a id="size-bit"></a>

### Size（容量，单位 bit）

- 本工具配置里的 **Size 单位为 bit**，且为\*\*总容量\*\*。
- **Datasheet 常见写法**：如 “16 Mbit”、”2 MB”。
- **换算**：
  \- 若写的是 **Mbit**：Size \= 16\*1024\*1024（16Mbit）。
  \- 若写的是 **MB（Byte）**：先乘 8 再按 bit 算，如 2MB \= 2×1024×1024×8，也可写成 16×1024×1024（16Mbit）。
- 配置中直接写表达式即可，例如：`4*1024*1024`、`32*1024*1024`。

<a id="unprot-bits-prot-bits"></a>

### 状态寄存器与保护位（UNPROT\_BITS / PROT\_BITS）

工具在\*\*擦写前会解保护（unprotect）\*\*，**擦写后可选择加保护（protect）**。这通过\*\*写状态寄存器（Status Register）\*\* 实现，需要从 datasheet 中明确：

- 哪些\*\*位\*\*控制“块保护”（Block Protect，常叫 **BP2、BP1、BP0** 或 SR1 的 bit2\~bit4）；
- 是否有 **CMP（Complement Protect）** 等位；
- 解保护时这些位应写成 0 还是 1，加保护时写成 1 还是 0（有的芯片 CMP\=1 表示反转保护含义）。

**配置里的 bit 数组规则：**

- 数组按 **从高到低** 排列：**第 1 个元素对应字节的最高位（MSB），最后一个对应最低位（LSB）**。
- 若芯片有 **2 个状态寄存器 SR1、SR2**，则数组共 **16 个元素**：前 8 个是 SR1（bit7…bit0），后 8 个是 SR2（bit7…bit0）。
- 若芯片只有 **1 个状态寄存器（8 位）**，则数组共 **8 个元素**。
- 每个元素取值：
  \- `0` 或 `1`：表示解保护/加保护时要强制写成 0 或 1；
  \- `null`：表示不关心、不修改该位（读回后保留原值再写回）。

**Datasheet 典型 SR1 表（仅作示意）：**

| Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 名 | SRP | (reserved) | (reserved) | BP2 | BP1 | BP0 | WEL | BUSY |

- **解保护**：BP2、BP1、BP0 都应为 0，在对应位置填 `0`，其余不修改填 `null`。
- **加保护**：BP2、BP1、BP0 设为 1 表示保护一定区域，在对应位置填 `1`，其余填 `null`。

例如只关心 SR1 的 bit5\~bit2（BP2 BP1 BP0 和一位 reserved），8 位配置可写成：

- UNPROT：`[null, null, 0, 0, 0, 0, null, null]`（BP 全 0）
- PROT：`[null, null, 0, 1, 1, 1, null, null]`（BP 设为 111 表示全片保护，具体以 datasheet 为准）

若是 16 位（SR1\+SR2），则前 8 个为 SR1，后 8 个为 SR2；SR2 中不涉及的位全部填 `null`。

<a id="r-sr-cmd-w-sr-cmd"></a>

### R\_SR\_CMD 与 W\_SR\_CMD

- **R\_SR\_CMD（读状态寄存器）**
  \- Datasheet 中 “Read Status Register” 的指令码，常见：读 SR1 为 0x05，读 SR2 为 0x35，读 SR3 为 0x15。
  \- 若只有 1 个 SR：填 `0x05`。
  \- 若有 2 个 SR（SR1\+SR2）：填 `[0x05, 0x35]`，顺序与 UNPROT\_BITS/PROT\_BITS 的字节顺序一致（先 SR1 再 SR2）。
- **W\_SR\_CMD（写状态寄存器）**
  \- Datasheet 中 “Write Status Register” 的指令码，常见：写 SR1 为 0x01，写 SR2 为 0x31，写 SR3 为 0x11。
  \- 若芯片只支持用 0x01 写 SR1（一次写一个字节）：W\_SR\_CMD 填 `0x01` 即可；工具会按 R\_SR\_CMD 的个数依次写每个 SR。
  \- 若芯片支持分别写 SR1、SR2（如 0x01 写 SR1、0x31 写 SR2）：填 `[0x01, 0x31]`。
  \- 部分芯片 0x01 可一次写多个 SR，则有时只需填 `0x01`，具体以 datasheet 为准。

<a id="lb-prot-bits"></a>

### LB\_PROT\_BITS（可选）

- 部分 Flash 有 **Security Register / Lock Bit（LB）** 等保护，对应 SR2 或 SR3 的某些位。
- 若 datasheet 中有 “LB”、”Security Register”、”Block Protection (SR2)” 等表，且需要工具参与解/加保护，则在 **LB\_PROT\_BITS** 中按与 UNPROT\_BITS/PROT\_BITS 相同的 bit 顺序填写；不涉及则整段填 `null`。
- 若不确定，可先照抄同厂、同系列已支持型号的 LB\_PROT\_BITS（或全 `null`），再根据实测调整。

<a id="id6"></a>

### 完整示例：从 Datasheet 到一条配置

假设为 GD25Q16C（16Mbit）添加配置，从 datasheet 查到：

- **JEDEC ID**：15 40 C8 → MID \= `0x001540c8`
- **容量**：16 Mbit，Size \= `16*1024*1024`
- **SR1**：有 BP2、BP1、BP0；解保护时 BP\=000，加保护时 BP\=111；其余位不修改
- **SR2**：本工具不修改 → 全 null
- **读 SR**：0x05（SR1）、0x35（SR2）→ R\_SR\_CMD \= `[0x05, 0x35]`
- **写 SR**：0x01 写 SR1 即可（或 0x01/0x31 各写一个）→ W\_SR\_CMD \= `0x01` 或 `[0x01, 0x31]`

则配置中一条可写成（YAML 数组一行，这里拆成多行便于阅读）。示例：

```
[ 0x001540c8, "GD25Q16C", "GD", 16*1024*1024,
  [null, 0, null, null, null, null, null, null, null, 0, 0, 0, 0, 0, null, null],   # UNPROT: SR1 的 BP 全 0，SR2 不关心
  [null, 0, null, null, null, null, null, null, null, 0, 0, 1, 1, 1, null, null],   # PROT:  SR1 的 BP 设为 111，SR2 不关心
  [null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null],  # LB 不涉及
  [0x05, 0x35],
  0x01
]
```

若该芯片只有 8 位 SR1（无 SR2），则 UNPROT\_BITS/PROT\_BITS 只写 8 个元素，R\_SR\_CMD 只写 `0x05`，例如：

```
[ 0x00134051, "MD25D40D", "GD", 4*1024*1024,
  [null, 0, 0, 0, 0, 0, null, null],
  [null, 0, 0, 1, 1, 1, null, null],
  [null, null, null, null, null, null, null, null],
  0x05,
  0x01
]
```

<a id="id7"></a>

### 添加与验证流程小结

1. **拿到 datasheet**，按 4.1 的表格找到 JEDEC ID、容量、Status Register、读/写 SR 指令。
2. **确定 MID**：0x9F 返回的 3 字节 → 写成 `0x00MMMMDD` 形式。
3. **确定 Size**：按 Mbit/MB 换算成 bit，写 `N*1024*1024` 或等价表达式。
4. **画出 SR 的 bit 表**，确定哪些位是 BP/CMP，解保护与加保护时各应为何值；按 MSB 到 LSB、SR1 再 SR2 填 UNPROT\_BITS、PROT\_BITS（不修改的填 null）。
5. 填 R\_SR\_CMD、W\_SR\_CMD（单字节或列表），LB 不需要则 LB\_PROT\_BITS 全 null。
6. 在内置配置或外置 YAML 中新增一条，保存。
7. **验证**：连接真实设备，执行 download 或 erase，确认能识别到该 Flash 且擦写正常；若报 “No support flash” 请检查 MID 是否与工具读出的 3 字节一致。

备注

错误的 BP/CMP 或写 SR 命令可能导致无法解保护或误保护，修改前请备份配置文件，并严格按 datasheet 核对。

<a id="id8"></a>

## 添加新 Flash 的简要步骤（内置或外置）

1. 获取该 Flash 的 datasheet，按\*\*第 4 节\*\*逐项提取 MID、Size、状态寄存器及 R/W SR 命令。
2. 在内置配置或外置 YAML 中新增一条 9 列数组；外置时保存到 `flash_config_out.yaml` 或指定路径。
3. 命令行验证时加上 `--flash_config_path_out`；UI 验证时确保外置文件在默认路径。
4. 执行 download/erase 等操作，确认能识别并正常擦写。

<a id="id9"></a>

## 常见问题

**Q：外置配置不生效？**

- 确认传入的路径是否正确、文件是否存在。
- 确认外置文件是合法 YAML，且根节点为数组，每条为 9 列。
- 若 MID 与内置重复，会以内置为准，外置同 MID 条目不会生效。

**Q：UI 下外置文件放在哪里？**

- Windows/Linux：放在可执行文件目录下的 `data/flutter_assets/assets/config/flash_config_out.yaml`。
- macOS：放在用户缓存目录下的 `bkfil/config/flash_config_out.yaml`。
- UI 仅支持上述默认路径，不支持自定义路径。

**Q：修改配置后需要重启吗？**

- 每次执行 download/erase/read 等操作时会重新加载配置，无需重启进程；但若使用 UI，建议重新执行一次任务以确保读到最新文件内容。

—

以上即为本项目外置 Flash 的配置方式与说明。新增 Flash 时请务必对照 datasheet 核对 MID、容量及状态寄存器相关字段，避免误配置导致擦写异常。
