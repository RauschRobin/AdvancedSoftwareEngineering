from newsapi import NewsApiClient

class NewsAPI:
    '''
    This class communicates with the newsapi.org API.
    '''

    def __init__(self, api_key="4664c3868e8e41bd9b9c8d41245ba35a"):
        '''
        This method initializes the class.

        Parameters: api_key - string (optional)
        Returns: None
        '''
        self.newsapi = NewsApiClient(api_key)

    def get_top_headlines(self, q=None, sources=None, category=None, language=None, country=None):
        '''
        This method returns the top headlines from the newsapi.org API.

        Parameters: q - string (optional), sources - string (optional), category - string (optional), language - string (optional), country - string (optional)
        Returns: top headlines (json)
        '''
        return self.newsapi.get_top_headlines(q=q, sources=sources, category=category, language=language, country=country)

    def get_everything(self, q=None, sources=None, domains=None, from_param=None, to=None, language=None, sort_by=None, page=None):
        '''
        This method returns everything from the newsapi.org API.

        Parameters: q - string (optional), sources - string (optional), domains - string (optional), from_param - string (optional), to - string (optional), language - string (optional), sort_by - string (optional), page - string (optional)
        Returns: everything (json)
        '''
        return self.newsapi.get_everything(q=q, sources=sources, domains=domains, from_param=from_param, to=to, language=language, sort_by=sort_by, page=page)

    def get_sources(self):
        '''
        This method returns the sources from the newsapi.org API.

        Parameters: None
        Returns: sources (json)
        '''
        return self.newsapi.get_sources()
