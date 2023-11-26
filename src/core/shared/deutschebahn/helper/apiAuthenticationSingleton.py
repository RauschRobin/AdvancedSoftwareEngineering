import os
from dotenv import load_dotenv
import requests

from threading import Lock
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
        load_dotenv()
        self.client_id = os.environ("DEUTSCHEBAHN_CLIENT_ID")
        self.client_secret = os.environ("DEUTSCHEBAHN_SECRET")

    def test_credentials(self) -> bool:
        response = requests.get(
            "https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/station/BLS",
            headers={
                "DB-Client-Id": self.client_id,
                "DB-Api-Key": self.client_secret,
            }
        )
        return response.status_code == 200

    def get_headers(self) -> dict[str, str]:
        return {
            "DB-Client-Id": self.client_id,
            "DB-Api-Key": self.client_secret,
        }
