import smbus
from .font import font
from .IS31FL3730 import IS31FL3730

IS31FL3730_1 = IS31FL3730(smbus, font)
IS31FL3730_1.initialize()
rotate = False

def initialize():
    IS31FL3730_1.initialize()

# The public interface maintains compatibility with previous singleton
# pattern.
def rotate5bits(x):
    IS31FL3730_1.rotate = rotate # Needed on every method for existing interface
    IS31FL3730_1.rotate5bits(x)

def update():
    IS31FL3730_1.rotate = rotate
    IS31FL3730_1.update()

def set_mode(mode):
    IS31FL3730_1.rotate = rotate
    IS31FL3730_1.set_mode(mode)

def set_brightness(brightness):
    IS31FL3730_1.rotate = rotate
    IS31FL3730_1.set_brightness(brightness)

def set_col(x, value):
    IS31FL3730_1.rotate = rotate
    IS31FL3730_1.set_col(x, value)

def write_string( chars, x = 0):
    IS31FL3730_1.rotate = rotate
    IS31FL3730_1.write_string(chars,x)

def graph(values, low=None, high=None):
    IS31FL3730_1.rotate = rotate
    IS31FL3730_1.graph(values, low, high)

# This is breaking encapsulation - could it be dropped?
def buffer_len():
    IS31FL3730_1.rotate = rotate
    return IS31FL3730_1.buffer_len()

def scroll(delta = 1):
    IS31FL3730_1.rotate = rotate
    IS31FL3730_1.scroll(delta)

def clear():
    IS31FL3730_1.rotate = rotate
    IS31FL3730_1.clear()

def load_font(new_font):
    IS31FL3730_1.rotate = rotate
    IS31FL3730_1.load_font(new_font)

def scroll_to(pos = 0):
    IS31FL3730_1.rotate = rotate
    IS31FL3730_1.scroll_to(pos)

def io_errors():
    IS31FL3730_1.rotate = rotate
    return IS31FL3730_1.io_errors()

def set_pixel(x,y,value):
    IS31FL3730_1.rotate = rotate
    IS31FL3730_1.set_pixel(x,y,value)

