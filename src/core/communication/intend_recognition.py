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
        '''
        Initializes the class by loading the dataset and training the model.

        Parameters: None 
        Returns: None
        '''
        self.threshhold = 0.2 # The threshhold for the confidence of the model

        # Get the directory of the script
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, 'dataset_intend_recognition.json')

        # Load the data from the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Convert the data to a Pandas DataFrame
        self.df = pd.DataFrame(data)

        # Shuffle the dataset order to improve the training
        self.df = self.df.sample(frac=1, random_state=42).reset_index(drop=True)

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
        '''
        Takes a new command and predicts the intent of the command. 

        Parameters: recorded_command (string) 
        Returns: predicted_intend (string=function name)
        '''
        # Preprocess and vectorize the recorded command
        recorded_command_tfidf = self.tfidf_vectorizer.transform([recorded_command])

        # Predict the intent
        predicted_intend = self.clf.predict(recorded_command_tfidf)[0]

        confidence = self.clf.predict_proba(recorded_command_tfidf).max()
        print("CONFIDENCE: " + str(confidence))
        
        if confidence > self.threshhold:
            return predicted_intend
        else:
            return "fallback"
