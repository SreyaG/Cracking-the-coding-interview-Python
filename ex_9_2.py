def findmagic (arr, start, end):
    if (start > end | start < 0):
        return -1
    midsize = (start + end) // 2
    if arr[midsize] == midsize:
        return midsize
    elif arr[midsize] > midsize:
        return findmagic (arr,start,midsize-1)
    else:
        return findmagic(arr,midsize+1,end)
def findmagicdist (arr, start, end):
    if (start > end | start < 0):
        return -1
    midsize = (start + end) // 2
    midvalue = arr[midsize]
    if arr[midsize] == midsize:
        return midsize
    elif arr[midsize] > midsize:
        leftIndex = min (midsize-1, midvalue)
        return findmagic (arr,start,leftIndex)
    else:
        rightIndex = max (midsize+1, midvalue)
        return findmagic(arr,rightIndex,end)

arr=[-10,-5,1,1,2,3,4,7,9,9,13]
print findmagicdist(arr,0,10)
