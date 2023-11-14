from ...communication.voice_output import VoiceOutput
from ...shared.tagesschau.tagesschau import TagesschauAPI
from ...shared.roundcube.roundcube import RoundcubeMock
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
        self.roundcube = RoundcubeMock()
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
                    top_headlines = self.newsapi.get_top_headlines(q=interest, language='de')
                    print(top_headlines)
                    #self.voice_output.add_message(json.dumps(random.choice(top_headlines['articles'])))
                    # TODO: This throws an error!!

            newEmail = self.roundcube.checkForNewEmail()
            if newEmail is not None:
                self.voice_output.add_message("Du hast eine neue Email erhalten. " + newEmail)

            time.sleep(60)
    
    def getLastReceivedEmail(self):
        self.voice_output.add_message(self.roundcube.getLastReceivedEmail())

    def getNewsOfInterest(self):
        for interest in self.interests:
            newsOfInterest = self.newsapi.get_everything(q=interest, language='de')
            print(newsOfInterest)
            self.voice_output.add_message(json.dumps(random.choice(newsOfInterest['articles'])))
