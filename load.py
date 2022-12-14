import os
from process import Process


class Load:

    processList = []

    # assign directory
    directory = 'files'

    def getFileNames():
        fileNames = []

        for filename in os.listdir(Load.directory):
            str = filename.split(".")
            if str[1] == "in":
                fileNames.append(filename)

        return fileNames

    def readFile(fileName):
        strList = []
        f = open("files/" + fileName, "r")

        for x in f:
            strList.append(x.replace("\n", ""))
        Load.createProcesses(strList)

    def createProcesses(fileList):
        """
        Create a list of processes from a list of strings.        
        @param fileList - the list of strings to create processes from.
        """
        for row in fileList:
            str = row.split(";")

            if len(str) == 1:
                Load.processList.append(Process(str[0]))
            elif len(str) == 2:
                Load.processList.append(Process(str[0], int(str[1])))
            else:
                Load.processList.append(
                    Process(str[0], int(str[1]), int(str[2])))
