import yaml

class YamlFetcher:
    '''
    This class allows the fetching of preferences from a yaml file.
    '''

    @staticmethod
    def fetch(key, filepath):
        '''
        This method fetches a preference from a yaml file.

        Parameters: key - string
                    filepath - string (optional)
        Returns: value - string
        '''
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
