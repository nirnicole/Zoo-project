from objects.animals.aquatic import Acuatic
from objects.animals.mammal import Mammal
from objects.consts import *

class Whale(Mammal, Acuatic):

    def __init__(self, args):
        Mammal.__init__(self, args)
        Acuatic.__init__(self, args)
        self.favorite_food = WHALE_FOOD
        self.daily_consumption = DAILY_CONS_WHALE