import unittest
import time
from ..core.shared.currentLocation.CurrentLocation import CurrentLocation as cl


class TestCurrentLocation(unittest.TestCase):

    def test_init(self):
        result = cl()
        expected = cl
        self.assertIsInstance(result, expected,
                              "Error in CurrentLocation.__init__()")

    def test_get_location(self):
        result = cl().get_location()
        t = time.localtime()
        current_time = time.strftime("%H", t)
        expected = ""
        if (int(current_time) > 7 or int(current_time) < 16):
            expected = "Uni"
        else:
            expected = "Home"

        self.assertEqual(result, expected,
                         "Error in CurrentLocation.get_location method")
