# ItemsAccessor Documentation

## Basic Usage

1. Store the items as a dictionary via get_item_dictionary()

2. Transform the dictionary into a json-string by using convert_dictionary_to_json() and return it.


## Methods

The following methods are available:

- get_item_dictionary()
- convert_dictionary_to_json()


### get_item_dictionary
Gets items and returns them as a dictionary

Parameter: self
Returns: dict


### convert_dictionary_to_json
Converty dictionary of get_item_dictionary() into JSON

Parameter: self
Returns: str


# AppContext Documentation
    
## Basic Usage
Class to implement Flask as Singleton to prohibit flask to run more than once

## Methods
The following methods are available:
- \__init__()
- app()

### __init__
Prevents call of standard-constructor

### app:
Classmethod. Constructor to instantiate as Singleton-object

Parameter: class
Returns: object



# InventoryManager Documentation


## Basic Usage

1. Start InventoryManager

2. Flask is building the Web-API

3. By calling ItemAcessor the InventoryManager-object manages access to inventory

4. Returns the data fetched from ItemAcessor-object from the index-route

## Methods

The following methods are available:

- index()
- get_json()


### index

Returns index-route

Parameter: self

### get_json

Calls ItemsAccessor() to access items and converts them into a json-object

Parameter: self
Returns: str
