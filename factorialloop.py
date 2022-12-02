#Iterative using for loop
x = 5
fact = 1

if x != 0:
    for i in range(1,x+1):
        fact = fact * i

print("Factorial of ", x, "using iterative approach is ", fact)

#recursion

def factorial(number):
    if (number == 0):
        return 1
    else:
        return number * factorial(number-1)

print("Factorial of ", x, "using Recursion is ",  factorial(x))