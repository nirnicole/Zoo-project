from objects.foods.food import Food
from objects.consts import *

class Seeds(Food):
    def __init__(self, args):
        Food.__init__(self, "Seeds", args["quentity"])