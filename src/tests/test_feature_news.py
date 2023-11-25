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

def test_news_init(news_instance, mocked_voice_output):
    assert news_instance.voice_output == mocked_voice_output
    assert news_instance.tagesschau is not None
    assert news_instance.roundcube is not None
    assert news_instance.newsapi is not None
    assert news_instance.chatgpt is not None
    assert news_instance.interests is not None

def test_get_last_received_email(news_instance, mocked_voice_output):
    news_instance.roundcube.getLastReceivedEmail = lambda: 'Test Email'
    news_instance.getLastReceivedEmail()

    assert mocked_voice_output.add_message.called_once_with('Test Email')

def test_get_news_of_interest(news_instance, mocked_voice_output, monkeypatch):
    # Mocking the dependencies for this specific test
    news_instance.interests = ['test_interest']
    news_instance.newsapi.get_everything = lambda search_keyword, language: {'articles': [{'title': 'Test Article'}]}
    news_instance.chatgpt.get_response = lambda message: 'Test Response'

    # Run the method
    news_instance.getNewsOfInterest()

    # Assertions
    assert mocked_voice_output.add_message.called_once_with('Test Response')

def test_get_news_with_keyword(news_instance, mocked_voice_output, monkeypatch):
    # Mocking the dependencies for this specific test
    news_instance.newsapi.get_everything = lambda search_keyword, language: {'articles': [{'title': 'Test Article'}]}
    news_instance.chatgpt.get_response = lambda message: 'Test Response'

    # Run the method
    news_instance.getNewsWithKeyword('test_keyword')

    # Assertions
    assert mocked_voice_output.add_message.called_once_with('Test Response')

