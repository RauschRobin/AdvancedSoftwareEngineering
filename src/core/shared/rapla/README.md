# rapla.py

This module provides functionality for interacting with the Rapla scheduling system. It includes classes and methods for retrieving, creating, updating, and deleting events in Rapla.

# FILEPATH: DateParser.py

DateParser.py is a Python module that provides functions for parsing and manipulating dates.

The module includes a DateParser class, which allows for parsing dates from various formats and converting them to a standardized format. It also provides methods for comparing dates, calculating the difference between dates, and formatting dates in different styles.

Example usage:
```
parser = DateParser()
date = parser.parse_date("2022-01-01")

formatted_date = parser.format_date(date, style="dd/mm/yyyy")
print(formatted_date)  # Output: 01/01/2022
```
