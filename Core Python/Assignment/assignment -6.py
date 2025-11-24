#Write a program to input two angles from user and find third angle of the triangle.

#Take input Angle 1 and Angle 2

Angle1 = int(input('Enter Angle 1:'))
Angle2 = int(input('Enter Angle 2:'))

#Operation 
Angle3 = 180 - (Angle1 + Angle2)

#Output
print('Third angle of the Triangle is :',Angle3)
