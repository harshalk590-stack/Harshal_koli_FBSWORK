#Write a program to input angles of a triangle and check whether triangle is valid or not.

# Take Input angles of a triangle
a = float(input("Enter angle 1: "))
b = float(input("Enter angle 2: "))
c = float(input("Enter angle 3: "))

# Check validity
if(a <= 0 | b <= 0 | c <= 0):
    print("Triangle is NOT valid ")  #(angles must be greater than 0)
elif a + b + c < 180:
    print("Triangle is NOT valid ")  #(sum of angles is less than 180)
elif a + b + c > 180:
    print("Triangle is NOT valid ")  #(sum of angles is greater than 180)
else:
    print("Triangle is VALID")