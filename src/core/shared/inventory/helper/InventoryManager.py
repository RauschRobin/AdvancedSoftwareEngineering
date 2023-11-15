from flask import Flask
from flask_classful import FlaskView
from .ItemsAccessor import ItemsAccessor as ia


app = Flask(__name__)

class InventoryManager(FlaskView):
    """Class to manage access to inventory
    """
    def index(self):
        """Returns index-route
        """
        return self.get_json()

    def get_json(self):
        """Calls ItemsAccessor() to access item.csv
        and converts it into json-object

        Parameter: self
        Returns: str
        """
        accessor = ia.ItemsAccessor()
        json_data = accessor.convert_dictionary_to_json()

        return json_data


InventoryManager.register(app, route_base = '/')


if (__name__ == "__main__"):
    app.run(debug=True)
