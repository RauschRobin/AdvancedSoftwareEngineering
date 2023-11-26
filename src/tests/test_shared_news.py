from ..core.shared.newsapiorg.news import NewsAPI
import pytest

# pytest fixture
@pytest.fixture
def news_api():
    return NewsAPI()

def test_get_top_headlines(news_api):
    response = news_api.get_top_headlines(search_keyword='bitcoin')
    assert response['status'] == 'ok'

def test_get_everything(news_api):
    response = news_api.get_everything(search_keyword='bitcoin')
    assert response['status'] == 'ok'

def test_get_sources(news_api):
    response = news_api.get_sources()
    assert response['status'] == 'ok'
