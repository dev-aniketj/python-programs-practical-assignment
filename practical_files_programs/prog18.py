a = int(input("Enter the first value : "))
b = int(input("Enter the second value : "))

small = b if a > b else a
gcd = 0

for i in range(1, b + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print(f"The GCD of {a} and {b} is {gcd}")
