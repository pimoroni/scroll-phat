import unittest
from scrollphat.IS31FL3730 import IS31FL3730, I2cConstants

# Fakes i2c to allow testing off-device
# - May return canned data (stubbing)
# - May record method calls (mocking)
class FakeI2c:
    def __init__(self):
        self.write_i2c_block_data_calls = []
        pass
    def write_i2c_block_data(self,addr,mode,size):
        call = {"addr":addr, "mode":mode, "size": size}
        self.write_i2c_block_data_calls.append(call)

    def get_write_i2c_block_data(self):
        return self.write_i2c_block_data_calls

class DeviceTest(unittest.TestCase):

    def test_set_brightness_after_setting_it(self):
        font= {}
        fakeI2c = FakeI2c()
        sut = IS31FL3730(fakeI2c, font)
        constants = I2cConstants()
        sut.set_brightness(5)
        self.assertEquals(fakeI2c.write_i2c_block_data_calls[0]["size"], [5])
        self.assertEquals(sut.get_brightness(), 5)

    def test_set_brightness_when_it_was_never_set(self):
        font= {}
        fakeI2c = FakeI2c()
        sut = IS31FL3730(fakeI2c, font)
        constants = I2cConstants()
        self.assertEquals(sut.get_brightness(), -1)

    def test_rotate5bits_inrange(self):
        font= {}
        sut = IS31FL3730(FakeI2c(), font)
        self.assertEquals(sut.rotate5bits(1), 16)
        self.assertEquals(sut.rotate5bits(2), 8)
        self.assertEquals(sut.rotate5bits(4), 4)
        self.assertEquals(sut.rotate5bits(8), 2)
        self.assertEquals(sut.rotate5bits(16), 1)

    def test_rotate5bits_outrange_returns_zero(self):
        font= {}
        sut = IS31FL3730(FakeI2c(), font)
        self.assertEquals(sut.rotate5bits(0), 0)
        self.assertEquals(sut.rotate5bits(32), 0)

    def test_create_scrollphat_with_fake_i2c(self):
        font= {}
        sut = IS31FL3730(FakeI2c(), font)
        self.assertTrue(sut is not None)

    def test_set_mode_default(self):
        font= {}
        fakeI2c = FakeI2c()
        sut = IS31FL3730(fakeI2c, font)
        constants = I2cConstants()
        sut.set_mode(constants.MODE_5X11)
        self.assertEquals(fakeI2c.write_i2c_block_data_calls[0]["size"], [constants.MODE_5X11])

if __name__ == '__main__':
    unittest.main()
