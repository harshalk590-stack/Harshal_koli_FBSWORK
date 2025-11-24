#WAP to convert days into year, weeks, days
#take input
day = int(input("Enter Days"))

#calculate year
year = day // 365
print(year)
#Calculate 
remainingD = day % 365

print(remainingD)

weeks = remainingD//7
print(weeks)
dayleft = remainingD % 7
print(dayleft)

