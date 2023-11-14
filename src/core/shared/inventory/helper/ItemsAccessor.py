import csv
import json


class ItemsAccessor:
    """Class to access and convert the items.csv-file"""

    def read_csv_into_dictionary(self):
        """Reads csv and returns it as a dictionary
        """

        data_dictionary = {}
        i = 0

        with open("items.csv") as item_file:
            items = csv.DictReader(item_file, delimiter="\t")
            for rows in items:
                data_dictionary[i] = rows
                i = i + 1

        return data_dictionary

    def convert_dictionary_to_json(self):
        """Converty dictionary of read_csv_into_dictionary() into JSON
        """

        data_dictionary = self.read_csv_into_dictionary()
        json_data = json.dumps(data_dictionary, ensure_ascii=False)
        return json_data
