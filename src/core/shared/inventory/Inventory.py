import os
from threading import Thread
import pandas


class Inventory:
    """Returns the inventory
    """
    def init_inventory(self):
        try:
            if (os.name == 'nt'):
                os.system("cd helper && python InventoryManager.py")
            elif (os.name == 'posix'):
                os.system("cd helper; python InventoryManager.py")
        except Exception as e:
            print(e)

    def start_thread(self):
        thread = Thread(target=self.init_inventory)
        thread.daemon = True
        thread.start()
        return thread

    def call_url(self):
        self.start_thread()
        json_data = pandas.read_json("http://127.0.0.1:5000/")
        return json_data
    




print(Inventory().call_url())
