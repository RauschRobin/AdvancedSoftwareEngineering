from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

from .sentence import Sentence


class LunchbreakBuilder(ABC):
    @property
    @abstractmethod
    def sentence(self) -> None:
        pass

    @abstractmethod
    def add_current_time(self, hour, minute) -> None:
        '''Add current time to the sentence

        Pramaters: time (string) e.g. "12:45"
        Returns: None
        '''
        pass

    @abstractmethod
    def add_lunchbreak_duration_in_minutes(self, duration) -> None:
        '''Add break duration in minutes to the sentence

        Pramaters: duration (int)
        Returns: None
        '''
        pass

    @abstractmethod
    def add_name_of_the_restaurant(self, name) -> None:
        '''Add the name of the restaurant to the sentence

        Pramaters: name (string)
        Returns: None
        '''
        pass

    @abstractmethod
    def add_restaurant_adress(self, street, city) -> None:
        '''Add the address and city to the sentence

        Pramaters: street (string), city (string)
        Returns: None
        '''
        pass


class LunchbreakMessageBuilder(LunchbreakBuilder):
    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object,
        which is used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._sentence = Sentence()

    @property
    def sentence(self) -> Sentence:
        sentence = self._sentence
        self.reset()
        return sentence

    def add_current_time(self, hour, minute) -> None:
        # Ensures hour is in two-digit format
        formatted_hour_hh = f"{hour:02d}"
        # Ensures minute is in two-digit format
        formatted_minute_mm = f"{minute:02d}"
        self._sentence.add(
            f"Es ist {str(formatted_hour_hh)}:{str(formatted_minute_mm)}")

    def add_lunchbreak_duration_in_minutes(self, duration: int) -> None:
        self._sentence.add(f"Du hast {str(duration)} Minuten Mittagspause")

    def add_name_of_the_restaurant(self, name) -> None:
        self._sentence.add(
            f"Du kannst heute im Restaurant {name} essen gehen")

    def add_restaurant_adress(self, street, city) -> None:
        self._sentence.add(
            f"Die Adresse ist {street} in {city}")
