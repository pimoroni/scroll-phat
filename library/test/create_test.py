import unittest
from scrollphat.controller import controller

class FakeI2c:
   def __init__(self):
        pass

class CreateTest(unittest.TestCase):
    def test_create_scrollphat_with_fake_i2c(self):
        font= {}
        controller1 = controller(FakeI2c(), font)
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

