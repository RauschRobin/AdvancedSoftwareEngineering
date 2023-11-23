# Carschten
Introducing Carschten, your all-in-one voice-controlled assistant designed to seamlessly integrate into your daily routine. Imagine starting your day with a personalized wake-up call, where Carschten not only ensures you rise on time but also provides a brief overview of the Deutsche Bahn route for your commute.

As you prepare for the day, Carschten becomes your indispensable companion, updating you on the next lecture at university, suggesting activities based on the weather forecast, and keeping you informed about the latest news and emails. Need help deciding what to eat? Carschten has you covered, offering meal suggestions and even checking your calendar to make sure your dining plans align with your schedule.

With its intuitive voice recognition technology, Carschten effortlessly responds to your commands, making it easy to manage your day hands-free. Stay organized, informed, and on track with Carschten, your personalized assistant for a smoother, more efficient daily life.

Carschten is the result of our group work in the lecture advanced software engineering.

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