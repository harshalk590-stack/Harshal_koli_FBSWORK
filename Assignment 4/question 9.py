# WAP to print all numbers in a range divisible by a given number.

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
divisor = int(input("Enter the number to check divisibility: "))

print(f"Numbers divisible by {divisor} are:")

for num in range(start, end + 1):
    if num % divisor == 0:
        print(num)



