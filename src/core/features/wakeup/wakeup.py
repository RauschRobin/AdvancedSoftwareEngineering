import time
import datetime
import json
from ...shared.rapla.rapla import Rapla
from ...communication.voice_output import VoiceOutput
from ...shared.deutschebahn.deutschebahn import DeutscheBahn
from ...shared.PreferencesFetcher.PreferencesFetcher import PreferencesFetcher
from ...shared.rapla.DateParser import DateParser as dp

class WakeUpAssistant:
    def __init__(self, voice_output:VoiceOutput):
        self.voice_output = voice_output
        rapla_url = PreferencesFetcher.fetch("rapla-url")
        self.rapla = Rapla(rapla_url)
        self.deutsche_bahn = DeutscheBahn()
        self.wakeUpTimeNeeded = PreferencesFetcher.fetch("wake-up-time-in-minutes")
        self.timeToWalkToUniversity = PreferencesFetcher.fetch("time-to-walk-to-university")
        self.currentWeekTimeTable = json.loads(self.rapla.fetchLecturesOfWeek(dp.get_current_calendar_week(), datetime.datetime.now().isocalendar()[0]))
        self.currentCalendarWeek = dp.get_current_calendar_week()
        self.localTrainStationDetails = self.deutsche_bahn.getStationDetailByStationname("Ludwigsburg")
        self.getWakeUpTimeForNextLecture()

    def run(self):
        self.startWakeUpAssistant()

    def startWakeUpAssistant(self):
        if self.voice_output == None:
            print("No voice output!")
            raise SystemError("WakeUp has no instance of VoiceOutput")
        
        while True:
            now = datetime.datetime.now()
            if now.hour == 12 and now.minute == 26:
                message = "Good morning! It's 8:00 AM."
                self.voice_output.add_message(message)
            if self.currentCalendarWeek != dp.get_current_calendar_week():
                self.currentCalendarWeek = dp.get_current_calendar_week()
                self.currentWeekTimeTable = json.loads(self.rapla.fetchLecturesOfWeek(dp.get_current_calendar_week(), datetime.datetime.now().isocalendar()[0]))

            time.sleep(60)  # Sleep for 1 minute before checking again

    def getNextPlannedDbConnection(self):
        self.voice_output.add_message("Dein nächster Zug kommt in 20 Minuten auf Gleis 7 und fährt nach Bietigheim-Bissingen")

    def getNextLecture(self):
        '''
        This function reads the rapla timetable and returns the next upcoming lecture. The lecture can also be next week. 

        Parameters: None
        Returns: dictionary (JSON)
        '''
        nextLecture = None
        current_week = dp.get_current_calendar_week()
        current_datetime = datetime.datetime.now()
        current_timetable = self.currentWeekTimeTable
        while nextLecture == None and current_week < 53:
            for day in current_timetable:
                for lecture in current_timetable[day]:
                    lecture_date = datetime.datetime.strptime(lecture["lecture"]["date"], "%Y-%m-%d")
                    lecture_time_start = datetime.datetime.strptime(lecture["lecture"]["time_start"], "%H:%M")
                    if lecture_date.date() == current_datetime.date() and lecture_time_start.time() >= current_datetime.time() or lecture_date.date() > current_datetime.date():
                        nextLecture = lecture
                        break
            current_week += 1
            current_timetable = json.loads(self.rapla.fetchLecturesOfWeek(current_week, current_datetime.isocalendar()[0]))
        return nextLecture
    
    def getWakeUpTimeForNextLecture(self):
        nextLecture = self.getNextLecture()
        nextTrainToTake = self.getTrainConnectionForLecture(nextLecture)
    
    def getTrainConnectionForLecture(self, lecture):
        lectureStartTime = datetime.datetime.strptime(lecture["lecture"]["time_start"], "%H:%M")
        trainArrivalTime = lectureStartTime - datetime.timedelta(minutes=self.timeToWalkToUniversity)
        print(self.deutsche_bahn.getTimetableByDestinationStationidDateHour("Stuttgart Hbf", self.localTrainStationDetails, "011123", "16"))

# TODO: Implement function to figure our if lecture is first lecture of the day