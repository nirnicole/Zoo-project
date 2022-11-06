from objects.animals.animal import Animal
from objects.consts import *

class Bird(Animal):

    def __init__(self, args):
        Animal.__init__(self, args["type"], args["name"])
        self.wing_span = args["wing"]

    def tweet(Self):
        super().make_sound("tweet")

    def fly(self):
        pass
