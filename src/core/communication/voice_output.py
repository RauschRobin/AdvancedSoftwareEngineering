from ..shared.YamlFetcher.YamlFetcher import YamlFetcher
import os
import threading
import re
from dotenv import load_dotenv
from elevenlabs import *

output_file = os.path.join(os.path.dirname(__file__), "output.mp3")

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class VoiceOutput(metaclass=SingletonMeta):
    def __init__(self, stop_listening_event:threading.Event, language='de'):
        '''
        Initializes the VoiceOutput class.

        Parameters: language - String (optional)
        Returns: None
        '''
        self.stop_listening_event = stop_listening_event
        self.language = language
        self.is_running = False
        self.speech_thread = None
        self.lock = threading.Lock()
        self.message_queue = []

    def start(self):
        '''
        Starts the VoiceOutput class.

        Parameters: None
        Returns: None
        '''
        self.is_running = True
        self.speech_thread = threading.Thread(target=self.speak)
        self.speech_thread.start()
        user_name = YamlFetcher.fetch('user-name', "preferences.yaml")
        self.add_message("Hallo " + user_name)

    def stop(self):
        '''
        Starts the VoiceOutput class.

        Parameters: None
        Returns: None
        '''
        self.is_running = False
        if self.speech_thread and self.speech_thread.is_alive():
            self.speech_thread.join()

    def speak(self):
        '''
        Starts the loop to read out the message_queue.

        Parameters: None
        Returns: None
        '''
        load_dotenv()
        api_key=os.getenv('ELEVENLABS_KEY')
        set_api_key(api_key)
        while self.is_running:
            if self.message_queue:
                self.stop_listening_event.set()
                text = self.message_queue.pop(0)
                print("VoiceOutput: " + text)
                self.text_to_speech(text)
                self.stop_listening_event.clear()

    def add_message(self, message):
        '''
        Adds a message to the message_queue.

        Parameters: message - String
        Returns: None
        '''
        message = message.strip()
        if message:
            with self.lock:
                self.message_queue.append(message)

    def remove_unpronounceable_characters(self, input_string):
        '''
        Removes unpronounceable characters from strings (like &/($% etc.) and replaces special characters like ':' with 'Uhr' if it represents a time, otherwise replaces with '.'.

        Parameters: input_string - String
        Returns: cleaned_string - String
        '''
        # List of characters that gTTS may not pronounce correctly
        unpronounceable_characters = '|&^%$#@!,'

        # Define a dictionary of special characters and their replacements
        special_characters = {
            ':': 'Uhr'  # Replace ':' with 'Uhr' if it represents a time
        }

        # Use regular expressions to find time expressions
        time_expressions = re.findall(r'\d+:\d+', input_string)

        # Replace ':' with 'Uhr' within time expressions
        for time_expression in time_expressions:
            input_string = input_string.replace(time_expression, time_expression.replace(':', 'Uhr'))

        # Use regular expressions to replace unwanted characters
        cleaned_string = re.sub(r'[{}]'.format(re.escape(unpronounceable_characters)), ' ', input_string)

        # Replace special characters defined in the dictionary
        for char, replacement in special_characters.items():
            if char == ':' and not self.is_time(input_string):
                replacement = '.'  # Replace ':' with '.' if it doesn't represent a time
            cleaned_string = cleaned_string.replace(char, replacement)

        return cleaned_string

    def is_time(self, input_string):
        '''
        Checks if the input string represents a time in the format HH:MM.

        Parameters: input_string - String
        Returns: is_time - Boolean
        '''
        time_pattern = r'^\d{2}:\d{2}$'
        return re.match(time_pattern, input_string) is not None

    def text_to_speech(self, text, filename=output_file):
        '''
        Turns a text into a mp3 file that will be played. 

        Parameters: text - String
                    filename - String (optional)
        Returns: None
        '''
        if text == "":
            raise ValueError("Cannot say ''!")

        text = self.remove_unpronounceable_characters(text)
        audio_stream = generate(text, voice="George", stream=True, model="eleven_multilingual_v2", latency=4)
        stream(audio_stream)
        return
