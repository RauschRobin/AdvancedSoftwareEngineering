from unittest.mock import mock_open, patch
import yaml
from ..PreferencesFetcher import PreferencesFetcher
import pytest

class TestPreferencesFetcher:
    def test_fetch_existing_key(self):
        preferences = {'user_preferences': {'key1': 'value1', 'key2': 'value2'}}
        with patch('builtins.open', mock_open(read_data=yaml.dump(preferences))):
            result = PreferencesFetcher.fetch('key1')
            assert result == 'value1'

    def test_fetch_nonexistent_key(self):
        preferences = {'user_preferences': {'key1': 'value1', 'key2': 'value2'}}
        with patch('builtins.open', mock_open(read_data=yaml.dump(preferences))):
            with pytest.raises(KeyError):
                PreferencesFetcher.fetch('nonexistent_key')