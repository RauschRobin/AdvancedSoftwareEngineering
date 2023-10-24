from ...communication.voice_output import VoiceOutput
# https://pypi.org/project/deutsche-bahn-api/ --> Wenn man das benutzen möchte


# Todo:
# - Add DeutscheBahn API 
# - Request XML Data from deutschebahn api
# - use Adapter Pattern to convert XML to JSON?

# Decorator pattern
# Use default Timetable and decorate the timetable (filtering) by specific usecases
# Component interface
class Timetable:
    def data(self):
        pass

# Concrete Component
class SimpleTimetable(Timetable):
    def data(self):
        return "data" # replace with data from deutschebahn api
    
# Decorator
class TimetableDecorator(Timetable):
    def __init__(self, timetable):
        self.timetable = timetable

    def data(self):
        return self.timetable.data()
    

# Concrete Decorators
class FilterByLine(TimetableDecorator):
    def __init__(self, timetable, line: str):
        super().__init__(timetable)
        self.line = line

    def data(self):
        return self.timetable.data() + f" filtered by Line: {self.line}"
    
class FilterByDestination(TimetableDecorator):
    def __init__(self, timetable, destination: str):
        super().__init__(timetable)
        self.destination = destination

    def data(self):
        return self.timetable.data() + f" filtered by Destination: {self.destination}"

    

class DeutscheBahn:
    def __init__(self, voice_output:VoiceOutput):
        self.voice_output = voice_output

    def getConnection(self):
        self.voice_output.add_message("Bietigheim-Bissingen|Stuttgart Hbf, S5, 12:37")


# Example how to access the timetable and filterd versions
timetable = SimpleTimetable()
print(f"Data: {timetable.data()}") # Output: data

filterd_by_line = FilterByLine(timetable, "S4")
print(f"Data: {filterd_by_line.data()}") # Output: data filtered by Line

filter_by_destination = FilterByDestination(timetable, "Bietigheim-Bissingen")
print(f"Data: {filter_by_destination.data()}") # Output: data filtered by Destination
