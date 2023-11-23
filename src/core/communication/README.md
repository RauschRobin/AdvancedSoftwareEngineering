# Communication

This folder contains the code related to communication in the Carschten project.

## voice_input.py

This module listens to the voice input and delegates the commands to the Feature Composite. It is responsible for capturing the user's voice commands and passing them to the appropriate feature for further processing.

## FeatureComposite.py

The Feature Composite module is a central component that holds instances of all features in the BetterCarschten project. It is responsible for calling the methods that will handle the voice commands received from the voice_input module. This module acts as a bridge between the voice input and the individual features.

## intent_recognition.py

The intent_recognition module is an AI-based mapping of recorded voice commands onto methods. It uses machine learning techniques to recognize the user's intent based on the voice commands received. This module plays a crucial role in understanding and interpreting the user's commands accurately.

## voice_output.py

The voice_output module is responsible for providing audio feedback to the user. It has a message queue that stores the messages to be read out to the user. This module retrieves the messages from the queue and plays them back to the user, providing necessary information or responses.
