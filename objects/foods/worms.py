from objects.foods.food import Food
from objects.consts import *

class Worms(Food):

    def __init__(self, args):
        Food.__init__(self, "Worms", args["quentity"])