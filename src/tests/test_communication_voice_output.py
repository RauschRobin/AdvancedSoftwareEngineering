from ..core.communication.voice_output import VoiceOutput
import pytest
import threading

stop_listening_event = threading.Event()

def test_text_to_speech():
    output = VoiceOutput(stop_listening_event)
    with pytest.raises(ValueError):
        output.text_to_speech("") 
    