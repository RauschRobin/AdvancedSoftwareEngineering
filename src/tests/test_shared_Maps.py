from ..core.shared.Maps.maps import Maps

def test_get_food_places():
    '''
    Selects places nearby a specific location, within a certain radius(default: 2000).
        Tests search for food places in Stuttgart Stadtmitte.

        Parameters: none
        Returns: test_succeded (Boolean)
    '''
    maps_api = Maps()
    location = "48.7802284375507, 9.17955500617001"
    try:
        response = maps_api.get_nearby_places(location, keyword = 'food')
        assert response['status'] != ""
    except:
        assert False