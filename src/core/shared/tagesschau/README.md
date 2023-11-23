# TagesschauAPI Class

This Python code defines a class named `TagesschauAPI`, which is designed to communicate with the Tagesschau API. The class provides methods to retrieve news information, check for the latest breaking news (`Eilmeldung`), and search for news based on a provided keyword or sentence.

## Class Methods

### `__init__(self)`

The class constructor initializes the `TagesschauAPI` class. It sets the API URL (`api_url`), initializes the `last_eilmeldung` attribute, and calls the `checkForLastEilmeldung` method to get the latest breaking news.

**Parameters:** None
**Returns:** None

### `_make_request(self, endpoint, params=None)`

This internal method is responsible for making requests to the Tagesschau API. It takes an `endpoint` and optional `params` as input, constructs the URL, and sends a GET request. If the response status code is 200 (OK), it returns the JSON content; otherwise, it raises an exception.

**Parameters:** endpoint (string), params (dict)
**Returns:** response (json)

### `getNewsOfToday(self)`

This method retrieves a list of all the news for the current day from the Tagesschau API.

**Parameters:** None
**Returns:** List of news (json)

### `checkForLastEilmeldung(self)`

This method checks if there are new breaking news (`Eilmeldungen`). It iterates through the news of the day, searches for the presence of "Eilmeldung" in the JSON representation of each news item, and returns the last breaking news if found.

**Parameters:** None
**Returns:** Last breaking news (json)

### `searchForNewsWithKeyword(self, keyword)`

This method searches for news containing a specified keyword or sentence by making a request to the Tagesschau API with the provided `keyword`.

**Parameters:** keyword (string)
**Returns:** List of news with the specified keyword (json)

## Usage Example

```python
# Instantiate TagesschauAPI
tagesschau_api = TagesschauAPI()

# Get news of today
today_news = tagesschau_api.getNewsOfToday()

# Check for the last breaking news
last_eilmeldung = tagesschau_api.checkForLastEilmeldung()

# Search for news with a keyword
keyword_news = tagesschau_api.searchForNewsWithKeyword("Python")
