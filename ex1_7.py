def make0 (matinp):
    row = len(matinp)
    print row
    for n in range(row):
        if( matinp[n].count(0) > 0):
            matinp[n]=[0] * len(matinp[n])
    return matinp


def main():
    print make0([[1,2,3],[4,0,6],[7,0,9],[10,11,12]])

if __name__ == '__main__':
    main()
