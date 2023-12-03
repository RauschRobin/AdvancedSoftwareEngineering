# Inventory Documentation

## Basic Usage

1. Create a new instance of Inventory

```Python
Inventory()
```

2. Call the method get_inventory()

```Python
Inventory.call_url()
```

3. get_inventory() will initialize a new thread with start_thread()

4. start_thread() will call init_flask(), which will start the Web-API through os-interaction

5. During those calls get_inventory() will wait until server is up (function wait_for_server() will ensure this)

6. get_inventory() will call the specified url and will return a response-object from the flask server


## Methods

The following methods are available:

- def get_rel_path_to_flask()
- def get_path_to_flask()
- init_flask()
- start_thread()
- wait_for_server()
- get_inventory()


### def get_rel_path_to_flask
Formats the relative path to directory of Web-API depending on operating-system

Parameter: self
Returns: str

### def get_path_to_flask
Returns absolute file path to flask-API

Parameter: self
Returns: str

### init_flask

Initialize the Web-API 

Parameter: self
Returns: None


### start_thread()

Start init_flask as own thread

Parameter: self
Returns: thread


### wait_for_server
Wait for the server to start within the specified timeout.

Parameter: url (str)
Returns: bool

### get_inventory
Call the URL of the Web-API to get Inventory and response object

Parameter: self
Returns: str
