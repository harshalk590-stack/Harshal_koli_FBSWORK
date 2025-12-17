n = 5   # height of upper half

# upper part
for i in range(n):
    print(" " * (n - i) + "*", end="")
    if i != 0:
        print(" " * (2 * i - 1) + "*")
    else:
        print()

# middle part
for i in range(n - 2, -1, -1):
    print(" " * (n - i) + "*", end="")
    if i != 0:
        print(" " * (2 * i - 1) + "*")
    else:
        print()
