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

- init_flask()
- start_thread()
- call_url()


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
