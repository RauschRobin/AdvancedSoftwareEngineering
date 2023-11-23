import requests
from ...shared.YamlFetcher.YamlFetcher import YamlFetcher

class Maps:
    def __init__(self):
        self.maps_api_key = YamlFetcher.fetch("maps", "API_Keys.yaml")
        
    def get_nearby_places(self, location, radius=2000, keyword='restaurant'):
        '''
        Selects places nearby a specific location, within a certain radius(default: 2000).
        Keywords can be modified. By default it is 'restaurant'

        Parameters: location, radius, keywords
        Returns: places (list)
        '''
        base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
        
        params = {
            'key': self.maps_api_key,
            'location': location,
            'radius': radius,
            'keyword': keyword,
        }

        try:
            response = requests.get(base_url, params=params)
            data = response.json()
            print(data)
            if response.status_code == 200 and data['status'] == 'OK':
                restaurants = []

                for place in data['results']:
                    name = place.get('name', 'N/A')
                    address = place.get('vicinity', 'N/A')
                    restaurants.append({'name': name, 'address': address})

                return restaurants
            else:
                print(f"Error1: {data['status']}")
        except Exception as e:
            print(f"Error2: {e}")


# if __name__ == "__main__":
#     myobj = Maps('API_KEY')
#     location = "49.03843923727726, 9.094928563014196" # Example Coordinates of Bönnigheim
#     locations = myobj.get_nearby_restaurants(location)
