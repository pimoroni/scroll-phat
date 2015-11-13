import smbus

I2C_ADDR = 0x60

bus = smbus.SMBus(1)

CMD_SET_MODE = 0x00
CMD_SET_BRIGHTNESS = 0x19
MODE_5X11 = 0b00000011

buffer = [0] * 11

def set_mode(mode=MODE_5X11):
    bus.write_i2c_block_data(I2C_ADDR, CMD_SET_MODE, [MODE_5X11])

def set_brightness(brightness):
    bus.write_i2c_block_data(I2C_ADDR, CMD_SET_BRIGHTNESS, [brightness])

def update(new_buffer=None):
    if new_buffer is not None:
        buffer = new_buffer

    bus.write_i2c_block_data(I2C_ADDR,
        0x01,
        buffer + [0xff])

def set_pixel(x,y,value):
    if value:
        buffer[x] |= (1 << y)
    else:
        buffer[x] &= ~(1 << y)

set_mode()    
