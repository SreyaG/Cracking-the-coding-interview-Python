def quickSort (arr,start,end):
    if start < end:
        pindex=partition(arr,start,end)
        arr=quickSort(arr,start,pindex-1)
        arr=quickSort(arr,pindex+1,end)
    return arr
def partition(arr,start,end):
    pindex=start
    val=arr[end]
    for i in range(start,end):
        if arr[i] < val:
            arr[i],arr[pindex]=arr[pindex],arr[i]
            pindex+=1
    arr[pindex],arr[end]=arr[end],arr[pindex]
    return pindex


a= [10,8, 15.5,2,4, 6,7]
print quickSort(a,0,len(a)-1)
