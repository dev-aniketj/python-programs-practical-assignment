a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))
if a > b > c:
    print(f"{a} is greater than {b, c}")
elif b > c:
    print(f"{b} is greater than {a, c}")
else:
    print(f"{c} is greater than {a, b}")
