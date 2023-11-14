import threading
import speech_recognition as sr
from ..communication.intend_recognition import IntendRecognizer
from ..communication.FeatureComposite import FeatureComposite
import playsound
import os
import time

keyword_recognized_sound_filepath = os.path.join(os.path.dirname(__file__), 'keyword.mp3')

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class VoiceInput(metaclass=SingletonMeta):
    def __init__(self, featureComposite:FeatureComposite, stop_listening_event:threading.Event, language="de-DE"):
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
        time.sleep(2)
        just_said_something = False
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            lastRecordedText = ""
            while self.is_running:
                while not self.stop_listening_event.is_set():
                    print("Listening...")
                    audio = self.recognizer.listen(source)
                    try:
                        recognized_text = self.recognizer.recognize_google(audio, language=self.language)
                        print(recognized_text)

                        if "stop" in recognized_text.lower() or "stopp" in recognized_text.lower() or "danke" in recognized_text.lower():
                            just_said_something = False
                            recognized_text = ""

                        if "hey karsten" in recognized_text.lower() or "hey carsten" in recognized_text.lower():
                            print("Keyword recognized")
                            playsound.playsound(os.path.normpath(keyword_recognized_sound_filepath))
                            if (recognized_text.lower().startswith("hey karsten") or recognized_text.lower().startswith("hey carsten")) and len(recognized_text[11:]) > 12:
                                recognized_text = recognized_text[11:]
                                self.execute_voice_command(recognized_text)
                        
                        if "hey karsten" in lastRecordedText or "hey carsten" in lastRecordedText or just_said_something:
                            just_said_something = False
                            self.execute_voice_command(recognized_text)

                        lastRecordedText = recognized_text.lower()
                        time.sleep(0.2)
                    except sr.UnknownValueError:
                        lastRecordedText = ""
                        print("Spracherkennung konnte nichts verstehen.")
                    except sr.RequestError as e:
                        print(f"Fehler bei der Verbindung zur Google Web Speech API: {str(e)}")
                just_said_something = True

    def execute_voice_command(self, recognized_text):
        '''
        This function takes the recognized text from the voice input, asks our ai intent model what to do 
        and executes that function. The exexution works by calling the method via our FeatureComposite class.
        To call methods from our features, execute self.featureComposite.call_feature_method(method_name).

        Parameter: recognized_text - String
        Returns: None
        '''
        command = self.intent_recognizer.recognize_intend(recognized_text)
        match command:
            case "GetNextDhbwLecture":
                print("COMMAND: GetNextDhbwLecture")
                self.featureComposite.call_feature_method("readNextDhbwLecture")
                return
            case "GetNewsOfToday":
                # call function         --> Tim?
                print("COMMAND: GetNewsOfToday")
                return
            case "GetLastReceivedEmail":
                # call function
                print("COMMAND: GetLastReceivedEmail")
                self.featureComposite.call_feature_method("getLastReceivedEmail")
                return
            case "GetDeutscheBahnTrainOrBus":
                print("COMMAND: GetDeutscheBahnTrainOrBus")
                self.featureComposite.call_feature_method("readTrainConnectionForNextLecture")
                return
            case "GetWakeUpTime":
                print("COMMAND: GetWakeUpTime")
                self.featureComposite.call_feature_method("getWakeUpTimeForNextMorning")
                return
            case "GetLecturesOfWeek":
                print("COMMAND: GetLecturesOfWeek")
                self.featureComposite.call_feature_method("getLecturesOfEntireWeek")
                return
            case "GetNewsOfInterest":
                print("COMMAND: GetNewsOfInterest")
                self.featureComposite.call_feature_method("getNewsOfInterest")
                return
            # ...
            case _:
                print("COMMAND: I don't know what to do?")
                return
