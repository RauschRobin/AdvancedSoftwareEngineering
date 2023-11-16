from ..core.communication.voice_input import VoiceInput
from unittest.mock import Mock
from ..core.communication.FeatureComposite import FeatureComposite
import threading

stop_listening_event = threading.Event()

def test_start():
    wakeup = Mock()
    ernaehrungsplaner = Mock()
    news = Mock()
    terminplaner = Mock()
    featureComposite = FeatureComposite([wakeup, ernaehrungsplaner, news, terminplaner])
    voice_input = VoiceInput(featureComposite, stop_listening_event)
    
    voice_input.start()
    assert voice_input.is_running is True
    voice_input.stop()

def test_stop():
    wakeup = Mock()
    ernaehrungsplaner = Mock()
    news = Mock()
    terminplaner = Mock()
    featureComposite = FeatureComposite([wakeup, ernaehrungsplaner, news, terminplaner])
    voice_input = VoiceInput(featureComposite, stop_listening_event)
    
    voice_input.stop()
    assert voice_input.is_running is False
