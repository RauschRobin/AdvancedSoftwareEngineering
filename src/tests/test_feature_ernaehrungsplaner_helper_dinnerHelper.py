import unittest

from unittest.mock import patch
from unittest.mock import Mock
from datetime import datetime
from ..core.features.ernaehrungsplaner.helper.dinnerHelper import DinnerHelper


class TestDinnerHelper(unittest.TestCase):
    def setUp(self):
        # Initialize the DinnerHelper with a mock for TheMealDb
        self.mock_the_meal_db = Mock()
        self.dinner_helper = DinnerHelper()
        self.dinner_helper.theMealDb = self.mock_the_meal_db

    def test_find_the_best_meal(self):
        # Mock the return value of search_meal_by_name
        self.mock_the_meal_db.search_meal_by_name.return_value = {
            "meals": [{
                "strMeal": "Spaghetti Carbonara",
                "strCategory": "Pasta"
            }]
        }

        weekly_meals = "Spaghetti Carbonara;Spaghetti Carbonara;Spaghetti Carbonara;Spaghetti Carbonara;Spaghetti Carbonara;Spaghetti Carbonara;Spaghetti Carbonara;"

        # Call the method and check the result
        result = self.dinner_helper.find_the_best_meal(weekly_meals.split(";"))

        # Extract individual elements from the dictionary
        expected_result = ("Spaghetti Carbonara",
                           "Spaghetti Carbonara", "Pasta")
        actual_result = (
            result[0]["strMeal"],
            result[0]["strMeal"],
            result[0]["strCategory"]
        )

        self.assertEqual(actual_result, expected_result)

    def test_find_details_for_meal(self):
        # Mock the return value of search_meal_by_name
        meal_name = "Spaghetti Carbonara"
        self.mock_the_meal_db.search_meal_by_name.return_value = {
            "meals": [{
                "strMeal": meal_name,
                "strInstructions": "Cook spaghetti carbonara..."
            }]
        }

        # Call the method and check the result
        result = self.dinner_helper.find_details_for_meal(meal_name)

        # Extract individual elements from the result tuple
        expected_result = (meal_name, meal_name, "Cook spaghetti carbonara...")
        actual_result = (
            result[0]["strMeal"],
            result[0]["strMeal"],
            result[0]["strInstructions"]
        )

        self.assertEqual(actual_result, expected_result)

    def test_find_random_meal(self):
        # Mock the return value of lookup_single_random_meal
        random_meal_name = "Random Meal"
        self.mock_the_meal_db.lookup_single_random_meal.return_value = {
            "meals": [{
                "strMeal": random_meal_name,
                "strCategory": "Random Category"
            }]
        }

        # Call the method and check the result
        result = self.dinner_helper.find_random_meal()

        # Assert that the returned meal name matches the expected random meal name
        self.assertEqual(result, random_meal_name)

    def test_check_which_ingredients_needed(self):
        # Mock a meal object with various ingredient keys
        your_meal = {
            "strIngredient1": "Ingredient 1",
            "strIngredient2": "",
            "strIngredient3": "Ingredient 3",
            "strIngredient4": None,
            "strIngredient5": "Ingredient 5"
        }

        # Call the method and check the result
        result = self.dinner_helper.check_which_ingredients_needed(your_meal)

        # Assert that the returned list of ingredients matches the expected ingredients
        expected_result = ["Ingredient 1", "Ingredient 3", "Ingredient 5"]
        self.assertEqual(result, expected_result)

    def test_check_which_ingredients_are_at_home(self):
        # Mock inventory_objects as a dictionary of items
        inventory_objects = {
            "item1": {"Item": "Ingredient 1"},
            "item2": {"Item": "Ingredient 2"},
            "item3": {"Item": "Ingredient 3"}
        }

        # Call the method and check the result
        result = self.dinner_helper.check_which_ingredients_are_at_home(
            inventory_objects)

        # Assert that the returned list of inventory matches the expected inventory items
        expected_result = ["Ingredient 1", "Ingredient 2", "Ingredient 3"]
        self.assertEqual(result, expected_result)

    @patch('AdvancedSoftwareEngineering.src.core.features.ernaehrungsplaner.helper.dinnerHelper.datetime')
    def test_is_time_for_dinner_true(self, mock_datetime):
        # Mock the current time to be 18:00 (dinner time)
        mock_datetime.datetime.now.return_value = datetime(
            2023, 11, 30, 18, 0)

        # Call the method and assert that it returns True
        result = self.dinner_helper.is_time_for_dinner()
        self.assertTrue(result)

    @patch('AdvancedSoftwareEngineering.src.core.features.ernaehrungsplaner.helper.dinnerHelper.datetime')
    def test_is_time_for_dinner_false(self, mock_datetime):
        # Mock the current time to be something other than 18:00
        mock_datetime.datetime.now.return_value = datetime(
            2023, 11, 30, 12, 0)

        # Call the method and assert that it returns False
        result = self.dinner_helper.is_time_for_dinner()
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
