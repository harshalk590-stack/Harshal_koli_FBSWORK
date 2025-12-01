#Write a program to calculate profit or loss.

#take input Cost Price (CP) Selling Price (SP)

cp = int(input('Enter Cost price :'))
sp = int(input('Enter selling price :'))

if(sp > cp):
    profit = sp - cp
    print ("Profit = ", profit)
elif(cp > sp):
    Loss = cp - sp
    print("Loss = ",Loss)
else:
   print("No Profit, No Loss")

