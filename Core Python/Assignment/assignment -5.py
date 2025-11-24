#Write a program to enter P.T.R and calculate compound Interest.

#take input P T R

P = int(input('Enter Principal'))
R = int(input('Enter Rate of Interest'))
T = int(input('Enter Time'))

#Operation compound interest

CI = P * (1+R/100)**T - P

print('Compound Interest',CI)

