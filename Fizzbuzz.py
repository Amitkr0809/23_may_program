def fizz_buzz(number):
    if ((number % 3 == 0) and (number % 5 == 0)):
        str = "FizzBuzz"
    elif ((number % 3 == 0)):
        str = "Fizz"
    elif (number % 5 == 0):
        str = "Buzz"
    else:
        str = number

    return str


number = int(input("enter number : "))
result = fizz_buzz(number)
print(result)