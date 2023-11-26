import os
from dotenv import load_dotenv
from newsapi import NewsApiClient

class NewsAPI:
    '''
    This class communicates with the newsapi.org API and is responsible for fetching news from newsapi.org.
    '''

    def __init__(self):
        '''
        This method initializes the class.

        Parameters: api_key - string (optional)
        Returns: None
        '''
        load_dotenv()
        key=os.environ('NEWSAPI_SECRET')
        self.newsapi = NewsApiClient(api_key=key)

    def get_top_headlines(self, search_keyword=None, sources=None, category=None, language=None, country=None):
        '''
        This method returns the top headlines from the newsapi.org API.

        Parameters: search_keyword - string (optional), sources - string (optional), category - string (optional), language - string (optional), country - string (optional)
        Returns: top headlines (json)
        '''
        return self.newsapi.get_top_headlines(q=search_keyword, sources=sources, category=category, language=language, country=country)

    def get_everything(self, search_keyword=None, sources=None, domains=None, from_param=None, to=None, language=None, sort_by=None, page=None):
        '''
        This method returns everything from the newsapi.org API.

        Parameters: search_keyword - string (optional), sources - string (optional), domains - string (optional), from_param - string (optional), to - string (optional), language - string (optional), sort_by - string (optional), page - string (optional)
        Returns: everything (json)
        '''
        if search_keyword is None or search_keyword == "":
            return None
        return self.newsapi.get_everything(q=search_keyword, sources=sources, domains=domains, from_param=from_param, to=to, language=language, sort_by=sort_by, page=page)

    def get_sources(self):
        '''
        This method returns the sources from the newsapi.org API.

        Parameters: None
        Returns: sources (json)
        '''
        return self.newsapi.get_sources()
