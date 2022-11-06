from facilities.facility import Facility
from facilities.invetories.foods import FoodInvetory

class FoodStorage(Facility):

    def __init__(self):
        self.invetory = FoodInvetory()

    def buy_supplies(self, all_food):
        super().add_items(all_food, 'foods')


    def use_supplies(self, food):
        return self.invetory.pop(food)

