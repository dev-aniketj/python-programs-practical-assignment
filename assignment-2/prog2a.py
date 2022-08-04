n = int(input("Enter the height of pattern : "))
for i in range(1, n + 1):
    for j in range(1, n * 2):
        if i + j == n + 1 or i == n or j - i == n - 1:
            print("* ", end='')
        else:
            print("  ", end='')
    print()

