class ZooElement():
    _id = 0

    def __init__(self):
        self.id = self.generate_id()

    def get_id(self):
        return type(self)._id

    def set_id(self,val):
        type(self)._id = val

    def generate_id(self):
        self.set_id(self.get_id() + 1)
        return self.get_id()

    def to_string(self):
        pass

    def to_json(self):
        pass
