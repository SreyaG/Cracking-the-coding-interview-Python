def erastotheneses (n):
    multiples = []
    multiples.append (2)
    for i in range(3,n,2):
        flag =1
        for k in multiples:
            if i%k == 0:
                flag=0
                break;
        if flag == 1:
            multiples.append(i)
    return multiples




print erastotheneses (100)
