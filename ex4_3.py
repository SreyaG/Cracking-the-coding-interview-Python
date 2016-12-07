import binaryTree
def minHeight ( arr, start,end):
    if start > end:
        return None
    else:
        i=(start+end)//2
        n=binaryTree.BinaryTree(arr[i])
        n.leftChild=minHeight(arr,start,i-1)
        n.rightChild=minHeight(arr,i+1,end)
        return n
def preorder (tree):
    if tree:
        print tree.getRootVal()
        preorder (tree.getLeftChild())
        preorder (tree.getRightChild())
arr= [1,2,3,4,5,6,7,8]
n=minHeight(arr,0,7)
preorder(n)
