import os
from threading import Lock
from dotenv import load_dotenv

import requests

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
        load_dotenv()
        self.token = os.getenv("YELP_SECRET")

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
