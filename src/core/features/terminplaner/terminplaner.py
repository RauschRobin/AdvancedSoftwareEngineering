from ...communication.voice_output import VoiceOutput
from ...shared.Chat_GPT.ChatGPT import ChatGpt
from ...shared.Maps.maps import Maps
from ...shared.WeatherAPI.weather import Weather
from ...shared.rapla.rapla import Rapla
from ...shared.rapla.DateParser import DateParser
import datetime
import time
import random

class Terminplaner:
    def __init__(self, voice_output:VoiceOutput):
        '''
        Initializes the class. 

        Parameters: voice_output (VoiceOutput)
        Returns: None
        '''
        self.voice_output = voice_output
        self.chatgpt = ChatGpt()
        self.maps = Maps()
        self.weather = Weather()
        self.rapla = Rapla()
        self.activity = ""
        self.places = ""

    def run(self):
        '''
        Starts the while loop of this feature.

        Parameters: None
        Returns: None
        '''
        while True:
            # check if Time is in wake up time-span
            # check if lecture has ended

            time.sleep(300)  # Sleep before running and checking again

    def find_activity(self):
        '''
        Finds possible activities for the users free time, while regarding the weather. 

        Parameters: none
        Returns: activities (string[])
        '''
        # get weather of today
        if self.weather.is_weather_data_up_to_date():
            weather_data = self.weather.weather_data
        else:
            weather_data = self.weather.get_weather_of_date()

        # get freetime span of today
        today = datetime.date.today()
        current_year = today.year

        timetable = self.rapla.fetchLecturesOfWeek(DateParser.get_current_calendar_week(), current_year)

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

        current_date = datetime.datetime.now().date()

        activity = self.chatgpt.get_response(
        f"Gebe mir eine JSON-Liste an Aktivitäten, die ich heute (am {current_date}) unternehmen kann. "
        f"Hier sind Wetterdaten für heute: {weather_data}. "
        f"Und zu diesen Uhrzeiten habe ich keine Zeit aufgrund der Vorlesungen: {timetable}"
        f"Der JSON String solte die Syntax aus folgendem Beispiel übernehmen: {example_json_output}"
        )

        self.activity = self.chatgpt.extract_json_code(activity)

        request = f"lese mir den JSON String kurz in grammatikalisch korrekten sätzen vor: {self.activity}"
        proposal = self.chatgpt.get_response(request)

        return proposal

    def find_place(self, activity = None):
        '''
        Finds possible locations for a specific activity. 

        Parameters: activity
        Returns: places (string[])
        '''
        if activity:
            # find places for a specifc activity using the Google Maps API  
            places = self.maps.get_nearby_places("Stuttgart", keyword=activity)
            self.places = places

            request = f"Lese mir den JSON String kurz in grammatikalisch korrekten sätzen vor: {self.places}"
            answer = self.chatgpt.get_response(request)

            return answer
        else:
            # Loop for listing the activities
            if self.activity:
                for activity in self.activity["activities"]:
                    places = self.maps.get_nearby_places("Stuttgart", keyword=activity['location-keyword'])
                    self.places = places

                    request = f"Lese mir den JSON String kurz in grammatikalisch korrekten sätzen vor: {self.places}"
                    answer = self.chatgpt.get_response(request)

                    # The return in for-loop only returns the first answer
                    return answer
                
            else:
                return "Tut mir leid. Ich habe keinen passenden Ort gefunden."