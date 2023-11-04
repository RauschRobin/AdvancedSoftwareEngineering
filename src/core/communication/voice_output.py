from gtts import gTTS
import playsound
import os
import threading
import re
import time

output_file = os.path.join(os.path.dirname(__file__), "output.mp3")

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class VoiceOutput(metaclass=SingletonMeta):
    def __init__(self, language='de'):
        self.language = language
        self.is_running = False
        self.speech_thread = None
        self.lock = threading.Lock()
        self.message_queue = []

    def start(self):
        self.is_running = True
        self.speech_thread = threading.Thread(target=self.speak)
        self.speech_thread.start()

    def stop(self):
        self.is_running = False
        if self.speech_thread and self.speech_thread.is_alive():
            self.speech_thread.join()

    def speak(self):
        while self.is_running:
            if self.message_queue:
                text = self.message_queue.pop(0)
                print("VoiceOutput: " + text)
                self.text_to_speech(text)

    def add_message(self, message):
        message = message.strip()
        if message:
            with self.lock:
                self.message_queue.append(message)

    def remove_unpronounceable_characters(self, input_string):
        # List of characters that gTTS may not pronounce correctly
        unpronounceable_characters = '|&^%$#@!,'

        # Define a dictionary of special characters and their replacements
        special_characters = {
            ':': 'Uhr'  # Replace ':' with 'Uhr'
        }

        # Use regular expressions to replace unwanted characters
        cleaned_string = re.sub(r'[{}]'.format(re.escape(unpronounceable_characters)), ' ', input_string)

        # Replace special characters defined in the dictionary
        for char, replacement in special_characters.items():
            cleaned_string = cleaned_string.replace(char, replacement)
            
        return cleaned_string

    def text_to_speech(self, text, filename=output_file):
        if text == "":
            raise ValueError("Cannot say ''!")

        text = self.remove_unpronounceable_characters(text)

        # Normalize the output file path
        filename = os.path.normpath(filename)

        # Create a text to speech element
        tts = gTTS(text=text, lang=self.language, slow=False)

        # Save the audio file
        tts.save(filename)

        # play the audio file
        playsound.playsound(filename)

        # Delete temporary file
        os.remove(output_file)

        time.sleep(2)
