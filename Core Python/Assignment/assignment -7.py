#Program to Find the roots of a Quadratic Equation

#Take input a,b,c

a = int(input('Enter the value of a '))
b = int(input('Enter the value of b '))
c = int(input('Enter the value of c '))

#operation

D = (b*b - 4*a*c) ** 0.5

root1 = (-b + D) / (2*a)
root2 = (-b - D) / (2*a)

print('Root 1 :', root1)
print('Root 2 :', root2)



