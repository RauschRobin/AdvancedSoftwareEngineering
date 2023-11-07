from newsapi import NewsApiClient

class NewsAPI:
    def __init__(self, api_key="4664c3868e8e41bd9b9c8d41245ba35a"):
        self.newsapi = NewsApiClient(api_key)

    def get_top_headlines(self, q=None, sources=None, category=None, language=None, country=None):
        return self.newsapi.get_top_headlines(q=q, sources=sources, category=category, language=language, country=country)

    def get_everything(self, q=None, sources=None, domains=None, from_param=None, to=None, language=None, sort_by=None, page=None):
        return self.newsapi.get_everything(q=q, sources=sources, domains=domains, from_param=from_param, to=to, language=language, sort_by=sort_by, page=page)

    def get_sources(self):
        return self.newsapi.get_sources()
