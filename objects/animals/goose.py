from objects.animals.mammal import Mammal
from objects.consts import *

class Goose(Mammal):

    def __init__(self, args):
        Mammal.__init__(self, args)
        self.favorite_food = GOOSE_FOOD
        self.daily_consumption = DAILY_CONS_GOOSE