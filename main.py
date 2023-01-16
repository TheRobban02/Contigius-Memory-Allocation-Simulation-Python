from list import List
from load import Load
from errorHandler import ErrorHandler
from error import Error
from save import Save


class Main:

    def simulation(strategy):
        """
        Run the simulation with the given strategy.
        @param strategy - the strategy to run the simulation with
        """
        fileList = Load.getFileNames()

        for file in fileList:

            Save.saveList.append(strategy)

            intermediateCounter = 0
            counter = 0
            Load.readFile(file)

            for x in Load.processList:

                
                if x.type not in ["A", "D", "O", "C"]:
                    List.maxMemory = int(x.type) - 1
                    List.addFirstHole()
                elif x.type == "A":
                    x.attemptedAllocation = True
                    if strategy == "First fit":
                        if List.firstFit(x) is False:
                            ErrorHandler.addError(
                                Error("A", counter, List.getLargestHole()))
                    elif strategy == "Best fit":
                        if List.bestFit(x) is False:
                            ErrorHandler.addError(
                                Error("A", counter, List.getLargestHole()))
                    else:
                        if List.worstFit(x) is False:
                            ErrorHandler.addError(
                                Error("A", counter, List.getLargestHole()))
                elif x.type == "D":
                    if List.deAllocate(x) is False:
                        ErrorHandler.addError(
                            Error("D", counter,
                                  ErrorHandler.getFailureReason(x)))
                elif x.type == "O":
                    intermediateCounter += 1
                    Save.prepIntermididate(file, intermediateCounter)
                    Save.saveList.append(strategy)
                else:
                    List.compress()
                
                counter += 1

            Save.prepareSaving(file)
            Save.clearList()
            List.memoryList.clear()
            ErrorHandler.errorList.clear()
            Load.processList.clear()

    Save.deleteFiles()
    simulation("First fit")
    simulation("Best fit")
    simulation("Worst fit")
