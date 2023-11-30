
import datetime

from ....shared.theMealDb.theMealDb import TheMealDb


class DinnerHelper():
    def __init__(self):
        self.theMealDb = TheMealDb()

    def find_the_best_meal(self, preferred_meals_week):
        '''Find the best meal for the user today

        Parameters: preferred_meals_week
        Returns: your_meal, your_meal_name, your_meal_category
        '''
        now = datetime.datetime.now()
        preferrd_meal_for_today = preferred_meals_week[now.weekday()]
        meal_object = self.theMealDb.search_meal_by_name(
            preferrd_meal_for_today)

        your_meal = meal_object["meals"][0]
        your_meal_name = your_meal["strMeal"]
        your_meal_category = your_meal["strCategory"]

        return your_meal, your_meal_name, your_meal_category

    def find_details_for_meal(self, meal_name):
        '''Find the instructions for the meal

        Parameters: meal_name
        Returns: your_meal, your_meal_name, your_meal_instruction
        '''
        meal_object = self.theMealDb.search_meal_by_name(
            meal_name)

        your_meal = meal_object["meals"][0]
        your_meal_name = your_meal["strMeal"]
        your_meal_instruction = your_meal["strInstructions"]

        return your_meal, your_meal_name, your_meal_instruction

    def find_random_meal(self):
        '''Find a random meal

        Parameters: None
        Returns: your_meal_name
        '''
        meal_object = self.theMealDb.lookup_single_random_meal()

        your_meal = meal_object["meals"][0]
        your_meal_name = your_meal["strMeal"]
        your_meal_category = your_meal["strCategory"]

        return your_meal_name

    def check_which_ingredients_needed(self, your_meal):
        '''Check which ingredients are needed for the meal

        Parameters: your_meal
        Returns: ingredients
        '''
        ingredients = []
        for key in your_meal:
            if key.startswith("strIngredient") and your_meal[key]:
                ingredients.append(your_meal[key])

        return ingredients

    def check_which_ingredients_are_at_home(self, inventory_objects):
        '''Check which ingredients are at home in the inventory

        Parameters: inventory_objects
        Returns: inventory
        '''
        inventory = []
        for key in inventory_objects:
            inventory.append(inventory_objects[key]["Item"])

        return inventory

    def is_time_for_dinner(self) -> bool:
        '''Calculate the dinner and return true/false

        Parameters: None
        Returns: True/False
        '''
        now = datetime.datetime.now()
        if now.hour == 18 and now.minute == 0:
            return True
        else:
            return False
