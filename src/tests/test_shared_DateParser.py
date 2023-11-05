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
    