x1 = float(input("Enter the x1 coordinate : "))
y1 = float(input("Enter the y1 coordinate : "))
x2 = float(input("Enter the x2 coordinate : "))
y2 = float(input("Enter the y2 coordinate : "))
distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1 / 2)
print(f"Distance between two points is {distance:.2f}")
