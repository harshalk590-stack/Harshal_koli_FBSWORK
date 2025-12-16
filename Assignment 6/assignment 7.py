rows = 5

for i in range(1, rows + 1):
    # print spaces
    print("  " * (rows - i), end="")

    # print alphabets
    for j in range(2 * i - 1):
        print(chr(65 + j), end=" ")
    
    print()