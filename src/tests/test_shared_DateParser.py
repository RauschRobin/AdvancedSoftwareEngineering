import unittest
import datetime
import dateutil.relativedelta as rd
from ..core.shared.rapla.DateParser import DateParser as dp

class TestDateParser(unittest.TestCase):

    def test_get_current_calendar_week(self):
        result = dp.get_current_calendar_week()
        expected = datetime.datetime.now().isocalendar()[1]
        self.assertEqual(result, expected, "Error in get_current_calendar_week method")

    def test_get_calendar_week(self):
        result = dp.get_calendar_week(2023, 10, 26)
        expected = datetime.date(2023, 10, 26).isocalendar()[1]
        self.assertEqual(result, expected, "Error in get_calendar_week method")

    def test_get_week_day(self):
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        for i in range(7):
            result = dp.get_week_day(i)
            expected = days[i]
            self.assertEqual(result, expected, f"Error in get_week_day method for {expected}")

    def test_get_date_from_week(self):
        result = dp.get_date_from_week(2023, 43, 3)

        # Calculate the expected result
        first_day_of_year = datetime.date(2023, 1, 1)
        week_difference = 43
        first_day_of_week = first_day_of_year + datetime.timedelta(days=week_difference * 7 - first_day_of_year.weekday())
        expected = first_day_of_week + datetime.timedelta(days=3)

        self.assertEqual(result, expected, "Error in get_date_from_week method")

def test_get_current_calendar_week():
    current_week = dp.get_current_calendar_week()
    assert isinstance(current_week, int)

def test_get_current_year():
    current_year = dp.get_current_year()
    assert isinstance(current_year, int)

def test_get_current_datetime():
    current_datetime = dp.get_current_datetime()
    assert isinstance(current_datetime, datetime.datetime)

def test_get_calendar_week():
    year, month, day = 2023, 11, 23  # Replace with your own values
    calendar_week = dp.get_calendar_week(year, month, day)
    assert isinstance(calendar_week, int)

def test_get_week_day():
    day_counter = 0  # Replace with your own value
    week_day = dp.get_week_day(day_counter)
    assert week_day.lower() in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

def test_get_date_from_week():
    year, calendar_week, day_counter = 2023, 47, 3  # Replace with your own values
    target_date = dp.get_date_from_week(year, calendar_week, day_counter)
    assert isinstance(target_date, datetime.date)

def test_get_date_from_week_invalid_day_counter():
    year, calendar_week, day_counter = 2023, 47, 7  # Invalid day counter
    try:
        dp.get_date_from_week(year, calendar_week, day_counter)
    except OverflowError as e:
        assert str(e) == "Day counter must be between 0 and 6"
    else:
        assert False, "Expected OverflowError, but no exception was raised"
    