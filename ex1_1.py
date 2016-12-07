astring =raw_input("Enter the string:")
flag=0
if len(astring) > 256:
    print("This is not unique")
else:
    for n in range(len(astring)):
        i=0
        while i<n :
            if astring[n]!=astring[i]:
                i=i+1
            else:
                print("This is not unique")
                flag=1
                break
        if flag==1:
            break
