from list import List
from process import Process
from block import Block
from hole import Hole
from load import Load

class main:

    fileList = Load.getFileNames()
    
    for file in fileList:
        
        Load.readFile(file)
        for x in Load.processList:
            if(x.type != "A" and x.type != "D" and x.type != "O" and x.type != "C"):
                List.maxMemory = int(x.type) -1
                List.addFirstBlock()
            elif(x.type == "A"):
                List.bestFit(x)
            elif(x.type == "D"):
                List.deAllocate(x)
            elif(x.type == "O"):
                print("Add output immidiete") 
            else:
                print("Add compact method")


        # Do best fit/worst fit/first fit
        # Create output files
        # Create immidiete files


    print("Allocated blocks")
    for x in List.blockList:
        if(type(x) == Block):
            print(f"{x.process.id};{x.startAdress};{x.endAdress}")
    
    print("Free blocks")
    for x in List.blockList:
        if(type(x) == Hole):
            print(f"{x.startAdress};{x.endAdress}")

    print(f"Fragmentation\n{List.calcFragmentation()}")
    