from importlib import import_module
from facilities.facility import Facility
from facilities.invetories.workers import WorkersInvetory


class WorkManager(Facility):

    def __init__(self):
        self.invetory = WorkersInvetory()
        self.facilities = []


    def hire_workers(self, all_workers):
        super().add_items(all_workers, 'workers')
        for worker in self.invetory.get_by_catagory("feeder"):
            worker.assign_facilities(self.facilities)

    def update_facilities(self, facilities):
        self.facilities += facilities
            
    def activate_all(self):
        for catagory in self.invetory:
            for item in self.invetory[catagory]:
                item.run()

    def activate_workers(self):
        self.invetory.activate_all()

    
