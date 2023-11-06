from bs4 import BeautifulSoup
import requests
from .apiAuthenticationSingleton import ApiAuthenticationSingleton

class StationRequest(): 
    def __init__(self, station_name):
        self.api = ApiAuthenticationSingleton()
        self.url = f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/station/{station_name}"

    def execute(self):
        response = requests.get(self.url, headers=self.api.get_headers(), timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')

            station_tag = soup.find('station')

            #meta = station_tag['meta']
            name = station_tag['name']
            eva = station_tag['eva']
            #ds100 = station_tag['ds100']
            db = station_tag['db']
            #creationts = station_tag['creationts']

            json_data = {
                'name': name,
                'eva': eva,
                'db': db
            }

            return json_data
        else:
            return None
        