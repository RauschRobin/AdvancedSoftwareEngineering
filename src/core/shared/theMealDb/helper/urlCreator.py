from abc import ABC, abstractmethod


class URLCreator(ABC):

    def __init__(self, param: str | int | None):
        self.param = param

    @abstractmethod
    def factory_method(self):
        pass

    def construct_url(self) -> str:
        """
        This method uses the URLTheMealDb object returned by the factory method.
        It constructs the URL using the base URL and the search parameter provided
        by the URLTheMealDb.
        """

        meal = self.factory_method()
        return f"{meal.base_url()}?{meal.search_param(self.param)}"


# Use this methods to get the right URL
class SearchByMealURLCreator(URLCreator):
    """
    Concrete creator for searching by meal name.
    """

    def factory_method(self):
        return ConcreteSearchByMeal()


class ListAllMealsByFirstLetterURLCreator(URLCreator):
    """
    Concrete creator for listing all meals by the first letter.
    """

    def factory_method(self):
        return ConcreteListAllMealsByFirstLetter()


class LookupMealDetailsByIdURLCreator(URLCreator):
    """
    Concrete creator for meal details by id.
    """

    def factory_method(self):
        return ConcreteLookupMealDetailsById()


#
class URLTheMealDb(ABC):
    """
    The URLTheMealDb interface declares the operations that all concrete URL meals
    must implement.
    """

    @abstractmethod
    def base_url(self) -> str:
        pass

    @abstractmethod
    def search_param(self, param: str) -> str:
        pass


# Setup the concrete implementation
class ConcreteSearchByMeal(URLTheMealDb):
    """
    Concrete URL meal for searching by meal name.
    """

    def base_url(self) -> str:
        return "https://www.themealdb.com/api/json/v1/1/search.php"

    def search_param(self, param: str) -> str:
        return f"s={param}"


class ConcreteListAllMealsByFirstLetter(URLTheMealDb):
    """
    Concrete URL meal for listing all meals by the first letter.
    """

    def base_url(self) -> str:
        return "https://www.themealdb.com/api/json/v1/1/search.php"

    def search_param(self, param: str) -> str:
        return f"f={param}"


class ConcreteLookupMealDetailsById(URLTheMealDb):
    """
    Concrete URL meal for listing all meals by the id
    """

    def base_url(self) -> str:
        return "https://www.themealdb.com/api/json/v1/1/lookup.php"

    def search_param(self, param: int) -> str:
        if param is not None:
            return f"i={param}"
