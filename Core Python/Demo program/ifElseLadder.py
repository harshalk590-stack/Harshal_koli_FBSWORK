#WAP to check number positive or negative using if else ladder.

num = int(input('Enter the number to check pos or neg '))

if(num == 0):
    print(f'{num} is a neutral number. ')
elif(num > 0):
    print(f'{num} is a positive number.')
else:
    print(f'{num} is a negative number. ')