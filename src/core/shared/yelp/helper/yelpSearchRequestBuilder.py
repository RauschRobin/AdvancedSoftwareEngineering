
from .builder import Builder


class YelpSearchRequestBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._params = {}

    @property
    def params(self) -> dict:
        params = self._params.copy()
        self.reset()
        return params

    def add_param(self, key: str, value: str) -> None:
        self._params[key] = value