https://blog.csdn.net/weixin_44115575/article/details/136713792

![img](./assets/7e41055ef39d50b8136305fd7adc1596.png)

IIC中，**任何时候都是主机（CPU）完全掌控SCL线**，在空闲状态下，主机可以主动发起对SDA线的控制，只有在**从机发送数据（主机发送读取从机命令之后）和从机应答**的时候，主机才会转交SDA的控制权给从机。
