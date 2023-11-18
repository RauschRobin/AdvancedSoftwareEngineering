import datetime
import time
import json

from .helper.message.dinnerMessageBuilder import SuccessDinnerMessageBuilder

from .helper.message.lunchbreakMessageBuilder import LunchbreakMessageBuilder
from .helper.lunchbreakHelper import LunchbreakHelper
from .helper.dinnerHelper import DinnerHelper

from ...communication.voice_output import VoiceOutput
from ...shared.PreferencesFetcher.PreferencesFetcher import PreferencesFetcher
from ...shared.yelp.yelp import Yelp
from ...shared.theMealDb.theMealDb import TheMealDb
from ...shared.currentLocation.CurrentLocation import CurrentLocation
from ...shared.inventory.Inventory import Inventory


class Ernaehrungsplaner:
    def __init__(self, voice_output: VoiceOutput):
        '''
        Initializes the class. 

        Parameters: voice_output (VoiceOutput)
        Returns: None
        '''
        self.voice_output = voice_output
        self.load_preferences()

        self.yelp = Yelp()
        self.theMealDb = TheMealDb()
        self.currentLocation = CurrentLocation()
        self.inventory = Inventory()

        self.dinner = DinnerHelper()
        self.lunchbreak = LunchbreakHelper()

    def load_preferences(self):
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
        self.preferred_meals_week = PreferencesFetcher.fetch(
            "meal-dinner-plan").split(";")

    def run(self):
        '''
        Starts the while loop of this feature.

        Parameters: None
        Returns: None
        '''
        self.start_ernaehrungsplaner_loop()

    def start_ernaehrungsplaner_loop(self):
        '''
        Runs the while loop of this feature.

        Parameters: None
        Returns: None
        '''
        if self.voice_output == None:
            raise SystemError("WakeUp has no instance of VoiceOutput")

        while True:
            # check lunchbreak case at round about 12 am
            self.suggest_restaurant_for_lunchbreak()
            # check dinner case at round about 18 pm
            self.tell_dinner_meal_and_missing_ingredients()

            time.sleep(45)

    def suggest_restaurant_for_lunchbreak(self):
        '''
        This function is running in a loop and will proactively tell the user options about the lunchbreak

        Parameters: None
        Returns: None
        '''
        now = datetime.datetime.now()

        # TODO
        # Basic Lunchbreak (12 am)
        # - Calculate the lunchbreak time via rapla // if no then tell the user 30 minutes

        if self.lunchbreak.is_time_for_lunchbreak():
            # Find a restaurant near the user with given preferences
            location = self.currentLocation.get_location_adress()
            limit = 1
            radius = 1000
            categories = self.prefred_user_restaurant_categories

            response_businesses = self.yelp.get_restaurants_by_location_limit_radius_categories(
                location, limit, radius, categories)

            if self.lunchbreak.is_businesses_not_none(response_businesses):
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
                success_message_builder = LunchbreakMessageBuilder()
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
                message = "Ich habe leider kein passendes Restaurant in der Nähe gefunden."

                self.voice_output.add_message(message)

    def tell_dinner_meal_and_missing_ingredients(self):
        '''
        This function is running in a loop and will proactively tell the user options about the lunchbreak

        Parameters: None
        Returns: None
        '''
        if self.dinner.is_time_for_dinner():
            now = datetime.datetime.now()
            preferrd_meal_for_today = self.preferred_meals_week[now.weekday()]
            meal_object = self.theMealDb.search_meal_by_name(
                preferrd_meal_for_today)

            your_meal = meal_object["meals"][0]
            your_meal_name = your_meal["strMeal"]
            your_meal_category = your_meal["strCategory"]

            # Check what ingredients are neccessary for this meal
            ingredients = []
            for key in your_meal:
                if key.startswith("strIngredient") and your_meal[key]:
                    ingredients.append(your_meal[key])

            inventory_objects = json.loads(self.inventory.call_url())

            # Check which ingredients are at home
            inventory = []
            for key in inventory_objects:
                inventory.append(inventory_objects[key]["Item"])

            ingredients_at_home = list(set(ingredients) & set(inventory))
            missing_ingredients = list(set(ingredients) - set(inventory))

            # construct the output message
            dinner_message_builder = SuccessDinnerMessageBuilder()
            dinner_message_builder.add_meal_name(your_meal_name)
            dinner_message_builder.add_meal_category(your_meal_category)
            dinner_message_builder.add_meal_to_buy_ingredients(
                missing_ingredients)

            message = dinner_message_builder.sentence.get_all()

            self.voice_output.add_message(message)
