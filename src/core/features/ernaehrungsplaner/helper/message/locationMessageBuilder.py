from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

from .sentence import Sentence


class LocationBuilder(ABC):
    @property
    @abstractmethod
    def sentence(self) -> None:
        pass

class LocationMessageBuilder(LocationBuilder):
    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object,
        which is used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._sentence = Sentence()
