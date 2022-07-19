def check_number(n):
    if n > 1:
        flag = True
        if n == 2:
            return flag
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
                else:
                    flag = True
        return flag


prime_count, composite_count = 0, 0
N = int(input("Enter number : "))
while N != -1:
    if check_number(N):
        prime_count += 1
    else:
        composite_count += 1
    N = int(input("Enter number : "))

print(f"The total prime numbers are {prime_count} and composite numbers are {composite_count}")
