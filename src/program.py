import threading
from core.communication.voice_input import VoiceInput
from core.communication.voice_output import VoiceOutput
from core.features.wakeup.wakeup import WakeUpAssistant
from core.features.ernaehrungsplaner.ernaehrungsplaner import Ernaehrungsplaner
from core.features.news.news import News
from core.features.terminplaner.terminplaner import Terminplaner
from core.communication.FeatureComposite import FeatureComposite

# Start the voice of carschten
voice_output = VoiceOutput()
voice_output.start()

# Create instances of features --> pass the features the VoiceOutput instance
wakeup = WakeUpAssistant(voice_output)
ernaehrungsplaner = Ernaehrungsplaner(voice_output)
news = News(voice_output)
terminplaner = Terminplaner(voice_output)

# Initialize and start the feature modules
features = [wakeup, ernaehrungsplaner, news, terminplaner]  # Add all features here
threads = []

for feature in features:
    thread = threading.Thread(target=feature.run)
    threads.append(thread)
    thread.start()

# Create a composite of all features
feature_composite = FeatureComposite(features)

# Pass the composite to the VoiceInput instance
voice_input = VoiceInput(feature_composite)
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
