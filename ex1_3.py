def checkPermutation (astring):
    if len(astring[0])==len(astring[1]):
        a= set(astring[0]) <= set(astring[1])
        if a is True:
            print ("This is a permutation")
        else:
            print ("This is not a permutation")
    else:
        print ("This is not a permutation")

def main():
    #astring =raw_input("Enter 2 string:")
    checkPermutation (['apple','banana'])
    checkPermutation (['ohme','home'])
    checkPermutation (['bath','ball'])



if __name__ == '__main__':
    main()
