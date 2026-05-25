# WSL2 下 ESP-IDF 开发完整指南

本文档整合：ESP-IDF 编译命令、WSL2 开发流程、WSL 代理设置。

---

## 一、WSL 代理设置（可选）

开发前若需访问外网（安装依赖、拉取组件等），可在 WSL 中配置代理。

### 1. Git 代理

**设置代理：**

```bash
git config --global http.proxy http://192.168.224.1:7890
git config --global https.proxy http://192.168.224.1:7890
```

**取消代理：**

```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

**查看当前代理：**

```bash
git config --global --get http.proxy
git config --global --get https.proxy
```

### 2. 终端环境变量代理

**临时设置（当前终端有效）：**

```bash
export http_proxy=http://192.168.224.1:7890
export https_proxy=http://192.168.224.1:7890
# SOCKS5 可选
export all_proxy=socks5://192.168.224.1:7890
```

**临时取消：**

```bash
unset http_proxy
unset https_proxy
unset all_proxy
```

**永久生效：** 在 `~/.bashrc` 或 `~/.zshrc` 末尾加入上述 `export` 行，保存后执行 `source ~/.bashrc`（或 `source ~/.zshrc`）。

**永久取消：** 删除 `~/.bashrc` / `~/.zshrc` 中的代理相关行，再 `source` 一次。

### 3. 桌面应用（可选）

- 系统设置 → 网络 → 代理 → 设为 **None / 不使用**
- 使用 Clash、V2Ray 等时，可关闭全局/系统代理，仅用环境变量或 Git 代理

---

## 二、ESP-IDF 环境准备

### 2.1 首次安装（仅一次）

```bash
cd ~/esp32/esp-idf
export http_proxy=http://192.168.224.1:7890
export https_proxy=http://192.168.224.1:7890
./install.sh
```

> 安装 ESP-IDF Python 虚拟环境和工具链；需代理时先设置环境变量。

### 2.2 激活环境（每次新开终端）

```bash
cd ~/esp32/esp-idf
. ./export.sh
```

或：

```bash
. ~/esp32/esp-idf/export.sh
```

> 注意：开头是 **点+空格** `.`，将 `idf.py` 和工具链加入当前 shell。  
> 可将 `source ~/esp32/esp-idf/export.sh` 写入 `~/.bashrc` / `~/.zshrc`，实现打开终端自动激活。

---

## 三、WSL2 串口映射（烧录/监控前必做）

WSL2 默认不能直接访问 Windows 的 USB 串口，需用 **usbipd** 把串口“挂”到 WSL2。

1. **在 Windows PowerShell（管理员）** 安装 usbipd：

   ```powershell
   winget install usbipd
   ```

2. **查看 USB 设备**，找到 ESP32 对应的 BUSID：

   ```powershell
   usbipd list
   ```

   示例：`1-9    10C4:EA60  USB Serial` → BUSID 为 `1-9`。

3. **绑定并挂载到 WSL2**（将 `4-4` 换成你的 BUSID）：

   ```powershell
   usbipd bind --busid 3-1
   usbipd attach -b 3-1 -w
   ```

4. **在 WSL2 里确认串口**：

   ```bash
   ls /dev/tty*
   ```

   常见为 `/dev/ttyACM0` 或 `/dev/ttyUSB0`。

5. **赋予权限**：

   ```bash
   sudo chmod 777 /dev/ttyACM0
   ```

6. **烧录后可解绑（可选）**：

   ```powershell
   usbipd detach -b 4-4
   ```

---

## 四、项目配置与编译流程

### 4.1 进入项目目录

```bash
cd ~/esp32/project/graduation-software/xiaozhi-esp32-main-v2/xiaozhi-esp32
# 或你的实际项目路径
```

### 4.2 设置目标芯片（首次或换芯片时）

```bash
idf.py set-target esp32s3
```

### 4.3 配置工程

```bash
idf.py menuconfig
```

可配置：串口、芯片型号、Flash 大小与频率、分区表、功能模块等。按 **S** 保存，**Q** 退出。

### 4.4 编译

```bash
idf.py build
```

成功后会提示：`Project build complete. To flash, run 'idf.py -p (PORT) flash'`。

### 4.5 烧录

```bash
# 串口以实际为准，如 /dev/ttyACM0 或 /dev/ttyUSB0
idf.py -p /dev/ttyACM0 flash
```

> `-p` 指定串口；ESP-IDF 会按分区表擦写并烧录固件。

### 4.6 串口监控

```bash
idf.py -p /dev/ttyACM0 monitor
```

退出监控：**Ctrl+]**。

### 4.7 一键流程示例

```bash
# 激活环境（若未写入 .bashrc）
. ~/esp32/esp-idf/export.sh

# 进入项目
cd ~/esp32/project/graduation-software/xiaozhi-esp32-main-v2/xiaozhi-esp32

# 配置、编译、烧录、监控
idf.py menuconfig
idf.py build
idf.py -p /dev/ttyACM0 flash
idf.py -p /dev/ttyACM0 monitor
```

---

## 五、ESP-IDF 常用命令归纳

### 5.1 配置

| 命令 | 说明 |
|------|------|
| `idf.py menuconfig` | 图形化配置（芯片、串口、分区表、功能等） |
| `idf.py defconfig` | 恢复默认配置 |
| `idf.py fullclean` | 完全清理 build 与缓存（相当于重置） |

### 5.2 编译

| 命令 | 说明 |
|------|------|
| `idf.py build` | 编译工程 |
| `idf.py build -j N` | 多线程编译，如 `idf.py build -j 8` |
| `idf.py build flash` | 编译完成后直接烧录 |

### 5.3 烧录

| 命令 | 说明 |
|------|------|
| `idf.py -p /dev/ttyACM0 flash` | 指定串口烧录 |
| `idf.py -p /dev/ttyACM0 erase-flash` | 擦除整片 Flash |

### 5.4 清理

| 命令 | 说明 |
|------|------|
| `idf.py clean` | 清理 build 目录（保留部分缓存） |
| `idf.py fullclean` | 完全清理（含 CMake 配置，相当于新工程） |

### 5.5 调试与信息

| 命令 | 说明 |
|------|------|
| `idf.py -p /dev/ttyACM0 monitor` | 串口监控；退出 **Ctrl+]** |
| `idf.py size` | 查看固件大小（Flash/RAM） |
| `idf.py size-components` | 各组件占用 |
| `idf.py reconfigure` | 重新生成 CMake（改过 CMakeLists 时用） |
| `idf.py clean build` | 先清理再编译 |

---

## 六、使用 esptool 手动烧录（可选）

若需自定义地址或单独烧录 assets 等：

```bash
python -m esptool --chip esp32s3 -b 460800 \
  --before default_reset --after hard_reset \
  write_flash --flash_mode dio --flash_size 16MB --flash_freq 80m \
  0x0 build/bootloader/bootloader.bin \
  0x8000 build/partition_table/partition-table.bin \
  0xd000 build/ota_data_initial.bin \
  0x10000 build/srmodels/srmodels.bin \
  0x100000 build/xiaozhi.bin
```

烧录 assets 分区示例（地址、路径按实际分区表修改）：

```bash
python -m esptool --chip esp32s3 --port /dev/ttyACM0 --baud 460800 \
  write_flash 0x920000 /path/to/assets.bin
```

---

## 七、常见问题

- **串口找不到**：确认已在 Windows 用 usbipd 绑定并 attach 到 WSL2，且在 WSL 中执行 `chmod`。
- **权限拒绝**：`sudo chmod 666 /dev/ttyACM0` 或把用户加入 `dialout` 组。
- **编译/下载慢**：需要时在 WSL 中配置代理（见第一节），再执行 `install.sh` 或 `idf.py build`。
- **分区表/固件过大**：在 menuconfig 的 **Partition Table** 中选用工程提供的自定义 CSV（如 desktop-pet 的 `16m_desktop_pet_single_app.csv`），路径不要带前导空格。

---

*文档合并自：esp-idf编译命令.md、wsl开发esp.md、wsl走代理方法.md*
