import yaml

class PreferencesFetcher:
    @staticmethod
    def fetch(key, filepath="preferences.yaml"):
        with open(filepath, 'r') as file:
            preferences = yaml.safe_load(file)
            return preferences['user_preferences'][key]
