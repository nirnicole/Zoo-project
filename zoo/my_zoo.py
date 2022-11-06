from facilities.animal_cages import AnimalCages
from facilities.food_storage import FoodStorage
from facilities.worker_office import WorkManager
from zoo.load_data import animals_data as ad
from zoo.load_data import employees_data as ed
from zoo.load_data import supplies_data as sd
from zoo import zoo_scenerios as zs

class Zoo():
    
    def __init__(self):
        self.animal_cages = AnimalCages()
        self.work_manager = WorkManager()
        self.supplies = FoodStorage()
        self.date = 1
        self.build_zoo()


    def build_zoo(self):
        self.work_manager.update_facilities( [self.animal_cages, self.supplies])
        self.supplies.buy_supplies(sd)
        self.animal_cages.add_animals(ad)
        self.work_manager.hire_workers(ed)
        
    def run(self, duration = 1):
        while duration > 0:
            zs.good_day_flow(self)
            duration -= 1

    def status(self):
        print(self.get_date())
        self.supplies.print()
        self.animal_cages.print()   

    def get_date(self):
        return f"\nDay {self.date}:"