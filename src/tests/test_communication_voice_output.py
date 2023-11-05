from ..core.communication.voice_output import VoiceOutput
import pytest

def test_text_to_speech():
    output = VoiceOutput()
    with pytest.raises(ValueError):
        output.text_to_speech("") 
    