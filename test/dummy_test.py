import unittest

from bibliopixel.led.strip import LEDStrip
from bibliopixel.drivers.dummy_driver import DriverDummy


class DummyTest(unittest.TestCase):
    def test_dummy(self):
        for driver in DriverDummy(32), DriverDummy(32, 0.01):
            led = LEDStrip([driver])
            led.push_to_driver()
