import pytest
from unittest.mock import Mock
from datetime import datetime
from ..core.communication.voice_output import VoiceOutput
from ..core.shared.Chat_GPT.ChatGPT import ChatGpt
from ..core.shared.Maps.maps import Maps
from ..core.shared.WeatherAPI.weather import Weather
from ..core.shared.rapla.rapla import Rapla
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
    current_time = datetime.strptime("12:03", "%H:%M").time()  # Aktuelle Uhrzeit auf 12:03 setzen
    terminplaner.current_time = current_time  # Setze die aktuelle Zeit in Terminplaner
    
    start_time = "12:00"
    end_time = "12:05"
    
    result = terminplaner.is_time_in_range(start_time, end_time, current_time)
    
    assert result, f"Expected time {current_time.strftime('%H:%M')} to be in range {start_time}-{end_time}"
