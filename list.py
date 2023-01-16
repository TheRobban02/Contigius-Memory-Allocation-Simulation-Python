from block import Block
from hole import Hole


class List:

    maxMemory = 0
    memoryList = []

    def firstFit(process):
        """
        Check the memory list for a hole that is big enough to fit the process.
        If there is one, create a new block and add it to the list.
        @param process - the process we are trying to fit into memory
        @returns True if the process was successfully added to memory, False otherwise.
        """
        for x in List.memoryList:
            if isinstance(x, Hole) and x.size >= process.size:
                new_block = Block(x.startAdress,
                    x.startAdress + process.size - 1, process)
                List.memoryList.append(new_block)
                if new_block.endAdress == List.maxMemory:
                    List.memoryList.remove(x)
                else:
                    x.startAdress = new_block.endAdress + 1
                List.memoryList.sort(key=lambda x: x.startAdress)
                List.mergeHoles()
                return True
        return False

    def addFirstHole():
        List.memoryList.append(Hole(0, List.maxMemory))

    def deAllocate(process):
        """
        Deallocate the memory of a process.
        @param process - the process to deallocate memory for
        @returns True if the process was deallocated, False otherwise
        """
        counter = -1
        for block in List.memoryList:
            counter += 1
            if isinstance(block, Block) and block.process.id == process.id:
                new_hole = Hole(block.startAdress, block.endAdress)
                List.memoryList.insert(counter, new_hole)
                List.memoryList.remove(block)
                List.mergeHoles()
                return True
        return False

    def mergeHoles():
        """
        Merge any holes that are next to each other.
        """
        for i, x in enumerate(List.memoryList):
            if (isinstance(x, Hole)
                    and len(List.memoryList) > 1
                    and x != List.memoryList[-1]
                    and (isinstance(List.memoryList[i + 1], Hole))):
                x.endAdress = List.memoryList[i + 1].endAdress
                List.memoryList.remove(List.memoryList[i + 1])

    def calcFragmentation():
        """
        Calculate the fragmentation of the memory.
        @return The fragmentation of the memory.
        """

        largestFreeMemory = 0
        totalFreeMemory = 0

        counter = 0
        for x in List.memoryList:
            if isinstance(x, Hole):
                blockSize = x.endAdress + 1 - x.startAdress
                counter += 1
                if (blockSize > largestFreeMemory):
                    largestFreeMemory = blockSize
                totalFreeMemory += blockSize

        if largestFreeMemory == totalFreeMemory:
            return "0.000000"
        else:
            return round(1 - (largestFreeMemory / totalFreeMemory), 6)

    def bestFit(process):
        """
        Method that finds the smallest hole in wich the process fits in.
        Creates a new block and replaces that Hole with a Block.
        returns True if the process fit, otherwise false.
        """
        temp_list = []
        for hole in List.memoryList:
            if isinstance(hole, Hole) and hole.size >= process.size - 1:
                temp_list.append(hole)

        temp_list.sort(key=lambda x: x.size)

        if len(temp_list) > 0:
            new_block = Block(temp_list[0].startAdress, temp_list[0].startAdress + process.size - 1, process)
            List.memoryList.insert(List.memoryList.index(temp_list[0]), new_block)
            if new_block.endAdress == List.maxMemory:
                List.memoryList.remove(temp_list[0])
            else:
                temp_list[0].startAdress = new_block.endAdress + 1
            return True
        return False

    def worstFit(process):
        """
        Check if the process fits in the memory. If it does, create
        a new block and insert it into the list.
        @param process - the process we are adding.
        @returns True if the process fits, False otherwise.
        """
        processFits = False
        tempList = []
        for x in List.memoryList:
            if (isinstance(x, Hole)
                    and x.endAdress - x.startAdress >= process.size - 1):
                tempList.append(x)

        difference = 0
        for x in tempList:
            if (x.endAdress + 1 - x.startAdress > difference):
                difference = x.endAdress + 1 - x.startAdress

        for x in List.memoryList:
            if (x.endAdress + 1 - x.startAdress == difference
                    and isinstance(x, Hole)):
                newBlock = Block(x.startAdress,
                                 x.startAdress + process.size - 1, process)
                List.memoryList.insert(List.memoryList.index(x), newBlock)
                processFits = True
                if (newBlock.endAdress == List.maxMemory):
                    List.memoryList.remove(x)  # Remove hole if memory is full.
                else:
                    x.startAdress = newBlock.endAdress + 1
                # Change startAdress on the Hole

        return processFits

    def getLargestHole():
        """
        Find the largest hole in the memory list.
        @return The size of the largest hole in the memory list.
        """
        size = 0
        for x in List.memoryList:
            if isinstance(x, Hole) and x.endAdress + 1 - x.startAdress > size:
                size = x.endAdress + 1 - x.startAdress
        return size

    def compress():
        """
        This function will compress the memory list.
        """
        blockList = []

        for x in List.memoryList:
            if (isinstance(x, Block)):
                blockList.append(x)

        List.memoryList.clear()
        blockList.sort(key=lambda x: x.startAdress)

    
        for i, block in enumerate(blockList):
          
            if (i == 0):
                block.startAdress = 0
                block.endAdress = block.process.size - 1
                List.memoryList.append(block)
            else:
                if (blockList[i - 1].endAdress + 1 != block.startAdress):
                    
                    block.startAdress = blockList[i - 1].endAdress + 1
                    block.endAdress = block.startAdress + block.process.size - 1
                    List.memoryList.append(block)
                else:
                    List.memoryList.append(block)
            
            

        List.memoryList.append(
            Hole(List.memoryList[-1].endAdress + 1, List.maxMemory))
