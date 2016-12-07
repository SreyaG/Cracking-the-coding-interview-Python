class node (object):
    def __init__(self,val=None,nextNode=None):
        self.val=val
        self.nextNode=nextNode
    def getVal (self):
        return self.val
    def getnextNode (self):
        return self.nextNode
class linkedList (object):
    def __init__(self):
        self.head = None
    def insert(self,val):
        newnode = node(val,self.head)
        self.head=newnode
    def delete(self,index):
        current=self.head
        previous=False
        found=False
        while found == False and current != None:
            if current.getVal() == index:
                found=True
            else:
                previous=current
                current=current.getnextNode()
        if found == True:
            previous.nextNode = current.getnextNode()
        else:
            print "Nahi hai bapu"
    def size(self):
        count=0
        current=self.head
        while current:
            current=current.getnextNode()
            count+=1
        return count
    def search (self,index):
        found=False
        current=self.head
        while found == False and current.nextNode !=None:
            if current.getVal() == index :
                found = True
            else:
                current=current.getnextNode()
        if found == True:
            return current.getVal()
        else:
            return "Not here"

    def printList(self):
        current=self.head
        count=0
        while current:
            print "Element:", count, "is" , current.getVal()
            current=current.getnextNode()
            count+=1

temp=linkedList()
temp.insert(10)
temp.insert(20)
temp.insert(20)
temp.insert(5)
temp.insert(18)
temp.insert(40)
temp.printList()
print "Size: ", temp.size()
temp.delete(5)
print temp.search(20)
