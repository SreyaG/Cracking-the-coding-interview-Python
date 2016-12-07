def fibonacci(n):
    fibo=[None]* (n+1)
    fibonaccihelper(fibo, n)
    return fibo

def fibonaccihelper(fibo,n):
    #print n
    if n == 0 or n ==1:
        fibo[n]=1
        return 1
    if n > 1:
        if fibo[n] != None:
            return fibo[n]
        else:
            fibo[n]=fibonaccihelper(fibo, n-1)+fibonaccihelper(fibo, n-2)
            return fibo[n]
print fibonacci(6)
