#Write a program to accept an integer amount from user and tell minimum
#number of notes needed for representing that amount.

#Take input 
amt = int(input('Enter the amount'))

#operation

two_T = amt // 2000
amt = amt % 2000

five_H = amt // 500
amt = amt % 500

two_H = amt // 200
amt = amt % 200

one_H = amt // 100
amt = amt % 100

fifty = amt // 50
amt = amt % 50

tw = amt // 20
amt = amt % 20

ten = amt // 10
amt = amt % 10

notes = two_T + five_H + two_H + one_H + fifty + tw + ten
print('Notes needed for representing amount :', notes)

