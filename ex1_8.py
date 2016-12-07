from itertools import cycle
def issubstring (astring):
    if (len(astring[0]) == len(astring[1])) and len(set(astring[0])-set(astring[1])) == 0:
        n = astring[1].index(astring[0][1])
        temp=[]
        flag=1
        i=1
        for i in range(len(astring[1])):
            p=(n+i-1) % len(astring[1])
            print p
            if astring[1][p]==astring[0][i]:
                flag=0
            else:
                print ("This is not a sub-string")
                break
        if flag==0:
            print ("This is a string")

    else:
        print ("This is not a sub-string")

def main():
    #astring =raw_input("Enter 2 string:")
    issubstring (['apple','banana'])
    issubstring (['meho','home'])
    issubstring (['bath','ball'])



if __name__ == '__main__':
    main()
