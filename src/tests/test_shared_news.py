from ..core.shared.newsapiorg.news import NewsAPI

def test_get_top_headlines():
    news_api = NewsAPI()
    response = news_api.get_top_headlines(search_keyword='bitcoin')
    assert response['status'] == 'ok'

def test_get_everything():
    news_api = NewsAPI()
    response = news_api.get_everything(search_keyword='bitcoin')
    assert response['status'] == 'ok'

def test_get_sources():
    news_api = NewsAPI()
    response = news_api.get_sources()
    assert response['status'] == 'ok'