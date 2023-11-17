import datetime
import time
import json

from .helper.message.dinnerMessageBuilder import SuccessDinnerMessageBuilder

from .helper.message.failureMessageBuilder import LunchbreakFailureMessageBuilder
from .helper.message.successMessageBuilder import LunchbreakSuccessMessageBuilder

from ...communication.voice_output import VoiceOutput
from ...shared.PreferencesFetcher.PreferencesFetcher import PreferencesFetcher
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
            # check lunchbreak case at round about 12 am
            self.loop_lunchbreak()
            # check dinner case at round about 18 pm
            self.loop_dinner()

            time.sleep(45)

    def loop_lunchbreak(self):
        '''
        This function is running in a loop and will proactively tell the user options about the lunchbreak

        Parameters: None
        Returns: None
        '''
        now = datetime.datetime.now()

        # TODO
        # Basic Lunchbreak (12 am)
        # - Calculate the lunchbreak time via rapla // if no then tell the user 30 minutes

        if self.is_time_for_lunchbreak():
            # Find a restaurant near the user with given preferences
            location = self.currentLocation.get_location_adress()
            limit = 1
            radius = 1000
            categories = self.prefred_user_restaurant_categories

            response_businesses = self.yelp.get_restaurants_by_location_limit_radius_categories(
                location, limit, radius, categories)

            if self.is_businesses_not_none(response_businesses):
                your_restaurant = response_businesses["businesses"][0]
                # destruct restaurant
                your_restaurant_name = your_restaurant["name"]
                your_restaurant_location = your_restaurant["location"]
                # destruct restaurant location
                your_restaurant_display_adress_street = your_restaurant_location[
                    "display_address"][0]
                your_restaurant_display_adress_city = your_restaurant_location[
                    "display_address"][1]

                # use the builder pattern to dynamically create the message
                success_message_builder = LunchbreakSuccessMessageBuilder()
                success_message_builder.add_current_time(now.hour, now.minute)
                # success_message_builder.add_lunchbreak_duration_in_minutes(60)
                success_message_builder.add_name_of_the_restaurant(
                    your_restaurant_name)
                success_message_builder.add_restaurant_adress(
                    your_restaurant_display_adress_street, your_restaurant_display_adress_city)

                message = success_message_builder.sentence.get_all()

                self.voice_output.add_message(message)

            else:
                # construct message when no restaurant was found
                failure_message_builder = LunchbreakFailureMessageBuilder()
                failure_message_builder.add_failure()
                message = failure_message_builder.sentence.get_all()

                self.voice_output.add_message(message)

    def loop_dinner(self):
        '''
        This function is running in a loop and will proactively tell the user options about the lunchbreak

        Parameters: None
        Returns: None
        '''

        # TODO
        # Bsic evening meal shopping (18 pm)
        # - Notify the user at 18 pm which things he/she can cook or have to buy
        # ...- Use preferences to know what the user likes
        # ...- Check the inventory and use the meal db if everything is available to cook

        # Proactive calculation for cooking and meal shopping in the evening
        if self.is_time_for_dinner():
            # TODO: select a meal from the preferences
            prefered_meals = PreferencesFetcher.fetch(
                "meal-dinner-plan").split(";")
            now = datetime.datetime.now()
            preferd_meal_for_today = prefered_meals[now.weekday()]
            meal_object = self.theMealDb.search_meal_by_name(
                preferd_meal_for_today)

            random_meal = meal_object["meals"][0]

            your_meal_name = random_meal["strMeal"]
            your_meal_category = random_meal["strCategory"]

            ingredients = []
            for key in random_meal:
                if key.startswith("strIngredient") and random_meal[key]:
                    ingredients.append(random_meal[key])

            inventory_objects = json.loads(self.inventory.call_url())

            inventory = []
            for key in inventory_objects:
                inventory.append(inventory_objects[key]["Item"])

            have = list(set(ingredients) & set(inventory))
            missing_ingredients = list(set(ingredients) - set(inventory))

            dinner_builder = SuccessDinnerMessageBuilder()
            dinner_builder.add_meal_name(your_meal_name)
            dinner_builder.add_meal_category(your_meal_category)
            dinner_builder.add_meal_to_buy_ingredients(missing_ingredients)

            message = dinner_builder.sentence.get_all()

            self.voice_output.add_message(message)

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

        else:
            lunchbreak_hour = 12
            lunchbreak_minute = 0

        return lunchbreak_hour, lunchbreak_minute

    def is_time_for_lunchbreak(self) -> bool:
        '''Calculate the lunchtime and return true/false

        Parameters: None
        Returns: True/False
        '''
        now = datetime.datetime.now()
        is_lunchbreak_hour, is_lunchbreak_minute = self.calculate_lunchbreak_time()

        if now.hour == is_lunchbreak_hour and now.minute == is_lunchbreak_minute:
            return True
        else:
            return False

    def is_businesses_not_none(self, businesses) -> bool:
        '''Find out if the businesses response are not null and return true/false

        Parameters: businesses (Dic, None)
        Returns: True/False
        '''
        if len(businesses.get("businesses", [])) > 0:
            return True
        else:
            return False

    def is_time_for_dinner(self) -> bool:
        '''Calculate the dinner and return true/false

        Parameters: None
        Returns: True/False
        '''
        now = datetime.datetime.now()
        if now.hour == 18 and now.minute == 0:
            return True
        else:
            # For testing True
            return True
