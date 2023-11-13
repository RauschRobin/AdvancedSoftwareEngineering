import time


class CurrentLocation:
    """Gets the current location
    """

    def __init__(self) -> None:
        pass

    def get_location(self) -> str:
        t = time.localtime()
        current_time = time.strftime("%H", t)
        if (int(current_time) > 7 or int(current_time) < 16):
            return "Uni"
        else:
            return "Home"


ort = CurrentLocation()
ort.get_location()
print(type(ort))
#print(isinstance(ort, CurrentLocation))