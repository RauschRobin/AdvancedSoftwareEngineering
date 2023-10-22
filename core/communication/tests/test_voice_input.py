from ..voice_input import VoiceInput
from unittest.mock import Mock

def test_start():
    wakeup = Mock()
    ernaehrungsplaner = Mock()
    news = Mock()
    terminplaner = Mock()
    voice_input = VoiceInput(wakeup, ernaehrungsplaner, news, terminplaner)
    
    voice_input.start()
    assert voice_input.is_running is True
    voice_input.stop()

def test_stop():
    wakeup = Mock()
    ernaehrungsplaner = Mock()
    news = Mock()
    terminplaner = Mock()
    voice_input = VoiceInput(wakeup, ernaehrungsplaner, news, terminplaner)
    
    voice_input.stop()
    assert voice_input.is_running is False
