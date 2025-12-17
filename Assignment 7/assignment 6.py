n = 5

for i in range(1, n + 1):
    if (i == 1 or j!=5):
        for j in range(1, n + 1):
            print(j, end=" ")
        print()
    else:
        print(i, end=" ")
        print("  " * (n - i -1  ), end="")
        print(n)
    