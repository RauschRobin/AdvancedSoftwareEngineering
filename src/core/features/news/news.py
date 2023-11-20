from ...communication.voice_output import VoiceOutput
from ...shared.tagesschau.tagesschau import TagesschauAPI
from ...shared.roundcube.roundcube import RoundcubeMock
from ...shared.YamlFetcher.YamlFetcher import YamlFetcher
from ...shared.newsapiorg.news import NewsAPI
from ...shared.Chat_GPT.ChatGPT import ChatGpt
import time
import json
import datetime
import random

class News:
    def __init__(self, voice_output:VoiceOutput):
        '''
        Initializes the class. 

        Parameters: voice_output (VoiceOutput)
        Returns: None
        '''
        self.voice_output = voice_output
        self.tagesschau = TagesschauAPI()
        self.roundcube = RoundcubeMock()
        self.newsapi = NewsAPI()
        self.chatgpt = ChatGpt()
        self.interests = YamlFetcher.fetch("news-interests", "preferences.yaml").split(';')

    def run(self):
        '''
        Starts the while loop of this feature.

        Parameters: None
        Returns: None
        '''
        self.startNewsCheckingLoop()

    def startNewsCheckingLoop(self):
        '''
        Runs the while loop of this feature.

        Parameters: None
        Returns: None
        '''
        while True:
            eilmeldung = self.tagesschau.checkForLastEilmeldung()
            if eilmeldung:
                self.voice_output.add_message(self.chatgpt.get_response("Formuliere mir diese Eilmeldung als Klartext in 2-3 Sätzen: " + json.dumps(eilmeldung)))
            
            currentTime = datetime.datetime.now()
            # Between 9 am and 10 pm, inform me about news of my interest
            if currentTime.hour > 9 and currentTime.hour < 22 and currentTime.minute == 0:
                interest = random.choice(self.interests)
                top_headlines = self.newsapi.get_top_headlines(q=interest, language='de')
                if top_headlines['articles'] != []:
                    self.voice_output.add_message(self.chatgpt.get_response("Formuliere mir diese API Response als Klartext in 2-4 Sätzen:" + json.dumps(random.choice(top_headlines['articles']))))

            newEmail = self.roundcube.checkForNewEmail()
            if newEmail is not None:
                self.voice_output.add_message("Du hast eine neue Email erhalten. " + newEmail)

            time.sleep(60)
    
    def getLastReceivedEmail(self):
        '''
        Gets the last received email from the roundcube mock and adds the message to the voice output message_queue.

        Parameters: None
        Returns: None
        '''
        self.voice_output.add_message(self.roundcube.getLastReceivedEmail())

    def getNewsOfInterest(self):
        '''
        Gets the news of interest and adds the message to the voice output message_queue.

        Parameters: None
        Returns: None
        '''
        for interest in self.interests:
            newsOfInterest = self.newsapi.get_everything(q=interest, language='de')
            #print(newsOfInterest)
            self.voice_output.add_message(self.chatgpt.get_response("Formuliere mir diese API Response als Klartext in 2-4 Sätzen:" + json.dumps(random.choice(newsOfInterest['articles']))))

    def getNewsWithKeyword(self, keyword):
        '''
        Gets the news with a specific keyword and adds the message to the voice output message_queue.

        Parameters: keyword (string)
        Returns: None
        '''
        newsOfInterest = self.newsapi.get_everything(q=keyword, language='de')
        self.voice_output.add_message(self.chatgpt.get_response("Formuliere mir diese API Response als Klartext in 2-4 Sätzen:" + json.dumps(random.choice(newsOfInterest['articles']))))
