import smbus
from .font import font
from controller import controller

controller1 = controller(smbus, font)
controller1.initialize()
rotate = False

def initialize():
    controller1.initialize()

# The public interface maintains compatibility with previous singleton
# pattern.
def rotate5bits(x):
    controller1.rotate = rotate # Needed on every method for existing interface
    controller1.rotate5bits(x)
def update():
    controller1.rotate = rotate
    controller1.update()
def set_mode(mode):
    controller1.rotate = rotate
    controller1.set_mode(mode)
def set_brightness(brightness):
    controller1.rotate = rotate
    controller1.set_brightness(brightness)
def set_col(x, value):
    controller1.rotate = rotate
    controller1.set_col(x, value)
def write_string( chars, x = 0):
    controller1.rotate = rotate
    controller1.write_string(chars,x)
def graph(values, low=None, high=None):
    controller1.rotate = rotate
    controller1.graph(values, low, high)
def buffer_len():
    controller1.rotate = rotate
    controller1.buffer_len()
def scroll(delta = 1):
    controller1.rotate = rotate
    controller1.scroll(delta)
def clear():
    controller1.rotate = rotate
    controller1.clear()
def load_font(new_font):
    controller1.rotate = rotate
    controller1.load_font(new_font)
def scroll_to(pos = 0):
    controller1.rotate = rotate
    controller1.scroll_to(pos)
def io_errors():
    controller1.rotate = rotate
    controller1.io_errors()
def set_pixel(x,y,value):
    controller1.rotate = rotate
    controller1.set_pixel(x,y,value)
