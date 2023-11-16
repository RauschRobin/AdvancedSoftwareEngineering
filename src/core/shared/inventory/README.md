# Inventory Documentation

## Basic Usage

1. Create a new instance of Inventory

```Python
Inventory()
```

2. Call the method call_url()

```Python
Inventory.call_url()
```

3. call_url() will initialize a new thread

```Python
Inventory.start_thread()
```

4. start_thread() will call init_flask(), which will start the Web-API

5. call_url() will return a response-object


## Methods

The following methods are available:

- def get_rel_path_to_flask()
- def get_path_to_flask()
- init_flask()
- start_thread()
- call_url()


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


### call_url
Call the URL of the Web-API to get Inventory and response object

Parameter: self
Returns: response object
