class Process:

    def __init__(self, type, id = "*", size = "*"):
        self.type = type
        self.id = id
        self.size = size
    
    @property
    def type(self):
        return self._type
    
    @property
    def id(self):
        return self._id
    
    @property
    def size(self):
        return self._size
