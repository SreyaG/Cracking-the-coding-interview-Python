def insertSort(arr):
    if arr != None:

        for i in range(len(arr)):
            temp=arr[i]
            ind=i
            while ind > 0 and arr[ind-1] > temp:
                arr[ind]=arr[ind-1]
                ind-=1
            arr[ind]=temp
    else:
        return "Elements not found"
a= [10,8, 15.5,2,4, 6,7]
insertSort(a)
print(a)
