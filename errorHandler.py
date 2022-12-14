from load import Load


class ErrorHandler:

    errorList = []

    def addError(error):
        ErrorHandler.errorList.append(error)

    def getErrors():
        if len(ErrorHandler.errorList) > 0:
            return ErrorHandler.errorList
        else:
            return "None"

    def getFailureReason(process):
        for x in Load.processList:
            if x.id == process.id:
                if x.attemptedAllocation:
                    return 1
                else:
                    return 0
