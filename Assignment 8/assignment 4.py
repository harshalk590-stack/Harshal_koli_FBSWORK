#Sum of all odd numbers between 1 to n

def sum_of_odd(n):
    total = 0
    for i in range(1, n + 1, 2):
        total += i
    return total

# Taking input from user
n = int(input("Enter value of n: "))

result = sum_of_odd(n)
print("Sum of all odd numbers from 1 to", n, "=", result)