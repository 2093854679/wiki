# 使用外部32K[](#k "永久链接至标题")



## 开启外部32K时钟源方法[](#id1 "永久链接至标题")


- 确保硬件已经焊接了外部32K时钟源

- 在middleware/soc/bk72xx/bk7258.defconfig中设置CONFIG_EXTERN_32K=y

重要

当本地工程应用于其他项目时，为避免定义外部32K影响该工程，请新建工程，将CONFIG_EXTERN_32K定义在根目录下projects的新建工程的config/bk72xx.config中。
