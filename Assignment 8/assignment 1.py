#Write a program to calculate area of rectangle
def area_of_rectangle(length, width):
    area = length * width
    return area

# Taking input from user
l = float(input("Enter length: "))
w = float(input("Enter width: "))

result = area_of_rectangle(l, w)
print("Area of Rectangle =", result)
