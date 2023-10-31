import datetime
import dateutil.relativedelta as rd

class WeekAndDaysHandling:
    @staticmethod
    def get_current_calendar_week():
        calendar_week = datetime.datetime.now().isocalendar()[1]
        return calendar_week

    @staticmethod
    def get_calendar_week(year, month, day):
        calendar_week = datetime.date(year, month, day).isocalendar()[1]
        return calendar_week
    
    @staticmethod
    def get_week_day(day_counter):
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
        # Berechnen Sie das Datum des ersten Tages des Jahres
        first_day_of_year = datetime.datetime(year, 1, 1)

        # Berechnen Sie das Datum des ersten Montags des Jahres
        if first_day_of_year.weekday() > 3:
            first_monday_of_year = first_day_of_year + rd.relativedelta(days=(7 - first_day_of_year.weekday() + 1))
        else:
            first_monday_of_year = first_day_of_year - rd.relativedelta(days=(first_day_of_year.weekday() - 1))

        # Berechnen Sie das Datum basierend auf der Kalenderwoche und dem Wochentag
        date = first_monday_of_year + rd.relativedelta(days=((calendar_week - 1) * 7 + day_counter))

        return date.date()