#Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.

n = int(input("Enter number of students: "))

total_percentage = 0

for i in range(1, n + 1):
    print(f"\nEnter marks for student {i}")

    m1 = float(input("Subject 1: "))
    m2 = float(input("Subject 2: "))
    m3 = float(input("Subject 3: "))
    m4 = float(input("Subject 4: "))
    m5 = float(input("Subject 5: "))

    total = m1 + m2 + m3 + m4 + m5
    percentage = (total / 500) * 100

    print(f"Percentage of student {i} = {percentage:.2f}%")

    total_percentage += percentage

average_percentage = total_percentage / n
print(f"\nAverage percentage of all students = {average_percentage:.2f}%")



