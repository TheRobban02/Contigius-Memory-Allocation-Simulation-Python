from list import List
from process import Process
from block import Block
from hole import Hole

class main:

    List.maxMemory = 1000 - 1
    List.addFirstBlock()

    # p1 = Process("A", 0, 100)
    # p2 = Process("A", 1, 100)
    # p3 = Process("A", 2, 500)
    # p4 = Process("D", 1)
    # p5 = Process("A", 3, 200)
    # p6 = Process("D", 2)
    
    # List.firstFit(p1)
    # List.firstFit(p2)
    # List.firstFit(p3)
    # List.deAllocate(p4)
    # List.firstFit(p5)
    # List.deAllocate(p6)

    p1 = Process("A", 0, 200)
    p2 = Process("A", 1, 100)
    p4 = Process("D", 0)
    p6 = Process("D", 1)
    p7 = Process("A", 3, 50)

    List.bestFit(p1)
    List.bestFit(p2)
    List.deAllocate(p4)
    List.deAllocate(p6)
    List.bestFit(p7)
   
    print("Allocated blocks")
    for x in List.blockList:
        if(type(x) == Block):
            print(f"{x.process.id};{x.startAdress};{x.endAdress}")
    
    print("Free blocks")
    for x in List.blockList:
        if(type(x) == Hole):
            print(f"{x.startAdress};{x.endAdress}")

    print(f"Fragmentation\n{List.calcFragmentation()}")
    