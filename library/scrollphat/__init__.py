import smbus
from time import sleep
from .font import font
from .IS31FL3730 import IS31FL3730
from threading import Thread

controller = IS31FL3730(smbus, font)
controller.initialize()
rotate = False
_autoscroll_run = False

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

def write_string(chars, x = 0, scroll=None, repeat=None, delay=None, repeat_delay=None):
    controller.rotate = rotate
    if scroll:
        auto_scroll(chars, repeat=repeat, delay=delay, repeat_delay=repeat_delay)
    else:
        controller.write_string(chars,x)

def auto_scroll(chars, repeat=None, delay=None, repeat_delay=None):
    global _autoscroll_run

    delay = 0.1 if delay is None else delay
    repeat = 1 if repeat is None else repeat
    repeat_delay = delay * 10 if repeat_delay is None else repeat_delay
    
    def _do_scroll(chars, delay, repeat, repeat_delay):
        global _autoscroll_run
        _autoscroll_run = True
        for x in range(repeat):
            clear()
            controller.write_string(chars,11)
            for p in range(buffer_len()):
                if not _autoscroll_run:
                    return
                sleep(delay)
                scroll()
            sleep(repeat_delay)
        clear()
        _autoscroll_run = False

    _autoscroll_run = True
    _t = Thread(target=_do_scroll, args=(chars, delay, repeat, repeat_delay))
    _t.start()

def stop():
    global _autoscroll_run
    _autoscroll_run = False

def busy():
    global _autoscroll_run
    return _autoscroll_run

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

