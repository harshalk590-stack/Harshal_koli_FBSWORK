#Write a program to check if entered number is a palindrome or
#not.

def is_palindrome(num):
    original = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    if original == rev:
        return True
    else:
        return False

# Taking input from user
n = int(input("Enter a number: "))

if is_palindrome(n):
    print("The number is Palindrome")
else:
    print("The number is NOT Palindrome")