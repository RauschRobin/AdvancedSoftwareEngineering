# Carschten
Carschten is our AI based assistant. This is a project from the lecture advanced software engineering. 

## Dependencies
To install the dependencies, please execute `pip install -r requirements.txt`
Please note that macos users need to install a different version for the playsound package: `pip install playsound==1.3.0`

tg: Ich habe ein Virtual Environment mit pyenv angelegt:
- https://blog.teclado.com/how-to-use-pyenv-manage-python-versions/
- enable venv mit `source .venv/bin/activate`
- run `pip install -r requirements.txt`

## Tests
To run the tests, execute `pytest`.
If you want to know more about the code coverage, please execute:
```
coverage run --source "PATH_TO_ROOT_FOLDER" -m pytest   
coverage report
```

## API Keys
The private API keys are stored in a extra yaml file next to the `preferences.yaml` called `API_Keys.yaml`.
These keys must be generated individually from each user.