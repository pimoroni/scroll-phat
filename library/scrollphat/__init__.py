import smbus
from .font import font

I2C_ADDR = 0x60

bus = smbus.SMBus(1)

CMD_SET_MODE = 0x00
CMD_SET_BRIGHTNESS = 0x19
MODE_5X11 = 0b00000011

buffer = [0] * 11
offset = 0
rotate = False

def rotate5bits(x):
    r = 0
    if x & 16:
        r = r | 1
    if x & 8:
        r = r | 2
    if x & 4:
        r = r | 4
    if x & 2:
        r = r | 8
    if x & 1:
        r = r | 16
    return r

def update():
    global buffer, offset

    if offset + 11 <= len(buffer):
        window = buffer[offset:offset + 11]
    else:
        window = buffer[offset:]
        window += buffer[:11 - len(window)]

    if rotate:
        window.reverse()
        for i in range(len(window)):
            window[i] = rotate5bits(window[i])

    window.append(0xff)

    try:
        bus.write_i2c_block_data(I2C_ADDR, 0x01, window)
    except IOError:
        print("IO error")

def set_mode(mode=MODE_5X11):
    bus.write_i2c_block_data(I2C_ADDR, CMD_SET_MODE, [MODE_5X11])

def set_brightness(brightness):
    bus.write_i2c_block_data(I2C_ADDR, CMD_SET_BRIGHTNESS, [brightness])

def set_col(x, value):
    global buffer

    if len(buffer) <= x:
        buffer += [0] * (x - len(buffer) + 1)

    buffer[x] = value

def write_string(chars, x = 0):
    for char in chars:
        if ord(char) == 0x20 or ord(char) not in font:
            set_col(x, 0)
            x += 1
            set_col(x, 0)
            x += 1
            set_col(x, 0)
            x += 1
        else:
            font_char = font[ord(char)]
            for i in range(0, len(font_char)):
                set_col(x, font_char[i])
                x += 1

            set_col(x, 0)
            x += 1 # space between chars

    update()

# draw a graph across the screen either using
# the supplied min/max for scaling or auto
# scaling the output to the min/max values
# supplied
def graph(values, low=None, high=None):
    if low == None:
        low = min(values)

    if high == None:
        high = max(values)

    span = high - low

    col = 0
    for value in values:
        value -= low
        value /= span
        value *= 5
        value = int(value)

        bits = 0
        if value > 1:
            bits |= 0b10000
        if value > 2:
            bits |= 0b11000
        if value > 3:
            bits |= 0b11100
        if value > 4:
            bits |= 0b11111
        if value > 5:
            bits |= 0b11111
        set_col(col, bits)
        col += 1

    update()

def buffer_len():
    global buffer
    return len(buffer)

def scroll(delta = 1):
    global offset
    offset += delta
    offset %= len(buffer)
    update()

def clear():
    global buffer, offset
    offset = 0
    buffer = [0] * 11
    update()

def scroll_to(pos = 0):
    global offset
    offset = pos
    offset %= len(buffer)
    update()

def set_pixel(x,y,value):
    if value:
        buffer[x] |= (1 << y)
    else:
        buffer[x] &= ~(1 << y)

set_mode()
