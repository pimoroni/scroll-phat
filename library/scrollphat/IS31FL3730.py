ADDR = 0x60
MODE_5X11 = 0b00000011
ROTATE_OFF = False
ROTATE_180 = True

class I2cConstants:
    def __init__(self):
        self.CMD_SET_MODE = 0x00
        self.CMD_SET_BRIGHTNESS = 0x19
        self.MODE_5X11 = 0b00000011

class IS31FL3730:
    def __init__(self, font, i2c_bus=None, addr=ADDR):
        self.i2cConstants = I2cConstants()

        self.i2c_bus = i2c_bus
        if not hasattr(i2c_bus, "write_i2c_block_data"):
            raise TypeError("Object given for i2c_bus must implement write_i2c_block_data")

        self.addr = addr
        self.font = font
        self._rotate = False
        self.buffer = [0] * 11
        self.offset = 0
        self.error_count = 0
        self.set_mode(self.i2cConstants.MODE_5X11)

    def set_rotate(self, value):
        self._rotate = value

    def rotate5bits(self, x):
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

    def update(self):
        if self.offset + 11 <= len(self.buffer):
            self.window = self.buffer[self.offset:self.offset + 11]
        else:
            self.window = self.buffer[self.offset:]
            self.window += self.buffer[:11 - len(self.window)]

        if self._rotate:
            self.window.reverse()
            for i in range(len(self.window)):
                self.window[i] = self.rotate5bits(self.window[i])

        self.window.append(0xff)

        try:
            self.i2c_bus.write_i2c_block_data(self.addr, 0x01, self.window)
        except IOError:
            self.error_count += 1
            if self.error_count == 10:
                print("A high number of IO Errors have occurred, please check your soldering/connections.")

    def set_mode(self, mode=MODE_5X11):
        self.i2c_bus.write_i2c_block_data(self.addr, self.i2cConstants.CMD_SET_MODE, [self.i2cConstants.MODE_5X11])

    def get_brightness(self):
        if hasattr(self, 'brightness'):
            return self.brightness
        return -1

    def set_brightness(self, brightness):
        self.brightness = brightness
        self.i2c_bus.write_i2c_block_data(self.addr, self.i2cConstants.CMD_SET_BRIGHTNESS, [self.brightness])

    def set_col(self, x, value):
        if len(self.buffer) <= x:
            self.buffer += [0] * (x - len(self.buffer) + 1)

        self.buffer[x] = value

    def write_string(self, chars, x = 0):
        for char in chars:
            if ord(char) == 0x20 or ord(char) not in self.font:
                self.set_col(x, 0)
                x += 1
                self.set_col(x, 0)
                x += 1
                self.set_col(x, 0)
                x += 1
            else:
                font_char = self.font[ord(char)]
                for i in range(0, len(font_char)):
                    self.set_col(x, font_char[i])
                    x += 1

                self.set_col(x, 0)
                x += 1 # space between chars
        self.update()

    # draw a graph across the screen either using
    # the supplied min/max for scaling or auto
    # scaling the output to the min/max values
    # supplied
    def graph(self, values, low=None, high=None):
        values = [float(x) for x in values]

        if low == None:
            low = min(values)

        if high == None:
            high = max(values)

        span = high - low

        for col, value in enumerate(values):
            value -= low
            value /= span
            value *= 5

            if value > 5: value = 5
            if value < 0: value = 0

            self.set_col(col, [0,16,24,28,30,31][int(value)])

        self.update()

    def set_buffer(self, replacement):
        self.buffer = replacement

    def buffer_len(self):
        return len(self.buffer)

    def scroll(self, delta = 1):
        self.offset += delta
        self.offset %= len(self.buffer)
        self.update()

    def clear_buffer(self):
        self.offset = 0
        self.buffer = [0] * 11

    def clear(self):
        self.clear_buffer()
        self.update()

    def load_font(self, new_font):
        self.font = new_font

    def scroll_to(self, pos = 0):
        self.offset = pos
        self.offset %= len(self.buffer)
        self.update()

    def io_errors(self):
        return self.error_count

    def set_pixel(self, x,y,value):
        if value:
            self.buffer[x] |= (1 << y)
        else:
            self.buffer[x] &= ~(1 << y)


    def set_rotate(self, value):
        """Set the rotation of Scroll pHAT
    
        :param value: Rotate 180 degrees: True/False
        """
    
        self.set_rotate(value)
    
    # The public interface maintains compatibility with previous singleton
    # pattern.
    def rotate5bits(self, x):
        self.rotate5bits(x)
    
    def update():
        """Update Scroll pHAT with the current buffer"""
    
        self.update()
    
    def set_buffer(self, buf):
        """Overwrite the buffer
    
        :param buf: One dimensional array of int: 0 to 31 - pixels are 1,2,4,8,16 and 1 is top-most pixel
        """
        self.set_buffer(buf)
    
    def set_brightness(self, brightness):
        """Set the brightness of Scroll pHAT
        
        :param brightness: Brightness value: 0 to 255
        """
        self.set_brightness(brightness)
    
    def set_col(self, x, value):
        """Set a single column in the buffer
    
        :param x: Position of column to set, buffer will auto-expand if necessary
        :param value: Value to set: 0 to 31 - pixels are 1,2,4,8,16 and 1 is top-most pixel
        """
        self.set_col(x, value)
    
    def write_string(self, chars, x = 0):
        """Write a text string to the buffer
    
        :param chars: Text string to write
        :param x: Left offset in pixels
        """
        self.write_string(chars,x)
    
    def graph(self, values, low=None, high=None):
        """Write a bar graph to the buffer
    
        :param values: List of values to display
        :param low: Lowest possible value (default min(values))
        :param high: Highest possible value (default max(values))
        """
        self.graph(values, low, high)
    
    def buffer_len():
        """Returns the length of the internal buffer"""
        return self.buffer_len()
    
    def scroll(self, delta = 1):
        """Scroll the offset
    
        Scroll pHAT displays an 11 column wide window into the buffer,
        which starts at the left offset.
    
        :param delta: Amount to scroll (default 1)
        """
        self.scroll(delta)
    
    def clear_buffer(self):
        """Clear just the buffer, do not update Scroll pHAT"""
        self.clear_buffer()
    
    def clear(self):
        """Clear the buffer, and then update Scroll pHAT"""
        self.clear()
    
    def load_font(self, new_font):
        """Replace the internal font array
    
        The font is a dictionary of lists, keyed on character ordinal.
    
        For example, space ' ' would have the key 32 (ord(' ')).
    
        Each list includes one or more numbers between 0 and 31, these
        numbers specify which pixels in that column will be on.
    
        Each pixel is assigned a bit, either: 1, 2, 4, 8 or 16.
    
        1 is the top-most pixel (nearest the header) and 16 the bottom-most.
    
        A value of 17 would light the top and bottom pixels.
        """
        self.load_font(new_font)
    
    def scroll_to(self, pos = 0):
        """Set the internal offset to a specific position
    
        :param pos: Position to set
        """
        self.scroll_to(pos)
    
    def io_errors():
        """Return the internal count of IO Error events"""
        return self.io_errors()
    
    def set_pixel(self, x,y,value):
        """Turn a specific pixel on or off
    
        :param x: The horizontal position of the pixel
        :param y: The vertical position of the pixel: 0 to 4
        :param value: On/Off state: True/False
        """
        self.set_pixel(x,y,value)
    
    def set_pixels(self, handler, auto_update=False):
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
