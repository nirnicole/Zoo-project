from objects.zoo_elements import ZooElement
from objects.consts import *

class Food(ZooElement):

    def __init__(self, catagory, quentity):
        ZooElement.__init__(self)
        self.type = catagory
        self.quentity = quentity
        
    def to_string(self):
        return f"\nFood of type: {self.__class__.__name__}\nQuentity: '{self.quentity}'\nId: {self.id}"

    def to_json(self):
        return {
            "id": self.id,
            "type": self.__class__.__name__,
            "quentity": self.name,
        }
