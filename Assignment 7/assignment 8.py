n = 5

for i in range(1, n + 1):

    # Left increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    # Spaces in between
    for s in range(2 * (n - i)):
        print(" ", end=" ")

    # Right decreasing numbers
    for j in range(i, 0, -1):
         print(j, end=" ")
    print()
