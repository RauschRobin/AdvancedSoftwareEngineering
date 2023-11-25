from datetime import datetime, timedelta
from ..core.features.wakeup.wakeup import WakeUpAssistant
import datetime

def test_isWakeUpTime():
    # Define the current time and wake-up time for the test case
    now = datetime.datetime(2023, 1, 1, 8, 0)  # January 1, 2023, 8:00 AM
    wake_up_time = datetime.datetime(2023, 1, 1, 8, 0)  # January 1, 2023, 8:00 AM

    # Test when the current time is equal to the wake-up time
    assert WakeUpAssistant.isWakeUpTime(now, wake_up_time) is True

    # Test when the current time is different from the wake-up time
    wake_up_time = datetime.datetime(2023, 1, 1, 9, 0)  # January 1, 2023, 9:00 AM
    assert WakeUpAssistant.isWakeUpTime(now, wake_up_time) is False

    # Test with a different date
    wake_up_time = datetime.datetime(2023, 1, 2, 8, 0)  # January 2, 2023, 8:00 AM
    assert WakeUpAssistant.isWakeUpTime(now, wake_up_time) is False

    # Test with a different hour
    wake_up_time = datetime.datetime(2023, 1, 1, 7, 0)  # January 1, 2023, 7:00 AM
    assert WakeUpAssistant.isWakeUpTime(now, wake_up_time) is False

    # Test with a different minute
    wake_up_time = datetime.datetime(2023, 1, 1, 8, 30)  # January 1, 2023, 8:30 AM
    assert WakeUpAssistant.isWakeUpTime(now, wake_up_time) is False

    # Test with a timedelta difference
    wake_up_time = now + datetime.timedelta(minutes=30)
    assert WakeUpAssistant.isWakeUpTime(now, wake_up_time) is False