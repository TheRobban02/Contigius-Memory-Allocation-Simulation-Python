from list import List
from load import Load
from errorHandler import ErrorHandler
from error import Error
from save import Save

class Main:

    def simulation(strategy):

        fileList = Load.getFileNames()
    
        for file in fileList:
            
            Save.saveList.append(strategy)

            intermediateCounter = 0
            counter = 0
            Load.readFile(file)

            for x in Load.processList:
                
                counter += 1
                if(x.type != "A" and x.type != "D" and x.type != "O" and x.type != "C"):
                    List.maxMemory = int(x.type) -1
                    List.addFirstBlock()
                elif(x.type == "A"):
                    x.attemptedAllocation = True
                    if(strategy == "First fit"):
                        if(List.firstFit(x) == False):
                            ErrorHandler.addError(Error("A", counter, List.getLargestHole()))
                    elif(strategy == "Best fit"):
                        if(List.bestFit(x) == False):
                            ErrorHandler.addError(Error("A", counter, List.getLargestHole()))
                    else:
                        if(List.worstFit(x) == False):
                            ErrorHandler.addError(Error("A", counter, List.getLargestHole()))
                elif(x.type == "D"):
                    if(List.deAllocate(x) == False):
                        ErrorHandler.addError(Error("D", counter, ErrorHandler.getFailureReason(x)))
                elif(x.type == "O"):
                    intermediateCounter += 1
                    Save.prepIntermididate(file, intermediateCounter)
                    Save.saveList.append(strategy)
                else:
                    print("Add compact method")

            Save.prepareSaving(file)        


    simulation("First fit")
    Save.clearList()
    List.memoryList.clear()
    ErrorHandler.errorList.clear()
    Load.processList.clear()

    simulation("Best fit")
    Save.clearList()
    List.memoryList.clear()
    ErrorHandler.errorList.clear()
    Load.processList.clear()

    simulation("Worstfit")
