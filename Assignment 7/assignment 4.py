n = 5

for i in range(1, n + 1):
    # spaces
    print("  " * (n - i), end="")

    # increasing numbers
    for j in range(i, 2 * i):
        print(j, end=" ")

    # decreasing numbers
    for j in range(2 * i - 2, i - 1, -1):
        print(j, end=" ")

    print()