#Write a program to enter P.T.R and calculate simple Interest.

#Take value P, T, R

P = int(input('Enter Principal:'))
R = int(input('Enter Rate of Interest:'))
T = int(input('Enter Time:'))


#operation
SI = P * R * T / 100
print ('Simple Interest:',SI)


