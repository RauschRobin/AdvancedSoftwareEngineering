import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import os

# This class contains an ai model that can recognize the intent of a users voice command. 
# Currently, this class is not used yet.
# This class is a singleton (DESIGN_PATTERN: You can only create a single instance (only 1) 
# --> train the model at the start of our program by creating a intsance of this class).
class IntendRecognizer:
    _instance = None  # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(IntendRecognizer, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        # Get the directory of the script
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, 'dataset_intend_recognition.json')

        # Load the data from the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Convert the data to a Pandas DataFrame
        self.df = pd.DataFrame(data)

        # Split the dataset into training and testing sets (for simplicity, we use the entire dataset)
        self.X_train = self.df['recorded_voice_command']
        self.y_train = self.df['intent']

        # Initialize and fit a TF-IDF vectorizer
        self.tfidf_vectorizer = TfidfVectorizer()
        self.X_train_tfidf = self.tfidf_vectorizer.fit_transform(self.X_train)

        # Initialize and train a Naive Bayes classifier
        self.clf = MultinomialNB()
        self.clf.fit(self.X_train_tfidf, self.y_train)

    def recognize_intend(self, recorded_command):
        # Preprocess and vectorize the recorded command
        recorded_command_tfidf = self.tfidf_vectorizer.transform([recorded_command])

        # Predict the intent
        predicted_intend = self.clf.predict(recorded_command_tfidf)[0]
        return predicted_intend
