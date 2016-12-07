def countways (cnt, n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif cnt [n] != -1:
        return cnt[n]
    else:
        cnt[n]=countways(cnt,n-1)+countways(cnt,n-2)+countways(cnt,n-3)
        return cnt[n]

n=3
cnt=[-1]*(n+1)
'''cnt[0]=0
cnt[1]=1
cnt[2]=1
cnt[3]=2'''
print (countways(cnt,n))
