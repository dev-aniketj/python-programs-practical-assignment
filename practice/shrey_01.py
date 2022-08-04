num = int(input("Enter the number : "))
flag = True

for i in range(2, num - 1):
    if (num % i == 0):
        flag = False
        break

print("Prime") if (flag) else print("Not Prime")
