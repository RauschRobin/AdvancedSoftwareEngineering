# Terminplaner

This module provides a Python class, ChatGpt, which represents an instance of the OpenAI GPT-3.5-turbo model for generating chat-based responses. The class includes methods for initializing the instance and obtaining responses from the model.

## Class Methods

### `__init__()`

Initializes the 'Terminplaner' class.

**Parameters:** 
- `voice_output` (VoiceOutput): An instance of the VoiceOutput class.

**Returns:** 
- None

### `run(self)`

Starts the while loop of this feature, periodically checking if the current time is within a specified range to trigger activity suggestions.

**Parameters:** 
- None

**Returns:** 
- None

### `is_time_in_range(start_time, end_time)`

Checks if the current time is within a specified time range.

**Parameters:** 
- `start_time` (string): The start time of the range.
- `end_time` (string): The end time of the range.

**Returns:** 
- `True` if the current time is within the specified range; otherwise, `False`.

### `find_activity(self)`

Finds possible activities for the user's free time, taking into account the current weather and class schedule.

**Parameters:** 
- None

**Returns:** 
- None

### `find_place(self, activity=None)`

Finds possible locations for a specific activity or for the previously identified activity.

**Parameters:** 
- `activity` (string, optional): The specific activity for which locations are to be found.

**Returns:** 
- None

## Example Usage

```
from ...communication.voice_output import VoiceOutput
from ...shared.Terminplaner import Terminplaner

# Create an instance of VoiceOutput
voice_output = VoiceOutput()

# Create an instance of Terminplaner
terminplaner = Terminplaner(voice_output)

# Run the Terminplaner feature
terminplaner.run()
```
