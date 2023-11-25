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
        data_dict[7] = {'Item': 'Carrot', 'Quantity': '300', 'Unit': 'g'}
        data_dict[8] = {'Item': 'Garlic', 'Quantity': '50', 'Unit': 'g'}
        data_dict[9] = {'Item': 'French Lentils',
                        'Quantity': '200', 'Unit': 'g'}
        data_dict[10] = {'Item': 'Celery', 'Quantity': '200', 'Unit': 'g'}
        data_dict[11] = {'Item': 'Bay Leaf', 'Quantity': '5', 'Unit': 'pieces'}
        data_dict[12] = {'Item': 'Thyme', 'Quantity': '15', 'Unit': 'g'}
        data_dict[13] = {'Item': 'Salt', 'Quantity': '100', 'Unit': 'g'}
        data_dict[14] = {'Item': 'Onion', 'Quantity': '150', 'Unit': 'g'}
        data_dict[15] = {'Item': 'Olive Oil', 'Quantity': '250', 'Unit': 'ml'}
        data_dict[16] = {'Item': 'Rice', 'Quantity': '1', 'Unit': 'kg'}
        data_dict[17] = {'Item': 'Sugar', 'Quantity': '500', 'Unit': 'g'}
        data_dict[18] = {'Item': 'Eggs', 'Quantity': '12', 'Unit': 'pieces'}
        data_dict[19] = {'Item': 'Milk', 'Quantity': '2', 'Unit': 'l'}
        data_dict[20] = {'Item': 'Bread', 'Quantity': '1', 'Unit': 'loaf'}
        data_dict[21] = {'Item': 'Butter', 'Quantity': '250', 'Unit': 'g'}
        data_dict[22] = {'Item': 'Cheese', 'Quantity': '200', 'Unit': 'g'}
        data_dict[23] = {'Item': 'Chicken Breasts',
                         'Quantity': '500', 'Unit': 'g'}
        data_dict[24] = {'Item': 'Apples', 'Quantity': '1', 'Unit': 'kg'}
        data_dict[25] = {'Item': 'Bananas', 'Quantity': '6', 'Unit': 'pieces'}
        data_dict[26] = {'Item': 'Tea', 'Quantity': '100', 'Unit': 'g'}
        data_dict[27] = {'Item': 'Coffee', 'Quantity': '200', 'Unit': 'g'}
        data_dict[28] = {'Item': 'Pasta', 'Quantity': '500', 'Unit': 'g'}
        data_dict[29] = {'Item': 'Cereal', 'Quantity': '500', 'Unit': 'g'}

        return data_dict

    def convert_dictionary_to_json(self):
        """Converty dictionary of get_item_dictionary() into JSON

        Parameter: self
        Returns: str
        """
        data_dictionary = self.get_item_dictionary()
        json_data = json.dumps(data_dictionary, ensure_ascii=False)
        return json_data


class AppContext(object):
    _app = None

    def __init__(self):
        raise RuntimeError('call app()')

    @classmethod
    def app(cls):
        if cls._app is None:
            cls._app = Flask(__name__)
        return cls._app


app = AppContext.app()


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
