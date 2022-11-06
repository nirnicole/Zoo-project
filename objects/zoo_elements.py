class ZooElement():
    _id = 0

    def __init__(self):
        self.id = self.generate_id()

    def run(self):
        pass

    def get_id(self):
        return type(self)._id

    def set_id(self,val):
        type(self)._id = val

    def generate_id(self):
        self.set_id(self.get_id() + 1)
        return self.get_id()

    def to_string(self):
        res = ""
        attr_value = self.__dict__         
        for att in attr_value:
            res += f"{att}: {self.__dict__[att]}\n"
        return res
        
    def to_json(self):
        res = {}
        attr_value = self.__dict__         
        for att in attr_value:
            res[att] = self.__dict__[att]

        return res