from objects.foods.food import Food
from objects.consts import *

class Algae(Food):

    def __init__(self, args):
        Food.__init__(self, "Algae", args["quentity"])