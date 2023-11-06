from .helper.stationRequest import StationRequest
from .helper.timetable import FilterByDestination, FilterByLine, SimpleTimetable
from .helper.timetableRequest import TimetableRequest
# Inspiration from: https://pypi.org/project/deutsche-bahn-api/

class DeutscheBahn:
    def __init__(self):
        pass

    def getStationDetailByStationname(self, station_name: str):
        """Returns one station that fits to the inputtext
    
        Input: E.g. station_name="Stuttgart Hbf (tief)"
        Return: E.g. {'name': 'Stuttgart Hbf (tief)', 'eva': '8098096', 'db': 'true'}
        """
        station_request = StationRequest(station_name)
        station = station_request.execute()
        return station

    def getTimetableByLineStationidDateHour(self, line: str, station_id: str, date: str, hour: str):
        """Return JSON data for a given line, stationid and date and hour.

        Input: E.g. line="4" station_id="8098096", date="231025", hour="10"
        Output: E.g. { 'station': 'NAME', 'timetable': {[ Object ]}}
        """
        timetable_request = TimetableRequest(station_id, date, hour) 
        data = timetable_request.execute()
        timetable = SimpleTimetable(data)
        filterd_by_line = FilterByLine(timetable, line)
        return filterd_by_line.data()

    def getTimetableByDestinationStationidDateHour(self, destination: str, station_id: str, date: str, hour: str):
        """Returns Timetable (all trains) for a given destination, stationid and date and hour.
     
        Input: E.g. destination="Bietigheim-Bissingen" station_id="8098096", date="231025", hour="10"
        Output: E.g. {'station': 'NAME', 'timetable': {[ Object ]}}
        """
        timetable_request = TimetableRequest(station_id, date, hour)
        data = timetable_request.execute()
        timetable = SimpleTimetable(data)

        # destination: "Marbach(Neckar)" or "Bietigheim-Bissingen"
        filter_by_destination = FilterByDestination(timetable, destination) 
        return filter_by_destination.data()
