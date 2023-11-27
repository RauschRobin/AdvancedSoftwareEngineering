import unittest
from unittest.mock import patch, Mock

from ..core.shared.yelp.yelp import Yelp


class TestYelp(unittest.TestCase):

    @patch('AdvancedSoftwareEngineering.src.core.shared.yelp.yelp.requests.get')
    def test_get_restaurants_by_location_limit(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "businesses": [{"name": "Test Restaurant"}]}
        mock_get.return_value = mock_response

        yelp = Yelp()
        result = yelp.get_restaurants_by_location_limit("NYC", 5)

        self.assertEqual(result, {"businesses": [{"name": "Test Restaurant"}]})

        mock_get.assert_called_with(
            "https://api.yelp.com/v3/businesses/search?location=NYC&limit=5",
            headers=yelp.api.get_headers()
        )

    @patch('AdvancedSoftwareEngineering.src.core.shared.yelp.yelp.requests.get')
    def test_restaurants_by_location_limit_radius(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "businesses": [{"name": "Test Restaurant"}]}
        mock_get.return_value = mock_response

        yelp = Yelp()
        result = yelp.get_restaurants_by_location_limit_radius(
            "NYC", "5", 1000)

        self.assertEqual(result, {"businesses": [{"name": "Test Restaurant"}]})

        expected_url = "https://api.yelp.com/v3/businesses/search?location=NYC&radius=1000&limit=5"
        mock_get.assert_called_with(
            expected_url, headers=yelp.api.get_headers())

    @patch('AdvancedSoftwareEngineering.src.core.shared.yelp.yelp.requests.get')
    def test_get_restaurants_by_location_limit_radius_categories(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "businesses": [{"name": "Test Restaurant"}]}
        mock_get.return_value = mock_response

        yelp = Yelp()
        result = yelp.get_restaurants_by_location_limit_radius_categories(
            "NYC", "5", 1000, "bars,french")

        self.assertEqual(result, {"businesses": [{"name": "Test Restaurant"}]})

        expected_url = "https://api.yelp.com/v3/businesses/search?location=NYC&radius=1000&limit=5&categories=bars,french"
        mock_get.assert_called_with(
            expected_url, headers=yelp.api.get_headers())

    @patch('AdvancedSoftwareEngineering.src.core.shared.yelp.yelp.requests.get')
    def test_get_restaurants_by_location_limit_radius_categories_price(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "businesses": [{"name": "Test Restaurant"}]}
        mock_get.return_value = mock_response

        yelp = Yelp()
        result = yelp.get_restaurants_by_location_limit_radius_categories_price(
            "NYC", "5", 1000, "bars,french", 1)

        self.assertEqual(result, {"businesses": [{"name": "Test Restaurant"}]})

        expected_url = "https://api.yelp.com/v3/businesses/search?location=NYC&radius=1000&limit=5&categories=bars,french&price=1"
        mock_get.assert_called_with(
            expected_url, headers=yelp.api.get_headers())


if __name__ == '__main__':
    unittest.main()
