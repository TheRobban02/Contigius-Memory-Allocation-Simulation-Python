class Save:

    saveList = []
    
    # assign directory
    directory = 'files'

    def writeFile(fileName):
        
        outputName = Save.getOutputName(fileName)
        f = open("files/" + outputName, "a")
        for x in Save.saveList:
            f.write(f"{x}\n")


    def writeIntermediateFile(fileName, count):
        outputName = Save.getIntermediateName(fileName, count)
        f = open("files/" + outputName, "a")
        for x in Save.saveList:
            f.write(f"{x}\n")


    def getOutputName(fileName):
        str = fileName.split(".")
        return f"{str[0]}.out"
    

    def getIntermediateName(fileName, count):
        str = fileName.split(".")
        return f"{str[0]}.out{count}"

    
    def clearList():
        Save.saveList.clear()