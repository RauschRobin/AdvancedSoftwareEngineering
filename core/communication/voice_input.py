import threading
import speech_recognition as sr
from ..communication.intend_recognition import IntendRecognizer
from FeatureComposite import FeatureComposite

class VoiceInput:
    def __init__(self, featureComposite:FeatureComposite, language="de-DE"):
        self.featureComposite = featureComposite
        self.recognizer = sr.Recognizer()
        self.intent_recognizer = IntendRecognizer()
        self.language = language
        self.is_running = False

    def start(self):
        self.is_running = True
        user_input_thread = threading.Thread(target=self.listen_continuous)
        user_input_thread.start()

    def stop(self):
        self.is_running = False

    def listen_continuous(self):
        with sr.Microphone() as source:
            print("Bitte sprechen Sie.")
            self.recognizer.adjust_for_ambient_noise(source)
            while self.is_running:
                audio = self.recognizer.listen(source)
                try:
                    recognized_text = self.recognizer.recognize_google(audio, language=self.language)
                    
                    print(recognized_text)
                    
                    if "hey karsten" in recognized_text.lower() or "hey carsten" in recognized_text.lower():
                        print("Keyword recognized!")
                    
                    # Ends the voice recognition --> does not restart
                    if "stop" in recognized_text.lower():
                        print("Stop recognition")
                        break

                    self.execute_voice_command(recognized_text)
                except sr.UnknownValueError:
                    print("Spracherkennung konnte nichts verstehen.")
                except sr.RequestError as e:
                    print(f"Fehler bei der Verbindung zur Google Web Speech API: {str(e)}")

    # This function takes the recognized text from the voice input, asks our 
    # ai intent model what to do and executed that function.
    def execute_voice_command(self, recognized_text):
        command = self.intent_recognizer.recognize_intend(recognized_text)
        match command:
            case "GetNextDhbwLecture":
                # call function
                print("COMMAND: GetNextDhbwLecture")
                return
            case "GetNewsOfToday":
                # call function
                print("COMMAND: GetNewsOfToday")
                return
            case "GetLastReceivedEmail":
                # call function
                print("COMMAND: GetLastReceivedEmail")
                return
            case "GetDeutscheBahnTrainOrBus":
                # call function
                self.featureComposite.call_feature_method("getNextPlannedDbConnection")
                print("COMMAND: GetDeutscheBahnTrainOrBus")
                return
            # ...
            case _:
                print("COMMAND: I don't know what to do?")
                return
