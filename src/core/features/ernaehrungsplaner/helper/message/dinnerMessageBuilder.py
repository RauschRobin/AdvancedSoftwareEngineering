from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

from .sentence import Sentence


class DinnerBuilder(ABC):
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


class DinnerMessageBuilder(DinnerBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._sentence = Sentence()

    @property
    def sentence(self) -> Sentence:
        sentence = self._sentence
        self.reset()
        return sentence

    def add_meal_name(self, name) -> None:
        self._sentence.add(f"Du kannst heute {name} kochen")

    def add_meal_category(self, category) -> None:
        self._sentence.add(f"Das essen gehört zur Kategorie {category}")

    def add_meal_to_buy_ingredients(self, missing_ingredients) -> None:
        if len(missing_ingredients) > 1:
            # Join all but last item with comma, then add " und " and last item
            comma_separated_string = ', '.join(
                missing_ingredients[:-1]) + ' und ' + missing_ingredients[-1]
        else:
            # If there's only one item in the list, use that item
            comma_separated_string = missing_ingredients[0]

        self._sentence.add(
            f"Für dieses Gericht musst du noch {comma_separated_string} kaufen")
