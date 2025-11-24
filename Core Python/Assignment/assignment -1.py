#Write a program to calculate the percentage of student based on marks of any 5 subjects

#Take 5 Subjects marks
sub1 = int(input("Enter marks sub1:"))
sub2 = int(input("Enter marks sub2:"))
sub3 = int(input("Enter marks sub3:"))
sub4 = int(input("Enter marks sub4:"))
sub5 = int(input("Enter marks sub5:"))

#operation
Total = sub1+sub2+sub3+sub4+sub5
print ('Total makrs :',Total
       )
persentage = (Total / 500) * 100
print('Persentage :',persentage,"%")

