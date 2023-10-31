from .builder import Builder


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_search(self, search_params: dict) -> None:
        for key, value in search_params.items():
            self.builder.add_param(key, value)