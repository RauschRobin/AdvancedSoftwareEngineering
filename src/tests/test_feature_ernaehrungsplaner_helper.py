import datetime
import json

from ..core.features.ernaehrungsplaner.helper.dinnerHelper import DinnerHelper

from ..core.features.ernaehrungsplaner.helper.lunchbreakHelper import LunchbreakHelper
from ..core.features.ernaehrungsplaner.helper.message.sentence import Sentence
from ..core.features.ernaehrungsplaner.helper.message.lunchbreakMessageBuilder import LunchbreakMessageBuilder
from ..core.features.ernaehrungsplaner.helper.message.dinnerMessageBuilder import DinnerMessageBuilder

from ..core.shared.rapla.rapla import Rapla
from ..core.shared.rapla.DateParser import DateParser as dp


# Test the dinner message builder
def test_dinner_message_builder():
    builder = DinnerMessageBuilder()

    builder.add_meal_name("Spaghetti Carbonara")
    builder.add_meal_category("Italienische Küche")
    builder.add_meal_to_buy_ingredients(["Speck", "Eier", "Parmesan"])

    sentence = builder.sentence.get_all()

    expected_sentence = "Du kannst heute Spaghetti Carbonara kochen. " \
                        "Das essen gehört zur Kategorie Italienische Küche. " \
                        "Für dieses Gericht musst du noch Speck, Eier und Parmesan kaufen"

    assert str(sentence) == expected_sentence


def test_dinner_message_builder_reset():
    builder = DinnerMessageBuilder()

    builder.add_meal_name("Spaghetti Carbonara")

    builder.reset()
    sentence = builder.sentence.get_all()

    assert str(sentence) == ""


# test the lunchbreak message builder
def test_lunchbreak_message_builder():
    builder = LunchbreakMessageBuilder()

    builder.add_current_time(12, 30)
    builder.add_lunchbreak_duration_in_minutes(60)
    builder.add_name_of_the_restaurant("Bella Italia")
    builder.add_restaurant_adress("Main Street", "Stuttgart")

    sentence = builder.sentence.get_all()

    expected_sentence = "Es ist 12:30. Du hast 60 Minuten Mittagspause. " \
                        "Du kannst heute im Restaurant Bella Italia essen gehen. " \
                        "Die Adresse ist Main Street in Stuttgart"

    assert str(sentence) == expected_sentence


def test_lunchbreak_message_builder_reset():
    builder = LunchbreakMessageBuilder()

    builder.add_current_time(12, 30)
    builder.reset()
    sentence = builder.sentence.get_all()

    assert str(sentence) == ""


# Test the Sentence Class
def test_initialization():
    sentence = Sentence()
    assert sentence.sentences == []


def test_adding_sentences():
    sentence = Sentence()
    sentence.add("Hello")
    sentence.add("World")
    assert sentence.sentences == ["Hello", "World"]


def test_get_all_sentences():
    sentence = Sentence()
    sentence.add("Hello")
    sentence.add("World")
    assert sentence.get_all() == "Hello. World"


# test dinner helper
def test_check_which_ingredients_needed():
    dinner = DinnerHelper()
    your_meal = {
        "strIngredient1": "Tomato",
        "strIngredient2": "Cheese",
    }

    expected_ingredients = ["Tomato", "Cheese"]
    ingredients = dinner.check_which_ingredients_needed(your_meal)

    assert ingredients == expected_ingredients, "The ingredients list does not match the expected outcome"


def test_check_which_ingredients_are_at_home():
    dinner = DinnerHelper()
    inventory_objects = {
        "item1": {"Item": "Tomato"},
        "item2": {"Item": "Cheese"},
        "item3": {"Item": "Basil"}
    }

    # Expected outcome
    expected_ingredients = ["Tomato", "Cheese", "Basil"]

    # Test
    ingredients = dinner.check_which_ingredients_are_at_home(inventory_objects)

    # Assert
    assert ingredients == expected_ingredients, "The ingredients list does not match the expected outcome"


# test lunchbreak helper
def test_is_businesses_not_none_with_non_empty_list():
    # Test with a non-empty list
    businesses = {"businesses": ["business1", "business2"]}
    lunchbreak = LunchbreakHelper()
    assert lunchbreak.is_businesses_not_none(businesses) == True


def test_is_businesses_not_none_with_empty_list():
    # Test with an empty list
    businesses = {"businesses": []}
    lunchbreak = LunchbreakHelper()
    assert lunchbreak.is_businesses_not_none(businesses) == False
