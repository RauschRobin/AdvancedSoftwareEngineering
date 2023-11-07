from ...communication.voice_output import VoiceOutput
from ...shared.tagesschau.tagesschau import TagesschauAPI
from ...shared.roundcube.roundcube import RoundcubeMock
import time
import json

class News:
    def __init__(self, voice_output:VoiceOutput):
        self.voice_output = voice_output
        self.tagesschau = TagesschauAPI()
        self.roundcube = RoundcubeMock()

    def run(self):
        self.startNewsCheckingLoop()

    def startNewsCheckingLoop(self):
        while True:
            eilmeldung = self.tagesschau.checkForLastEilmeldung()
            if eilmeldung:
                self.voice_output.add_message(json.dumps(eilmeldung))
            
            newEmail = self.roundcube.checkForNewEmail()
            if newEmail is not None:
                self.voice_output.add_message(newEmail)

            time.sleep(60)
    
    def getLastReceivedEmail(self):
        self.voice_output.add_message(self.roundcube.getLastReceivedEmail())
