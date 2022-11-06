from objects.animals.animal import Animal
from objects.consts import *

class Acuatic(Animal):

    def __init__(self, args):
        Animal.__init__(self, args["type"], args["name"])
        self.lowest_depth = args["lowest"]

    def swim(self):
        pass