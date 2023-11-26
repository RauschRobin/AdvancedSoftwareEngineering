from ..core.shared.newsapiorg.news import NewsAPI
import pytest

@pytest.fixture
def news_api():
    return NewsAPI()    #does not work?

# Tests get_top_headlines()
def test_get_top_headlines(news_api):
    response = news_api.get_top_headlines(search_keyword='bitcoin')
    assert response['status'] == 'ok'

# Tests get_everything()
def test_get_everything(news_api):
    response = news_api.get_everything(search_keyword='bitcoin')
    assert response['status'] == 'ok'

# Tests get_sources()
def test_get_sources(news_api):
    response = news_api.get_sources()
    assert response['status'] == 'ok'
