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
            if (type(x) == Hole and x.size >= process.size):
                newBlock = Block(x.startAdress,
                                 x.startAdress + process.size - 1, process)
                List.memoryList.append(newBlock)
                if (newBlock.endAdress == List.maxMemory):
                    List.memoryList.remove(x)
                else:
                    x.startAdress = newBlock.endAdress + 1
                List.memoryList.sort(key=lambda x: x.startAdress)
                List.mergeHoles()
                return True
        return False

    def addFirstBlock():
        """
        Add the first Hole to the memory list.
        """
        List.memoryList.append(Hole(0, List.maxMemory))

    def deAllocate(process):
        """
        Deallocate the memory of a process.
        @param process - the process to deallocate memory for
        @returns True if the process was deallocated, False otherwise
        """
        counter = -1
        processRemoved = False
        for x in List.memoryList:
            counter += 1
            if (type(x) == Block and x.process.id == process.id):
                newHole = Hole(x.startAdress, x.endAdress)  # Create new Hole
                List.memoryList.insert(
                    counter, newHole)  # insert the hole before the block
                List.memoryList.remove(x)  # remove the block
                processRemoved = True
        List.mergeHoles()
        if (processRemoved):
            return True
        else:
            return False

    def mergeHoles():
        """
        Merge any holes that are next to each other.
        """
        counter = len(List.memoryList)
        while (counter > 0):
            counter -= 1
            for x in List.memoryList:
                index = List.memoryList.index(
                    x)  # Gets the index of the current Hole/Block
                if (type(List.memoryList[index]) == Hole
                        and len(List.memoryList) > 1
                        and x != List.memoryList[-1]
                        and (type(List.memoryList[index + 1]) == Hole)):
                    x.endAdress = List.memoryList[index + 1].endAdress
                    List.memoryList.remove(List.memoryList[index + 1])

    def calcFragmentation():
        """
        Calculate the fragmentation of the memory.
        @return The fragmentation of the memory.
        """

        largestFreeMemory = 0
        totalFreeMemory = 0

        counter = 0
        for x in List.memoryList:
            if (type(x) == Hole):
                blockSize = x.endAdress + 1 - x.startAdress
                counter += 1
                if (blockSize > largestFreeMemory):
                    largestFreeMemory = blockSize
                totalFreeMemory += blockSize

        if (largestFreeMemory == totalFreeMemory):
            return "0.000000"
        else:
            return round(1 - (largestFreeMemory / totalFreeMemory), 6)

    def bestFit(process):
        """
        Method that finds the smallest hole in wich the process fits in.
        Creates a new block and replaces that Hole with a Block.
        returns True if the process fit, otherwise false.
        """
        processFits = False
        tempList = []
        for x in List.memoryList:
            if (type(x) == Hole and x.size >= process.size - 1):
                tempList.append(x)
                processFits = True

        tempList.sort(key=lambda x: x.size)

        if (len(tempList) > 0):
            newBlock = Block(tempList[0].startAdress,
                             tempList[0].startAdress + process.size - 1,
                             process)
            List.memoryList.insert(List.memoryList.index(tempList[0]),
                                   newBlock)

            if (newBlock.endAdress == List.maxMemory):
                List.memoryList.remove(tempList[0])
                # Remove hole if memory is full.
            else:
                tempList[0].startAdress = newBlock.endAdress + 1
            # Change startAdress on the Hole (Remove if space left is empty

        return processFits

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
            if (type(x) == Hole
                    and x.endAdress - x.startAdress >= process.size - 1):
                tempList.append(x)

        difference = 0
        for x in tempList:
            if (x.endAdress + 1 - x.startAdress > difference):
                difference = x.endAdress + 1 - x.startAdress

        for x in List.memoryList:
            if (x.endAdress + 1 - x.startAdress == difference
                    and type(x) == Hole):
                newBlock = Block(x.startAdress,
                                 x.startAdress + process.size - 1, process)
                List.memoryList.insert(List.memoryList.index(x), newBlock)
                processFits = True
                if (newBlock.endAdress == List.maxMemory):
                    List.memoryList.remove(x)  # Remove hole if memory is full.
                else:
                    x.startAdress = newBlock.endAdress + 1
                # Change startAdress on the Hole (Remove if space left is empty

        return processFits

    def getLargestHole():
        """
        Find the largest hole in the memory list.
        @return The size of the largest hole in the memory list.
        """
        size = 0
        for x in List.memoryList:
            if (type(x) == Hole and x.endAdress + 1 - x.startAdress > size):
                size = x.endAdress + 1 - x.startAdress
        return size

    def compress():
        """
        This function will compress the memory list.
        """
        blockList = []
        holeList = []

        for x in List.memoryList:
            if (type(x) == Block):
                blockList.append(x)
            else:
                holeList.append(x)

        List.memoryList.clear()
        blockList.sort(key=lambda x: x.startAdress)

        count = -1
        for x in blockList:
            count += 1
            if (count == 0):
                List.memoryList.append(x)
            else:
                if (blockList[count - 1].endAdress + 1 != x.startAdress):
                    x.startAdress = blockList[count - 1].endAdress + 1
                    List.memoryList.append(x)
                else:
                    List.memoryList.append(x)

        List.memoryList.append(
            Hole(List.memoryList[-1].endAdress + 1, List.maxMemory))
