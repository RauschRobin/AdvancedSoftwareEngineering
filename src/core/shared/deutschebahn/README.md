# Deutsche Bahn Module

This module provides a simple interface to retrieve station details and timetables from the Deutsche Bahn API.

## Installation

To install the Deutsche Bahn module, use the following pip command:

```bash
pip install deutsche-bahn-module
```

## Usage

### Initialize DeutscheBahn Object

```python
from deutsche_bahn_module import DeutscheBahn

db = DeutscheBahn()
```

### Get Station Details by Station Name

```python
station_name = "Stuttgart Hbf (tief)"
station = db.getStationDetailByStationname(station_name)
print(station)
```

#### Output

```python
# Example Output
{'name': 'Stuttgart Hbf (tief)', 'eva': '8098096', 'db': 'true'}
```

### Get Timetable by Line, Station ID, Date, and Hour

```python
line = "4"
station_id = "8098096"
date = "231025"
hour = "10"

timetable_line = db.getTimetableByLineStationidDateHour(line, station_id, date, hour)
print(timetable_line)
```

### Get Timetable by Destination, Station ID, Date, and Hour

```python
destination = "Bietigheim-Bissingen"
timetable_dest = db.getTimetableByDestinationStationidDateHour(destination, station_id, date, hour)
print(timetable_dest)
```

## API Reference

### `getStationDetailByStationname(station_name: str)`

Returns details of a station based on the provided station name.

### `getTimetableByLineStationidDateHour(line: str, station_id: str, date: str, hour: str)`

Returns JSON data for a given line, station ID, date, and hour.

### `getTimetableByDestinationStationidDateHour(destination: str, station_id: str, date: str, hour: str)`

Returns a timetable for all trains heading to a specific destination at a given station, date, and hour.
