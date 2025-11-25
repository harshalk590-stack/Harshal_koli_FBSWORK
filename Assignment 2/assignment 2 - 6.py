#WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.

#Take input of Basic salary

B_Salary = float(input('Enter Basic salary'))

#Add Da to Basic salary
DA = B_Salary / 10
B_Salary = DA + B_Salary

#Add TA to Basic salary
TA = B_Salary * 0.12 
B_Salary = TA + B_Salary

#Add HRA to basic salary
HRA = B_Salary * 0.15
B_Salary = HRA + B_Salary

print('Total salary of Employee :', B_Salary)


