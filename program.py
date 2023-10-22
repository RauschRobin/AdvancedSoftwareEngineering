import threading
from core.communication.voice_input import VoiceInput
from core.communication.voice_output import VoiceOutput
from core.features.wakeup.wakeup import WakeUpAssistant
from core.features.ernaehrungsplaner.ernaehrungsplaner import Ernaehrungsplaner
from core.features.news.news import News
from core.features.terminplaner.terminplaner import Terminplaner

# Start the voice of carschten
voice_output = VoiceOutput()
voice_output.start()

# Create instances of features --> pass the features the VoiceOutput instance
wakeup = WakeUpAssistant(voice_output)
ernaehrungsplaner = Ernaehrungsplaner(voice_output)
news = News(voice_output)
terminplaner = Terminplaner(voice_output)

# Initialize and start the feature modules
features = [wakeup, ernaehrungsplaner, news, terminplaner]  # Add other feature modules here
threads = []

for feature in features:
    thread = threading.Thread(target=feature.run)
    threads.append(thread)
    thread.start()

# Start the user input handler and pass them the features so that they can be accessed via voice commands
voice_input = VoiceInput(wakeup, ernaehrungsplaner, news, terminplaner)
voice_input.start()

# Main class to coordinate features and user input
class MainApp:
    def __init__(self):
        # Initialize any shared data or variables
        pass

    def run(self):
        # Main logic to coordinate features and user input
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    main_app = MainApp()
    main_app.run()
