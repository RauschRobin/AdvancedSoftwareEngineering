from ...communication.voice_output import VoiceOutput
from ...shared.tagesschau.tagesschau import TagesschauAPI
from ...shared.PreferencesFetcher.PreferencesFetcher import PreferencesFetcher
from ...shared.newsapiorg.news import NewsAPI
import time
import json
import datetime
import random

class News:
    def __init__(self, voice_output:VoiceOutput):
        self.voice_output = voice_output
        self.tagesschau = TagesschauAPI()
        self.newsapi = NewsAPI()
        self.interests = PreferencesFetcher.fetch("news-interests").split(';')

    def run(self):
        self.startNewsCheckingLoop()

    def startNewsCheckingLoop(self):
        while True:
            eilmeldung = self.tagesschau.checkForLastEilmeldung()
            if eilmeldung:
                self.voice_output.add_message(json.dumps(eilmeldung))
            
            currentTime = datetime.datetime.now()
            if currentTime.hour > 9 and currentTime.hour < 22 and currentTime.minute == 0:
                for interest in self.interests:
                    top_headlines = json.loads(self.newsapi.get_top_headlines(q=interest, language='de'))
                    print(top_headlines)
                    self.voice_output.add_message(random.choice(top_headlines['articles']))

            time.sleep(60)
    