a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

# using elif (using if, elif, else)
if a > b and a > c:
    print(a, "is greater.")
elif b > c:
    print(b, "is greater.")
else:
    print(c, "is greater.")

# using nested if/else - without using elif
if a > b:
    if a > c:
        print(a, "is greater.")
    else:
        print(c, "is greater.")
else:
    if b > c:
        print(b, "is greater.")
    else:
        print(c, "is greater.")
