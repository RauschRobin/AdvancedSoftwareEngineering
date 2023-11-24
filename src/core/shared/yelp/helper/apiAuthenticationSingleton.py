from threading import Lock

import requests

from ....shared.YamlFetcher.YamlFetcher import YamlFetcher

# Singleton Pattern
# Thread save singleton


class ApiAuthenticationSingletonMeta(type):
    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class ApiAuthenticationSingleton(metaclass=ApiAuthenticationSingletonMeta):
    def __init__(self) -> None:
        # "bYSsCZNRkZrpu2FDmwIQbKZO8a9dSIUbQLNNB3ZKNE6GLl2-xguUmfhBunTJmpmJkvV8zbl_Wg-G7MI76OXOBeOSgueurc-ZsbX5SoaQFny3B3URu9wHBcpNzDdBZXYx"
        self.token = YamlFetcher.fetch("yelp", "API_Keys.yaml")

    def try_credentials(self) -> bool:
        response = requests.get(
            "https://api.yelp.com/v3/businesses/search?location=NYC&sort_by=best_match&limit=1",
            headers={
                'Authorization': f'Bearer {self.token}',
            }
        )
        return response.status_code == 200

    def get_headers(self) -> dict[str, str]:
        return {
            'Authorization': f'Bearer {self.token}',
        }
