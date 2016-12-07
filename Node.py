class Node (object):
    def __init__(self,data=None,next_node=None):
        self.data=data
        self.next_node=next_node
    def getData(self):
        return self.data
    def getNextnode (self):
        return self.next_node

class unorderedList (object):

    def __init__(self):
        self.head=None

    def addItem(self,data):
        new_node=Node(data)
        new_node.next_node=self.head
        self.head=new_node
    def sizeList(self):
        current=self.head
        count=0
        while current!=None:
            count=count+1
            current=current.getNextnode()
        return count
    def search(self, index):
        current=self.head
        count=0
        found=False
        while current!=None and found==False :
            if current.getData()==index:
                found=True
            else:
                current=current.getNextnode()
                count=count+1

        return count
    def removeData(self,index):
        current=self.head
        previous=None
        found=False
        while current != False and found==False:
            if current.getData()==index:
                current=current.getNextnode()
                found=True
            else:
                previous=current
                current=current.getNextnode()
        if previous ==None:
            self.head=current.getNextnode()
        else:
            previous.next_node=current.getNextnode()

    def printList(self):
        current=self.head
        while current!=None:
            print (current.getData())
            current=current.getNextnode()
