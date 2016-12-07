from ex5 import *
def insertBits (N,M,i,j):
    return((clearBiti20(N,i)) | (M << j))


def main():
    N = int('10000000000', 2)
    M = int('10011', 2)
    i = 2
    j = 6
    print bin(insertBits(N,M,i,j))

if __name__ == "__main__":
    main ()
