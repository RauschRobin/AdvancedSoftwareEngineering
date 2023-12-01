import pytest
from datetime import datetime
from unittest.mock import Mock
from ..core.communication.voice_output import VoiceOutput
from ..core.shared.Chat_GPT.ChatGPT import ChatGpt
from ..core.shared.Maps.maps import Maps
from ..core.shared.WeatherAPI.weather import Weather
from ..core.shared.rapla.rapla import Rapla
from ..core.shared.rapla.DateParser import DateParser
from ..core.features.terminplaner.terminplaner import Terminplaner

@pytest.fixture
def mock_voice_output():
    return Mock(spec=VoiceOutput)

@pytest.fixture
def mock_chatgpt():
    return Mock(spec=ChatGpt)

@pytest.fixture
def mock_maps():
    return Mock(spec=Maps)

@pytest.fixture
def mock_weather():
    return Mock(spec=Weather)

@pytest.fixture
def mock_rapla():
    return Mock(spec=Rapla)

def test_init(mock_voice_output):
    terminplaner = Terminplaner(mock_voice_output)
    assert terminplaner.voice_output == mock_voice_output

def test_is_time_in_range():
    terminplaner = Terminplaner(Mock())
    assert terminplaner.is_time_in_range("12:00", "12:05")  # Test within range
    assert not terminplaner.is_time_in_range("00:00", "00:05")  # Test outside range
