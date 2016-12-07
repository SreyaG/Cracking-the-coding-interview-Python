from bitManipulation import *
def getBit(data,index):
    return (data & (1 << index))

def setBit(data,index):
    return (data | (1 << index))
def clearBit(data,index):
    return (data & ~(1 << index))

def clearBitmaxtoi(data,index):
    return (data & ((1 << index)-1))

def clearBiti20(data,index):
    return (data & ~((1 << index+1)-1))
def updateBit(data,v,index):
    temp=clearBit(data,index)
    return(temp | (v << index))

def main ():
    #a=bitManipulation()
    print (bin(576))
    print (getBit( 576, 3))
    print (bin(setBit( 576, 3)))
    print (bin(clearBit( 15, 2)))
    print (bin(clearBitmaxtoi( 15, 2)))
    print (bin(clearBiti20( 15, 2)))
    print (bin(updateBit( 15, 0, 2)))




if __name__=="__main__":
    main()
