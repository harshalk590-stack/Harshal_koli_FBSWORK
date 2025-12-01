#Write a program to accept distance in Km and convert it into meters and centimeters both
#Take input principal rate and time 

p = int(input('Enter the principal interest '))
r = int(input('Enter the Rate of interest'))
t = int(input('Enter the time of interest'))

#operation on 

SI = p * r * t / 100

print(f'{SI} is the simple interest')


