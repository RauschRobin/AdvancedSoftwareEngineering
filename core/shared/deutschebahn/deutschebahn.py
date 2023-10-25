
from .helper.timetable import FilterByDestination, FilterByLine, SimpleTimetable, TimetableRequest
from ...communication.voice_output import VoiceOutput
# https://pypi.org/project/deutsche-bahn-api/ --> Wenn man das benutzen möchte

class DeutscheBahn:
    def __init__(self, voice_output:VoiceOutput):
        self.voice_output = voice_output

    def getConnection(self):
        self.voice_output.add_message("Bietigheim-Bissingen|Stuttgart Hbf, S5, 12:37")

    # E.g. line="4" station_id="8098096", date="231025", hour="10"
    def getJsonByLineStationidDateHour(self, line: str, station_id: str, date: str, hour: str):
        timetable_request = TimetableRequest(station_id, date, hour) 
        data = timetable_request.execute()

        timetable = SimpleTimetable(data)
        #print(f"Data: {timetable.data()}")

        filterd_by_line = FilterByLine(timetable, line)
        #print(f"Filtered by Line: {filterd_by_line.data()}")

        return filterd_by_line.data()
    
    # E.g. destination="Bietigheim-Bissingen" station_id="8098096", date="231025", hour="10"
    def getJsonByDestinationStationidDateHour(self, destination: str, station_id: str, date: str, hour: str):
        timetable_request = TimetableRequest(station_id, date, hour)
        data = timetable_request.execute()
        #print(f"Data Execute: {data}")

        timetable = SimpleTimetable(data)
        #print(f"Data: {timetable.data()}")

        filter_by_destination = FilterByDestination(timetable, destination) # destination: "Marbach(Neckar)" or "Bietigheim-Bissingen"
        #print(f"Filtered by Destination: {filter_by_destination.data()}")

        return filter_by_destination.data()
       













