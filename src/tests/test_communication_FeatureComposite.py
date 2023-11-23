import pytest
from unittest.mock import MagicMock
from ..core.communication.FeatureComposite import FeatureComposite
from ..core.features.wakeup.wakeup import WakeUpAssistant
from ..core.features.news.news import NewsAPI
from ..core.features.terminplaner.terminplaner import Terminplaner
from ..core.features.ernaehrungsplaner.ernaehrungsplaner import Ernaehrungsplaner

@pytest.fixture
def mock_wakeup():
    return MagicMock(spec=WakeUpAssistant)

@pytest.fixture
def mock_ernaehrungsplaner():
    return MagicMock(spec=Ernaehrungsplaner)

@pytest.fixture
def mock_news():
    return MagicMock(spec=NewsAPI)

@pytest.fixture
def mock_terminplaner():
    return MagicMock(spec=Terminplaner)

@pytest.fixture
def feature_instances(mock_wakeup, mock_ernaehrungsplaner, mock_news, mock_terminplaner):
    return [mock_wakeup, mock_ernaehrungsplaner, mock_news, mock_terminplaner]

def test_feature_composite_initialization(feature_instances):
    feature_composite = FeatureComposite(feature_instances)
    assert len(feature_composite.features) == 3 

def test_call_feature_method_with_existing_method(mock_wakeup):
    mock_wakeup.some_existing_method = MagicMock() 
    feature_instances = [mock_wakeup]
    feature_composite = FeatureComposite(feature_instances)
    feature_composite.call_feature_method("some_existing_method")

def test_call_feature_method_with_nonexistent_method(feature_instances):
    feature_composite = FeatureComposite(feature_instances)
    with pytest.raises(AttributeError):
        feature_composite.call_feature_method("nonexistent_method")
