import requests

from helper.urlCreator import SearchByMealURLCreator, ListAllMealsByFirstLetterURLCreator, LookupMealDetailsByIdURLCreator


class TheMealDb:
    def __init__(self):
        pass

    def search_meal_by_name(self, name: str):
        ''' Search a meal by name

        Parameters: name e.g. "Arrabiata"
        Returns: { meals: [objects]}
        '''

        creator = SearchByMealURLCreator(name)
        request_url = creator.construct_url()

        response = requests.get(
            request_url)
        if response.status_code == 200:
            return response.json()
        else:
            return {}

    def list_all_meals_by_first_letter(self, first_letter: str):
        ''' Search a meal by first letter

        Parameters: name e.g. "a"
        Returns: { meals: [objects]}
        '''
        creator = ListAllMealsByFirstLetterURLCreator(first_letter)
        request_url = creator.construct_url()

        response = requests.get(
            request_url)
        if response.status_code == 200:
            return response.json()
        else:
            return {}

    def lookup_meal_details_by_id(self, first_letter: str):
        ''' Search a meal by id

        Parameters: name e.g. 52772
        Returns: { meals: [objects]}
        '''
        creator = LookupMealDetailsByIdURLCreator(first_letter)
        request_url = creator.construct_url()

        response = requests.get(
            request_url)
        if response.status_code == 200:
            return response.json()
        else:
            return {}

    def lookup_single_random_meal(self):
        ''' Find a single random meal

        Parameters: None
        Returns: { meals: [objects]}
        '''

        request_url = "https://www.themealdb.com/api/json/v1/1/random.php"

        response = requests.get(
            request_url)
        if response.status_code == 200:
            return response.json()
        else:
            return {}

    def lookup_categories(self):
        ''' Lookup all categories

        Parameters: None
        Returns: { categories: [objects]}
        '''

        request_url = "https://www.themealdb.com/api/json/v1/1/categories.php"

        response = requests.get(
            request_url)
        if response.status_code == 200:
            return response.json()
        else:
            return {}
