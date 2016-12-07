def permute(a,start,end):
    if start==end:
        print "".join(a)
    else:
        for x in range(start,end+1):
            a[x],a[start]=a[start],a[x]
            permute(a,start+1,end)
            a[x],a[start]=a[start],a[x]


string="cat"
permute (list(string),0, len(string)-1)
