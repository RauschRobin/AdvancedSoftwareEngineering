import requests
from ...shared.YamlFetcher.YamlFetcher import YamlFetcher
import os
import googlemaps
from dotenv import load_dotenv

class Maps:
    def __init__(self):
        load_dotenv()
        self.maps_api_key = os.getenv('MAPS_SECRET')
        
    def get_nearby_places(self, location=None, radius=2000, keyword='restaurant'):
        '''
        Selects places nearby a specific location, within a certain radius(default: 2000).
        Keywords can be modified. By default it is 'restaurant'
        Limit of locations is set to 3.

        Parameters: location, radius, keywords
        Returns: places (string[])
        '''

        # Replace 'YOUR_API_KEY' with your actual API key
        gmaps = googlemaps.Client(key=self.maps_api_key)

        # Perform a Places API nearby search
        if location:
            places_result = gmaps.places(query=f'{keyword} in {location}', radius=radius)
        else:
            # Default location are coordinates of Stuttgart DHBW Fakult#t Technik
            latitude = 48.78308282048639
            longitude = 9.165828554195217

            places_result = gmaps.places_nearby(location=(latitude, longitude), radius=radius, type=keyword)

        # Prepare a list to store formatted information about each place
        formatted_places = []

        # Format information about each place
        for place in places_result['results'][:3]:
            formatted_place = {
                "Name": place['name'],
                "Address": place.get('vicinity', 'N/A'),
                "Rating": place.get('rating', 'N/A')
            }
            formatted_places.append(formatted_place)

        return formatted_places

