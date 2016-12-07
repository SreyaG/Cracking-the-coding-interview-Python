class bitManipulation (object):
    #def _init_(self):

    def getBit(data,index):
        return (data & (1 << index) == 0)
