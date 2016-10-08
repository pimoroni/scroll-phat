from .font import font

ADDR = 0x60

class I2cConstants:
    def __init__(self):
        self.CMD_SET_MODE = 0x00
        self.CMD_SET_BRIGHTNESS = 0x19
        self.MODE_5X11 = 0b00000011

class IS31FL3730:
    def __init__(self, i2c_bus=None, addr=ADDR, font):
        self.i2cConstants = I2cConstants()

        self.i2c_bus = i2c_bus
        if not hasattr(i2c_bus, "write_i2c_block_data") or not hasattr(i2c_bus, "read_i2c_block_data"):
            raise TypeError("Object given for i2c_bus must implement write_i2c_block_data and read_i2c_block_data")

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
