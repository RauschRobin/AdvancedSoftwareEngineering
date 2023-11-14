import unittest
from threading import Thread
import requests
from ..core.shared.inventory.Inventory import Inventory as inv


class TestInventory(unittest.TestCase):

    def test_init(self):
        result = inv()
        expected = inv
        self.assertIsInstance(result, expected,
                              "Error in ItemsAccessor.__init__()")

    def test_start_thread(self):
        result = inv.start_thread()
        expected = Thread
        self.assertIsInstance(result, expected,
                              "Error in ItemsAccessor.test_index()")

    def test_call_url(self):
        result = inv().call_url()
        expected = requests.get("http://127.0.0.1:5000/")
        self.assertIsInstance(result, expected,
                              "Error in ItemsAccessor.get_json()")
