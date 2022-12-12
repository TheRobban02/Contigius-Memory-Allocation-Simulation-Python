from list import List
from process import Process
from block import Block
from hole import Hole
from load import Load
from errorHandler import ErrorHandler
from error import Error
from save import Save

class Main:

    def simulation(strategy):

        fileList = Load.getFileNames()
    
        for file in fileList:
            
            Save.saveList.append(strategy)

            counter = 0
            Load.readFile(file)

            for x in Load.processList:
                intermediateCounter = 0
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
                    Save.writeIntermediateFile(file, intermediateCounter)
                else:
                    print("Add compact method")
            
            Save.saveList.append("Allocated blocks")
            for x in List.memoryList:
                if(type(x) == Block):
                    Save.saveList.append(f"{x.process.id};{x.startAdress};{x.endAdress}")

            Save.saveList.append("Free blocks")
            for x in List.memoryList:
                if(type(x) == Hole):
                   Save.saveList.append(f"{x.startAdress};{x.endAdress}")

            Save.saveList.append("Fragmentation")
            Save.saveList.append(f"{List.calcFragmentation()}")
            Save.saveList.append("Errors")
            
            if(len(ErrorHandler.errorList) == 0):
                Save.saveList.append("None")
            else:
                for error in ErrorHandler.errorList:
                    Save.saveList.append(f"{error.type};{error.instructionNumber};{error.freeParameter}")

            Save.writeFile(file)

    simulation("First fit")
    Save.clearList()
    List.memoryList.clear()
    simulation("Best fit")
    Save.clearList()
    List.memoryList.clear()
    simulation("Worstfit")







    # print("Allocated blocks")
    # for x in List.memoryList:
    #     if(type(x) == Block):
    #         print(f"{x.process.id};{x.startAdress};{x.endAdress}")
    
    # print("Free blocks")
    # for x in List.memoryList:
    #     if(type(x) == Hole):
    #         print(f"{x.startAdress};{x.endAdress}")

    # print(f"Fragmentation\n{List.calcFragmentation()}")
    
    # print(f"Errors")

    # for error in ErrorHandler.errorList:
    #     print(f"{error.type};{error.instructionNumber};{error.freeParameter}")

    