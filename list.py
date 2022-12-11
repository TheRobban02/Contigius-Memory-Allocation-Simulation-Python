from block import Block
from hole import Hole

class List:

    maxMemory = 0
    blockList = []

    def firstFit(process):
        counter = 0
        for x in List.blockList:
            counter += 1
            if(type(x) == Hole and x.endAdress + 1 - x.startAdress >= process.size):
                newBlock = Block(x.startAdress, x.startAdress + process.size - 1, process) # Create a new Block
                if(newBlock.endAdress == List.maxMemory):
                    List.blockList.remove(x)  
                else:
                    x.startAdress = newBlock.endAdress + 1  # Change startAdress on the Hole (Remove if space left is empty)
                    
        List.blockList.insert(counter-1, newBlock)  # Insert new block

    def addFirstBlock():
        List.blockList.append(Hole(0, List.maxMemory))


    def deAllocate(process): # Method that substitutes Blocks with Holes
        counter = -1
        for x in List.blockList:
            counter += 1
            if(type(x) == Block and x.process.id == process.id):
                newHole = Hole(x.startAdress, x.endAdress) # Create new Hole
                List.blockList.insert(counter, newHole) # insert the hole before the block
                List.blockList.remove(x) # remove the block 
        List.mergeHoles()

    def mergeHoles(): # If there are two Holes next to each other we merge these togheter
        counter = len(List.blockList)
        while(counter > 0):
            counter -= 1
            for x in List.blockList:
                index = List.blockList.index(x) # Gets the index of the current Hole/Block
                if(type(List.blockList[index]) == Hole and len(List.blockList) > 1 and x != List.blockList[-1] and (type(List.blockList[index + 1]) == Hole)):
                    x.endAdress = List.blockList[index + 1].endAdress
                    List.blockList.remove(List.blockList[index + 1])
    

    def calcFragmentation():

        largestFreeMemory = 0
        totalFreeMemory = 0

        counter = 0
        for x in List.blockList:
            if(type(x) == Hole):
                blockSize = x.endAdress + 1 - x.startAdress
                counter += 1
                if(blockSize > largestFreeMemory):
                    largestFreeMemory = blockSize
                totalFreeMemory += blockSize

        if(counter == 0):
            return 0
        else:
            return round(1 - (largestFreeMemory / totalFreeMemory), 6)
    

    def bestFit(process):

        difference = List.maxMemory # The difference between the size of the process and the hole size

        counter = 0
        for x in List.blockList:
            if(type(x) == Hole and x.endAdress + 1 - x.startAdress >= process.size):
                if(difference >= x.endAdress - x.startAdress - process.size):
                    difference = x.endAdress + 1 - x.startAdress - process.size # Looks up the smallest Hole the process fits in
                    tempHole = List.blockList[counter]
            counter += 1
        newBlock = Block(tempHole.startAdress, tempHole.startAdress + process.size - 1, process)  # Creates the new block
        if(newBlock.endAdress == List.maxMemory):
            List.blockList.remove(x)  
        else:
            x.startAdress = newBlock.endAdress + 1  # Change startAdress on the Hole (Remove if space left is empty)
        
        List.blockList.insert(counter-1, newBlock)  # Insert new block       
    
    def worstFit(process):

        tempList = []
        for x in List.blockList:
            if(type(x) == Hole and x.endAdress - x.startAdress >= process.size - 1):
                tempList.append(x)
        
        difference = 0
        for x in tempList:
            if(x.endAdress + 1 - x.startAdress > difference):
                difference = x.endAdress + 1 - x.startAdress

        for x in List.blockList:
            if(x.endAdress + 1 - x.startAdress == difference and type(x) == Hole):
                newBlock = Block(x.startAdress, x.startAdress + process.size - 1, process)
                List.blockList.insert(List.blockList.index(x), newBlock)
       
                if(newBlock.endAdress == List.maxMemory):
                    List.blockList.remove(x) # Remove hole if memory is full.  
                else:
                    x.startAdress = newBlock.endAdress + 1  # Change startAdress on the Hole (Remove if space left is empty)
