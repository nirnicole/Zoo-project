from objects.animals.animal import Animal
from objects.consts import *

class Mammal(Animal):

    def __init__(self, args):
        Animal.__init__(self, args["type"], args["name"])
        self.pregnancy = args["pregnancy"]
