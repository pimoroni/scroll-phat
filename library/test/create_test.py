import unittest
from scrollphat.IS31FL3730 import IS31FL3730

class FakeI2c:
   def __init__(self):
        pass

class CreateTest(unittest.TestCase):
    def test_create_scrollphat_with_fake_i2c(self):
        font= {}
        sut = IS31FL3730(FakeI2c(), font)

        self.assertTrue(sut is not None)

if __name__ == '__main__':
    unittest.main()

