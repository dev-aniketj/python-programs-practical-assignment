n = int(input("Enter the height of the pattern : "))
for i in range(1, n + 1):
    for j in range(1, n * 2):
        if i == 1 or i == j or i + j == n * 2:
            print("* ", end='')
        else:
            print("  ", end='')
    print()
