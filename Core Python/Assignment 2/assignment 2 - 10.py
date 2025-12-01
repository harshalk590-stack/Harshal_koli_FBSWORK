#Write a program to reverse three-digit number.

#Take Three digit number

num = int(input('Enter three-digit number'))

#operation

D1 = num // 100          
D2 = (num // 10) % 10    
D3 = num % 10

reverse = (D3 * 100) + (D2 * 10) + D1

print('Reverse three-digit number :', reverse)