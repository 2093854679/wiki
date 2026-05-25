# WIFI DTIM10 TCP保活开发

## 任务目标
- WIFI连接指定路由器后进入dtim10低压保活模式，连接一个TCP SERVER并定时60s发送一个TCP心跳包，支持server唤醒命令。

## 参考例程
- projects/wifi/sta_connect
- projects/wifi/iperf

## 开发计划
- [ ] 方案设计与流程图
- [ ] DTIM10省电模式配置
- [ ] TCP长连接与心跳包实现
- [ ] server唤醒命令支持

## 问题记录
-

## 代码区
```c
// 代码片段可在此补充
```

---

## DTIM10省电与TCP保活实现细节

### 1. DTIM10省电模式配置

BK7236 SDK支持WiFi省电（DTIM）模式，可通过相关API设置DTIM间隔。

```c
#include "modules/wifi.h"

// 设置DTIM间隔为10
bk_wifi_sta_set_dtim(10);
```

---

### 2. TCP长连接与心跳包实现

```c
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <string.h>

#define SERVER_IP   "192.168.1.100"
#define SERVER_PORT 9000

void tcp_keepalive_task(void *param) {
    int sockfd;
    struct sockaddr_in server_addr;
    char heartbeat[] = "HEARTBEAT";

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(SERVER_PORT);
    server_addr.sin_addr.s_addr = inet_addr(SERVER_IP);
    connect(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr));

    while (1) {
        send(sockfd, heartbeat, strlen(heartbeat), 0);
        rtos_delay_milliseconds(60000); // 60秒心跳
        // 可在此处接收server唤醒命令
    }
    close(sockfd);
}
```

---

### 3. Server唤醒命令支持
- 在心跳循环中可用`recv()`接收server下发的唤醒命令，根据命令内容唤醒设备或执行特定操作。

---

### 4. 关键点说明
- **省电与实时性权衡**：DTIM间隔越大，功耗越低，但响应延迟增加。
- **心跳包内容**：可自定义心跳包格式，建议带设备ID等信息。
- **异常处理**：需处理TCP断线重连、网络异常等情况。

---

### 5. 参考资料
- [lwIP socket官方文档](https://www.nongnu.org/lwip/2_1_x/group__socket.html)
- BK7236 SDK省电与TCP例程（如有）
