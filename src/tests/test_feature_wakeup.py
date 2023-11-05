import pytest
import sys
import os
from ..core.features.wakeup.wakeup import WakeUpAssistant

# Create a mock VoiceOutput class for testing
class MockVoiceOutput:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

@pytest.fixture
def mock_voice_output():
    return MockVoiceOutput()

def test_wake_up_assistant_initialization(mock_voice_output):
    wake_up_assistant = WakeUpAssistant(mock_voice_output)
    assert wake_up_assistant is not None

def test_load_preferences(mock_voice_output):
    wake_up_assistant = WakeUpAssistant(mock_voice_output)
    wake_up_assistant.loadPreferences()
    assert wake_up_assistant.rapla_url is not None
    assert wake_up_assistant.wakeUpTimeNeeded is not None
    assert wake_up_assistant.timeItTakesFromHomeStationToUniversity is not None
    assert wake_up_assistant.localTrainStationName is not None

def test_get_next_lecture(mock_voice_output):
    wake_up_assistant = WakeUpAssistant(mock_voice_output)
    next_lecture = wake_up_assistant.getNextLecture()
    assert next_lecture is not None

def test_is_lecture_first_of_the_day(mock_voice_output):
    wake_up_assistant = WakeUpAssistant(mock_voice_output)
    lecture = {
        "lecture": {
            "date": "2023-11-06",
            "time_start": "09:00",
            "time_end": "12:00",
            "subject": "Test Lecture",
            "prof": "Test Professor",
            "room": "Test Room"
        }
    }
    assert wake_up_assistant.isLectureFirstOfTheDay(lecture) is True

def test_get_wake_up_time_for_next_morning(mock_voice_output):
    wake_up_assistant = WakeUpAssistant(mock_voice_output)
    wake_up_time = wake_up_assistant.getWakeUpTimeForNextMorning()
    assert wake_up_time is not None

def test_get_train_connection_for_next_lecture(mock_voice_output):
    wake_up_assistant = WakeUpAssistant(mock_voice_output)
    train_connection = wake_up_assistant.getTrainConnectionForNextLecture()
    assert train_connection is not None

def test_start_and_run_wake_up_assistant(mock_voice_output):
    # This test just checks if the method runs without errors, actual functionality is difficult to test
    wake_up_assistant = WakeUpAssistant(mock_voice_output)
    wake_up_assistant.startAndRunWakeUpAssistant()

def test_get_lectures_of_entire_week(mock_voice_output):
    wake_up_assistant = WakeUpAssistant(mock_voice_output)
    wake_up_assistant.getLecturesOfEntireWeek()
    assert mock_voice_output.messages is not None

def test_read_next_dhbw_lecture(mock_voice_output):
    wake_up_assistant = WakeUpAssistant(mock_voice_output)
    wake_up_assistant.readNextDhbwLecture()
    assert mock_voice_output.messages is not None
