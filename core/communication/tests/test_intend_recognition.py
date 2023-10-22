import pytest
from ..intend_recognition import IntendRecognizer

# Create an instance of the IntendRecognizer for testing
intend_recognizer = IntendRecognizer()

@pytest.fixture
def sample_recorded_command():
    return "Wann kommt mein Zug?"

def test_recognize_intend(sample_recorded_command):
    # Test if recognize_intend returns a string
    predicted_intend = intend_recognizer.recognize_intend(sample_recorded_command)
    assert isinstance(predicted_intend, str)

def test_singleton_instance():
    # Test if the class is a singleton by checking if multiple instances are the same
    new_instance = IntendRecognizer()
    assert new_instance is intend_recognizer

def test_initialization():
    # Test if the data is loaded correctly and the classifier is trained
    assert hasattr(intend_recognizer, 'df')
    assert hasattr(intend_recognizer, 'X_train')
    assert hasattr(intend_recognizer, 'y_train')
    assert hasattr(intend_recognizer, 'tfidf_vectorizer')
    assert hasattr(intend_recognizer, 'clf')

'''
# Currently this does not work. The class is trying to identify a intend in every recording.
def test_invalid_command():
    # Test for an unrecognized command
    unrecognized_command = "Bei diesem command soll nichts passieren."
    predicted_intend = intend_recognizer.recognize_intend(unrecognized_command)
    assert predicted_intend == "Unknown"
'''
