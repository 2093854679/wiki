|  |  |
| --- | --- |
| Supported Targets | **BK7236** |


# SPI_MASTER[](#spi-master "永久链接至标题")


## Overview[](#overview "永久链接至标题")

This project is used for demonstrating [SPI User Guide](https://docs.bekencorp.com/armino/bk7236/en/latest/developer-guide/peripheral/bk_spi.html "https://docs.bekencorp.com/armino/bk7236/en/latest/developer-guide/peripheral/bk_spi.html") .


**The SPI function of BK7236 is still under development and improvement, please note the following restrictions**

> - This project only supports running on 8M FLASH.


## Hardware Requirements[](#hardware-requirements "永久链接至标题")


- BK7236 development board with 8MB FLASH and 40MHz crystal.(e.g., [BK7236_V1 QFN80_8X8 2022.10.18](https://docs.bekencorp.com/armino/bk7236/en/latest/get-started/bk7236.html "https://docs.bekencorp.com/armino/bk7236/en/latest/get-started/bk7236.html")).

- BK7236 download firmware with uart board, such as BEKEN 20221108 UART_V8.

备注

How to download firmware please reference this doc [Burn Code](https://docs.bekencorp.com/armino/bk7236/en/latest/get-started/index.html#hurn-code "https://docs.bekencorp.com/armino/bk7236/en/latest/get-started/index.html#hurn-code")


- BK7236 SPI project need 2 boards at least, and all of them need to support SPI function.And they connection is shown as Figure **SPI Connection** below.

![SPI Connection](../../../../../_images/spi_connection.png)


**SPI Connection**[](#id1 "永久链接至图片")

备注

SPI project should be consist of only one SPI_mater device and one SPI_slave at least.If the SPI system just consist of two devices, so they must be one master and one slave.


## Software Requirements[](#software-requirements "永久链接至标题")


- [Armino SDK](https://github.com/bekencorp/armino "https://github.com/bekencorp/armino").

备注

You can clone Armino SDK by referring to this doc [Armino SDK Code download](https://docs.bekencorp.com/armino/bk7236/en/latest/get-started/index.html#armino-sdk-code-download "https://docs.bekencorp.com/armino/bk7236/en/latest/get-started/index.html#armino-sdk-code-download") step by step.


## Configure and Build[](#configure-and-build "永久链接至标题")


### Configure[](#configure "永久链接至标题")

The SPI master device should be configured as follows:

> - SPI ID
> - SPI_BAUD_RATE
> - SPI_BUF_LEN
> - SPI_TX_TIMEOUT
> - SPI_RX_TIMEOUT
> - UART_ID
> - SPI_ROLE
> - SPI_BIT_WIDTH
> - SPI_POLARITY_MODE
> - SPI_PHASE_MODE
> - SPI_WIRE_MODE
> - SPI_BIT_ORDER_MODE
> - DMA_MODE

备注

The configuration of SPI master device is almost the same as that configuration of SPI slave device.The only difference is the configuration of **SPI_ROLE** which will be **SPI_master_role** or **SPI_slave_role**.


### Build[](#build "永久链接至标题")

Enter the following command in Armino root directory to compile:

`make bk7236 PROJECT=examples/peripherals/spi/spi_master`

For preparation such as toolchain installation, please refer to [Quick Start](https://docs.bekencorp.com/armino/bk7236/en/latest/get-started/index.html "https://docs.bekencorp.com/armino/bk7236/en/latest/get-started/index.html").


### Connect UART[](#connect-uart "永久链接至标题")

UART0 is used for:

> - BKFIL to download images
> - Logging and CLI


### FLASH *all-app.bin*[](#flash-all-app-bin "永久链接至标题")

Burn *Armino/build/spi_master/bk7236/app-app.bin* to the board using BKFIL.


## Running and Output[](#running-and-output "永久链接至标题")


### Case 1 - SPI_master Send data[](#case-1-spi-master-send-data "永久链接至标题")


#### SPI_master_device Send Operation[](#spi-master-device-send-operation "永久链接至标题")


**Case 1.1** edit the function of main() in *spi_master_main.c*, and you will send 0~1023 to SPI_slave_device.


```
 1int main(void)
 2{
 3     BK_LOG_ON_ERR(bk_spi_driver_init());
 4     BK_LOG_ON_ERR(spi_example_send_data());
 5  // BK_LOG_ON_ERR(spi_example_dma_send_data());
 6  // BK_LOG_ON_ERR(spi_example_recv_data());
 7  // BK_LOG_ON_ERR(spi_example_dma_recv_data());
 8
 9     return 0;
10}

```


**Case 1.2** edit the function of main() in *spi_master_main.c*, and you will send 0~1023 to SPI_slave_device through DMA which write data to SPI regesiter.


```
 1int main(void)
 2{
 3     BK_LOG_ON_ERR(bk_spi_driver_init());
 4  // BK_LOG_ON_ERR(spi_example_send_data());
 5     BK_LOG_ON_ERR(spi_example_dma_send_data());
 6  // BK_LOG_ON_ERR(spi_example_recv_data());
 7  // BK_LOG_ON_ERR(spi_example_dma_recv_data());
 8
 9     return 0;
10}

```


### Case 2 - SPI_master Receive data[](#case-2-spi-master-receive-data "永久链接至标题")


#### SPI_master_device Receive Operation[](#spi-master-device-receive-operation "永久链接至标题")


**Case 2.1** edit the function of main() in *spi_master_main.c*, and you will receive data from SPI_slave_device.


```
 1int main(void)
 2{
 3     BK_LOG_ON_ERR(bk_spi_driver_init());
 4  // BK_LOG_ON_ERR(spi_example_send_data());
 5  // BK_LOG_ON_ERR(spi_example_dma_send_data());
 6     BK_LOG_ON_ERR(spi_example_recv_data());
 7  // BK_LOG_ON_ERR(spi_example_dma_recv_data());
 8
 9     return 0;
10}

```


**Case 2.2** edit the function of main() in *spi_master_main.c*, and you will receive data from SPI_slave_device through DMA which read data from SPI regesiter.


```
 1int main(void)
 2{
 3     BK_LOG_ON_ERR(bk_spi_driver_init());
 4  // BK_LOG_ON_ERR(spi_example_send_data());
 5  // BK_LOG_ON_ERR(spi_example_dma_send_data());
 6  // BK_LOG_ON_ERR(spi_example_recv_data());
 7     BK_LOG_ON_ERR(spi_example_dma_recv_data());
 8
 9     return 0;
10}

```
