import unittest
from ..core.shared.inventory.helper.ItemsAccessor import ItemsAccessor as ia


class TestItemsAccessor(unittest.TestCase):

    def test_init(self):
        result = ia()
        expected = ia
        self.assertIsInstance(result, expected,
                              "Error in ItemsAccessor.__init__()")

    def test_read_csv_into_dictionary(self):
        result = ia().read_csv_into_dictionary()
        expected = "???"



    def test_convert_dictionary_to_json(self):
        result = ia().convert_dictionary_to_json()
        expected = "???"
