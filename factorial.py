def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


num = int(input("enter Number : "))
result = factorial(num)
print(result)