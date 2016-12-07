def reverseString (astring):
    n=0
    while astring[n] != None:
        a=astring[::-1]
        n=n+1
    return a

astring =raw_input("Enter the string:")
print "The reverse of %s is %s" % (astring,reverseString(astring))
