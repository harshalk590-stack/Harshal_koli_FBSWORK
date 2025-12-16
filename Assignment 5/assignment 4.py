#
# WAP to print Armstrong number within a given range

 
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("\nArmstrong numbers in the given range are:")

for num in range(start, end + 1):
    temp = num
    total = 0
    digits = len(str(num))

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == num:
        print(num)


