from Node import *




def removeNode(k):
    if k.next_node != None:
        k.data=k.next_node.data
        k.next_node=k.next_node.next_node
    else:
        print ("Nothing to lose")
def main():
    temp=unorderedList()
    temp.addItem(10)
    temp.addItem(20)
    temp.addItem(20)
    temp.addItem(5)
    temp.addItem(22)
    temp.addItem(18)
    temp.addItem(40)
    temp.printList()
    k=temp.head
    for i in range(3):
        if k != None:
            k=k.next_node
        else :
            print ("Too short")

    removeNode(k)
    temp.printList()

if __name__ == "__main__":
    main ()
