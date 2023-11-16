from ..core.shared.WeatherAPI.weather import Weather


def test_get_weather_data():
    '''
    Tests if weather data can be requested by API.

    Parameters: none
    Returns: test_succeded (Boolean)
    '''
    try:
        singleton = Weather()
        current_weather_data = singleton.get_weather_of_date()
        
        assert current_weather_data != ""
    except:
        assert False

    
def test_get_weather_is_up_to_date():
    '''
    Tests if weather data is up to date.

    Parameters: none
    Returns: test_succeded (Boolean)
    '''
    try:
        singleton = Weather()
        singleton.get_weather_of_date()
        newsingleton = Weather()
        
        assert newsingleton.is_weather_data_up_to_date()
    except:
        assert False