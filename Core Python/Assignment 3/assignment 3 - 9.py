# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

s1 = float(input('Enter Subject 1 Marks : '))
s2 = float(input('Enter Subject 2 Marks : '))
s3 = float(input('Enter Subject 3 Marks : '))
s4 = float(input('Enter Subject 4 Marks : '))
s5 = float(input('Enter Subject 5 Marks : '))

total = s1+s2+s3+s4+s5
percentage = total / 5

if(percentage >= 85):
    print(f'Distinction with {percentage}')
elif(percentage >= 70):
    print(f'First class with {percentage}')
elif(percentage >= 55):
    print(f'Second class with {percentage}')
elif(percentage >= 35):
    print(f'Pass with {percentage}')
else:
    print(f"Fail with {percentage}")

