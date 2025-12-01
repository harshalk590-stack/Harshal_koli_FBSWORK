#Calculate the cost of painting the following building's walls (both interior and exterior). you need to accept area (one wall) and cost of both interior and exterior wall.
#note(1 Below diagram is of two joint rooms. 2 itis upper view of building.)

#Take input one wall interior exterior

interior_area = float(input("Enter area of one interior wall (sq ft): "))
exterior_area = float(input("Enter area of one exterior wall (sq ft): "))

interior_cost = float(input("Enter cost per sq ft for interior painting: "))
exterior_cost = float(input("Enter cost per sq ft for exterior painting: "))

num_interior = int(input("Enter number of interior walls: "))
num_exterior = int(input("Enter number of exterior walls: "))

# Calculations
total_interior = interior_area * interior_cost * num_interior
total_exterior = exterior_area * exterior_cost * num_exterior

total = total_exterior + total_interior


print("Total interior wall painting cost: ", total_interior)
print("Total exterior wall painting cost: ", total_exterior)
print("Total cost of painting: ", total)

