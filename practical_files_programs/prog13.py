a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
c = float(input("Enter the value of c : "))
S = (a + b + c) / 2
area = (S * (S - a) * (S - b) * (S - c)) ** (1 / 2)
print(f"Area of Triangle is {area:.2f}")
