
import datetime


class DinnerHelper():
    def is_time_for_dinner(self) -> bool:
        '''Calculate the dinner and return true/false

        Parameters: None
        Returns: True/False
        '''
        now = datetime.datetime.now()
        if now.hour == 18 and now.minute == 0:
            return True
        else:
            # For testing True
            return False
