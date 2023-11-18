from ..core.communication.voice_output import VoiceOutput
from ..core.features.wakeup.wakeup import WakeUpAssistant


def test_loadPreferences():
    test = WakeUpAssistant(VoiceOutput)
    test = test.loadPreferences()
