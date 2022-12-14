class Process:

    def __init__(self, type, id="*", size="*", attemptedAllocation=False):
        """
        Initialize the object with the type, id, size, and attemptedAllocation.
        @param type - the type of object (A, D, O, C)
        @param id - the id of the object
        @param size - the size of the object
        @param attemptedAllocation-whether or not the object has been allocated
        """
        self.type = type
        self.id = id
        self.size = size
        self.attemptedAllocation = attemptedAllocation

    @property
    def type(self):
        return self._type

    @property
    def id(self):
        return self._id

    @property
    def size(self):
        return self._size

    @property
    def attemptedAllocation(self):
        return self._attemptedAllocation

    @attemptedAllocation.setter
    def attemptedAllocation(self, x):
        self._attemptedAllocation = x

    @type.setter
    def type(self, x):
        self._type = x

    @id.setter
    def id(self, x):
        self._id = x

    @size.setter
    def size(self, x):
        self._size = x
