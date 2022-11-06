from objects.foods.food import Food
from objects.consts import *

class Plankton(Food):
    def __init__(self, args):
        Food.__init__(self, "Plankton", args["quentity"])