import datetime


class CurrentLocation:
    """Gets the current location
    """

    def __init__(self) -> None:
        pass

    def get_location_adress(self) -> str:
        """Returns the location adress based on the current time

        Returns: String
        """

        # This simulates the user location and can be changed later wit google maps api
        now = datetime.datetime.now()
        if (now.hour > 7 and now.hour < 16):
            return "Stuttgart"
        else:
            return "Ludwigsburg"
