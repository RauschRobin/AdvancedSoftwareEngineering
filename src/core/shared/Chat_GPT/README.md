# ChatGpt

This module provides a Python class, ChatGpt, which represents an instance of the OpenAI GPT-3.5-turbo model for generating chat-based responses. The class includes methods for initializing the instance and obtaining responses from the model.

## Class Methods

### `__init__()`

Initializes the ChatGpt class, creating an instance with an OpenAI client for API communication.

**Parameters:** 
- None

**Returns:** 
- None

### `get_response(request)`

Generates a response using ChatGpt based on the user's input.

**Parameters:** 
- `request` (string): The user's input or request.

**Returns:** 
- `answer` (string): The generated response from ChatGpt.

## Example Usage

```
# Instantiate the ChatGpt class
chatbot = ChatGpt()

# Get a response for a user request
user_request = "Tell me a joke."
response = chatbot.get_response(user_request)
print(response)
```
