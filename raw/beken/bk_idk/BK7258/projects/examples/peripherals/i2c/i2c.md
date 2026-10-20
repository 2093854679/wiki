---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v2.0.1/projects/examples/peripherals/i2c/i2c.html
sdk_family: bk_idk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

**Support Board: BK7236**

<a id="i2c"></a>

# I2c

<a id="project-overview"></a>

## Project Overview

This project is used to demonstrate the functions of the peripheral module i2c

<a id="hardware-requirements"></a>

## Hardware Requirements

BK7236 development board

<a id="configure-and-build"></a>

## Configure and Build

<a id="configure"></a>

### Configure

<a id="build"></a>

### Build

Execute the following command in the Armino root directory to compile:make bk7236

<a id="connect-uart"></a>

### Connect UART

Uart0 is used for Logging and CLI

<a id="flash"></a>

### Flash

Burn all-app.bin to the board using BKFIL.

<a id="running-and-output"></a>

## Running and Output

i2c0 communication as follows:

> - The BK7236 development board is used as the master device, and the eeprom is used as the slave device
> - The clock interface swclk of BK7236 i2c module is connected with the clock interface sclk\_e2 of eeprom i2c module
> - The data interface swdio of BK7236 i2c module is connected with the data interface sdio\_e2 of eeprom i2c module
> - Block block BK7236 development board and eeprom, total eeprom external voltage of 3.3v
> - The SWCLK BK7236 and swdio on 2k resistors, respectively

The cmd example of i2c0 as follows:

> - i2c\_driver init
> - i2c 0 init
> - i2c 0 memory\_write 10 0x50
> - i2c 0 memory\_read 10

i2c1 communication as follows:

> - The BK7236 development board is used as the master device, and the eeprom is used as the slave device
> - The clock interface TXD of BK7236 i2c module is connected with the clock interface sclk\_e2 of eeprom i2c module
> - The data interface RXD of BK7236 i2c module is connected with the data interface sdio\_e2 of eeprom i2c module
> - Block block BK7236 development board and eeprom, total eeprom external voltage of 3.3v

The cmd example of i2c1 as follows:

> - i2c\_driver init
> - i2c 1 init
> - i2c 1 memory\_write 10 0x50
> - i2c 1 memory\_read 10

<a id="case-1-of-i2c0"></a>

### Case 1 of i2c0

<a id="operate"></a>

### Operate

Execute cmd init i2c\_driver and observe the process

<a id="output"></a>

### Output

```
[SYNC]:i2c driver init
```

<a id="case-2-of-i2c0"></a>

### Case 2 of i2c0

<a id="id1"></a>

### Operate

Execute cmd init i2c and observe the process

<a id="id2"></a>

### Output

```
[SYNC]:I2C(0) init ok, baud_rate:400000
[SYNC]:I2C(0) init
```

<a id="case-3-of-i2c0"></a>

### Case 3 of i2c0

<a id="id3"></a>

### Operate

Execute cmd i2c 0 memory\_write 10 0x50 and observe the process

<a id="id4"></a>

### Output

```
[SYNC]:memory_write buf_len:10
```

<a id="case-4-of-i2c0"></a>

### Case 4 of i2c0

<a id="id5"></a>

### Operate

Execute cmd i2c 0 memory\_read 10 and observe the process

<a id="id6"></a>

### Output

```
[SYNC]:i2c_read_buf[0]=0
[SYNC]:i2c_read_buf[1]=1
[SYNC]:i2c_read_buf[2]=2
[SYNC]:i2c_read_buf[3]=3
[SYNC]:i2c_read_buf[4]=4
[SYNC]:i2c_read_buf[5]=5
[SYNC]:i2c_read_buf[6]=6
[SYNC]:i2c_read_buf[7]=7
[SYNC]:i2c_read_buf[8]=8
[SYNC]:i2c_read_buf[9]=9
[SYNC]:i2c(0) memory_read buf_len:10
```

<a id="case-5-of-i2c1"></a>

### Case 5 of i2c1

<a id="id7"></a>

### Operate

Execute cmd init i2c\_driver and observe the process

<a id="id8"></a>

### Output

```
[SYNC]:i2c driver init
```

<a id="case-6-of-i2c1"></a>

### Case 6 of i2c1

<a id="id9"></a>

### Operate

Execute cmd init i2c and observe the process

<a id="id10"></a>

### Output

```
[SYNC]:I2C(1) init ok, baud_rate:400000
[SYNC]:I2C(1) init
```

<a id="case-7-of-i2c1"></a>

### Case 7 of i2c1

<a id="id11"></a>

### Operate

Execute cmd i2c 1 memory\_write 10 0x50 and observe the process

<a id="id12"></a>

### Output

```
[SYNC]:memory_write buf_len:10
```

<a id="case-8-of-i2c1"></a>

### Case 8 of i2c1

<a id="id13"></a>

### Operate

Execute cmd i2c 1 memory\_read 10 and observe the process

<a id="id14"></a>

### Output

```
[SYNC]:i2c_read_buf[0]=0
[SYNC]:i2c_read_buf[1]=1
[SYNC]:i2c_read_buf[2]=2
[SYNC]:i2c_read_buf[3]=3
[SYNC]:i2c_read_buf[4]=4
[SYNC]:i2c_read_buf[5]=5
[SYNC]:i2c_read_buf[6]=6
[SYNC]:i2c_read_buf[7]=7
[SYNC]:i2c_read_buf[8]=8
[SYNC]:i2c_read_buf[9]=9
[SYNC]:i2c(1) memory_read buf_len:10
```
