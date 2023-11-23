from ..core.communication.voice_output import VoiceOutput
import pytest
from unittest.mock import patch
import threading

stop_listening_event = threading.Event()

def test_add_empty_message(voice_output_instance):
    # Test if add_message does not add an empty message to the message_queue
    voice_output_instance.add_message("")
    assert voice_output_instance.message_queue == []

def test_text_to_speech():
    output = VoiceOutput(stop_listening_event)
    with pytest.raises(ValueError):
        output.text_to_speech("") 
    
@pytest.fixture
def voice_output_instance():
    stop_listening_event = threading.Event()
    return VoiceOutput(stop_listening_event)

def test_add_message(voice_output_instance):
    # Test if add_message adds a message to the message_queue
    message = "Test message"
    voice_output_instance.add_message(message)
    assert voice_output_instance.message_queue == [message]

def test_remove_unpronounceable_characters():
    # Test remove_unpronounceable_characters method
    voice_output_instance = VoiceOutput(stop_listening_event)
    input_string = "Hello @ World!"
    expected_result = "Hello   World "
    result = voice_output_instance.remove_unpronounceable_characters(input_string)
    assert result == expected_result

@patch.object(VoiceOutput, 'is_time', return_value=True)
def test_remove_unpronounceable_characters_with_time(mock_is_time):
    # Test remove_unpronounceable_characters method with is_time returning True
    input_string = "12:34"
    expected_result = "12Uhr34"
    result = VoiceOutput.remove_unpronounceable_characters(VoiceOutput, input_string)
    print(result)
    assert result == expected_result

@patch.object(VoiceOutput, 'is_time', return_value=False)
def test_remove_unpronounceable_characters_without_time(mock_is_time):
    # Test remove_unpronounceable_characters method with is_time returning False
    input_string = "Hello: World!"
    expected_result = "Hello. World "
    result = VoiceOutput.remove_unpronounceable_characters(VoiceOutput, input_string)
    assert result == expected_result