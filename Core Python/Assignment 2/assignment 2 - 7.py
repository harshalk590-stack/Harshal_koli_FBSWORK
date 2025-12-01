#Find the sum of three-digit number.

#Take Three digit number

num = int(input('Enter three-digit number'))

#operation

D1 = num // 100          
D2 = (num // 10) % 10    
D3 = num % 10

Sum = D1 + D2 + D3
print("Sum of Three-Digit number :", Sum)


