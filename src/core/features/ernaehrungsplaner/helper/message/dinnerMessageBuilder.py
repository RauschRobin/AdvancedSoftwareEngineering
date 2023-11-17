from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

from .sentence import Sentence1


class DinnerBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def sentence(self) -> None:
        pass

    @abstractmethod
    def add_meal_name(self, name) -> None:
        '''Add meal name

        Pramaters: name (string)
        Returns: None
        '''
        pass

    @abstractmethod
    def add_meal_category(self, category) -> None:
        '''Add category 

        Pramaters: category (string)
        Returns: None
        '''
        pass

    @abstractmethod
    def add_meal_to_buy_ingredients(self, missing_ingredients) -> None:
        '''Add ingredients to buy

        Pramaters: missing_ingredients (string)
        Returns: None
        '''
        pass


class SuccessDinnerMessageBuilder(DinnerBuilder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._sentence = Sentence1()

    @property
    def sentence(self) -> Sentence1:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        sentence = self._sentence
        self.reset()
        return sentence

    def add_meal_name(self, name) -> None:
        self._sentence.add(f"Du kannst heute {name} kochen")

    def add_meal_category(self, category) -> None:
        self._sentence.add(f"Das essen gehört zur Kategorie {category}")

    def add_meal_to_buy_ingredients(self, missing_ingredients) -> None:
        if len(missing_ingredients) > 1:
            # Join all but the last item with comma, then add " und " and the last item
            comma_separated_string = ', '.join(
                missing_ingredients[:-1]) + ' und ' + missing_ingredients[-1]
        else:
            # If there's only one item in the list, just use that item
            comma_separated_string = missing_ingredients[0]

        self._sentence.add(
            f"Für dieses Gericht musst du noch {comma_separated_string} kaufen")
