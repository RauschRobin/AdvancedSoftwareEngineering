import unittest
import requests
from ..core.shared.inventory.helper.InventoryManager import InventoryManager as im


class TestInventoryManager(unittest.TestCase):

    def test_init(self):
        result = im()
        expected = im
        self.assertIsInstance(result, expected,
                              "Error in ItemsAccessor.__init__()")

    def test_index(self):
        result = requests.get("http://127.0.0.1:5000/")
        expected = requests.models.Response
        self.assertIsInstance(result, expected,
                              "Error in ItemsAccessor.test_index()")

    def test_get_json(self):
        result = im().get_json()
        expected = str
        bool_expression = len(result) > 5
        self.assertIsInstance(result, expected,
                              "Error in ItemsAccessor.get_json()")
        self.assertTrue(bool_expression,
                        "Error in ItemsAccessor.get_json()")
