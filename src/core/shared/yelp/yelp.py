


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

    def getRestaurantsByLocationLimit(self, location: str, limit: int):
        '''
        Returns a list of restaurants near that location (return limited)
        
        Input: location e.g. "New York City", "NYC"; limit: 5   

        Output: { "businesses": [{ obejct}]}       
        '''
        success: bool = self.api.try_credentials()

        if(success):
            params = {
                "location": location,
                "limit": limit
            }

            self.director.build_search(params)
            params = self.builder.params

            base_url = "https://api.yelp.com/v3/businesses/search"
            request_url = f"{base_url}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"

            response = requests.get(request_url, headers=self.api.get_headers())
            if response.status_code == 200:
                return response.json()
            
            else: 
                return {}

        else:
            print("Error while connecting to yelp api.")

    def getRestaurantsByLocationLimitRadius(self, location:str, limit:str, radius:int):
        '''
        Returns a list of restaurants near that location with a given radius (return limited)
        
        Input: location e.g. "New York City", "NYC"; limit: 5; radius: 1000 (Meter, max 40.000 m)  
        
        Output: { "businesses": [{ obejct}]}       
        '''
        success: bool = self.api.try_credentials()

        if(success):
            params = {
                "location": location,
                "radius": radius,
                "limit": limit
            }

            self.director.build_search(params)
            params = self.builder.params

            base_url = "https://api.yelp.com/v3/businesses/search"
            request_url = f"{base_url}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"

            response = requests.get(request_url, headers=self.api.get_headers())
            if response.status_code == 200:
                return response.json()
            
            else: 
                return {}

        else:
            print("Error while connecting to yelp api.")
    
    def getRestaurantsByLocationLimitRadiusCategories(self, location: str, limit: int, radius: int, categories):
        '''
        Returns a list of restaurants near that location with a given radius and categories (return limited)

        Input:

        location e.g. "New York City", "NYC"; 
        limit: 5; radius: 1000 (Meter, max 40.000 m); 
        categories: Comma delimited e.g. "bars,french"
        ------
        Output: { "businesses": [{ obejct}]}       
        '''
        success: bool = self.api.try_credentials()

        if(success):
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

            response = requests.get(request_url, headers=self.api.get_headers())
            if response.status_code == 200:
                return response.json()
            
            else: 
                return {}

        else:
            print("Error while connecting to yelp api.")






yelp = Yelp()
yelp.getRestaurantsByLocationLimitRadiusCategories("NYC", 1, 1000, "bars,french")











        