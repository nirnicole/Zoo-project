from objects.animals.aquatic import Acuatic
from objects.consts import *

class Clownfish(Acuatic):

    def __init__(self, args):
        Acuatic.__init__(self, args)
        self.favorite_food = CLOWNFISH_FOOD
        self.daily_consumption = DAILY_CONS_CLOWNFISH