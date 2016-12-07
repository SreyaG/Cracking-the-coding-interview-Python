def findsubSet(arr,index):
    allsubset=[]
    if len(arr) == index :
        allsubset.append([])
    else:
        allsubset = findsubSet(arr, index+1)
        item=arr[index]
        moresubset=[]
        for subset in allsubset:
            newsubset=[]
            newsubset.extend(subset)
            newsubset.append(item)
            print "".join(newsubset)
            moresubset.append("".join(newsubset))
        allsubset.extend(moresubset)
    return allsubset


arr=list("abc")
print (findsubSet(arr, 0))
