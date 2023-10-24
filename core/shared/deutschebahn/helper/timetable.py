

import requests
from .apiAuthentication import ApiAuthentication


class TimetableRequest(): 
    def __init__(self, station_id, date, hour):
        self.api = ApiAuthentication("", "")
        self.url = f"https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/plan/{station_id}/{date}/{hour}"

    def execute(self):
        response = requests.get(self.url, headers=self.api.get_headers())
        if response.status_code == 200:
            return response.text # response.text (xml)
        else:
            return None

# Decorator Pattern
# Use default Timetable and decorate the timetable (filtering) by specific usecases
# Component interface
class Timetable:
    def __init__(self):
        pass

    def data(self):
        pass

# Concrete Component
class SimpleTimetable(Timetable):
    # Timetable as XML
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
        useData = self.timetable.data()
        fileredData = useData
        return fileredData + f" filtered by Line: {self.line}"
    
class FilterByDestination(TimetableDecorator):
    def __init__(self, timetable, destination: str):
        super().__init__(timetable)
        self.destination = destination

    def data(self):
        # add filter logic by Destination
        useData = self.timetable.data()
        fileredData = useData
        return fileredData + f" filtered by Destination: {self.destination}"