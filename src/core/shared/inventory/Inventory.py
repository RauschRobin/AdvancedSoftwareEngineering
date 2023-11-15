import os
from threading import Thread
import requests


class Inventory:
    """Returns the inventory
    """
    def get_rel_path_to_flask(self):
        """Formats the relative path to directory
        of Web-API depending on operating-system

        Parameter: self
        Returns: str
        """
        ret_str = ""
        if (os.name == 'nt'):
            ret_str = "\\src\\core\\shared\\inventory\\helper\\"
        elif (os.name == 'posix'):
            ret_str = "/src/core/shared/inventory/helper/"
        return ret_str

    def get_path_to_flask(self):
        """Returns absolute file path to flask-API

        Parameter: self
        Returns: str
        """
        file_path = os.getcwd()
        file_path = file_path + self.get_rel_path_to_flask()
        return file_path

    def init_flask(self):
        """Initialize the Web-API

        Parameter: self
        Returns: None
        """
        try:
            if (os.name == 'nt'):
                os.system("cd " + self.get_path_to_flask()
                          + " && python InventoryManager.py")
            elif (os.name == 'posix'):
                os.system("cd " + self.get_path_to_flask()
                          + "; python InventoryManager.py")
        except Exception as e:
            print(e)

    def start_thread(self):
        """Run the Web-API as own thread

        Parameter: self
        Returns: thread
        """
        thread = Thread(target=self.init_flask)
        thread.daemon = True
        thread.start()
        return thread

    def call_url(self):
        """Call the URL of the Web-API to get Inventory
        and response object

        Parameter: self
        Returns: response object
        """
        self.start_thread()
        response_obj = requests.get("http://127.0.0.1:8000/")
        return response_obj
