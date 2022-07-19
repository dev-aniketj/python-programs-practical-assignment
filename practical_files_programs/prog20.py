n = int(input("Enter the value of N : "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"The factorial of {n} is {fact}")
