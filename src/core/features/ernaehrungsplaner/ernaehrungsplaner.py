import datetime
import time
from ...communication.voice_output import VoiceOutput
from ...shared.yelp.yelp import Yelp
from ...shared.theMealDb.theMealDb import TheMealDb
from ...shared.currentLocation import CurrentLocation
from ...shared.inventory import Inventory


class Ernaehrungsplaner:
    def __init__(self, voice_output: VoiceOutput):
        '''
        Initializes the class. 

        Parameters: voice_output (VoiceOutput)
        Returns: None
        '''
        self.voice_output = voice_output
        self.yelp = Yelp()
        self.theMealDb = TheMealDb()
        self.currentLocation = CurrentLocation()
        self.inventory = Inventory()

        self.loadPreferences()

    def loadPreferences(self):
        '''
        This methods loads all the preferences used in this class and stores them in variables.

        Parameters: None
        Returns: None
        '''
        pass

    def run(self):
        '''
        Starts the while loop of this feature.

        Parameters: None
        Returns: None
        '''
        self.startErnaehrungsplanerLoop()

    def startErnaehrungsplanerLoop(self):
        '''
        Runs the while loop of this feature.

        Parameters: None
        Returns: None
        '''
        if self.voice_output == None:
            raise SystemError("WakeUp has no instance of VoiceOutput")

        while True:
            now = datetime.datetime.now()

            # TODO
            # Basic Lunchbreak (12 am)
            # - Calculate the lunchbreak time
            # - Find a restaurant near the user
            # ...- Use preferences to know what the user likes (restaurants)

            # Proactive calculation for the lunchbreak
            if now.hour == 6 and now.minute == 0:
                pass

            # TODO
            # Bsic evening meal shopping (18 pm)
            # - Notify the user at 18 pm which things he/she can cook or have to buy
            # ...- Use preferences to know what the user likes
            # ...- Check the inventory and use the meal db if everything is available to cook

            # Proactive calculation for cooking and meal shopping in the evening
            if now.hour == 18 and now.minute == 0:
                pass

            # Check every day
            time.sleep(1440)
