from Node import *
class LinkedList (object):
    def __init__(self,head=None):
        self.head=head
    def insert(self, Data):
        new_node=Node(data)
        new_node.setNext=node
        self.head=new_node
    def size(self):
        current=self.head
        count=0
        while current:
            count+1
            current = current.get_next()
        return count

    def search(self,data):
        current=self.head
        found=False
        while current and found==False:
            if current.getData==data:
                found=True
            else:
                current=current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current=self.head
        previous=None
        found=False

        while found == False and current:
            if current.getData()==data:
                found=True
            else:
                previous=current
                current=current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.setNext(current.getNextData())
