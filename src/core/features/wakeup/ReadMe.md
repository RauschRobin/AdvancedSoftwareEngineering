# WakeUpAssistant

## Overview
The `WakeUpAssistant` class is a feature class responsible for waking up the user in the morning. It also manages the train and rapla (lecture timetable) logic. The class uses various preferences loaded from a YAML file and interfaces with external APIs for Deutsche Bahn and Rapla.

## Dependencies
- `time`, `datetime`: Python standard library modules for handling time and dates.
- `json`: Python standard library module for JSON parsing.
- `os`: Python standard library module for interacting with the operating system.
- `random`: Python standard library module for generating random numbers.
- `playsound`: A third-party library for playing sound files.
- `...shared.rapla.rapla`, `...communication.voice_output`, `...shared.deutschebahn.deutschebahn`, `...shared.YamlFetcher.YamlFetcher`, `...shared.rapla.DateParser`, `...shared.Chat_GPT.ChatGPT`: Custom modules or external libraries for specific functionalities.

## Class: WakeUpAssistant

### Methods
1. `__init__(self, voice_output: VoiceOutput)`: Constructor method initializing the class with the given `VoiceOutput` instance and loading preferences from a YAML file.
2. `loadPreferences(self)`: Method to load preferences used in the class from a YAML file.
3. `run(self)`: Method to start the loop for the wakeup assistant.
4. `startAndRunWakeUpAssistant(self)`: Method to start the wakeup assistant loop and check every minute if it is time to wake up. It also handles logic for Deutsche Bahn and Rapla.
5. `getNextLecture(self)`: Method to read the Rapla timetable and return the next upcoming lecture.
6. `getWakeUpTimeForNextMorning(self)`: Method to calculate the wakeup time for the next lecture.
7. `getTrainConnectionForLecture(self, lecture)`: Method to ask for the train connection for a given lecture.
8. `getTrainConnectionForNextLecture(self)`: Method to ask for the train connection for the next lecture.
9. `readTrainConnectionForNextLecture(self)`: Method to add the train connection for the next lecture to the message queue of `VoiceOutput`.
10. `getBestConnectionFromDbTimetable(self, api_response, formatted_date)`: Method to figure out the best connection to take from a given Deutsche Bahn timetable.
11. `isLectureFirstOfTheDay(self, lecture)`: Method to check if a given lecture is the first one of the day.
12. `getLecturesOfEntireWeek(self)`: Method to add the lectures of the entire week to the message queue of `VoiceOutput`.
13. `readNextDhbwLecture(self)`: Method to read out the next DHBW lecture in formal text.
