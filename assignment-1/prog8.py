import math

print("Enter the sides of the triangle : ")
a = int(input("Enter the a : "))
b = int(input("Enter the b : "))
c = int(input("Enter the c : "))
S = float(a + b + c) / 2
# area = (S * (S - a) * (S - b) * (S - c)) ** (1 / 2)
area = math.sqrt(S * (S - a) * (S - b) * (S - c))
print("Area of Triangle :", area)
