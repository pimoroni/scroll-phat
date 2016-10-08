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
        altcontroller = IS31FL3730(font, altbus)
    except (NameError, IOError):
        pass
else:
    try:
        controller = IS31FL3730(font, altbus)
    except (NameError, IOError):
        exit("Scroll pHAT can't be detected!")
