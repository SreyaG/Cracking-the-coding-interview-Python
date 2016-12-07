def powerset (arr,index):
    findset=[]
    if index == len(arr):
        findset.append([])
    else:
        findset=powerset (arr,index + 1)
        item=arr[index]
        moresubset=[]
        for i in findset:
            newsubset=[]
            newsubset.extend(i)
            newsubset.append(item)
            moresubset.extend("".join(newsubset)
        findset.extend(moresubset)
    return findset

string="abc"
print powerset(list(string),0)
