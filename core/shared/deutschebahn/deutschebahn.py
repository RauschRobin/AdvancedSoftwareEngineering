
import os

from .helper.apiAuthentication import ApiAuthentication
from .helper.timetable import FilterByDestination, FilterByLine, SimpleTimetable, Timetable, TimetableRequest
from ...communication.voice_output import VoiceOutput
# https://pypi.org/project/deutsche-bahn-api/ --> Wenn man das benutzen möchte

# Todo:
# - Add DeutscheBahn API 
# - Request XML Data from deutschebahn api
# - use Adapter Pattern to convert XML to JSON?

class DeutscheBahn:
    def __init__(self, voice_output:VoiceOutput):
        self.voice_output = voice_output

    def getConnection(self):
        self.voice_output.add_message("Bietigheim-Bissingen|Stuttgart Hbf, S5, 12:37")



timetable_request = TimetableRequest(station_id="8098096", date="231024", hour="10")
data = timetable_request.execute()

timetable = SimpleTimetable(data)
#print(f"Data: {timetable.data()}")

filterd_by_line = FilterByLine(timetable, "S4")
#print(f"Data: {filterd_by_line.data()}") # Output: xml filtered by Line

filter_by_destination = FilterByDestination(timetable, "Bietigheim-Bissingen")
#print(f"Data: {filter_by_destination.data()}") # Output: xml filtered by Destination

