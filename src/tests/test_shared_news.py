from ..core.shared.newsapiorg.news import NewsAPI

news_api = NewsAPI()

def test_get_top_headlines():
    response = news_api.get_top_headlines(search_keyword='bitcoin')
    assert response['status'] == 'ok'

def test_get_everything():
    response = news_api.get_everything(search_keyword='bitcoin')
    assert response['status'] == 'ok'

def test_get_sources():
    response = news_api.get_sources()
    assert response['status'] == 'ok'