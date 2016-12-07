def rot90 (mat):
    columns=len(mat[0])
    #mato=[[0 for x in range(columns)] for y in range(columns)]
    mat=zip(*mat)
    for n in range(columns):
        print mat[n]
        mat[n]=mat[n][::-1]

    print mat



def main():
    rot90([(1,2,3),(4,5,6),(7,8,9)])
if __name__ == '__main__':
    main()
