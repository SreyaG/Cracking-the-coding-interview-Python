class treeNode (object):
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.leftChild = left
        self.rightChild = right
        self.payload = val
        self.parent=parent

    def hasRightChild(self):
        return self.rightChild
    def hasLeftChild(self):
        return self.leftChild
    def isleftChild(self):
        return self.parent and self.parent.leftChild == self
    def isrightChild (self):
        return self.parent and self.parent,rightChild == self
    def isRoot(self):
        return not self.parent
    def isLeaf(self):
        return not (self.right or self.left)
    def hasChildren(self):
        return self.right or self.left
    def hasBothChildren (self):
        return self.right and self.left
    def replaceNode (self,key,value,lc,rc):
        self.key=key
        self.payoad=value
        self.leftChild=lc
        self.rightChild=rc
        if self.hasLeftChild():
            self.leftChild.parent()=self
        if self.hasRightChild():
            self.rightChild.parent()=self
