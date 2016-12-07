def mergeSort(arr):
    if arr != None:
        if len(arr) > 2:
            L=mergeSort(arr[:(len(arr)/2)])
            R=mergeSort(arr[(len(arr)/2):])
            print L
            print R
            arr=merge(L,R,arr)
        return arr
    else:
        return "Elements not found"

def merge(L,R,arr):
    lind=0
    rind=0
    ind=0
    while lind < len(L) and rind < len(R):
        if L[lind] < R[rind]:
            arr[ind]= L[lind]
            lind+=1
        else:
            arr[ind]= R[rind]
            rind+=1
        ind+=1
    if lind < len(L):
        arr[ind:]=L[lind:]
    else:
        arr[ind:]=R[rind:]
    return arr

a= [10,8, 15.5,2,4, 6,7]
mergeSort(a)
print(a)
