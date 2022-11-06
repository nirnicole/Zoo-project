from objects.consts import *
from utils.module_operations import get_class

class Facility():

    def __init__(self):
        self.invetory = None

    def add_items(self, data_dict, folder):
        for key, item_list in data_dict.items():
            for item_data in item_list:
                class_str: str = key.strip().capitalize()
                my_class = get_class(f'objects.{folder}.{class_str.lower()}', class_str)
                new_item = my_class(item_data)   #dynamicly creating classes by name given in json data
                self.invetory.add(key, new_item)

    def use_supplies(self, food):
        return self.invetory.delete(food)

    def print(self):
        print(self.invetory.stocks_status())