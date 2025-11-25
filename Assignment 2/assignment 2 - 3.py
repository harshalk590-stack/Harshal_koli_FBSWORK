#Convert distant given in feet and inches into meter and centimeter.

#1 foot = 30.48 cm
#1 inch = 2.54 cm
#1 meter = 100 cm

#take Feet and inches

Feet = float(input('Enter feet :'))
Inches = float(input('Enter Inches :'))

#operation 

T_CM = (Feet * 30.48) + (Inches * 2.54)

meter = T_CM / 100
centimeter = T_CM % 100

print('Distant in Meter',meter)
print('Distant in Centimeter',centimeter)

