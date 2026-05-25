# examples/peripherals 外设子工程 API 速查

本节整理 `projects/examples/peripherals` 目录下所有子工程的主要API及其功能说明，便于快速查阅和开发。

---

## 1. SPI 主机示例（spi_master）
- **编译命令**：
  ```sh
  make bk7236 PROJECT=examples/peripherals/spi/spi_master
  ```
- **主要API及说明**：
  - `bk_spi_driver_init()`：初始化SPI驱动。
  - `bk_spi_init(spi_id, &config)`：初始化指定SPI控制器，配置主/从、时钟、极性等参数。
  - `bk_spi_write_bytes(spi_id, buf, len)`：SPI发送数据（非DMA）。
  - `bk_spi_dma_write_bytes(spi_id, buf, len)`：SPI通过DMA方式发送数据。
  - `bk_spi_read_bytes(spi_id, buf, len)`：SPI接收数据（非DMA）。
  - `bk_spi_dma_read_bytes(spi_id, buf, len)`：SPI通过DMA方式接收数据。
  - `bk_dma_alloc(dev)`：分配DMA通道。

---

## 2. SPI 从机示例（spi_slave）
- **编译命令**：
  ```sh
  make bk7236 PROJECT=examples/peripherals/spi/spi_slave
  ```
- **主要API及说明**：
  - 同上，区别在于 `spi_config_t` 结构体的 `.role` 字段为 `SPI_ROLE_SLAVE`。

---

## 3. PWM 占空比/周期设置（pwm_set_period_duty）
- **编译命令**：
  ```sh
  make bk7236 PROJECT=examples/peripherals/pwm/pwm_set_period_duty
  ```
- **主要API及说明**：
  - `bk_pwm_driver_init()`：初始化PWM驱动。
  - `bk_pwm_init(chan, &config)`：初始化指定PWM通道。
  - `bk_pwm_set_period_duty(chan, period, duty)`：设置PWM周期和占空比。
  - `bk_pwm_start(chan)`：启动PWM输出。
  - `bk_pwm_stop(chan)`：停止PWM输出。

---

## 4. PWM 相位偏移（phase_shift）
- **编译命令**：
  ```sh
  make bk7236 PROJECT=examples/peripherals/pwm/phase_shift
  ```
- **主要API及说明**：
  - 同上，增加了多通道相位配置。

---

## 5. PWM 互补输出（complementary_outputs）
- **编译命令**：
  ```sh
  make bk7236 PROJECT=examples/peripherals/pwm/complementary_outputs
  ```
- **主要API及说明**：
  - `pwm_group_init_without_dead_time()`：初始化无死区互补输出。
  - `pwm_group_init_with_dead_time()`：初始化带死区互补输出。
  - `pwm_group_update_duty(group, duty1, duty2)`：更新互补输出的占空比。

---

## 6. I2C 示例（i2c）
- **编译命令**：
  ```sh
  make bk7236 PROJECT=examples/peripherals/i2c
  ```
- **主要API及说明**：
  - `bk_i2c_driver_init()`：初始化I2C驱动。
  - `bk_i2c_init(i2c_id, &config)`：初始化指定I2C控制器。
  - `bk_i2c_memory_write(i2c_id, &mem_param)`：向I2C设备指定地址写数据。
  - `bk_i2c_memory_read(i2c_id, &mem_param)`：从I2C设备指定地址读数据。

---

## 7. GPIO 示例（gpio）
- **编译命令**：
  ```sh
  make bk7236 PROJECT=examples/peripherals/gpio
  ```
- **主要API及说明**：
  - （当前仅有占位代码，建议参考 `bk_gpio_driver_init()`、`bk_gpio_set_output_high()`、`bk_gpio_set_output_low()` 等API，分别用于初始化、设置高电平、设置低电平。）

---

## 8. DMA 示例（dma）
- **编译命令**：
  ```sh
  make bk7236 PROJECT=examples/peripherals/dma
  ```
- **主要API及说明**：
  - （当前仅有占位代码，建议参考 `bk_dma_driver_init()`、`bk_dma_alloc()`、`bk_dma_start()` 等API，分别用于初始化、分配通道、启动DMA传输。）

---

## 9. ADC 示例（adc）
- **编译命令**：
  ```sh
  make bk7236 PROJECT=examples/peripherals/adc
  ```
- **主要API及说明**：
  - `bk_adc_driver_init()`：初始化ADC驱动。
  - `bk_adc_acquire()`：申请ADC资源。
  - `bk_adc_init(chan)`：初始化指定ADC通道。
  - `bk_adc_start()`：启动ADC采样。
  - `bk_adc_set_config(&config)`：配置ADC参数。
  - `bk_adc_register_isr(cb, buf_size)`：注册ADC采样完成中断回调。
  - `bk_adc_set_channel(chan)`：选择ADC采样通道。
  - `bk_adc_read(&value, timeout)`：读取ADC采样值。
  - `bk_adc_deinit(chan)`：反初始化ADC通道。
  - `bk_adc_release()`：释放ADC资源。

---

> 以上API均为外设驱动常用接口，具体参数和用法请参考对应头文件和官方开发手册。
