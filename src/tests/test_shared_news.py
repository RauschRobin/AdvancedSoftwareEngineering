from ..core.shared.newsapiorg.news import NewsAPI

def test_get_top_headlines():
    news_api = NewsAPI(override_api_key="4664c3868e8e41bd9b9c8d41245ba35a")
    response = news_api.get_top_headlines(q='bitcoin')
    assert response['status'] == 'ok'

def test_get_everything():
    news_api = NewsAPI(override_api_key="4664c3868e8e41bd9b9c8d41245ba35a")
    response = news_api.get_everything(q='bitcoin')
    assert response['status'] == 'ok'

def test_get_sources():
    news_api = NewsAPI(override_api_key="4664c3868e8e41bd9b9c8d41245ba35a")
    response = news_api.get_sources()
    assert response['status'] == 'ok'