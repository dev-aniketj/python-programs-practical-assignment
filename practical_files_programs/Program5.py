a = int(input("Enter the first number(int) : "))
b = int(input("Enter the second number(int) : "))
c = float(input("Enter the third number(float) : "))
d = float(input("Enter the fourth number(float) : "))

# int and int
print("Int to Int")
print(a + b)
print(a - b)
print(a * b)
print("{:.2f}".format(a / b))
print(a // b)
print(a % b)

# float and float
print("Float to Float")
print(c + d)
print(c - d)
print(c * d)
print("{:.2f}".format(c / d))
print(c // d)
print(c % d)

# float and int
print("Float to Int")
print(c + a)
print(c - a)
print(c * a)
print("{:.2f}".format(c / a))
print(c // a)
print(c % a)
