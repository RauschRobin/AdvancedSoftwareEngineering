# InventoryManager Documentation

## Basic Usage

1. Start InventoryManager as own thread

2. Flask is building the Web-API

3. By calling ItemAcessor the InventoryManager-object manages access to inventory


## Methods

The following methods are available:

- index()
- get_json()


### index

Returns index-route

Parameter: self

### get_json

Calls ItemsAccessor() to access item.csv and converts it into json-object

Parameter: self
Returns: str


# ItemsAccessor Documentation

## Basic Usage

1. Access and read the file via get_csv_file_path()

2. Convert the input via read_csv_into_dictionary() into a dictionary

3. Transform the dictionary into a json-string by using convert_dictionary_to_json() and return it.


## Methods

The following methods are available:

- get_rel_path()
- get_csv_file_path()
- read_csv_into_dictionary()
- convert_dictionary_to_json()


### get_rel_path
Formats the relative path to directory of items.csv depending on operating-system

Parameter: self
Returns: str


### get_csv_file_path()
Returns absolute file path to csv-file

Parameter: self
Returns: str


### read_csv_into_dictionary
Reads csv and returns it as a dictionary

Parameter: self
Returns: dict


### convert_dictionary_to_json
Converty dictionary of read_csv_into_dictionary() into JSON

Parameter: self
Returns: str
