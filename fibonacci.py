
def fibonacci (n):
    if n in fibo:
        return fibo[n]
    p = fibonacci (n-1) + fibonacci(n-2)
    fibo[n]=p
    print "Iter:", n ,"result", fibo[n]
    return p


n=5
fibo={0:1,1:1}
print fibonacci(n)
