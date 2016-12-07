
class Hanoi (object):

    def __init__(self,size=5):
        self.tower=[[],[],[]]
        self.size=size
        self.tower[0]=[x for x in range(size)]

    def playHanoi (self):
        self.printTower()
        self.moveDiscs(self.size,1,2,3)
        self.printTower()
    def moveDiscs(size,fr,buf,to):
        if size == 1:
            data=self.tower[fr-1].pop()
            self.tower[to -1].append(data)
            print "Disk", data, ": Tower", fr, "->", to

        else:
            moveDiscs(size-1,fr,to,buf)
            moveDiscs(1,fr,buf,to)
            moveDiscs(size-1,buf,fr,to)
    def printTower(self):
        for i in self.towers:
            print i

hanoi=Honaoi(5)
hanoi.playHanoi( )
