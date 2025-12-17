#Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n
#b. 1!+ 2! + 3! + 4!+..... + n!
#c. 1^1 + 2^2 + 3^3+ ...... n^n


##a. 1+ 2 + 3 + 4+..... + n
def sum_natural(n):
    return n * (n + 1) // 2

n = int(input("Enter value of n: "))
print("Sum of series =", sum_natural(n))


##b. 1!+ 2! + 3! + 4!+..... + n!
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def sum_factorial(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total

n = int(input("Enter value of n: "))
print("Sum of factorial series =", sum_factorial(n))

#c. 1^1 + 2^2 + 3^3+ ...... n^n
def sum_power(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

n = int(input("Enter value of n: "))
print("Sum of power series =", sum_power(n))

