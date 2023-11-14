import os
import csv
import json


class ItemsAccessor:
    """Class to access and convert the items.csv-file"""

    def get_rel_path(self):
        """Formats the relative path to directory of items.csv
        depending on operating-system

        Parameter: self
        Returns: str
        """
        ret_str = ""
        if (os.name == 'nt'):
            ret_str = "\\src\\core\\shared\\inventory\\helper\\"
        elif (os.name == 'posix'):
            ret_str = "/src/core/shared/inventory/helper/"
        return ret_str

    def get_csv_file_path(self):
        """Returns absolute file path to csv-file

        Parameter: self
        Returns: str
        """
        file_path = os.getcwd()
        file_path = file_path + self.get_rel_path()
        file_path = file_path + "items.csv"

        return file_path

    def read_csv_into_dictionary(self):
        """Reads csv and returns it as a dictionary

        Parameter: self
        Returns: dict
        """

        items_csv = self.get_csv_file_path()
        data_dictionary = {}
        i = 0

        with open(items_csv) as item_file:
            items = csv.DictReader(item_file, delimiter="\t")
            for rows in items:
                data_dictionary[i] = rows
                i = i + 1

        return data_dictionary

    def convert_dictionary_to_json(self):
        """Converty dictionary of read_csv_into_dictionary() into JSON

        Parameter: self
        Returns: str
        """

        data_dictionary = self.read_csv_into_dictionary()
        json_data = json.dumps(data_dictionary, ensure_ascii=False)
        return json_data
