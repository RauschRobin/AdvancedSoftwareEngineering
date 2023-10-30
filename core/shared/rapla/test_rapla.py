import pytest
from unittest.mock import Mock, patch
from rapla import Rapla  # Replace 'your_module' with the actual module name

@pytest.fixture
def rapla_instance():
    return Rapla()

def test_get_current_calendar_week(rapla_instance):
    with patch('your_module.datetime') as mock_datetime:
        mock_datetime.now.return_value = Mock(isocalendar=lambda: (2023, 43))
        result = rapla_instance.get_current_calendar_week()
        assert result == 43

def test_get_calendar_week(rapla_instance):
    result = rapla_instance.get_calendar_week(2023, 10, 26)
    assert result == 43  # Assuming October 26, 2023, is in week 43

def test_get_week_day(rapla_instance):
    assert rapla_instance.get_week_day(0) == "monday"
    assert rapla_instance.get_week_day(1) == "tuesday"

def test_get_date_from_week(rapla_instance):
    result = rapla_instance.get_date_from_week(2023, 43, 3)
    assert result == datetime.date(2023, 10, 26)

def test_get_week_data(rapla_instance):
    with patch('your_module.requests.get') as mock_get:
        mock_get.return_value.text = "HTML content here"
        result = rapla_instance.get_week_data(43, 2023)
        assert isinstance(result, str)  # Check if it's a JSON string