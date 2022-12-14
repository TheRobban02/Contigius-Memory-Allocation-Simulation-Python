class Hole:

    def __init__(self, startAdress, endAdress):
        """
        Initialize the object with a start and end adress.
        @param startAdress - the start adress.
        @param endAdress - the end adress.
        """
        self.startAdress = startAdress
        self.endAdress = endAdress

    @property
    def startAdress(self):
        return self._startAdress

    @property
    def endAdress(self):
        return self._endAdress

    @property
    def size(self):
        return self.endAdress + 1 - self.startAdress

    @startAdress.setter
    def startAdress(self, x):
        self._startAdress = x

    @endAdress.setter
    def endAdress(self, x):
        self._endAdress = x
