import pytest
from unittest.mock import Mock, patch
from ..core.shared.tagesschau.tagesschau import TagesschauAPI

# Create a test instance of the TagesschauAPI class
@pytest.fixture
def api_instance():
    return TagesschauAPI()

# Mock the requests.get function to avoid making real HTTP requests
@pytest.fixture
def mock_requests_get():
    with patch('requests.get') as mock_get:
        yield mock_get

# Test the _make_request method
def test_make_request(api_instance, mock_requests_get):
    # Mock a successful response
    response_json = {'key': 'value'}
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = response_json

    result = api_instance._make_request('test_endpoint')
    assert result == response_json

    # Mock a failed response
    mock_requests_get.return_value.status_code = 404
    with pytest.raises(Exception) as exc_info:
        api_instance._make_request('test_endpoint')
    assert "Error while trying to access the tagesschau API" in str(exc_info.value)

# Test the getNewsOfToday method
def test_get_news_of_today(api_instance, mock_requests_get):
    # Mock a successful response
    response_json = {'news': ['news_item1', 'news_item2']}
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = response_json

    result = api_instance.getNewsOfToday()
    assert result == response_json

# Test the checkForLastEilmeldung method
def test_check_for_last_eilmeldung(api_instance, mock_requests_get):
    # Mock a response with a new Eilmeldung
    eilmeldung_json = {'title': 'Eilmeldung: Breaking News'}
    news_json = {'news': [eilmeldung_json, 'news_item2']}
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = news_json

    result = api_instance.checkForLastEilmeldung()
    assert result == eilmeldung_json

    # Mock a response with the same Eilmeldung as before
    result = api_instance.checkForLastEilmeldung()
    assert result is None

# Test the searchForNewsWithKeyword method
def test_search_for_news_with_keyword(api_instance, mock_requests_get):
    keyword = "test_keyword"

    # Mock a successful response
    response_json = {'results': ['result1', 'result2']}
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = response_json

    result = api_instance.searchForNewsWithKeyword(keyword)
    assert result == response_json
