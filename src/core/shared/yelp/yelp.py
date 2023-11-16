import requests
from .helper.yelpSearchRequestBuilder import YelpSearchRequestBuilder
from .helper.director import Director
from .helper.apiAuthenticationSingleton import ApiAuthenticationSingleton


class Yelp:
    def __init__(self) -> None:
        self.api = ApiAuthenticationSingleton()
        self.director = Director()
        self.builder = YelpSearchRequestBuilder()
        self.director.builder = self.builder

    def get_restaurants_by_location_limit(self, location: str, limit: int):
        '''Returns a list of restaurants near that location (return limited)

        Parameters: location e.g. "New York City", "NYC"; limit: 5   
        Returns: { "businesses": [{ obejct}]}       
        '''
        success: bool = self.api.try_credentials()

        if (success):
            params = {
                "location": location,
                "limit": limit
            }

            self.director.build_search(params)
            params = self.builder.params

            base_url = "https://api.yelp.com/v3/businesses/search"
            request_url = f"{base_url}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"

            response = requests.get(
                request_url, headers=self.api.get_headers())
            if response.status_code == 200:
                return response.json()

            else:
                return {}

        else:
            print("Error while connecting to yelp api.")

    def get_restaurants_by_location_limit_radius(self, location: str, limit: str, radius: int):
        '''Returns a list of restaurants near that location with a given radius (return limited)

        Parameters: location e.g. "New York City", "NYC"; limit: 5; radius: 1000 (Meter, max 40.000 m)  
        Returns: { "businesses": [{ obejct}]}       
        '''
        success: bool = self.api.try_credentials()

        if (success):
            params = {
                "location": location,
                "radius": radius,
                "limit": limit
            }

            self.director.build_search(params)
            params = self.builder.params

            base_url = "https://api.yelp.com/v3/businesses/search"
            request_url = f"{base_url}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"

            response = requests.get(
                request_url, headers=self.api.get_headers())
            if response.status_code == 200:
                return response.json()

            else:
                return {}

        else:
            print("Error while connecting to yelp api.")

    def get_restaurants_by_location_limit_radius_categories(self, location: str, limit: int, radius: int, categories: str):
        '''Returns a list of restaurants near that location with a given radius and categories (return limited)

        Parameters:blocation e.g. "New York City", "NYC"; limit: 5; radius: 1000 (Meter, max 40.000 m); categories: Comma delimited e.g. "bars,french"
        Returns: { "businesses": [{ obejct}]}       
        '''
        success: bool = self.api.try_credentials()

        if (success):
            params = {
                "location": location,
                "radius": radius,
                "limit": limit,
                "categories": categories
            }

            self.director.build_search(params)
            params = self.builder.params

            base_url = "https://api.yelp.com/v3/businesses/search"
            request_url = f"{base_url}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"

            response = requests.get(
                request_url, headers=self.api.get_headers())
            if response.status_code == 200:
                return response.json()

            else:
                return {}

        else:
            print("Error while connecting to yelp api.")

    def get_restaurants_by_location_limit_radius_categories_price(self, location: str, limit: int, radius: int, categories: str, price: int):
        '''Returns a list of restaurants near that location with a given radius, categories and price (return limited)

        Parameters:blocation e.g. "New York City", "NYC"; limit: 5; radius: 1000 (Meter, max 40.000 m); categories: Comma delimited e.g. "bars,french", price: 1 = $, 2 = $$, 3 = $$$, 4 = $$$$ (cheap to expensive)
        Returns: { "businesses": [{ obejct}]}       
        '''
        success: bool = self.api.try_credentials()

        if (success):
            params = {
                "location": location,
                "radius": radius,
                "limit": limit,
                "categories": categories,
                "price": price
            }

            self.director.build_search(params)
            params = self.builder.params

            base_url = "https://api.yelp.com/v3/businesses/search"
            request_url = f"{base_url}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"

            response = requests.get(
                request_url, headers=self.api.get_headers())
            if response.status_code == 200:
                return response.json()

            else:
                return {}

        else:
            print("Error while connecting to yelp api.")
