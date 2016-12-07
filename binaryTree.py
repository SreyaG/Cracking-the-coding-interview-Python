class BinaryTree (object):
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
    def preorder(self):
        return self.key
        if self.leftChild:
            return self.leftChild().preorder()
        if self.rightChild:
            return self.rightChild().preorder()

def preorder (tree):
    if tree:
        print tree.getRootVal()
        preorder (tree.getLeftChild())
        preorder (tree.getRightChild())
def postorder (tree):
    if tree != None:
        postorder (tree.getLeftChild())
        postorder (tree.getRightChild())
        print tree.getRootVal()
def inorder (tree):
    if tree:
        preorder (tree.getLeftChild())
        print tree.getRootVal()
        preorder (tree.getRightChild())

def printexp(tree):
  sVal = ""
  if tree:
      sVal = '(' + printexp(tree.getLeftChild())
      sVal = sVal + str(tree.getRootVal())
      sVal = sVal + printexp(tree.getRightChild())+')'
  return sVal



def main():
    r = BinaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild().getRootVal())
    r.getLeftChild().insertRight('d')
    print(r.getLeftChild().getRightChild().getRootVal())

    r.insertRight('c')
    print(r.getRightChild().getRootVal())

    r.getRightChild().insertLeft('e')
    r.getRightChild().insertRight('f')


    print "Left of right", r.getRightChild().getLeftChild().getRootVal()
    print "Right of right",r.getRightChild().getRightChild().getRootVal()


    inorder(r)
    print ("post order")
    preorder(r)

    print ("pre order")
    postorder (r)

    print ("printexp")
    print(printexp(r))

if __name__== "__main__":
    main()
