class singleArrayStack (object):

    def __init__ (self, stacksize =100, number =3):
        self.stacksize = stacksize
        self.number = number
        self.array = [None] * self.stacksize * self.number
        self.pointer = [-1] * self.number

    def push (self,stacknum,value):
        if self.pointer[stacknum] + 1 >= self.stacksize:
            print ("Out of space")
        else:
            self.pointer[stacknum] = self.pointer[stacknum]+1
            self.array[self.stacktop(stacknum)]=value
            print (self.pointer)

    def pop (self,stacknum):
        if self.pointer[stacknum] < 0:
            return ("its Empty")
        else:
            data = self.array[self.stacktop(stacknum)]
            self.array[self.stacktop(stacknum)] = None
            self.pointer[stacknum] -= 1
            return data

    def peek (self,stacknum):
        if self.pointer[stacknum] < 0:
            print ("Its empty")
        else:
            return self.array[self.stacktop(stacknum)]


    def isEmpty (self,stacknum):
        return self.array[self.stacktop(stacknum)]== -1

    def stacktop (self, stacknum):
        return self.stacksize * stacknum + self.pointer[stacknum]




if __name__ == "__main__":
    array=singleArrayStack()
    array.push(2,13)
    array.push(2,20)
    print (array.pop(0))
    print (array.pop(2))
    array.push(0,23)
    array.push(0,22)
    print array.peek(2)
    print array.isEmpty(1)
    print array.isEmpty(0)
