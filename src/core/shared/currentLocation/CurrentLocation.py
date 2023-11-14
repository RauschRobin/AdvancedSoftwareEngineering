import time


class CurrentLocation:
    """Gets the current location
    """

    def __init__(self) -> None:
        pass

    def get_location(self) -> str:
        """Returns the location based on the current time
        
        Returns: String
        """
        t = time.localtime()
        current_time = time.strftime("%H", t)
        if (int(current_time) > 7 or int(current_time) < 16):
            return "Uni"
        else:
            return "Home"
