class binarySearchTree (object):
    def __init__(self,data=0):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        self.key=None
    def getRightChild (self):
        return self.rightChild
    def getLeftChild (self):
        return self.leftChild
    def getData (self):
        return self.data
    def insert (self,data):
        if self:
            if self.data > data:
                if self.leftChild != None:
                    self.leftChild.insert(data)
                else:
                    self.leftChild=binarySearchTree(data)
            else:
                if self.rightChild != None:
                    self.rightChild.insert(data)
                else:
                    self.rightChild=binarySearchTree(data)
        else:
            self.data=data
    def search(self, data, parentNode = None):
        if data < self.data:
            if self.leftChild != None:
                return self.leftChild.search(data,self)
            else:
                return None,None
        elif data > self.data:
            if self.rightChild != None:
                return self.rightChild.search(data.self)
            else:
                return None, None
        else:
            return self, parent

    def returnTree (self):
        print self.data
        if self.leftChild:
            print self.leftChild.returnTree()
        if self.rightChild:
            print self.rightChild.returnTree()




root= binarySearchTree (8)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

root.returnTree()
