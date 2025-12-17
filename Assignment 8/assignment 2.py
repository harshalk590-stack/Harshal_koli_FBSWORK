#Write a program to calculate area of circle
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

r = float(input("Enter radius of the circle: "))

result = area_of_circle(r)
print("Area of Circle =", result)