#8. Write a program find reverse of a number

def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev

# Taking input from user
n = int(input("Enter a number: "))

result = reverse_number(n)
print("Reverse of the number =", result)