class Invetory():
    
    def __init__(self):
        self.invetory = {}

    def add(self, catagory, item):
        self.invetory.setdefault(catagory, []).append(item)

    def pop(self, catagory):
        if catagory in list(self.invetory.keys()):
            if len(self.invetory[catagory])>0 :
                return self.invetory[catagory].pop()
        return None

    def get_by_catagory(self, catagory):
        if catagory in list(self.invetory.keys()):
            return self.invetory[catagory]
        return []


    def get_all(self):
        return self.invetory

    def clear_all(self):
        self.invetory = {}

    def activate(self, catagory, item=None):
        if item == None:
            for c in self.invetory[catagory]:
                c.run()
        else:
            self.invetory[catagory].find(item).run()
    
    def activate_all(self):
        for catagory in self.invetory:
            for item in self.invetory[catagory]:
                item.run()
