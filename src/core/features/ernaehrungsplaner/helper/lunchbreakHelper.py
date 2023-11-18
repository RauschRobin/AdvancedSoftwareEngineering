import datetime
import json

from ....shared.PreferencesFetcher.PreferencesFetcher import PreferencesFetcher

from ....shared.rapla.rapla import Rapla
from ....shared.rapla.DateParser import DateParser as dp


class LunchbreakHelper():
    def __init__(self):
        self.load_preferences()

        self.rapla = Rapla(self.rapla_url)
        # store current week timetable & calendar week to reduce number of requests
        self.current_calendar_week = dp.get_current_calendar_week()
        self.current_week_time_table = json.loads(self.rapla.fetchLecturesOfWeek(
            self.current_calendar_week, datetime.datetime.now().isocalendar()[0]))

        self.calculate_lunchbreak_time()

    def load_preferences(self):
        '''
        This methods loads all the preferences used in this class and stores them in variables.

        Parameters: None
        Returns: None
        '''
        self.rapla_url = PreferencesFetcher.fetch("rapla-url")

    def calculate_lunchbreak_time(self):
        '''Calculate the lunchbreak time for the user via rapla

        Parameters: None
        Returns: lunchbreak_hour (int) lunchbreak_minute (int) lunchbreak_duration_in_minutes (int)
        '''
        now = datetime.datetime.now()
        weekday_as_string = now.strftime("%A").lower()

        todays_lectures = self.current_week_time_table.get(
            weekday_as_string, [])

        lunchbreak_hour = 12
        lunchbreak_minute = 0

        # TODO
        # - Use Rapla to calculate the lunchbreak

        if todays_lectures is not None:
            # find the end time of the lecture near the lunchbreak time
            for lecture in todays_lectures:
                end_time_hour_minute_string = lecture['lecture']['time_end']
                end_time_hour = int(end_time_hour_minute_string.split(":")[0])
                end_time_minute = int(
                    end_time_hour_minute_string.split(":")[1])
                if end_time_hour > 10 and end_time_hour < 15:
                    lunchbreak_hour = end_time_hour
                    lunchbreak_minute = end_time_minute

        return lunchbreak_hour, lunchbreak_minute

    def is_time_for_lunchbreak(self) -> bool:
        '''Calculate the lunchtime and return true/false

        Parameters: None
        Returns: True/False
        '''
        now = datetime.datetime.now()
        is_lunchbreak_hour, is_lunchbreak_minute = self.calculate_lunchbreak_time()

        if now.hour == is_lunchbreak_hour and now.minute == is_lunchbreak_minute:
            return True
        else:
            return False

    def is_businesses_not_none(self, businesses) -> bool:
        '''Find out if the businesses response are not null and return true/false

        Parameters: businesses (Dic, None)
        Returns: True/False
        '''
        if len(businesses.get("businesses", [])) > 0:
            return True
        else:
            return False
