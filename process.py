from list import List

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
    
    @type.setter
    def type(self, x):
        self._type = x
    
    @id.setter
    def id(self, x):
        self._id = x

    @size.setter
    def size(self, x):
        self._size = x
