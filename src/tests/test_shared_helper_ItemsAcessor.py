import unittest
import os
from ..core.shared.inventory.helper.ItemsAccessor import ItemsAccessor as ia


class TestItemsAccessor(unittest.TestCase):

    def test_init(self):
        result = ia()
        expected = ia
        self.assertIsInstance(result, expected,
                              "Error in ItemsAccessor.__init__()")

    def test_get_rel_path(self):
        file_sign = ""
        if (os.name == 'nt'):
            file_sign = "\\"
        elif (os.name == 'posix'):
            file_sign = "/"
        bool_expression = file_sign in ia().get_rel_path()
        self.assertTrue(bool_expression,
                        "Error in ItemsAccessor.test_get_rel_path()")

    def test_get_csv_file_path(self):
        bool_expression = os.path.exists(ia().get_csv_file_path())
        self.assertTrue(bool_expression,
                        "Error in ItemsAccessor.convert_dictionary_to_json()")

    def test_read_csv_into_dictionary(self):
        result = ia().read_csv_into_dictionary()
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
        self.assertIsInstance(result, expected,
                              "Error in ItemsAccessor.convert_dictionary_to_json()")
        self.assertTrue(bool_expression,
                        "Error in ItemsAccessor.convert_dictionary_to_json()")
