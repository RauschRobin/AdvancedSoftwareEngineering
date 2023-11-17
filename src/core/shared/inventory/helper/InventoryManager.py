import json
from flask import Flask
from flask_classful import FlaskView


class ItemsAccessor:
    """Class to access and convert the items.csv-file"""

    def get_item_dictionary(self):
        """Gets items and returns them as a dictionary

        Parameter: self
        Returns: dict
        """
        data_dict = {}
        data_dict[0] = {'Item': 'Potatoes', 'Quantity': '2', 'Unit': 'kg'}
        data_dict[1] = {'Item': 'Spaghetti', 'Quantity': '500', 'Unit': 'g'}
        data_dict[2] = {'Item': 'Tomatoes', 'Quantity': '250', 'Unit': 'g'}
        data_dict[3] = {'Item': 'Tomato Paste',
                        'Quantity': '100', 'Unit': 'ml'}
        data_dict[4] = {'Item': 'Flour', 'Quantity': '500', 'Unit': 'g'}
        data_dict[5] = {'Item': 'Kidney Beans', 'Quantity': '250', 'Unit': 'g'}
        data_dict[6] = {'Item': 'Vinegar', 'Quantity': '1', 'Unit': 'l'}

        return data_dict

    def convert_dictionary_to_json(self):
        """Converty dictionary of get_item_dictionary() into JSON

        Parameter: self
        Returns: str
        """
        data_dictionary = self.get_item_dictionary()
        json_data = json.dumps(data_dictionary, ensure_ascii=False)
        return json_data


app = Flask(__name__)


class InventoryManager(FlaskView):
    """Class to manage access to inventory
    """

    def index(self):
        """Returns index-route
        """
        return self.get_json()

    def get_json(self):
        """Calls ItemsAccessor() to access items
        and converts them into a json-object

       Parameter: self
        Returns: str
        """
        accessor = ItemsAccessor()
        json_data = accessor.convert_dictionary_to_json()

        return json_data


InventoryManager.register(app, route_base='/')


if (__name__ == "__main__"):
    app.run(port=8000, debug=True)
