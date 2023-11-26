import pytest
from unittest.mock import Mock
from ..core.shared.newsapiorg.news import NewsAPI

@pytest.fixture
def newsapi_instance():
    # Mocking the NewsApiClient so that we don't make actual API calls during testing
    newsapi = NewsAPI()
    newsapi.newsapi = Mock()
    return newsapi

def test_get_top_headlines(newsapi_instance):
    # Test when search_keyword is provided
    result = newsapi_instance.get_top_headlines(search_keyword='bitcoin')
    newsapi_instance.newsapi.get_top_headlines.assert_called_once_with(q='bitcoin', sources=None, category=None, language=None, country=None)

def test_get_everything(newsapi_instance):
    # Test when search_keyword is not provided
    result = newsapi_instance.get_everything(search_keyword=None)
    assert result is None

    # Test when search_keyword is provided
    result = newsapi_instance.get_everything(search_keyword='bitcoin')
    newsapi_instance.newsapi.get_everything.assert_called_once_with(q='bitcoin', sources=None, domains=None, from_param=None, to=None, language=None, sort_by=None, page=None)

def test_get_sources(newsapi_instance):
    result = newsapi_instance.get_sources()
    newsapi_instance.newsapi.get_sources.assert_called_once()
