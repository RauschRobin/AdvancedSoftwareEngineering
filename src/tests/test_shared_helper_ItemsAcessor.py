import unittest
from ..core.shared.inventory.helper.InventoryManager import ItemsAccessor as ia


class TestItemsAccessor(unittest.TestCase):

    def test_init(self):
        result = ia()
        expected = ia
        self.assertIsInstance(result, expected,
                              "Error in ItemsAccessor.__init__()")

    def test_get_item_dictionary(self):
        result = ia().get_item_dictionary()
        expected = dict
        bool_expression = len(result) > 5
        self.assertIsInstance(result, expected,
                              "Error in ItemsAccessor.read_csv_into_dictionary()")
        self.assertTrue(bool_expression,
                        "Error in ItemsAccessor.convert_dictionary_to_json()")

    def test_convert_dictionary_to_json(self):
        result = ia().convert_dictionary_to_json()
        expected = str
        bool_expression = len(result) > 5
        self.assertIsInstance(result, expected, "Error in ItemsAccessor.convert_dictionary_to_json()")
        self.assertTrue(bool_expression, "Error in ItemsAccessor.convert_dictionary_to_json()")
