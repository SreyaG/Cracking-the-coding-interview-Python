def compress (astring):
    unq=[]
    for n in range(len(astring)):
        if astring[n] in unq:
            flag=1
        else:
            unq.append(astring[n])
    print unq
    bstring=[]
    for n in range(len(unq)):
        if astring.count(unq[n]) > 1:
            bstring=bstring + [unq[n]]+[astring.count(unq[n])]
        else:
            bstring=bstring + [unq[n]]
    print ''.join(str(e) for e in bstring)


def main():
    compress ('sreya')
    compress ('abracadabra')

if __name__=='__main__':
    main()
