import unittest
from unittest.mock import mock_open, patch
from ..PreferencesFetcher import PreferencesFetcher
import yaml

class TestPreferencesFetcher(unittest.TestCase):
    def test_fetch(self):
        preferences = {'key1': 'value1', 'key2': 'value2'}
        m = mock_open(read_data=yaml.dump(preferences))
        with patch('builtins.open', m):
            result = PreferencesFetcher.fetch('key1')
            self.assertEqual(result, 'value1')
