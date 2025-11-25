#WAP to calculate selling price of book based on cost price and discount.

#Take intput 

costprice = float(input('Enter cost price of book: '))
discount = float(input("Enter Discount percentage: "))

#Operation 
D_price = (discount / 100)* costprice   #Discount amount


S_price = costprice - D_price       #Selling price

print("Selling Price of the book =", S_price)



