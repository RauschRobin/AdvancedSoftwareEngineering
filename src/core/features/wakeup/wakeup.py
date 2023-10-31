import time
import datetime
from ...shared.rapla.rapla import Rapla
from ...communication.voice_output import VoiceOutput
from ...shared.deutschebahn.deutschebahn import DeutscheBahn
from ...shared.PreferencesFetcher.PreferencesFetcher import PreferencesFetcher

class WakeUpAssistant:
    def __init__(self, voice_output:VoiceOutput):
        rapla_url = PreferencesFetcher.fetch("rapla-url")
        self.rapla = Rapla(rapla_url)
        self.voice_output = voice_output
        self.deutsche_bahn = DeutscheBahn(voice_output)
        self.wakeUpTimeNeeded = PreferencesFetcher.fetch("wake-up-time-in-minutes")

    def run(self):
        self.greet_at_8_am()

    def greet_at_8_am(self):
        print("Wake Up start")
        if self.voice_output == None:
            print("No voice output!")
            raise SystemError("WakeUp has no instance of VoiceOutput")
        self.voice_output.add_message("Aufwach-Assistent wurde gestartet.")
        while True:
            print("checking rapla")
            # self.voice_output.add_message(self.rapla.getRaplaTimeTableOfGivenWeek(1))
            now = datetime.datetime.now()
            if now.hour == 8 and now.minute == 0:
                message = "Good morning! It's 8:00 AM."
                print(message)
                self.voice_output.add_message(message)
            time.sleep(60)  # Sleep for 1 minute before checking again

    def getNextPlannedDbConnection(self):
        self.voice_output.add_message("Dein nächster Zug kommt in 20 Minuten auf Gleis 7 und fährt nach Bietigheim-Bissingen")
