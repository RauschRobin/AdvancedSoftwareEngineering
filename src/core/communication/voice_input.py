import threading
import speech_recognition as sr
from ..communication.intend_recognition import IntendRecognizer
from ..communication.FeatureComposite import FeatureComposite
from ..communication.voice_output import VoiceOutput
import playsound
import os
import time

keyword_recognized_sound_filepath = os.path.join(os.path.dirname(__file__), 'keyword.mp3')
LIST_OF_KEYWORDS = ["politik", "umwelt", "klima", "wetter", "deutschland", "krieg", "ukraine", "außenpolitik", "fussball", "sport", "innenpolitik", "ki", "künstliche intelligenz", "innenpolitisches", "außenpolitisches", "künstlicher intelligenz", "Spazieren gehen", "Musik hören", "Bücher lesen", "Kochen", "Fahrradfahren", "Fotografieren", "Yoga", "Gärtnern", "Malen", "Film schauen", "Reisen", "Klettern", "Treffen mit Freunden", "Sport treiben", "Meditieren", "Stricken", "Sprachen lernen", "Singen", "Theater besuchen", "Picknicken", "Gaming", "Badminton spielen", "Kunsthandwerk betreiben", "Tauchen", "Ski", "Tanzen", "Schach", "Segeln", "Vogelbeobachtung", "Flohmarkt", "Segway-Tour", "Konzerte", "Museum", "Angeln", "Surfen", "Freiwilligenarbeit", "Stadtbummel", "Schwimmen", "Höhlenforschung", "Stand-up-Paddeln", "Kajakfahren", "eins", "zwei", "drei"]

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class VoiceInput(metaclass=SingletonMeta):
    def __init__(self, featureComposite: FeatureComposite, stop_listening_event: threading.Event, voice_ouput: VoiceOutput, language="de-DE"):
        '''
        Initializes the VoiceInput class.

        Parameters: featureComposite - FeatureComposite
                    language - String (optional)
        Returns: None
        '''
        self.stop_listening_event = stop_listening_event
        self.featureComposite = featureComposite
        self.recognizer = sr.Recognizer()
        self.intent_recognizer = IntendRecognizer()
        self.voice_output = voice_ouput
        self.language = language
        self.is_running = False

    def start(self):
        '''
        This method starts the voice_input to listens for commands.

        Parameter: None
        Returns: None
        '''
        self.is_running = True
        user_input_thread = threading.Thread(target=self.listen_continuous)
        user_input_thread.start()

    def stop(self):
        '''
        This method stops the voice_input class from listening for commands.

        Parameter: None
        Returns: None
        '''
        self.is_running = False

    def listen_continuous(self):
        '''
        This method listens continuously for incoming voice commands and passes them to 
        the method execute_voice_command(). This method contains a while True loop and does not stop by itself.

        Parameters: None
        Returns: None
        '''
        just_said_something = False
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            lastRecordedText = ""
            while self.is_running:
                while not self.stop_listening_event.is_set():
                    print("Listening...")
                    audio = self.recognizer.listen(source, timeout=10)
                    try:
                        if self.stop_listening_event.is_set():
                            print("Stopped listening: Carschten said something during the listening phase.")
                            break
                        recognized_text = self.recognizer.recognize_google(audio, language=self.language)
                        print(recognized_text)

                        if "stop" in recognized_text.lower() or "stopp" in recognized_text.lower() or "danke" in recognized_text.lower() or "dankeschön" in recognized_text.lower():
                            just_said_something = False
                            recognized_text = ""

                        if "hey karsten" in recognized_text.lower() or "hey carsten" in recognized_text.lower():
                            print("Keyword recognized")
                            playsound.playsound(os.path.normpath(keyword_recognized_sound_filepath))
                            if (recognized_text.lower().startswith("hey karsten") or recognized_text.lower().startswith("hey carsten")) and len(recognized_text[11:]) > 12:
                                recognized_text = recognized_text[11:]
                                self.execute_voice_command(recognized_text)
                                time.sleep(0.2) # Speed at wich humans still thinks its instant and natural
                        elif "hey karsten" in lastRecordedText or "hey carsten" in lastRecordedText or just_said_something:
                            just_said_something = False
                            self.execute_voice_command(recognized_text)
                            time.sleep(0.2) # Speed at wich humans still thinks its instant and natural

                        lastRecordedText = recognized_text.lower()
                    except sr.UnknownValueError:
                        lastRecordedText = ""
                        print("Spracherkennung konnte nichts verstehen.")
                    except sr.RequestError as e:
                        print(
                            f"Fehler bei der Verbindung zur Google Web Speech API: {str(e)}")
                just_said_something = True

    def execute_voice_command(self, recognized_text):
        '''
        This function takes the recognized text from the voice input, asks our ai intent model what to do 
        and executes that function. The exexution works by calling the method via our FeatureComposite class.
        To call methods from our features, execute self.featureComposite.call_feature_method(method_name).

        Parameter: recognized_text - String
        Returns: None
        '''
        detected_keyword = ""
        for keyword in LIST_OF_KEYWORDS:
            if keyword in recognized_text.lower():
                detected_keyword = keyword
        command = self.intent_recognizer.recognize_intend(recognized_text)
        match command:
            case "GetNextDhbwLecture":
                print("COMMAND: GetNextDhbwLecture")
                self.featureComposite.call_feature_method(
                    "readNextDhbwLecture")
                return
            case "GetLastReceivedEmail":
                print("COMMAND: GetLastReceivedEmail")
                self.featureComposite.call_feature_method(
                    "getLastReceivedEmail")
                return
            case "GetDeutscheBahnTrainOrBus":
                print("COMMAND: GetDeutscheBahnTrainOrBus")
                self.featureComposite.call_feature_method(
                    "readTrainConnectionForNextLecture")
                return
            case "GetWakeUpTime":
                print("COMMAND: GetWakeUpTime")
                self.featureComposite.call_feature_method(
                    "getWakeUpTimeForNextMorning")
                return
            case "GetLecturesOfWeek":
                print("COMMAND: GetLecturesOfWeek")
                self.featureComposite.call_feature_method(
                    "getLecturesOfEntireWeek")
                return
            case "GetNewsOfInterest":
                print("COMMAND: GetNewsOfInterest")
                self.featureComposite.call_feature_method("getNewsOfInterest")
                return
            case "GetActivitiesForToday":
                print("COMMAND: GetActivitiesForToday")
                self.featureComposite.call_feature_method("find_activity")
                return
            case "FindPlace":
                print("COMMAND: FindPlace")
                self.featureComposite.call_feature_method("find_place", keyword=detected_keyword)
                return
            case "GetNewsWithKeyword":
                print("COMMAND: GetNewsWithKeyword")
                self.featureComposite.call_feature_method(
                    "getNewsWithKeyword", keyword=detected_keyword)
                return
            case "ChooseRestaurantWithKeyword":
                print("COMMAND: ChooseRestaurantWithKeyword")
                self.featureComposite.call_feature_method("chooseRestaurantWithKeyword", keyword=detected_keyword)
                return
            case "GetRestaurantContact":
                print("COMMAND: GetRestaurantContact")
                self.featureComposite.call_feature_method("getRestaurantContact")
                return
            case "GetRestaurantLocation":
                print("COMMAND: GetRestaurantLocation")
                self.featureComposite.call_feature_method("getRestaurantLocation")
                return
            case "how_to_cook_the_meal":
                print("COMMAND: how_to_cook_the_meal")
                self.featureComposite.call_feature_method(
                    "how_to_cook_the_meal")
            case "cook_something_different":
                print("COMMAND: cook_something_different")
                self.featureComposite.call_feature_method(
                    "cook_something_different")
            case "ingredients_at_home_to_cook":
                print("COMMAND: ingredients_at_home_to_cook")
                self.featureComposite.call_feature_method(
                    "ingredients_at_home_to_cook")
            case "generate_shopping_list_for_meal":
                print("COMMAND: generate_shopping_list_for_meal")
                self.featureComposite.call_feature_method(
                    "generate_shopping_list_for_meal")
            case "fallback":
                # TODO: You could also redirect the question/recorded text to chatgpt
                self.voice_output.add_message(
                    "Ich bin mir nicht sicher was du von mir willst. Kannst du das anders formulieren?")
                print(
                    "I could not match your voice command onto a function. I do not know what to do...")
                return
            # ...
            case _:
                raise SyntaxError(
                    "Something went wrong while trying to match your voice command onto a function.")
