import json

# Decorator Pattern
# Component interface
class Timetable:
    def __init__(self):
        pass

    def data(self):
        pass

# Concrete Component
class SimpleTimetable(Timetable):
    # Timetable as JSON
    def __init__(self, timetable):
        self.timetable = timetable

    def data(self):
        return self.timetable # replace with data from deutschebahn api
    
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
        # add filter logic by Line
        use_data = self.timetable.data()
        filtered_data = [
            item for item in use_data['timetable']
            if 'ar' in item and 'l' in item['ar'] and item['ar']['l'] == self.line
        ]
                
        filtered_data_json = {
            'station': use_data['station'],
            'timetable': filtered_data
        }

        filtered_data_json = json.dumps(filtered_data_json)
        return filtered_data_json
    
class FilterByDestination(TimetableDecorator):
    def __init__(self, timetable, destination: str):
        super().__init__(timetable)
        self.destination = destination

    def data(self):
        # add filter logic by Destination
        use_data = self.timetable.data()

        if use_data is None:
            return "[]"

        filered_data = [
            item for item in use_data['timetable']
            if self.destination in item['dp']['ppth']
        ]

        filteredJsonData = {
            'station': use_data['station'],
            'timetable': filered_data
        }

        filtered_data_json = json.dumps(filteredJsonData)
        return filtered_data_json
    