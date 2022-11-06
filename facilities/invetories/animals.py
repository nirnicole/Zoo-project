from facilities.invetories.invetory import Invetory

class AnimalInvetory(Invetory):
    
    def __init__(self):
        Invetory.__init__(self)

    def stocks_status(self):
        res = {}
        for key, item_list in self.get_all().items():
            res[key] = {"total": len(item_list), "details": {}}
            for item_data in item_list:
                res[key]["details"][item_data.name] = {"health": item_data.health}
                

        return res