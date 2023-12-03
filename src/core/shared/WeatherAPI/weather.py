import requests
from datetime import datetime
from ..YamlFetcher.YamlFetcher import YamlFetcher
import os
from dotenv import load_dotenv

class Weather(object):
    # shared variable
    weather_data = ""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Weather, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        load_dotenv()
        self.weather_api_key = os.getenv('WEATHER_SECRET')

    # returns json string of following weather events in german
    def get_weather_of_date(self):
        '''
        Gets the current weather data for the next hours.

        Parameters: None
        Returns: weather_data (json)
        '''
        latitude = 49.038495434511
        longitude = 9.093383552930298
        url = f"https://api.meteonomiqs.com/rlknl9m9vxwh91p4/v3_1/forecast/{latitude}/{longitude}/"
        headers = {
            "X-BLOBR-KEY": self.weather_api_key 
        }

        response = requests.get(url, headers=headers)
        self.weather_data = response.json()

        return self.weather_data

    def is_weather_data_up_to_date(self):
      '''
        Checks if weather data is up to date.
        Othervise, or if weather_data is not set yet, the function returns false.

        Parameters: None
        Returns: weather_data.date == datetime.date.now() (boolean)
        '''
      if(not self.weather_data):
         return False
      # Convert date string to a datetime object
      date_string = self.weather_data.get("forecastDate")
      date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
      # Get the current date
      current_date = datetime.now().date()
      # Compare the dates
      return date_object.date() == current_date
    
# if __name__ == "__main__":
#   singleton = Weather("API_KEY")
#   print(singleton.is_weather_data_up_to_date())
#   current_weather_data = singleton.get_weather_of_date()

#   # Use the current_weather_data as needed
#   print(current_weather_data)

#   newobj = Weather("API_KEY")
#   print(newobj.is_weather_data_up_to_date())
#   if not newobj.is_weather_data_up_to_date():
#     current_weather_data = newobj.get_weather_of_date()
#     print(current_weather_data)
