from objects.foods.food import Food
from objects.consts import *

class Meat(Food):

    def __init__(self, args):
        Food.__init__(self, "Meat", args["quentity"])