#Write a program to solve the following series :
#a. 1! + 2! + 3! + 4! + .....n!
#b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
#d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
#e. x - x2/3 + x3/5 - x4/7 + .... to n terms


#1. 1! + 2! + 3! + 4! + .....n!
n = int(input("Enter n: "))
fact = 1
sum = 0

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + fact

print("Sum of series =", sum)

#2. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

N = int(input("Enter N: "))
sum = 0

for i in range(1, N + 1):
    sum = sum + (N ** i)

print("Sum of series =", sum)

#3. Find the sum of a geometric series from 1 to n where the common ratio is 2.

n = int(input("Enter number of terms: "))
term = 1
sum = 0

for i in range(n):
    sum = sum + term
    term = term * 2

print("Sum of geometric series =", sum)

#4. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a = int(input("Enter a: "))
sum = 0

for i in range(1, 11):
    sum = sum + (a ** i) / i

print("Sum of series =", sum)

#5. x - x2/3 + x3/5 - x4/7 + .... to n terms

x = int(input("Enter x: "))
n = int(input("Enter number of terms: "))
sum = 0
sign = 1
den = 1

for i in range(1, n + 1):
    sum = sum + sign * (x ** i) / den
    sign = -sign
    den = den + 2

print("Sum of series =", sum)
