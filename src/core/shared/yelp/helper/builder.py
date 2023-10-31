from abc import ABC, abstractmethod


class Builder(ABC):

    @property
    @abstractmethod
    def params(self) -> None:
        pass

    @abstractmethod
    def add_param(self, key: str, value: str) -> None:
        pass