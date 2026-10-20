---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_mesh/app/zh_CN/latest/q_and_a/index.html
sdk_family: bk_toolkit
chip: ''
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="q-a"></a>

# Q\&A

<a id="id1"></a>

## 串口报错

> 串口未连接、USB HUB供电能力不足均会导致该错误。请从以下几方面排查问题:
>
> 1. 请确保电脑正常识别了串口
> 2. 其它串口工具未打开该串口
> 3. USB HUB供电正常

```
2024-12-17 15:20:31,926 ERROR   # connect serial COM33 fail.
2024-12-17 15:20:31,926 ERROR   # Traceback (most recent call last):
File "utils\serial_utils.py", line 37, in connect
File "serial\serialwin32.py", line 31, in __init__
File "serial\serialutil.py", line 240, in __init__
File "serial\serialwin32.py", line 62, in open
serial.serialutil.SerialException: could not open port 'COM33': FileNotFoundError(2, '系统找不到指定的文件。', None, 2)
```

```
serial.serialutil.SerialException: WriteFile failed (PermissionError(13, '拒绝访问。', None, 5))
```

## 模块导航

- [1. 简介](summary.md)
- [2. 下载安装](download.md)
- [3. 硬件准备](device_prepare.md)
- [4. 新建群组](new_group.md)
- [5. 群组控制](group_control.md)
- [6. 群组拓扑](group_topology.md)
- [7. ota](ota.md)
