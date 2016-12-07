
def findBits(M,N):
    temp = M ^ N
    cnt=0
    while temp != 0:
        if (temp & 1) == 1:
            cnt=cnt+1
        print bin(temp)
        temp = temp >> 1
    return cnt
def main():
    N = int('10000', 2)
    M = int('10011', 2)
    print ("Number of integers changed")
    print findBits(N,M)

if __name__ == "__main__":
    main ()
