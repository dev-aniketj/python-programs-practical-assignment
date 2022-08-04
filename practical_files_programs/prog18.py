a = int(input("Enter the first value : "))
b = int(input("Enter the second value : "))

small = a if a < b else b
gcd = 0

for i in range(1, small + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print(f"The GCD of {a} and {b} is {gcd}.")
