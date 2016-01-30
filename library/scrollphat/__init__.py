import smbus
from .font import font
from .IS31FL3730 import IS31FL3730

controller = IS31FL3730(smbus, font)
controller.initialize()
rotate = False

def initialize():
    controller.initialize()

# The public interface maintains compatibility with previous singleton
# pattern.
def rotate5bits(x):
    controller.rotate = rotate # Needed on every method for existing interface
    controller.rotate5bits(x)

def update():
    controller.rotate = rotate
    controller.update()

def set_buffer(buffer):
    controller.rotate = rotate
    controller.set_buffer(buffer)

def set_mode(mode):
    controller.rotate = rotate
    controller.set_mode(mode)

def set_brightness(brightness):
    controller.rotate = rotate
    controller.set_brightness(brightness)

def set_col(x, value):
    controller.rotate = rotate
    controller.set_col(x, value)

def write_string( chars, x = 0):
    controller.rotate = rotate
    controller.write_string(chars,x)

def graph(values, low=None, high=None):
    controller.rotate = rotate
    controller.graph(values, low, high)

# This is breaking encapsulation - could it be dropped?
def buffer_len():
    controller.rotate = rotate
    return controller.buffer_len()

def scroll(delta = 1):
    controller.rotate = rotate
    controller.scroll(delta)

def clear():
    controller.rotate = rotate
    controller.clear()

def load_font(new_font):
    controller.rotate = rotate
    controller.load_font(new_font)

def scroll_to(pos = 0):
    controller.rotate = rotate
    controller.scroll_to(pos)

def io_errors():
    controller.rotate = rotate
    return controller.io_errors()

def set_pixel(x,y,value):
    controller.rotate = rotate
    controller.set_pixel(x,y,value)

