from threading import Lock

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
        self.client_id = "eaace190c7864a763aabef94bc7a9170"
        self.client_secret = "83060b5545efc7db0593f3974cde71ad"

    def test_credentials(self) -> bool:
        response = requests.get(
            "https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/station/BLS",
            headers={
                "DB-Api-Key": self.client_secret,
                "DB-Client-Id": self.client_id,
            }
        )
        return response.status_code == 200

    def get_headers(self) -> dict[str, str]:
        return {
            "DB-Api-Key": self.client_secret,
            "DB-Client-Id": self.client_id,
        }
