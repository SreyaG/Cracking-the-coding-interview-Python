from Node import *


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
        print "The %d element from the end is : %s " % (4,findn_k(temp,4))

def findn_k(listThis,k):
    if k <= 0:
        return "Invalid request"
    pointer1=listThis.head
    for i in range(k-1):
        if pointer1.next_node !=None:
            pointer1=pointer1.next_node
            print (i)
        else:
            return "k exceeds the length of linkedlist"
    pointer2=listThis.head
    while pointer1.next_node != None:
        pointer1=pointer1.next_node
        pointer2=pointer2.next_node
    return pointer2.data


if __name__ == "__main__":
    main()
