from objects.zoo_elements import ZooElement
from objects.consts import *

class Employee(ZooElement):

    def __init__(self, catagory, name):
        ZooElement.__init__(self)
        self.type = catagory
        self.name = name
        self.assigned_facilities = {}

    def run(self):
        self.work()

    def work(self):
        print(EMPLOYEE_WORK)
        print(self.to_string())

    def assign_facilities(self, facilities):
        for facility in facilities:
            self.assigned_facilities[facility.__class__.__name__] = facility

    def report_hours(self):
        pass
        