class binaryHeap(object):
    def __init__(self):
        self.heapList=[0]
        self.currentSize=0
    def percolateup (self, i):
        while i//2 != 0
        if self.heapList[val] < self.heapList[val//2]:
            self.heapList[val], self.heapList[val//2] = self.heapList[val//2], self.heapList[val]
        i=i//2
    def insert (self,val):
        self.heapList.append(val)
        self.currentSize + =1
        percolateup (self.currentSize)
    def percolatedown (self, i):
        while (i*2) < self.currentSize:
            mc = self.minChild(i)
            if self.heapList[mc] < self.heapList[i]:
                self.heapList[i],self.heapList[mc]=self.heapList[mc],self.heapList[i]
            i=mc

    def minChild(self,i):
        if i*2 + 1 > self.currentSize:
            return i*2
        elif self.heapList[i*2] < self.heapList[i*2 + 1]:
            return i*2
        else:
            return i*2+1

    def deletemin(self):
        retval=self.heapList [1]
        self.heapList [1]=self.heapList [self.currentSize]
        self.currentSize - = 1
        self.heapList.pop()
        percolatedown (1)
        return retval
   def buildHeap (self, alist):
        
