## Background and Motivation
- 目标：将 startnorva 的 `app1_page`（时钟页）背景从固件内置资源 `img_picture`，改为 **从 SD 卡读取** `clock/1.bmp`（用户确认该 BMP 为 16 位）。
- 约束：用户要求 **一次只改一个文件**，改完一个文件必须等待用户确认后才能继续下一个文件。
- 新任务：在 startnorva 屏幕实现 **手动输入 SSID/密码 的 WiFi 连接界面**，入口放在 `app3_page` 按钮，物理分辨率 240×280（UI 坐标系按 280×240 继续布局）。
- 新问题：WiFi 页面无法左滑返回（用户决定只保留返回按钮即可）；软键盘不显示；屏幕偏小希望改成 **T9 多字母按键** 输入（同键循环选字母）。

## Key Challenges and Analysis
- **LVGL 解码与文件系统**：需要在 menuconfig 已启用 `LV_USE_BMP` 与 `LV_USE_FS_FATFS`，并设置 `LV_FS_FATFS_LETTER = 'S'`（ASCII 83）。用户已完成该配置。
- **初始化时序**：当前 `ui_init()` 在显示初始化阶段执行，而 `sd_card_init()` 在 `startnorva()` 构造后段执行。若在 `screens.c` 创建时直接将背景 src 设为 `S:/clock/1.bmp`，可能因 SD 尚未挂载导致打开失败。
- **FatFs 路径与盘符**：LVGL 的 FatFs 驱动会把 `S:/clock/1.bmp` 解析为 FatFs 路径 `/clock/1.bmp`（不含 `0:`）。为稳妥需在 SD 挂载成功后 `f_chdrive("0:")`，确保默认盘正确。
- **线程安全**：修改 LVGL 对象需使用 `lvgl_port_lock/unlock`（项目已使用）。
- **键盘组件依赖**：当前 LVGL 键盘在默认配置中关闭；即使启用也会占屏，需要更轻量的 T9 键盘（按钮矩阵 + 计时确认）。

## High-Level Task Breakdown
1) 在 UI 的 `objects_t` 中保存时钟页背景 `lv_img` 对象指针（新增字段 `app1_bg_img`）。
   - 成功标准：编译通过；运行时 `objects.app1_bg_img` 非空（可通过日志/调试验证）。
2) 在创建时钟页时将背景 `lv_img` 对象写入 `objects.app1_bg_img`（仍先用 `img_picture` 兜底）。
   - 成功标准：编译通过；UI 逻辑不变；背景仍正常显示。
3) 在 SD 挂载成功后切换背景：`lv_img_set_src(objects.app1_bg_img, "S:/clock/1.bmp")`，并 `f_chdrive("0:")`。
   - 成功标准：启动后时钟页背景显示为 SD 中 `clock/1.bmp`；串口日志能看到切换动作与必要的错误日志（若失败）。

## Project Status Board
- [x] 1. 给 `objects_t` 增加 `app1_bg_img` 字段
- [ ] 2. 在 `create_screen_app1_page()` 保存背景对象到 `objects.app1_bg_img`
- [ ] 3. SD 挂载成功后切换背景到 `S:/clock/1.bmp`（含 `f_chdrive("0:")` 与 LVGL 加锁）

### WiFi UI
- [x] 1. 定位 esp-wifi-connect 组件头文件（wifi_station/ssid_manager/wifi_configuration_ap）
- [x] 2. 扩展 `screens.h`：新增 wifi 页面对象指针与 Screen ID
- [x] 3. 新增 `wifi_page` 界面布局（标题/输入框/键盘/状态/连接按钮）
- [x] 4. `app3_page` 增加 WiFi 入口按钮
- [x] 5. actions 实现：进入/返回/连接/状态更新与日志输出
- [ ] 6. 手动测试与结果记录
- [x] 7. 改为 T9 键盘（按钮矩阵）并修复键盘显示问题

## Current Status/Progress Tracking
- menuconfig：用户已启用 `File system on top of FatFS`（letter=83/'S'）与 `BMP decoder library`。
- 已完成：`screens.h` 增加 `objects.app1_bg_img` 字段。
 
 进行中：准备修改 `screens.c`，在创建时钟页背景时保存对象指针到 `objects.app1_bg_img`。

- WiFi 组件头文件来源：`/home/hghhgh/.cache/Espressif/ComponentManager/.../78__esp-wifi-connect_2.5.2_.../include/`，可用 API 包括 `WifiStation::AddAuth/Start/WaitForConnected`、`WifiConfigurationAp::ConnectToWifi/Save`、`SsidManager::AddSsid`。
- WiFi UI：已新增 `wifi_page`、入口按钮与事件处理；`sdkconfig.defaults` 启用 `LV_USE_BTNMATRIX`，禁用 `LV_USE_KEYBOARD`。
- WiFi UI：已替换为 T9 按钮矩阵键盘（`lv_btnmatrix`），移除 `lv_keyboard` 依赖；支持同键循环选字母（超时自动确认）。
- 修复中：点击输入框未弹出键盘，已对输入框增加 `LV_EVENT_PRESSED` 并将键盘置顶显示。
- 继续修复：将按钮矩阵宏与 API 更正为 `LV_USE_BUTTONMATRIX` + `lv_buttonmatrix_*`（之前使用了旧命名导致键盘未创建）。
- UI调整：WiFi 页面左上角添加返回按钮（"<" 符号），支持点击返回；同时保留左滑返回手势。
- UI布局：SSID/PWD/按钮/状态按 20px 间距重新排列；键盘显示时隐藏按钮与状态，避免贴合。
- 最终布局：Connect 按钮放大到 140×36 并下移；键盘增大到 118px；标签字体统一为 montserrat_14；状态文本改为英文（Ready/Connecting.../Connected/Failed）。
- 输入框字体：SSID 和 PWD 输入框使用默认字体大小（移除了自定义字体设置，避免字体过大）。
- WiFi 按钮改进：添加 ON（连接）和 OFF（断开）两个并排按钮，ON 按钮为蓝色，OFF 按钮为红色；尺寸均为 100×36，位置分别为 (20,144) 和 (160,144)；实现了 action_wifi_disconnect 断开连接功能。
- WiFi 断开优化增强版：OFF按钮不仅断开连接，还会：
  1. 调用 WifiStation::Stop() 停止WiFi Station
  2. 调用 SsidManager::Clear() 清除NVS中所有保存的WiFi凭证
  3. 清除 ESP-IDF WiFi配置
  4. 完全重置WiFi设置（相当于恢复出厂设置）
- WiFi 连接逻辑修复（解决连接旧WiFi的问题）- 第三版最终优化：
  1. 断开当前WiFi连接（如果已连接）
  2. Stop() 停止WiFi Station（阻止自动重连）
  3. SsidManager::Clear() 清除所有NVS保存的WiFi凭证
  4. esp_wifi_set_config() 清除ESP-IDF底层的WiFi配置
  5. AddAuth() 仅添加新输入的WiFi认证
  6. Start() 启动WiFi Station（队列中只有新WiFi）
  7. 扫描并连接（**30秒超时**，避免过早显示Failed）
  8. 连接后验证SSID是否匹配，记录详细日志便于调试
  
- WiFi 输入验证增强：
  1. SSID验证：非空检查 + 长度检查（1-32字符）
  2. 密码验证：长度检查（0或8-63字符，符合WiFi标准）
  3. 验证失败时显示具体错误信息（"SSID too long", "Password too short"等）
  4. 记录详细日志，便于调试

- WiFi 内存和资源优化：
  1. **任务栈优化**：WiFi连接任务栈从4096减少到2048字节（节省2KB RAM）
  2. **T9定时器泄漏修复**：离开WiFi页面时删除定时器，防止资源泄漏和CPU浪费
  3. **std::string优化**：
     - 使用右值引用（临时对象）传递给AddAuth，支持移动语义
     - 使用const引用避免不必要的复制
     - 减少堆内存分配次数
  4. **缓冲区优化**：状态字符串缓冲区从96字节减少到48字节（节省48字节栈空间）
  5. **代码清理**：移除未使用的变量声明
  6. **总节省**：约2.1KB RAM + 降低堆碎片 + 减少CPU占用

- app3_page界面图标化优化：
  1. **图标资源**：使用用户生成的新`image_game`(55×55)和`img_wifi`(55×55)
  2. **统一尺寸**：两个图标都是55×55，视觉更协调
  3. **极简布局**：
     - 纯黑色背景(#000000)，去掉背景图片
     - 游戏图标：位置(112, 60)，水平居中
     - WiFi图标：位置(112, 155)，水平居中
     - 两图标间距40px，布局平衡
     - **无文字标签**，纯图标交互
  4. **交互优化**：图标可点击，事件使用LV_EVENT_CLICKED
  5. **视觉效果**：极简现代风格，纯黑背景+统一尺寸图标

## Executor Feedback or Request for Help
- 构建问题：启用 LVGL FatFs 后，`ff.h` include 与 FatFs API 可用性存在差异。已将 `lvgl__lvgl` 组件依赖强制加入 `fatfs`，并在 `sd_card.cc` 中移除 `f_chdrive()`，改用 `S:0:/clock/1.bmp` 方式显式指定 FatFs 卷号。

## Executor Feedback or Request for Help
- 将开始修改 UI 相关文件（`screens.h/.c`、`actions.h/action.cc`）以加入 WiFi 配网页面与入口按钮；如需新增 glue 文件会在修改前再次记录。
- IDE lints 仍提示 `machine/endian.h` 缺失与 `std::string` 相关误报，推测为本地 clang 配置/SDK 头路径未对齐；待实际构建验证。
- 已按要求改为 T9 按钮矩阵键盘；WiFi 页面不启用左滑返回，仅保留返回按钮。
- 若键盘仍不弹出，请反馈是否能触发输入框聚焦（可临时加日志/高亮验证）。

## Executor Feedback or Request for Help
- 用户已确认第 1 个文件修改，按“一次一个文件”继续执行第 2 步。
- 2026-01-24：用户在 WSL 远程连接且开梯子时，Cursor 代码索引握手失败。已给出代理/DNS/证书/登录与重启的排查建议。
- 2026-01-24：用户反馈 WSL 检测到 localhost 代理未镜像；`curl -I https://cursor.sh` 成功（HTTP 308 到 cursor.com），说明基本出网 OK，但 WSL 未走 Windows 代理。
- 2026-01-24：已验证 WSL 使用 `192.168.224.1:7890` 代理可访问 `https://cursor.com`，但 Cursor 仍提示 `Handshake failed`，需排查 Cursor Server 环境变量/代理对 WebSocket/HTTP2 支持。
- 2026-01-24：用户在 WSL 远程环境右键无 “Go to Definition”。需要排查索引状态、语言服务器与 C/C++ 编译数据库。

## Lessons Learned
- LVGL FatFs 驱动内部 `fs_init()` 为空，需由应用侧先完成 SD/FatFs 挂载；本项目使用 `esp_vfs_fat_sdmmc_mount()`，并在挂载后再切换 UI 图片可避免时序问题。

