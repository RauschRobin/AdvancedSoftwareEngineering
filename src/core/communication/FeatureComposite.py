from ..features.wakeup.wakeup import WakeUpAssistant
from ..features.ernaehrungsplaner.ernaehrungsplaner import Ernaehrungsplaner
from ..features.news.news import News
from ..features.terminplaner.terminplaner import Terminplaner
import inspect

class FeatureComposite:
    '''
    This class uses Reflection to make it possible to call functions from all feature classes. The main purpose
    of this class is to have a single instance to pass to the voice_input instead of passing around all feature
    instances.
    '''

    def __init__(self, feature_instances):
        '''
        This is the constructor.

        Parameters: list of features created in program.py
        Returns: None
        '''
        self.features = {}
        for feature in feature_instances:
            if isinstance(feature, WakeUpAssistant):
                self.features['wakeup'] = feature
            elif isinstance(feature, Ernaehrungsplaner):
                self.features['ernaehrungsplaner'] = feature
            elif isinstance(feature, News):
                self.features['news'] = feature
            elif isinstance(feature, Terminplaner):
                self.features['terminplaner'] = feature

    def call_feature_method(self, method_name, keyword=""):
        '''
        This function makes it possible to call every function from all of the features. You choose the 
        function by passing the method name as parameter. If it cannot find the function by it's name, it 
        will throw an exception.

        Parameters: method_name - String
        Returns: None
        '''
        for feature_name, feature_instance in self.features.items():
            if hasattr(feature_instance, method_name) and callable(getattr(feature_instance, method_name)):
                method = getattr(feature_instance, method_name)
                if inspect.signature(method).parameters:
                    method(keyword)
                else:
                    method()
                return None
            
        raise AttributeError("FeatureComposite: Could not find a fitting method with that name (& parameters) in your features.")
    