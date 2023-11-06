import requests
import json

class TagesschauAPI:
    def __init__(self):
        self.api_url = "https://www.tagesschau.de/api2/"
        self.last_eilmeldung = None

    def _make_request(self, endpoint, params=None):
        url = f"{self.api_url}{endpoint}"
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error while trying to access the tagesschau API: {response.status_code}")

    def getNewsOfToday(self):
        """
        Returns a list of all the news of today.
        """
        return self._make_request("news/")

    def checkForLastEilmeldung(self):
        """
        Checks if there are new Eilmeldungen.
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
        """
        params = {"searchText": keyword}
        return self._make_request("search/", params=params)
