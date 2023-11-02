from bs4 import BeautifulSoup
import requests

from .apiAuthenticationSingleton import ApiAuthenticationSingleton

class TimetableRequest(): 
    def __init__(self, station_id, date, hour):
        self.api = ApiAuthenticationSingleton()
        self.url = f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/plan/{station_id}/{date}/{hour}"

    def execute(self):
        response = requests.get(self.url, headers=self.api.get_headers())
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "xml")

            station_element = soup.find('timetable')
            station_name = station_element.get('station')

            timetable = []

            for entry in soup.find_all('s'):
                tl = entry.tl.attrs
                ar = entry.ar.attrs
                dp = entry.dp.attrs

                timetable.append({
                    'tl': tl,
                    'ar': ar,
                    'dp': dp
                })

            json_data = {
                'station': station_name,
                'timetable': timetable
            }

            return json_data
        else:
            return None
        