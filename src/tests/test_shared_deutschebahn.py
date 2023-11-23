import unittest
from unittest.mock import patch

from ..core.shared.deutschebahn.deutschebahn import DeutscheBahn


class TestDeutscheBahn(unittest.TestCase):

    @patch('AdvancedSoftwareEngineering.src.core.shared.deutschebahn.deutschebahn.StationRequest')
    def test_get_station_detail_by_stationname(self, mock_station_request):
        # Mock the StationRequest and its return value
        mock_station_request_instance = mock_station_request.return_value
        mock_station_request_instance.execute.return_value = {
            'name': 'Stuttgart Hbf (tief)', 'eva': '8098096', 'db': 'true'}

        # Test the method
        db = DeutscheBahn()
        result = db.getStationDetailByStationname("Stuttgart Hbf (tief)")

        # Assertions
        self.assertEqual(
            result, {'name': 'Stuttgart Hbf (tief)', 'eva': '8098096', 'db': 'true'})
        mock_station_request.assert_called_with("Stuttgart Hbf (tief)")

    @patch('AdvancedSoftwareEngineering.src.core.shared.deutschebahn.deutschebahn.TimetableRequest')
    @patch('AdvancedSoftwareEngineering.src.core.shared.deutschebahn.deutschebahn.SimpleTimetable')
    @patch('AdvancedSoftwareEngineering.src.core.shared.deutschebahn.deutschebahn.FilterByLine')
    def test_get_timetable_by_line_stationid_date_hour(self, mock_filter_by_line, mock_simple_timetable, mock_timetable_request):
        # Setup mocks
        mock_timetable_request_instance = mock_timetable_request.return_value
        mock_timetable_request_instance.execute.return_value = 'raw_data'
        mock_simple_timetable.return_value = 'simple_timetable'
        mock_filter_by_line_instance = mock_filter_by_line.return_value
        mock_filter_by_line_instance.data.return_value = {
            'result': 'filtered_data'}

        # Test the method
        db = DeutscheBahn()
        result = db.getTimetableByLineStationidDateHour(
            "4", "8098096", "231025", "10")

        # Assertions
        self.assertEqual(result, {'result': 'filtered_data'})
        mock_timetable_request.assert_called_with("8098096", "231025", "10")
        mock_simple_timetable.assert_called_with('raw_data')
        mock_filter_by_line.assert_called_with('simple_timetable', "4")

    @patch('AdvancedSoftwareEngineering.src.core.shared.deutschebahn.deutschebahn.TimetableRequest')
    @patch('AdvancedSoftwareEngineering.src.core.shared.deutschebahn.deutschebahn.SimpleTimetable')
    @patch('AdvancedSoftwareEngineering.src.core.shared.deutschebahn.deutschebahn.FilterByDestination')
    def test_get_timetable_by_destination_stationid_date_hour(self, mock_filter_by_destination, mock_simple_timetable, mock_timetable_request):
        # Setup mocks
        mock_timetable_request_instance = mock_timetable_request.return_value
        mock_timetable_request_instance.execute.return_value = 'raw_data'
        mock_simple_timetable.return_value = 'simple_timetable'
        mock_filter_by_destination_instance = mock_filter_by_destination.return_value
        mock_filter_by_destination_instance.data.return_value = {
            'result': 'filtered_data'}

        # Test the method
        db = DeutscheBahn()
        result = db.getTimetableByDestinationStationidDateHour(
            "Bietigheim-Bissingen", "8098096", "231025", "10")

        # Assertions
        self.assertEqual(result, {'result': 'filtered_data'})
        mock_timetable_request.assert_called_with("8098096", "231025", "10")
        mock_simple_timetable.assert_called_with('raw_data')
        mock_filter_by_destination.assert_called_with(
            'simple_timetable', "Bietigheim-Bissingen")
