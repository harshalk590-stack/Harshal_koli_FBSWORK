#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# Check the type of triangle
if(a == b == c):
    print("The triangle is Equilateral")
elif(a == b or a == c or b == c):
    print("The triangle is Isosceles")
else:
    print("The triangle is Scalene")

