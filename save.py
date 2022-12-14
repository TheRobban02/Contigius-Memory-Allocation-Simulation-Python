from list import List
from block import Block
from hole import Hole
from errorHandler import ErrorHandler
import os
import glob


class Save:

    saveList = []

    # assign directory
    directory = 'files'

    def writeFile(fileName):
        outputName = Save.getOutputName(fileName)
        f = open("files/" + outputName, "a")
        for x in Save.saveList:
            f.write(f"{x}\n")

    def deleteFiles():
        pattern = "files/*.out*"
        files = glob.glob(pattern)

        for file in files:
            os.remove(file)

    def writeIntermediateFile(fileName, count):
        outputName = Save.getIntermediateName(fileName, count)
        f = open("files/" + outputName, "a")
        for x in Save.saveList:
            f.write(f"{x}\n")
        Save.saveList.clear()

    def getOutputName(fileName):
        str = fileName.split(".")
        return f"{str[0]}.out"

    def getIntermediateName(fileName, count):
        str = fileName.split(".")
        return f"{str[0]}.out{count}"

    def clearList():
        Save.saveList.clear()

    def prepareSaving(file):

        Save.saveList.append("Allocated blocks")
        tempList = []
        for x in List.memoryList:
            if isinstance(x, Block):
                tempList.append(x)

        tempList.sort(
            key=lambda x: x.process.id)  # Sorts the allocated blocks by id
        for x in tempList:
            Save.saveList.append(
                f"{x.process.id};{x.startAdress};{x.endAdress}")

        Save.saveList.append("Free blocks")
        for x in List.memoryList:
            if isinstance(x, Hole):
                Save.saveList.append(f"{x.startAdress};{x.endAdress}")

        Save.saveList.append("Fragmentation")
        Save.saveList.append(f"{List.calcFragmentation()}")
        Save.saveList.append("Errors")

        if len(ErrorHandler.errorList) == 0:
            Save.saveList.append("None")
        else:
            for error in ErrorHandler.errorList:
                Save.saveList.append(
                    f"{error.type};{error.instructionNumber};{error.freeParameter}"
                )

        Save.saveList.append("")
        Save.writeFile(file)

    def prepIntermididate(file, count):
        Save.saveList.append("Allocated blocks")
        for x in List.memoryList:
            if isinstance(x, Block):
                Save.saveList.append(
                    f"{x.process.id};{x.startAdress};{x.endAdress}")

        Save.saveList.append("Free blocks")
        for x in List.memoryList:
            if isinstance(x, Hole):
                Save.saveList.append(f"{x.startAdress};{x.endAdress}")

        Save.saveList.append("Fragmentation")
        Save.saveList.append(f"{List.calcFragmentation()}")
        Save.saveList.append("Errors")

        if (len(ErrorHandler.errorList) == 0):
            Save.saveList.append("None")
        else:
            for error in ErrorHandler.errorList:
                Save.saveList.append(
                    f"{error.type};{error.instructionNumber};{error.freeParameter}"
                )

        Save.saveList.append("")
        Save.writeIntermediateFile(file, count)
