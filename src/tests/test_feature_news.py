import pytest
from unittest.mock import Mock, patch
from ..core.communication.voice_output import VoiceOutput
from ..core.features.news.news import News
from ..core.shared.newsapiorg.news import NewsAPI

@pytest.fixture
def mocked_voice_output():
    return Mock(spec=VoiceOutput)

@pytest.fixture
def news_instance(mocked_voice_output):
    return News(mocked_voice_output)

# Use patch to mock the YamlFetcher.fetch method
@pytest.fixture
def mock_yaml_fetcher():
    with patch('AdvancedSoftwareEngineering.src.core.shared.YamlFetcher.YamlFetcher.YamlFetcher.fetch', return_value='your_mocked_value'):
        yield

# Apply the mock_yaml_fetcher fixture to your tests
@pytest.mark.usefixtures('mock_yaml_fetcher')
def test_news_init(news_instance, mocked_voice_output):
    assert news_instance.voice_output == mocked_voice_output
    assert news_instance.tagesschau is not None
    assert news_instance.roundcube is not None
    assert news_instance.newsapi is not None
    assert news_instance.chatgpt is not None
    assert news_instance.interests is not None
