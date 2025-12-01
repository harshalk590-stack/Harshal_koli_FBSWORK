#Write a program to check if given 3 digit number is a palindrome or not


num = int(input("Enter a 3-digit number: "))

# Extract digits
first = num // 100
middle = (num // 10) % 10
last = num % 10

# Reverse number
reverse = last*100 + middle*10 + first

# Check palindrome
if num == reverse:
    print(num, "is a Palindrome number")
else:
    print(num, "is NOT a Palindrome number")

