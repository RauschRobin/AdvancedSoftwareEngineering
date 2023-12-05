from ..core.shared.Chat_GPT.ChatGPT import ChatGpt
import pytest

def test_chat_gpt_initialization():
    chat_gpt = ChatGpt()
    assert chat_gpt is not None

def test_chat_gpt_generate_response(monkeypatch):
    # Mock the get_response method to avoid actual API requests
    def mock_get_response(self, message):
        return "Mocked response"

    # Apply the monkeypatch to replace the actual method with the mock
    monkeypatch.setattr(ChatGpt, 'get_response', mock_get_response)

    chat_gpt = ChatGpt()
    message = "Hello, how are you?"
    response = chat_gpt.get_response(message)

    assert isinstance(response, str)
    assert response != ""

@pytest.fixture
def example_response_content():
    # Provide a sample response content for testing
    return "This is some text before the JSON content {\"key\": \"value\"} and some text after."

def test_extract_json_code_with_valid_content(example_response_content):
    gpt = ChatGpt()  # Create an instance of your class

    # Call the function with valid JSON content
    json_code = gpt.extract_json_code(example_response_content)

    # Perform assertions
    assert json_code is not None
    assert len(json_code) == 1

def test_extract_json_code_with_no_json_content():
    gpt = ChatGpt()  # Create an instance of your class

    # Call the function with no JSON content
    json_code = gpt.extract_json_code("This is a response with no JSON content.")

    # Perform assertions
    assert json_code is None

def test_extract_json_code_with_invalid_json_content():
    gpt = ChatGpt()

    # Call the function with invalid JSON content
    json_code = gpt.extract_json_code("This is not a valid JSON content.")

    # Perform assertions
    assert json_code is None
