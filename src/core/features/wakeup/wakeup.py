import time
import datetime
import json
import os
import random
from playsound import playsound
from ...shared.rapla.rapla import Rapla
from ...communication.voice_output import VoiceOutput
from ...shared.deutschebahn.deutschebahn import DeutscheBahn
from ...shared.PreferencesFetcher.PreferencesFetcher import PreferencesFetcher
from ...shared.rapla.DateParser import DateParser as dp
from ...shared.Chat_GPT.ChatGPT import ChatGpt

alarm_sound_file = os.path.join(os.path.dirname(__file__), "alarm_sound.mp3")

class WakeUpAssistant:
    '''
    This class is a feature class that is responsible for waking the user up in the morning. It also manages the train and rapla logic.
    '''
    
    def __init__(self, voice_output:VoiceOutput):
        '''
        This is the constructor that sets the voice_output and initializes this class.

        Parameters: voice_output (VoiceOutput)
        Returns: None
        '''
        self.voice_output = voice_output
        self.loadPreferences()
        self.chatgpt = ChatGpt()

        self.rapla = Rapla(self.rapla_url)
        # store current week timetable & calendar week to reduce number of requests
        self.currentCalendarWeek = dp.get_current_calendar_week()
        self.currentWeekTimeTable = json.loads(self.rapla.fetchLecturesOfWeek(self.currentCalendarWeek, datetime.datetime.now().isocalendar()[0]))

        self.deutsche_bahn = DeutscheBahn()
        self.localTrainStationDetails = self.deutsche_bahn.getStationDetailByStationname(self.localTrainStationName)
        self.nextLecture = self.getNextLecture()

    def loadPreferences(self):
        '''
        This methods loads all the preferences used in this class and stores them in variables.

        Parameters: None
        Returns: None
        '''
        self.rapla_url = PreferencesFetcher.fetch("rapla-url")
        self.wakeUpTimeNeeded = PreferencesFetcher.fetch("time-user-needs-between-waking-up-and-arriving-at-local-train-station")
        self.timeItTakesFromHomeStationToUniversity = PreferencesFetcher.fetch("travel-time-from-home-station-to-university-via-train")
        self.localTrainStationName = PreferencesFetcher.fetch("home-train-station-name")

    def run(self):
        '''
        This starts the loop for the wakeup assistant.

        Parameters: None
        Returns: None
        '''
        self.startAndRunWakeUpAssistant()

    def startAndRunWakeUpAssistant(self):
        '''
        This method starts the wakeup assistant loop and checks every minute if it is time to wake up.
        It also handles the logic for deutschebahn and rapla.

        Parameters: None
        Returns: None
        '''
        if self.voice_output == None:
            raise SystemError("WakeUp has no instance of VoiceOutput")
        
        wakeUpTime = None
        while True:
            now = datetime.datetime.now()

            # When a new week begins, the new timetable gets fetched and stored
            if self.currentCalendarWeek != dp.get_current_calendar_week():
                self.currentCalendarWeek = dp.get_current_calendar_week()
                self.currentWeekTimeTable = json.loads(self.rapla.fetchLecturesOfWeek(dp.get_current_calendar_week(), datetime.datetime.now().isocalendar()[0]))
            
            # When the next lecture is today or tomorrow and the time is right, calculate the wakeuptime
            if self.nextLecture["lecture"]["date"] == now.date() or self.nextLecture["lecture"]["date"] == now.date() + datetime.timedelta(days=1) and self.nextLecture["lecture"]["time_start"] <= now.time():
                wakeUpTime = self.getWakeUpTimeForNextMorning()
                if wakeUpTime:
                    self.voice_output.add_message("Morgen musst du um " + wakeUpTime.strftime("%H:%M") + " aufstehen.")

            # Wake the user up if it's wakeuptime
            if wakeUpTime:
                if now.date() == wakeUpTime.date() and now.hour == wakeUpTime.hour and now.minute == wakeUpTime.minute:
                    playsound(alarm_sound_file)
                    self.voice_output.add_message("Guten morgen. Es ist Zeit aufzustehen.")
                    self.getNextLecture()
                    self.getTrainConnectionForNextLecture()
                
            # check if the rapla timetable changed and tell user about it
            if now.minute == 30:
                updatedWeekTimeTable = json.loads(self.rapla.fetchLecturesOfWeek(dp.get_current_calendar_week(), datetime.datetime.now().isocalendar()[0]))
                lectureChanges = self.rapla.compareTimetablesAndRespondWithLecturesThatChanged(self.currentWeekTimeTable, updatedWeekTimeTable)
                if lectureChanges != []:
                    for lecture in lectureChanges:
                        # TODO: improve the voice output message on what lectures have changed
                        self.voice_output.add_message("Diese Vorlesungen haben sich soeben geändert:")
                        self.voice_output.add_message(lecture)
                    self.currentWeekTimeTable = updatedWeekTimeTable

            # update nextLecture every 5 minutes
            if now.minute % 5 == 0:
                self.nextLecture = self.getNextLecture()

            time.sleep(60)  # Sleep for 1 minute before checking again

    def getNextLecture(self):
        '''
        This function reads the rapla timetable and returns the next upcoming lecture. The lecture can also be next week. 
        If there is no upcoming lecture in rapla for the rest of the current year, it will return None.

        Parameters: None
        Returns: dictionary (JSON)
        '''
        current_week = self.currentCalendarWeek
        current_datetime = datetime.datetime.now()
        current_timetable = self.currentWeekTimeTable
        while current_week < 53:
            for day in current_timetable:
                for lecture in current_timetable[day]:
                    lecture_date = datetime.datetime.strptime(lecture["lecture"]["date"], "%Y-%m-%d")
                    lecture_time_start = datetime.datetime.strptime(lecture["lecture"]["time_start"], "%H:%M")
                    if (lecture_date.date() == current_datetime.date() and lecture_time_start.time() >= current_datetime.time()) or lecture_date.date() > current_datetime.date():
                        return lecture
            current_week += 1
            current_timetable = json.loads(self.rapla.fetchLecturesOfWeek(current_week, current_datetime.isocalendar()[0]))
        return None
    
    def getWakeUpTimeForNextMorning(self):
        '''
        This method calculates the wakeup time for the next lecture. If the next lecture is not tomorrow, it will return None.

        Parameters: None
        Returns: wakeuptime (datetime)
        '''
        if self.nextLecture is None:
            print("No upcoming lectures.")
            return None
        
        if self.isLectureFirstOfTheDay(self.nextLecture):
            bestConnection = self.getTrainConnectionForNextLecture()
            if bestConnection is None:
                self.voice_output.add_message("Schlaf einfach mal aus.")
                return None

            wakeupTime = self.trainDepartureTime - datetime.timedelta(minutes=self.wakeUpTimeNeeded)
            date_string = bestConnection['ar']['pt'][:6]
            year = 2000 + int(date_string[:2])
            month = int(date_string[2:4])
            day = int(date_string[4:])
            
            wakeupTime = wakeupTime.replace(year=year, month=month, day=day)

            self.voice_output.add_message("Du musst um " + wakeupTime.strftime("%H:%M") + " aufstehen.")

            return wakeupTime
        else:
            # The lecture is not the first of the day
            self.voice_output.add_message("Frage mich einfach nach deiner nächsten Vorlesung nochmal.")
            return None
    
    def getTrainConnectionForLecture(self, lecture):
        '''
        This method asks for the train connection for a given lecture.

        Parameters: lecture (dictionary)
        Returns: bestConnection (dictionary)
        '''
        lectureStartTime = datetime.datetime.strptime(lecture["lecture"]["time_start"], "%H:%M")
        self.trainDepartureTime = lectureStartTime - datetime.timedelta(minutes=self.timeItTakesFromHomeStationToUniversity)
        nextLectureDate = lecture["lecture"]["date"].replace("-", "")
        parsed_date = datetime.datetime.strptime(nextLectureDate, "%Y%m%d")
        formatted_date = parsed_date.strftime("%y%m%d")
        api_response = json.loads(self.deutsche_bahn.getTimetableByDestinationStationidDateHour("Stuttgart", self.localTrainStationDetails['eva'], formatted_date, self.trainDepartureTime.strftime("%H")))

        if api_response == []:
            print("The deutsche bahn api returned an empty list.")
            self.voice_output.add_message("Frag mich später nochmal. Der gesuchte Zug liegt noch zu weit in der Zukunft und die doofe Deutsche Bahn API gibt mir keine Informationen.")
            return None
        bestConnection = self.getBestConnectionFromDbTimetable(api_response, formatted_date)
        return bestConnection
    
    def getTrainConnectionForNextLecture(self):
        '''
        This method asks for the train connection for the next lecture.

        Parameters: None
        Returns: bestConnection (dictionary)
        '''
        lectureStartTime = datetime.datetime.strptime(self.nextLecture["lecture"]["time_start"], "%H:%M")
        self.trainDepartureTime = lectureStartTime - datetime.timedelta(minutes=self.timeItTakesFromHomeStationToUniversity)
        nextLectureDate = self.nextLecture["lecture"]["date"].replace("-", "")
        parsed_date = datetime.datetime.strptime(nextLectureDate, "%Y%m%d")
        formatted_date = parsed_date.strftime("%y%m%d")
        api_response = json.loads(self.deutsche_bahn.getTimetableByDestinationStationidDateHour("Stuttgart", self.localTrainStationDetails['eva'], formatted_date, self.trainDepartureTime.strftime("%H")))

        if api_response == []:
            print("The deutsche bahn api returned an empty list.")
            self.voice_output.add_message("Frag mich später nochmal. Der nächste Zug liegt noch zu weit in der Zukunft und die doofe Deutsche Bahn API gibt mir keine Informationen.")
            return None
        bestConnection = self.getBestConnectionFromDbTimetable(api_response, formatted_date)

        return bestConnection
    
    def readTrainConnectionForNextLecture(self):
        '''
        Add the train connection for the next lecture to the message_queue of voice_output.

        Parameters: None
        Returns: None
        '''
        self.voice_output.add_message(json.dumps(self.getTrainConnectionForNextLecture()))
        
    def getBestConnectionFromDbTimetable(self, api_response, formatted_date):
        '''
        This method figures out the best connection to take from a given timetable.

        Parameters: api_response (dictionary), formatted_date (string)
        Returns: best_connection (dictionary)
        '''
        # Initialize variables to store the best connection and its departure time
        best_connection = None
        best_departure_time = None

        # Iterate through the connections in the 'timetable'
        for connection in api_response['timetable']:
            pt = connection['ar']['pt']  # Departure time
            departure_time = int(pt[-4:])  # Extract last 4 digits as an integer

            # Check if the departure time is within the allowed range
            if departure_time <= int(self.trainDepartureTime.strftime('%H%M')):
                # Update the best connection if this one is better
                if best_connection is None or departure_time > best_departure_time:
                    best_connection = connection
                    best_departure_time = departure_time

        if best_connection is None:
            print("recursive call: best connection may be in timetable with range of 1 hour earlier")
            api_response = json.loads(self.deutsche_bahn.getTimetableByDestinationStationidDateHour("Stuttgart", self.localTrainStationDetails['eva'], formatted_date, self.trainDepartureTime.strftime("%H") - 1))
            self.getBestConnectionFromDbTimetable(api_response, formatted_date)

        return best_connection

    def isLectureFirstOfTheDay(self, lecture):
        '''
        This method checks if a given lecture is the first one of the day.

        Parameters: lecture (dictionary)
        Returns: boolean
        '''
        # Split the date string into year, month, and day
        year, month, day = map(int, lecture["lecture"]["date"].split('-'))
        week = dp.get_calendar_week(year, month, day)

        timetable = json.loads(self.rapla.fetchLecturesOfWeek(week, year))

        # Get the list of lectures for the same day as the given lecture
        weekday = datetime.date(year, month, day).strftime("%A")
        lectures_for_day = timetable[weekday.lower()]

        # Convert the lecture's start time to a datetime object
        lecture_start_time = datetime.datetime.strptime(lecture["lecture"]["time_start"], '%H:%M')

        # Check if the lecture is the first one of the day
        for other_lecture in lectures_for_day:
            if other_lecture != lecture:
                other_lecture_start_time = datetime.datetime.strptime(other_lecture["lecture"]["time_start"], '%H:%M')
                if lecture_start_time > other_lecture_start_time:
                    return False
        return True
    
    def getLecturesOfEntireWeek(self):
        '''
        Adds the lectures of the entire week to message_queue of voice_output.

        Parameters: None
        Returns: None
        '''
        # TODO: convert json string to grammatically correct text
        self.voice_output.add_message(json.dumps(self.currentWeekTimeTable))

    def readNextDhbwLecture(self):  # OVERKILL: generate text with chatpgt class in the future?
        '''
        This method reads out the next Lecture in formal text.

        Parameters: None
        Returns: None
        '''
        nextLecture = self.nextLecture
        date = nextLecture['lecture']['date']
        time_start = nextLecture['lecture']['time_start']
        time_end = nextLecture['lecture']['time_end']
        subject = nextLecture['lecture']['subject']
        prof = nextLecture['lecture']['prof']
        room = nextLecture['lecture']['room']

        statements = [
            f"Am {date} von {time_start} bis {time_end} findet die Vorlesung über '{subject}' statt, geleitet von Professor {prof}, im Raum {room}.",
            f"Die Vorlesung mit dem Thema '{subject}' wird am {date} von {time_start} bis {time_end} von Professor {prof} im Raum {room} abgehalten.",
            f"Merkt euch den {date}, denn da wird eine Vorlesung mit dem Titel '{subject}' von Professor {prof} in Raum {room} stattfinden, beginnend um {time_start}.",
            f"Am {date} könnt ihr eine Vorlesung über '{subject}' besuchen, die von Professor {prof} von {time_start} bis {time_end} im Raum {room} abgehalten wird.",
            f"Professor {prof} wird am {date} von {time_start} bis {time_end} eine Vorlesung über '{subject}' im Raum {room} geben.",
        ]

        message = random.choice(statements)
        self.voice_output.add_message(message)

'''
EXAMPLE RAPLA WEEK TIMETABLE RESPONSE
    {
        'monday': [
            {'lecture': {'date': '2023-10-30', 'time_start': '09:00', 'time_end': '12:15', 'subject': 'Grundlagen Maschineller Lernverfahren', 'prof': 'Dirk Reichardt', 'room': 'C3.02 Vorlesung'}}, 
            {'lecture': {'date': '2023-10-30', 'time_start': '15:15', 'time_end': '18:30', 'subject': 'Wahlfach "Bioinformatik 1"', 'prof': 'Sabine Gillner', 'room': 'STG-TINF21A'}}
        ], 
        'tuesday': [
            {'lecture': {'date': '2023-10-31', 'time_start': '09:15', 'time_end': '13:00', 'subject': 'Advanced Software Engineering', 'prof': 'Horst Rößler', 'room': 'C3.02 Vorlesung'}}
        ], 
        'wednesday': [
        
        ], 
        'thursday': [
        
        ], 
        'friday': [
            {'lecture': {'date': '2023-11-03', 'time_start': '08:30', 'time_end': '11:00', 'subject': 'IT Architekturen', 'prof': 'Stefan Fütterling', 'room': 'C3.02 Vorlesung'}}, 
            {'lecture': {'date': '2023-11-03', 'time_start': '11:45', 'time_end': '15:00', 'subject': 'Data Warehouse', 'prof': 'Andreas Buckenhofer', 'room': 'C3.02 Vorlesung'}}
        ], 
        'saturday': [
            
        ], 
        'sunday': [
        
        ]
    }
'''

'''
EXAMPLE TRAIN TIMETABLE RESPONSE:
    {'station': 'Ludwigsburg', 'timetable': [
        {'tl': {'f': 'S', 't': 'p', 'o': '800643', 'c': 'S', 'n': '28457'}, 'ar': {'pt': '2311031001', 'pp': '3', 'l': '5', 'ppth': 'Bietigheim-Bissingen|Tamm(Württ)|Asperg'}, 'dp': {'pt': '2311031001', 'pp': '3', 'l': '5', 'ppth': 'Kornwestheim Pbf|Stuttgart-Zuffenhausen|Stuttgart-Feuerbach|Stuttgart Nord|Stuttgart Hbf (tief)|Stuttgart Stadtmitte|Stuttgart Feuersee|Stuttgart Schwabstr.'}}, 
        {'tl': {'f': 'S', 't': 'p', 'o': '800643', 'c': 'S', 'n': '7421'}, 'ar': {'pt': '2311031006', 'pp': '3', 'l': '4', 'ppth': 'Backnang|Burgstall(Murr)|Kirchberg(Murr)|Erdmannhausen|Marbach(Neckar)|Benningen(Neckar)|Freiberg(Neckar)|Favoritepark'}, 'dp': {'pt': '2311031006', 'pp': '3', 'l': '4', 'ppth': 'Kornwestheim Pbf|Stuttgart-Zuffenhausen|Stuttgart-Feuerbach|Stuttgart Nord|Stuttgart Hbf (tief)|Stuttgart Stadtmitte|Stuttgart Feuersee|Stuttgart Schwabstr.'}}, 
        {'tl': {'f': 'S', 't': 'p', 'o': '800643', 'c': 'S', 'n': '28389'}, 'ar': {'pt': '2311031051', 'pp': '3', 'l': '4', 'ppth': 'Marbach(Neckar)|Benningen(Neckar)|Freiberg(Neckar)|Favoritepark'}, 'dp': {'pt': '2311031051', 'pp': '3', 'l': '4', 'ppth': 'Kornwestheim Pbf|Stuttgart-Zuffenhausen|Stuttgart-Feuerbach|Stuttgart Nord|Stuttgart Hbf (tief)|Stuttgart Stadtmitte|Stuttgart Feuersee|Stuttgart Schwabstr.'}}, 
        {'tl': {'f': 'N', 't': 'p', 'o': 'GARE', 'c': 'RE', 'n': '19061'}, 'ar': {'pt': '2311031039', 'pp': '4', 'l': '8', 'ppth': 'Würzburg Hbf|Lauda|Osterburken|Möckmühl|Bad Friedrichshall Hbf|Neckarsulm|Heilbronn Hbf|Bietigheim-Bissingen'}, 'dp': {'pt': '2311031040', 'pp': '4', 'l': '8', 'ppth': 'Stuttgart Hbf'}}, 
        {'tl': {'t': 'p', 'o': 'SBSMEX', 'c': 'MEX', 'n': '19611'}, 'ar': {'pt': '2311031000', 'pp': '4', 'l': '17c', 'ppth': 'Bruchsal|Bruchsal Tunnelstraße|Bruchsal Schlachthof|Heidelsheim Nord|Heidelsheim|Helmsheim|Gondelsheim Schlossstadion|Gondelsheim(Baden)|Diedelsheim|Bretten|Bretten Rechberg|Bretten-Ruit|Knittlingen-Kleinvillars|Ölbronn-Dürrn|Maulbronn West|Ötisheim|Mühlacker|Mühlacker Rößlesweg|Illingen(Württ)|Vaihingen(Enz)|Sersheim|Sachsenheim|Ellental|Bietigheim-Bissingen'}, 'dp': {'pt': '2311031000', 'pp': '4', 'l': '17c', 'ppth': 'Stuttgart Hbf'}}, 
        {'tl': {'t': 'p', 'o': 'SBSMEX', 'c': 'MEX', 'n': '19511'}, 'ar': {'pt': '2311031000', 'pp': '4', 'l': '17a', 'wings': '8241763680225741619-2311030835', 'ppth': 'Pforzheim Hbf|Eutingen(Baden)|Niefern|Enzberg|Mühlacker|Mühlacker Rößlesweg|Illingen(Württ)|Vaihingen(Enz)|Sersheim|Sachsenheim|Ellental|Bietigheim-Bissingen'}, 'dp': {'pt': '2311031000', 'pp': '4', 'l': '17a', 'wings': '8241763680225741619-2311030835', 'ppth': 'Stuttgart Hbf'}}, 
        {'tl': {'f': 'S', 't': 'p', 'o': '800643', 'c': 'S', 'n': '28459'}, 'ar': {'pt': '2311031031', 'pp': '3', 'l': '5', 'ppth': 'Bietigheim-Bissingen|Tamm(Württ)|Asperg'}, 'dp': {'pt': '2311031031', 'pp': '3', 'l': '5', 'ppth': 'Kornwestheim Pbf|Stuttgart-Zuffenhausen|Stuttgart-Feuerbach|Stuttgart Nord|Stuttgart Hbf (tief)|Stuttgart Stadtmitte|Stuttgart Feuersee|Stuttgart Schwabstr.'}}, 
        {'tl': {'f': 'S', 't': 'p', 'o': '800643', 'c': 'S', 'n': '7525'}, 'ar': {'pt': '2311031046', 'pp': '3', 'l': '5', 'ppth': 'Bietigheim-Bissingen|Tamm(Württ)|Asperg'}, 'dp': {'pt': '2311031046', 'pp': '3', 'l': '5', 'ppth': 'Kornwestheim Pbf|Stuttgart-Zuffenhausen|Stuttgart-Feuerbach|Stuttgart Nord|Stuttgart Hbf (tief)|Stuttgart Stadtmitte|Stuttgart Feuersee|Stuttgart Schwabstr.'}}, 
        {'tl': {'f': 'S', 't': 'p', 'o': '800643', 'c': 'S', 'n': '28387'}, 'ar': {'pt': '2311031021', 'pp': '3', 'l': '4', 'ppth': 'Marbach(Neckar)|Benningen(Neckar)|Freiberg(Neckar)|Favoritepark'}, 'dp': {'pt': '2311031021', 'pp': '3', 'l': '4', 'ppth': 'Kornwestheim Pbf|Stuttgart-Zuffenhausen|Stuttgart-Feuerbach|Stuttgart Nord|Stuttgart Hbf (tief)|Stuttgart Stadtmitte|Stuttgart Feuersee|Stuttgart Schwabstr.'}}, 
        {'tl': {'f': 'S', 't': 'p', 'o': '800643', 'c': 'S', 'n': '7423'}, 'ar': {'pt': '2311031036', 'pp': '3', 'l': '4', 'ppth': 'Backnang|Burgstall(Murr)|Kirchberg(Murr)|Erdmannhausen|Marbach(Neckar)|Benningen(Neckar)|Freiberg(Neckar)|Favoritepark'}, 'dp': {'pt': '2311031036', 'pp': '3', 'l': '4', 'ppth': 'Kornwestheim Pbf|Stuttgart-Zuffenhausen|Stuttgart-Feuerbach|Stuttgart Nord|Stuttgart Hbf (tief)|Stuttgart Stadtmitte|Stuttgart Feuersee|Stuttgart Schwabstr.'}}, 
        {'tl': {'t': 'p', 'o': 'SBSMEX', 'c': 'MEX', 'n': '19313'}, 'ar': {'pt': '2311031004', 'pp': '4', 'l': '18', 'ppth': 'Osterburken|Adelsheim Ost|Sennfeld|Roigheim|Möckmühl|Züttlingen|Siglingen|Neudenau|Herbolzheim(Jagst)|Untergriesheim|Bad Friedrichshall Hbf|Neckarsulm|Heilbronn Sülmertor|Heilbronn Hbf|Nordheim(Württ)|Lauffen(Neckar)|Kirchheim(Neckar)|Walheim(Württ)|Besigheim|Bietigheim-Bissingen'}, 'dp': {'pt': '2311031005', 'pp': '4', 'l': '18', 'ppth': 'Stuttgart Hbf|Stuttgart-Bad Cannstatt|Esslingen(Neckar)|Plochingen|Wendlingen(Neckar)|Nürtingen|Metzingen(Württ)|Reutlingen Hbf|Tübingen Hbf'}}, 
        {'tl': {'f': 'S', 't': 'p', 'o': '800643', 'c': 'S', 'n': '7523'}, 'ar': {'pt': '2311031016', 'pp': '3', 'l': '5', 'ppth': 'Bietigheim-Bissingen|Tamm(Württ)|Asperg'}, 'dp': {'pt': '2311031016', 'pp': '3', 'l': '5', 'ppth': 'Kornwestheim Pbf|Stuttgart-Zuffenhausen|Stuttgart-Feuerbach|Stuttgart Nord|Stuttgart Hbf (tief)|Stuttgart Stadtmitte|Stuttgart Feuersee|Stuttgart Schwabstr.'}}, 
        {'tl': {'t': 'p', 'o': 'SBSMEX', 'c': 'MEX', 'n': '19219'}, 'ar': {'pt': '2311031031', 'pp': '4', 'l': '12', 'ppth': 'Heilbronn Hbf|Nordheim(Württ)|Lauffen(Neckar)|Kirchheim(Neckar)|Walheim(Württ)|Besigheim|Bietigheim-Bissingen'}, 'dp': {'pt': '2311031032', 'pp': '4', 'l': '12', 'ppth': 'Stuttgart Hbf|Stuttgart-Bad Cannstatt|Esslingen(Neckar)|Plochingen|Wendlingen(Neckar)|Oberboihingen|Nürtingen|Bempflingen|Metzingen(Württ)|Reutlingen Hbf|Tübingen Hbf'}}
    ]}
'''
