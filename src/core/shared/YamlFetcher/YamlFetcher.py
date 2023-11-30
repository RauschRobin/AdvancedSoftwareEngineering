import yaml


class YamlFetcher:
    '''
    This class allows the fetching of preferences or api keys from yaml files.
    '''

    @staticmethod
    def fetch(key, filepath):
        '''
        This method fetches a value from a yaml file with its key.

        Parameters: key - string
                    filepath - string (optional)
        Returns: value - string
        '''
        try:
            with open(filepath, 'r') as file:
                preferences = yaml.safe_load(file)
                if 'user_preferences' in preferences and key in preferences['user_preferences']:
                    return preferences['user_preferences'][key]
                elif 'api_keys' in preferences and key in preferences['api_keys']:
                    return preferences['api_keys'][key]
                else:
                    raise KeyError(
                        f"Key '{key}' not found in preferences file")
        except FileNotFoundError:
            raise FileNotFoundError(f"Preferences file '{filepath}' not found")
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing preferences file: {e}")
