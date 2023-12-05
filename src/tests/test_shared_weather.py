from ..core.shared.WeatherAPI.weather import Weather
import pytest
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_weather_api_key(monkeypatch):
    monkeypatch.setenv('WEATHER_SECRET', 'your_mocked_api_key')

def test_get_weather_of_date(mock_weather_api_key):
    weather = Weather()
    
    # Mocking the response from the API
    mock_response = MagicMock()
    mock_response.json.return_value = {"forecastDate": "2023-12-04T12:00:00Z", "other_data": "example"}
    
    with patch('requests.get', return_value=mock_response):
        weather_data = weather.get_weather_of_date()
    
    assert isinstance(weather_data, dict)
    assert "forecastDate" in weather_data
    assert "other_data" in weather_data

def test_is_weather_data_up_to_date_with_valid_data(mock_weather_api_key):
    weather = Weather()

    # Mocking the weather_data with a date in the future
    mock_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    weather.weather_data = {"forecastDate": mock_date}

    assert not weather.is_weather_data_up_to_date()
