from ..core.shared.theMealDb.helper.urlCreator import (ConcreteSearchByMeal, ConcreteListAllMealsByFirstLetter,
                                                       ConcreteLookupMealDetailsById, SearchByMealURLCreator,
                                                       ListAllMealsByFirstLetterURLCreator, LookupMealDetailsByIdURLCreator)


# Test ConcreteSearchByMeal
def test_concrete_search_by_meal():
    obj = ConcreteSearchByMeal()
    assert obj.base_url() == "https://www.themealdb.com/api/json/v1/1/search.php"
    assert obj.search_param("chicken") == "s=chicken"


# Test ConcreteListAllMealsByFirstLetter
def test_concrete_list_all_meals_by_first_letter():
    obj = ConcreteListAllMealsByFirstLetter()
    assert obj.base_url() == "https://www.themealdb.com/api/json/v1/1/search.php"
    assert obj.search_param("c") == "f=c"


# Test ConcreteLookupMealDetailsById
def test_concrete_lookup_meal_details_by_id():
    obj = ConcreteLookupMealDetailsById()
    assert obj.base_url() == "https://www.themealdb.com/api/json/v1/1/lookup.php"
    assert obj.search_param(52772) == "i=52772"


# Test SearchByMealURLCreator
def test_search_by_meal_url_creator():
    creator = SearchByMealURLCreator("chicken")
    assert isinstance(creator.factory_method(), ConcreteSearchByMeal)
    assert creator.construct_url(
    ) == "https://www.themealdb.com/api/json/v1/1/search.php?s=chicken"


# Test ListAllMealsByFirstLetterURLCreator
def test_list_all_meals_by_first_letter_url_creator():
    creator = ListAllMealsByFirstLetterURLCreator("c")
    assert isinstance(creator.factory_method(),
                      ConcreteListAllMealsByFirstLetter)
    assert creator.construct_url() == "https://www.themealdb.com/api/json/v1/1/search.php?f=c"


# Test LookupMealDetailsByIdURLCreator
def test_lookup_meal_details_by_id_url_creator():
    creator = LookupMealDetailsByIdURLCreator(52772)
    assert isinstance(creator.factory_method(), ConcreteLookupMealDetailsById)
    assert creator.construct_url(
    ) == "https://www.themealdb.com/api/json/v1/1/lookup.php?i=52772"
