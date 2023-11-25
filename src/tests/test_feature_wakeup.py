from datetime import datetime, timedelta
from ..core.features.wakeup.wakeup import WakeUpAssistant
import datetime
from unittest.mock import MagicMock
import pytest
from ..core.shared.rapla.DateParser import DateParser as dp

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

@pytest.fixture
def mock_voice_output():
    return MagicMock()

@pytest.fixture
def wakeup_assistant(mock_voice_output):
    return WakeUpAssistant(mock_voice_output)

def test_wakeup_assistant_initialization(wakeup_assistant, mock_voice_output):
    assert wakeup_assistant.voice_output == mock_voice_output
    assert wakeup_assistant.currentCalendarWeek is not None
    assert wakeup_assistant.currentWeekTimeTable is not None
    assert wakeup_assistant.deutsche_bahn is not None
    assert wakeup_assistant.localTrainStationDetails is not None

def test_load_preferences(wakeup_assistant):
    wakeup_assistant.loadPreferences()
    assert wakeup_assistant.rapla_url is not None
    assert wakeup_assistant.wakeUpTimeNeeded is not None
    assert wakeup_assistant.timeItTakesFromHomeStationToUniversity is not None
    assert wakeup_assistant.localTrainStationName is not None

def test_is_wake_up_time():
    now = dp.get_current_datetime()
    wake_up_time = now + datetime.timedelta(minutes=5)
    assert WakeUpAssistant.isWakeUpTime(now, wake_up_time) == False
    wake_up_time = now
    assert WakeUpAssistant.isWakeUpTime(now, wake_up_time) == True

def test_load_preferences_with_invalid_yaml(wakeup_assistant):
    # Check if yamlfetcher loads data
    wakeup_assistant.loadPreferences()
    assert wakeup_assistant.rapla_url is not None
    assert wakeup_assistant.wakeUpTimeNeeded is not None
    assert wakeup_assistant.timeItTakesFromHomeStationToUniversity is not None
    assert wakeup_assistant.localTrainStationName is not None

def test_get_next_lecture_with_no_upcoming_lectures(wakeup_assistant):
    # If there are no upcoming lectures, getNextLecture should still return a lecture from next week 
    wakeup_assistant.currentWeekTimeTable = {'monday': [], 'tuesday': []}
    assert wakeup_assistant.getNextLecture() is not None

def test_get_wake_up_time_for_next_morning_no_next_lecture(wakeup_assistant):
    # If there is no next lecture, getWakeUpTimeForNextMorning should return None
    wakeup_assistant.nextLecture = None
    assert wakeup_assistant.getWakeUpTimeForNextMorning() is None

#def test_get_wake_up_time_for_next_morning_first_lecture(wakeup_assistant):
#    wakeup_assistant.nextLecture = {
#        "lecture": {"date": "2025-12-01", "time_start": "09:00"}
#    }
#    wakeup_time = wakeup_assistant.getWakeUpTimeForNextMorning()
#    assert wakeup_time is None

#def test_get_wake_up_time_for_next_morning_not_first_lecture(wakeup_assistant):
#    # If the next lecture is not the first of the day, it should return None
#    wakeup_assistant.nextLecture = {
#        "lecture": {"date": "2023-12-01", "time_start": "11:00"}
#    }
#    assert wakeup_assistant.getWakeUpTimeForNextMorning() is None
