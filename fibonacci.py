def fib(N):
    if N<=1:
        return N
    else:
        return fib(N-1)+fib(N-2)
def get_fib_ser(N):
    fib_ser=[]
    for i in range(N):
        term=fib(i)
        fib_ser.append(term)
    return fib_ser
N=int(input("enter number : "))
res=get_fib_ser(N)
print(res)