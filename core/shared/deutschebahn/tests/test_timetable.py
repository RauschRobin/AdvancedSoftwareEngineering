import json
from ..helper.timetable import FilterByDestination, FilterByLine, SimpleTimetable

def test_simple_timetable():
    timetable_data = {"station": "Stuttgart Hbf (tief)", "timetable": [{"entry1": "data1"}, {"entry2": "data2"}]}
    simple_timetable = SimpleTimetable(timetable_data)
    assert simple_timetable.data() == timetable_data


def test_filter_by_line():
    timetable_data = {"station": "Stuttgart Hbf (tief)", "timetable": [{"ar": {"l": "1"}}, {"ar": {"l": "2"}}]}
    timetable = SimpleTimetable(timetable_data)
    filtered_timetable = FilterByLine(timetable, "1")

    expected_result = {"station": "Stuttgart Hbf (tief)", "timetable": [{"ar": {"l": "1"}}]}
    assert filtered_timetable.data() == json.dumps(expected_result)

def test_filter_by_destination():
    timetable_data = {"station": "Stuttgart Hbf (tief)", "timetable": [{"dp": {"ppth": "Stuttgart Nürnberger Str.|Stuttgart-Sommerrain"}}, {"dp": {"ppth": "Stuttgart-Bad Cannstatt|Stuttgart Nürnberger Str.|Stuttgart-Sommerrain"}}]}
    timetable = SimpleTimetable(timetable_data)
    filtered_timetable = FilterByDestination(timetable, "Stuttgart-Bad Cannstatt")
    
    expected_result = {"station": "Stuttgart Hbf (tief)", "timetable": [{"dp": {"ppth": "Stuttgart-Bad Cannstatt|Stuttgart Nürnberger Str.|Stuttgart-Sommerrain"}}]}
    assert filtered_timetable.data() == json.dumps(expected_result)


