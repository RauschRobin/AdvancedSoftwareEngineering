import unittest
import datetime
import dateutil.relativedelta as rd
from ..rapla import Rapla # TODO: relativen Pfad from 'rapla' finden und Klasse Rapla importieren

class TestRapla(unittest.TestCase):
    def setUp(self):
        self.rapla = Rapla()

    def test_get_current_calendar_week(self):
        result = self.rapla.get_current_calendar_week()
        expected = datetime.datetime.now().isocalendar()[1]
        self.assertEqual(result, expected, "Fehler in get_current_calendar_week Methode")

    def test_get_calendar_week(self):
        result = self.rapla.get_calendar_week(2023, 10, 26)
        expected = datetime.date(2023, 10, 26).isocalendar()[1]
        self.assertEqual(result, expected, "Fehler in get_calendar_week Methode")

    def test_get_week_day(self):
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        for i in range(7):
            result = self.rapla.get_week_day(i)
            expected = days[i]
            self.assertEqual(result, expected, f"Fehler in get_week_day Methode für {expected}")

    def test_get_date_from_week(self):
        result = self.rapla.get_date_from_week(2023, 43, 3)
        first_day_of_year = datetime.datetime(2023, 1, 1)
        if first_day_of_year.weekday() > 3:
            first_monday_of_year = first_day_of_year + rd.relativedelta(days=(7 - first_day_of_year.weekday() + 1))
        else:
            first_monday_of_year = first_day_of_year - rd.relativedelta(days=(first_day_of_year.weekday() - 1))
        expected = (first_monday_of_year + rd.relativedelta(days=((43 - 1) * 7 + 3))).date()
        self.assertEqual(result, expected, "Fehler in get_date_from_week Methode")