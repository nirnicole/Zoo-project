from facilities.facility import Facility
from facilities.invetories.animals import AnimalInvetory

class AnimalCages(Facility):

    def __init__(self):
        self.invetory = AnimalInvetory()

    def add_animals(self, all_animales):
        super().add_items(all_animales, 'animals')

    def activate_animals(self):
        self.invetory.activate_all()

    def get_cages(self):
        return self.invetory.get_all()
