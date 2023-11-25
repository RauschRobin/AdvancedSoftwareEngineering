# News Class

This Python code defines a class named `News` that represents a feature providing news-related functionalities. It utilizes various external modules and APIs for fetching and processing news, handling emails, and interacting with a chatbot.

## Class Initialization

### `__init__(self, voice_output: VoiceOutput)`

The constructor initializes the `News` class with instances of different components:
- `voice_output`: An instance of the `VoiceOutput` class for handling voice output.
- `tagesschau`: An instance of `TagesschauAPI` for checking breaking news.
- `roundcube`: An instance of `RoundcubeMock` for checking emails.
- `newsapi`: An instance of `NewsAPI` for retrieving news from a news API.
- `chatgpt`: An instance of `ChatGpt` for interacting with a chatbot.
- `interests`: A list of news interests fetched from a YAML file.

**Parameters:** 
- `voice_output` (VoiceOutput): Instance of the `VoiceOutput` class.
**Returns:** None

## Class Methods

### `run(self)`

Starts the while loop of the news feature by calling `startNewsCheckingLoop()`.

**Parameters:** None
**Returns:** None

### `startNewsCheckingLoop(self)`

Runs the main while loop of the news feature, continuously checking for breaking news, personalized news of interest, and new emails. It also periodically interacts with a chatbot.

**Parameters:** None
**Returns:** None

### `getLastReceivedEmail(self)`

Gets the last received email from the `RoundcubeMock` and adds the message to the `VoiceOutput` message queue.

**Parameters:** None
**Returns:** None

### `getNewsOfInterest(self)`

Gets news of interest based on user preferences and adds the message to the `VoiceOutput` message queue.

**Parameters:** None
**Returns:** None

### `getNewsWithKeyword(self, keyword)`

Gets news with a specific keyword and adds the message to the `VoiceOutput` message queue.

**Parameters:** 
- `keyword` (string): The keyword for which to fetch news.
**Returns:** None

## Usage Example

```python
# Example usage of News class

# Instantiate VoiceOutput
voice_output_instance = VoiceOutput()

# Instantiate News feature
news_feature = News(voice_output_instance)

# Run the news feature
news_feature.run()
