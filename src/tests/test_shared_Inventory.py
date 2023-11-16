import unittest
import os
import requests
from threading import Thread
from ..core.shared.inventory.Inventory import Inventory as inv


class TestInventory(unittest.TestCase):

    def test_init(self):
        result = inv()
        expected = inv
        self.assertIsInstance(result, expected,
                              "Error in Inventory.__init__()")

    def test_get_rel_path_to_flask(self):
        result = inv().get_rel_path_to_flask()
        expected = ""
        if (os.name == 'nt'):
            expected = "\\src\\core\\shared\\inventory\\helper\\"
        elif (os.name == 'posix'):
            expected = "/src/core/shared/inventory/helper/"
        self.assertEqual(result, expected, "Error in get_rel_path_to_flask()")

    def test_get_path_to_flask(self):
        result = inv().get_path_to_flask()
        expected = os.getcwd()
        appendix = ""
        if (os.name == 'nt'):
            appendix = "\\src\\core\\shared\\inventory\\helper\\"
        elif (os.name == 'posix'):
            appendix = "/src/core/shared/inventory/helper/"
        expected = expected + appendix
        self.assertEqual(result, expected, "Error in get_rel_path_to_flask()")

    def init_flask(self):
        inv().init_flask()
        result = requests.get("http://127.0.0.1:8000/").status_code
        expected = 200
        self.assertEqual(result, expected, "Error in get_rel_path_to_flask()")

    def test_start_thread(self):
        result = inv().start_thread()
        expected = Thread
        self.assertIsInstance(result, expected,
                              "Error in Inventory.test_index()")

#    def test_call_url(self):
#        result = inv().call_url().text
#        expected = requests.get("http://127.0.0.1:8000/").text
#        bool_expression = result == expected
#        self.assertTrue(bool_expression,
#                        "Error in Inventory.get_json()")
