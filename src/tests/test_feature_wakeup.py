import datetime
from unittest.mock import patch, Mock
import pytest
from ..core.features.wakeup.wakeup import WakeUpAssistant
import datetime

# Mock class for VoiceOutput (replace with actual implementation)
class MockVoiceOutput:
    def add_message(self, message):
        pass

# Mock class for ChatGpt (replace with actual implementation)
class MockChatGpt:
    def get_response(self, message):
        return "Mocked response for testing"

# Use pytest fixture to set up the mocked classes
@pytest.fixture
def mock_yaml_fetcher():
    with patch('AdvancedSoftwareEngineering.src.core.shared.YamlFetcher.YamlFetcher.YamlFetcher.fetch', return_value='your_mocked_value'):
        yield

# Use pytest fixture to set up the mocked ChatGpt class
@pytest.fixture
def mock_chatgpt():
    with patch('AdvancedSoftwareEngineering.src.core.shared.Chat_GPT.ChatGPT.ChatGpt', return_value=MockChatGpt()):
        yield

# Test class using the pytest fixtures
class TestWakeUpAssistant:
    def setup(self):
        # Initialize the WakeUpAssistant with mocked instances
        self.wake_up_assistant = WakeUpAssistant(MockVoiceOutput())

    def test_get_next_lecture(self, mock_yaml_fetcher, mock_chatgpt):
        # Test the getNextLecture method
        next_lecture = self.wake_up_assistant.getNextLecture()
        assert isinstance(next_lecture, dict) or next_lecture is None

    def test_get_wake_up_time_for_next_morning(self, mock_yaml_fetcher, mock_chatgpt):
        # Test the getWakeUpTimeForNextMorning method
        wake_up_time = self.wake_up_assistant.getWakeUpTimeForNextMorning()
        assert isinstance(wake_up_time, datetime.datetime) or wake_up_time is None

    def test_get_train_connection_for_next_lecture(self, mock_yaml_fetcher, mock_chatgpt):
        # Test the getTrainConnectionForNextLecture method
        train_connection = self.wake_up_assistant.getTrainConnectionForNextLecture()
        assert isinstance(train_connection, dict) or train_connection is None

    def test_is_lecture_first_of_the_day(self, mock_yaml_fetcher, mock_chatgpt):
        # Test the isLectureFirstOfTheDay method
        next_lecture = self.wake_up_assistant.getNextLecture()
        if next_lecture:
            result = self.wake_up_assistant.isLectureFirstOfTheDay(next_lecture)
            assert isinstance(result, bool)

# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])
