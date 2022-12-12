from block import Block
from hole import Hole

class List:

    maxMemory = 0
    memoryList = []

    def firstFit(process):
        counter = 0
        processFits = False
        for x in List.memoryList:
            counter += 1
            if(type(x) == Hole and x.endAdress + 1 - x.startAdress >= process.size):
                newBlock = Block(x.startAdress, x.startAdress + process.size - 1, process) # Create a new Block
                processFits = True
                if(newBlock.endAdress == List.maxMemory):
                    List.memoryList.remove(x)  
                else:
                    x.startAdress = newBlock.endAdress + 1  # Change startAdress on the Hole (Remove if space left is empty)
        if(processFits):
            List.memoryList.insert(counter-1, newBlock)  # Insert new block
            return True
        else:
            return False

    def addFirstBlock():
        List.memoryList.append(Hole(0, List.maxMemory))


    def deAllocate(process): # Method that substitutes Blocks with Holes
        counter = -1
        processRemoved = False
        for x in List.memoryList:
            counter += 1
            if(type(x) == Block and x.process.id == process.id):
                newHole = Hole(x.startAdress, x.endAdress) # Create new Hole
                List.memoryList.insert(counter, newHole) # insert the hole before the block
                List.memoryList.remove(x) # remove the block 
                processRemoved = True
        List.mergeHoles()
        if(processRemoved):
            return True
        else:
            return False

    def mergeHoles(): # If there are two Holes next to each other we merge these togheter
        counter = len(List.memoryList)
        while(counter > 0):
            counter -= 1
            for x in List.memoryList:
                index = List.memoryList.index(x) # Gets the index of the current Hole/Block
                if(type(List.memoryList[index]) == Hole and len(List.memoryList) > 1 and x != List.memoryList[-1] and (type(List.memoryList[index + 1]) == Hole)):
                    x.endAdress = List.memoryList[index + 1].endAdress
                    List.memoryList.remove(List.memoryList[index + 1])
    

    def calcFragmentation():

        largestFreeMemory = 0
        totalFreeMemory = 0

        counter = 0
        for x in List.memoryList:
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
        processFits = False
        counter = 0
        for x in List.memoryList:
            if(type(x) == Hole and x.endAdress + 1 - x.startAdress >= process.size):
                if(difference >= x.endAdress - x.startAdress - process.size):
                    difference = x.endAdress + 1 - x.startAdress - process.size # Looks up the smallest Hole the process fits in
                    tempHole = List.memoryList[counter]
                    processFits = True
            counter += 1
        
        if(processFits): # Checks if the process have fitted in a hole or not
            newBlock = Block(tempHole.startAdress, tempHole.startAdress + process.size - 1, process)  # Creates the new block
            List.memoryList.insert(counter-1, newBlock)  # Insert new block   
            
            if(newBlock.endAdress == List.maxMemory): # Removes Hole if the memory is filled
                List.memoryList.remove(x)  
            else:
                x.startAdress = newBlock.endAdress + 1  # Change startAdress on the Hole (Remove if space left is empty)
            return True
        else:
            return False            

    def worstFit(process):
        processFits = False
        tempList = []
        for x in List.memoryList:
            if(type(x) == Hole and x.endAdress - x.startAdress >= process.size - 1):
                tempList.append(x)

        difference = 0
        for x in tempList:
            if(x.endAdress + 1 - x.startAdress > difference):
                difference = x.endAdress + 1 - x.startAdress

        for x in List.memoryList:
            if(x.endAdress + 1 - x.startAdress == difference and type(x) == Hole):
                newBlock = Block(x.startAdress, x.startAdress + process.size - 1, process)
                List.memoryList.insert(List.memoryList.index(x), newBlock)
                processFits = True
                if(newBlock.endAdress == List.maxMemory):
                    List.memoryList.remove(x) # Remove hole if memory is full.  
                else:
                    x.startAdress = newBlock.endAdress + 1  # Change startAdress on the Hole (Remove if space left is empty)
        
        return processFits

    def getLargestHole():
        size = 0
        for x in List.memoryList:
            if (type(x) == Hole and x.endAdress + 1 - x.startAdress > size):
                size = x.endAdress + 1 - x.startAdress
        return size

    def compress():
        for x in List.memoryList:
            if(type(x) == Hole):
                for y in List.memoryList:
                    if(List.processFits(y, x) and type(y) == Block):
                        if(y.startAdress > x.endAdress):
                            temp = y.endAdress
                            y.startAdress = x.startAdress
                            y.endAdress = x.startAdress + y.process.size - 1
                            x.startAdress = y.endAdress + 1
                            x.endAdress = temp
                            
                            index = List.memoryList.index(y)

                            if(y.endAdress + 1 != List.memoryList[index + 1].startAdress):
                                List.memoryList.insert(index, Hole(y.endAdress + 1, List.memoryList[index + 1].startAdress -1))
        List.mergeHoles()
        # Inserteas på fel ställe

    def processFits(block, hole):
        if(block.endAdress + 1 - block.startAdress <= hole.endAdress + 1 - hole.startAdress):
            return True
        else:
            return False
