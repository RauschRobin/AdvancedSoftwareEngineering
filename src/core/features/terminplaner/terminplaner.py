from ...communication.voice_output import VoiceOutput
from ...shared.Chat_GPT.ChatGPT import ChatGpt
from ...shared.Maps.maps import Maps
from ...shared.WeatherAPI.weather import Weather
from ...shared.rapla.rapla import Rapla
from ...shared.rapla.DateParser import DateParser
import datetime

class Terminplaner:
    def __init__(self, voice_output:VoiceOutput):
        '''
        Initializes the class. 

        Parameters: voice_output (VoiceOutput)
        Returns: None
        '''
        self.voice_output = voice_output

    def run(self):
        pass

    def find_activity(self):
        '''
        Finds possible activities for the users free time, while regarding the weather. 

        Parameters: none
        Returns: activities (string[])
        '''
        # get weather of today
        weather_obj = Weather()
        if weather_obj.is_weather_data_up_to_date():
            weather_data = weather_obj.weather_data
        else:
            weather_data = weather_obj.get_weather_of_date()

        # # get freetime span of today
        # rapla_obj = Rapla()
        
        # today = datetime.date.today()
        # current_year = today.year

        # timetable = rapla_obj.fetchLecturesOfWeek(DateParser.get_current_calendar_week(), current_year)

        # start: test mock ------------------------------------------------------------------
        timetable = '''{"lectures": [
        {
        "title": "Einführung in die Informatik",
        "professor": "Dr. Müller",
        "time": "10:00 - 12:00",
        "location": "Hauptgebäude, Raum 101"
        },
        {
        "title": "Mathematik für Anfänger",
        "professor": "Prof. Schmidt",
        "time": "13:00 - 15:00",
        "location": "Mathegebäude, Raum 203"
        },
        {
        "title": "Geschichte der Kunst",
        "professor": "Dr. Wagner",
        "time": "15:30 - 17:30",
        "location": "Kunstgebäude, Raum 301"
        }]}'''
        
        # end: test mock ------------------------------------------------------------------

        # find activities using the ChatGPT API
        example_json_output = '''
        {
        "activities": [
            {
            "activity-keyword": "Spazieren",
            "location-keyword": "Park",
            "time": "09:00 - 10:00"
            },
            {
            "activity-keyword": "Mittagessen",
            "location-keyword": "Restaurant",
            "time": "12:00 - 13:00"
            }
        ]
        }
        '''
        chat_obj = ChatGpt()
        activity = chat_obj.get_response(
        f"Gebe mir eine JSON-Liste an Aktivitäten, die ich heute unternehmen kann. "
        f"Hier sind Wetterdaten für heute: {weather_data}. "
        f"Und zu diesen Uhrzeiten habe ich keine Zeit aufgrund der Vorlesungen: {timetable}"
        f"Der JSON String solte die Syntax aus folgendem Beispiel übernehmen: {example_json_output}"
        )
        print(activity)
        activity = chat_obj.extract_json_code(activity)
        print(activity)
        return activity

    def find_place(self, activity):
        '''
        Finds possible locations for a specific activity. 

        Parameters: activity
        Returns: places (string[])
        '''
        # find places for a specifc activity using the Google Maps API
        maps_obj = Maps()
        
        places = maps_obj.get_nearby_places("Stuttgart", keyword=activity)

        return places