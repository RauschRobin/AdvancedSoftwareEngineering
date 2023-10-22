from ...communication.voice_output import VoiceOutput

# https://pypi.org/project/deutsche-bahn-api/ --> Wenn man das benutzen möchte

class DeutscheBahn:
    def __init__(self, voice_output:VoiceOutput):
        self.voice_output = voice_output

    def getConnection(self):
        self.voice_output.add_message("Bietigheim-Bissingen|Stuttgart Hbf, S5, 12:37 Uhr")
