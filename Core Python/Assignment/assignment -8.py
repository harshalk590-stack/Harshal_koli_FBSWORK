#Write a program to convert days into years, weeks and days.

#Take input of days

D = int(input('Enter Days'))

#Calculate years

years = D//365
print(years)

#calculate Remaining Days

RD = D %365
print(RD)

#Calculate Weeks

Weeks = RD // 7
print(Weeks)

#Calculate left Days

LD = RD % 7
print(LD)
