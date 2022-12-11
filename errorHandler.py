class ErrorHandler:

    errorList = []

    def addError(error):
        ErrorHandler.errorList.append(error)
    
    def getErrors():
        if(len(ErrorHandler.errorList) > 0):
            return ErrorHandler.errorList
        else:
            return "None"

    def getErrorType(process):
        if(process.type == "A"):
            return "A"
        else:
            return "D"

    def getInstructionNumber(process):
        print("TODO")
    
    def getFailureReason(process):
        # Figure out way to check if the process.id has been attempted to be allocated before or not
        return