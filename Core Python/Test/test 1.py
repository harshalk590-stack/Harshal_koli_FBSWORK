#Write a program to find the area and perimeter of following figure (accept the length, breadth and radius from user).

#Take input length breadth and radius
length = float(input('Enter the length'))
breadth = float(input('Enter the breadth '))
radius = float(input('Enter the radius')) 

#operation on area

area_rect = length * breadth
area_circle = (3.14*radius*radius) / 2

perimeter_rect = 2 * (length * breadth)
perimeter_circle = 3.14 * radius + breadth

area = area_rect + area_circle
perimeter = perimeter_rect + area_circle

print(f"Area of the figure is {area}")
print(f'Area of the figure is {perimeter}')



