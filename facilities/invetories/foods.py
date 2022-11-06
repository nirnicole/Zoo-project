from facilities.invetories.invetory import Invetory

class FoodInvetory(Invetory):
    
    def __init__(self):
        Invetory.__init__(self)

    def stocks_status(self):
        res = {}
        for key, item_list in self.get_all().items():
            res[key] = {"total": 0, "bags": 0}
            for item_data in item_list:
                res[key]["bags"] += 1
                res[key]["total"] += item_data.quentity

        return res