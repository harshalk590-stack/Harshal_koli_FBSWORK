#Accept age of five people and also per person ticket amount and then calculate total
#amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

age1 = int(input("Enter age of person 1: "))
ticket1 = float(input("Enter ticket amount for person 1: "))
if age1 < 12:
    a1 = ticket1 - (ticket1 * 0.30)
elif age1 > 59:
    a1 = ticket1 - (ticket1 * 0.50)
else:
    a1 = ticket1

# Person 2
age2 = int(input("Enter age of person 2: "))
ticket2 = float(input("Enter ticket amount for person 2: "))
if age2 < 12:
    a2 = ticket2 - (ticket2 * 0.30)
elif age2 > 59:
    a2 = ticket2 - (ticket2 * 0.50)
else:
    a2 = ticket2

# Person 3
age3 = int(input("Enter age of person 3: "))
ticket3 = float(input("Enter ticket amount for person 3: "))
if age3 < 12:
    a3 = ticket3 - (ticket3 * 0.30)
elif age3 > 59:
    a3 = ticket3 - (ticket3 * 0.50)
else:
    a3 = ticket3

# Person 4
age4 = int(input("Enter age of person 4: "))
ticket4 = float(input("Enter ticket amount for person 4: "))
if age4 < 12:
    a4 = ticket4 - (ticket4 * 0.30)
elif age4 > 59:
    a4 = ticket4 - (ticket4 * 0.50)
else:
    a4 = ticket4

# Person 5
age5 = int(input("Enter age of person 5: "))
ticket5 = float(input("Enter ticket amount for person 5: "))
if age5 < 12:
    a5 = ticket5 - (ticket5 * 0.30)
elif age5 > 59:
    a5 = ticket5 - (ticket5 * 0.50)
else:
    a5 = ticket5

# Total amount
total = a1 + a2 + a3 + a4 + a5
print("Total ticket amount for all 5 people =", total)