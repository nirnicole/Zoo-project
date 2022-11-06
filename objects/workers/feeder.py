from objects.workers.employee import Employee
from objects.consts import *

class Feeder(Employee):

    def __init__(self, args):
        Employee.__init__(self, "Feeder", args["name"])
        self.feed_map = {
            "lion": LION_FOOD,
            "whale": WHALE_FOOD,
            "clownfish": CLOWNFISH_FOOD,
            "goose": GOOSE_FOOD,
            "owl": OWL_FOOD
        }
        self.shop_map = {
            "meat": MEAT_SHOP_AMT,
            "plankton": PLANKTON_SHOP_AMT,
            "algae": ALGAE_SHOP_AMT,
            "seeds": SEEDS_SHOP_AMT,
            "worms": WORMS_SHOP_AMT
        }

    def work(self):
        super().work()
        self.feed()

    def assign_facility(self, cages):
        self.assigned_cages = cages

    def feed(self):
        animal_cages = self.assigned_facilities["AnimalCages"]
        food_storage = self.assigned_facilities["FoodStorage"]
        for catagory, animal_list in animal_cages.get_cages().items():
            food_type = self.feed_map[catagory]
            for animal in animal_list:
                food_bag = None
                while food_bag == None:
                    food_bag = food_storage.use_supplies(food_type)                
                    print(ATTEMPT_FEED, animal.type,' ', animal.name)
                    if food_bag:
                        animal.append_food(food_bag)
                        print(SUCCESS_FEED, food_type)
                    else:
                        print(REFILL_MSG, food_type)
                        self.refill_Stock(food_type, 2)

    def refill_Stock(self, food_type, amount):
        food_storage = self.assigned_facilities["FoodStorage"]
        food_bag = {"name": "bag of food", "quentity": self.shop_map[food_type]}
        shopping_list = {}
        while amount > 0:        
            shopping_list.setdefault(food_type, []).append(food_bag)
            food_storage.buy_supplies(shopping_list)
            amount -=1

    def report_hours(self):
        pass
        