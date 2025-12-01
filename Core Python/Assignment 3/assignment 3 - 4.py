#Write a program to input all sides of a triangle and check whether triangle is valid or not.

#Take input all sides of triangle
a = float(input('Enter side A'))
b = float(input('Enter side B'))
c = float(input('Enter side C'))

if a + b <= c:
    print("Triangle is NOT valid ") #(a + b is not greater than c)
elif a + c <= b:
    print("Triangle is NOT valid ")  #(a + c is not greater than b)
elif b + c <= a:
    print("Triangle is NOT valid ") #(b + c is not greater than a)
else:
    print("Triangle is VALID")


