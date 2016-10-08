from .i2c_bus import bus
try:
    from .i2c_bus import altbus
except ImportError:
    pass

from .font import font
from .IS31FL3730 import IS31FL3730

mainbus = bus

try:
    controller = IS31FL3730(font, bus)
except IOError:
    mainbus = None

if mainbus != None:
    try:
        altscrollphat = IS31FL3730(font, altbus)
    except (NameError, IOError):
        pass
else:
    try:
        controller = IS31FL3730(font, altbus)
    except (NameError, IOError):
        exit("Scroll pHAT can't be detected!")
        

ROTATE_OFF = False
ROTATE_180 = True


def set_rotate(value):
    """Set the rotation of Scroll pHAT

    :param value: Rotate 180 degrees: True/False
    """

    controller.set_rotate(value)

# The public interface maintains compatibility with previous singleton
# pattern.
def rotate5bits(x):
    controller.rotate5bits(x)

def update():
    """Update Scroll pHAT with the current buffer"""

    controller.update()

def set_buffer(buf):
    """Overwrite the buffer

    :param buf: One dimensional array of int: 0 to 31 - pixels are 1,2,4,8,16 and 1 is top-most pixel
    """
    controller.set_buffer(buf)

def set_brightness(brightness):
    """Set the brightness of Scroll pHAT
    
    :param brightness: Brightness value: 0 to 255
    """
    controller.set_brightness(brightness)

def set_col(x, value):
    """Set a single column in the buffer

    :param x: Position of column to set, buffer will auto-expand if necessary
    :param value: Value to set: 0 to 31 - pixels are 1,2,4,8,16 and 1 is top-most pixel
    """
    controller.set_col(x, value)

def write_string( chars, x = 0):
    """Write a text string to the buffer

    :param chars: Text string to write
    :param x: Left offset in pixels
    """
    controller.write_string(chars,x)

def graph(values, low=None, high=None):
    """Write a bar graph to the buffer

    :param values: List of values to display
    :param low: Lowest possible value (default min(values))
    :param high: Highest possible value (default max(values))
    """
    controller.graph(values, low, high)

def buffer_len():
    """Returns the length of the internal buffer"""
    return controller.buffer_len()

def scroll(delta = 1):
    """Scroll the offset

    Scroll pHAT displays an 11 column wide window into the buffer,
    which starts at the left offset.

    :param delta: Amount to scroll (default 1)
    """
    controller.scroll(delta)

def clear_buffer():
    """Clear just the buffer, do not update Scroll pHAT"""
    controller.clear_buffer()

def clear():
    """Clear the buffer, and then update Scroll pHAT"""
    controller.clear()

def load_font(new_font):
    """Replace the internal font array

    The font is a dictionary of lists, keyed on character ordinal.

    For example, space ' ' would have the key 32 (ord(' ')).

    Each list includes one or more numbers between 0 and 31, these
    numbers specify which pixels in that column will be on.

    Each pixel is assigned a bit, either: 1, 2, 4, 8 or 16.

    1 is the top-most pixel (nearest the header) and 16 the bottom-most.

    A value of 17 would light the top and bottom pixels.
    """
    controller.load_font(new_font)

def scroll_to(pos = 0):
    """Set the internal offset to a specific position

    :param pos: Position to set
    """
    controller.scroll_to(pos)

def io_errors():
    """Return the internal count of IO Error events"""
    return controller.io_errors()

def set_pixel(x,y,value):
    """Turn a specific pixel on or off

    :param x: The horizontal position of the pixel
    :param y: The vertical position of the pixel: 0 to 4
    :param value: On/Off state: True/False
    """
    controller.set_pixel(x,y,value)

def set_pixels(handler, auto_update=False):
    """Use a pixel shader function to set 11x5 pixels

    Useful for displaying patterns and animations, or the result of simple functions. For example::

        scrollphat.set_pixels(lambda x, y: (x + y) % 2, True)

    Will display a check pattern.

    :param handler: A function which accepts an x and y position, and returns True or False
    :param auto_update: Whether to update Scroll pHAT after setting all pixels (default False)    
    """
    for x in range(11):
        for y in range(5):
            set_pixel(x, y, handler(x, y))
    if auto_update:
        update()
