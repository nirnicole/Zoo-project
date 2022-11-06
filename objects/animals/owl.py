from objects.animals.bird import Bird
from objects.consts import *

class Owl(Bird):

    def __init__(self, args):
        Bird.__init__(self, args)
        self.favorite_food = OWL_FOOD
        self.daily_consumption = DAILY_CONS_OWL