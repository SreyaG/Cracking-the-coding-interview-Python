def selSort (arr):
    if arr != None:
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if arr[i] >= arr[j]:
                    arr[i], arr[j]=arr[j],arr[i]
        return arr
    else:
        return "Elements not found"
a= [10,8, 15.5,2,4, 6,7]
selSort(a)
print(a)        
