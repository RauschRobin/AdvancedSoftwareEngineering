import unittest
from flask import Flask
from ..core.shared.inventory.helper.InventoryManager import AppContext as ac


class TestAppContext(unittest.TestCase):


    def test_instance(self):
        result = ac.app()
        expected = Flask
        bool_expression = ac.app() is result
        self.assertIsInstance(result, expected,
                              "Error in AppContext.app()")
        self.assertTrue(bool_expression,
                        "Error in ItemsAccessor.convert_dictionary_to_json()")
        