from ...communication.voice_output import VoiceOutput
from ...shared.tagesschau.tagesschau import TagesschauAPI
import time
import json

class News:
    def __init__(self, voice_output:VoiceOutput):
        self.voice_output = voice_output
        self.tagesschau = TagesschauAPI()

    def run(self):
        self.startNewsCheckingLoop()

    def startNewsCheckingLoop(self):
        while True:
            eilmeldung = self.tagesschau.checkForLastEilmeldung()
            if eilmeldung:
                self.voice_output.add_message(json.dumps(eilmeldung))
            time.sleep(60)
    