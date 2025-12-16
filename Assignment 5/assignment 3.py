#Accept no. of passengers from user and per ticket cost. Then accept age of each
#passenger and then calculate total amount to ticket to travel for all of them based on
#following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

n = int(input("Enter number of passengers: "))
ticket_price = float(input("Enter ticket price per person: "))

total_amount = 0

for i in range(1, n + 1):
    age = int(input(f"Enter age of passenger {i}: "))

    if age < 12:
        discount = 0.30      # 30% discount
    elif age > 59:
        discount = 0.50      # 50% discount
    else:
        discount = 0.0       # No discount

    payable = ticket_price - (ticket_price * discount)
    total_amount += payable

    print(f"Passenger {i} needs to pay: ₹{payable:.2f}")

print("\nTotal amount to be paid for all passengers: ₹", format(total_amount, ".2f"))

