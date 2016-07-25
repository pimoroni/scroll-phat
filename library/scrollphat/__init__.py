try:
    import smbus
except ImportError:
    if sys.version_info[0] < 3:
        exit("This library requires python-smbus\nInstall with: sudo apt-get install python-smbus")
    elif sys.version_info[0] == 3:
        exit("This library requires python3-smbus\nInstall with: sudo apt-get install python3-smbus")

from .font import font
from .IS31FL3730 import IS31FL3730, I2cConstants


ROTATE_OFF = False
ROTATE_180 = True

controller = IS31FL3730(smbus, font)

def set_rotate(value):
    controller.set_rotate(value)

def initialize():
    controller.initialize()

# The public interface maintains compatibility with previous singleton
# pattern.
def rotate5bits(x):
    controller.rotate5bits(x)

def update():
    controller.update()

def set_buffer(buf):
    controller.set_buffer(buf)

def set_mode(mode):
    controller.set_mode(mode)

def set_brightness(brightness):
    controller.set_brightness(brightness)

def set_col(x, value):
    controller.set_col(x, value)

def write_string( chars, x = 0):
    controller.write_string(chars,x)

def graph(values, low=None, high=None):
    controller.graph(values, low, high)

# This is breaking encapsulation - could it be dropped?
def buffer_len():
    return controller.buffer_len()

def scroll(delta = 1):
    controller.scroll(delta)

def clear_buffer():
    controller.clear_buffer()

def clear():
    controller.clear()

def load_font(new_font):
    controller.load_font(new_font)

def scroll_to(pos = 0):
    controller.scroll_to(pos)

def io_errors():
    return controller.io_errors()

def set_pixel(x,y,value):
    controller.set_pixel(x,y,value)

def set_pixels(handler, auto_update=False):
    for x in range(11):
        for y in range(5):
            set_pixel(x, y, handler(x, y))
    if auto_update:
        update()
