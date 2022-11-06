from objects.zoo_elements import ZooElement
from objects.consts import *

class Food(ZooElement):

    def __init__(self, catagory, quentity):
        ZooElement.__init__(self)
        self.type = catagory
        self.quentity = quentity
        
