from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

from .sentence import Sentence1


class FailureLunchbreakBuilder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    """

    @property
    @abstractmethod
    def sentence(self) -> None:
        pass

    @abstractmethod
    def add_failure(self) -> None:
        '''Add failure text

        Pramaters: None
        Returns: None
        '''
        pass


class LunchbreakFailureMessageBuilder(FailureLunchbreakBuilder):
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

    def add_failure(self) -> None:
        self._sentence.add(
            f"Ich habe kein Restaurant für dich in der Nähe gefunden.")
