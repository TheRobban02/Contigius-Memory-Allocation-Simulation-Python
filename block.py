class Block:

    def __init__(self, startAdress, endAdress, process):
        """
        Initialize the objecct with a start and end adress and the process number.
        @param startAdress - the start adress of the process
        @param endAdress - the end adress of the process
        @param process - the process number
        """
        self.startAdress = startAdress
        self.endAdress = endAdress
        self.process = process

    @property
    def startAdress(self):
        return self._startAdress

    @property
    def endAdress(self):
        return self._endAdress

    @property
    def process(self):
        return self._process

    @startAdress.setter
    def startAdress(self, x):
        self._startAdress = x

    @endAdress.setter
    def endAdress(self, x):
        self._endAdress = x

    @process.setter
    def process(self, x):
        self._process = x
