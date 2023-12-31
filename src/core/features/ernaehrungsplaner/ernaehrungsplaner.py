import datetime
import time
import json
from ...shared.Chat_GPT.ChatGPT import ChatGpt
from .helper.message.dinnerMessageBuilder import DinnerMessageBuilder
from .helper.message.lunchbreakMessageBuilder import LunchbreakMessageBuilder
from .helper.lunchbreakHelper import LunchbreakHelper
from .helper.dinnerHelper import DinnerHelper
from ...communication.voice_output import VoiceOutput
from ...shared.YamlFetcher.YamlFetcher import YamlFetcher
from ...shared.yelp.yelp import Yelp
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
        self.yelp = Yelp()
        self.chatgpt = ChatGpt()
        self.currentLocation = CurrentLocation()
        self.inventory = Inventory()
        self.dinner = DinnerHelper()
        self.lunchbreak = LunchbreakHelper()
        self.restaurants = {}
        self.selected_restaurant = {}
        self.meal_to_cook = ""

    def load_preferences(self):
        '''
        This methods loads all the preferences used in this class and stores them in variables.

        Parameters: None
        Returns: None
        '''
        self.prefred_user_restaurant_categories = YamlFetcher.fetch(
            "restraurants-categories-interests", "preferences.yaml")
        self.prefred_user_restaurant_price = YamlFetcher.fetch(
            "restaurants-price", "preferences.yaml")
        self.preferred_meals_week = YamlFetcher.fetch(
            "meal-dinner-plan", "preferences.yaml").split(";")

    def run(self):
        '''
        Starts the while loop of this feature.

        Parameters: None
        Returns: None
        '''
        self.load_preferences()
        self.start_ernaehrungsplaner_loop()

    def start_ernaehrungsplaner_loop(self):
        '''
        Runs the while loop of this feature.

        Parameters: None
        Returns: None
        '''
        if self.voice_output is None:
            raise SystemError("WakeUp has no instance of VoiceOutput")

        while True:
            # check lunchbreak case at round about 12 am
            self.suggest_restaurant_for_lunchbreak()
            # check dinner case at round about 18 pm
            self.tell_dinner_meal_and_missing_ingredients()

            time.sleep(60)

    def set_response_businesses(self) -> None:
        """ Find a restaurant near the user with
        given preferences and save it inside restaurants

        Parameters: self
        Returns: None
        """
        location = self.currentLocation.get_location_adress()
        limit = 1
        radius = 1000
        categories = self.prefred_user_restaurant_categories
        self.restaurants = self.yelp.get_restaurants_by_location_limit_radius_categories(
                location, limit, radius, categories)

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

            self.set_response_businesses()

            response_businesses = self.restaurants

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

                # TODO: refactor with director pattern
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
            your_meal, your_meal_name, your_meal_category = self.dinner.find_the_best_meal(
                self.preferred_meals_week)

            self.your_meal_name = your_meal_name

            ingredients = self.dinner.check_which_ingredients_needed(your_meal)

            inventory_objects = json.loads(self.inventory.get_inventory())
            inventory = self.dinner.check_which_ingredients_are_at_home(
                inventory_objects)

            ingredients_at_home = list(set(ingredients) & set(inventory))
            missing_ingredients = list(set(ingredients) - set(inventory))

            # construct the output message
            # TODO: refactor with director pattern
            dinner_message_builder = DinnerMessageBuilder()
            dinner_message_builder.add_meal_name(your_meal_name)
            dinner_message_builder.add_meal_category(your_meal_category)
            dinner_message_builder.add_meal_to_buy_ingredients(
                missing_ingredients)

            message = dinner_message_builder.sentence.get_all()

            self.voice_output.add_message(message)

    def chooseRestaurantWithKeyword(self, keyword) -> None:
        """User chooses a restaurant, which will be
        the referential-point for other functions

        Parameters: keyword (string)
        Returns: none
        """
        # define and set variables
        message = "Restaurant nicht gefunden"
        restaurant_name = "nicht"
        self.set_response_businesses()

        # check if self.restaurants is set
        if (self.restaurants is not None and self.restaurants != {}):
            restaurants_lst = self.restaurants["businesses"]
            match keyword:
                case "eins":
                    self.selected_restaurant = restaurants_lst[0]
                    restaurant_name = self.selected_restaurant["name"]
                case "zwei":
                    self.selected_restaurant = restaurants_lst[1]
                    restaurant_name = self.selected_restaurant["name"]
                case "drei":
                    self.selected_restaurant = restaurants_lst[2]
                    restaurant_name = self.selected_restaurant["name"]

        # return message
        message = f'Restaurant {restaurant_name} ausgewählt'
        print(restaurant_name)
        self.voice_output.add_message(message)

    def getRestaurantContact(self) -> bool:
        '''
        Gets the Contact-Information of a a specific restaurant
        and adds the message to the voice output message_queue.

        Parameters: keyword (string)
        Returns: bool
        '''
        # define and set variable
        message = "Es wurde kein Restaurant ausgewählt"

        # check if self.restaurants is set, construct and add output-message
        if (self.selected_restaurant is None and self.restaurants != {}):
            print(message)
            self.voice_output.add_message(message)
            return False
        else:
            message = f"Die Telefonnummer "
            message = message + f"von {self.selected_restaurant['name']} "
            message = message + f"lautet: {self.selected_restaurant['phone']}"
            print(message)
            self.voice_output.add_message(message)
            return True

    def getRestaurantLocation(self) -> bool:
        '''
        Gets the Location-Information of a a specific restaurant
        and adds the message to the voice output message_queue.

        Parameters: keyword (string)
        Returns: bool
        '''
        # define and set variable
        message = "Es wurde kein Restaurant ausgewählt"

        # check if self.restaurants is set, construct and add output-message
        if (self.selected_restaurant is None and self.restaurants != {}):
            print(message)
            self.voice_output.add_message(message)
            return False
        else:
            message = f"Das Restaurant {self.selected_restaurant['name']} "
            message = message + f"befindet sich in {self.selected_restaurant['location']['zip_code']} "
            message = message + f"{self.selected_restaurant['location']['city']} in "
            message = message + f"{self.selected_restaurant['location']['address1']}"
            print(message)
            self.voice_output.add_message(message)
            return True

    def how_to_cook_the_meal(self):
        '''
        This function enables the user to get a detailed meal information.

        Parameters: None
        Returns: None
        '''
        # find the details for the meal to cook
        if self.meal_to_cook:
            your_meal, your_meal_name, cooking_instructions = self.dinner.find_details_for_meal(
                self.meal_to_cook)
            self.voice_output.add_message(
                f"Hier sind die Schritte um {self.meal_to_cook} zu kochen.")
        else:
            your_meal, your_meal_name, cooking_instructions = self.dinner.find_the_best_meal(
                self.preferred_meals_week)
            self.voice_output.add_message(
                f"Auf dem Ernährungsplan steht heute {your_meal_name}. Hier ist die Anleitung dazu.")

        # tell the user the instructions
        if isinstance(cooking_instructions, str):
            sentences = cooking_instructions.split('. ')

            for i, sentence in enumerate(sentences):
                message = str(self.chatgpt.get_response(
                    "Geb nur den übersetzen Satz aus. Übersetze den folgenden Satz auf deutsch: " + sentence.lower()))

                self.voice_output.add_message(message)
        else:
            message = "Ich kann keine Anleitung finden."

            self.voice_output.add_message(message)

    def cook_something_different(self):
        '''
        This function finds a random meal

        Parameters: None
        Returns: None
        '''
        your_meal_name = self.dinner.find_random_meal()
        self.meal_to_cook = your_meal_name

        message = f"Du kannst stattdessen {your_meal_name} kochen."

        self.voice_output.add_message(message)

    def ingredients_at_home_to_cook(self):
        # find the inventory for the meal to cook
        if self.meal_to_cook:
            your_meal, your_meal_name, your_meal_instruction = self.dinner.find_details_for_meal(
                self.meal_to_cook)
        else:
            your_meal, your_meal_name, your_meal_instruction = self.dinner.find_the_best_meal(
                self.preferred_meals_week)

        ingredients = self.dinner.check_which_ingredients_needed(your_meal)

        inventory_objects = json.loads(self.inventory.get_inventory())
        inventory = self.dinner.check_which_ingredients_are_at_home(
            inventory_objects)
        ingredients_at_home = list(set(ingredients) & set(inventory))

        message = self.chatgpt.get_response(
            f"Umformulieren als Text und übersetzen auf deutsch: Du hast folgende Zutaten hast du für das Gericht {your_meal_name} daheim: {str(ingredients_at_home)}")
        self.voice_output.add_message(message)

    def generate_shopping_list_for_meal(self):
        # find the inventory for the meal to cook
        if self.meal_to_cook:
            your_meal, your_meal_name, your_meal_instruction = self.dinner.find_details_for_meal(
                self.meal_to_cook)
        else:
            your_meal, your_meal_name, your_meal_instruction = self.dinner.find_the_best_meal(
                self.preferred_meals_week)

        ingredients = self.dinner.check_which_ingredients_needed(your_meal)

        inventory_objects = json.loads(self.inventory.get_inventory())
        inventory = self.dinner.check_which_ingredients_are_at_home(
            inventory_objects)

        missing_ingredients = list(set(ingredients) - set(inventory))

        message = self.chatgpt.get_response(
            f"Umformulieren als Text und übersetzen auf deutsch: Du hast musst diese Zutaten für das Gericht {your_meal_name} noch einkaufen: {str(missing_ingredients)}")
        self.voice_output.add_message(message)
