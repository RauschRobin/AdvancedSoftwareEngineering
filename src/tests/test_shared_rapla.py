from ..core.shared.rapla.rapla import Rapla

# Create a sample timetable for testing
sample_timetable = {
    "monday": [
        {"lecture": {"date": "2023-11-27", "time_start": "09:00", "time_end": "10:00", "subject": "Math", "prof": "Dr. Smith", "room": "Room 101"}}
    ],
    "tuesday": [],
    "wednesday": [],
    "thursday": [],
    "friday": [],
    "saturday": [],
    "sunday": []
}

class TestRapla:
    def test_compareTimetablesAndRespondWithLecturesThatChanged(self):
        # Create two identical timetables
        timetable1 = sample_timetable
        timetable2 = sample_timetable

        # Create an instance of Rapla
        rapla_instance = Rapla("http://example.com")

        # Call the method to test
        result = rapla_instance.compareTimetablesAndRespondWithLecturesThatChanged(timetable1, timetable2)

        # Assert the result
        assert result == []

    def test_isLectureFirstOfTheDay(self):
        # Create an instance of Rapla
        rapla_instance = Rapla("http://example.com")

        # Call the method to test
        lecture = {
            "lecture": {"date": "2023-11-27", "time_start": "09:00", "time_end": "10:00", "subject": "Math", "prof": "Dr. Smith", "room": "Room 101"}
        }
        result = rapla_instance.isLectureFirstOfTheDay(lecture)

        # Assert the result
        assert result is True
