def permute ( arr, start, end ):
    if start == end:
        print (''.join(arr))
    else:
        for x in xrange (start,end+1):
            arr[start],arr[x]=arr[x],arr[start]
            permute(arr,start+1,end)
            arr[start],arr[x]=arr[x],arr[start]


arr=list("kittens")
permute(arr,0,len(arr)-1)
