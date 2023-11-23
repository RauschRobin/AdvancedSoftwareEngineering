import pytest
from unittest.mock import Mock
from ..core.communication.voice_output import VoiceOutput
from ..core.features.news.news import News

@pytest.fixture
def mocked_voice_output():
    return Mock(spec=VoiceOutput)

@pytest.fixture
def news_instance(mocked_voice_output):
    return News(mocked_voice_output)

def test_news_init(news_instance, mocked_voice_output):
    assert news_instance.voice_output == mocked_voice_output
    assert news_instance.tagesschau is not None
    assert news_instance.roundcube is not None
    assert news_instance.newsapi is not None
    assert news_instance.chatgpt is not None
    assert news_instance.interests is not None
