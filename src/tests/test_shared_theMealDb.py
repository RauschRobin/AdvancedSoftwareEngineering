import unittest
from unittest.mock import patch, Mock

from ..core.shared.theMealDb.theMealDb import TheMealDb


class TestTheMealDb(unittest.TestCase):
    @patch('AdvancedSoftwareEngineering.src.core.shared.theMealDb.theMealDb.SearchByMealURLCreator')
    @patch('AdvancedSoftwareEngineering.src.core.shared.theMealDb.theMealDb.requests.get')
    def test_search_meal_by_name(self, mock_get, mock_url_creator):
        mock_creator_instance = mock_url_creator.return_value
        mock_creator_instance.construct_url.return_value = 'http://testurl.com/search?name=Arrabiata'

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"meals": [{"name": "Arrabiata"}]}
        mock_get.return_value = mock_response

        obj = TheMealDb()
        result = obj.search_meal_by_name("Arrabiata")

        self.assertEqual(result, {"meals": [{"name": "Arrabiata"}]})

        mock_url_creator.assert_called_with("Arrabiata")

        mock_get.assert_called_with('http://testurl.com/search?name=Arrabiata')

    @patch('AdvancedSoftwareEngineering.src.core.shared.theMealDb.theMealDb.requests.get')
    def test_search_meal_by_name_handles_error(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        obj = TheMealDb()
        result = obj.search_meal_by_name("InvalidMeal")

        self.assertEqual(result, {})

    @patch('AdvancedSoftwareEngineering.src.core.shared.theMealDb.theMealDb.ListAllMealsByFirstLetterURLCreator')
    @patch('AdvancedSoftwareEngineering.src.core.shared.theMealDb.theMealDb.requests.get')
    def test_list_all_meals_by_first_letter(self, mock_get, mock_url_creator):
        mock_creator_instance = mock_url_creator.return_value
        mock_creator_instance.construct_url.return_value = 'http://testurl.com/list?first_letter=a'

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"meals": [{"name": "Apple Pie"}]}
        mock_get.return_value = mock_response

        obj = TheMealDb()
        result = obj.list_all_meals_by_first_letter("a")

        self.assertEqual(result, {"meals": [{"name": "Apple Pie"}]})

        mock_url_creator.assert_called_with("a")

        mock_get.assert_called_with('http://testurl.com/list?first_letter=a')

    @patch('AdvancedSoftwareEngineering.src.core.shared.theMealDb.theMealDb.requests.get')
    def test_list_all_meals_by_first_letter_handles_error(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        obj = TheMealDb()
        result = obj.list_all_meals_by_first_letter("InvalidLetter")

        self.assertEqual(result, {})

    @patch('AdvancedSoftwareEngineering.src.core.shared.theMealDb.theMealDb.LookupMealDetailsByIdURLCreator')
    @patch('AdvancedSoftwareEngineering.src.core.shared.theMealDb.theMealDb.requests.get')
    def test_lookup_meal_details_by_id(self, mock_get, mock_url_creator):
        mock_url_creator_instance = mock_url_creator.return_value
        mock_url_creator_instance.construct_url.return_value = 'http://testurl.com/lookup?id=52772'

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"meals": [{"id": "52772"}]}
        mock_get.return_value = mock_response

        obj = TheMealDb()
        result = obj.lookup_meal_details_by_id("52772")

        self.assertEqual(result, {"meals": [{"id": "52772"}]})
        mock_url_creator.assert_called_with("52772")
        mock_get.assert_called_with('http://testurl.com/lookup?id=52772')

    @patch('AdvancedSoftwareEngineering.src.core.shared.theMealDb.theMealDb.requests.get')
    def test_lookup_meal_details_by_id_handles_error(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        obj = TheMealDb()
        result = obj.lookup_meal_details_by_id("InvalidID")

        self.assertEqual(result, {})

    @patch('AdvancedSoftwareEngineering.src.core.shared.theMealDb.theMealDb.requests.get')
    def test_lookup_categories(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "categories": [{"name": "Category 1"}]}
        mock_get.return_value = mock_response

        obj = TheMealDb()
        result = obj.lookup_categories()

        self.assertEqual(result, {"categories": [{"name": "Category 1"}]})
        mock_get.assert_called_with(
            "https://www.themealdb.com/api/json/v1/1/categories.php")

    @patch('AdvancedSoftwareEngineering.src.core.shared.theMealDb.theMealDb.requests.get')
    def test_lookup_categories_handles_error(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        obj = TheMealDb()
        result = obj.lookup_categories()

        self.assertEqual(result, {})
