class Error:

    def __init__(self, type, instructionNumber, freeParameter):
        """
        Initialize the class.
        @param type - the type of instruction ("A" or "D")
        """
        self.type = type
        self.instructionNumber = instructionNumber
        self.freeParameter = freeParameter

    @property
    def type(self):
        return self._type

    @property
    def instructionNumber(self):
        return self._instructionNumber

    @property
    def freeParameter(self):
        return self._freeParameter

    @type.setter
    def type(self, x):
        self._type = x

    @instructionNumber.setter
    def instructionNumber(self, x):
        self._instructionNumber = x

    @freeParameter.setter
    def freeParameter(self, x):
        self._freeParameter = x
