from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class LunchbreakBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def sentence(self) -> None:
        pass

    @abstractmethod
    def add_current_time(self, time) -> None:
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


class MessageBuilder(LunchbreakBuilder):
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

    def add_current_time(self, time) -> None:
        self._sentence.add(f"Es ist {time}")

    def add_lunchbreak_duration_in_minutes(self, duration: int) -> None:
        self._sentence.add(f"Du hast {str(duration)} Minuten Mittagspause")

    def add_name_of_the_restaurant(self, name) -> None:
        self._sentence.add(
            f"Du kannst heute im Restaurant {name} essen gehen")

    def add_restaurant_adress(self, street, city) -> None:
        self._sentence.add(
            f"Die Adresse ist {street} in {city}")


class Sentence1():
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated products. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.sentences = []

    def add(self, sentence: Any) -> None:
        self.sentences.append(sentence)

    def get_all(self):
        return '. '.join(self.sentences)

    def list_sentences(self) -> None:
        print(f"Combined sentences: {', '.join(self.sentences)}", end="")
