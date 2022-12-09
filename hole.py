class Hole:

    def __init__(self, startAdress, endAdress):
        self.startAdress = startAdress
        self.endAdress = endAdress
    
    @property
    def startAdress(self):
        return self._startAdress

    @property
    def endAdress(self):
        return self._endAdress
    
    @startAdress.setter
    def startAdress(self, x):
        self._startAdress = x
    
    @endAdress.setter
    def endAdress(self, x):
        self._endAdress = x