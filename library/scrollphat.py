import smbus
from PIL import Image
import os

I2C_ADDR = 0x60

bus = smbus.SMBus(1)

CMD_SET_MODE = 0x00
CMD_SET_BRIGHTNESS = 0x19
MODE_5X11 = 0b00000011

INVERT = False

# 1  0
# 2  0
# 4  0
# 8  0
# 16 0


font = {}

buffer = [0] * 11
offset = 0

def invert(x):
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

    if INVERT:
        window.reverse()
        for i in range(len(window)):
            window[i] = invert(window[i])

    window.append(0xff)

    try:
        bus.write_i2c_block_data(I2C_ADDR, 0x01, window)
    except IOError:
        print("IO error")

# font image contains a grid of 3 x 32 characters each of which is
# contained in a 6x6 box. The first character is ASCII 0x20 which
# increments down the column
def load_font():
    font_path = os.path.join(os.path.dirname(__file__), "font.png")
    font_image = Image.open(font_path)

    char = 0x20
    for cx in range(0, 3):
        for cy in range(0, 32):
            char_bits = []

            for x in range(0, 5):
                bits = 0
                for y in range(0, 5):
                    if font_image.getpixel(((cx * 6) + x, (cy * 6) + y)) == 0:
                        bits |= (1 << y)

                char_bits.append(bits)

            # remove all "empty" columns from end of character
            while len(char_bits) > 0 and char_bits[-1] == 0:
                char_bits.pop()

            font[char] = char_bits

            char += 1

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

load_font()
set_mode()

