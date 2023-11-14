from flask import Flask
from flask_classful import FlaskView
import ItemsAccessor as ia


app = Flask(__name__)

class InventoryManager(FlaskView):
    """Class to manage access to inventory
    """
    def index(self):
        return self.get_json()
    
    def get_json(self):
        accessor = ia.ItemsAccessor()
        json_data = accessor.convert_dictionary_to_json()

        return json_data


InventoryManager.register(app, route_base = '/')


if (__name__ == "__main__"):
    app.run(debug=True)
