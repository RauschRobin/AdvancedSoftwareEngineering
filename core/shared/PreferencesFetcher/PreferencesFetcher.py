import yaml

class PreferencesFetcher:
    @staticmethod
    def fetch(key, filepath="preferences.yaml"):
        try:
            with open(filepath, 'r') as file:
                preferences = yaml.safe_load(file)
                if 'user_preferences' in preferences and key in preferences['user_preferences']:
                    return preferences['user_preferences'][key]
                else:
                    raise KeyError(f"Key '{key}' not found in preferences file")
        except FileNotFoundError:
            raise FileNotFoundError(f"Preferences file '{filepath}' not found")
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing preferences file: {e}")
