import requests

class Maps:
    def __init__(self, maps_api_key):
        self.maps_api_key = maps_api_key
        
    # def get_nearby_restaurants(self, location, radius=6000, keyword='restaurant'):
    #     base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    #     params = {
    #         'location': location,
    #         'radius': radius,
    #         'type': keyword,
    #         'key': self.maps_api_key,
    #     }

    #     response = requests.get(base_url, params=params)
    #     print(response)
    #     results = response.json().get('results', [])

    #     print(results)
    #     return results
    
    def get_nearby_restaurants(self, location, radius=1000, keyword='restaurant'):
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


if __name__ == "__main__":
    myobj = Maps('AIzaSyA7chC-01o61wlNkzdLbb5hRLyVZTqNKc0')
    location = "49.03843923727726, 9.094928563014196"
    locations = myobj.get_nearby_restaurants(location)
