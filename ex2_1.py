from Node import *

def removeDupe(listThis):
        current=listThis.head

        while current != None:
                runner=current
                while runner.next_node !=None:
                    if current.data == runner.next_node.data:
                        runner.next_node=runner.next_node.next_node
                    else:
                        runner=runner.next_node
                current=current.getNextnode()
        return listThis
def main():
    temp=unorderedList()
    temp.addItem(10)
    temp.addItem(20)
    temp.addItem(20)
    temp.addItem(5)
    temp.addItem(18)
    temp.addItem(40)
    (removeDupe(temp)).printList()

if __name__ == "__main__":
    main()
