import requests
import json

class TagesschauAPI:
    '''
    This class communicates with the tagesschau API.
    '''
    
    def __init__(self):
        '''
        Initializes the class.

        Parameters: None
        Returns: None
        '''
        self.api_url = "https://www.tagesschau.de/api2/"
        self.last_eilmeldung = None
        self.last_eilmeldung = self.checkForLastEilmeldung()

    def _make_request(self, endpoint, params=None):
        '''
        Makes the request with endpoint and params to the tagesschau API.

        Parameters: endpoint (string), params (dict)
        Returns: response (json)
        '''
        url = f"{self.api_url}{endpoint}"
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error while trying to access the tagesschau API: {response.status_code}")

    def getNewsOfToday(self):
        """
        Returns a list of all the news of today.

        Parameters: None
        Returns: list of news (json)
        """
        return self._make_request("news/")

    def checkForLastEilmeldung(self):
        """
        Checks if there are new Eilmeldungen.

        Parameters: None
        Returns: last eilmeldung (json)
        """
        new_eilmeldung = None
        for news in self.getNewsOfToday()["news"]:
            if "Eilmeldung" in json.dumps(news):
                new_eilmeldung = news
                break
        if new_eilmeldung:
            if new_eilmeldung != self.last_eilmeldung:
                self.last_eilmeldung = new_eilmeldung
                return new_eilmeldung
        return None

    def searchForNewsWithKeyword(self, keyword):
        """
        Searches for news with a keyword or sentence.

        Parameters: keyword
        Returns: list of news with keyword (json)
        """
        params = {"searchText": keyword}
        return self._make_request("search/", params=params)
