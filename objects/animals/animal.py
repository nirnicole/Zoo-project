from objects.zoo_elements import ZooElement
from objects.consts import *

class Animal(ZooElement):

    def __init__(self, a_type, name):
        ZooElement.__init__(self)
        self.type = a_type
        self.name = name
        self.health = MAX_HEALTH
        self.favorite_food = "*"
        self.personal_supply = []

    def run(self):
        self.eat()
    
    def eat(self):
        food = self.personal_supply.pop() if (len(self.personal_supply) > 0) else None
        if food != None and ( self.favorite_food == "*" or food.type.lower() == self.favorite_food.lower() ):
            self.increase_health(5)
            print(ANIMAL_EAT)
        else:
            self.decrease_health(10)
            print(ANIMAL_DIDNT_EAT)
        print(self.to_string())

    def append_food(self, food):
        self.personal_supply.append(food)

    def update_health(self):
        if self.health > MAX_HEALTH:
            self.health = MAX_HEALTH
        elif self.health < MIN_HEALTH:
            self.health = MIN_HEALTH
            print(ANIMAL_DEAD)
        
    def increase_health(self, value):
        if value>=0 :
            self.health += value
            self.update_health()
        else:
            print(INVALID_INPUT, value)
        return self.health

    def decrease_health(self, value):
        if value>=0 :
            self.health -= value
            self.update_health()
        else:
            print(INVALID_INPUT, value)
        return self.health

        
    def to_string(self):
        return f"Animal of type: {self.type}\nName: '{self.name}'\nHealth: {self.health}\nFavorite food: {self.favorite_food}\nId: {self.id}"

    def to_json(self):
        return {
            "id": self.id,
            "type": self.type,
            "name": self.name,
            "health": self.health
        }
