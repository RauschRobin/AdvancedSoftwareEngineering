import datetime
import unittest.mock
import unittest
import pytest

from ..core.communication.voice_output import VoiceOutput

from ..core.features.ernaehrungsplaner.ernaehrungsplaner import Ernaehrungsplaner


@pytest.fixture
def voice_output_mock():
    return unittest.mock.Mock()


@pytest.fixture
def ernaehrungsplaner_instance(voice_output_mock):
    return Ernaehrungsplaner(voice_output_mock)


def test_suggest_restaurant_for_lunchbreak_lunchtime_found(ernaehrungsplaner_instance):
    # Mocken Sie lunchbreak.is_time_for_lunchbreak, damit es True zurückgibt
    ernaehrungsplaner_instance.lunchbreak.is_time_for_lunchbreak = unittest.mock.Mock(
        return_value=True)

    # Mocken Sie die yelp.get_restaurants_by_location_limit_radius_categories-Methode, damit sie eine gültige Antwort zurückgibt
    ernaehrungsplaner_instance.yelp.get_restaurants_by_location_limit_radius_categories = unittest.mock.Mock(return_value={
        "businesses": [{
            "name": "Restaurant XYZ",
            "location": {
                "display_address": ["Straße 123", "Stadt"]
            }
        }]
    })

    # Mocken Sie das aktuelle Datum und die Uhrzeit
    custom_time = datetime.datetime(2023, 11, 30, 21, 24)
    with unittest.mock.patch('datetime.datetime') as mock_datetime:
        mock_datetime.now.return_value = custom_time

        # Rufen Sie die Methode auf
        ernaehrungsplaner_instance.suggest_restaurant_for_lunchbreak()

    # Überprüfen Sie, ob die voice_output.add_message-Methode mit der erwarteten Nachricht aufgerufen wurde
    ernaehrungsplaner_instance.voice_output.add_message.assert_called_once_with(
        "Es ist 21:24. Du kannst heute im Restaurant Restaurant XYZ essen gehen. Die Adresse ist Straße 123 in Stadt")


def test_suggest_restaurant_for_lunchbreak_lunchtime_no_restaurant(ernaehrungsplaner_instance):
    # Mocken Sie lunchbreak.is_time_for_lunchbreak, damit es True zurückgibt
    ernaehrungsplaner_instance.lunchbreak.is_time_for_lunchbreak = unittest.mock.Mock(
        return_value=True)

    # Mocken Sie die yelp.get_restaurants_by_location_limit_radius_categories-Methode, damit sie eine leere Antwort zurückgibt
    ernaehrungsplaner_instance.yelp.get_restaurants_by_location_limit_radius_categories = unittest.mock.Mock(return_value={
        "businesses": []
    })

    # Rufen Sie die Methode auf
    ernaehrungsplaner_instance.suggest_restaurant_for_lunchbreak()

    # Überprüfen Sie, ob die voice_output.add_message-Methode mit der erwarteten Nachricht aufgerufen wurde
    ernaehrungsplaner_instance.voice_output.add_message.assert_called_once_with(
        "Ich habe leider kein passendes Restaurant in der Nähe gefunden.")


def test_cook_something_different(ernaehrungsplaner_instance):
    # Mocken Sie die DinnerHelper.find_random_meal-Methode, damit sie ein festes Gericht zurückgibt
    ernaehrungsplaner_instance.dinner.find_random_meal = unittest.mock.Mock(
        return_value="Spaghetti Carbonara")

    # Rufen Sie die Methode cook_something_different auf
    ernaehrungsplaner_instance.cook_something_different()

    # Überprüfen Sie, ob die voice_output.add_message-Methode mit der erwarteten Nachricht aufgerufen wurde
    ernaehrungsplaner_instance.voice_output.add_message.assert_called_once_with(
        "Du kannst stattdessen Spaghetti Carbonara kochen.")


def test_ingredients_at_home_to_cook():
    pass


def test_generate_shopping_list_for_meal():
    pass


def test_chooseRestaurantWithKeyword(ernaehrungsplaner_instance):
    ernaehrungsplaner_instance.chooseRestaurantWithKeyword("eins")
    restaurant_name = "nicht"
    if(ernaehrungsplaner_instance.selected_restaurant is None or ernaehrungsplaner_instance.selected_restaurant == {}):
        restaurant_name = "nicht"
    else:
        restaurant_name = ernaehrungsplaner_instance.selected_restaurant['name']    
    message = f'Restaurant {restaurant_name} ausgewählt'
    ernaehrungsplaner_instance.voice_output.add_message.assert_called_once_with(message)


def test_getRestaurantContact(ernaehrungsplaner_instance):
    ernaehrungsplaner_instance.selected_restaurant['name'] = "Spatzennest"
    ernaehrungsplaner_instance.selected_restaurant['phone'] = "0000"
    message = f"Die Telefonnummer von {ernaehrungsplaner_instance.selected_restaurant['name']} "
    message = message + f"lautet: {ernaehrungsplaner_instance.selected_restaurant['phone']}"
    ernaehrungsplaner_instance.getRestaurantContact()
    ernaehrungsplaner_instance.voice_output.add_message.assert_called_once_with(message)

def test_getRestaurantLocation(ernaehrungsplaner_instance):
    ernaehrungsplaner_instance.selected_restaurant['name'] = "Abrakadabra"
    loc_dict = {'zip_code' : '70151', 'city' : 'Stuttgart', 'address1' : "Leonhardstr 8"}
    ernaehrungsplaner_instance.selected_restaurant['location'] = loc_dict 
    message = f"Das Restaurant {ernaehrungsplaner_instance.selected_restaurant['name']} "
    message = message + f"befindet sich in {ernaehrungsplaner_instance.selected_restaurant['location']['zip_code']} "
    message = message + f"{ernaehrungsplaner_instance.selected_restaurant['location']['city']} in "
    message = message + f"{ernaehrungsplaner_instance.selected_restaurant['location']['address1']}"
    ernaehrungsplaner_instance.getRestaurantLocation()
    ernaehrungsplaner_instance.voice_output.add_message.assert_called_once_with(message)
