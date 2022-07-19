radius, side = input("Enter the radius & side : ").split()
radius = int(radius)  # convert str to int
side = int(side)  # convert str to int

# print("Area of Circle : ", round((2 * 3.14 * radius), 2))
print("Area of Circle : {:.2f}".format(3.14 * radius* radius))
print("Area of Square :", side * side)
