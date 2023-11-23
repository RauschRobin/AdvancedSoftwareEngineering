import datetime
from ..core.shared.currentLocation.CurrentLocation import CurrentLocation


def test_current_location():
    currentLocation = CurrentLocation()
    current_address = currentLocation.get_location_adress()

    now = datetime.datetime.now()
    expected_address = "Stuttgart" if (
        7 < now.hour < 16) else "Ludwigsburg"

    assert current_address == expected_address, "Address returned is not as expected"
