import datetime
import dateutil.relativedelta as rd

class DateParser:
    @staticmethod
    def get_current_calendar_week():
        '''
        Gets the current calendar week.

        Parameters: None
        Returns: calendar_week (int)
        '''
        calendar_week = datetime.datetime.now().isocalendar()[1]
        return calendar_week

    @staticmethod
    def get_calendar_week(year, month, day):
        '''
        Get calendar week from given date.

        Parameters: year, month, day
        Returns: calendar week (int)
        '''
        calendar_week = datetime.date(year, month, day).isocalendar()[1]
        return calendar_week
    
    @staticmethod
    def get_week_day(day_counter):
        '''
        Gets the weeday based on the day counter.

        Parameters: day_counter (int)
        Returns: day (STRING: "monday", ...)
        '''
        week_day = ""
        if(day_counter == 0):
            week_day = "monday"
        elif(day_counter == 1):
            week_day = "tuesday"
        elif(day_counter == 2):
            week_day = "wednesday"
        elif(day_counter == 3):
            week_day = "thursday"
        elif(day_counter == 4):
            week_day = "friday"
        elif(day_counter == 5):
            week_day = "saturday"
        elif(day_counter == 6):
            week_day = "sunday"
        
        return week_day
    
    @staticmethod
    def get_date_from_week(year, calendar_week, day_counter):
        '''
        Get the date from a day of a calendar week.

        Parameters: year, calendar_week, day_counter
        Returns: date (datetime)
        '''
        if day_counter < 0 or day_counter > 6:
            raise OverflowError("Day counter must be between 0 and 6")
        # Create a date for the first day of the specified year
        first_day_of_year = datetime.date(year, 1, 1)

        # Calculate the date for the first day (Monday) of the specified calendar_week
        first_day_of_week = first_day_of_year + datetime.timedelta(days=(calendar_week) * 7 - first_day_of_year.weekday())

        # Calculate the date of the specified day within the week
        target_date = first_day_of_week + datetime.timedelta(days=day_counter)
        return target_date
    