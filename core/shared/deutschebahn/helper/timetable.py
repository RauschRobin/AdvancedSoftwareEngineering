

import json
import requests

from bs4 import BeautifulSoup
from .apiAuthentication import ApiAuthentication


class TimetableRequest(): 
    def __init__(self, station_id, date, hour):
        self.api = ApiAuthentication("", "")
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

# Component interface
class Timetable:
    def __init__(self):
        pass

    def data(self):
        pass

# Concrete Component
class SimpleTimetable(Timetable):
    # Timetable as JSON
    def __init__(self, timetable):
        self.timetable = timetable

    def data(self):
        return self.timetable # replace with data from deutschebahn api
    
# Decorator
class TimetableDecorator(Timetable):
    def __init__(self, timetable):
        self.timetable = timetable

    def data(self):
        return self.timetable.data()
    

# Concrete Decorators
class FilterByLine(TimetableDecorator):
    def __init__(self, timetable, line: str):
        super().__init__(timetable)
        self.line = line

    def data(self):
        # add filter logic by Line
        use_data = self.timetable.data()
        filtered_data = [
            item for item in use_data['timetable']
            if 'ar' in item and 'l' in item['ar'] and item['ar']['l'] == self.line
        ]
                
        filtered_data_json = {
            'station': use_data['station'],
            'timetable': filtered_data
        }

        filtered_data_json = json.dumps(filtered_data_json)

        return filtered_data_json
    
class FilterByDestination(TimetableDecorator):
    def __init__(self, timetable, destination: str):
        super().__init__(timetable)
        self.destination = destination

    def data(self):
        # add filter logic by Destination
        use_data = self.timetable.data()
        filered_data = [
            item for item in use_data['timetable']
            if self.destination in item['dp']['ppth']
        ]

        filteredJsonData = {
            'station': use_data['station'],
            'timetable': filered_data
        }

        filtered_data_json = json.dumps(filteredJsonData)
        return filtered_data_json