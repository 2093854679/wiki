# SOFTAP配网开发

## 任务目标
- 实现SOFTAP配网，流程与BLE配网类似。

## 参考例程
- projects/wifi/ap
- projects/wifi/softap
- projects/bluetooth/provisioning

## 开发计划
- [ ] 方案设计与流程图
- [ ] SoftAP启动与手机连接
- [ ] 配网信息接收（HTTP/Socket）
- [ ] 切换STA联网
- [ ] 联网结果反馈

## 问题记录
-

## 代码区
```c
// 代码片段可在此补充
```

---

## SOFTAP配网 C代码模板（BK7236 SDK标准API版）

```c
#include "modules/wifi.h"
#include "os/os.h"
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// 全局变量
static char received_ssid[64] = {0};
static char received_password[64] = {0};
static volatile bool received_wifi_info = false;

// HTTP回调：接收手机端下发的WiFi信息
void on_receive_wifi_info(const char* ssid, const char* password) {
    strncpy(received_ssid, ssid, sizeof(received_ssid) - 1);
    strncpy(received_password, password, sizeof(received_password) - 1);
    received_wifi_info = true;
    printf("收到配网信息: ssid=%s, pwd=%s\n", received_ssid, received_password);
    // 可回复手机“收到配网信息”
    // http_server_send_response("OK"); // 需结合实际HTTP服务器实现
}

// 启动SoftAP
void start_softap(const char* ssid, const char* password, int channel) {
    wifi_ap_config_t ap_config = WIFI_DEFAULT_AP_CONFIG();
    strcpy(ap_config.ssid, ssid);
    strcpy(ap_config.password, password);
    ap_config.channel = channel;
    bk_wifi_ap_set_config(&ap_config);
    bk_wifi_ap_start();
    printf("SoftAP已启动，SSID: %s, 密码: %s\n", ssid, password);
}

// 停止SoftAP
void stop_softap(void) {
    bk_wifi_ap_stop();
    printf("SoftAP已停止\n");
}

// 连接STA
void connect_sta(const char* ssid, const char* password) {
    wifi_sta_config_t sta_config = WIFI_DEFAULT_STA_CONFIG();
    strcpy(sta_config.ssid, ssid);
    strcpy(sta_config.password, password);
    bk_wifi_sta_set_config(&sta_config);
    bk_wifi_sta_connect();
    printf("STA开始连接路由器: %s\n", ssid);
}

// 查询STA连接状态
bool is_sta_connected(void) {
    wifi_link_status_t link_status = {0};
    bk_wifi_sta_get_link_status(&link_status);
    return (link_status.state == WIFI_LINK_CONNECTED);
}

// 主流程
void softap_provision_main(void) {
    // 1. 启动SoftAP模式
    start_softap("Device_XXXX", "12345678", 6);
    printf("等待手机连接到设备热点...\n");

    // 2. 启动HTTP服务器（需结合实际SDK或lwIP httpd实现）
    // http_server_init(80, on_receive_wifi_info);

    // 3. 等待配网信息
    while (!received_wifi_info) {
        rtos_delay_milliseconds(100);
        // 可加超时处理
    }

    // 4. 关闭SoftAP，切换为STA模式
    stop_softap();
    connect_sta(received_ssid, received_password);
    printf("尝试连接用户路由器...\n");

    // 5. 检查联网结果
    int retry = 50; // 最多等待5秒
    while (retry-- > 0) {
        if (is_sta_connected()) {
            printf("联网成功，通知手机/用户\n");
            // 可通过HTTP或其他方式通知手机
            break;
        }
        rtos_delay_milliseconds(100);
    }
    if (retry <= 0) {
        printf("联网失败，重新进入配网流程\n");
        // 可重启流程或提示用户
    }
}

// main入口
int main(void) {
    softap_provision_main();
    while (1) {
        // 其他任务
    }
    return 0;
}
```

---

### 说明
- SoftAP相关API：`bk_wifi_ap_set_config`、`bk_wifi_ap_start`、`bk_wifi_ap_stop`
- STA相关API：`bk_wifi_sta_set_config`、`bk_wifi_sta_connect`、`bk_wifi_sta_disconnect`、`bk_wifi_sta_get_link_status`
- 延时函数：`rtos_delay_milliseconds`
- HTTP服务器部分需结合实际SDK或lwIP httpd实现，回调函数`on_receive_wifi_info`负责接收配网信息
- 代码结构清晰，便于直接开发和扩展

如需HTTP服务器、网页表单等具体实现细节，请告知！

---

## HTTP服务器与网页表单实现细节

### 1. HTTP服务器实现（lwIP httpd为例）

BK7236 SDK通常集成了lwIP协议栈，推荐使用lwIP自带的httpd模块实现嵌入式HTTP服务器。

#### 1.1 启用lwIP httpd
- 确认SDK配置已启用lwIP和httpd（通常在menuconfig或Kconfig中）。
- 工程中包含`lwip/apps/httpd.h`。

#### 1.2 注册POST/CGI回调

```c
#include "lwip/apps/httpd.h"

// 假设网页表单POST到 /provision
err_t httpd_post_begin(void *connection, const char *uri, const char *http_request,
                       u16_t http_request_len, int content_len, char *response_uri,
                       u16_t response_uri_len, u8_t *post_auto_wnd) {
    if (strcmp(uri, "/provision") == 0) {
        // 初始化接收缓冲区
        // ...
        return ERR_OK;
    }
    return ERR_VAL;
}

err_t httpd_post_receive_data(void *connection, struct pbuf *p) {
    // 解析pbuf中的数据，提取ssid和password
    // 假设数据格式为"ssid=xxx&password=yyy"
    char *data = (char *)p->payload;
    char ssid[64] = {0}, password[64] = {0};
    sscanf(data, "ssid=%63[^&]&password=%63s", ssid, password);
    on_receive_wifi_info(ssid, password);
    return ERR_OK;
}

void httpd_post_finished(void *connection, char *response_uri, u16_t response_uri_len) {
    // 可重定向到结果页面
    strncpy(response_uri, "/result.html", response_uri_len);
}
```

- 具体API和回调注册方式请参考`lwip/apps/httpd.h`和SDK文档。
- 你也可以用CGI方式处理GET/POST参数，见`httpd_cgi_handler`。

---

### 2. 网页表单示例

将此HTML文件放入设备的httpd文件系统（如fsdata.c），或用动态页面生成。

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>SOFTAP配网</title>
</head>
<body>
    <h2>WiFi配网</h2>
    <form action="/provision" method="post">
        SSID: <input type="text" name="ssid"><br>
        密码: <input type="password" name="password"><br>
        <input type="submit" value="提交">
    </form>
</body>
</html>
```

- 用户连接设备热点后，访问如`http://192.168.10.1/`即可看到此页面。
- 提交后，表单数据会POST到`/provision`，由上面的C代码回调处理。

---

### 3. 关键点说明

- **安全性**：建议对表单输入做长度和字符校验，防止缓冲区溢出。
- **用户体验**：可在网页上增加联网结果提示（如“连接成功/失败”）。
- **多平台适配**：如用第三方HTTP库（如mongoose、microhttpd等），思路类似，回调函数参数略有不同。

---

### 4. 参考资料
- [lwIP httpd官方文档](https://www.nongnu.org/lwip/2_1_x/group__httpd.html)
- BK7236 SDK自带的HTTP/SoftAP例程（如有）

---

## SOFTAP网页配网原理与常见问题

### 1. SoftAP网页配网整体流程
1. 设备启动SoftAP（热点），如SSID为“MySoftAP”，分配本地IP（如192.168.4.1）。
2. 设备启动lwIP httpd服务器，监听80端口，提供网页服务。
3. 手机连接设备热点，在浏览器输入 http://192.168.4.1 访问网页。
4. 用户填写WiFi信息并提交，设备端通过CGI/POST等方式接收并处理。
5. 设备收到信息后，关闭SoftAP，切换到STA模式连接目标WiFi。

### 2. lwIP httpd服务器简介与集成方法
- lwIP httpd是轻量级嵌入式HTTP服务器，适合MCU/SoC等资源受限平台。
- 只需调用`httpd_init()`即可启动服务器，网页资源可嵌入固件或存储在文件系统中。
- 支持静态网页、表单、CGI（动态网页）、SSI（服务器端包含）。
- 典型API：`httpd_init()`（初始化HTTP服务器），`http_set_cgi_handlers()`（注册CGI处理函数），`http_set_ssi_handler()`（注册SSI处理函数）。
- 你项目中代码路径：components/lwip_intf_v2_1/lwip-2.1.2/src/apps/http/httpd.c

#### 集成步骤简述：
1. 启动SoftAP（见主流程代码）。
2. 初始化lwIP（通常SDK已完成）。
3. 调用`httpd_init()`启动HTTP服务器。
4. 用makefsdata工具将网页转为C数组，或用文件系统存储网页。
5. 实现POST/CGI回调，解析表单数据，处理配网。
6. 配网成功后切换到STA模式。

### 3. 手机访问步骤
1. 手机连接设备热点（如“MySoftAP”）。
2. 在浏览器输入 http://192.168.4.1 访问网页。
3. 填写WiFi信息并提交，设备端即可收到表单数据。

### 4. 为什么用HTTP服务器最简单
- 手机/电脑自带浏览器即可访问，无需额外App。
- HTML表单交互直观易用，开发和调试方便。
- lwIP httpd等轻量级HTTP服务器资源消耗低，适合嵌入式。
- 其它如FTP、MQTT、Socket等方案不适合网页配网场景。

### 5. 常见问题与建议
- **网页打不开？** 检查手机是否连上设备热点，设备IP和httpd是否启动。
- **网页显示不完整？** 检查网页资源是否正确嵌入或烧录。
- **安全性？** 建议SoftAP设置密码，网页输入做校验。
- **网页资源如何嵌入？** 推荐用makefsdata工具将网页转为C数组，或用LittleFS等文件系统。
- **如何调试？** 用串口打印调试配网流程，或在网页中增加调试信息。

---

如需网页配网完整代码模板、网页资源嵌入方法、表单数据解析等详细指导，请随时联系AI助手！
