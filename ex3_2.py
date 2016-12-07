class stackwithMin (object) :

    def __init__ (self):
        self.array=[0]
        self.minval=[0]

    def push (self, val):
        self.array.append(val)
        if len(self.array) >= 1:
            minVal2=self.findMin(val)
            self.minval.append(minVal2)
        else:
            self.array.append(val)
            self.minval.append(val)

    def popit (self):
        self.minval.pop()
        return(self.array.pop())

    def findMin (self,val):
        if val < self.minval[-1]:
            return self.minval[-1]
        else:
            return val

    def getMin(self):
        return self.minval[-1]


def main():
    stack = stackwithMin()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print stack
    node = stack.popit ()
    print node
    stack.push(0)
    stack.push(4)
    print stack

    node = stack.popit()
    #print stack.findMin()
    print stack

if __name__ == '__main__':
    main()
