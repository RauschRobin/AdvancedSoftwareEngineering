import datetime
import time
import json

from .helper.lunchbreakBuilder import MessageBuilder

from ...shared.PreferencesFetcher.PreferencesFetcher import PreferencesFetcher
from ...communication.voice_output import VoiceOutput
from ...shared.yelp.yelp import Yelp
from ...shared.theMealDb.theMealDb import TheMealDb
from ...shared.currentLocation.CurrentLocation import CurrentLocation
from ...shared.inventory.Inventory import Inventory
from ...shared.rapla.rapla import Rapla
from ...shared.rapla.DateParser import DateParser as dp


class Ernaehrungsplaner:
    def __init__(self, voice_output: VoiceOutput):
        '''
        Initializes the class. 

        Parameters: voice_output (VoiceOutput)
        Returns: None
        '''
        self.voice_output = voice_output
        self.loadPreferences()

        self.yelp = Yelp()
        self.theMealDb = TheMealDb()
        self.currentLocation = CurrentLocation()
        self.inventory = Inventory()
        self.rapla = Rapla(self.rapla_url)
        # store current week timetable & calendar week to reduce number of requests
        self.currentCalendarWeek = dp.get_current_calendar_week()
        self.currentWeekTimeTable = json.loads(self.rapla.fetchLecturesOfWeek(
            self.currentCalendarWeek, datetime.datetime.now().isocalendar()[0]))

        self.calculate_lunchbreak_time()

    def loadPreferences(self):
        '''
        This methods loads all the preferences used in this class and stores them in variables.

        Parameters: None
        Returns: None
        '''
        self.rapla_url = PreferencesFetcher.fetch("rapla-url")
        self.prefred_user_restaurant_categories = PreferencesFetcher.fetch(
            "restraurants-categories-interests")
        self.prefred_user_restaurant_price = PreferencesFetcher.fetch(
            "restaurants-price")

    def run(self):
        '''
        Starts the while loop of this feature.

        Parameters: None
        Returns: None
        '''
        self.startErnaehrungsplanerLoop()

    def startErnaehrungsplanerLoop(self):
        '''
        Runs the while loop of this feature.

        Parameters: None
        Returns: None
        '''
        if self.voice_output == None:
            raise SystemError("WakeUp has no instance of VoiceOutput")

        while True:
            now = datetime.datetime.now()

            # TODO
            # Basic Lunchbreak (12 am)
            # - Calculate the lunchbreak time via rapla

            is_lunchbreak_hour, is_lunchbreak_minute, lunchbreak_duration_in_minutes = self.calculate_lunchbreak_time()
            # Proactive calculation for the lunchbreak
            # if True only for testing purpose
            if True:  # now.hour == is_lunchbreak_hour and now.minute == is_lunchbreak_minute:
                # Find a restaurant near the user with given preferences
                location = self.currentLocation.get_location_adress()
                limit = 1
                radius = 1000
                categories = self.prefred_user_restaurant_categories

                response_businesses = self.yelp.get_restaurants_by_location_limit_radius_categories(
                    location, limit, radius, categories)

                if len(response_businesses.get("businesses", [])) > 0:
                    your_restaurant = response_businesses["businesses"][0]
                    # destruct restaurant
                    your_restaurant_name = your_restaurant["name"]
                    your_restaurant_rating = your_restaurant["rating"]
                    your_restaurant_price = your_restaurant["price"]
                    your_restaurant_location = your_restaurant["location"]

                    # destruct restaurant location
                    your_restaurant_display_adress_street = your_restaurant_location[
                        "display_address"][0]
                    your_restaurant_display_adress_city = your_restaurant_location[
                        "display_address"][1]

                    # construct and convert to string
                    current_hour_minute_string = str(
                        now.hour) + ":" + str(now.minute)
                    current_lunchbreak_duration_string = str(
                        lunchbreak_duration_in_minutes) + " Minuten"

                    # construct the output message
                    message = "Es ist " + current_hour_minute_string + " und " + current_lunchbreak_duration_string + " Mittagspause." + \
                        " Du kannst heute im Restaurant " + \
                        your_restaurant_name + " essen gehen. " + \
                        "Die Adresse ist " + your_restaurant_display_adress_street + \
                        " in " + your_restaurant_display_adress_city

                    # use the builder pattern to dynamically create the message
                    builder = MessageBuilder()

                    builder.add_current_time(current_hour_minute_string)
                    builder.add_lunchbreak_duration_in_minutes(
                        lunchbreak_duration_in_minutes)
                    builder.add_name_of_the_restaurant(your_restaurant_name)
                    builder.add_restaurant_adress(
                        your_restaurant_display_adress_street, your_restaurant_display_adress_city)

                    message = builder.sentence.get_all()

                    self.voice_output.add_message(message)

                else:
                    message = "Ich habe kein Restaurant für dich in der Nähe gefunden."

                    self.voice_output.add_message(message)

            # TODO
            # Bsic evening meal shopping (18 pm)
            # - Notify the user at 18 pm which things he/she can cook or have to buy
            # ...- Use preferences to know what the user likes
            # ...- Check the inventory and use the meal db if everything is available to cook

            # Proactive calculation for cooking and meal shopping in the evening
            if True:  # now.hour == 18 and now.minute == 0:
                message = "Hi, du hast nicht viel Zuhause, geh doch einkaufen du blödes Stück!"

                self.voice_output.add_message(message)
                pass

            # Check every day
            time.sleep(1440)

    def calculate_lunchbreak_time(self):
        '''Calculate the lunchbreak time for the user via rapla

        Parameters: None
        Returns: lunchbreak_hour (int) lunchbreak_minute (int) lunchbreak_duration_in_minutes (int)
        '''
        now = datetime.datetime.now()
        weekday_as_string = now.strftime("%A").lower()

        todays_lectures = self.currentWeekTimeTable.get(
            weekday_as_string, [])

        # TODO
        # - Use Rapla to calculate the lunchbreak

        if todays_lectures is not None:
            # find the end time of the lecture near the lunchbreak time
            for lecture in todays_lectures:
                end_time_hour_minute_string = lecture['lecture']['time_end']
                end_time_hour = int(end_time_hour_minute_string.split(":")[0])
                end_time_minute = int(
                    end_time_hour_minute_string.split(":")[1])
                if end_time_hour > 10 and end_time_hour < 15:
                    lunchbreak_hour = end_time_hour
                    lunchbreak_minute = end_time_minute
                    lunchbreak_duration_in_minutes = 50

        else:
            lunchbreak_hour = 12
            lunchbreak_minute = 0
            lunchbreak_duration_in_minutes = 60

        return lunchbreak_hour, lunchbreak_minute, lunchbreak_duration_in_minutes
