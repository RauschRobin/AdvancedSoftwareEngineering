import unittest

from ..core.shared.theMealDb.helper.urlCreator import ListAllMealsByFirstLetterURLCreator, LookupMealDetailsByIdURLCreator, SearchByMealURLCreator


class TestURLCreators(unittest.TestCase):

    def test_search_by_meal_url(self):
        creator = SearchByMealURLCreator("Chicken")
        url = creator.construct_url()
        self.assertEqual(
            url, "https://www.themealdb.com/api/json/v1/1/search.php?s=Chicken")

    def test_list_all_meals_by_first_letter_url(self):
        creator = ListAllMealsByFirstLetterURLCreator("C")
        url = creator.construct_url()
        self.assertEqual(
            url, "https://www.themealdb.com/api/json/v1/1/search.php?f=C")

    def test_lookup_meal_details_by_id_url(self):
        creator = LookupMealDetailsByIdURLCreator(52772)
        url = creator.construct_url()
        self.assertEqual(
            url, "https://www.themealdb.com/api/json/v1/1/lookup.php?i=52772")


if __name__ == '__main__':
    unittest.main()
